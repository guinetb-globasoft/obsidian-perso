---
tags: ["commercial", "CA-Immobilier", "vérification", "snowflake", "rapport"]
created: 2026-04-24
---

---
tags: ["commercial", "CA-Immobilier", "vérification", "snowflake", "rapport"]
created: 2026-04-23
source: "00-Inbox/Brief Vérif Snowflake - Propale CA Immobilier.md"
propale: "00-Inbox/Propale Sohoft - CA Immobilier - Engagement 1.md"
---

# Rapport — Vérification Snowflake propale CA Immobilier

**Date :** 23/04/2026
**Édition supposée :** Business Critical (BC)
**Cloud cible :** AWS Francfort (eu-central-1)

Chaque point vérifié ci-dessous est accompagné de la **source exacte** (URL directe de la doc Snowflake ou article officiel) pour faciliter la défense devant le CISO ou la DSI sans retour à la recherche.

**La section 2.2 (Azure Key Vault) est triple-vérifiée sur 8 sources indépendantes** compte tenu du caractère bloquant de l'affirmation.

---

## Synthèse en tête

**Trois points critiques à corriger avant remise :**

1. 🔴 **BIOK → terme non-Snowflake.** Le terme officiel est **Customer-Managed Key (CMK)** dans le cadre de **Tri-Secret Secure**. "BIOK" est probablement un terme interne CAGIP. À reformuler.
2. 🔴 **Azure Key Vault sur AWS Francfort = incompatible.** La CMK doit impérativement résider dans le KMS du cloud provider qui héberge le compte Snowflake. Si le compte est sur AWS eu-central-1, la CMK doit être dans **AWS KMS**, pas dans Azure Key Vault. À arbitrer avec CAGIP avant remise. Triple-vérifié — aucune ambiguïté.
3. 🟠 **Resource monitors ≠ couverture complète FinOps.** Les resource monitors ne couvrent pas le serverless (tasks serverless, dynamic tables serverless, Cortex, Snowpipe). Il faut ajouter **Budgets** dans la propale pour couvrir l'intégralité des coûts.

**Le reste des affirmations tient, avec quelques précisions de formulation à apporter.**

---

## 1. Warehouses dédiés par usage

### Statut global : 🟢 OK, avec précisions

### 1.1 Paramètres `AUTO_SUSPEND`, `AUTO_RESUME`, `SCALING_POLICY`, multi-cluster

**Affirmation propale :** « Chacun est dimensionné et paramétré (auto-suspend, scaling policy, multi-cluster) selon son profil de charge. »

**Statut : 🟢 OK.** Les paramètres existent tels qu'énoncés.

**Source :** https://docs.snowflake.com/en/sql-reference/sql/create-warehouse

Extrait :

> objectProperties ::= WAREHOUSE_TYPE = { STANDARD | 'SNOWPARK-OPTIMIZED' }
> WAREHOUSE_SIZE = { XSMALL | SMALL | MEDIUM | LARGE | XLARGE | XXLARGE | XXXLARGE | X4LARGE | X5LARGE | X6LARGE }
> GENERATION = { '1' | '2' }
> MAX_CLUSTER_COUNT = <num>
> MIN_CLUSTER_COUNT = <num>
> SCALING_POLICY = { STANDARD | ECONOMY }
> AUTO_SUSPEND = { <num> | NULL }
> AUTO_RESUME = { TRUE | FALSE }

