---
tags: ["commercial", "CA-Immobilier", "propale", "sohoft", "synthese"]
created: 2026-04-23
---

# Proposition technique et financière — Synthèse

**SoHoft x Crédit Agricole Immobilier**

**Socle Modern Data Stack sur Snowflake — Phase 1**

Date : 22/04/2026

*Document synthétique destiné aux sponsors (CDO, Direction Générale).*
*Le dossier technique détaillé est remis séparément.*




```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



# Sommaire

1. Compréhension du besoin (contexte, vision cible, enjeux clés)
2. Proposition technique (périmètre, architecture Snowflake, cas d'usage MVP, livrables)
3. Planning macro
4. Engagements SoHoft
5. Hypothèses structurantes
6. Proposition financière
7. Conditions contractuelles




```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



# 1. Compréhension du besoin




```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 3.1 Contexte et enjeux métier

Crédit Agricole Immobilier est l'entité du groupe dédiée aux activités immobilières : Property Management, Promotion Immobilière et Agence. Les opérations de croissance externe conduites ces dernières années ont abouti à une fragmentation du système data :

➜ Deux DSI distinctes héritées des entités rachetées.

➜ Quatre datawarehouses exploités en parallèle.

➜ Des données fortement silotées et une vision business globale difficile à produire.

➜ Un stack d'intégration historique (Talend + SSIS) arrivé en fin de vie, avec 37 flux et 1200 tables à maintenir.

Cette configuration génère aujourd'hui une charge de maintenance élevée — de l'ordre de 70% du temps consacré au MCO — au détriment de la capacité à construire de nouveaux cas d'usage métier.

L'objectif global partagé par votre Direction Data est clair : rationaliser le SI data, sortir du stack legacy, consolider les quatre datawarehouses en une plateforme unique, et restaurer un ratio build / run compatible avec vos ambitions business.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```






```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 3.3 Vision cible (AS-IS → TO-BE)

La cible formalisée par votre Direction Data s'inscrit dans une logique Modern Data Stack, alignée sur les préconisations Groupe. **Snowflake en constitue la pierre angulaire** : la plateforme data devient l'actif central du SI data, autour duquel s'organisent l'ingestion, la transformation, la restitution et la gouvernance.

| Composant | Outil actuel | Cible |
|---|---|---|
| **Stockage / plateforme data** | **SQL Server (4 DWH)** | **Snowflake (plateforme unique)** |
| Ingestion | Talend, SSIS | Python + DLT |
| Transformation | Talend Jobs | dbt Core |
| Orchestration | Talend, SJ7 | Airflow |
| Restitution | Power BI, Business Objects | Power BI |

**Pourquoi Snowflake change la donne :**

➜ **Plateforme unique** — les 4 datawarehouses hérités convergent vers un socle data unifié, fin de la fragmentation issue des rachats.

➜ **Élasticité native** — séparation stockage / compute, dimensionnement à la demande par usage, fin des arbitrages douloureux sur la capacité.

➜ **Modèle de consommation** — fin des licences dimensionnées par anticipation, paiement à l'usage réel, maîtrise possible par le FinOps.

➜ **Écosystème moderne** — intégration native avec dbt, DLT, Power BI, outils de gouvernance et de lineage.

➜ **Sécurité de niveau banque** — support du référentiel CISO Groupe (BIOK, Tri Secret Secure Encryption, Private Link, RBAC fin).

**Bénéfices attendus :**

➜ **Agilité** — dbt Core accélère les cycles de transformation et favorise la collaboration entre équipes Data.

➜ **Performance et scalabilité** — Snowflake offre une élasticité native, sans gestion d'infrastructure on-premise.

➜ **Gouvernance** — traçabilité end-to-end, lineage des données, conformité renforcée.

➜ **Modèle économique** — passage d'un modèle de licences vers un modèle de consommation, à piloter finement (FinOps).



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```






