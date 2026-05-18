---
tags: ["comptabilité", "guinet-digital-group", "exercice-2024", "à-nouveau", "phase5"]
created: 2026-05-09
---

---
tags: ["comptabilité", "guinet-digital-group", "exercice-2024", "à-nouveau", "phase5"]
created: 2026-05-09
updated: 2026-05-09
---

# Phase 5 — OD d'à-nouveau GDG au 31/12/2024

> Reconstitution dans Odoo du bilan de clôture Super Compteur. Permet d'ouvrir 2025 avec les bons soldes par compte.

## Référence Odoo

| Élément | Valeur |
|---|---|
| Move ID | **5530** |
| Name | `OD/2024/12/A-NOUVEAU` |
| Date | 2024-12-31 |
| Journal | OD (id 24, Miscellaneous Operations) |
| Référence | À-nouveau 2024 — Bilan Super Compteur |
| Statut | posted |
| Total D/C | 156 595,00 € (équilibré) |
| Lignes | 25 |

## Tableau d'à-nouveau

| # | Compte | account_id | partner_id | Libellé | Débit | Crédit |
|--:|---|---:|---:|---|---:|---:|
| 1 | 218200 | 1003 | — | Matériel transport (Citroën C5) | 30 000,00 | |
| 2 | 281820 | 3170 | — | Amort. C5 (2 mois) | | 1 033,33 |
| 3 | 411100 | 1149 | 14 (Sohoft) | Clients (Sohoft FAC 22+23) | 13 680,00 | |
| 4 | 418100 | 1154 | — | Clients factures à établir | 14 400,00 | |
| 5 | 425000 | 1164 | — | Avance acompte personnel | 116,00 | |
| 6 | 445860 | 1207 | — | TVA / FNP | 18,00 | |
| 7 | 451000 | 1215 | 1 (Guinet Group) | C/C Guinet Group | 89 352,00 | |
| 8 | 512001 | 1597 | — | Banque BNK1 | 6 309,00 | |
| 9 | 486000 | 1248 | — | Charges constatées d'avance | 2 720,00 | |
| 10 | 101300 | 850 | — | Capital social | | 1 000,00 |
| 11 | 120000 | 883 | — | Résultat exercice 2024 | | 32 646,67 |
| 12 | 164100 | 3169 | — | Emprunt Citroën C5 | | 29 093,00 |
| 13 | 512002 | 1603 | — | Banque N°4634 | | 36,00 |
| 14 | 408100 | 1140 | — | FNP fournisseurs | | 110,00 |
| 15 | 421000 | 1160 | — | Personnel - rémunération | | 40,00 |
| 16 | 428200 | 1167 | — | Congés à payer | | 543,00 |
| 17 | 431000 | 1171 | — | Sécurité sociale | | 40,00 |
| 18 | 437200 | 3171 | — | Caisse retraite salarié | | 16,00 |
| 19 | 438200 | 1173 | — | ORG.SOC. CH/CONGES | | 4,00 |
| 20 | 438600 | 1174 | — | URSSAF gérant TNS | | 18 776,00 |
| 21 | 444000 | 1184 | — | IS dû | | 5 891,00 |
| 22 | 445510 | 1189 | — | TVA à décaisser | | 18 876,00 |
| 23 | 445870 | 1208 | — | TVA / FAE | | 2 400,00 |
| 24 | 445740 | 1200 | — | TVA collectée en attente | | 2 280,00 |
| 25 | 455010 | 3172 | 3 (Benoit GUINET) | C/C Benoit Guinet | | 43 810,00 |
| | | | | **TOTAUX** | **156 595,00** | **156 595,00** |

## Décisions techniques

- **Résultat** : 32 646,67 € (au lieu de 32 646 € arrondi du bilan SC) — chiffre exact qui équilibre.
- **Affectation** : sur 120000 (Profit for the financial year), pré-AG. À reclasser sur 110000 (Profit carried forward) après validation de l'AG.
- **TVA collectée en attente** : 445872 SAGE → 445740 Odoo (`VAT collected on unsettled transactions`), équivalent fonctionnel.
- **Compte 451000** : reste typé `liability_current` malgré le solde débiteur (89 352 €) — Odoo accepte ce sens.
- **Anomalie de séquençage Odoo** : le `name` initialement généré était `VAT Juin1` (mauvaise séquence du journal OD). Forcé manuellement en `OD/2024/12/A-NOUVEAU` via `update_record`. À investiguer en Phase 6 si besoin de standardiser le journal OD.

## Actions post-Phase 5

1. **Re-lettrer les 4 paires bridges 2024↔2025** :
   - FAC/2024/00023 (à-nouveau 411 sur Sohoft, dans cette OD) ↔ BNK1/2025/00005 (1 174 €) [partie de 13 680 €]
   - FAC/2024/00022 (à-nouveau 411 sur Sohoft, dans cette OD) ↔ BNK1/2025/00004 (12 506 €) [partie de 13 680 €]
   - FACTU/2024/10/0001 Gandi (NB : le 401100 n'a pas été repris dans cet à-nouveau car le bilan SC n'avait que 408100 FNP. Lettrage manuel à voir.)
   - BNK2/2024/00035 Dicapo acompte ↔ FACTU/2025/04/0006 (27,50 €) — idem.
2. **Vérifier les soldes** au 01/01/2025 et le 31/12/2025 pour s'assurer que la chaîne reste cohérente.
3. **Reconstruire le bilan miroir Guinet Group au 31/12/2024** (compte 451100 + OD complémentaire).

