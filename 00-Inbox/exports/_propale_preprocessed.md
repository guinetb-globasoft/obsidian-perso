---
tags: ["commercial", "CA-Immobilier", "propale", "sohoft", "DAT"]
created: 2026-04-23
---
	
# Proposition technique et financière

**SoHoft x Crédit Agricole Immobilier**

**Socle Modern Data Stack sur Snowflake — Phase 1**

Date : 22/04/2026



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



# Sommaire

1. Synthèse générale de notre offre
2. Qui est SoHoft
3. Compréhension du besoin
   3.1 Contexte et enjeux métier
   3.2 Situation AS-IS
   3.3 Vision cible (AS-IS → TO-BE)
   3.4 Enjeux clés identifiés
   3.5 Alignement avec les 5 composants de votre démarche
4. Proposition technique
   4.1 Périmètre de notre intervention
   4.2 Notre approche méthodologique
   4.3 Architecture cible recommandée
   4.4 Intégration des recommandations CISO
   4.5 Focus sur les deux cas d'usage MVP
   4.6 Cadre FinOps
   4.7 Roadmap de migration globale
   4.8 Livrables du Périmètre 1
   4.9 Livrables des Périmètres 2 et 3
5. Organisation projet
   5.1 Équipe projet dédiée
   5.2 Répartition des rôles et responsabilités
   5.3 Instances de pilotage
   5.4 Disponibilité des ressources client et prérequis
6. Jalons et planning
   6.1 Macro-planning global (3 périmètres)
   6.2 Jalons de validation
   6.3 Logique d'enchaînement et parallélisation
   6.4 Points de vigilance planning
7. Engagements SoHoft
   7.1 Engagement de résultat sur les livrables
   7.2 Engagement de délai
   7.3 Engagement de qualité
   7.4 Engagement de transparence
8. Facteurs de risque et mesures d'atténuation
   8.1 Risques identifiés
   8.2 Plan de mitigation
   8.3 Conditions limites de notre engagement
9. Hypothèses structurantes
   9.1 Préambule
   9.2 Hypothèses sur le système d'information existant
   9.3 Hypothèses sur le référentiel CISO et les services Groupe
   9.4 Hypothèses sur le déploiement Snowflake (Périmètre 2)
   9.5 Hypothèses sur les cas d'usage MVP (Périmètre 3)
   9.6 Hypothèses sur la disponibilité des parties prenantes
   9.7 Hypothèses contractuelles et administratives
   9.8 Invalidation d'une hypothèse
10. Proposition financière
   10.1 Modèle d'engagement
   10.2 Détail Périmètre 1 par lot
   10.3 Détail Périmètre 2 — Déploiement Snowflake
   10.4 Détail Périmètre 3 — Réalisation des Quick Wins
   10.5 Modalités de facturation
   10.6 Conditions de révision
11. Conditions contractuelles
   11.1 Durée et démarrage
   11.2 Modalités de collaboration
   11.3 Propriété intellectuelle
   11.4 Confidentialité
   11.5 Validité de l'offre

**Annexes**
   A. Schéma d'architecture cible
   B. Arborescence type d'un projet dbt
   C. Exemple concret d'un modèle YAML-driven (NPM Altaix)



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



# 3. Compréhension du besoin



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



## 3.2 Situation AS-IS

L'écosystème actuel repose sur un stack historique orienté SQL Server, exploité à 90%, complété par Oracle pour les ERP majeurs.

| Composant | Outil actuel |
|---|---|
| Ingestion | Talend, SSIS |
| Transformation | Talend Jobs |
| Orchestration | Talend, SJ7 |
| Stockage | SQL Server |
| Restitution | Power BI, Business Objects |

**Points d'attention observés :**

➜ Incidents de production récurrents, notamment sur la couche SSIS.

➜ Modèle de licences (Talend, SQL Server) sans maîtrise fine de la consommation par usage.

➜ Gouvernance data à construire — un Data Management Office est en cours de structuration.

➜ Compétences internes majoritairement SQL, avec une appétence Python chez les Data Analysts.



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



## 3.5 Alignement avec les 5 composants de votre démarche

Votre démarche de Phase 1 est structurée autour de 5 composants. Notre proposition les couvre intégralement :

| Composant | Intitulé                       | Positionnement SoHoft                                                 |
| ----- | ------------------------------ | --------------------------------------------------------------------- |
| 1     | Conception & Validation du DAT | **Couvert par la présente proposition (Périmètre 1)**                |
| 2     | Déploiement Snowflake          | **Couvert par la présente proposition (Périmètre 2, setup de base)** |
| 3     | Quick Wins Métiers             | **Couvert par la présente proposition (Périmètre 3)**                |
| 4     | Rapport FinOps                 | **Couvert par la présente proposition (cadre + templates)**           |
| 5     | Roadmap de Migration Globale   | **Couvert par la présente proposition**                               |

La présente proposition constitue **une prestation unique au forfait**, couvrant l'ensemble des 5 composants de votre démarche. Elle se structure en trois périmètres indissociables : Périmètre 1 (Cadrage & Conception), Périmètre 2 (Déploiement Snowflake), Périmètre 3 (Réalisation des Quick Wins).

Les intégrations transverses avec les services Groupe lors du déploiement Snowflake (Private Link, SSO Cerbère/ILEX, Azure Key Vault, Usercube, Graylog) sont portées par les équipes CAGIP et RSI CA Immobilier. Voir section 9 — Hypothèses structurantes pour le détail.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



# 4. Proposition technique



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



## 4.2 Notre approche méthodologique

### 4.2.1 Principes directeurs

Notre approche s'appuie sur quatre principes structurants :

➜ **Ateliers structurants en amont.** Les ateliers de cadrage sont programmés en début de mission pour sécuriser les choix d'architecture avant la phase de rédaction. Les décisions prises sont tracées en comptes-rendus partagés avec les parties prenantes.

➜ **Alignement CISO anticipé.** Le CISO est intégré au dispositif dès la deuxième semaine. Ses exigences sont prises en compte en amont de la rédaction, pas en fin de parcours.

➜ **Orientation industrialisation.** Le DAT est pensé pour minimiser le code ad hoc et maximiser les patterns génériques (macros dbt, modèles paramétrés, sources YAML-driven). L'industrialisation n'est pas un chapitre, c'est une ligne directrice.

➜ **Grille de chiffrage, outil de pilotage durable.** Nous construisons dès le Périmètre 1 une grille de chiffrage standardisée (livrable 4.8.2) qui deviendra l'outil opérationnel de pilotage budgétaire de la migration sur toute la durée du programme. Elle sera empiriquement calibrée par les deux cas d'usage MVP du Périmètre 3 avant les vagues de migration ultérieures, pour garantir sa fiabilité.

### 4.2.2 Industrialisation et généricité

L'industrialisation est au cœur de notre proposition. Elle se traduit concrètement par :

➜ Des **macros dbt réutilisables** pour les patterns récurrents (ingestion, historisation, dédoublonnage, gestion des changements dans les dimensions).

➜ Des **modèles génériques configurables** (YAML) — au lieu de recoder le même traitement pour chaque table similaire (comme les 15 tables de NPM Altaix), un seul modèle est paramétré par un fichier de configuration. Ajouter une table revient à ajouter quelques lignes de configuration, pas à créer un nouveau fichier de code. Bénéfice : logique de sécurité et de qualité codée une seule fois, maintenance simplifiée, contribution accessible à des profils data analyst.

➜ Un **générateur de squelettes de code** (scaffolding) — une commande unique génère instantanément les fichiers types (modèle, tests, documentation) pour un nouveau flux, avec les bonnes conventions et dépendances pré-câblées. Sur un périmètre de 1200 tables, ce type d'outillage permet de diviser par 2 à 3 le temps de mise en place initial de chaque flux.

➜ Une **convention de nommage** et une organisation par couches (staging / intermediate / marts) uniformes sur l'ensemble du projet.

Cette orientation permettra, en Phase 2 de réalisation, de traiter les 1200 tables avec un effort de développement significativement réduit par rapport à une approche ligne à ligne.

### 4.2.3 Règle des ateliers

Nos ateliers suivent une discipline stricte :

➜ **Préparation** : trame de questionnement, hypothèses à confirmer, support de décision.

➜ **Animation** : décisions explicites en séance, pas de renvoi à plus tard.

➜ **Compte-rendu** : formalisation dans les 48h, diffusion à l'ensemble des parties prenantes.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 4.3 Architecture cible recommandée

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

### 4.3.2 Stack d'ingestion, transformation et orchestration autour de Snowflake