```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 3.4 Enjeux clés identifiés

Quatre enjeux structurent la réussite du projet :

**Enjeu 1 — Réussir l'adoption de Snowflake comme plateforme data unique.**
Snowflake n'est pas un simple remplaçant de SQL Server : c'est une plateforme SaaS, multi-tenant, à modèle de consommation, avec ses propres patterns de sécurité, d'organisation et d'administration. Le DAT doit traduire cette rupture en choix structurants (zones, warehouses, RBAC, gouvernance) avant tout déploiement, pour éviter les erreurs coûteuses à corriger en production.

**Enjeu 2 — Alignement avec le référentiel CISO Groupe.**
Le référentiel de sécurité Groupe est dense et contraignant (BIOK, Tri Secret Secure Encryption, Azure Key Vault, SSO Cerbère/ILEX CAGIP, alimentation unilatérale, Data Masking, désensibilisation non-prod). La validation CISO doit être anticipée dès le cadrage pour éviter les re-travaux.

**Enjeu 3 — Piloter la consommation Snowflake dès le jour 1.**
Le passage au modèle de consommation exige un dispositif FinOps dès le démarrage pour éviter les dérives et préparer le passage à l'échelle. Les engagements de crédits Snowflake contractés au niveau Groupe imposent une discipline de consommation structurée.

**Enjeu 4 — Réussir les premiers cas d'usage (Quick Wins) et industrialiser dès le départ.**
Les deux cas d'usage MVP — Natio (Talend / SQL Server) et NPM Altaix (SSIS / Oracle) — sont les vitrines de Snowflake auprès des métiers. Leur réussite conditionne l'adhésion au programme. Par ailleurs, le volume à migrer (37 flux, 1200 tables) impose une approche par patterns génériques dès la conception — l'industrialisation se pense dès le DAT, pas en fin de projet.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```






```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



# 2. Proposition technique




```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 4.1 Périmètre de notre intervention

### 4.1.1 Trois périmètres couvrant les 5 composants

La présente proposition constitue **une prestation unique au forfait**, couvrant l'ensemble des 5 composants de votre démarche. Elle se structure en trois périmètres indissociables :

➜ **Périmètre 1 — Cadrage & Conception (composants 1, 4, 5).** Production du DAT aligné avec les standards Groupe et les recommandations CISO, cadre FinOps, roadmap de migration globale.

➜ **Périmètre 2 — Déploiement Snowflake (composant 2).** Setup de base de la plateforme : compte, zones, warehouses, RBAC, environnements, conformément au DAT validé.

➜ **Périmètre 3 — Réalisation des Quick Wins (composant 3).** Développement des deux cas d'usage MVP Natio et NPM Altaix : pipelines DLT, modèles dbt, tests, orchestration Airflow.

Chaque périmètre fait l'objet d'un détail de charges et d'un montant dédié dans la proposition financière (voir section 10), mais l'ensemble forme un forfait global.

### 4.1.2 Articulation entre les trois périmètres

Les trois périmètres s'enchaînent selon une logique de maturité croissante :

➜ **Le Périmètre 1 produit le référentiel technique** (DAT) qui guide les suivants.

➜ **Le Périmètre 2 matérialise ce référentiel** dans la plateforme Snowflake.

➜ **Le Périmètre 3 développe les premiers cas d'usage métier** sur la plateforme déployée.

Chaque périmètre a ses propres conditions d'activation et livrables, permettant un reporting d'avancement clair et une facturation échelonnée.

### 4.1.3 Intégrations transverses hors périmètre SoHoft

Les intégrations avec les services Groupe lors du déploiement Snowflake (Périmètre 2) sont à la charge des équipes CAGIP et RSI CA Immobilier :

➜ Private Link AWS

➜ SSO Cerbère / ILEX

➜ BIOK, Tri Secret Secure Encryption, Azure Key Vault

➜ Intégration Usercube

➜ Déversement Graylog

Le DAT produit dans le Périmètre 1 formalise les spécifications d'intégration attendues de ces services, mais leur mise en œuvre technique relève des équipes Groupe. Voir section 9 — Hypothèses structurantes.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```






