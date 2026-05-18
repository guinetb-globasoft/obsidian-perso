---
tags: ["commercial", "CA-Immobilier", "brief", "snowflake", "vérification"]
created: 2026-04-23
---

# Brief — Vérification Snowflake pour propale CA Immobilier

**Date :** 23/04/2026
**Objectif :** Valider techniquement les affirmations Snowflake de la propale avant remise commerciale, en s'appuyant sur la documentation officielle Snowflake à jour.

---

## Contexte

Je rédige une proposition commerciale au nom de **SoHoft** pour **Crédit Agricole Immobilier** (migration Modern Data Stack vers Snowflake). La propale contient plusieurs affirmations techniques sur Snowflake que je dois vérifier avant remise.

**Contexte client :**
- Crédit Agricole Immobilier, entité Groupe CA
- Migration de 4 datawarehouses SQL Server hérités vers plateforme unique Snowflake
- 37 flux Talend + SSIS, 1200 tables à terme
- Référentiel CISO Groupe CA très exigeant
- Stack cible : Python + DLT (ingestion) / dbt Core (transfo) / Snowflake / Airflow / Power BI
- Hébergement AWS Francfort
- Démarrage 4 mai 2026

**Édition Snowflake probablement retenue :** Business Critical (vu les exigences sécurité Groupe CA : BIOK, Tri Secret Secure Encryption, Private Link obligatoire, Azure Key Vault). À confirmer.

---

## Ce qui doit être vérifié

### 1. Warehouses dédiés par usage

**Affirmation dans la propale :**
> "Warehouses séparés pour l'ingestion, la transformation, la BI et l'exploration ad hoc. Chacun est dimensionné et paramétré (auto-suspend, scaling policy, multi-cluster) selon son profil de charge, pour maîtriser la consommation dès le départ."

**Pattern proposé (4 warehouses) :**

| Warehouse | Usage | Taille démarrage | Auto-suspend | Scaling |
|---|---|---|---|---|
| WH_INGESTION | DLT depuis Oracle/SQL Server | S ou M | 60s | Single cluster |
| WH_TRANSFORM | Runs dbt | M ou L | 60s | Single cluster |
| WH_BI | Power BI (DirectQuery, dashboards) | M | 300s | Multi-cluster (1-4) |
| WH_ADHOC | Analystes, exploration | XS ou S | 60s | Single cluster |

**À vérifier sur docs.snowflake.com :**

- [ ] Les paramètres `AUTO_SUSPEND`, `AUTO_RESUME`, `MIN_CLUSTER_COUNT`, `MAX_CLUSTER_COUNT`, `SCALING_POLICY` existent-ils toujours en 2026 ? Syntaxe et valeurs autorisées ?
- [ ] Le multi-cluster est-il disponible sur **Business Critical** ? (Je pense que oui à partir de Enterprise, mais à confirmer)
- [ ] Les valeurs de scaling policy sont-elles toujours `STANDARD` et `ECONOMY` ?
- [ ] Le pattern 4 warehouses (ingestion / transform / BI / ad hoc) est-il toujours le pattern recommandé par Snowflake dans ses whitepapers "Workload Isolation Best Practices" ou équivalent ?
- [ ] Les tailles de warehouse disponibles : XS, S, M, L, XL, 2XL, 3XL, 4XL, 5XL, 6XL → toujours vraies ? Nouveaux paliers introduits depuis début 2026 ?
- [ ] Y a-t-il de nouveaux types de warehouses (Snowpark-optimized, etc.) pertinents pour ce cas d'usage ?

**URLs à consulter (existaient en janvier 2026, à vérifier qu'elles sont toujours actives) :**
- https://docs.snowflake.com/en/user-guide/warehouses
- https://docs.snowflake.com/en/user-guide/warehouses-multicluster
- https://docs.snowflake.com/en/sql-reference/sql/create-warehouse
- https://docs.snowflake.com/en/user-guide/intro-editions (features par édition)

### 2. Sécurité — référentiel CISO CA

**Affirmations dans la propale :**
> "Mise en œuvre de BIOK avec Tri Secret Secure Encryption, gestion des clés via Azure Key Vault, SSO Cerbère / ILEX CAGIP, Private Link depuis les postes CAGIP."

**À vérifier :**

- [ ] **Tri Secret Secure Encryption** : fonctionnalité Snowflake qui permet au client de fournir sa propre clé en plus de celle de Snowflake et de celle gérée par le service. À confirmer que c'est bien disponible sur Business Critical uniquement.
- [ ] **BIOK (Bring Your Own Key)** : terme Snowflake officiel ? Ou c'est un terme CA Groupe ? Vérifier la terminologie exacte côté Snowflake (je crois que c'est "Customer-managed keys" ou "Tri Secret Secure").
- [ ] **Azure Key Vault integration** avec Snowflake : est-ce natif ou via un mécanisme tiers ?
- [ ] **AWS PrivateLink** : toujours disponible ? Sur Business Critical ? Quelles régions AWS (Francfort = eu-central-1) ?
- [ ] **SAML 2.0 / SSO** : Snowflake supporte-t-il les fournisseurs IdP que CAGIP utilise (Cerbère / ILEX) ? Au minimum SAML standard ?
- [ ] **Row Access Policies** et **Dynamic Data Masking** : à quelle édition ? Business Critical OK ?

**URLs :**
- https://docs.snowflake.com/en/user-guide/security-encryption-manage
- https://docs.snowflake.com/en/user-guide/admin-security-fed-auth-overview
- https://docs.snowflake.com/en/user-guide/admin-security-privatelink
- https://docs.snowflake.com/en/user-guide/security-row-intro
- https://docs.snowflake.com/en/user-guide/security-column-intro

