# 📋 Synthèse exécutive — Analyse volumétrie base de données IFS

> **Contexte** : IFS demande une facturation supplémentaire pour le dépassement de volume.
> **Objectif** : Disposer d'éléments factuels pour négocier sur la base d'une décomposition technique précise.
> **Version IFS analysée** : 25R2 (Cloud)
> **Date d'analyse** : Mai 2026

---

## 🎯 Le chiffre clé

> **Sur les 122 Go facturés par IFS, seulement ~13 Go correspondent à des données métier réellement générées par notre activité.**
> **Soit ~11 % du volume total.**

Le reste (~109 Go) correspond à du framework IFS, du code applicatif IFS, des logs techniques IFS, du système Oracle géré par IFS et de l'espace alloué vide.

---

## ⚠️ Point méthodologique important : tablespace ≠ propriétaire du contenu

Une lecture rapide des tablespaces Oracle peut induire en erreur. Le tablespace **`IFSAPP_LOB`** (28,7 Go) **n'est PAS la mesure de "nos fichiers"**. C'est un conteneur Oracle qui regroupe **tous les LOBSEGMENT du schéma IFSAPP**, qu'ils appartiennent à des tables métier (DocMan) ou à des tables internes du framework IFS (modèles UI, logs de debug, traductions...).

**Décomposition réelle de `IFSAPP_LOB`** :

| Origine du contenu | Volume dans IFSAPP_LOB | Part |
|---------------------|-------------------------|------|
| 👤 Documents client (EDM + PDF archive) | 10,6 Go | **37 %** |
| 🏢 Framework IFS (FND_MODEL_*, langues, profils) | 13,0 Go | 45 % |
| 🏢 Logs IFS (BPMN debug, IFS Connect, lobby) | 4,4 Go | 15 % |
| 🏢 Autres petits LOB IFS (templates, libs, permission sets) | 0,7 Go | 3 % |
| **TOTAL** | **28,7 Go** | 100 % |

➡️ **Sur le tablespace nommé "IFSAPP_LOB", seulement 37 % du contenu est à nous.** Le nom du tablespace ne reflète pas la propriété fonctionnelle du contenu.

Cette confusion potentielle est en soi un argument de négociation : la méthode de mesure par tablespace n'est pas adaptée pour distinguer les données générées par le client de celles générées par IFS.

---

## 📊 Décomposition synthétique

| Catégorie                                                      | Volume     | %     | Responsable  |
| -------------------------------------------------------------- | ---------- | ----- | ------------ |
| **Données métier client** (transactions, documents uploadés)   | ~13 Go     | 11 %  | 👤 Nous      |
| **Framework et métadonnées IFS** (UI Aurena, modèles, doc API) | ~12 Go     | 10 %  | 🏢 IFS       |
| **Logs et audit IFS** (BPMN debug, IAM, événements)            | ~10 Go     | 8 %   | 🏢 IFS       |
| **Code PL/SQL IFS compilé** dans schéma SYS                    | ~9 Go      | 7 %   | 🏢 IFS       |
| **Bug Oracle non purgé** (`WRI$_ADV_OBJECTS`)                  | ~11 Go     | 9 %   | 🏢 IFS (DBA) |
| **AWR / stats / dictionnaire Oracle**                          | ~7 Go      | 6 %   | 🏢 IFS (DBA) |
| **Traductions, profils, archives diverses IFS**                | ~8 Go      | 7 %   | 🏢 IFS       |
| **Espace alloué vide** (datafiles non remplis)                 | ~20 Go     | 16 %  | 🏢 IFS (DBA) |
| **TEMP / UNDO / redo logs** (estimation)                       | ~22 Go     | 18 %  | 🏢 IFS (DBA) |
| **Autres petits schémas Oracle**                               | ~10 Go     | 8 %   | 🏢 IFS       |
| **TOTAL**                                                      | **122 Go** | 100 % |              |

---

## 📁 Nature des 13 Go de "données métier client"

**~10 Go sont des documents EDM**, dont la composition réelle a été analysée (cf. `05_Analyse_documents_DocMan.md`) :