```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



### 4.3.1 Snowflake, plateforme data centrale

Snowflake constitue le cœur de la cible. Sa conception structure tout le reste de l'architecture, et notre DAT y consacre un chapitre dédié pour traiter les choix suivants :

➜ **Organisation logique** : structuration en databases et schemas selon deux axes complémentaires :

- **Axe maturité** (zones) : raw → staging → core → marts, dans la lignée du pattern médaillon (Bronze / Silver / Gold), avec une distinction staging / core qui sépare le nettoyage technique de la modélisation métier.
- **Axe domaine fonctionnel** (patrimoine, vente de neuf, locatif, promotion, gestion, finance) pour gérer la volumétrie à terme (1200 tables), aligner le RBAC sur les besoins métier, et identifier les data owners.

Cette organisation à deux axes conditionne la lisibilité de la plateforme, la finesse du modèle RBAC, et l'attribution des coûts FinOps par domaine.

➜ **Warehouses dédiés par usage** : warehouses séparés pour l'ingestion, la transformation, la BI et l'exploration ad hoc. Chacun est dimensionné et paramétré (auto-suspend, scaling policy, clustering) selon son profil de charge, pour maîtriser la consommation dès le départ.

➜ **Modèle RBAC (Role-Based Access Control)** : modèle à deux niveaux (functional roles + access roles) aligné avec les groupes Active Directory et le référentiel d'habilitations Groupe (Usercube). Row Access Policies et Dynamic Data Masking pour satisfaire les exigences CISO sur les données sensibles.

➜ **Sécurité** : mise en œuvre de BIOK avec Tri Secret Secure Encryption, gestion des clés via Azure Key Vault, SSO Cerbère / ILEX CAGIP, Private Link depuis les postes CAGIP. Conformité totale avec les recommandations CISO Groupe.

➜ **Gestion du cycle de vie des données** : paramétrage de Time Travel et Fail-safe selon les zones, politiques de rétention, clones pour les environnements non-prod (désensibilisés), suppression contrôlée.

➜ **Observabilité et FinOps** : resource monitors avec seuils gradués, query tags pour la refacturation interne, dashboards de consommation, account usage pour l'analyse des coûts.

Le DAT produit tous les éléments de spécification nécessaires pour paramétrer Snowflake conformément à ces choix, avant même le démarrage du déploiement technique (Périmètre 2).




```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 4.5 Focus sur les deux cas d'usage MVP

Les cas d'usage MVP sont déjà identifiés. Notre engagement porte sur la rédaction de leurs spécifications détaillées dans le DAT.

### 4.5.1 Projet Natio (Talend / SQL Server)

| Caractéristique | Valeur |
|---|---|
| Technologie ETL actuelle | Talend |
| Source | SQL Server |
| Périmètre ODS | Source DR + tables de configuration |
| Périmètre DWH | Modélisation indicateurs niveau ligne, historisation mensuelle |
| Modèle cible | 2 tables de faits (Déclaration + Valeurs) + 2 dimensions |
| Complexité | Moyenne |
| Nombre de sources | 9 |
| Nombre de cibles | 4 |
| Périmètre MVP réduit | Source DR uniquement, activité Vente de Neuf |

**Point d'attention technique :** la conception Talend actuelle intègre des règles de gestion en SQL et en Java. Notre DAT formalisera le pattern de ré-implémentation (RG SQL traitées en dbt, RG Java à rejouer en SQL dbt ou en Python DLT selon les cas).

### 4.5.2 Projet NPM Altaix (SSIS / Oracle)

| Caractéristique | Valeur |
|---|---|
| Technologie ETL actuelle | SSIS |
| Source | Oracle |
| Périmètre ODS | One Altaix actuel |
| Périmètre DWH | Base DWH NPM + re-modélisation éventuelle |
| Pattern actuel | SSIS simple et générique par table (requête source + requête contrôle) |
| Complexité | Simple |
| Nombre de sources | 15 |
| Nombre de cibles | 7 |
| Périmètre MVP réduit | Patrimoine (CABINET, SECTEUR, SERVICE, LOT, BATIMENT, IMMEUBLE) |

**Opportunité de démonstration :** le pattern générique de NPM Altaix se prête particulièrement bien à la démonstration de l'industrialisation dbt. Un modèle paramétré + une macro génèreront les 15 traitements avec un minimum de code.

### 4.5.3 Articulation avec la grille de chiffrage de migration

Au-delà du chiffrage ferme des deux cas d'usage MVP (voir section 10.4), la mise en œuvre de Natio et NPM Altaix dans le Périmètre 3 fournira la **calibration finale de la grille de chiffrage** (livrable 4.8.2) : les charges réellement consommées alimentent les charges moyennes de référence par catégorie, pour que la grille soit **empiriquement validée et non théorique** avant le démarrage des vagues de migration de Phase 2.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```