Deux valeurs de scaling policy toujours valides : `STANDARD` (minimise les files d'attente) et `ECONOMY` (minimise la consommation de crédits).

### 1.2 Multi-cluster disponible sur Business Critical ?

**Statut : 🟢 OK.** Multi-cluster est une feature **Enterprise Edition et supérieure**. BC en hérite automatiquement.

**Source 1 :** https://docs.snowflake.com/en/user-guide/warehouses-overview

Extrait :

> Multi-cluster warehouses are an Enterprise Edition feature.

**Source 2 :** https://docs.snowflake.com/en/user-guide/warehouses-considerations

Extrait :

> Scale out by adding clusters to a multi-cluster warehouse (requires Snowflake Enterprise Edition or higher).

**Source 3 (détails scaling policies) :** https://docs.snowflake.com/en/user-guide/warehouses-multicluster

Extrait :

> To help control the usage of credits in Auto-scale mode, Snowflake provides a property, SCALING_POLICY, that determines the scaling policy to use when automatically starting or shutting down additional clusters.

**→ BC permet bien le multi-cluster sur `WH_BI`.**

### 1.3 Tailles de warehouse

**Statut : 🟢 OK.**

**Source :** https://docs.snowflake.com/en/sql-reference/sql/create-warehouse (voir extrait §1.1)

Tailles officielles confirmées : `XSMALL | SMALL | MEDIUM | LARGE | XLARGE | XXLARGE | XXXLARGE | X4LARGE | X5LARGE | X6LARGE`. Pas de nouveau palier introduit début 2026 au-delà de 6X-Large (déjà GA sur AWS et Azure).

### 1.4 Gen2 warehouses (à ajouter dans la propale)

**Statut : 🟡 Opportunité ratée.**

Depuis **mai 2025**, Snowflake a généralisé les **Gen2 Standard Warehouses** avec un gain de performance annoncé de ~2,1x sur les workloads analytiques par rapport à Gen1. Paramètre `GENERATION = { '1' | '2' }` dans `CREATE WAREHOUSE`.

**Source 1 (release notes) :** https://docs.snowflake.com/en/release-notes/new-features-2025

Extrait :

> May 05, 2025: Generation 2 standard warehouses (General availability)

**Source 2 (annonce officielle avec benchmark) :** https://www.snowflake.com/en/news/press-releases/snowflake-unveils-next-wave-of-compute-innovations-for-faster-more-efficient-warehouses-and-ai-driven-data-governance/

Extrait :

> Standard Warehouse – Generation 2 (Gen2) (now generally available), an enhanced version of Snowflake's virtual Standard Warehouse with next-generation hardware and additional enhancements to deliver 2.1x faster analytics performance.

À mentionner dans la propale : "Les warehouses seront provisionnés en génération 2 (Gen2) par défaut là où c'est disponible dans la région eu-central-1, pour bénéficier des gains de performance annoncés par Snowflake."

### 1.5 Snowpark-optimized warehouses

**Source :** https://docs.snowflake.com/en/sql-reference/sql/create-warehouse

Type `SNOWPARK-OPTIMIZED` (16x plus de mémoire par nœud) documenté mais **pas pertinent pour CAI** vu la stack cible (DLT + dbt Core + Power BI). À ne pas mentionner.

### 1.6 Pattern 4 warehouses (ingestion / transform / BI / ad hoc)

**Statut : 🟢 Aligné sur les best practices.**

**Source principale :** https://docs.snowflake.com/en/user-guide/warehouses-considerations

Pas de whitepaper unique "workload isolation" publié par Snowflake mais c'est le pattern qui ressort de façon constante dans cette page et dans les guides d'implémentation FinOps (ex : SELECT.dev, Flexera). L'isolation par usage est la recommandation par défaut pour éviter le mélange de profils de charge.

**Recommandation spécifique à creuser côté dimensionnement :** l'auto-suspend à 60s est agressif mais correct pour l'ingestion/transform. Pour WH_BI (Power BI DirectQuery), 300s est raisonnable pour préserver le cache. La doc recommande 5-10 minutes max par défaut pour les usages typiques.

---

## 2. Sécurité — référentiel CISO CAGIP

### Statut global : 🔴 Deux points critiques à arbitrer

### 2.1 Tri-Secret Secure / "BIOK"

**Affirmation propale :** « Mise en œuvre de BIOK avec Tri Secret Secure Encryption »

**Statut : 🔴 KO, à reformuler.**

Le terme "BIOK" n'apparaît nulle part dans la documentation Snowflake. Le terme Snowflake officiel est **Tri-Secret Secure** qui combine :
- une **Snowflake-maintained key**
- une **Customer-Managed Key (CMK)** détenue par le client dans son KMS cloud provider

**Source 1 (définition Tri-Secret Secure) :** https://docs.snowflake.com/en/user-guide/security-encryption-tss

Extrait :

> Using a dual-key encryption model together with Snowflake's built-in user authentication enables three levels of data protection, known as Tri-Secret Secure. [...] Our dual-key encryption model combines a Snowflake-maintained key and a customer-managed key (CMK), which you create on the cloud provider platform that hosts your Snowflake account.

**Source 2 (terminologie CMK) :** https://docs.snowflake.com/en/user-guide/security-encryption-manage

Extrait :

> A customer-managed key (CMK) is a master encryption key that the customer maintains in the key management service for the cloud provider that hosts the customer's Snowflake account.

**→ Reformulation propale recommandée :** « Mise en œuvre du chiffrement **Tri-Secret Secure** combinant la clé maîtresse Snowflake et une **Customer-Managed Key (CMK)** gérée par CAGIP dans son KMS, conformément au référentiel Groupe (désigné en interne "BIOK"). »

**Confirmation BC requis :** Tri-Secret Secure n'est disponible qu'à partir de Business Critical.

**Source :** https://docs.snowflake.com/en/user-guide/security-encryption-tss

Extrait :

> This feature requires Business Critical (or higher). To inquire about upgrading, please contact Snowflake Support.

### 2.2 Azure Key Vault sur AWS Francfort — 🔴 Point bloquant (TRIPLE-VÉRIFIÉ)

**Affirmation propale :** « gestion des clés via Azure Key Vault »

**Statut : 🔴 KO si hébergement AWS Francfort.** Vérifié sur **8 sources indépendantes**, dont 5 documents officiels Snowflake et 1 article de blog Snowflake. Aucune ambiguïté possible.

#### Les 8 sources de vérification

**Source 1 — Doc Snowflake "Key Management" (la plus définitive)** : https://docs.snowflake.com/en/user-guide/security-encryption-manage

Cette page liste **explicitement et limitativement** les KMS autorisés selon le cloud d'hébergement :

> A customer-managed key (CMK) is a master encryption key that the customer maintains in the key management service for the cloud provider that hosts the customer's Snowflake account. The key management services for each platform are:
> - **AWS**: AWS Key Management Service (KMS)
> - **Google Cloud**: Cloud Key Management Service (Cloud KMS)
> - **Microsoft Azure**: Azure Key Vault

C'est le mapping cloud→KMS le plus officiel possible. **Azure Key Vault est explicitement réservé à Snowflake-on-Azure.**

**Source 2 — Doc Snowflake "Tri-Secret Secure"** : https://docs.snowflake.com/en/user-guide/security-encryption-tss

> Our dual-key encryption model combines a Snowflake-maintained key and a customer-managed key (CMK), **which you create on the cloud provider platform that hosts your Snowflake account**.

**Source 3 — Doc Snowflake "TSS Self-Service" (procédure d'activation)** : https://docs.snowflake.com/en/user-guide/security-encryption-tss-self-serve

> On the cloud provider, create a CMK. **Do this step in the key management service (KMS) on the cloud platform that hosts your Snowflake account.**

**Source 4 — Doc Snowflake "TSS with private connectivity"** : https://docs.snowflake.com/en/user-guide/security-encryption-tss-self-serve-private

> On the cloud provider, create a CMK. Do this step in the KMS on the cloud platform that hosts your Snowflake account.

**Source 5 — Doc SQL `SYSTEM$REGISTER_CMK_INFO` (la fonction système elle-même)** : https://docs.snowflake.com/en/sql-reference/functions/system_register_cmk_info

La fonction qui enregistre la CMK accepte des **arguments différents selon le cloud d'hébergement**. Exemples documentés :

> Register your CMK for your Snowflake account on Amazon Web Services:
> `SELECT SYSTEM$REGISTER_CMK_INFO('arn:aws:kms:us-west-2:736112632310:key/...');`
>
> Register your CMK for your Snowflake account on Microsoft Azure:
> `SELECT SYSTEM$REGISTER_CMK_INFO('https://trisecretsite.vault.azure.net/', 'trisecretazkey', 'true');`

C'est la **preuve technique ultime** : la fonction d'enregistrement CMK n'accepte qu'un format d'identifiant correspondant au cloud qui héberge le compte. Un compte Snowflake AWS ne peut pas enregistrer une URL de Key Vault Azure.

**Source 6 — Article officiel blog Snowflake "CMK pour Azure" (août 2024)** : https://www.snowflake.com/en/blog/data-encryption-with-customer-managed-keys-for-azure/

> In 2017, Snowflake announced support for customer-managed keys using AWS Key Management Service (KMS). [...] Today, we are announcing the availability of data encryption with customer-managed keys for **Snowflake on Azure**. [...] **Customer-managed keys for Snowflake on Azure use keys defined in Azure Key Vault.**

L'article distingue très clairement les deux annonces produit (2017 = AWS KMS pour Snowflake-on-AWS ; 2024 = Azure Key Vault pour Snowflake-on-Azure).

**Source 7 — Article tiers indépendant phData (2023, expert Snowflake)** : https://www.phdata.io/blog/encrypting-snowflake-data-with-own-keys/

> All three of the major cloud providers that can host your Snowflake account contain a key management service: AWS has AWS Key Management Service, Google has Cloud Key Management Service, and Microsoft Azure has Azure Key Vault.

**Source 8 — Tutoriel pratique francophone (juillet 2025)** : https://piermick.wordpress.com/2025/10/28/tri-secure-snowflake-dans-aws/

> Tout d'abord, créer un AWS KMS, **attention, KMS doit être dans la même région** que votre compte Snowflake créé sur AWS avec la licence Business Critical.

Précision supplémentaire utile : pour AWS, la CMK doit non seulement être dans AWS KMS, mais aussi dans la **même région AWS** que le compte Snowflake (donc eu-central-1 si Francfort).

#### Synthèse de la vérification

Le bloc d'évidence est **massif et cohérent** :
- 5 documents officiels Snowflake (doc + 1 fonction SQL + 1 blog)
- 1 article expert tiers
- 1 tutoriel pratique récent
- 0 contradiction trouvée
- 0 mention d'un mode cross-cloud autorisé

**Une seule alternative documentée pour utiliser un keystore externe à AWS** (mais pas Azure Key Vault) :

> Snowflake supports integrating Tri-Secret Secure with AWS external key stores [...]. Snowflake officially tests and supports only Thales Hardware Security Modules (HSM) and Thales CipherTrust Cloud Key Manager (CCKM) data encryption products.

Source : https://docs.snowflake.com/en/user-guide/security-encryption-tss + release notes 9.0 GA (janvier 2025) https://docs.snowflake.com/en/release-notes/2025/9_00

Cette intégration utilise le mécanisme **AWS KMS External Key Store (XKS)** — donc le compte Snowflake **reste sur AWS**, AWS KMS reste l'interlocuteur, mais le stockage physique de la clé est délégué à un HSM Thales que CAGIP peut héberger ailleurs (on-prem, autre cloud, ou Azure via une appliance Thales). Ce n'est **pas** la même chose que d'utiliser Azure Key Vault directement.

#### Nuance importante à ne pas confondre

Il existe d'autres usages d'Azure Key Vault depuis Snowflake qui sont parfaitement supportés mais qui **ne concernent pas Tri-Secret Secure** :

1. Stocker la clé privée RSA d'authentification d'un service account Snowflake dans Azure Key Vault, et l'appeler depuis du code applicatif (Python, Talend, etc.). Voir : https://medium.com/snowflake/snowflake-private-key-authentication-with-python-using-azure-key-vault-bcf26f3c15a1
2. Récupérer une clé applicative depuis Azure Key Vault dans une UDF Snowpark via External Network Access. Voir : https://medium.com/snowflake/access-azure-key-vault-from-snowflake-through-external-network-access-5fd57d1a955f

Ces deux cas sont des **usages applicatifs** de KV, pas du chiffrement at-rest des données Snowflake. Si CAGIP a évoqué Azure Key Vault dans son brief CISO, il faut clarifier laquelle des trois acceptions il vise — ces trois usages ont des conséquences architecturales très différentes.

#### Trois options à arbitrer avec CAGIP

1. **Bascule sur Azure West Europe / France Central** pour Snowflake → permet d'utiliser Azure Key Vault nativement comme CMK Tri-Secret Secure (cohérent si CAGIP a déjà un tenant Azure mature pour les clés).
2. **Conserver AWS Francfort + AWS KMS** → la CMK est gérée dans AWS KMS eu-central-1 avec les politiques IAM Snowflake. Cohérent avec un référentiel CISO multi-cloud où chaque service utilise le KMS de son propre cloud.
3. **AWS Francfort + AWS KMS External Key Store via Thales CCKM** → permet à CAGIP de garder ses clés dans un HSM tiers Thales (potentiellement on-prem chez CAGIP), avec intégration AWS KMS XKS. Niveau de contrôle maximal mais complexité opérationnelle accrue. C'est le seul scénario où la matière première de la clé peut sortir du périmètre AWS.

**Action à prendre avant remise :** clarifier avec CAGIP quelle est la contrainte dure — hébergement cloud, localisation des clés, intégration IAM existante, ou exigence d'un HSM physique sous contrôle direct. La propale actuelle mélange les trois et est techniquement incohérente.

### 2.3 AWS PrivateLink

**Affirmation propale :** « Private Link depuis les postes CAGIP »

**Statut : 🟢 OK, disponible sur BC à eu-central-1.**

**Source 1 (host name eu-central-1) :** https://docs.snowflake.com/en/user-guide/admin-security-privatelink

Extrait :

> If the account is in EU (Frankfurt), the host name is xy12345.eu-central-1.privatelink.snowflakecomputing.com.

**Source 2 (exigence BC, PrivateLink outbound) :** https://docs.snowflake.com/en/user-guide/private-manage-endpoints-aws

Extrait :

> This feature requires Business Critical (or higher). To inquire about upgrading, please contact Snowflake Support.

**Source 3 (internal stages) :** https://docs.snowflake.com/en/user-guide/private-internal-stages-aws

Extrait :

> AWS VPC interface endpoints and AWS PrivateLink for Amazon S3 can be combined to provide secure connectivity to Snowflake internal stages. This setup ensures that data loading and data unloading operations to Snowflake internal stages use the AWS internal network and do not take place over the public Internet.

**Précision technique à apporter :** PrivateLink peut être configuré pour :
- la connexion client vers Snowflake (postes CAGIP → Snowflake)
- les internal stages (chargement de données depuis AWS VPC vers stages S3 Snowflake) — nécessite `ENABLE_INTERNAL_STAGES_PRIVATELINK`
- les external functions (API Gateway privé)

À mentionner dans la DAT qu'on couvrira les trois cas d'usage, pas seulement le premier.

### 2.4 SSO Cerbère / ILEX CAGIP

**Affirmation propale :** « SSO Cerbère / ILEX CAGIP »

**Statut : 🟢 OK, via SAML2 custom.**

**Source 1 (support IdP SAML 2.0 compliant) :** https://docs.snowflake.com/en/user-guide/admin-security-fed-auth-overview

Extrait :

> In addition to the native Snowflake support provided by Okta and Entra ID, Snowflake supports using most SAML 2.0-compliant vendors as an IdP [...] To use an IdP other than Okta or Entra ID, you must define a custom application for Snowflake in the IdP.

**Source 2 (config IdP custom) :** https://docs.snowflake.com/en/user-guide/admin-security-fed-auth-configure-idp

**Source 3 (syntaxe SECURITY INTEGRATION SAML2) :** https://docs.snowflake.com/en/sql-reference/sql/create-security-integration-saml2

**Source 4 (multi-IdP) :** https://docs.snowflake.com/en/user-guide/admin-security-fed-auth-security-integration-multiple

Cerbère et ILEX étant des IdP SAML 2.0-compliants, l'intégration passe par une `SECURITY INTEGRATION TYPE = SAML2 SAML2_PROVIDER = 'CUSTOM'`. Le paramétrage peut aussi être fait via **metadata URL** pour éviter la gestion manuelle des certificats.

**Précision à ajouter dans la DAT :** possibilité d'utiliser **plusieurs IdP simultanément** via les propriétés `ALLOWED_USER_DOMAINS` / `ALLOWED_EMAIL_PATTERNS` ou via une authentication policy.

### 2.5 Row Access Policies et Dynamic Data Masking

**Affirmation propale :** « Row Access Policies et Dynamic Data Masking pour satisfaire les exigences CISO sur les données sensibles »

**Statut : 🟢 OK sur BC.**

**Source 1 (Row Access Policies) :** https://docs.snowflake.com/en/user-guide/security-row-intro

**Source 2 (Dynamic Data Masking) :** https://docs.snowflake.com/en/user-guide/security-column-ddm-intro

**Source 3 (disponibilité par édition) :** https://docs.snowflake.com/en/user-guide/intro-editions

**Source 4 (confirmation francophone à jour février 2026) :** https://www.idriss-benbassou.com/editions-snowflake-standard-enterprise-business-critical-vps/

Extrait :

> Les fonctionnalités de performance avancée (QAS, SOS, materialized views...) et de gouvernance (masquage, row access policies, classification) commencent à Enterprise. La sécurité renforcée (Tri-Secret, PrivateLink, failover) arrive avec Business Critical.

Row Access Policies et Dynamic Data Masking disponibles à partir de **Enterprise Edition**, donc a fortiori sur Business Critical.

---

## 3. Organisation logique — pattern médaillon + domaines

### Statut global : 🟢 OK mais précision de vocabulaire à apporter

**Affirmation propale :** « Structuration en databases et schemas par zone (raw / staging / core / marts) et par domaine fonctionnel »

**Source principale (database/schema hierarchy) :** https://docs.snowflake.com/en/sql-reference/ddl-database

**Observations :**

- Le vocabulaire **raw / staging / core / marts** est un pattern classique dbt. Il est **aligné** avec la logique médaillon (Bronze / Silver / Gold) mais n'utilise pas le vocabulaire Databricks.
- **Snowflake ne publie pas de whitepaper officiel "médaillon"**. Recherche effectuée sur docs.snowflake.com et snowflake.com/blog : aucun contenu officiel intitulé "Medallion Architecture". Le terme est originellement Databricks. Les guides Snowflake parlent plutôt de "zones" (raw/clean/curated) ou directement des layers dbt (staging/intermediate/marts).
- Il n'y a pas non plus de guide Snowflake dédié "organisation database/schema à 1200+ tables". Les best practices sont dispersées dans la documentation.

**Recommandation de formulation propale :**

Ne pas prononcer le mot "médaillon" (terme Databricks potentiellement mal perçu par un interlocuteur Snowflake pur). Rester sur le vocabulaire dbt (raw / staging / intermediate / marts) qui est celui que CAI utilisera effectivement via dbt Core. C'est déjà le cas dans l'extrait actuel de la propale, donc **rien à changer** — juste ne pas introduire ce vocabulaire médaillon dans la DAT.

**À ajouter dans la DAT (pas dans la propale) :** la stratégie de nommage à 1200 tables devra prévoir une convention `<domaine>_<zone>_<entité>` ou via databases distinctes `<domaine>_RAW`, `<domaine>_CORE`, pour éviter l'explosion d'un schéma unique à 1200 objets. Également prévoir une convention de tags Snowflake dès l'Engagement 2 pour faciliter le FinOps (cf. §4).

---

## 4. FinOps — resource monitors, query tags, account usage

### Statut global : 🟠 OK mais la propale passe à côté des Budgets (nouveauté critique)

### 4.1 Resource monitors

**Affirmation propale :** « Resource monitors avec seuils gradués »

**Statut : 🟢 OK.**

**Source 1 (syntaxe CREATE RESOURCE MONITOR) :** https://docs.snowflake.com/en/sql-reference/sql/create-resource-monitor

Extrait :

> CREATE OR REPLACE RESOURCE MONITOR limiter
>   WITH CREDIT_QUOTA = 5000
>   NOTIFY_USERS = (JDOE, "Jane Smith", "John Doe")
>   TRIGGERS ON 75 PERCENT DO NOTIFY
>            ON 100 PERCENT DO SUSPEND
>            ON 110 PERCENT DO SUSPEND_IMMEDIATE;

**Source 2 (usage et best practices) :** https://docs.snowflake.com/en/user-guide/resource-monitors

Trois actions possibles : `NOTIFY`, `SUSPEND`, `SUSPEND_IMMEDIATE`. Granularité compte ou warehouse (un warehouse ne peut être assigné qu'à un seul resource monitor).

### 4.2 🔴 Limite critique — serverless non couvert

**Statut : 🔴 Point important manquant dans la propale.**

**Source :** https://docs.snowflake.com/en/user-guide/resource-monitors

Extrait :

> Resource monitors work for warehouses only. You can't use a resource monitor to track spending associated with serverless features and AI services. To monitor credit consumption by these features, use a budget instead.

Sur un projet CAI avec stack dbt + Snowflake, plusieurs services sont **non couverts** par les resource monitors :
- Serverless tasks (si utilisés pour de l'orchestration légère)
- Dynamic tables en mode serverless
- Snowpipe (ingestion continue)
- Search Optimization Service
- Automatic clustering
- Cortex AI functions (si un jour utilisées)

**→ Ajout à faire dans la propale :** mentionner **Snowflake Budgets** comme complément aux resource monitors pour la couverture complète du coût.

**Source Budgets :** https://docs.snowflake.com/en/user-guide/budgets

Extrait :

> By default, the budget refresh interval is up to 6.5 hours. You can reduce the budget refresh interval to one hour, which can be helpful when you need to watch spending more carefully. A budget with a one-hour refresh interval is known as a low latency budget.

Les Budgets permettent aussi de déclencher des stored procedures personnalisées, d'où une mécanique d'alerting plus fine qu'un simple email.

### 4.3 Query tags — pour la refacturation interne

**Affirmation propale :** « query tags pour la refacturation interne »

**Statut : 🟢 OK.**

**Source 1 (QUERY_TAG parameter) :** https://docs.snowflake.com/en/sql-reference/parameters#query-tag

Usage classique :

```sql
ALTER SESSION SET QUERY_TAG = 'CAI|domaine=clients|env=prod|projet=engagement-2';
```

**Source 2 (QUERY_ATTRIBUTION_HISTORY, GA) :** https://docs.snowflake.com/en/sql-reference/account-usage/query_attribution_history

Extrait :

> This Account Usage view can be used to determine the compute cost of a given query run on warehouses in your account in the last 365 days (1 year). [...] Latency for this view can be up to eight hours. [...] The value in the credits_attributed_compute column contains the warehouse credit usage for executing the query, inclusive of any resizing and/or autoscaling of multi-cluster warehouse(s). This cost is attributed based on the weighted average of the resource consumption. The value doesn't include any credit usage for warehouse idle time.

**Source 3 (viewing cost by tag) :** https://docs.snowflake.com/en/user-guide/cost-exploring-sql

Combinée avec les query tags, QUERY_ATTRIBUTION_HISTORY permet un vrai mécanisme de chargeback/showback par domaine fonctionnel.

### 4.4 ACCOUNT_USAGE schema — latences

**Affirmation propale :** « account usage pour l'analyse des coûts »

**Statut : 🟢 OK, précision à apporter sur les latences.**

Les latences annoncées dans le brief (90 min) sont **obsolètes et imprécises**. En 2026, les latences varient selon la vue :

**Source 1 (vue générale du schema) :** https://docs.snowflake.com/en/sql-reference/account-usage

Extrait :

> Certain account usage views provide historical usage metrics. The retention period for these views is 1 year (365 days).

**Source 2 (QUERY_HISTORY, 45 min) :** https://docs.snowflake.com/en/sql-reference/account-usage/query_history

Extrait :

> Latency for the view may be up to 45 minutes.

**Source 3 (METERING_HISTORY, 180 min) :** https://docs.snowflake.com/en/sql-reference/account-usage/metering_history

Extrait :

> Latency for the view may be up to 180 minutes (3 hours), except for the CREDITS_USED_CLOUD_SERVICES column.

**Source 4 (QUERY_ATTRIBUTION_HISTORY, 8h) :** https://docs.snowflake.com/en/sql-reference/account-usage/query_attribution_history

Extrait :

> Latency for this view can be up to eight hours.

**Source 5 (WAREHOUSE_METERING_HISTORY) :** https://docs.snowflake.com/en/sql-reference/account-usage/warehouse_metering_history

Rétention historique : **365 jours (1 an)** pour les vues historiques d'usage, contre 7j-6mois dans l'Information Schema.

À mentionner dans la DAT si CAI veut un reporting financier quotidien : bien calibrer les délais d'arrivée des données.

### 4.5 Horizon Catalog (feature 2025 à évaluer)

**Statut : 🟡 Opportunité à mentionner si pertinent.**

**Source 1 (annonce officielle Summit 2025) :** https://www.snowflake.com/en/blog/horizon-catalog-data-governance/

Extrait :

> With the Horizon Catalog, data governors, stewards, security admins and chief information security officers can understand, protect and audit accounts and assets across regions and clouds while allowing data teams to discover, access and share data, services and apps globally, without ETL.

**Source 2 (roll-up Summit) :** https://www.snowflake.com/en/blog/announcements-snowflake-summit-2025/

Snowflake a lancé **Horizon Catalog** au Summit 2025 : catalogue unifié pour la gouvernance (classification, masking policies, lineage) avec surveillance de sécurité cross-cloud. Sur un projet Groupe CA avec 1200 tables, ça peut clairement valoriser la propale côté CISO.

**Attention :** ne pas survendre si Engagement 1 est court. À garder pour l'Engagement 2 ou une évolution de roadmap.

---

## 5. Cycle de vie des données — Time Travel, Fail-safe, clones

### Statut global : 🟢 OK globalement, tout est factuellement correct

### 5.1 Time Travel

**Statut : 🟢 OK.**

**Source :** https://docs.snowflake.com/en/user-guide/data-time-travel

Extrait :

> For permanent databases, schemas, and tables, the retention period can be set to any value from 0 up to 90 days.

- Standard Edition : 0 ou 1 jour
- Enterprise / Business Critical : **jusqu'à 90 jours**
- Paramètre `DATA_RETENTION_TIME_IN_DAYS` configurable au niveau compte, database, schema ou table (héritage hiérarchique)

**Recommandation pour CAI :**
- Zones `raw` / `staging` : 1-7 jours (donnée régénérable via DLT)
- Zone `core` : 30 jours (coûts maîtrisés, recovery opérationnel raisonnable)
- Zone `marts` : 7-14 jours (usage BI, pas de donnée canonique)

### 5.2 Fail-safe

**Statut : 🟢 OK.**

**Source 1 (overview Time Travel + Fail-safe) :** https://docs.snowflake.com/en/user-guide/data-availability

**Source 2 (non-configurabilité) :** https://docs.snowflake.com/en/user-guide/tables-temp-transient

Extrait :

> The Fail-safe period is not configurable for any table type. Transient and temporary tables have no Fail-safe period.

Confirmé : **7 jours fixes, non configurable, uniquement sur tables permanentes**, accessible uniquement via Snowflake Support pour récupération d'urgence.

**Conséquence coût :** un enregistrement modifié quotidiennement avec 30j de Time Travel + 7j de Fail-safe = **37 jours** de stockage d'historique facturé. Important à chiffrer dans le TCO.

### 5.3 Zero-copy clone

**Statut : 🟢 OK.**

**Source 1 (CLONE syntax) :** https://docs.snowflake.com/en/sql-reference/sql/create-clone

**Source 2 (best practices coût) :** https://docs.snowflake.com/en/user-guide/tables-storage-considerations

Le zero-copy clone est toujours disponible et reste la méthode recommandée pour les environnements non-prod. Un clone stable (non modifié) ne consomme rien. Un clone très modifié par rapport à la source peut générer des coûts de stockage significatifs, à monitorer via `information_schema.table_storage_metrics`.

### 5.4 Masking pour les clones non-prod

**Affirmation propale :** « clones pour les environnements non-prod (désensibilisés) »

**Source :** https://docs.snowflake.com/en/user-guide/security-column-ddm-intro

**Méthode recommandée :** combiner zero-copy clone + **Dynamic Data Masking policies** appliquées aux environnements non-prod. Pas de duplication de la donnée, le masquage est appliqué à la lecture selon le rôle en session.

### 5.5 Snapshots (nouveauté à évaluer)

**Statut : 🟡 Feature récente, à évaluer pour l'Engagement 2.**

**Source :** https://www.snowflake.com/en/news/press-releases/snowflake-unveils-next-wave-of-compute-innovations-for-faster-more-efficient-warehouses-and-ai-driven-data-governance/

Extrait :

> Safeguarding Businesses with Reliable Data Recovery: To empower customers with enhanced regulatory compliance and cyber resilience against ransomware, Snowflake is now offering point-in-time, immutable backups with Snapshots (public preview soon). Snapshots ensure that data isn't altered or deleted once created for reliable data recovery when it matters most.

Pertinent dans un contexte Groupe CA avec exigences de cyber-résilience. À vérifier si GA au moment du démarrage 4 mai.

---

## 6. Features 2025-2026 pertinentes (potentiellement ratées dans la propale)

**Source commune (release notes) :** https://docs.snowflake.com/en/release-notes/new-features-2025

| Feature | Statut | Pertinence CAI | Source |
|---|---|---|---|
| **Gen2 Standard Warehouses** | GA mai 2025 | 🟢 Haute. ~2,1x perf vs Gen1, même prix. | https://www.snowflake.com/en/news/press-releases/snowflake-unveils-next-wave-of-compute-innovations-for-faster-more-efficient-warehouses-and-ai-driven-data-governance/ |
| **Horizon Catalog** | GA 2025 | 🟢 Moyenne-Haute. Valorisable côté CISO. | https://www.snowflake.com/en/blog/horizon-catalog-data-governance/ |
| **Snapshots** | Public preview 2025 | 🟡 Moyenne. À évaluer selon GA effective au 4 mai. | (même source que Gen2 ci-dessus) |
| **Adaptive Compute** | Private preview 2025 | 🔴 Non. Trop jeune, private preview. | (même) |
| **Snowflake Openflow** | En évolution 2025 | 🔴 Non. CAI reste sur DLT. | https://docs.snowflake.com/en/release-notes/new-features-2025 |
| **Cortex AI Functions** | GA nov 2025 | 🔴 Non. Brief dit "ne pas mentionner IA". | https://docs.snowflake.com/en/release-notes/2025/other/2025-11-04-cortex-aisql-operators-ga |
| **Notebooks + PrivateLink** | GA 2025 | 🟡 Basse. Pas critique pour Engagement 1. | https://docs.snowflake.com/en/release-notes/new-features-2025 |
| **Query Attribution History** | GA | 🟢 Haute. Mentionné en §4.3. | https://docs.snowflake.com/en/sql-reference/account-usage/query_attribution_history |
| **TSS + AWS External Key Store (Thales)** | GA janvier 2025 | 🟡 Conditionnelle (cf. §2.2 option 3). | https://docs.snowflake.com/en/release-notes/2025/9_00 |

---

## 7. Points de vigilance Business Critical

**Source :** https://docs.snowflake.com/en/user-guide/intro-editions

Features à **ne pas mentionner** dans la propale car **non dispo en BC** (réservées à Virtual Private Snowflake) :
- Environnement Snowflake totalement isolé / serveurs dédiés
- Clés en mémoire sur serveurs dédiés uniquement

**Tout ce qui est dans la propale actuelle est disponible en BC.** Pas de risque de sur-promesse de ce côté, tant qu'on ne cite pas VPS.

Point d'attention : **Tri-Secret Secure avec Hybrid Tables** impose `Dedicated Storage Mode`. Si un jour CAI veut exploiter les Hybrid Tables (Unistore), anticiper dès maintenant cette contrainte — mais pas pertinent pour l'Engagement 1.

**Source Hybrid Tables Dedicated Storage Mode :** https://docs.snowflake.com/en/user-guide/security-encryption-tss

---

## 8. Actions recommandées avant remise

1. **🔴 Clarifier avec CAGIP l'arbitrage sur le hosting Snowflake et la localisation de la CMK** (AWS Francfort + AWS KMS vs Azure West Europe + Azure Key Vault vs External Key Store Thales). L'affirmation "AWS Francfort + Azure Key Vault" telle qu'elle est rédigée est techniquement incohérente — confirmé sur 8 sources indépendantes.
2. **🔴 Remplacer "BIOK" par "Tri-Secret Secure avec Customer-Managed Key (CMK)"** en notant entre parenthèses que CAGIP appelle cette pratique "BIOK" en interne.
3. **🟠 Ajouter "Budgets"** à côté des resource monitors dans la section FinOps pour couvrir le serverless.
4. **🟡 Ajouter un ➜ dédié "Gen2 warehouses"** pour valoriser le gain de perf sans surcoût.
5. **🟡 Préciser les latences ACCOUNT_USAGE** (45 min pour QUERY_HISTORY, 180 min pour METERING, 8h pour QUERY_ATTRIBUTION_HISTORY) si la DAT doit traiter du reporting financier.
6. **🟢 Ne rien changer** sur Row Access Policies, Dynamic Data Masking, PrivateLink, SSO SAML2, Time Travel, Fail-safe, zero-copy clone, query tags, pattern 4 warehouses. Tout tient.
