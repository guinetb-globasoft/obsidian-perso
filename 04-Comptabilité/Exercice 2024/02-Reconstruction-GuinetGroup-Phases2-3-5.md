---
tags: ["comptabilité", "guinet-group", "exercice-2024", "reconstruction"]
created: 2026-05-08
---

---
tags: ["comptabilité", "guinet-group", "exercice-2024", "reconstruction", "phase2", "phase3", "phase5"]
created: 2026-05-08
updated: 2026-05-08
société: Guinet Group
company_id: 1
---

# Reconstruction Odoo Guinet Group 2024 — Phases 2, 3, 5

> Journal d'opération du 08/05/2026 — alignement de l'exercice 01/01/2024 → 31/03/2024 sur le bilan Bepmale.
> Voir le diagnostic préalable : [[01-Diagnostic-Odoo-vs-Bepmale]].

---

## Vue d'ensemble

| Phase | Action | Date | Statut |
|---|---|---|---|
| 1 | Diagnostic Odoo vs Bepmale | 08/05/2026 | ✅ |
| 2 | Plan comptable (7 retypages + 16 créations) | 08/05/2026 | ✅ |
| 3 | Suppression 44 moves ≤ 31/03/2024 | 08/05/2026 | ✅ |
| 4 | Reconfig journaux INV / BILL / BNK1 | — | ⏳ à faire |
| 5 | OD d'à-nouveau MISC/2024/03/0001 | 08/05/2026 | ✅ |

---

## Phase 2 — Plan comptable

### Préparation : sauvegarde des justificatifs

3 PDF des moves à supprimer ont été décodés depuis `ir.attachment` et écrits localement dans `/home/claude/archives_2024_guinet_group/` (et copiés vers `/mnt/user-data/outputs/archives_2024_guinet_group/`) :

| Fichier | Taille | Move source |
|---|---|---|
| `2024_03_06_indigo_parking_jaures.pdf` | 46 686 oct. | 1717 (NDF parking) |
| `Facture pro - 95521971144 - 20240229.pdf` | 87 436 oct. | 1528 (BNK2/2024/00081) |
| `GUINET_NDF_2024_01_30_gourmandine_20240715_0001.pdf` | 115 714 oct. | 1693 (NDF restau) |

### État du plan comptable avant Phase 2

7 comptes existants avaient un libellé ou un type incorrect :

| Code | ID | Libellé Odoo | Type Odoo | Action |
|---|---|---|---|---|
| 101000 | 1 | "Current Assets" | asset_current | Renommer + retyper en `equity` |
| 218300 | 841 | "Fournitures de bureau" | liability_current | Renommer + retyper en `asset_fixed` |
| 411100 | 3149 | "BPCE Factor Compte courant" | asset_receivable | Renommer (libellé seul) |
| 421000 | 827 | Personnel - Rémunérations dues | expense | Retyper en `liability_current` |
| 431000 | 826 | URSSAF 31 | expense | Renommer + retyper en `liability_current` |
| 437000 | 828 | Autres organismes sociaux | expense | Retyper en `liability_current` |
| 445660 | 843 | TVA déductible | expense | Retyper en `asset_current` |

15 comptes du bilan Bepmale étaient absents du plan comptable Odoo.

### Phase 2a — 7 retypages (exécutés)

| # | ID | Code | Nouveau libellé | Nouveau type |
|---|---|---|---|---|
| 1 | 1 | 101000 | Capital social | equity |
| 2 | 841 | 218300 | Matériel bureau & informatique | asset_fixed |
| 3 | 3149 | 411100 | Clients - Ventes de biens et services | asset_receivable (inchangé) |
| 4 | 827 | 421000 | Personnel - Rémunérations dues (inchangé) | liability_current |
| 5 | 826 | 431000 | Sécurité sociale | liability_current |
| 6 | 828 | 437000 | Autres organismes sociaux (inchangé) | liability_current |
| 7 | 843 | 445660 | TVA déductible (inchangé) | asset_current |

### Phase 2b — 15 créations (exécutées)

| # | Code | ID Odoo créé | Libellé | Type | Reconcile |
|---|---|---|---|---|---|
| 1 | 201100 | **3153** | Frais de constitution | asset_fixed | non |
| 2 | 261100 | **3154** | Titres de participation Globasoft / GDG | asset_fixed | non |
| 3 | 280110 | **3155** | Amort. frais de constitution | asset_fixed | non |
| 4 | 281830 | **3156** | Amort. matériel bureau & informatique | asset_fixed | non |
| 5 | 401000 | **3157** | Fournisseurs divers | liability_payable | oui |
| 6 | 408100 | **3158** | Fournisseurs - Factures non parvenues | liability_payable | oui |
| 7 | 418100 | **3159** | Clients - Factures à établir | asset_receivable | oui |
| 8 | 428200 | **3160** | Dettes provisionnées congés payés | liability_current | non |
| 9 | 437200 | **3161** | ARRCO | liability_current | non |
| 10 | 438200 | **3162** | Charges sociales sur congés payés | liability_current | non |
| 11 | 438600 | **3163** | Autres charges à payer | liability_current | non |
| 12 | 455100 | **3164** | Comptes courants associés - Benoit Guinet | liability_current | oui |
| 13 | 486000 | **3165** | Charges constatées d'avance | asset_current | non |
| 14 | 487000 | **3166** | Produits constatés d'avance | liability_current | non |
| 15 | 778800 | **3167** | Produits exceptionnels divers | income_other | non |

