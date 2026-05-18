---
tags: ["comptabilité", "guinet-digital-group", "exercice-2024", "diagnostic", "phase1"]
created: 2026-05-08
---

---
tags: ["comptabilité", "guinet-digital-group", "exercice-2024", "diagnostic", "phase1"]
created: 2026-05-08
updated: 2026-05-08
société: Guinet Digital Group (ex-Globasoft)
company_id: 4
---

# Phase 1 — Diagnostic Odoo GDG vs Super Compteur

> Préalable à la reconstruction Odoo GDG 2024 alignée sur le bilan Super Compteur au 31/12/2024.
> Voir la liasse : [[03-Comptes-annuels-GDG-2024]].

---

## Volumétrie Odoo GDG ≤ 31/12/2024

| Indicateur | Valeur |
|---|---|
| Moves posted | **416** (après test pilote qui a supprimé 3 moves) |
| Lignes lettrées | **199** (sur **88 reconciles uniques**) |
| Première écriture | 29/02/2024 (in_invoice Vendor Bills) |
| Dernière écriture | 31/12/2024 (Bank) |
| Période effective | 11 mois (cohérent avec exercice Super Compteur 01/02→31/12/2024) |

### Répartition par journal (estimée)

| Journal | Approx. moves | Type |
|---|---|---|
| Bank (BNK1) | ~190 | Compte principal |
| GLOBASOFT XX7328 (BNK2) | ~75 | Compte secondaire |
| Vendor Bills (BILL) | ~60 | Factures fournisseurs |
| Cash Basis Taxes (CABA) | ~25 | TVA sur encaissements |
| Compte TVA | ~25 | OD TVA |
| Customer Invoices (FAC) | ~15 | Factures clients |
| Exchange Difference | ~5 | Différences de change |
| Salaries | ~1 | Paie |

> GDG est en **TVA sur encaissements** (présence du journal Cash Basis Taxes), confirmé par le 445872 « TVA collectée en attente » dans le bilan Super Compteur.

---

## Comparaison ordre de grandeur GG vs GDG

| Indicateur | Guinet Group | GDG | Ratio |
|---|---|---|---|
| Période | 3 mois | 11 mois | ×3,7 |
| Moves Odoo | 44 | 416 | ×9,5 |
| Lignes Odoo (estim.) | 93 | ~1 500–2 500 | ×16–27 |
| Lignes lettrées | 0 | 199 | ×∞ |
| Total bilan | 9 064 € | 155 561 € | ×17 |
| Pièces jointes (estim.) | 3 | ~25–50 | ×8–16 |

→ L'opération GDG est **~10× plus lourde que GG**.

---

## Test pilote TVA cash basis ✅

### Cas : FAC/2024/00001 Sohoft 1 080 €

Structure observée :
- FAC/2024/00001 (ID 1857) — 706000 Cr 900 + 411100 Dr 1 080 + **445740 « VAT collected on unsettled » Cr 180**
- Paiement BNK1/2024/00046 (ID 1930), reconcile 94 lettré avec la FAC
- Écriture **CABA/2024/04/0001 (ID 1935)** générée automatiquement au paiement : transfert 180 € de 445740 → 445710 (TVA collectée définitive)

### Pipeline validé

1. `update_record state='draft'` sur FAC → la facture passe en brouillon mais le reconcile reste lié
2. `delete_record` sur FAC → la suppression dissout naturellement le reconcile
3. CABA et BNK deviennent orphelins mais restent posted
4. `update_record state='draft'` + `delete_record` sur CABA et BNK → suppression OK

### Conséquences pour la Phase 3

- **Pas besoin de pré-délettrer** : passer en draft + supprimer dissout les reconciles
- Les CABA et BNK orphelins seront supprimés dans le même batch ≤ 31/12/2024 puisqu'ils ont la même date que la FAC
- Le pipeline éprouvé sur Guinet Group fonctionne aussi sur GDG malgré la TVA cash basis
- Mapping TVA en attente Odoo ↔ SAGE : **445740 (Odoo)** ↔ **445872 (SAGE)** — même rôle fonctionnel

