# 📋 Synthèse exécutive — Analyse volumétrie base de données IFS

> **Contexte** : IFS demande une facturation supplémentaire pour le dépassement de volume.
> **Objectif** : Disposer d'éléments factuels pour négocier sur la base d'une décomposition technique précise.
> **Version IFS analysée** : 25R2 (Cloud)
> **Date d'analyse** : Mai 2026

---

## 🎯 Le chiffre clé

> **Sur les 122 Go facturés par IFS, seulement ~13 Go correspondent à des données métiers réellement générées par notre activité.**
> **Soit ~11 % du volume total.**

Le reste (~109 Go) correspond à du framework IFS, du code applicatif IFS, des logs techniques IFS, du système Oracle géré par IFS et de l'espace alloué vide.

---

## 📊 Décomposition synthétique

| Catégorie | Volume | % | Responsable |
|-----------|--------|---|-------------|
| **Données métier client** (transactions, documents uploadés) | ~13 Go | 11 % | 👤 Nous |
| **Framework et métadonnées IFS** (UI Aurena, modèles, doc API) | ~12 Go | 10 % | 🏢 IFS |
| **Logs et audit IFS** (BPMN debug, IAM, événements) | ~10 Go | 8 % | 🏢 IFS |
| **Code PL/SQL IFS compilé** dans schéma SYS | ~9 Go | 7 % | 🏢 IFS |
| **Bug Oracle non purgé** (`WRI$_ADV_OBJECTS`) | ~11 Go | 9 % | 🏢 IFS (DBA) |
| **AWR / stats / dictionnaire Oracle** | ~7 Go | 6 % | 🏢 IFS (DBA) |
| **Traductions, profils, archives diverses IFS** | ~8 Go | 7 % | 🏢 IFS |
| **Espace alloué vide** (datafiles non remplis) | ~20 Go | 16 % | 🏢 IFS (DBA) |
| **TEMP / UNDO / redo logs** (estimation) | ~22 Go | 18 % | 🏢 IFS (DBA) |
| **Autres petits schémas Oracle** | ~10 Go | 8 % | 🏢 IFS |
| **TOTAL** | **122 Go** | 100 % | |

---

## 🔑 Points clés pour la négociation

1. **Seuls 11 % du volume sont réellement nos données métier.** Le ratio "données utiles / volume facturé" est anormalement bas.

2. **~10,9 Go sont occupés par une table de bug Oracle connu** (`WRI$_ADV_OBJECTS` — stockage du SQL Tuning Advisor non purgé). C'est un défaut d'administration côté IFS, pas un usage légitime de la BDD.

3. **~9 Go correspondent au code PL/SQL d'IFS lui-même** (packages, procédures stockées). Nous payons pour stocker leur propre code applicatif.

4. **~20 Go d'espace alloué mais vide** dans les datafiles. C'est de la sur-allocation côté IFS qu'ils nous facturent.

5. **~22 Go de structures Oracle techniques** (TEMP, UNDO, redo, archives) qui sont la responsabilité d'administration IFS et non liés à notre usage.

6. **Plan de purge identifié → gain potentiel de ~30 Go** sans toucher à aucune donnée métier (cf. document `03_Plan_purge.md`).

---

## 🎯 Demande à formuler à IFS

> *"Avant toute facturation supplémentaire, nous demandons :*
> 1. *La purge de `WRI$_ADV_OBJECTS` (10,9 Go récupérables immédiatement) ;*
> 2. *Une revue de la rétention AWR et de l'espace UNDO alloué ;*
> 3. *Une procédure officielle de purge sur `FND_MODEL_*`, `BPMN_DEBUG_*`, `IAM_LOGIN_EVENT_*` et `LANGUAGE_FILE_IMPORT_TAB` ;*
> 4. *Une clarification de la base de calcul de la facturation : volume total alloué, volume utilisé tous schémas confondus, ou volume métier client uniquement ?"*

---

## 📁 Documents de référence joints

| Fichier | Contenu |
|---------|---------|
| `00_Synthese_executive.md` | Ce document |
| `01_Analyse_volumetrie_complete.md` | Analyse technique détaillée par tablespace, schéma, segment |
| `02_Responsabilite_volumes.md` | **⭐ Document clé** — Qui génère quoi (nous vs IFS vs Oracle) |
| `03_Plan_purge.md` | Plan d'action de purge — gains estimés ~30 Go |
| `04_Argumentaire_negociation_IFS.md` | Arguments structurés pour la négociation |