Autour de la plateforme Snowflake, la stack s'organise comme suit :

➜ **Ingestion** : pipelines Python + DLT pour l'extraction Oracle et SQL Server, avec gestion native des schémas évolutifs et de l'incrémental. Écriture directe dans la zone raw de Snowflake.

➜ **Transformation** : dbt Core organisé selon le pattern staging / intermediate / marts, avec macros génériques et tests natifs. Exécution des transformations directement dans Snowflake (push-down), sans mouvement de données.

➜ **Orchestration** : Airflow pour l'enchaînement des pipelines DLT, des runs dbt, des contrôles qualité et de la coordination avec les processus métier.

➜ **Restitution** : Power BI en cible principale, connecté à Snowflake via DirectQuery ou import selon les usages. Traitement du legacy Business Objects.

### 4.3.3 Alimentation unilatérale et zone sécurisée

Une contrainte CISO structurante concerne l'alimentation unilatérale : Snowflake récupère les données via une zone sécurisée, sans flux retour vers les systèmes sources.

Notre DAT formalisera cette contrainte dans l'architecture d'ingestion :

➜ Mise en œuvre d'une zone tampon sécurisée alimentée par les systèmes sources.

➜ Pipelines DLT en mode "pull" depuis cette zone vers Snowflake, sans accès direct aux bases Oracle / SQL Server.

➜ Traçabilité complète des flux pour audit CISO.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 4.4 Intégration des recommandations CISO

Les recommandations CISO que vous avez formulées constituent un référentiel exigeant. Notre DAT les traite de manière structurée selon vos quatre axes.

### 4.4.1 Gouvernance & Communication

➜ Présentation du projet à la Direction Générale.

➜ Communication formelle à Square Habitat en tant que nouveau sous-traitant.

➜ Contractualisation via le contrat cadre Groupe.

➜ Formalisation du document d'architecture Data CA Immobilier.

➜ Réalisation d'une analyse de risques.

### 4.4.2 Sécurité des Données

➜ Mise en œuvre de BIOK avec Tri Secret Secure Encryption.

➜ Gestion des clés via Azure Key Vault (équipe RSI CA Immobilier).

➜ Interdiction des exports locaux de données.

➜ Interdiction du Data Sharing ou encadrement strict.

➜ Data Masking pour les outils tiers (Power BI).

➜ Désensibilisation des données en non-production.

### 4.4.3 Infrastructure & Accès

➜ Hébergement AWS Francfort (couvert par contrat).

➜ Accès Snowflake uniquement depuis postes CAGIP.

➜ SSO Cerbère / ILEX CAGIP obligatoire.

➜ Alimentation unilatérale (Snowflake récupère via zone sécurisée).

➜ Aucun autre mécanisme d'accès autorisé.

### 4.4.4 Gouvernance des Accès

➜ Définition d'un RACI et de profils d'habilitation.

➜ Séparation des rôles (admin ≠ Data Scientist).

➜ Intégration de la gestion des habilitations dans Usercube.

➜ Vérification des mécanismes de sauvegarde et de restauration (clones Snowflake).

➜ Déversement des événements de sécurité dans Graylog.



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



## 4.6 Cadre FinOps

### 4.6.1 Principes et périmètre

Notre livrable FinOps correspond au composant 4 de votre démarche : un **cadre de surveillance** des coûts Snowflake, sous forme de document et de templates prêts à déployer.

➜ Conventions de tagging (par projet, équipe, usage, environnement).

➜ Définition des resource monitors (seuils, actions automatiques).

➜ Structure du tableau de bord de consommation.

➜ Document de gouvernance des coûts (qui paie quoi, comment refacturer).

➜ Règles d'optimisation (auto-suspend, clustering, dimensionnement).

Le déploiement technique de ce cadre dans Snowflake sera réalisé dans le cadre du Périmètre 2.

### 4.6.2 Dispositif de surveillance et refacturation

Le dispositif conçu vise à :

➜ Prévenir la surconsommation par des seuils d'alerte gradués.

➜ Attribuer la consommation par projet / équipe pour permettre la refacturation interne.

➜ Fournir un reporting mensuel consolidé aux sponsors.

➜ Identifier les poches d'optimisation (warehouses surdimensionnés, requêtes coûteuses).



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 4.7 Roadmap de migration globale

La roadmap de migration couvre le composant 5 de votre démarche. Elle propose une priorisation et une planification des 37 flux legacy vers la Modern Data Stack.

**Critères de priorisation :**

