---
titre: Brief Claude Excel — mise à jour de l'onglet FLUX inter-APPS
statut: à exécuter
date: 2026-08-18
cible: INVENTAIRE - Applicatifs Métier.xlsx, onglet « FLUX inter-APPS »
tags: [referentiel, excel, brief, flux, correction]
---

# Brief Claude Excel — onglet « FLUX inter-APPS »

> Origine des corrections : relevé de la plateforme **Talend en production du 18/08/2026**
> (31 tâches) recoupé avec l'inventaire, plus les confirmations terrain de Benoît Guinet.
> Détail et justification dans [[01-Referentiel/02-Reconciliation-Talend-PROD]] et [[01-Referentiel/03-Perimetre-ERP-reel]].
>
> **29 modifications de cellules sur 28 lignes.** Aucune ligne à créer, aucune à supprimer.

---

## ⬇️ À COPIER À PARTIR D'ICI ⬇️

Tu vas mettre à jour un onglet d'un classeur Excel de référentiel d'interfaces.
Lis **toutes** les règles avant de commencer.

### Règles impératives

1. **Travaille sur une copie**, ou vérifie qu'une sauvegarde existe. Ce fichier est le
   référentiel de production de la DSI.
2. **Ne modifie que les cellules listées.** Aucune autre colonne, aucune autre ligne.
3. **Ne trie pas, ne filtre pas, ne reformate rien**, ne supprime ni n'insère de ligne.
   L'ordre des lignes doit rester identique.
4. **Vérifie la valeur actuelle avant d'écrire.** Chaque tableau donne la valeur attendue
   avant modification. **Si la valeur actuelle ne correspond pas, n'écris pas** : note la
   ligne et signale-la dans ton compte rendu. Une divergence signifie que quelqu'un est
   passé après moi.
5. **Respecte l'orthographe exacte** des valeurs cibles, accents compris. Elles doivent
   correspondre à la liste de l'onglet « Liste de valeurs flux ».
6. Si une ligne listée est **introuvable**, ne crée rien : signale-la.

### Repérage

- **Onglet** : `FLUX inter-APPS`
- **Ligne d'en-tête** : ligne 1. **Les données commencent ligne 2.**
- **Repère les colonnes par leur libellé d'en-tête**, pas par leur lettre. Les lettres
  ci-dessous sont ce que j'attends — **confirme-les avant d'écrire** et signale tout écart :

| Libellé d'en-tête | Lettre attendue |
|---|---|
| `Code` | **A** |
| `Géré avec Talend ?` | **J** |
| `Statut` | **N** |
| `Commentaires` | **AO** |

### Règle d'identification des lignes

La colonne `Code` contient des libellés complets du type
`INT-199-IFS-Sage Signature`. **Identifie chaque ligne par son code exact**, tel qu'il est
donné dans les tableaux ci-dessous.

⚠️ Si tu préfères faire une correspondance par préfixe, utilise **impérativement le tiret
final** : `INT-199-` et non `INT-199`, sinon tu risques d'attraper d'autres lignes.
Attention aussi : certains codes apparaissent **en double** dans l'onglet (INT-006, INT-012).
Aucun des codes ci-dessous n'est concerné, mais vérifie que tu ne modifies **qu'une seule
ligne par code**.

---

### Modification 1 — colonne `Statut` → `Actif` (7 lignes)

Ces flux **tournent en production**. Le référentiel les annonce encore « à venir ».

| Code exact (colonne A) | Valeur actuelle attendue | Écrire |
|---|---|---|
| `INT-199-IFS-Sage Signature` | A venir | `Actif` |
| `INT-209-Nibelis-IFS` | A venir | `Actif` |
| `INT-213-PaieGRH-IFS` | A venir | `Actif` |
| `INT-222-Infor Syteline (CSI)-IFS` | A venir | `Actif` |
| `INT-225-Infor Syteline (CSI)-IFS` | A venir | `Actif` |
| `INT-255-ESKER-Infor Syteline (CSI)` | A venir | `Actif` |
| `INT-260-Sage XRT Trésorerie-IFS` | A venir | `Actif` |

### Modification 2 — colonne `Géré avec Talend ?` → `Oui` (5 lignes)

Ces flux ont une tâche Talend active en production, non déclarée dans le référentiel.

