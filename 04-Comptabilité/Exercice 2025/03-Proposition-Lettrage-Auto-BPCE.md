---
tags: ["comptabilité", "guinet-digital-group", "exercice-2025", "lettrage", "à-valider"]
created: 2026-05-09
---

# Proposition — Écritures sans justificatif tiers (BNK1 / GDG 2025)

> Toutes les lignes ci-dessous sont issues des extraits BPCE déjà importés dans Odoo (BNK1 journal id=27, company_id=4).  
> **Action attendue** : valider ou rejeter chaque catégorie. Pour celles validées, le script peut générer les OD correspondantes.

---

## Niveau 1 — Frais bancaires purs → imputation directe, 0 document tiers

Ces lignes correspondent à des frais BPCE facturés directement au débit du compte.  
Aucune facture fournisseur n'existe (ni ne sera jamais émise). Contrepartie : **627000 Frais bancaires**.

| Catégorie | Nb lignes | Total 2025 | Montant typique | Action proposée |
|---|---:|---:|---|---|
| COMMISSION FACTURETTE CB | 115 | −205,85 € | 0,20 à 2 € | OD automatique → 627 |
| FRAIS SCT INST B2B EXT | 27 | −5,40 € | 0,20 € fixe | OD automatique → 627 |
| FRAIS COM INTERVENTION | 10 | −393,10 € | 11 à 48 € | OD automatique → 627 |
| FRAIS VIRT INSTANTANE | 3 | −3,00 € | 1 € fixe | OD automatique → 627 |
| FRAIS PRELEVEMENT IMPAYE | 3 | −20,00 € | 4 à 8 € | OD automatique → 627 |
| FRAIS SUR SAISIE ADMIN | 2 | −200,00 € | 100 € fixe | OD automatique → 627 |

**Total Niveau 1 : −827,35 €  |  160 lignes**

> ⚠️ Note : FRAIS SUR SAISIE ADMIN (2 × 100 €, oct et nov 2025) — frais de saisie administrative sur compte bancaire. À confirmer que c'est bien comptablement en 627 et non en compte spécifique.

---

## Niveau 2 — Intérêts et agios → compte 661

Charges financières BPCE, aucune facture fournisseur.

| Catégorie | Nb lignes | Total 2025 | Détail | Action proposée |
|---|---:|---:|---|---|
| FRAIS AUTO DECOUVERT | 3 | −150,00 € | 50 €/trimestre (juin, juil, sep) | OD → 661 |
| INT DEB ARRETE DE COMPT | 2 | −398,68 € | Agios T2 (−105,47) + T3 (−293,21) au TEG ~19% | OD → 661 |

**Total Niveau 2 : −548,68 €  |  5 lignes**

> ⚠️ Note : le taux d'intérêt à 19 % sur le compte courant est élevé — confirmer qu'il n'y a pas d'erreur de calcul bancaire sur T3 (293,21 € semble fort).

---

## Niveau 3 — Virement interne BNK1 ↔ BNK2 (Carte CB)

La ligne mensuelle **CARTE FACTURETTES CB** dans BNK1 est le reflet exact du total du Relevé CB importé dans BNK2 pour le même mois. Les deux côtés sont déjà dans Odoo.

| Mois | Montant BNK1 | Contrepartie BNK2 |
|---|---:|---|
| Déc 2024 | −3 717,48 € | ✅ déjà importé |
| Jan 2025 | −2 556,14 € | ✅ importé |
| Fév 2025 | −2 062,44 € | ✅ importé |
| Mar 2025 | −2 601,76 € | ✅ importé |
| Avr 2025 | −2 987,42 € | ✅ importé |
| Mai 2025 | −3 140,18 € | ✅ importé |
| Jun 2025 | −3 483,52 € | ✅ importé |
| Jul 2025 | −4 630,84 € | ✅ importé |
| Aoû 2025 | −? | ✅ importé |
| Sep 2025 | −? | ✅ importé |
| Oct 2025 | −? | ✅ importé |
| Nov 2025 | −? | ✅ importé |

**Action proposée** : créer un virement interne mensuel 512001 → 512002, chaque ligne CARTE FACTURETTES BNK1 et la ligne correspondante dans BNK2 lettrent ensemble (solde nul).

---

## Niveau 4 — Charges récurrentes à contrat connu (pas de facture mensuelle)

Ces prélèvements sont émis par des prestataires avec contrat annuel ou à tacite reconduction. Ils peuvent être imputés directement sans attendre une facture unitaire.

### 4a — Assurances

| Catégorie | Nb | Total 2025 | Compte | Condition |
|---|---:|---:|---|---|
| COTIS RYTHMEO PRO (assurance auto) | 12 | −547,28 € | 616 | Contrat CNV0008167429 — montant ~43,58 €/mois ✅ |
| PRLV BPCE IARD (assurance multirisque) | 10 | −3 029,42 € | 616 | Contrat 131376951 — ~302,94 €/mois ✅ |
| PRLV HUMANIS PREVOYANCE | 3 | −328,92 € | 645 | Cotisation prévoyance dirigeant |