➜ Valeur métier (criticité pour les sponsors, fréquence d'usage).

➜ Complexité technique (logique métier, volumétrie, dépendances).

➜ Dépendances entre flux (ordre de migration contraint).

➜ Coût de maintenance actuel (priorité aux flux qui consomment le plus de MCO).

**Structuration :**

➜ Vagues de migration trimestrielles.

➜ Jalon intermédiaire à fin décembre 2026 (2/3 du patrimoine migré).

➜ Cible T1 2027 pour la migration complète.

➜ Identification des pré-requis techniques par vague (RBAC, nouveaux warehouses, modèles génériques).



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 4.8 Livrables du Périmètre 1

À l'issue du Périmètre 1, nous remettrons six livrables structurants. Chaque livrable a une finalité opérationnelle précise et un destinataire identifié.

### 4.8.1 Document d'Architecture Technique (DAT)

**Finalité :** document de référence de la migration, cadrant toutes les décisions techniques structurantes pour Snowflake et la Modern Data Stack. Intègre également les spécifications détaillées des deux cas d'usage MVP, qui constituent le "contrat de réalisation" du Périmètre 3.

**Contenu principal :**

➜ Principes d'architecture et choix structurants.

➜ Chapitre Snowflake dédié : organisation logique, warehouses, RBAC, sécurité, cycle de vie, observabilité.

➜ Architecture d'ingestion DLT et pattern d'alimentation unilatérale.

➜ Architecture de transformation dbt Core (staging / intermediate / marts, macros, tests).

➜ Architecture d'orchestration Airflow.

➜ Traitement des 4 axes de recommandations CISO.

➜ **Spécifications détaillées des deux cas d'usage MVP** (Natio et NPM Altaix) : périmètre fonctionnel, sources, cibles, modèle de données, règles de gestion, volumétrie, critères d'acceptation, tests de recette attendus.

➜ Standards, conventions de nommage, bonnes pratiques.

➜ Schémas d'architecture (applicatifs, flux, sécurité).

**Destinataires :** CISO, DSI, équipe Data, référents métier Natio et NPM Altaix, SoHoft pour la réalisation du Périmètre 3.

**Validation :** par le CISO (jalon J4) et la DSI. Validation du chapitre "spécifications détaillées des cas d'usage MVP" par les référents métier avant démarrage du Périmètre 3.

### 4.8.2 Grille de chiffrage de migration

**Finalité :** outil opérationnel qui permet, en Phase 2, de chiffrer de manière ferme, rapide et reproductible les vagues de migration des 37 flux et 1200 tables restants, **sans ré-ouvrir les discussions à chaque vague**. Sécurise le passage à l'échelle.

**Contenu :**

➜ **Taxonomie des traitements** — catégorisation par type fonctionnel (extraction simple, extraction avec CDC, transformation de dimension, transformation de fait, historisation SCD, agrégation, réconciliation inter-sources).

➜ **Catégorisation par complexité** — règles objectives pour classer un traitement en simple / moyen / complexe, s'appuyant sur des critères mesurables (nombre de sources, nombre de règles de gestion, présence de code non-SQL, volumétrie, criticité, dépendances).

➜ **Charges moyennes par catégorie** — nombre de jours/homme standardisés par type × complexité, validés conjointement et engageants.

➜ **Règles d'affectation** — arbre de décision permettant à n'importe quel interlocuteur de catégoriser un traitement sans ambiguïté.

➜ **Pondérations transverses** — coefficients pour le pilotage, la recette, la documentation, appliqués à chaque vague.

➜ **Exemples calibrés** — application de la grille aux 2 cas d'usage MVP pour démontrer son fonctionnement.

➜ **Modèle de chiffrage Excel** — fichier de simulation permettant de chiffrer une vague en saisissant simplement la liste des traitements et leurs caractéristiques.

**Bénéfices clés pour CA Immobilier :**

➜ **Prévisibilité budgétaire** — à tout moment, vous pouvez estimer le coût de migration des 1200 tables restantes avec une marge d'erreur maîtrisée.

➜ **Sécurisation du forfait** sur les vagues suivantes — fini les discussions de chiffrage traitement par traitement.

➜ **Benchmark concurrentiel** — la grille permet d'appeler des offres concurrentes sur un même référentiel objectif.

➜ **Indépendance** — vous n'êtes pas captif d'un prestataire. La grille est votre propriété.

➜ **Accélération des décisions** — arbitrer une priorisation ou un changement de scope prend des minutes, pas des semaines.

**Destinataires :** Direction Data, Direction Achats, futurs prestataires de migration.

**Format :** chapitre dédié du DAT + fichier Excel de simulation autonome.

### 4.8.3 Cartographie macro de l'existant

**Finalité :** vision structurée et partagée du patrimoine actuel, base de travail pour la priorisation de la roadmap de migration.

**Contenu :**

➜ Inventaire des 37 flux Talend + SSIS avec caractéristiques (source, cible, fréquence, volumétrie, criticité).

➜ Inventaire macro des 1200 tables par domaine fonctionnel.

➜ Classification par complexité selon la grille de chiffrage (livrable 4.8.2).

➜ Identification des dépendances majeures entre flux.

➜ Estimation du coût MCO actuel par flux (sur la base des informations disponibles).

**Destinataires :** Direction Data, responsable du patrimoine data, futurs prestataires de migration.

**Format :** fichier Excel structuré et filtrable.

**Note :** cartographie macro, pas ligne à ligne. Le détail des règles de transformation de chaque flux reste à l'intérieur des développements unitaires ultérieurs.

### 4.8.4 Cadre FinOps

**Finalité :** dispositif de pilotage de la consommation Snowflake, prêt à déployer, couvrant le composant 4 de votre démarche.

**Contenu :**

➜ Document de gouvernance des coûts (qui paie quoi, comment refacturer, qui arbitre en cas de dérive).

➜ Conventions de tagging Snowflake (par projet, équipe, usage, environnement).

➜ Spécifications des resource monitors (seuils gradués, actions automatiques, destinataires des alertes).

➜ Maquette du tableau de bord de consommation (à implémenter dans Power BI ou natif Snowflake).

➜ Règles d'optimisation technique (auto-suspend, clustering, dimensionnement des warehouses).

➜ Processus de revue FinOps mensuelle (cadence, participants, indicateurs suivis).

**Destinataires :** Direction Data, Direction Financière, équipe plateforme.

**Note :** le déploiement technique de ce cadre dans Snowflake est réalisé dans le cadre du Périmètre 2.

### 4.8.5 Roadmap de migration globale

**Finalité :** plan de migration des 37 flux legacy vers la Modern Data Stack, priorisé et phasé, couvrant le composant 5 de votre démarche.

**Contenu :**

➜ Priorisation des flux selon 4 critères : valeur métier, complexité technique, dépendances, coût MCO actuel.

➜ Découpage en vagues de migration trimestrielles.

➜ Pré-chiffrage de chaque vague à partir de la grille de chiffrage (livrable 4.8.2).

➜ Jalon intermédiaire fin décembre 2026 (2/3 du patrimoine).

➜ Cible T1 2027 pour la migration complète.

➜ Pré-requis techniques par vague (nouveaux warehouses, modèles dbt à créer, habilitations à provisionner).

➜ Indicateurs de suivi global de la migration.

**Destinataires :** Direction Data, Direction Générale, futurs prestataires de migration.

### 4.8.6 Supports de présentation

**Finalité :** supports permettant au sponsor de porter le projet auprès des instances de décision.

**Contenu :**

➜ **Support CISO** — synthèse des choix d'architecture en regard des 4 axes de recommandations, éléments clés de conformité.

➜ **Support Direction Générale** — vision stratégique, enjeux, gains attendus, planning, budget global, ROI attendu.

**Destinataires :** Sponsor (CDO), CISO, DSI, Direction Générale.

**Format :** slides éditables remises au sponsor, adaptées au contexte de présentation.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 4.9 Livrables des Périmètres 2 et 3

### 4.9.1 Livrables du Périmètre 2 — Déploiement Snowflake

➜ **Plateforme Snowflake opérationnelle** — compte configuré, databases et schemas créés selon les zones DAT, warehouses dimensionnés, environnements dev / recette / production.

➜ **Modèle RBAC déployé** — functional roles et access roles créés conformément au DAT.

➜ **Procédure de déploiement documentée** — étapes exécutées, scripts utilisés, commit sur le référentiel de déploiement (infrastructure-as-code si applicable).

➜ **Procès-verbal de conformité** — checklist des éléments livrés, confirmation de bon fonctionnement, liste des prérequis transverses restant à la charge des équipes Groupe pour la mise en production complète.

### 4.9.2 Livrables du Périmètre 3 — Réalisation des Quick Wins

➜ **Pipelines DLT opérationnels** pour Natio (source DR) et NPM Altaix (Patrimoine).

➜ **Modèles dbt** (staging, intermediate, core) pour les deux cas d'usage, avec tests natifs.

➜ **Macro dbt générique + template YAML** réutilisables pour la Phase 2 de migration — patron d'industrialisation validé sur NPM Altaix.

➜ **DAGs Airflow d'orchestration** des deux cas d'usage.

➜ **Rapports de recette** validés par les référents métier.

➜ **Documentation technique et fonctionnelle** des deux cas d'usage : sources, règles de gestion implémentées, schémas cibles réels, procédure de run, procédure d'exploitation, guide de reprise sur incident.

➜ **Transfert de compétence** à l'équipe Data CA Immobilier (session dédiée + documentation).



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



# 5. Organisation projet



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 5.1 Équipe projet dédiée

Notre dispositif repose sur une équipe courte pour maximiser la réactivité, complétée par un expert Snowflake senior mobilisé aux étapes clés pour sécuriser les choix structurants.

**Périmètres 1 et 2 — Cadrage, Conception & Déploiement Snowflake :**

➜ **Architecte Data (lead)** : pilotage global, rédaction du DAT, animation des ateliers structurants (architecture, CISO, DG), déploiement Snowflake.

➜ **Expert Data Engineering** : cartographie AS-IS, spécifications détaillées des cas d'usage MVP, conception du cadre FinOps, arbitrages techniques de détail.

➜ **Expert Snowflake senior (SnowPro Advanced Architect)** : contribution à la conception de l'architecture Snowflake dans le DAT (organisation logique, dimensionnement warehouses, modèle RBAC, sécurité Business Critical, FinOps natif Snowflake), puis audit de conformité du déploiement à l'issue du Périmètre 2. Intervient en appui de l'Architecte Data aux jalons structurants, pas en continu — garantit l'alignement avec les best practices Snowflake sans alourdir le dispositif.

**Périmètre 3 — Réalisation des Quick Wins :**

➜ **Architecte Data** : pilotage, conception des patterns génériques (macro dbt, template YAML), analyse des règles de gestion Natio.

➜ **Développeur Data Engineer** : implémentation des pipelines DLT, des modèles dbt, des tests, de l'orchestration Airflow.

Cette configuration garantit un interlocuteur unique pour votre équipe et limite les points de friction dans les échanges techniques, tout en s'appuyant sur une expertise Snowflake certifiée aux moments où elle apporte le plus de valeur.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 5.2 Répartition des rôles et responsabilités

### 5.2.1 Côté Crédit Agricole Immobilier

| Rôle | Fonction | Mission |
|---|---|---|
| Sponsor | Chief Data Officer (CDO) | Arbitrages, validation des livrables, COPIL |
| Référent technique | Expert Talend / Référent technique | Expertise existant, connexion équipes |
| Validation sécurité | Responsable CISO | Validation du DAT au regard des recommandations CISO |
| Validation SI | DSI | Validation du DAT au regard de l'urbanisation SI |

### 5.2.2 Côté SoHoft

| Rôle | Périmètre | Mission |
|---|---|---|
| Architecte Data (lead) | P1 + P2 + P3 | Pilotage, rédaction DAT, ateliers, présentations, déploiement Snowflake, conception des patterns |
| Expert Snowflake senior (SnowPro Advanced Architect) | P1 + P2 | Appui à la conception du chapitre Snowflake du DAT (zones, warehouses, RBAC, sécurité BC, FinOps), audit de conformité du déploiement |
| Expert Data Engineering | P1 | Cartographie, cadre FinOps, spécifications détaillées MVP |
| Développeur Data Engineer | P3 | Implémentation DLT, dbt, tests, orchestration Airflow |

### 5.2.3 Articulation avec les services Groupe

Notre DAT intègrera les prérequis techniques liés aux services Groupe mobilisés :

➜ **CAGIP** : accès Snowflake depuis postes CAGIP, SSO Cerbère / ILEX.

➜ **RSI CA Immobilier** : gestion des clés via Azure Key Vault.

➜ **Usercube** : intégration de la gestion des habilitations.

➜ **Graylog** : déversement des événements de sécurité.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 5.3 Instances de pilotage

Trois instances rythment le projet, avec une logique de cadence adaptée à chaque finalité :

➜ **Comité projet hebdomadaire (30 min)** avec le référent technique : point d'avancement opérationnel, alertes à chaud, arbitrages techniques courants, préparation des ateliers de la semaine. Format court pour garder la cadence sans mobiliser excessivement les équipes.

➜ **Comité de pilotage (1h)** avec le sponsor (CDO), le référent technique et les parties prenantes pertinentes : revue consolidée, décisions structurantes, arbitrages budget / planning / scope, communication des points durs nécessitant un sponsorship. **Les COPIL sont positionnés sur les moments de décision du projet**.

Sur les 18 semaines de mission, cela se traduit par **4 COPIL positionnés stratégiquement** :

| COPIL | Semaine | Moment-clé | Objet |
|---|---|---|---|
| **COPIL 1** | S4 (25-29 mai) | Revue intermédiaire DAT — J3 | Go/no-go sur les choix d'architecture cible avant finalisation de la rédaction du DAT |
| **COPIL 2** | S8 (22-26 juin) | Clôture P1 — J6 | Validation formelle CISO + présentation DG, transition vers P2 et P3 |
| **COPIL 3** | S11 (13-17 juillet) | Modèles dbt en place — J8 | Bilan de la phase de construction des Quick Wins avant la coupure estivale du 20/07 au 15/08, validation du point d'arrêt avant pause |
| **COPIL 4** | S18 (31 août - 04 sept) | Clôture globale — J10 | Validation de la recette métier, transfert de compétence, clôture administrative et financière |

Les écarts sont de 4, 3 et 7 semaines. **L'écart de 7 semaines entre COPIL 3 et COPIL 4 est cohérent avec le principe de non-sollicitation des équipes CA Immobilier durant la coupure estivale du 20 juillet au 15 août** : aucun COPIL, aucun atelier, aucune validation demandée pendant cette période. Le COPIL 3 en S11 valide le verrouillage de la conception (J8) avant le départ en congés. Le COPIL 4 en S18 clôt la mission au retour. Le kickoff de S1 constitue en lui-même l'événement de lancement et ne nécessite pas de COPIL additionnel.

➜ **Comité technique à la demande** avec le référent technique et les experts concernés : décisions techniques et validation des livrables intermédiaires, déclenché selon les besoins des ateliers.

➜ **Échanges structurés avec le CISO** : questions écrites en semaine 3, réponses intégrées en semaine 5, validation formelle du DAT V1 en semaine 7-8.

**Principe de pilotage :** le coproj hebdo assure la réactivité opérationnelle (arbitrages techniques courants, alertes à chaud) ; le COPIL concentre les décisions structurantes aux moments où elles ont un impact réel sur la suite du projet. Cette logique évite la multiplication de réunions à faible valeur ajoutée et préserve le temps du sponsor pour les arbitrages qui comptent.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 5.4 Disponibilité des ressources client et prérequis

La réussite de la mission dans le planning contractuel dépend directement de la disponibilité des ressources client. Le forfait et l'engagement de résultat que nous proposons reposent sur les engagements de disponibilité suivants.

### 5.4.1 Disponibilité minimale requise des parties prenantes

| Interlocuteur                       | Disponibilité attendue                                                                                                                 | Finalité                                               |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **Sponsor (CDO)**                   | 4 COPIL de 1h répartis sur les 18 semaines de mission (S4, S8, S11, S18) + kickoff (1h en S1) + revues de livrables, soit ~7h cumulées | Arbitrages, validation des livrables                   |
| **Référent technique**              | 2 jours / semaine sur 8 semaines (dont coproj hebdo 30 min)                                                                            | Expertise existant, ateliers, relectures, coproj       |
| **Responsable CISO**                | Réponses écrites aux questions envoyées en S3 (sous 5 jours ouvrés) + validation formelle du DAT V1 en S7-S8 (2h)                      | Cadrage sécurité par écrit, validation formelle du DAT |
| **DSI CA Immobilier**               | 1 revue (2h) en semaine 5 + 1 présentation DG en semaine 8                                                                             | Validation SI + sponsorship                            |
| **Représentant Direction Générale** | 1 présentation (1h) en semaine 8                                                                                                       | Validation finale du DAT                               |
| **Interlocuteur CAGIP**             | Joignable avec réponse sous 3 jours ouvrés                                                                                             | Coordination Private Link, SSO, Graylog                |
| **Interlocuteur RSI CA Immobilier** | Joignable avec réponse sous 3 jours ouvrés                                                                                             | Coordination Azure Key Vault, chiffrement              |
| **Référent métier Natio**           | 2 ateliers (2h) pour spécifier le cas d'usage                                                                                          | Règles de gestion, recette                             |
| **Référent métier NPM Altaix**      | 2 ateliers (2h) pour spécifier le cas d'usage                                                                                          | Patrimoine, recette                                    |

**Total charge client estimée sur le Périmètre 1 :** environ 20 jours/homme cumulés sur 8 semaines, majoritairement portés par le référent technique.

### 5.4.2 Disponibilité des ressources pour le Périmètre 2 (Déploiement Snowflake)

| Interlocuteur | Disponibilité attendue |
|---|---|
| **Administrateur Snowflake CA Immobilier** | Disponible pour transfert d'accès et revue de conformité |
| **Interlocuteur CAGIP** | Disponible pour validation de la configuration réseau et SSO |
| **Équipe RSI** | Disponible pour la remise du matériel de chiffrement (Key Vault) |

### 5.4.3 Disponibilité des ressources pour le Périmètre 3 (Quick Wins)

| Interlocuteur | Disponibilité attendue |
|---|---|
| **Référent métier Natio** | 3 jours répartis sur la durée (ateliers, recette, validation) |
| **Référent métier NPM Altaix** | 3 jours répartis sur la durée (ateliers, recette, validation) |
| **Administrateur sources Oracle / SQL Server** | Joignable pour les questions d'accès et de schéma |

### 5.4.4 Autres prérequis

➜ **Accès à la documentation existante** des flux Talend et SSIS, a minima pour Natio et NPM Altaix, fournie en semaine 1.

➜ **Accès en lecture aux sources de données** (Oracle ERP, SQL Server applications) sur environnement de développement, fourni en semaine 2.

➜ **Inscription SoHoft au contrat cadre Groupe** : processus à enclencher par les équipes juridiques CA Immobilier dès la signature.

➜ **Mise à disposition des outils collaboratifs** Groupe (Teams, SharePoint, Git, Confluence) en semaine 1.

➜ **Compte Snowflake provisionné** (contrat actif, édition, région AWS Francfort) avant démarrage du Périmètre 2.

### 5.4.5 Conséquences d'une indisponibilité

Le non-respect des engagements de disponibilité ci-dessus constitue un des cas ouvrant droit à révision du forfait (voir section 10.6). Concrètement :

➜ Tout report d'atelier structurant supérieur à 5 jours ouvrés décale mécaniquement le jalon concerné.

➜ Une indisponibilité cumulée du référent technique de plus de 2 jours sur 2 semaines consécutives impacte la capacité de production et pourra justifier un avenant.

➜ Un délai de réponse CAGIP / RSI supérieur à 5 jours ouvrés sur un point bloquant peut conduire à sortir le sujet du scope du Périmètre concerné.

**Principe :** nous alertons en COPIL dès qu'une indisponibilité observée menace un jalon. Aucune facturation surprise — toute dérive est signalée et arbitrée conjointement.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



# 6. Jalons et planning



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 6.1 Macro-planning global (3 périmètres)

**Démarrage : 4 mai 2026 — Fin prévisionnelle : 4 septembre 2026 (18 semaines)**

### 6.1.1 Vue d'ensemble

| Périmètre                                    | Période                                                    | Durée                                         |
| -------------------------------------------- | ---------------------------------------------------------- | --------------------------------------------- |
| **Périmètre 1** — Cadrage & Conception       | 04/05 → 26/06/2026                                         | 8 semaines                                    |
| **Périmètre 2** — Déploiement Snowflake      | 22/06 → 03/07/2026 (partiellement en recouvrement avec P1) | 2 semaines                                    |
| **Périmètre 3** — Réalisation des Quick Wins | 06/07 → 04/09/2026                                         | 9 semaines (dont 4 semaines de fabrication sans utilisateurs du 20/07 au 15/08) |

### 6.1.2 Détail Périmètre 1 — Cadrage & Conception (S1 à S8)

| Semaine | Période    | Activités principales                                          | Jalon                        |
| ------- | ---------- | -------------------------------------------------------------- | ---------------------------- |
| S1      | 04-08 mai  | Kickoff, ateliers existant, démarrage cartographie             | J1 - Kickoff validé          |
| S2      | 11-15 mai  | Atelier architecture cible, atelier gouvernance                |                              |
| S3      | 18-22 mai  | Démarrage rédaction DAT, atelier FinOps                        | J2 - Questions CISO envoyées |
| S4      | 25-29 mai  | Rédaction DAT cœur, spécifications détaillées cas d'usage MVP  | J3 - Revue intermédiaire DAT |
| S5      | 01-05 juin | Intégration réponses CISO dans DAT, cadre FinOps               | J4 - Réponses CISO reçues    |
| S6      | 08-12 juin | Finalisation DAT V1, roadmap de migration                      | J5 - DAT V1 livré            |
| S7      | 15-19 juin | Soumission DAT V1 au CISO, itérations éventuelles              |                              |
| S8      | 22-26 juin | Validation CISO formelle, présentation DG, clôture P1          | J6 - Validation CISO + DG    |

### 6.1.3 Détail Périmètre 2 — Déploiement Snowflake (S7 à S9)

| Semaine | Période | Activités principales | Jalon |
|---|---|---|---|
| S7 | 15-19 juin | Setup compte Snowflake, databases, zones (en parallèle de P1) | |
| S8 | 22-26 juin | Déploiement warehouses + RBAC + environnements dev/rec/prod | |
| S9 | 29 juin - 03 juillet | Documentation, PV de conformité, revue avec administrateur Snowflake CA | J7 - Plateforme Snowflake opérationnelle |

Le Périmètre 2 démarre en semaine 7, en parallèle de la finalisation du Périmètre 1, pour garantir un environnement Snowflake opérationnel au démarrage du Périmètre 3.

### 6.1.4 Détail Périmètre 3 — Réalisation des Quick Wins (S10 à S18)

| Semaine | Période | Activités principales | Jalon |
|---|---|---|---|
| S10 | 06-10 juillet | Kickoff P3, analyse RG Natio (SQL + Java), conception macro dbt générique NPM Altaix, setup DLT Natio + NPM Altaix, **ateliers référents métier (finalisation conception)** | |
| S11 | 13-17 juillet | Modèles dbt staging + core Natio, instanciation 7 cibles NPM Altaix, DAGs Airflow de base, **verrouillage des spécifications fonctionnelles avec les référents métier** | J8 - Modèles dbt en place & conception verrouillée (vendredi 17/07) |
| S12-S13 | 20 juillet - 31 juillet | **Période estivale — fabrication possible sans interaction utilisateur** : itérations techniques dbt, optimisations, tests unitaires, rédaction documentation technique | |
| S14-S15 | 03 août - 14 août | **Période estivale — fabrication possible sans interaction utilisateur** : finalisation documentation, préparation supports de recette, ajustements mineurs | |
| S16 | 17-21 août | Reprise pleine : préparation recette métier, vérifications finales avant ouverture aux référents | |
| S17 | 24-28 août | Recette métier avec référents Natio et NPM Altaix, itérations | J9 - Recette métier validée |
| S18 | 31 août - 04 septembre | Transfert de compétence, finalisation documentation, clôture P3, mise en production assistée | J10 - Clôture globale de la mission |

**Note sur la période estivale :** le planning distingue deux régimes d'activité.

➜ **Du 20 juillet au 15 août (S12-S15)** : l'équipe SoHoft peut poursuivre les activités de **fabrication pure** qui ne nécessitent aucun échange avec les utilisateurs — itérations techniques dbt, optimisations, tests, documentation. **Cela suppose que la conception fonctionnelle soit totalement verrouillée au 17 juillet** : toutes les règles de gestion Natio validées, tous les schémas cibles NPM Altaix acceptés par les référents métier, tous les critères d'acceptation fixés. Le jalon J8 inclut explicitement ce verrouillage.

➜ **Aucune sollicitation des référents métier ni du sponsor n'est prévue durant la coupure.** Pas de COPIL, pas d'atelier, pas de validation demandée. La reprise pleine n'a lieu qu'au 17 août (S16).

➜ Si la conception n'est pas verrouillée au 17 juillet (absence de référent, RG Natio à retravailler, ambiguïtés non résolues), alors l'activité de l'été est **arrêtée** et non simplement ralentie — on ne prend pas le risque de fabriquer sur des spécifications instables. Dans ce cas, un avenant de décalage est proposé en COPIL 3 avant la coupure.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 6.2 Jalons de validation

### 6.2.1 Jalons du Périmètre 1

➜ **J1 — Kickoff validé (S1)**
Périmètre confirmé, planning affiné, interlocuteurs mobilisés, accès organisés.

➜ **J2 — Questions CISO envoyées (S3)**
Liste structurée de questions et hypothèses adressée au responsable CISO par mail : points de conformité à confirmer, précisions sur le référentiel Groupe (BIOK, Tri Secret, Azure Key Vault, SSO Cerbère, Data Masking, désensibilisation), validation des choix d'architecture envisagés. Cette formalisation évite un atelier dédié tout en sécurisant les arbitrages.

➜ **J3 — Revue intermédiaire DAT (S4)**
Présentation des choix d'architecture cible au sponsor (CDO) et au référent technique. Décision GO ou ajustements avant rédaction finale.

➜ **J4 — Réponses CISO reçues (S5)**
Réponses écrites du CISO aux questions envoyées à J2, intégrées directement dans la rédaction du DAT. Pas d'itération orale nécessaire si les réponses sont claires.

➜ **J5 — DAT V1 livré (S6)**
Version complète du DAT, intégrant les réponses CISO et les ajustements issus de la revue intermédiaire.

➜ **J6 — Validation CISO formelle + présentation DG et clôture du Périmètre 1 (S8)**
Validation formelle signée du DAT V1 par le responsable CISO (après revue en S7 et itérations éventuelles). Présentation Direction Générale. Validation du chapitre "spécifications détaillées des cas d'usage MVP" par les référents métier. Transfert des spécifications pour démarrage du Périmètre 2.

### 6.2.2 Jalon du Périmètre 2

➜ **J7 — Plateforme Snowflake opérationnelle (S9)**
Compte, databases, zones, warehouses, RBAC et environnements dev/recette/production livrés. PV de conformité remis. Prérequis transverses Groupe (Private Link, SSO, Key Vault, Usercube, Graylog) identifiés pour prise en charge par les équipes CAGIP et RSI.

### 6.2.3 Jalons du Périmètre 3

➜ **J8 — Modèles dbt en place & conception verrouillée (S11, vendredi 17 juillet)**
Pipelines DLT opérationnels pour Natio et NPM Altaix, modèles dbt staging et core déployés, macro générique Patrimoine instanciée sur les 7 cibles, DAGs Airflow de base. **Verrouillage fonctionnel explicite** : règles de gestion Natio validées, schémas cibles NPM Altaix acceptés par les référents métier, critères d'acceptation fixés. Ce verrouillage est la condition sine qua non pour que l'équipe SoHoft puisse poursuivre la fabrication technique durant la coupure estivale (20/07 → 15/08) sans sollicitation des utilisateurs. La reprise en S16 peut ainsi se consacrer directement à la recette métier.

➜ **J9 — Recette métier validée (S17)**
Recette métier signée par les référents Natio et NPM Altaix. Rapports de recette remis.

➜ **J10 — Clôture globale de la mission (S18)**
Transfert de compétence effectué, documentation complète remise, mise en production assistée des deux cas d'usage. Clôture administrative et financière de l'ensemble de la prestation.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 6.3 Logique d'enchaînement et parallélisation

Le planning repose sur deux principes d'optimisation :

➜ **Parallélisation P1 / P2** : le Périmètre 2 démarre dès la semaine 7 (S7), en recouvrement avec la finalisation du Périmètre 1. Les spécifications Snowflake sont stables à S6 et permettent de commencer le setup sans attendre la présentation DG finale.

➜ **Enchaînement immédiat P2 / P3** : le Périmètre 3 démarre la semaine suivant la clôture du Périmètre 2 (S10), sur une plateforme Snowflake opérationnelle.

Cette articulation permet de tenir l'objectif T3 2026 de fin de Phase 1 complète, avec une clôture prévisionnelle le 4 septembre 2026.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 6.4 Points de vigilance planning

### 6.4.1 Points durs généraux

➜ **Réactivité du CISO sur les questions écrites.** Les réponses attendues en semaine 5 conditionnent la rédaction du DAT. Un délai supérieur à 5 jours ouvrés à partir de l'envoi (S3) décale le planning.

➜ **Validation CISO formelle en fin de Périmètre 1.** Le jalon J6 est le point dur du Périmètre 1. Une indisponibilité du CISO en S7-S8 pour valider le DAT V1 décale mécaniquement toute la suite du planning.

➜ **Disponibilité du référent technique.** Un rythme de 2 jours par semaine sur le P1 est nécessaire pour maintenir la cadence.

➜ **Process sous-traitant Groupe CA.** L'inscription de SoHoft au contrat cadre Groupe doit être enclenchée dès la signature pour ne pas retarder les accès plateforme (critique pour P2 et P3).

### 6.4.2 Points de vigilance propres au Périmètre 2

➜ **Disponibilité du compte Snowflake.** Le compte doit être provisionné avant S7. Tout retard dans la contractualisation Snowflake ou son activation repousse le démarrage du P2.

➜ **Coordination CAGIP et RSI.** Les intégrations transverses (Private Link, SSO, Key Vault) sont hors de notre périmètre mais conditionnent la mise en production opérationnelle. Une coordination précoce est nécessaire.

### 6.4.3 Points de vigilance propres au Périmètre 3

➜ **Verrouillage de la conception avant la coupure estivale (17 juillet).** La période du 20 juillet au 15 août est utilisable par l'équipe SoHoft pour des activités de fabrication technique **uniquement si la conception fonctionnelle est verrouillée au jalon J8** (règles de gestion Natio validées, schémas cibles NPM Altaix acceptés, critères d'acceptation fixés). Tout point de conception resté ouvert au 17 juillet met en risque l'activité estivale et peut conduire à un décalage de J9 et J10. **La disponibilité des référents métier Natio et NPM Altaix en S10-S11 est donc critique** pour permettre ce verrouillage dans les temps.