## Liens

- Bilan source : [[03-Comptes-annuels-GDG-2024]]
- Plan comptable : [[06-Plan-Comptable-GDG-Mapping]]
- Diagnostic : [[04-Diagnostic-GDG-Odoo-vs-SuperCompteur]]
- Brief GDG : [[../Brief-Comptable-Odoo]]




---

## ✅ Re-lettrage post-Phase 5 (09/05/2026)

### Bridges Sohoft re-lettrés ✅

`account.full.reconcile,677` :

| Ligne | Move | Sens | Montant |
|---|---|---|---:|
| 12620 | OD/2024/12/A-NOUVEAU | Db | 13 680,00 |
| 7777 | BNK1/2025/00005 | Cr | 1 173,60 |
| 7778 | BNK1/2025/00004 | Cr | 12 506,40 |

→ Reconcile parfait. Le client Sohoft est désormais soldé pour les FAC 2024.

> Note technique : l'outil `reconcile_lines` a renvoyé une erreur XML-RPC marshaling (TypeError None) après exécution réussie. Toujours vérifier le résultat côté Odoo avant de retenter.

### Bridges Gandi (18 €) et Dicapo (27,50 €) — non re-lettrés (acceptés en l'état)

L'à-nouveau ne portait que 408100 FNP global (110 €) sans détail tiers. Les paiements 2025 (BNK2/2025/00017 Gandi, FACTU/2025/04/0006 Dicapo) sont sur 401100 par tiers.

**Décision** : laisser ces 2 bridges (45,50 € total) en lignes 401 ouvertes 2025. Bruit négligeable, à résorber par un comptable lors d'un futur lettrage manuel ou d'une OD ad-hoc.

| Ligne | Move | Compte | Tiers | Montant |
|---|---|---|---|---:|
| 10883 | BNK2/2025/00017 | 401100 Db | Gandi | 18,00 |
| 10792 | FACTU/2025/04/0006 | 401100 Cr | Dicapo | 27,50 |




---

## Décision sur l'écart 0,53 € (09/05/2026)

**Décision : Skip — laissé tel quel.**

L'OD à-nouveau Odoo porte un résultat de **32 646,67 €** alors que la liasse SC indique exactement **32 646,14 €** (page 1 attestation). Écart : **+0,53 €**.

L'écart vient des centimes des soldes individuels du bilan SC (présentés arrondis à l'euro dans la liasse, sauf total bilan 155 561,27 € et résultat 32 646,14 €). Sans la balance détaillée Bepmale/SC avec tous les centimes, impossible d'identifier précisément quel(s) compte(s) du passif portent les centimes "perdus".

**Justification du skip** : 0,53 € est largement sous le seuil de matérialité comptable (typiquement quelques milliers d'euros pour une entreprise de cette taille). L'à-nouveau Odoo reste un miroir suffisant et exploitable du bilan SC.

À reprendre ultérieurement si besoin d'un alignement parfait au centime, en demandant la balance détaillée à Super Compteur.




---

## Correction inversion mapping bancaire (09/05/2026 — soir)

Suite à l'audit des journaux bancaires 2025, découverte d'une **inversion des comptes 512xxx** dans l'à-nouveau initial.

### Avant correction
| ID | Compte | Db | Cr |
|---|---|---:|---:|
| 12625 | 512001 BNK1 | 6 309 | — |
| 12630 | 512002 BNK2 | — | 36 |

### Après correction
| ID | Compte | Db | Cr |
|---|---|---:|---:|
| 12625 | 512001 BNK1 (55621004634, principal opérationnel) | — | 36 |
| ~~12630~~ | ~~512002 BNK2~~ (supprimée — CB différé n'a pas de solde reportable) | — | — |
| 12671 | **512003 BNK3** (95621009495, compte TVA) | 6 309 | — |

### Justification
D'après les PDFs BPCE :
- **55621004634** = compte courant principal (CB, prélèvements, virements, factures Sohoft) — solde au 31/12/2024 = **-35,92 €** débiteur
- **95621009495** = compte annexe utilisé uniquement pour la TVA — solde au 31/12/2024 = **+6 309,12 €**
- L'à-nouveau initial avait inversé les soldes : 6 309 € posté sur BNK1 (qui doit être négatif) et -36 € sur BNK2 (qui doit être à 0)

### Procédure utilisée
- **Move 5530** passé `state=draft`
- Modification de la ligne 12625 + suppression 12630 + ajout de la ligne 512003 **dans un seul `update_record`** sur le move (les modifications unitaires plantent avec "L'écriture n'est pas équilibrée")
- Move re-`posted` avec `name` `OD/2024/12/A-NOUVEAU` préservé

### Validation post-correction
- Total bilan : 156 595 € Db = 156 595 € Cr ✅
- 25 lignes (au lieu de 25 avant — on a remplacé 1 ligne BNK2 par 1 ligne BNK3)
- Aucune réconciliation cassée (les 2 lignes modifiées n'étaient pas lettrées)

### Implications
Cette correction est **rétroactive au 31/12/2024**. Pour les imports BPCE 2025 à venir :
- Les transactions du 55621004634 doivent toutes aller dans **BNK1** (ce qui est déjà le cas)
- Les transactions du 95621009495 doivent toutes aller dans **BNK3** (à confirmer/compléter)
- BNK2 reste pour les **relevés CB** uniquement (CB différé)