| Source | Volume | Nature |
|--------|--------|--------|
| **Talend (TT, automatique)** | **7,4 Go (78 %)** | PJ factures fournisseurs déposées depuis mars 2026 dans le cadre d'un **archivage légal obligatoire** (conservation 10 ans, Code de Commerce L.123-22). **Impurgeable.** Croissance : ~36 Go/an. |
| **NELGRA (manuel)** | 0,9 Go (10 %) | Factures clients déposées manuellement (~100/mois). |
| Autres uploads humains | ~1,2 Go (12 %) | PJ commandes, BL, CRM, divers. |

→ **88 % des "données client" sont en réalité de l'archivage légal automatisé qui ne devrait pas être en BDD Oracle.** La feature `Cloud File Storage` native d'IFS (stockage Azure Blob) répond exactement à ce besoin — voir point clé 7 ci-dessous.

---

## 🔑 Points clés pour la négociation

1. **Seuls 11 % du volume sont réellement nos données métier.** Le ratio "données utiles / volume facturé" est anormalement bas.

2. **~10,9 Go sont occupés par une table de bug Oracle connu** (`WRI$_ADV_OBJECTS` — stockage du SQL Tuning Advisor non purgé). C'est un défaut d'administration côté IFS, pas un usage légitime de la BDD.

3. **~9 Go correspondent au code PL/SQL d'IFS lui-même** (packages, procédures stockées). Nous payons pour stocker leur propre code applicatif.

4. **~20 Go d'espace alloué mais vide** dans les datafiles. C'est de la sur-allocation côté IFS qu'ils nous facturent.

5. **~22 Go de structures Oracle techniques** (TEMP, UNDO, redo, archives) qui sont la responsabilité d'administration IFS et non liés à notre usage.

6. **Plan de purge identifié → gain potentiel de ~30 Go** sans toucher à aucune donnée métier (cf. document `03_Plan_purge.md`).

7. **La feature `Cloud File Storage` d'IFS Cloud (standard, documentée) permet de stocker les documents sur Azure Blob hors BDD Oracle.** Son activation et la migration des 9,5 Go d'EDM existants (essentiellement archivage légal Talend) feraient disparaître mécaniquement le poste documentaire de la BDD et freineraient la dérive (+36 Go/an évités sur le stockage BDD). Setup décrit par IFS comme *"an easy task"* + Web Assistant de migration *"fully automatic"*.

---

## 🎯 Demande à formuler à IFS

> *"Avant toute facturation supplémentaire, nous demandons :*
> 1. *La purge de `WRI$_ADV_OBJECTS` (10,9 Go récupérables immédiatement) ;*
> 2. *Une revue de la rétention AWR et de l'espace UNDO alloué ;*
> 3. *Une procédure officielle de purge sur `FND_MODEL_*`, `BPMN_DEBUG_*`, `IAM_LOGIN_EVENT_*` et `LANGUAGE_FILE_IMPORT_TAB` ;*
> 4. *Une clarification de la base de calcul de la facturation : volume total alloué, volume utilisé tous schémas confondus, ou volume métier client uniquement ?*
> 5. ***La vérification du statut de `Cloud File Storage` sur notre tenant** (la doc IFS précise qu'un storage Azure Blob est 'provisioned automatically per environment'), et si la feature n'est pas active, son activation + le lancement du Web Assistant `Transfer Documents` pour migrer les 9,5 Go d'EDM existants vers Azure Blob hors BDD Oracle ; avec **garantie de continuité pour nos intégrations tierces** consommant les PJ (en particulier Ootary, génération de mails sortants avec PJ factures)."*

---

## 📁 Documents de référence joints

| Fichier | Contenu |
|---------|---------|
| `00_Synthese_executive.md` | Ce document |
| `01_Analyse_volumetrie_complete.md` | Analyse technique détaillée par tablespace, schéma, segment |
| `02_Responsabilite_volumes.md` | **⭐ Document clé** — Qui génère quoi (nous vs IFS vs Oracle) |
| `03_Plan_purge.md` | Plan d'action de purge — gains estimés ~30 Go |
| `04_Argumentaire_negociation_IFS.md` | Arguments structurés pour la négociation |
| `05_Analyse_documents_DocMan.md` | Analyse fine des documents EDM (PJ factures Talend/NELGRA) |
| `06_Referentiel_SQL.md` | Référentiel des requêtes SQL pour audit Quick Report |
| `07_Database_Tasks_purge_IFS.md` | **⭐ Phase autonome** — 17 Database Tasks de purge IFS lançables sans DBA (gain ~10-15 Go) |