➜ **Qualité des données sources.** Découvrir en recette des problèmes de qualité des données (doublons, incohérences, historique manquant) non identifiés en amont peut entraîner des itérations supplémentaires.

➜ **Complexité des règles de gestion Java Natio.** Si la transposition s'avère plus complexe qu'anticipé (voir hypothèse 9.5), un avenant sera proposé sans attendre la fin du P3.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



# 7. Engagements SoHoft



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



# 8. Facteurs de risque et mesures d'atténuation



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 8.1 Risques identifiés

Nous avons identifié les risques principaux suivants :

**R1 — Indisponibilité des ressources client.**
Première cause de dérapage sur ce type de mission. Le forfait repose sur des engagements de disponibilité précis (voir section 5.4). Probabilité : moyenne à élevée dans un contexte grand groupe. Impact : élevé (décalage mécanique des jalons).

**R2 — Disponibilité du CISO insuffisante.**
Sous-ensemble critique de R1. Probabilité : moyenne. Impact : élevé (décalage du jalon J4).

**R3 — Ajustements CISO tardifs conduisant à une refonte partielle du DAT.**
Probabilité : moyenne. Impact : moyen (itérations supplémentaires).

**R4 — Documentation des flux Talend / SSIS incomplète.**
Probabilité : élevée. Impact : moyen (cartographie macro moins précise sur certains flux).

