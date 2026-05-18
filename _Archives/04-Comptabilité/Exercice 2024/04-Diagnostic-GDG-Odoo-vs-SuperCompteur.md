---
tags: ["comptabilité", "guinet-digital-group", "exercice-2024", "diagnostic", "phase1"]
created: 2026-05-08
---

---
tags: ["comptabilité", "guinet-digital-group", "exercice-2024", "diagnostic", "phase1"]
created: 2026-05-08
société: Guinet Digital Group (ex-Globasoft)
company_id: 4
---

# Phase 1 — Diagnostic Odoo GDG vs Super Compteur (08/05/2026)

> Objectif : préparer la reconstruction Odoo GDG 2024 alignée sur le bilan Super Compteur au 31/12/2024.

---

## 1. Volumétrie Odoo GDG ≤ 31/12/2024

| Indicateur | Valeur |
|---|---|
| Moves posted | **418** |
| Lignes lettrées | **201** (sur ~80-100 `full_reconcile`) |
| Première écriture | 29/02/2024 (in_invoice) |
| Dernière écriture | 31/12/2024 (Bank) |
| Période effective | 11 mois (cohérent avec exercice Super Compteur 01/02→31/12/2024) |

### Répartition par journal (approximation)

| Journal | Approx. moves | Type |
|---|---|---|
| Bank (BNK1) | ~190 | Compte BPCE Factor ? |
| GLOBASOFT XX7328 (BNK2) | ~75 | Compte secondaire |
| Vendor Bills (BILL) | ~60 | Factures fournisseurs |
| Cash Basis Taxes | ~25 | TVA sur encaissements |
| Compte TVA | ~25 | OD TVA |
| Customer Invoices (FAC) | ~15 | Factures clients |
| Exchange Difference | ~5 | Différences de change |
| Salaries | ~1 | Paie |

→ **GDG est en TVA sur encaissements** (présence du journal Cash Basis Taxes), confirmé par le 445872 "TVA collectée en attente" dans le bilan Super Compteur.

---

## 2. Comparaison ordre de grandeur GG vs GDG

| Indicateur | Guinet Group (déjà fait) | GDG (à faire) | Ratio |
|---|---|---|---|
| Période | 3 mois | **11 mois** | ×3.7 |
| Moves Odoo | 44 | **418** | ×9.5 |
| Lignes Odoo (estim.) | 93 | **~1500-2500** | ×16-27 |
| Lignes lettrées | 0 | **201** | ×∞ |
| Total bilan | 9 064 € | **155 561 €** | ×17 |
| Pièces jointes (estim.) | 3 | **~25-50** | ×8-16 |

→ **L'opération GDG est ~10× plus lourde que GG**.

---

## 3. 🚨 Point bloquant n°1 : les 201 lignes lettrées

### Problème

Sur GG aucune écriture n'était lettrée → suppression directe possible.
Sur GDG **201 lignes sont lettrées** → il faut délettrer avant suppression.

Mais certains lettrages couvrent **2024 ↔ 2025** (factures 2024 payées en 2025). Si on délettre brutalement :
- ✅ Côté 2024 : OK (on va supprimer tout 2024 de toute façon)
- ⚠️ Côté 2025 : on perd l'information de lettrage qu'on pourrait vouloir conserver

### Solutions possibles

**A — Délettrage global** : on accepte de délettrer toutes les 201 lignes, y compris celles dont une partie est en 2025. Conséquence : il faudra re-lettrer manuellement les couples 2024_disparu ↔ 2025_existant après l'à-nouveau, ce qui sera impossible (la facture 2024 aura disparu, remplacée par une ligne agrégée d'à-nouveau).