| Code exact (colonne A) | Valeur actuelle attendue | Écrire |
|---|---|---|
| `INT-199-IFS-Sage Signature` | (vide) | `Oui` |
| `INT-225-Infor Syteline (CSI)-IFS` | (vide) | `Oui` |
| `INT-251-Infor Syteline (CSI)-ESKER` | (vide) | `Oui` |
| `INT-253-Infor Syteline (CSI)-ESKER` | (vide) | `Oui` |
| `INT-255-ESKER-Infor Syteline (CSI)` | (vide) | `Oui` |

### Modification 3 — colonne `Statut` → `Décommissionné` (16 lignes)

Deux causes : l'application **Achats** et **IBAT** n'existent plus, et l'ancienne chaîne
facture fournisseur `ZyScan → PROGIDOC → Compta` est entièrement basculée.

| Code exact (colonne A) | Valeur actuelle attendue | Écrire |
|---|---|---|
| `INT-008-Achats-InfoLégal` | Actif | `Décommissionné` |
| `INT-009-Achats-Compta` | Actif, à disparaitre | `Décommissionné` |
| `INT-010-Achats-DevisNomenclatures` | Actif, à disparaitre | `Décommissionné` |
| `INT-011-Achats-Factory` | Actif, à disparaitre | `Décommissionné` |
| `INT-024-Chantier-Achats` | Actif, à disparaitre | `Décommissionné` |
| `INT-035-Compta-Achats` | Actif, à disparaitre | `Décommissionné` |
| `INT-053-DevisNomenclatures-Achats` | Actif, à disparaitre | `Décommissionné` |
| `INT-074-Factory-Achats` | Actif, à disparaitre | `Décommissionné` |
| `INT-124-PAQ-Achats` | Actif, à disparaitre | `Décommissionné` |
| `INT-139-PROGIDOC-Compta` | Actif, à disparaitre | `Décommissionné` |
| `INT-141-ProjetCommercial-Achats` | Actif, à disparaitre | `Décommissionné` |
| `INT-171-ZyLab (ZyScan, ZyTimer, ZyIndex)-PROGIDOC` | Actif, à disparaitre | `Décommissionné` |
| `INT-172-Compta-PROGIDOC` | Actif, à disparaitre | `Décommissionné` |
| `INT-173-Achats-PROGIDOC` | Actif, à disparaitre | `Décommissionné` |
| `INT-174-Progidoc-Compta` | Actif, à disparaitre | `Décommissionné` |
| `INT-176-PROGIDOC-Compta` | Actif, à disparaitre | `Décommissionné` |

### Modification 4 — colonne `Statut` → `Inactif` (1 ligne)

Ce flux ne sera jamais réalisé — décision métier, il ne s'agit pas d'un report.

| Code exact (colonne A) | Valeur actuelle attendue | Écrire |
|---|---|---|
| `INT-211-DevisNomenclatures-IFS` | A venir | `Inactif` |

### Modification 5 — traçabilité (28 lignes)

Sur **chaque ligne modifiée**, ajoute à la fin de la colonne `Commentaires` (AO), à la suite
du texte existant s'il y en a un, précédé d'un espace :

```
[18/08/2026 - MAJ d'apres releve Talend PROD]
```

Ne remplace jamais le contenu existant de `Commentaires`, ajoute à la suite.

---

### Compte rendu attendu

À la fin, donne-moi :

1. **Le nombre de cellules effectivement modifiées** (attendu : 29 valeurs + 28 commentaires).
2. **La liste des lignes non modifiées** et pourquoi : code introuvable, ou valeur actuelle
   différente de celle attendue. C'est l'information la plus importante de ton compte rendu.
3. **Les écarts de lettres de colonnes** par rapport au tableau de repérage, s'il y en a.
4. Confirmation que **l'ordre des lignes et le nombre de lignes sont inchangés**.

## ⬆️ À COPIER JUSQU'ICI ⬆️

---

## Phase 2 — optionnelle, à faire dans un second temps

À ne lancer **qu'après validation de la phase 1**. Elle enrichit plutôt qu'elle ne corrige.

### 2a. Créer une colonne `Tâche Talend`

C'est **la colonne qui manque le plus** au référentiel : sans elle, aucun recoupement
automatique entre l'inventaire et la plateforme n'est possible, et toute la réconciliation
doit être refaite à la main.

À insérer **après** la colonne `Géré avec Talend ?` (J), et à remplir ainsi :