**R5 — Délai de réponse des équipes transverses (CAGIP, RSI).**
Probabilité : élevée dans un contexte grand groupe. Impact : faible sur le Périmètre 1, élevé sur le Périmètre 2 (déploiement bloqué si Key Vault, Private Link ou SSO non disponibles).

**R6 — Process d'inscription sous-traitant Groupe CA long.**
Probabilité : moyenne. Impact : faible sur P1, élevé sur P2 (blocage démarrage).

**R7 — Divergence sur la définition du "terminé" pour les cas d'usage MVP.**
Probabilité : faible. Impact : moyen (recette P3 contestée).



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 8.2 Plan de mitigation

| Risque | Mesure de mitigation |
|---|---|
| R1 — Disponibilité ressources | Engagements de disponibilité précis formalisés en section 5.4, alerte COPIL immédiate en cas d'écart, arbitrage conjoint des impacts |
| R2 — CISO | Questions CISO par mail dès la semaine 2, dates de revue sécurisées en début de projet |
| R3 — Ajustements CISO | Présentation intermédiaire au CISO en semaine 2, avant toute rédaction |
| R4 — Documentation flux | Cartographie macro assumée ; zoom détaillé limité aux 2 cas d'usage MVP |
| R5 — Équipes transverses | Identification nominative des interlocuteurs CAGIP / RSI dès le kickoff, canal de communication direct, escalade via le sponsor (CDO) |
| R6 — Contrat cadre | Déclenchement du process dès la signature, en parallèle du kickoff |
| R7 — Définition "terminé" | Critères d'acceptation formalisés dans le chapitre "spécifications détaillées MVP" du DAT (Périmètre 1), validés avant démarrage P3 |



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 8.3 Conditions limites de notre engagement