```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 2.4 Livrables du Périmètre 1

À l'issue du Périmètre 1, SoHoft remet six livrables structurants. Chaque livrable a une finalité opérationnelle et un destinataire identifié. Le détail complet (contenu, destinataires, formats) figure dans le dossier technique.

### DAT — Document d'Architecture Technique

**Finalité :** document de référence de la migration, cadrant toutes les décisions techniques structurantes pour Snowflake et la Modern Data Stack. Intègre également les spécifications détaillées des deux cas d'usage MVP, qui constituent le "contrat de réalisation" du Périmètre 3.

### Grille de chiffrage de migration

**Finalité :** outil opérationnel qui permet, en Phase 2, de chiffrer de manière ferme, rapide et reproductible les vagues de migration des 37 flux et 1200 tables restants, **sans ré-ouvrir les discussions à chaque vague**. Sécurise le passage à l'échelle.

### Cartographie macro de l'existant

**Finalité :** vision structurée et partagée du patrimoine actuel, base de travail pour la priorisation de la roadmap de migration.

### Cadre FinOps

**Finalité :** dispositif de pilotage de la consommation Snowflake, prêt à déployer, couvrant le composant 4 de votre démarche.

### Roadmap de migration globale

**Finalité :** plan de migration des 37 flux legacy vers la Modern Data Stack, priorisé et phasé, couvrant le composant 5 de votre démarche.

### Supports de présentation

**Finalité :** supports permettant au sponsor de porter le projet auprès des instances de décision.




```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



# 3. Planning macro




```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## Vue d'ensemble (3 périmètres, 18 semaines)

| Périmètre                                    | Période                                                    | Durée                                         |
| -------------------------------------------- | ---------------------------------------------------------- | --------------------------------------------- |
| **Périmètre 1** — Cadrage & Conception       | 04/05 → 26/06/2026                                         | 8 semaines                                    |
| **Périmètre 2** — Déploiement Snowflake      | 22/06 → 03/07/2026 (partiellement en recouvrement avec P1) | 2 semaines                                    |
| **Périmètre 3** — Réalisation des Quick Wins | 06/07 → 04/09/2026                                         | 9 semaines (dont 4 semaines de fabrication sans utilisateurs du 20/07 au 15/08) |




```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



# 4. Engagements SoHoft




```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```






```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 7.1 Engagement de résultat sur les livrables

Nous nous engageons fermement sur la livraison des éléments listés en section 4.8, dans le respect du planning défini en section 6.

Chaque livrable fait l'objet :

➜ D'une relecture client (2 jours ouvrés).

➜ D'une validation formelle en COPIL.

➜ D'une itération de 2 jours ouvrés maximum si ajustements.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 7.2 Engagement de délai

Nous nous engageons sur les dates de fin suivantes, sous réserve du respect des engagements de disponibilité des ressources client listés en section 5.4 :

➜ **Fin du Périmètre 1** : 26 juin 2026 (8 semaines)

➜ **Fin du Périmètre 2** : 3 juillet 2026 (démarrage en recouvrement avec P1)

➜ **Fin du Périmètre 3** : 4 septembre 2026 (clôture globale de la mission)

Tout écart est signalé en COPIL dès qu'il est identifié, avec proposition de plan d'action.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 7.3 Engagement de qualité

Nos livrables respectent les standards suivants :

➜ **DAT** : structure conforme aux attendus Groupe, validé CISO avant remise finale.

➜ **Cartographie** : format exploitable (Excel structuré), revue avec le responsable du patrimoine data.

➜ **Grille de chiffrage de migration** : catégorisation objective, règles d'affectation explicites, charges de référence pré-acceptées, validation empirique via les deux cas d'usage MVP, utilisable de manière autonome par vos équipes et par des prestataires tiers.

➜ **Spécifications détaillées des cas d'usage MVP (chapitre du DAT)** : critères d'acceptation explicites, validés par les référents métier avant démarrage du Périmètre 3.

➜ **Présentations** : supports revus avec le sponsor avant diffusion.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 7.4 Engagement de transparence

Trois principes guident notre communication :

➜ **Alerte immédiate** en cas d'identification d'un risque ou d'un point dur — remontée en coproj hebdo au plus tard, avec escalade vers le sponsor hors COPIL si impact bloquant nécessitant un arbitrage rapide.

➜ **Reporting hebdomadaire** en coproj, consolidé aux 4 COPIL positionnés sur les jalons clés du projet, sans embellissement.

➜ **Traçabilité complète** des décisions via les comptes-rendus d'ateliers, de coproj et de COPIL.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```






