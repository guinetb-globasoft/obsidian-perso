---
titre: Réconciliation référentiel ↔ Talend PROD
statut: analysé — corrections à porter dans l'Excel
date: 2026-08-13
source: 03-Talend-PROD-inventaire.csv (31 tâches, relevé du 13/08/2026)
tags: [talend, tmc, referentiel, reconciliation, verite-terrain]
---

# Réconciliation référentiel ↔ Talend PROD

> Retour de l'IA connectée à Talend, **recoupé avec l'inventaire**. Deux de ses conclusions
> sont corrigées ici : la liste des « orphelines » et le verdict sur la question 4.

## Ce qui est confirmé

**31 tâches en PROD** : 17 actives, 14 en pause. 25 portent un code `INT-xxx`, 6 sont des
utilitaires techniques (nettoyage de dépôt, jeton d'API, table de correspondance) qui **ne
doivent pas entrer** au référentiel des flux. 16 codes INT distincts tournent réellement.

## ⚠️ Correction n°1 — les « 9 orphelines à créer » n'existent pas

L'IA conclut que `INT-234, 251, 252, 253, 255, 256, 257, 258, 269` sont absents du référentiel
et à créer. **Les 9 sont présents dans l'onglet FLUX.** L'erreur vient de moi : je ne lui avais
transmis que les **37 flux IFS**, pas les 250 lignes. Elle a donc lu « absent de la liste
fournie » comme « absent du référentiel ».

Rien à créer, mais **deux découvertes** dans ces 9 :

| Code | Déclaré | Réalité Talend | Lecture |
|---|---|---|---|
| `INT-234-Achats-IFS` | **Décommissionné**, Talend Oui | tâche `INT_234_main_ifs_esker_statut_paiement` **active**, ~600 exec | Un flux dit mort porte une tâche parmi les plus sollicitées |
| `INT-269-COMPTA-ESKER` | Décommissionné | tâche présente, cron défini, **jamais exécutée**, en pause | Cohérent : reliquat non nettoyé |

### L'hypothèse INT-259 / INT-234

La tâche s'appelle `INT_234_main_ifs_esker_statut_paiement` : **IFS → ESKER, statut de paiement**.
C'est mot pour mot la définition de `INT-259-IFS-ESKER « Statut du paiement »` (déclaré Actif),
et **pas** celle de `INT-234-Achats-IFS` (Achats → IFS, décommissionné).

→ **Hypothèse : la tâche porte un code obsolète.** Le flux réel est INT-259 ; INT-234 a été
recyclé sans renommage. À confirmer avec la TMA avant de toucher au référentiel — mais si c'est
le cas, INT-259 n'est pas « sans tâche Talend », il en a une, mal nommée.

## ⚠️ Correction n°2 — le verdict sur « tout passe par Talend »

L'IA écrit que *« 21 flux IFS déclarés n'ont aucune tâche Talend, ce qui contredit frontalement
l'affirmation »*. **Le raisonnement ne tient pas** : sur ces 21, **19 sont au statut « A venir »**.
Un flux pas encore construit n'a évidemment pas de tâche — ça ne dit rien sur la façon dont il
sera implémenté.

Le test valable ne porte que sur les flux **déclarés Actifs** :

| Flux IFS déclarés Actifs | 9 |
|---|---:|
| dont confirmés avec une tâche Talend en PROD | **6** |
| dont **sans aucune tâche Talend** | **3** |

Les trois exceptions :

| Code | Flux | À vérifier |
|---|---|---|
| `INT-140` | ProjetCommercial → IFS (informations chantiers) | Colonne « Géré avec Talend » = Non explicitement. Reprise native IFS ? dépôt de fichier ? |
| `INT-275` | IFS → QDV (articles) | QDV va-t-il chercher lui-même ? |
| `INT-276` | IFS → QDV (prix des articles) | idem |

→ **Verdict nuancé** : l'affirmation est vraie à **6 sur 9**. Elle n'est pas « frontalement
contredite », mais elle n'est pas exacte non plus. Trois flux actifs à instruire — et c'est
hors de Talend qu'il faut chercher, comme l'IA le souligne à juste titre.

## Les corrections à porter dans l'Excel

### A. Colonne « Géré avec Talend » — 5 flux à passer à Oui

`INT-199` · `INT-225` · `INT-251` · `INT-253` · `INT-255`

*(et non 25 comme je le supposais : la plupart des flux IFS non marqués ne sont pas encore
construits)*

### B. Colonne « Statut » — 7 flux qui tournent avec un statut faux

| Code | Déclaré | À passer à | Cadence réelle en PROD |
|---|---|---|---|
| `INT-199` | A venir | **Actif** | toutes les 5 min, 7h-20h, lun-ven (~168/jour) |
| `INT-209` | A venir | **Actif** | toutes les 5 min, 12 h/j (~144/jour) |
| `INT-213` | A venir | **Actif** | toutes les 10 min (~72/jour) |
| `INT-222` | A venir | **Actif** | toutes les 5 min, 14 h/j (~168/jour) |
| `INT-225` | A venir | **Actif** | 2 fois par jour (13h et 18h) |
| `INT-255` | A venir | **Actif** | toutes les 10 min (~72/jour) |
| `INT-234` | Décommissionné | **Actif** (ou fusion INT-259) | permanent |

> **C'est l'écart le plus coûteux en crédibilité.** `INT-199` (virements vers Sage Signature)
> et `INT-225` (écritures de vente Infor → IFS) tournent depuis des mois en production alors
> que le référentiel les annonce « à venir ». Toute personne qui connaît le terrain perd
> confiance dans le document entier en voyant ça.

### C. Colonnes techniques — enfin remplissables

Le CSV apporte, pour 17 tâches actives, ce que le référentiel n'avait pas : **cron exact,
fuseau (Europe/Paris), protocole, ressources, moteur**. Protocoles observés :
`REST + SFTP` (11), `BDD + SFTP` (6), `BDD + REST + SFTP` (6), `SFTP` (2), `REST` (1).
→ Le taux de remplissage « protocole » passe de **26/132** à environ **43/132**.

### D. Ce qu'il ne faut PAS verser au référentiel

Les 6 utilitaires : `clean_repo_logs`, `clean_repo_cls`, `clean_repo INT_185`,
`clean_repo_INIT_233`, `job_tester_bdd_mntr`, `call_api_get_token`,
`main_miseAjour_baseCorrespondance`. Ce ne sont pas des interfaces métier.

## Un signal à ne pas laisser passer

`main_miseAjour_baseCorrespondance` — **3 échecs sur 10 (30 %)**, dernière erreur
`tRunJob_1 → java.lang.RuntimeException: Child job running failed`.

Cette tâche met à jour la **table de correspondance** (transcodification). Or il existe un
défaut connu sur `INT-199` : le virement est rejeté quand le nom de banque du fichier contient
des `_` au lieu d'espaces, et **l'échec est invisible en monitoring** parce que `log_transco`
ne journalise que les succès (cf. [[int199-transco-silent-fail]] en mémoire projet).

→ Une table de correspondance qui échoue à se mettre à jour une fois sur trois, alimentant un
flux de virements qui tourne toutes les 5 minutes et dont les échecs de transco sont muets :
**c'est un risque financier, pas un sujet de cartographie**. À sortir du périmètre carto et à
traiter comme un incident.

## Sur les volumes — ne pas citer les comptages bruts

12 tâches ont un comptage **plafonné à 600** sur une fenêtre réelle de 5 à 10 jours
(l'API TMC pagine par 100 sans filtre de date). Les colonnes `fenetre_depuis` et
`comptage_tronque` du CSV le signalent — l'IA a eu raison de les ajouter.

**Ne jamais publier « 600 exécutions ».** La bonne mesure est la **cadence lue dans le cron**,
qui est exacte et parlante : « toutes les 5 minutes, 7h-20h, du lundi au vendredi ».

## Erreur de modélisation corrigée le 13/08 — le troisième état manquant

Les artefacts ne connaissaient que **deux états** : « en place » et « en cours de mise en
place ». Il en manquait un : **« ressaisie manuelle, rien d'engagé »**.

Conséquence : `INT-002` (liasse fiscale) et `INT-003` (consolidation), au statut *A prévoir*
avec `process = "?"` et `informations transmises = "?"` — c'est-à-dire des lignes où personne
n'a même défini ce qui circulerait — étaient affichées comme *« en cours de mise en place »*.
C'était faux, et inventé par le modèle d'affichage, pas par la donnée.

La réalité, documentée dans l'onglet **APPS - Focus FINANCE KMPG** du même fichier :

| Application | Ce que dit l'inventaire |
|---|---|
| `BilanETAFI` (YourCegid) | « saisie manuelle de la liasse pour intégration fiscale » |
| `viareport` | « Interface manuelle d'intégration des balances à partir de la compta » + « saisie manuelle des liasses (Ossabois) » |

**Corrections apportées :**

- **Page collaborateurs** : la famille « Clôture et pilotage » est retirée du schéma des
  échanges (5 familles au lieu de 6) — une ressaisie n'est pas un échange entre applications.
  Un bloc distinct **« Ce qui reste manuel »** dit les choses en clair.
- **Page DSI** : le groupe devient « Clôture & consolidation — aucune interface, ressaisie
  manuelle », **sans connecteur vers IFS**, avec un troisième symbole (✋) ajouté à la légende.
- La ligne « Power BI / Qlik Sense · restitution » est supprimée : elle ne correspondait à
  aucune ligne du référentiel des flux.

**Leçon pour la suite** : le référentiel distingue `A venir` (engagé) de `A prévoir`
(souhaité, non spécifié). Toute représentation qui écrase cette nuance transforme une intention
en projet. Les deux statuts doivent rester distincts dans les vues.

## Suites

- [ ] Confirmer l'hypothèse INT-259 / INT-234 avec la TMA avant correction
- [ ] Instruire les 3 flux actifs sans tâche Talend (INT-140, 275, 276) — hors Talend
- [ ] Porter les corrections A, B, C dans l'Excel
- [ ] Traiter `main_miseAjour_baseCorrespondance` comme un incident, pas comme une ligne de carto
- [x] Corriger les deux artefacts (voir [[03-Cartographies/01-Les-deux-vues-produites]])