> ⚠️ HUMANIS (3 lignes seulement sur 12 mois) — à vérifier si les autres mois ont un prélèvement sous un autre libellé ou si c'est trimestriel.

### 4b — Remboursement prêt BPCE 8945870

Le libellé détaille le prêt **chaque mois** : `DONT CAP xxx,xx ASS. 16,00E INT. xxx,xx COM. 0,00E`

| Mois | Total | Capital | Assurance | Intérêts |
|---|---:|---:|---:|---:|
| Déc 2024 | −568,50 € | 454,01 € | 16,00 € | 98,49 € |
| Jan 2025 | −568,50 € | 455,52 € | 16,00 € | 96,98 € |
| Mar 2025 | −568,50 € | 457,04 € | 16,00 € | 95,46 € |
| _(× 9 mois restants)_ | … | … | … | … |

**Action proposée** : OD mensuelle scriptable (les montants sont dans le libellé) :
- Débit 164xxx (capital remboursé) — montant variable
- Débit 616xxx (assurance prêt, 16 € fixe)
- Débit 661xxx (intérêts, variable)
- Crédit 512001 (BNK1)

> ✅ Pas de justificatif externe requis — le tableau d'amortissement BPCE est suffisant.

---

## Niveau 5 — Charges sociales (si OD DSN déjà postées)

Ces prélèvements sont directement liés aux déclarations DSN / bulletins de paie. Ils peuvent être rapprochés automatiquement **si les OD de paie sont déjà postées dans Odoo**.

| Catégorie | Nb | Total 2025 | Compte | Condition |
|---|---:|---:|---|---|
| PRLV URSSAF MIDI-PYRENEES | 12 | −4 048,00 € | 645 | OD DSN postée pour chaque mois |
| PRLV GIE KLESIA COTIS (retraite) | 11 | −904,32 € | 645 | Idem |

> ⚠️ **À vérifier** : les OD de paie GDG 2025 sont-elles déjà saisies dans Odoo ? Si oui, ces lignes peuvent être lettrées automatiquement par montant+mois.

---

## Niveau 6 — Impôts directs (si OD fiscales postées)

| Libellé | Nb | Total | Nature | Compte |
|---|---:|---:|---|---|
| PRLV INT DGFIP TVA1-052025 | 1 | −9 500,00 € | TVA mai 2025 | 44551 |
| PRLV INT DGFIP IS1-052025 | 1 | −5 891,00 € | IS 2025 (acompte mai) | 444 |
| PRLV INT DGFIP IS1-062025 | 1 | −3 946,00 € | IS 2025 (acompte juin) | 444 |
| PRLV INT DGFIP IS1-... | 1 | _(à vérifier)_ | IS 2025 (acompte suivant) | 444 |

**Action** : lettrer avec les OD fiscales si déjà postées, ou créer les OD.

---

## Niveau 7 — À clarifier avant de comptabiliser

Ces entrées ne rentrent pas dans une case évidente sans confirmation.

| Libellé | Nb | Total | Question |
|---|---:|---:|---|
| VIR DRFIP ILE DE FRANCE | 6 | +3 000,00 € | 500 €/mois entrant, réf "AUEA MINISTERE DU TRAVAIL EMPLOI". ARCE ? Subvention ? Remboursement ? → Quel compte produit ? |
| VIR BPCE FACTOR | 2 | +19 214,20 € | Décaissements affacturage (12 747 + 6 466 €). À lettrer avec les créances cédées (411 ou 467). |

---

## Récapitulatif

| Niveau | Description | Lignes | Montant net | Validation |
|---|---|---:|---:|---|
| 1 | Frais bancaires → 627 | 160 | −827,35 € | ☐ |
| 2 | Intérêts/agios → 661 | 5 | −548,68 € | ☐ |
| 3 | Virements internes BNK1↔BNK2 | 12 | −35 581,20 € | ☐ |
| 4a | Assurances → 616 | 25 | −3 905,62 € | ☐ |
| 4b | Prêt BPCE → 164/616/661 | 11 | −6 253,50 € | ☐ |
| 5 | Charges sociales → 645 (si DSN postée) | 23 | −4 952,32 € | ☐ |
| 6 | Impôts DGFIP → 444/445 (si OD postée) | 4 | −29 605,00 € | ☐ |
| 7 | À clarifier | 8 | +22 214,20 € | ☐ |

**Total couverts si tout validé : 248 lignes BNK1 sur ~448**

---

## Liens
- Brief import : [[02-Brief-ClaudeCode-Imports-BPCE]]
- Audit journaux : [[01-Audit-Journaux-Bancaires-2025-GDG]]