### 3. Organisation logique — pattern médaillon + domaines

**Affirmation dans la propale :**
> "Structuration en databases et schemas par zone (raw / staging / core / marts) et par domaine fonctionnel"

**À vérifier :**

- [ ] Le pattern **médaillon** (Bronze / Silver / Gold) est-il explicitement documenté par Snowflake ou est-ce plutôt un héritage Databricks adopté dans l'écosystème ?
- [ ] Snowflake a-t-il publié un whitepaper ou un guide sur l'organisation database/schema à grande échelle (1000+ tables) ?
- [ ] Bonnes pratiques officielles sur le **nommage des objets** à l'échelle d'un grand compte ?

### 4. FinOps — resource monitors, query tags, account usage

**Affirmation dans la propale :**
> "Resource monitors avec seuils gradués, query tags pour la refacturation interne, dashboards de consommation, account usage pour l'analyse des coûts."

**À vérifier :**

- [ ] **Resource monitors** : syntaxe actuelle, options (notifications, suspension, quotas), granularité (compte vs warehouse).
- [ ] **Query tags** : toujours la méthode standard pour taguer une session/requête ? Ou est-ce que Snowflake a introduit quelque chose de mieux (ex: session policies) ?
- [ ] **ACCOUNT_USAGE schema** : toujours le schema de référence pour le reporting FinOps ? Latence des vues (90 minutes historiquement) ?
- [ ] Nouveautés FinOps Snowflake 2025-2026 ? Je pense à des features récentes autour de cost management, budgets, alerting.

### 5. Cycle de vie des données — Time Travel, Fail-safe, clones

**Affirmation dans la propale :**
> "Paramétrage de Time Travel et Fail-safe selon les zones, politiques de rétention, clones pour les environnements non-prod (désensibilisés), suppression contrôlée."

**À vérifier :**

- [ ] **Time Travel** : durée max par édition (Business Critical = jusqu'à 90 jours je crois ?).
- [ ] **Fail-safe** : durée fixe (7 jours si je me souviens bien), non paramétrable.
- [ ] **Zero-copy clone** : toujours disponible pour créer rapidement des envs non-prod ? Performance, limites ?
- [ ] **Data masking** pour les clones non-prod : méthode recommandée ?

---

## Livrable attendu

Un rapport synthétique avec :

1. **Pour chaque affirmation vérifiée** : "OK / KO / à ajuster", avec citation de la doc Snowflake à jour (URL + extrait pertinent).
2. **Corrections de formulation** à apporter dans la propale si une affirmation est imprécise ou obsolète.
3. **Features 2025-2026** pertinentes que j'ai ratées et qui pourraient valoriser la propale (ex: Cortex, Snowflake Notebooks, Unistore, Streamlit in Snowflake si pertinent pour CA Immobilier).
4. **Points de vigilance** spécifiques à **Business Critical** : y a-t-il des features habituellement vantées qui ne sont pas disponibles sur cette édition et qu'il ne faudrait pas mentionner ?

---

## Contraintes de rédaction

- **Ton propale** : style Exakis, flèches ➜, concis, vouvoiement pro
- **Jamais mentionner** : IA, Globasoft, partenaire tiers — la propale est 100% SoHoft
- **dbt Core** (pas dbt Cloud — CA utilise Core)
- **Ne pas ajouter de fioritures techniques** qui n'apportent rien au CISO ou à la DSI : on reste sur l'essentiel

---

## Pour référence — extraits de la propale concernés

### Extrait 4.3.1 (Snowflake, plateforme data centrale)

> Snowflake constitue le cœur de la cible. Sa conception structure tout le reste de l'architecture, et notre DAT y consacre un chapitre dédié pour traiter les choix suivants :
>
> ➜ **Organisation logique** : structuration en databases et schemas par zone (raw / staging / core / marts) et par domaine fonctionnel. Cette organisation conditionne la lisibilité de la plateforme pour les 1200 tables à terme.
>
> ➜ **Warehouses dédiés par usage** : warehouses séparés pour l'ingestion, la transformation, la BI et l'exploration ad hoc. Chacun est dimensionné et paramétré (auto-suspend, scaling policy, clustering) selon son profil de charge, pour maîtriser la consommation dès le départ.
>
> ➜ **Modèle RBAC (Role-Based Access Control)** : modèle à deux niveaux (functional roles + access roles) aligné avec les groupes Active Directory et le référentiel d'habilitations Groupe (Usercube). Row Access Policies et Dynamic Data Masking pour satisfaire les exigences CISO sur les données sensibles.
>
> ➜ **Sécurité** : mise en œuvre de BIOK avec Tri Secret Secure Encryption, gestion des clés via Azure Key Vault, SSO Cerbère / ILEX CAGIP, Private Link depuis les postes CAGIP.
>
> ➜ **Gestion du cycle de vie des données** : paramétrage de Time Travel et Fail-safe selon les zones, politiques de rétention, clones pour les environnements non-prod (désensibilisés), suppression contrôlée.
>
> ➜ **Observabilité et FinOps** : resource monitors avec seuils gradués, query tags pour la refacturation interne, dashboards de consommation, account usage pour l'analyse des coûts.

---

## Note perso

La propale complète est dans le vault Obsidian : `00-Inbox/Propale Sohoft - CA Immobilier - Engagement 1.md`. Pas besoin de tout relire pour la vérif Snowflake, la section 4.3.1 suffit.

La priorité est **les warehouses** (affirmation qui m'engage opérationnellement dès l'Engagement 2) et **la sécurité** (affirmation qui sera scrutée par le CISO).

Le reste est secondaire mais bon à valider.