Pour garantir la tenue du forfait, nous précisons les limites de scope suivantes :

➜ **Cartographie AS-IS = macro.** Volumes, domaines, fréquences, criticité, classification des 37 flux et 1200 tables. La cartographie détaillée (règles de transformation ligne à ligne) est hors scope du Périmètre 1 et sera traitée lors du développement de chaque cas d'usage.

➜ **Cadre FinOps = conception.** Livrable sous forme de document et de templates. Le déploiement technique dans Snowflake est réalisé dans le cadre du Périmètre 2.

➜ **Développement des cas d'usage MVP (composant 3) chiffré fermement dans le Périmètre 3** (voir section 10.4), sous réserve du périmètre décrit en section 4.5. Tout élargissement (ajout de sources, extension du périmètre fonctionnel) fera l'objet d'un avenant.

➜ **Décommissionnement des anciens systèmes non couvert.** Conformément à votre positionnement (traité en interne).



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



# 9. Hypothèses structurantes



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 9.1 Préambule

Au stade de cette proposition, nous n'avons pas eu accès direct à votre environnement technique, à votre documentation interne ni à l'ensemble de vos interlocuteurs Groupe. Les engagements fermes que nous formulons reposent donc sur un ensemble d'hypothèses que nous explicitons ci-dessous en toute transparence.

**Règle contractuelle :** toute hypothèse significativement invalidée en cours de mission donnera lieu à un avenant documenté avant tout impact sur les livrables ou le planning.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 9.2 Hypothèses sur le système d'information existant

➜ **Volumétrie conforme aux éléments communiqués** : 37 flux Talend + SSIS, 1200 tables, environnement majoritairement SQL Server (90%) + Oracle pour les ERP majeurs.

➜ **Documentation des flux legacy disponible** : fiches fonctionnelles, schémas cibles, règles de gestion de chaque flux accessibles au moins pour les 2 cas d'usage MVP (Natio et NPM Altaix).

➜ **Accès en lecture aux sources** de développement mis à disposition durant le Périmètre 1 pour les spécifications détaillées des cas d'usage MVP.

➜ **Stabilité du paysage applicatif** pendant la durée de la mission : pas de migration simultanée des sources Oracle ou SQL Server susceptible de modifier les schémas ou les volumétries.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 9.3 Hypothèses sur le référentiel CISO et les services Groupe

➜ **Recommandations CISO stables** : le référentiel communiqué (BIOK, Tri Secret, Azure Key Vault, SSO Cerbère/ILEX, Usercube, Graylog, alimentation unilatérale, Data Masking, désensibilisation) ne connaîtra pas d'évolution majeure pendant la durée de la mission.

➜ **Validation CISO en une itération principale** : les questions CISO par mail en semaine 2 permettent d'identifier les points durs en amont ; la validation formelle en semaine 5 se fait sur un DAT aligné avec ces points, sans refonte majeure.

➜ **Services Groupe opérationnels** pour le déploiement Snowflake :
- Contrat cadre Groupe avec Snowflake actif
- Private Link AWS disponible auprès de CAGIP
- SSO Cerbère / ILEX CAGIP en service
- Azure Key Vault administré par RSI CA Immobilier
- Usercube en production
- Graylog opérationnel

➜ **Inscription SoHoft au contrat cadre Groupe** effective dans les 2 semaines suivant la signature de la présente proposition.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 9.4 Hypothèses sur le déploiement Snowflake (Périmètre 2)

Les 5 jours chiffrés pour le Périmètre 2 reposent sur les hypothèses suivantes :

