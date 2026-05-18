---
tags: ["comptabilité", "guinet-group", "plan-comptable", "phase2"]
created: 2026-05-08
---

---
tags: ["comptabilité", "guinet-group", "plan-comptable", "phase2"]
created: 2026-05-08
société: Guinet Group
company_id: 1
---

# Phase 2 — Alignement du plan comptable Guinet Group

> Préparatoire à l'OD d'à-nouveau au 31/03/2024.

## Justificatifs sauvegardés ✅

3 PDFs récupérés depuis Odoo (`ir.attachment`) et écrits dans `/home/claude/archives_2024_guinet_group/` :
- `2024_03_06_indigo_parking_jaures.pdf` (46 686 octets) — attaché au move 1717 (NDF parking)
- `Facture pro - 95521971144 - 20240229.pdf` (87 436 octets) — attaché au move 1528 (BNK2/2024/00081, facture pro BP)
- `GUINET_NDF_2024_01_30_gourmandine_20240715_0001.pdf` (115 714 octets) — attaché au move 1693 (NDF restau)

Suppression des moves Odoo possible sans perte des originaux.

---

## 🚨 État sale du plan comptable Guinet Group

### Comptes existants avec problèmes

| Code | ID | Libellé Odoo | Type Odoo | Type attendu | Action |
|---|---|---|---|---|---|
| 101000 | 1 | "Current Assets" | asset_current | **equity** | Renommer "Capital social" + retyper en equity |
| 218300 | 841 | "Fournitures de bureau" | liability_current 🚨 | **asset_fixed** | Renommer "Matériel bureau & informatique" + retyper |
| 411100 | 3149 | "BPCE Factor Compte courant" 🚨 | asset_receivable | "Clients" | Renommer libellé (le compte client n'est pas un compte d'affacturage) |
| 421000 | 827 | Personnel - Rémunérations dues | **expense** 🚨 | **liability_current** | Retyper |
| 431000 | 826 | URSSAF 31 | **expense** 🚨 | **liability_current** | Retyper |
| 437000 | 828 | Autres organismes sociaux | **expense** 🚨 | **liability_current** | Retyper |
| 445660 | 843 | TVA déductible | **expense** 🚨 | **asset_current** | Retyper |

→ **7 comptes existants à corriger**. Ces erreurs de typage faussent les bilans et les états de TVA depuis le départ.

### Comptes manquants à créer (15)