```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



# 5. Hypothèses structurantes

Les engagements fermes de SoHoft reposent sur un ensemble d'hypothèses explicites. Toute hypothèse significativement invalidée en cours de mission donne lieu à un avenant documenté avant impact sur les livrables ou le planning.

## Système d'information existant

➜ Volumétrie conforme : 37 flux Talend + SSIS, 1200 tables, SQL Server (90%) + Oracle.
➜ Documentation des flux legacy disponible au moins pour les 2 cas d'usage MVP.
➜ Stabilité du paysage applicatif pendant la durée de la mission.

## Référentiel CISO et services Groupe

➜ Recommandations CISO stables pendant la mission.
➜ Services Groupe opérationnels : Snowflake (contrat cadre actif), Private Link AWS, SSO Cerbère/ILEX, Azure Key Vault, Usercube, Graylog.
➜ Inscription SoHoft au contrat cadre Groupe effective dans les 2 semaines suivant la signature.

## Déploiement Snowflake (Périmètre 2)

➜ Compte Snowflake mis à disposition avant démarrage du P2.
➜ Intégrations Groupe transverses (Private Link, SSO, Key Vault…) portées par CAGIP/RSI.
➜ Modèle RBAC arrêté dans le DAT, sans ré-arbitrage en phase de déploiement.

## Cas d'usage MVP (Périmètre 3)

➜ Périmètres Natio et NPM Altaix stables (scope arrêté dans le DAT).
➜ Règles de gestion Java Natio de complexité standard, transposables en SQL dbt / Python DLT.
➜ Données sources de qualité exploitable (pas de reprise massive ni de déduplication complexe).

## Disponibilité des parties prenantes

➜ Disponibilités formalisées en section 5.4 effectivement tenues.
➜ Réponse des interlocuteurs transverses (CAGIP, RSI) sous 3 jours ouvrés.

## Contractuel

➜ Signature au plus tard le 30 avril 2026 pour un démarrage au 4 mai 2026.
➜ Process d'achat Groupe non-bloquant sur le démarrage.

## Invalidation d'une hypothèse

Notification immédiate en COPIL ➜ analyse d'impact ➜ avenant ➜ pas d'arrêt de la mission en dehors des lots directement impactés.




```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



# 6. Proposition financière




```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```