➜ **Compte Snowflake mis à disposition** avec un contrat actif (édition, région AWS Francfort, capacités) avant le démarrage du Périmètre 2.

➜ **Services Groupe transverses non couverts** par notre intervention : Private Link, SSO Cerbère/ILEX, BIOK/Tri Secret/Key Vault, Usercube, Graylog. Ces intégrations sont portées par les équipes CAGIP et RSI CA Immobilier.

➜ **Accès administrateur Snowflake** fournis à notre équipe pour la durée du setup.

➜ **Modèle RBAC préalablement défini dans le DAT** (Périmètre 1), sans ré-arbitrage structurel en phase de déploiement.

Si tout ou partie des intégrations Groupe transverses doit être portée par SoHoft, un chiffrage complémentaire sera proposé.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 9.5 Hypothèses sur les cas d'usage MVP (Périmètre 3)

➜ **Périmètre Natio stable** : source DR uniquement, activité Vente de Neuf, 9 sources → 4 cibles, 2 tables de faits + 2 dimensions, historisation mensuelle.

➜ **Périmètre NPM Altaix stable** : Patrimoine uniquement (CABINET, SECTEUR, SERVICE, LOT, BATIMENT, IMMEUBLE), 15 sources → 7 cibles, pattern SSIS générique par table.

➜ **Règles de gestion Java de Natio d'une complexité standard** : logique métier transposable en SQL dbt ou Python DLT. L'apparition de règles exotiques (appels de services externes, calculs récursifs complexes, manipulations d'objets métier spécifiques) fera l'objet d'un avenant.

➜ **Données sources de qualité exploitable** : les travaux prévus ne couvrent pas de reprise massive, de déduplication complexe ou de réconciliation inter-sources non documentée.

➜ **Environnement Snowflake opérationnel** (Périmètre 2 livré) au démarrage du Périmètre 3.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 9.6 Hypothèses sur la disponibilité des parties prenantes

Les engagements de disponibilité détaillés sont formalisés en section 5.4. En résumé, notre chiffrage repose sur l'hypothèse que :

➜ Les disponibilités listées en section 5.4 sont effectivement tenues par les interlocuteurs concernés.

➜ Les interlocuteurs transverses (CAGIP, RSI, équipes habilitations) répondent sous 3 jours ouvrés sur les points de coordination technique.

➜ Le CISO est disponible aux dates convenues pour l'atelier de cadrage et la revue de validation.

Tout écart significatif à ces hypothèses donne lieu à une alerte COPIL immédiate et à un arbitrage conjoint des impacts (voir section 8.2, risques R1 et R5).



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 9.7 Hypothèses contractuelles et administratives

➜ **Signature de la présente proposition** au plus tard le 30 avril 2026 pour tenir un démarrage au 4 mai 2026.

➜ **Inscription au contrat cadre Groupe** enclenchée par SoHoft dès la signature, avec accompagnement des équipes juridiques CA Immobilier.

➜ **Process de commande Groupe CA** : pas de contrainte d'achat (bons de commande, référencement, appels d'offres) susceptible de retarder le démarrage au-delà du 4 mai.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## 9.8 Invalidation d'une hypothèse

En cas d'invalidation significative de l'une des hypothèses ci-dessus :

➜ **Notification immédiate** en COPIL, avec qualification de l'impact.

➜ **Analyse d'impact** sur le périmètre, la charge, le planning et le prix.

➜ **Avenant** soumis à validation avant mise en œuvre.

➜ **Pas d'arrêt de la mission** en dehors des lots directement impactés — nous continuons à livrer ce qui peut l'être indépendamment de l'hypothèse invalidée.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



# 10. Proposition financière



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



# 11. Conditions contractuelles



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



# Annexes



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## Annexe A — Schéma d'architecture cible

Ce schéma illustre l'articulation entre les différents composants de la Modern Data Stack autour de Snowflake, plateforme centrale.

```
┌──────────────────────────────────────────────────────────────────────┐
│                          SOURCES DE DONNÉES                           │
│   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐               │
│   │  SQL Server  │  │    Oracle    │  │ Autres SI    │               │
│   │ (Natio, ...) │  │ (NPM Altaix) │  │    CA Imm.   │               │
│   └──────┬───────┘  └──────┬───────┘  └──────┬───────┘               │
└──────────┼─────────────────┼─────────────────┼──────────────────────┘
           │                 │                 │
           ▼                 ▼                 ▼
┌──────────────────────────────────────────────────────────────────────┐
│                     ZONE SÉCURISÉE (alimentation unilatérale)        │
│                   Tampon alimenté par les SI sources                  │
└──────────────────────────────┬───────────────────────────────────────┘
                               │ pull
                               ▼
┌──────────────────────────────────────────────────────────────────────┐
│                    INGESTION - Python + DLT                           │
│         Pipelines d'extraction, gestion schémas évolutifs            │
└──────────────────────────────┬───────────────────────────────────────┘
                               │
                               ▼
╔══════════════════════════════════════════════════════════════════════╗
║                    SNOWFLAKE - Plateforme Data Centrale               ║
║                                                                        ║
║   ┌──────────┐   ┌──────────────┐  ┌──────────┐   ┌──────────┐       ║
║   │   RAW    │──▶│   STAGING    │─▶│   CORE   │──▶│  MARTS   │       ║
║   │(sources) │   │(nettoyé/1:1) │  │(métier)  │   │(analyt.) │       ║
║   └──────────┘   └──────────────┘  └──────────┘   └──────────┘       ║
║                                                                        ║
║   ┌─────────────────────────────────────────────────────────────┐    ║
║   │  RBAC (functional + access roles, Usercube)                  │    ║
║   │  Sécurité (BIOK, Tri Secret, Azure Key Vault, Private Link)  │    ║
║   │  Warehouses dédiés (ingestion, transfo, BI, ad hoc)          │    ║
║   │  FinOps (resource monitors, query tags, dashboards)          │    ║
║   └─────────────────────────────────────────────────────────────┘    ║
╚═════════════╤════════════════════════════════════╤══════════════════╝
              │ push-down SQL                      │ Direct Query
              ▼                                    ▼
┌──────────────────────────┐         ┌────────────────────────────────┐
│  TRANSFORMATION          │         │   RESTITUTION - Power BI       │
│  dbt Core                │         │   (DirectQuery / import)       │
│  (macros, tests, YAML)   │         │                                │
└──────────┬───────────────┘         └────────────────────────────────┘
           │ déclenchement
           ▼
┌──────────────────────────────────────────────────────────────────────┐
│                   ORCHESTRATION - Airflow                             │
│              DAGs : ingestion → transformation → qualité              │
└──────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│             SÉCURITÉ & GOUVERNANCE TRANSVERSES (CA Groupe)            │
│  SSO Cerbère/ILEX  │  Usercube  │  Graylog (events sécurité)          │
│  CAGIP (postes, Private Link)   │  RSI CA Immo (Key Vault)            │
└──────────────────────────────────────────────────────────────────────┘
```

**Lecture du schéma :**

➜ **Alimentation unilatérale** : les sources ne sont jamais accédées directement. DLT lit une zone tampon alimentée par les SI sources, conformément à l'exigence CISO.

➜ **Snowflake au centre** : plateforme unique qui stocke les données dans 4 zones (raw / staging / core / marts) et exécute les transformations dbt en push-down.

➜ **dbt Core** : orchestre les transformations directement dans Snowflake, sans mouvement de données. Consomme les modèles YAML-driven (voir Annexe C).

➜ **Airflow** : orchestrateur global. Déclenche les runs DLT, les runs dbt, les contrôles qualité.

➜ **Power BI** : consomme les marts en DirectQuery (pour les données fraîches) ou en import (pour les tableaux de bord à forte interactivité).

➜ **Services Groupe** : intégrés de manière transverse (sécurité, authentification, observabilité sécurité).



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## Annexe B — Arborescence type d'un projet dbt pour CA Immobilier

Structure de référence du repository dbt, versionné dans Git, qui sera mis en œuvre dès le Périmètre 3.