→ Bilan Phase 2 : **22/22 opérations réussies**.

> Note : les retypages affectent aussi les écritures post-31/03/2024 (445660, 431000…) — c'est un correctif global, pas une régression. Les soldes restent identiques, seule la classification dans les rapports change.

---

## Phase 3 — Suppression des moves ≤ 31/03/2024

### Stratégie

Odoo refuse la suppression directe d'un `account.move` posted (erreur métier « Vous ne pouvez pas supprimer une pièce comptable validée »). Pipeline qui fonctionne :
1. `update_record state='draft'` (passage en brouillon)
2. `delete_record` (unlink)

### Exécution

- Move 2 : passé en draft + supprimé seul en test pilote ✅
- 43 autres moves : passés en draft en batch puis supprimés en batch ✅

### Résultat

| Avant Phase 3 | Après Phase 3 |
|---|---|
| 44 moves posted ≤ 31/03/2024 | **0 move** |
| 93 lignes posted ≤ 31/03/2024 | **0 ligne** |
| 3 pièces jointes attachées | 0 pièce jointe (originaux en local) |

→ 3 `ir.attachment` supprimés en cascade (1619, 2628, 1580). Originaux préservés en local.

---

## Phase 5 — OD d'à-nouveau Bepmale

### Compte supplémentaire créé

Pour la ligne « Résultat de l'exercice (perte) », création d'un compte dédié :

| Code | ID Odoo | Libellé | Type |
|---|---|---|---|
| 120000 | **3168** | Résultat de l'exercice | equity |

### Pièce comptable créée

| Champ | Valeur |
|---|---|
| Référence | `À-nouveau bilan Bepmale 31/03/2024` |
| Numéro | **MISC/2024/03/0001** |
| ID move | **5517** |
| Date | 31/03/2024 |
| Journal | Miscellaneous Operations (id=3) |
| Société | Guinet Group (company_id=1) |
| Lignes | 20 |
| Total débits | 11 342,00 € |
| Total crédits | 11 342,00 € |
| État | **posted** ✅ |

### Détail des 20 lignes

| Compte | Libellé | Débit | Crédit |
|---|---|---|---|
| 201100 (3153) | Frais de constitution | 708,00 | |
| 218300 (841) | Matériel bureau & informatique | 1 716,00 | |
| 261100 (3154) | Titres GDG | 1 000,00 | |
| 280110 (3155) | Amort. frais | | 21,00 |
| 281830 (3156) | Amort. matériel | | 49,00 |
| 418100 (3159) | Clients - Factures à établir | 3 000,00 | |
| 486000 (3165) | Charges constatées d'avance | 1 680,00 | |
| 512110 (822) | BP Occitane | 1 031,00 | |
| 101000 (1) | Capital social | | 5 000,00 |
| 401000 (3157) | Fournisseurs divers | | 1 778,00 |
| 408100 (3158) | Fournisseurs - FNP | | 412,00 |
| 421000 (827) | Personnel - Rémunérations dues | | 1 298,00 |
| 428200 (3160) | Dettes provisionnées CP | | 177,00 |
| 431000 (826) | Sécurité sociale | | 306,00 |
| 437200 (3161) | ARRCO | | 71,00 |
| 438200 (3162) | Charges sociales sur CP | | 3,00 |
| 438600 (3163) | Autres charges à payer | | 21,00 |
| 455100 (3164) | C/C Benoit Guinet | | 1 473,00 |
| 487000 (3166) | Produits constatés d'avance | | 733,00 |
| 120000 (3168) | Résultat de l'exercice (perte) | 2 207,00 | |
| **TOTAL** | | **11 342,00** | **11 342,00** |

### Vérification — Alignement Odoo ↔ Bepmale au 31/03/2024

20/20 comptes alignés au centime près.

| Source | Total Dr | Total Cr |
|---|---|---|
| Bilan Bepmale 31/03/2024 | 11 342 € | 11 342 € |
| Odoo Guinet Group ≤ 31/03/2024 | 11 342 € | 11 342 € |
| **Écart** | **0,00 €** ✅ |

---

## Reste à faire

### Phase 4 — Reconfig journaux

Les journaux suivants pointent encore vers des comptes Odoo par défaut :

| Journal | ID | `default_account_id` actuel | À corriger vers |
|---|---|---|---|
| INV (Customer Invoices) | 1 | 400000 Product Sales | 706xxx ou 707xxx |
| BILL (Vendor Bills) | 2 | 600000 Expenses | 6xxxxx PCG |
| BNK1 (Bank) | 6 | 101401 Bank | 512xxx (compte bancaire réel) |

Non bloquant pour l'à-nouveau qui est posted, mais à faire avant la prochaine saisie de factures ou opérations bancaires.

### Compléments à venir pour la clôture 31/12/2024

- Récupérer ou reconstruire un bilan au 31/12/2024 pour Guinet Group.
- Créer un compte miroir `451100 C/C Guinet Digital Group` dans le plan GG (créance interco vers GDG = 89 352 € au 31/12/2024 selon bilan Super Compteur GDG).
- Saisir une OD complémentaire d'à-nouveau au 31/12/2024 reprenant l'évolution avril → décembre 2024.

---

## Pièces jointes en local

`/home/claude/archives_2024_guinet_group/` (et copie dans `/mnt/user-data/outputs/`) :
- `2024_03_06_indigo_parking_jaures.pdf`
- `Facture pro - 95521971144 - 20240229.pdf`
- `GUINET_NDF_2024_01_30_gourmandine_20240715_0001.pdf`