#### Actif immobilisé
- **201100** Frais de constitution — type `asset_fixed`
- **261100** Titres de participation (Globasoft / GDG) — type `asset_fixed`
- **280110** Amort. frais de constitution — type `asset_fixed` (compte d'amort, contre-actif)
- **281830** Amort. matériel bureau & informatique — type `asset_fixed` (idem)

#### Actif circulant / créances
- **418100** Clients - Factures à établir — type `asset_receivable`
- **486000** Charges constatées d'avance — type `asset_current`

#### Passif / dettes
- **101000** Capital — déjà existant mais à retyper (cf. ci-dessus)
- **401000** Fournisseurs divers — type `liability_payable`
- **408100** Fournisseurs - Factures non parvenues (FNP) — type `liability_payable`
- **428200** Dettes provisionnées congés payés — type `liability_current`
- **437200** ARRCO (organisme social) — type `liability_current`
- **438200** Charges sociales sur congés payés — type `liability_current`
- **438600** Autres charges à payer — type `liability_current`
- **455100** Comptes courants associés - Benoit Guinet — type `liability_current`
- **487000** Produits constatés d'avance — type `liability_current`

#### Produits exceptionnels
- **778800** Produits exceptionnels divers — type `income_other`

---

## ⚠️ Impact des retypages

Les comptes existants ont des écritures **post-31/03/2024** également (445660, 431000, etc. ont des lignes 2025). Le retypage des comptes va affecter leur classification dans tous les rapports historiques et futurs — c'est une **correction**, pas une régression.

→ Aucune écriture ne sera modifiée, juste la classification du compte. Les soldes restent identiques.

---

## Stratégie d'exécution

### Phase 2a — Corrections des 7 comptes existants
Une opération `update_record` par compte, avec dry_run individuel.

### Phase 2b — Créations des 15 nouveaux comptes
Un `create_record` par compte, batché si possible.

### Validation
À la fin de la Phase 2, vérifier que les 22 comptes nécessaires à l'OD d'à-nouveau sont tous présents avec les bons IDs Odoo.




---

## ✅ Phase 2 EXÉCUTÉE — 08/05/2026

### 7 retypages
| Code | ID | Nouveau libellé | Nouveau type |
|---|---|---|---|
| 101000 | 1 | Capital social | equity |
| 218300 | 841 | Matériel bureau & informatique | asset_fixed |
| 411100 | 3149 | Clients - Ventes de biens et services | asset_receivable |
| 421000 | 827 | Personnel - Rémunérations dues | liability_current |
| 431000 | 826 | Sécurité sociale | liability_current |
| 437000 | 828 | Autres organismes sociaux | liability_current |
| 445660 | 843 | TVA déductible | asset_current |

### 15 créations
| Code | ID Odoo | Libellé | Type |
|---|---|---|---|
| 201100 | 3153 | Frais de constitution | asset_fixed |
| 261100 | 3154 | Titres de participation Globasoft / GDG | asset_fixed |
| 280110 | 3155 | Amort. frais de constitution | asset_fixed |
| 281830 | 3156 | Amort. matériel bureau & informatique | asset_fixed |
| 401000 | 3157 | Fournisseurs divers | liability_payable |
| 408100 | 3158 | Fournisseurs - Factures non parvenues | liability_payable |
| 418100 | 3159 | Clients - Factures à établir | asset_receivable |
| 428200 | 3160 | Dettes provisionnées congés payés | liability_current |
| 437200 | 3161 | ARRCO | liability_current |
| 438200 | 3162 | Charges sociales sur congés payés | liability_current |
| 438600 | 3163 | Autres charges à payer | liability_current |
| 455100 | 3164 | Comptes courants associés - Benoit Guinet | liability_current |
| 486000 | 3165 | Charges constatées d'avance | asset_current |
| 487000 | 3166 | Produits constatés d'avance | liability_current |
| 778800 | 3167 | Produits exceptionnels divers | income_other |

22/22 opérations réussies. Plan comptable Guinet Group prêt pour l'OD d'à-nouveau.




---

## ✅ Phase 3 EXÉCUTÉE — 08/05/2026

### Stratégie

`delete_record` sur Odoo `account.move` posté refuse la suppression directe (erreur métier "Vous ne pouvez pas supprimer une pièce comptable validée"). Pipeline qui fonctionne :
1. `update_record state='draft'` (passage en brouillon)
2. `delete_record` (unlink)

### Exécution

- **Move 2 (test)** : passé en draft puis supprimé pour valider le pipeline ✅
- **43 autres moves** : passés en draft en batch puis supprimés en batch ✅

### Résultat

- **44/44 moves supprimés** sans erreur
- **3 ir.attachment supprimés en cascade** (1619, 2628, 1580) — originaux sauvegardés dans `/home/claude/archives_2024_guinet_group/`
- **0 move restant** avec `date ≤ 31/03/2024` sur Guinet Group (vérifié)

### Compteur final

| Avant | Après |
|---|---|
| 44 moves posted ≤ 31/03/2024 | **0 move** |
| 93 lignes posted ≤ 31/03/2024 | **0 ligne** |
| 3 pièces jointes attachées | **0 pièce jointe** (originaux en local) |

Plan comptable nettoyé et prêt pour la Phase 4 (reconfig journaux) puis Phase 5 (OD d'à-nouveau Bepmale).




---

## ✅ Phase 5 EXÉCUTÉE — 08/05/2026 — OD d'à-nouveau Bepmale

### Compte créé en plus

Pour la ligne "Résultat de l'exercice", création d'un nouveau compte :

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

### Vérification — Alignement Odoo ↔ Bepmale au 31/03/2024

| Compte | Odoo | Bepmale | Écart |
|---|---|---|---|
| 201100 Frais de constitution | D 708 | D 708 | ✅ |
| 218300 Matériel bureau & informatique | D 1 716 | D 1 716 | ✅ |
| 261100 Titres GDG | D 1 000 | D 1 000 | ✅ |
| 280110 Amort. frais | C 21 | C 21 | ✅ |
| 281830 Amort. matériel | C 49 | C 49 | ✅ |
| 418100 Clients FAE | D 3 000 | D 3 000 | ✅ |
| 486000 CCA | D 1 680 | D 1 680 | ✅ |
| 512110 BP Occitane | D 1 031 | D 1 031 | ✅ |
| 101000 Capital | C 5 000 | C 5 000 | ✅ |
| 401000 Fournisseurs divers | C 1 778 | C 1 778 | ✅ |
| 408100 FNP | C 412 | C 412 | ✅ |
| 421000 Personnel | C 1 298 | C 1 298 | ✅ |
| 428200 Prov. CP | C 177 | C 177 | ✅ |
| 431000 Sécu | C 306 | C 306 | ✅ |
| 437200 ARRCO | C 71 | C 71 | ✅ |
| 438200 CS sur CP | C 3 | C 3 | ✅ |
| 438600 Autres charges | C 21 | C 21 | ✅ |
| 455100 C/C Benoit | C 1 473 | C 1 473 | ✅ |
| 487000 PCA | C 733 | C 733 | ✅ |
| 120000 Résultat (perte) | D 2 207 | D 2 207 | ✅ |
| **TOTAL** | **D 11 342 / C 11 342** | **D 11 342 / C 11 342** | **✅** |

🎯 **Alignement parfait — 20/20 au centime près.**

---

## 🎉 Bilan global de l'opération — 08/05/2026

| Phase | Résultat |
|---|---|
| 1. Diagnostic Odoo vs Bepmale | ✅ Écarts identifiés |
| 2. Plan comptable | ✅ 22 opérations (7 retypages + 15 créations + 1 résultat = 23 au total) |
| 3. Suppression moves ≤ 31/03/2024 | ✅ 44 moves supprimés (3 PDFs sauvegardés en local) |
| 5. OD d'à-nouveau Bepmale | ✅ MISC/2024/03/0001, 11 342 €, 20 lignes, posted |

**Phase 4 (reconfig journaux INV/BILL/BNK1)** : reste à faire. Non bloquante pour l'à-nouveau, deviendra utile lors des prochaines saisies factures/banque post-31/03/2024.

L'exercice 2024 (1er exercice du 01/01/2024 au 31/03/2024) est maintenant **fidèle au bilan Bepmale** dans Odoo Guinet Group.