```
ca-immobilier-dbt/
│
├── dbt_project.yml                      # Configuration globale du projet dbt
├── profiles.yml                         # Connexion Snowflake (par environnement)
├── README.md                            # Documentation du projet
│
├── models/
│   │
│   ├── staging/                         # ZONE STAGING
│   │   ├── sources.yml                  # Déclaration des sources Oracle/SQL Server
│   │   ├── _staging__models.yml         # Tests et documentation
│   │   │
│   │   ├── natio/
│   │   │   ├── stg_natio__declarations.sql
│   │   │   ├── stg_natio__valeurs.sql
│   │   │   └── stg_natio__referentiel_dr.sql
│   │   │
│   │   └── npm_altaix/
│   │       ├── stg_npm__cabinet.sql     # Généré automatiquement via YAML
│   │       ├── stg_npm__secteur.sql     # (voir Annexe C)
│   │       ├── stg_npm__service.sql
│   │       ├── stg_npm__lot.sql
│   │       ├── stg_npm__batiment.sql
│   │       └── stg_npm__immeuble.sql
│   │
│   ├── intermediate/                    # ZONE INTERMEDIATE (logique métier)
│   │   ├── _int__models.yml
│   │   │
│   │   └── patrimoine/
│   │       ├── int_patrimoine_hierarchy.sql
│   │       └── int_patrimoine_actif_par_secteur.sql
│   │
│   └── marts/                           # ZONES CORE + MARTS
│       ├── _marts__models.yml
│       │
│       ├── patrimoine/                  # Domaine fonctionnel Patrimoine
│       │   ├── npm_altaix_config.yml    # ← Config YAML (Annexe C)
│       │   ├── dim_cabinet.sql
│       │   ├── dim_secteur.sql
│       │   ├── dim_lot.sql
│       │   ├── dim_immeuble.sql
│       │   └── mart_patrimoine_overview.sql
│       │
│       └── vente_de_neuf/               # Domaine fonctionnel Vente de Neuf
│           ├── dim_produit_neuf.sql
│           ├── dim_programme.sql
│           ├── fct_declaration.sql
│           ├── fct_valeurs_mensuelles.sql
│           └── mart_vente_neuf_pilotage.sql
│
├── macros/                              # Bibliothèque de macros réutilisables
│   ├── generate_schema_name.sql
│   ├── get_raw_table.sql
│   ├── generate_patrimoine_dims.sql    # ← Macro qui lit le YAML (Annexe C)
│   ├── apply_masking_policy.sql
│   ├── historiser_scd2.sql
│   └── tests/
│       ├── test_coherence_cabinet_secteur.sql
│       └── test_dim_integrity.sql
│
├── tests/                               # Tests singletons (data quality)
│   ├── assert_cabinet_actif.sql
│   └── assert_continuite_mensuelle.sql
│
├── seeds/                               # Données statiques (référentiels)
│   └── type_cabinet.csv
│
├── snapshots/                           # Snapshots (historisation SCD2)
│   └── snap_dim_cabinet.sql
│
├── analyses/                            # Requêtes analytiques ad hoc
│
└── .github/workflows/                   # CI/CD
    ├── dbt_ci.yml                       # Tests automatiques sur PR
    └── dbt_deploy.yml                   # Déploiement recette / prod
```

**Points clés de cette organisation :**

➜ **Séparation zones (staging / intermediate / marts) × domaines fonctionnels** — lisibilité immédiate pour les 1200 tables à terme.

➜ **Convention de nommage systématique** — `stg_` pour staging, `int_` pour intermediate, `dim_` / `fct_` pour les dimensions et faits, `mart_` pour les vues métier.

➜ **Fichiers YAML de configuration** à côté des modèles génériques — les patterns répétitifs sont gérés par configuration, pas par duplication de code.

➜ **Macros centralisées** — la logique technique (sécurité, historisation, tests) est codée une fois, appliquée partout.

➜ **CI/CD** — tests automatiques sur chaque Pull Request via GitHub Actions, déploiement automatique vers Snowflake après validation.



```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```



## Annexe C — Exemple concret d'un modèle YAML-driven (NPM Altaix)

Illustration du pattern d'industrialisation par configuration, appliqué au cas d'usage NPM Altaix.

### Principe

Plutôt que d'écrire 6 fichiers SQL quasi identiques pour les 6 entités du Patrimoine (cabinet, secteur, service, lot, bâtiment, immeuble), on écrit :

➜ **Un seul fichier de configuration YAML** qui décrit chaque entité.

➜ **Une seule macro Jinja** qui lit ce YAML et génère le SQL dynamiquement.

➜ **Un seul modèle dbt** qui appelle la macro.

**Bénéfice :** ajouter une 7e entité = 5 lignes de YAML, pas 200 lignes de SQL.

### 1. Le fichier de configuration YAML

Fichier `models/marts/patrimoine/npm_altaix_config.yml` :

```yaml
# Configuration des dimensions du domaine Patrimoine
# Source : NPM Altaix (Oracle)
# Pattern : extraction simple + contrôle de cohérence

patrimoine_entities:

  - name: cabinet
    source_schema: raw__npm_altaix
    source_table: cabinet
    business_key: cabinet_id
    columns:
      - source: id_cabinet
        target: cabinet_id
        type: NUMBER
      - source: lib_cabinet
        target: cabinet_libelle
        type: VARCHAR(200)
      - source: date_crea
        target: created_at
        type: TIMESTAMP
    tests:
      - unique
      - not_null
    masking:
      cabinet_libelle: PII_STANDARD

  - name: secteur
    source_schema: raw__npm_altaix
    source_table: secteur
    business_key: secteur_id
    columns:
      - source: id_secteur
        target: secteur_id
        type: NUMBER
      - source: lib_secteur
        target: secteur_libelle
        type: VARCHAR(200)
      - source: id_cabinet_rattach
        target: cabinet_id
        type: NUMBER
    tests:
      - unique
      - not_null
      - relationships:
          to: ref('dim_cabinet')
          field: cabinet_id

  - name: immeuble
    source_schema: raw__npm_altaix
    source_table: immeuble
    business_key: immeuble_id
    columns:
      - source: id_immeuble
        target: immeuble_id
      - source: adresse
        target: adresse_complete
      - source: code_postal
        target: code_postal
      - source: id_secteur
        target: secteur_id
    tests:
      - unique
      - not_null
    masking:
      adresse_complete: PII_ADDRESS

  # ... service, lot, bâtiment suivent le même pattern
```

### 2. La macro Jinja qui génère le SQL

Fichier `macros/generate_patrimoine_dim.sql` :

```sql
{% macro generate_patrimoine_dim(entity_config) %}

  WITH source AS (
    SELECT
      {% for col in entity_config.columns %}
        {{ col.source }} AS {{ col.target }}{% if not loop.last %},{% endif %}
      {% endfor %}
    FROM {{ source(entity_config.source_schema, entity_config.source_table) }}
    WHERE is_deleted = FALSE
  ),

  dedupliqué AS (
    SELECT *,
      ROW_NUMBER() OVER (
        PARTITION BY {{ entity_config.business_key }}
        ORDER BY created_at DESC
      ) AS rn
    FROM source
  )

  SELECT
    {% for col in entity_config.columns %}
      {% if col.target in entity_config.masking %}
        {{ apply_masking(col.target, entity_config.masking[col.target]) }}
          AS {{ col.target }}{% if not loop.last %},{% endif %}
      {% else %}
        {{ col.target }}{% if not loop.last %},{% endif %}
      {% endif %}
    {% endfor %},
    CURRENT_TIMESTAMP() AS dbt_loaded_at
  FROM dedupliqué
  WHERE rn = 1

{% endmacro %}
```

### 3. Les modèles dbt qui appellent la macro

Fichier `models/marts/patrimoine/dim_cabinet.sql` (et un équivalent pour chaque entité) :

```sql
{{ config(
    materialized='table',
    tags=['patrimoine', 'dimension']
) }}

{{ generate_patrimoine_dim(
    var('patrimoine_entities') | selectattr('name', 'equalto', 'cabinet') | first
) }}
```

**C'est tout.** 3 lignes pour générer la dimension `cabinet`, qui va créer automatiquement :

➜ Les bonnes colonnes avec les bons types.

➜ La logique de déduplication.

➜ L'application du masquage PII (`cabinet_libelle` masqué).

➜ Les tests automatiques (unicité, non-null, relations).

### Impact sur le chiffrage

Sans ce pattern, chaque entité Patrimoine nécessiterait environ 1 jour de dev + tests + doc (soit 6 jours pour les 6 entités).

Avec ce pattern :

➜ **3 jours** pour concevoir la macro générique + le schéma YAML initial (fait une fois).

➜ **0,5 jour** pour instancier les 6 entités (écriture YAML + création des 6 petits fichiers dbt).

➜ Soit **3,5 jours** au lieu de 6 → économie de 40% dès les MVP.

**Sur 1200 tables**, ce même pattern (généralisé à tous les patterns récurrents) permet une économie estimée entre 30% et 50% de l'effort de développement, selon la part de traitements "industrialisables" dans le patrimoine.