| Code (colonne A commence par) | `Tâche Talend` | `Support & Protocole` | `Fréquence` |
|---|---|---|---|
| `INT-185-` | `INT_185_IFS_ESKER_Fournisseurs` | BDD + REST + SFTP | 5 fois par jour (7h, 10h, 11h, 14h, 16h), lun-ven |
| `INT-187-` | `INT_187_188_main_esker_ifs_ecriture_comptable_lien_Lot4` | BDD + REST + SFTP | Toutes les 5 min, 14 h/j, lun-ven |
| `INT-189-` | `INT_189_sftp_ESKER_to_GA` | BDD + SFTP | non planifié (déclenché par la tâche amont) |
| `INT-199-` | `INT_199_main_sage_signature` | SFTP | Toutes les 5 min, 14 h/j, lun-ven |
| `INT-209-` | `INT_209_main_nibelis_ifs_odpaie` | BDD + REST + SFTP | Toutes les 5 min, 12 h/j, lun-ven |
| `INT-213-` | `INT_213_main_PaieGRH_IFS_ODANALYTIQUE` | REST + SFTP | Toutes les 10 min, 12 h/j, lun-ven |
| `INT-217-` | `INT_217_Exfiles_IFS` | BDD + REST + SFTP | Toutes les 10 min, 12 h/j, lun-ven |
| `INT-222-` | `INT_222_main_infor_ifs_AIH` | BDD + REST + SFTP | Toutes les 5 min, 14 h/j, lun-ven |
| `INT-225-` | `INT_225_main_infor_ifs_ecriture_vente` | REST + SFTP | 2 fois par jour (13h, 18h), lun-ven |
| `INT-233-` | `INT_233_main_ifs_esker_bnk` | BDD + REST + SFTP | 4 fois par jour (7h, 10h, 14h, 18h), lun-ven |
| `INT-251-` | `INT_251_252_256_257_258_Infor_esker` | BDD + SFTP | Toutes les 30 min, 13 h/j, lun-ven |
| `INT-252-` | `INT_251_252_256_257_258_Infor_esker` | BDD + SFTP | Toutes les 30 min, 13 h/j, lun-ven |
| `INT-253-` | `INT_253_Infor_esker_ERPACK` | BDD + SFTP | Toutes les 10 min, 12 h/j, lun-ven |
| `INT-255-` | `INT_255_Esker_Infor` | BDD + SFTP | Toutes les 10 min, 12 h/j, lun-ven |
| `INT-256-` | `INT_251_252_256_257_258_Infor_esker` | BDD + SFTP | Toutes les 30 min, 13 h/j, lun-ven |
| `INT-257-` | `INT_251_252_256_257_258_Infor_esker` | BDD + SFTP | Toutes les 30 min, 13 h/j, lun-ven |
| `INT-258-` | `INT_251_252_256_257_258_Infor_esker` | BDD + SFTP | Toutes les 30 min, 13 h/j, lun-ven |

> **Une tâche porte cinq flux** : `INT_251_252_256_257_258_Infor_esker`. C'est la preuve que
> la relation code ↔ tâche n'est pas 1 pour 1, et pourquoi le compteur « 61 flux actifs »
> compte des lignes de déclaration et non des interfaces déployées.

### 2b. Ajouter une colonne `Dernière vérification`

Date + initiales, au moins sur la colonne `Statut`. **C'est la recommandation de fond** :
une donnée sans date de fraîcheur est indistinguable d'une donnée fausse. C'est exactement
ce qui s'est produit ici — trois sources concordantes décrivant un SI d'il y a un an, sans
que rien ne le signale.

---

## Ce que je n'ai PAS mis dans le brief, et pourquoi

| Sujet                                 | Raison                                                                                                                                                                                                                                 |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `INT-234` : Décommissionné → Actif    | La tâche `INT_234_main_ifs_esker_statut_paiement` tourne, mais son libellé décrit `INT-259`. **Hypothèse de code obsolète à confirmer avec la TMA** avant toute écriture. Modifier maintenant risque de créer un doublon avec INT-259. |
| `INT-223` : retirer le « Oui » Talend | Déclaré Talend sans tâche, mais le flux n'est pas construit — le « Oui » peut être une intention légitime. À trancher avec la TMA.                                                                                                     |
| `INT-232` : statut                    | L'accusé de réception est produit **à l'intérieur** de la tâche INT-187-188, sans tâche dédiée. Le statut dépend de la convention retenue pour les flux portés par une autre tâche.                                                    |
| `INT-269`, tâches `_old`              | Nettoyage à faire **côté Talend**, pas côté référentiel.                                                                                                                                                                               |
| Les 6 utilitaires techniques          | `clean_repo_*`, `call_api_get_token`, `main_miseAjour_baseCorrespondance` ne sont pas des interfaces métier : ils n'ont pas leur place dans l'onglet FLUX.                                                                             |
|                                       |                                                                                                                                                                                                                                        |