```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 10.1 Modèle d'engagement

La présente proposition constitue **une prestation unique au forfait**, avec engagement de résultat sur les livrables définis. Elle se structure en trois périmètres indissociables.

| Périmètre | Objet | Composants couverts | Charge | Montant (€ HT) |
|---|---|---|---:|---:|
| **Périmètre 1** | Cadrage & Conception | 1, 4, 5 | 56 j | **39 200 €** |
| **Périmètre 2** | Déploiement Snowflake (setup de base) | 2 (partiel) | 5 j | **3 500 €** |
| **Périmètre 3** | Réalisation des Quick Wins | 3 | 36 j | **21 300 €** |
| **Forfait global** | | | **97 j** | **64 000 €** |

Chaque périmètre couvre l'ensemble des lots de travail, le pilotage, les ateliers et une itération de 2 jours ouvrés par livrable.

**Précision importante sur le Périmètre 2 (Déploiement Snowflake) :** notre intervention couvre le setup de base de la plateforme (compte, zones, warehouses, RBAC, environnements). Les intégrations transverses avec les services Groupe (Private Link, SSO Cerbère/ILEX, Azure Key Vault, Usercube, Graylog) relèvent des équipes CAGIP et RSI CA Immobilier, et ne sont pas incluses dans ce chiffrage. Voir section 9 — Hypothèses structurantes pour le détail.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 10.2 Détail Périmètre 1 par lot

| Bloc fonctionnel | Phase | Charge (jours) | TJM (€) | Prix (€ HT) |
|---|---|---:|---:|---:|
| **Lot 1 — Cadrage et ateliers** | | | | |
| | Kickoff et ateliers cadrage | 8 | 700 | 5 600 |
| | Pilotage projet | 8 | 700 | 5 600 |
| **Lot 2 — DAT et architecture cible** | | | | |
| | Cartographie AS-IS macro | 5 | 700 | 3 500 |
| | Formalisation DAT | 12 | 700 | 8 400 |
| | Intégration recommandations CISO | 9 | 700 | 6 300 |
| | Spécifications détaillées cas d'usage MVP | 3 | 700 | 2 100 |
| **Lot 3 — FinOps, Roadmap et clôture** | | | | |
| | Cadre FinOps | 3 | 700 | 2 100 |
| | Roadmap de migration globale | 2 | 700 | 1 400 |
| | Présentations DG et CISO | 6 | 700 | 4 200 |
| **Total Périmètre 1** | | **56** | | **39 200 €** |



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 10.3 Détail Périmètre 2 — Déploiement Snowflake

| Bloc fonctionnel | Phase | Charge (jours) | TJM (€) | Prix (€ HT) |
|---|---|---:|---:|---:|
| Setup | Compte Snowflake, databases, schemas, zones (raw/staging/core/marts) | 1 | 700 | 700 |
| Configuration | Warehouses par usage + paramétrage (auto-suspend, scaling policy) | 1 | 700 | 700 |
| Sécurité | Déploiement RBAC (functional + access roles) selon DAT | 1,5 | 700 | 1 050 |
| Environnements | Dev / Recette / Production + documentation | 1 | 700 | 700 |
| Transverse | Pilotage & coordination | 0,5 | 700 | 350 |
| **Total Périmètre 2** | | **5** | | **3 500 €** |

**Périmètre précis de notre intervention :**

➜ Setup de la plateforme Snowflake sur l'environnement dédié à CA Immobilier.

➜ Déploiement de la structure logique (zones, databases, schemas) conforme au DAT.

➜ Création des warehouses dimensionnés par usage.

➜ Déploiement du modèle RBAC tel que défini dans le DAT.

➜ Mise en place des 3 environnements et documentation de déploiement.

**Hors périmètre — à la charge des équipes Groupe :**

➜ Mise en place du Private Link AWS (CAGIP).

➜ Intégration SSO Cerbère / ILEX (CAGIP).

➜ Activation BIOK + Tri Secret Secure Encryption + Azure Key Vault (RSI CA Immobilier).

➜ Intégration Usercube pour la gestion des habilitations (CAGIP / équipes habilitations).

➜ Déversement des événements sécurité vers Graylog (CAGIP).

➜ Déploiement technique des resource monitors et du dashboard FinOps.

Ces intégrations transverses font l'objet d'un chiffrage distinct lorsque les services Groupe concernés auront confirmé leur disponibilité et leurs prérequis. Elles ne conditionnent pas la livraison du Périmètre 2.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 10.4 Détail Périmètre 3 — Réalisation des Quick Wins

Les caractéristiques détaillées des deux cas d'usage nous permettent de proposer un chiffrage ferme dès la présente proposition.

### Détail par cas d'usage

| Bloc | Phase | Charge (jours) | TJM (€) | Prix (€ HT) |
|---|---|---:|---:|---:|
| **Natio** (Talend / SQL Server, complexité moyenne) | | | | |
| | Analyse & documentation des règles de gestion (SQL + Java) | 3 | 700 | 2 100 |
| | Setup pipelines DLT + modèles dbt staging (9 sources) | 5 | 550 | 2 750 |
| | Modèles dbt core (2 faits + 2 dimensions, historisation mensuelle) | 5 | 550 | 2 750 |
| | Tests dbt, recette métier, documentation | 6 | 550 | 3 300 |
| | **Sous-total Natio** | **19** | | **10 900** |
| **NPM Altaix** (SSIS / Oracle, complexité simple) | | | | |
| | Conception macro dbt générique + template YAML | 3 | 700 | 2 100 |
| | Instanciation des 7 cibles du Patrimoine via template | 3 | 550 | 1 650 |
| | Setup pipeline DLT, tests, recette, documentation | 5 | 550 | 2 750 |
| | **Sous-total NPM Altaix** | **11** | | **6 500** |
| **Transverse** | | | | |
| | Pilotage Périmètre 3 | 3 | 700 | 2 100 |
| | Intégration Airflow (orchestration des 2 cas d'usage) | 2 | 550 | 1 100 |
| | Coordination avec l'environnement Snowflake | 1 | 700 | 700 |
| | **Sous-total transverse** | **6** | | **3 900** |
| **TOTAL Périmètre 3** | | **36** | | **21 300 €** |

### Conditions d'activation

Le Périmètre 3 est ferme sous réserve des conditions suivantes :

➜ Validation formelle du DAT par le CISO à l'issue du Périmètre 1.

➜ Environnement Snowflake opérationnel (Périmètre 2 réalisé).

➜ Intégrations Groupe nécessaires au développement effectives (accès depuis postes CAGIP, SSO fonctionnel).

➜ Périmètre des deux cas d'usage identique à celui décrit en section 4.5.

➜ Disponibilité des sources de données et des accès nécessaires.

### Livrables du Périmètre 3

➜ Pipelines DLT opérationnels pour Natio (source DR) et NPM Altaix (Patrimoine).

➜ Modèles dbt staging, intermediate et core pour les deux cas d'usage.

➜ Macro dbt générique et template YAML réutilisables pour la Phase 2 de migration.

➜ Tests dbt (schema, fraîcheur, cohérence métier) et rapports de recette.

➜ DAGs Airflow d'orchestration.

➜ Documentation technique et fonctionnelle des deux cas d'usage.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 10.5 Modalités de facturation

➜ **Jalonnement proposé** (à ajuster selon le cadre contractuel Groupe) :

| Échéance | Montant (€ HT) | Base |
|---|---:|---|
| Signature | 19 200 € | 30% du forfait global |
| DAT V1 livré — J5 (S6) | 12 800 € | 20% du forfait global |
| Validation CISO + DG, clôture P1 — J6 (S8) | 12 800 € | 20% du forfait global |
| Clôture Périmètre 2 — J7 (S9) | 3 500 € | Solde P2 |
| Recette métier validée — J9 (S17) | 9 600 € | 15% du forfait global |
| Clôture globale — J10 (S18) | 6 100 € | Solde de la mission |
| **Total** | **64 000 €** | |

➜ **Délai de paiement** : 30 jours date de facture.

➜ **Frais de déplacement** : inclus dans la prestation pour les déplacements en Île-de-France. Au réel pour les déplacements hors Île-de-France (sur justificatifs, après accord préalable).



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 10.6 Conditions de révision

Le forfait est ferme et définitif dans les conditions définies dans la présente proposition.

Une révision du forfait ne pourrait intervenir que dans les cas suivants :

➜ **Élargissement du scope** demandé par le client en cours de mission.

➜ **Non-respect des engagements de disponibilité des ressources client** listés en section 5.4, entraînant un décalage de plus de deux semaines du planning ou une dégradation notable de la capacité de production.

➜ **Délai de réponse des équipes transverses** (CAGIP, RSI, équipes habilitations) supérieur à 5 jours ouvrés sur un point bloquant.

➜ **Évolution majeure des recommandations CISO** en cours de projet, non identifiée à date.

➜ **Invalidation significative d'une hypothèse structurante** listée en section 9.

Toute révision fait l'objet d'un avenant formel avant mise en œuvre. Conformément à notre engagement de transparence (section 7.4), nous alertons en COPIL dès l'apparition d'un facteur pouvant conduire à une révision, pour permettre un arbitrage conjoint sans surprise.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```