→ **Acceptable si** : on accepte que les paiements 2025 de factures 2024 deviennent des paiements "non lettrés" (mais cohérents en solde global, puisque l'à-nouveau Super Compteur reprend les factures 2024 ouvertes au 31/12 dans le 411 ou le 401).

**B — Délettrage sélectif** : on identifie les `full_reconcile_id` qui touchent uniquement 2024 (à délettrer) vs ceux qui touchent 2024+2025 (à laisser). On supprime ensuite les moves 2024 pleinement délettrés, et pour les autres, on laisse Odoo casser les lettrages naturellement à la suppression.

→ Plus propre mais plus complexe à mettre en œuvre.

**C — Migrer les lettrages 2025 vers l'à-nouveau** : pour chaque lettrage 2024↔2025, on identifie le solde "vivant" au 31/12/2024 et on le reporte dans une ligne nominative de l'à-nouveau (ex : "Sohoft - facture FAC/2024/00012 ouverte 5 280 €"). Le paiement 2025 pourra alors se lettrer contre cette ligne d'à-nouveau.

→ Plus rigoureux mais demande plus de travail manuel.

---

## 4. 🚨 Point bloquant n°2 : la TVA sur encaissements

GDG utilise le mécanisme **Cash Basis Taxes** d'Odoo : à chaque paiement client, Odoo crée une écriture qui transfère la TVA du compte "TVA en attente" (445872) vers le compte "TVA collectée" définitif.

→ Si on supprime les FAC 2024 et les paiements bancaires 2024, Odoo va potentiellement vouloir aussi supprimer ou modifier ces écritures Cash Basis associées.

→ Il faut comprendre **comment Odoo gère ça** quand on supprime une facture qui a déjà déclenché une écriture Cash Basis Tax. À tester sur 1 cas avant batch.

---

## 5. 🚨 Point bloquant n°3 : la portée multi-année du compte 451 Group

| Source | Solde 451 au 31/12/2024 |
|---|---|
| Bilan Super Compteur | **89 352 € (Dr — créance GDG sur GG)** |
| Odoo GDG (gelé depuis sept 2024) | ~56 500 € |

→ **Écart ~33 000 €** : Super Compteur a saisi des écritures interco entre sept et déc 2024 qui n'existent pas dans Odoo. L'à-nouveau Super Compteur reflètera la vraie créance.

→ Côté **Guinet Group**, ces 89 352 € de dette envers GDG **ne sont pas non plus saisis** (le bilan Bepmale GG s'arrête au 31/03/2024). Sans le bilan Bepmale GG au 31/12/2024, on ne peut pas avoir un miroir cohérent.

---

## 6. 🚨 Point bloquant n°4 : les pièces jointes

Sur GG : 3 PDFs / 44 moves (7%). Sur GDG si même ratio : **~25-50 PDFs à sauvegarder**.
À chiffrer avant suppression.

---

## 7. Plan comptable à analyser

À faire dans une étape ultérieure (Phase 2 du plan d'exécution) : confronter le plan Odoo GDG actuel aux comptes utilisés par Super Compteur dans la liasse. Estimation : **30-50 comptes à créer/retyper** (vs 22 sur GG).

---

## 8. Synthèse des décisions à prendre

Avant de continuer en Phase 2 (plan comptable), **5 questions clés** :

1. **Stratégie sur les 201 lignes lettrées** : option A (délettrage global), B (sélectif), ou C (migration vers à-nouveau) ?
2. **Comportement TVA cash basis** : faire un test pilote sur 1 facture pour voir comment Odoo réagit à la suppression ?
3. **Bilan Bepmale GG 31/12/2024** : peut-on l'obtenir, et si oui sous quel délai ? Sinon, accepte-t-on de désynchroniser temporairement l'interco GG↔GDG ?
4. **Pièces jointes** : on chiffre d'abord avec un script de comptage avant de décider du backup ?
5. **Ordre d'attaque** : on garde l'ordre Phase 2 → 3 → 4 → 5 comme sur GG, ou on adapte pour gérer le délettrage en amont ?




---

## ✅ Test pilote TVA cash basis (08/05/2026)

### Cas testé : FAC/2024/00001 Sohoft 1 080 €

**Structure** :
- FAC/2024/00001 (ID 1857) : 706000 Cr 900 + 411100 Dr 1080 + **445740 "VAT collected on unsettled" Cr 180**
- Paiement BNK1/2024/00046 (ID 1930), reco 94 lettré avec FAC
- **Écriture CABA/2024/04/0001 (ID 1935)** générée automatiquement au paiement : transfère 180 € de 445740 → 445710 (TVA collectée définitive)

### Pipeline testé et validé
1. `update_record state='draft'` sur FAC ✅ (le reconcile reste lié mais la facture est en brouillon)
2. `delete_record` sur FAC ✅ (le reconcile se dissout naturellement)
3. Le CABA et le BNK deviennent **orphelins** mais restent posted
4. `update_record state='draft'` + `delete_record` sur CABA et BNK ✅

### Conséquences pour le batch global
- **Pas besoin de pré-délettrer** : passer en draft + delete dissout les reconciles
- **Les CABA et BNK orphelins seront supprimés dans le même batch** ≤ 31/12/2024 puisqu'ils ont la même date que la FAC
- Le pipeline éprouvé sur GG marche aussi sur GDG malgré la TVA cash basis

---

## ✅ Analyse sélective des reconciles 2024 vs 2024-2025

### Statistiques
- **199 lignes lettrées** ≤ 31/12/2024 (après test pilote -2)
- **88 reconciles uniques** concernés
- **207 lignes au total** dans ces 88 reconciles → **8 lignes en 2025** → **5 reconciles bridges**

### 83 reconciles 2024-only ✅
Délettrage automatique sans impact sur 2025. Aucune action préalable requise.

### 5 reconciles bridges 2024↔2025 ⚠️

| Reco | Type | Détail | Montant |
|---|---|---|---|
| 448 | FAC 2024 → paiement 2025 | FAC/2024/00023 Sohoft (01/12/2024) ↔ BNK1/2025/00005 (07/01/2025) | 1 174 € |
| 449 | FAC 2024 → paiement 2025 | FAC/2024/00022 Sohoft (01/12/2024) ↔ BNK1/2025/00004 (07/01/2025) | 12 506 € |
| 481 | Frais BPCE multi-année | 4 lignes 2024 BNK1 + 4 lignes 2025 (BNK1 + FACTU) sur 401 BPCE | ~6 € |
| 513 | FACTU 2024 → paiement 2025 | Gandi FACTU/2024/10/0001 (11/10/2024) ↔ BNK2/2025/00017 (05/10/2025) | 18 € |
| 546 | Acompte 2024 → FACTU 2025 (inversé) | Dicapo BNK2/2024/00035 acompte 27,50 ↔ FACTU/2025/04/0006 | 27,50 € |

### Conséquences attendues post-Phase 3
Les **8 lignes 2025** des reconciles bridges deviendront **non lettrées**. Mais c'est cohérent avec l'à-nouveau Super Compteur :
- Les 13 680 € de **411000 CLIENTS** du bilan 31/12/2024 incluent les FAC Sohoft 22 et 23 (1 174 + 12 506 = 13 680 € exactement ✅)
- Quand on saisira l'à-nouveau, le 411 reprendra ces 13 680 € en Dr
- Le **paiement Sohoft 07/01/2025** pourra être re-lettré **manuellement** contre la ligne d'à-nouveau (après re-création des partenaires si besoin)
- Idem pour les fournisseurs (Gandi, Dicapo) : ouvertures dans le 110 € de 408100 ou 401000 du bilan

### Action post-Phase 5 à prévoir
Re-lettrage manuel de 4-5 paires :
- FAC 2024 (dans à-nouveau 411) ↔ paiement BNK1/2025
- FACTU 2024 (dans à-nouveau 401/408) ↔ paiement 2025

Le reconcile 481 (frais BPCE) sera abandonné — montants négligeables.