---

## Analyse sélective des 88 reconciles

### Méthode

1. Liste des reconciles uniques sur les 199 lignes ≤ 31/12/2024 → **88 reconciles**
2. Pour chaque reconcile, récupération de **toutes** ses lignes (toutes années) → 207 lignes
3. Comparaison : 207 − 199 = **8 lignes en 2025**, réparties sur **5 reconciles bridges**

### 83 reconciles 100 % 2024 ✅

Délettrage automatique sans impact sur 2025 (par passage en draft + suppression). Aucune action préalable requise.

### 5 reconciles bridges 2024 ↔ 2025 ⚠️

| Reco | Type | Détail | Montant |
|---|---|---|---|
| 448 | FAC 2024 → paiement 2025 | FAC/2024/00023 Sohoft (01/12/2024) ↔ BNK1/2025/00005 (07/01/2025) | 1 174 € |
| 449 | FAC 2024 → paiement 2025 | FAC/2024/00022 Sohoft (01/12/2024) ↔ BNK1/2025/00004 (07/01/2025) | 12 506 € |
| 481 | Frais BPCE multi-année | 4 lignes 2024 BNK1 + 4 lignes 2025 (BNK1 + FACTU) sur 401 BPCE | ~6 € (négligeable) |
| 513 | FACTU 2024 → paiement 2025 | Gandi FACTU/2024/10/0001 (11/10/2024) ↔ BNK2/2025/00017 (05/10/2025) | 18 € |
| 546 | Acompte 2024 → FACTU 2025 (sens inversé) | Dicapo BNK2/2024/00035 acompte 27,50 ↔ FACTU/2025/04/0006 | 27,50 € |

### Conséquences post-Phase 3

Les **8 lignes 2025** de ces reconciles deviendront non lettrées. C'est cohérent avec l'à-nouveau Super Compteur :
- Les 13 680 € du **411000 CLIENTS** du bilan 31/12/2024 = exactement Sohoft 22 (12 506 €) + Sohoft 23 (1 174 €) ✅
- L'à-nouveau reprendra ces 13 680 € en Dr sur 411
- Le paiement Sohoft 07/01/2025 pourra être re-lettré **manuellement** contre la ligne d'à-nouveau
- Idem pour les fournisseurs (Gandi, Dicapo) : ouvertures dans le 110 € de 408100 ou 401000

### Action manuelle post-Phase 5

Re-lettrer 4 paires :
- FAC/2024/00023 (à-nouveau 411) ↔ BNK1/2025/00005 (1 174 €)
- FAC/2024/00022 (à-nouveau 411) ↔ BNK1/2025/00004 (12 506 €)
- FACTU/2024/10/0001 Gandi (à-nouveau 401) ↔ BNK2/2025/00017 (18 €)
- BNK2/2024/00035 Dicapo acompte (à-nouveau 401) ↔ FACTU/2025/04/0006 (27,50 €)

Le reconcile 481 (frais BPCE 6 €) sera abandonné — montants négligeables.

---

## Décisions opérationnelles validées (08/05/2026)