```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



# 7. Conditions contractuelles




```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```






```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 11.1 Durée et démarrage

➜ **Démarrage prévu** : 4 mai 2026, sous réserve de signature préalable.

➜ **Durée totale de la mission** : 18 semaines.

➜ **Fin prévisionnelle globale** : 4 septembre 2026.

➜ Détail des jalons par périmètre : voir section 6.1.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 11.2 Modalités de collaboration


➜ **Mixte présentiel / distanciel** pour les ateliers, réunions et les temps de production.

➜ **Outils collaboratifs** : à convenir avec CA Immobilier (Teams, SharePoint, Git, Confluence selon le cadre Groupe).



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 11.3 Propriété intellectuelle

L'ensemble des livrables produits dans le cadre de la présente proposition (DAT, cartographie, cadre FinOps, roadmap, setup Snowflake, pipelines, supports) devient la propriété de Crédit Agricole Immobilier à l'issue du règlement complet de la prestation.

SoHoft conserve la propriété de ses méthodes, outils, frameworks et savoir-faire génériques, qui ne sont pas couverts par le transfert de propriété des livrables.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 11.4 Confidentialité

L'ensemble des informations échangées dans le cadre de la mission est couvert par une clause de confidentialité réciproque, pendant la durée de la mission et les 3 années qui suivent.

SoHoft s'engage à respecter les clauses de confidentialité du contrat cadre Groupe Crédit Agricole, dès son inscription effective en tant que sous-traitant.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 11.5 Validité de l'offre

La présente proposition est valable **30 jours** à compter de sa date de diffusion.

Au-delà, SoHoft se réserve le droit de réviser les conditions commerciales et de planning.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



**Bon pour accord**

Nom :
Fonction :
Date :
Signature précédée de la mention « Bon pour accord » :



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```