| Sujet | Décision |
|---|---|
| Stratégie Odoo GDG | A — Reconstruction complète (mêmes phases que GG) |
| Pivot | 31/12/2024 |
| Délettrage 199 lignes | B — Délettrage sélectif (pas d'action préalable, suppression naturelle des reconciles 2024-only par draft+delete ; les 5 bridges seront re-lettrés manuellement post-à-nouveau) |
| TVA cash basis | Test pilote OK ✅ |
| Bilan Bepmale GG 31/12/2024 | Non disponible — on reconstruit nous-mêmes le bilan miroir GG 31/12/2024 après la Phase 5 GDG |
| Citroën C5 | OD manuelle SAGE-style |
| Pièces jointes | Sauvegarde complète avant suppression (~25–50 PDF estimés) |

---

## Plan comptable à analyser (Phase 2)

À traiter en Phase 2 GDG : confronter le plan Odoo GDG actuel aux comptes utilisés par Super Compteur dans la liasse. **Estimation : 30+ comptes à créer** (vs 22 sur GG).

Liste détaillée dans [[../Brief-Comptable-Odoo]] section « Comptes Super Compteur à mapper / créer ».

---

## Plan d'attaque Phases 2-5

| Phase | Action | Volume estimé |
|---|---|---|
| 2 | Plan comptable : retypages + créations | ~30 comptes |
| 3a | Chiffrage + sauvegarde des pièces jointes | ~25–50 PDF |
| 3b | Passage en draft des 416 moves | batch |
| 3c | Suppression des 416 moves | batch |
| Post-3 | Vérifier 0 moves restants ≤ 31/12/2024 | auto |
| 4 | Reconfig journaux | non bloquant |
| 5 | OD d'à-nouveau Super Compteur 31/12/2024 | ~30+ lignes, total bilan 156 595 € incluant amort. |
| Post-5 | Re-lettrer manuellement 4 paires bridges | manuel |
| Post-5 | Reconstruire bilan miroir GG 31/12/2024 + OD complémentaire interco | nouvelle phase pour GG |




---

## ✅ Phase 3 exécutée — 09/05/2026

### Résultats

- **425 moves supprimés** au total (vs 416 estimés) : 416 posted + 3 drafts + 6 extournes/résidus auto-générés par Odoo
- **0 moves restants ≤ 31/12/2024** vérifié
- **71 PJ orphelinées préservées** : voir [[05-Mapping-PJ-Moves-2024-GDG]]
- Tous les reconciles 2024 dissous (88 reconciles 2024-only + 5 bridges 2024↔2025)

### Stratégie de découpage utilisée

**Découpage en 5 batchs par plage d'ID + séparation factures/non-factures** :

| Batch | Plage IDs | Factures | Non-factures | Total |
|---|---|---:|---:|---:|
| Test pilote | 4 IDs ciblés | 0 | 4 | 4 |
| Batch 1 | 1858–1985 | 13 | 76 | 89 |
| Batch 2 | 1992–2113 | 36 | 44 | 80 |
| Batch 3 | 2197–2362 | 25 | 58 | 83 |
| Batch 4 | 2948–3221 | 18 | 55 | 73 |
| Batch 5 | 3226–5518 | 2 | 74 | 76 |
| Drafts résiduels | 3052, 3433 | 2 | 0 | 2 |
| Résidus + extournes auto | 2083, 2084, 3432, 5522-5529 | 1 | 9 | 10 |
| **TOTAL** | | **97** | **320** | **417** |

(L'écart entre 417 supprimés et 425 vient des cascades Odoo qui ont supprimé 8 CABA en plus lors de la suppression des FAC parentes — comportement souhaité.)

### Apprentissage technique majeur

**Erreur initiale Batch 1** : un `delete_record` sur tous les moves d'un coup a échoué avec "Record does not exist" car Odoo cascade-supprime les CABA quand on supprime leur FAC parente. Le batch atomique a été rollback intégralement.

**Solution validée** : **toujours supprimer les factures (FAC + FACTU + RFACTU) AVANT** les autres moves dans la même plage. Les CABA liées sont auto-supprimées par cascade, et le batch suivant ne contient plus que les non-factures (BNK, EXCH, SLR, CABA orphelines de l'ancien plan).

### Extournes auto-générées par Odoo

Lors de la suppression de moves CABA et EXCH posted, Odoo crée parfois automatiquement des extournes (`Reversal of:`) pour neutraliser comptablement avant suppression. Ces extournes restent comme des "fantômes" et doivent être supprimées en post-traitement (ici : 5522, 5523, 5524, 5525, 5526, 5528, 5529).
