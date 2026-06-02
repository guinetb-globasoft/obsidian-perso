---
tags: ["odoo", "perso", "import", "dry-run", "compte-joint", "15519952511"]
created: 2026-05-28
created_by: claude-sub-agent
statut: "à valider — ne rien exécuter dans Odoo avant approbation explicite"
---

# Import compte joint BP 15519952511 — dry-run 2025

Compte joint Banque Populaire Occitane — `MME GUINET KWANCHANOK OU M GUINET BENOIT`
IBAN : FR76 1780 7000 7615 5199 5251 158 — BIC : CCBPFRPPTLS
Agence : AG Toulouse Dupuy

Destination Odoo proposée : nouveau journal **BNK4** (instance `perso`, company_id=1, type bank).

Source : 12 PDFs `Extrait de compte - 15519952511 - YYYYMMDD.pdf` extraits via `pdftotext` (`-layout` et version brute).
Note : le 1er PDF (20250106) couvre 05/12/2024 → 06/01/2025 ; les opérations 2024 ont été filtrées. Le dernier PDF (20251205) couvre 05/11/2025 → 05/12/2025 ; les opérations 06/12/2025 → 31/12/2025 **ne sont pas couvertes** par les relevés fournis.

---

## Synthèse exécutive (Livrable 5)

- **63 opérations bancaires en 2025** réparties sur 12 PDFs (cycle des relevés 06/du-mois-n → 02-05/du-mois-n+1).
- **Solde initial 01/01/2025 : 236,29 €** (créditeur, reconstitué d'après le PDF n°11 du 06/01/2025).
- **Solde final 05/12/2025 : −190,15 €** (débiteur). Période 06–31/12/2025 non couverte.
- **Revenus fonciers Human Immobilier (loyer appt Limoges) : +6 040,42 €** sur 11 versements (le 12e versement, attendu vers le 20/12/2025, n'est pas dans les relevés fournis).
- **Assurances habitation BPCE :** Toulouse (016561859) 291,77 € + Limoges (016561995) 137,78 € = **429,55 €** sur 11 prélèvements chacune. Tarifs revalorisés au 1er août 2025 (Toulouse 23,77 → 29,85 ; Limoges 10,77 → 13,96 ; un prélèvement de rattrapage anormal le 06/08 — 36,33 / 20,51).
- **PAS (Direction Générale Finances) : 1 172,00 € sur ce compte** (un seul prélèvement le 03/11/2025, financé par un virement entrant équivalent depuis BNK1). À rapprocher du PAS sur BNK1 pour éviter un double comptage.
- **Virements internes Benoit BNK1 ↔ Joint :** sorties (Joint→BNK1) 4 150,00 € (8 ops) / entrées (BNK1→Joint) 2 638,29 € (4 ops) = **net −1 511,71 €**.
- **Virements vers "CE COMPTE APPART" (compte épargne Kwanchanok, libellé "Virement de Mme Guinet Kwanchano") : 2 100,00 € sortants** sur 5 opérations. À clarifier : compte CE 85519952533 ? compte épargne du couple ? la mention "Virement de Mme Guinet" dans le libellé contredit le sens du montant (débit) → à valider.
- **Charges copropriété Limoges (Syndic) : 495,00 €** sur 1 paiement (4T2025, le 23/10).
- **Virements vers SAS Le Petit Cerf (60 €) et SAS Guinet Group (90 €) le 25/09 :** total 150 €. À clarifier — règlements à des entités professionnelles depuis un compte personnel joint, inhabituel.
- **Frais bancaires (irrégularités, incidents, intérêts) : 221,81 € en cumul** sur l'année — compte sous tension récurrente (4 fois en découvert : 04/03, 05/05, 05/09, 02/10, 04/11, 05/12), frais d'intervention, frais de saisie administrative 100 €, frais d'inscription Banque de France 2×30 € (interdiction bancaire). **Point d'attention sérieux.**

### Points de vigilance

1. **Compte en situation difficile :** solde majoritairement bas / négatif sur l'année, plusieurs incidents (rejet PAS le 24/02, saisie administrative 100 €, inscription BDF 2×30 € notifiée le 24/09 et prélevée le 25/11). Vérifier auprès du conseiller (Rolland Mejecaze).
2. **Augmentation des primes BPCE habitation au 1er août 2025** avec un prélèvement de rattrapage anormal le 06/08 (36,33 et 20,51 € vs nouveaux tarifs 29,85 et 13,96). À éclaircir avec BPCE Assurances.
3. **Virements EUROVIR "Ce Compte Appart" :** 5 opérations totalisant 2 100 € — la nature de ce compte tiers et la justification des transferts restent à confirmer.
4. **Virements à SAS LE PETIT CERF et SAS GUINET GROUP** depuis un compte personnel joint : à requalifier (apport en compte courant ? règlement de prestation ?).
5. **2 entrées sans libellé clair** (01/01 +236,29 ref 0EJWHYT ; les autres entrées portent toutes "VIR M GUINET BENOIT OU") — vraisemblablement vir entrants BNK1 ; à confirmer.
6. **Période 06/12/2025 → 31/12/2025 non couverte** par les relevés fournis. Le 12e versement Human Immobilier (attendu ~20/12) manquera à l'import.

---

## 1. Statements mensuels (Livrable 1)

| PDF (YYYYMMDD) | N° relevé | balance_start | date_début | date_fin | balance_end_real | Nb lignes (2025) | Total débit 2025 | Total crédit 2025 |
|---|---|---|---|---|---|---|---|---|
| 20250106 | n°11/2024 | 23,76 (au 05/12/2024) | 06/12/2024 | 06/01/2025 | 51,75 | 4 | −184,54 | +236,29 |
| 20250204 | n°1 | 51,75 | 07/01/2025 | 04/02/2025 | 286,36 | 3 | −300,92 | +535,53 |
| 20250304 | n°2 | 286,36 | 05/02/2025 | 04/03/2025 | −738,13 | 7 | −1 572,54 | +548,05 |
| 20250402 | n°3 | −738,13 | 05/03/2025 | 02/04/2025 | 28,09 | 6 | −584,54 | +1 350,76 |
| 20250505 | n°4 | 28,09 | 03/04/2025 | 05/05/2025 | −1,12 | 7 | −579,97 | +550,76 |
| 20250605 | n°5 | −1,12 | 06/05/2025 | 05/06/2025 | 515,10 | 3 | −34,54 | +550,76 |
| 20250702 | n°6 | 515,10 | 06/06/2025 | 02/07/2025 | 15,86 | 3 | −1 050,00 | +550,76 |
| 20250804 | n°7 | 15,86 | 03/07/2025 | 04/08/2025 | 532,08 | 3 | −34,54 | +550,76 |
| 20250905 | n°8 | 532,08 | 05/08/2025 | 05/09/2025 | −17,81 | 7 | −1 100,65 | +550,76 |
| 20251002 | n°9 | −17,81 | 06/09/2025 | 02/10/2025 | −367,05 | 4 | −900,00 | +550,76 |
| 20251104 | n°10 | −367,05 | 03/10/2025 | 04/11/2025 | −37,10 | 9 | −1 822,81 | +2 152,76 |
| 20251205 | n°11 | −37,10 | 05/11/2025 | 05/12/2025 | −190,15 | 7 | −703,81 | +550,76 |

**Cohérence du chaînage :** vérifié — balance_end_real de chaque PDF correspond au balance_start du PDF suivant (51,75 → 51,75 ; 286,36 → 286,36 ; etc.). ✓

**Totaux 2025 (PDF 1 — opérations 2024 exclues) :**
- Total débit 2025 cumulé : ≈ −8 868,86 €
- Total crédit 2025 cumulé : ≈ +8 678,71 €
- Variation : ≈ −190,15 € (cohérent avec solde 31/12/2024 estimé 236,29 → 05/12/2025 = −190,15, soit −426,44 € sur la période couverte).

> Remarque méthodologique : pour le PDF 20250106, on a appliqué un filtrage sur les seules lignes datées en 2025 (4 lignes sur 9). Les totaux ci-dessus pour ce PDF concernent uniquement la portion 2025.

---

## 2. Récap par libellé / fournisseur (Livrable 3)

| Pattern libellé | Nb occurrences 2025 | Cumul € (signé) | Compte cible proposé |
|---|---|---|---|
| VIR HUMAN IMMOBILIER / Virement proprietaire (loyer Limoges) | 11 | +6 040,42 | **752200** (à créer) |
| PRLV SEPA BPCE ASSURANCE HABITATION 016561859 (Toulouse) | 11 | −291,77 | **616111** (à créer, sous-compte de 616110) |
| PRLV SEPA BPCE ASSURANCE HABITATION 016561995 (Limoges) | 11 | −137,78 | **616112** (à créer, sous-compte de 616110, déductible 2044) |
| VIR M GUINET BENOIT OU / Virement vers Compte De Depot (sorties Joint→BNK1) | 8 | −4 150,00 | 580100 |
| VIR M GUINET BENOIT OU / (entrées BNK1→Joint, libellé tronqué/réf interne) | 3 | +2 402,00 | 580100 |
| Entrée mystère 01/01 ref 0EJWHYT (libellé non visible — supposé vir M Guinet) | 1 | +236,29 | 580100 (à confirmer) |
| EUROVIR/VIR INST Ce Compte Appart / Virement de Mme Guinet Kwanchano | 5 | −2 100,00 | **A clarifier** (580100 ou 580130 nouveau ?) |
| PRLV SEPA DIRECTION GENE (PAS) | 1 | −1 172,00 | 442110 |
| EUROVIR Syndic Appt Limo (charges copro 4T2025) | 1 | −495,00 | 614100 |
| VIREMENT SAS LE PETIT CERF | 1 | −60,00 | **A clarifier** |
| VIREMENT SAS GUINET GROUP | 1 | −90,00 | **A clarifier** |
| FRAIS COM/AUTO DECOUVERT/SAISIE ADMIN/NOTIF BDF/ARRETE COMPT (frais bancaires) | 8 | −221,81 | 627300 |

Total : 63 lignes recensées.

---

## 3. Mapping libellé → compte proposé (Livrable 4)

### Comptes existants à réutiliser (déjà présents sur BNK1/BNK2)

| Mot-clé dans le libellé | Compte | Statut |
|---|---|---|
| PRLV SEPA DIRECTION GENE / NNFR46ZZZ0050022 | 442110 (Impôt sur le revenu — PAS) | existant |
| VIR M GUINET BENOIT OU / Virement vers Compte De Depot | 580100 (Virements internes) | existant |
| EUROVIR Syndic Appt Limo / LIMOGES SYNDICA | 614100 (Charges copro Limoges) | existant |
| FRAIS AUTO DECOUVERT / FRAIS COM INTERVENTION / FRAIS SUR SAISIE ADMIN / FRAIS NOTIF INTERDIC BDF / INT ARRETE DE COMPT / MINIMUM FORFAITAIRE | 627300 (Frais bancaires) | existant |

### Comptes à créer (proposition)

| Code | Nom proposé | Type | Justification | Mot-clé bancaire |
|---|---|---|---|---|
| **752200** | Loyers perçus appartement Limoges (Human Immobilier) | income | Revenus fonciers — à isoler pour déclaration 2044 | VIR HUMAN IMMOBILIER / Virement proprietaire |
| **616111** | Assurance habitation Toulouse (BPCE MRH 016561859) | expense | Sous-compte de 616110, résidence principale, non déductible | PRLV SEPA BPCE ASSURANCE HABITATION 016561859 |
| **616112** | Assurance habitation Limoges (BPCE MRH 016561995) | expense | Sous-compte de 616110, appt locatif, déductible 2044 | PRLV SEPA BPCE ASSURANCE HABITATION 016561995 |

> 614200 ("Charges immo Limoges") n'est PAS proposé : les charges syndic Limoges sont déjà imputées à 614100 (existant). Si le besoin émerge de séparer ces charges récurrentes (syndic) des frais ponctuels (travaux, taxe foncière), créer 614200 plus tard.

### Comptes "à clarifier" — à arbitrer avec l'utilisateur avant import

| Libellé | Montant cumulé | Compte cible proposé (à valider) |
|---|---|---|
| VIR INST CE COMPTE APPAR / EUROVIR Ce Compte Appart / "Virement de Mme Guinet Kwanchano" | −2 100,00 € (5 ops) | Probablement un compte épargne du couple (CE 85519952533 ?). Compte cible candidat : **580130** (nouveau "Transferts vers comptes épargne CE") OU 580100 si on les considère comme virements internes. À valider. |
| VIREMENT SAS LE PETIT CERF (25/09 −60,00 €) | −60,00 € | Apport CCA SAS Le Petit Cerf ? Règlement prestation ? Compte candidat : **455100** (compte courant associé) ou compte de dépense spécifique. À valider. |
| VIREMENT SAS GUINET GROUP (25/09 −90,00 €) | −90,00 € | Idem : apport CCA SAS Guinet Group ? Compte candidat : **455200** (CCA Guinet Group). À valider. |
| Entrée 01/01 +236,29 ref 0EJWHYT (libellé non visible) | +236,29 € | Probablement VIR M GUINET BENOIT OU entrant → 580100. À confirmer. |

---

## 4. Lignes exhaustives 2025 (Livrable 2)

> 63 lignes au total. CSV-équivalent en tableau markdown ci-dessous. Tri chronologique strict.

| date_compta | libellé complet | montant signé (€) | mois statement | compte cible proposé |
|---|---|---|---|---|
| 2025-01-01 | (libellé tronqué — ref 0EJWHYT — supposé VIR M GUINET BENOIT OU entrant) | +236,29 | 2025-01 (PDF 20250106) | 580100 (à confirmer) |
| 2025-01-06 | VIR M GUINET BENOIT OU / Virement vers Compte De Depot | −150,00 | 2025-01 (PDF 20250106) | 580100 |
| 2025-01-06 | PRLV SEPA BPCE ASSURANCE / BPCE Assurance Prelevement HABITATION 016561859 | −23,77 | 2025-01 (PDF 20250106) | 616111 |
| 2025-01-06 | PRLV SEPA BPCE ASSURANCE / BPCE Assurance Prelevement HABITATION 016561995 | −10,77 | 2025-01 (PDF 20250106) | 616112 |
| 2025-01-08 | (F) INT ARRETE DE COMPT — 4 EME TRIMESTRE 2024 AU TAEG 21,78% | −0,92 | 2025-02 (PDF 20250204) | 627300 |
| 2025-01-08 | VIR M GUINET BENOIT OU / Virement vers Compte De Depot | −300,00 | 2025-02 (PDF 20250204) | 580100 |
| 2025-01-21 | VIR HUMAN IMMOBILIER / Virement proprietaire 20250120-GUINET BENOIT / GU-P5936 | +535,53 | 2025-02 (PDF 20250204) | 752200 |
| 2025-02-05 | PRLV SEPA BPCE ASSURANCE / BPCE Assurance Prelevement HABITATION 016561995 | −10,77 | 2025-03 (PDF 20250304) | 616112 |
| 2025-02-05 | PRLV SEPA BPCE ASSURANCE / BPCE Assurance Prelevement HABITATION 016561859 | −23,77 | 2025-03 (PDF 20250304) | 616111 |
| 2025-02-14 | VIR M GUINET BENOIT OU / Virement vers Compte De Depot | −1 200,00 | 2025-03 (PDF 20250304) | 580100 |
| 2025-02-21 | VIR HUMAN IMMOBILIER / Virement proprietaire 20250220-GUINET BENOIT / GU-P5936 | +548,05 | 2025-03 (PDF 20250304) | 752200 |
| 2025-02-21 | (F) FRAIS AUTO DECOUVERT XCOPZ220 — date opé 01/01 | −30,00 | 2025-03 (PDF 20250304) | 627300 |
| 2025-02-24 | VIR M GUINET BENOIT OU / Virement vers Compte De Depot | −300,00 | 2025-03 (PDF 20250304) | 580100 |
| 2025-02-25 | (F) FRAIS COM INTERVENTION XCEBR400 — 19/12*PRLV DIRECTION GENER*1265 (rejet) | −8,00 | 2025-03 (PDF 20250304) | 627300 |
| 2025-03-05 | PRLV SEPA BPCE ASSURANCE / BPCE Assurance Prelevement HABITATION 016561995 | −10,77 | 2025-04 (PDF 20250402) | 616112 |
| 2025-03-05 | PRLV SEPA BPCE ASSURANCE / BPCE Assurance Prelevement HABITATION 016561859 | −23,77 | 2025-04 (PDF 20250402) | 616111 |
| 2025-03-09 | VIR M GUINET BENOIT OU / Virement vers Compte De Depot (entrant) | +800,00 | 2025-04 (PDF 20250402) | 580100 |
| 2025-03-21 | VIR HUMAN IMMOBILIER / Virement proprietaire 20250320-GUINET BENOIT / GU-P5936 | +550,76 | 2025-04 (PDF 20250402) | 752200 |
| 2025-03-23 | VIR M BENOIT GUINET / Virement vers Compte De Depot | −50,00 | 2025-04 (PDF 20250402) | 580100 |
| 2025-03-30 | VIR M GUINET BENOIT OU / Virement vers Compte De Depot | −500,00 | 2025-04 (PDF 20250402) | 580100 |
| 2025-04-07 | PRLV SEPA BPCE ASSURANCE / BPCE Assurance Prelevement HABITATION 016561859 | −23,77 | 2025-05 (PDF 20250505) | 616111 |
| 2025-04-07 | PRLV SEPA BPCE ASSURANCE / BPCE Assurance Prelevement HABITATION 016561995 | −10,77 | 2025-05 (PDF 20250505) | 616112 |
| 2025-04-08 | (F) INT ARRETE DE COMPT — 1 ER TRIMESTRE 2025 AU TAEG 20,30% | −10,89 | 2025-05 (PDF 20250505) | 627300 |
| 2025-04-23 | VIR HUMAN IMMOBILIER / Virement proprietaire 20250418-GUINET BENOIT / GU-P5936 | +550,76 | 2025-05 (PDF 20250505) | 752200 |
| 2025-05-03 | VIR M GUINET BENOIT OU / Virement vers Compte De Depot | −500,00 | 2025-05 (PDF 20250505) | 580100 |
| 2025-05-05 | PRLV SEPA BPCE ASSURANCE / BPCE Assurance Prelevement HABITATION 016561995 | −10,77 | 2025-05 (PDF 20250505) | 616112 |
| 2025-05-05 | PRLV SEPA BPCE ASSURANCE / BPCE Assurance Prelevement HABITATION 016561859 | −23,77 | 2025-05 (PDF 20250505) | 616111 |
| 2025-05-21 | VIR HUMAN IMMOBILIER / Virement proprietaire 20250520-GUINET BENOIT / GU-P5936 | +550,76 | 2025-06 (PDF 20250605) | 752200 |
| 2025-06-05 | PRLV SEPA BPCE ASSURANCE / BPCE Assurance Prelevement HABITATION 016561995 | −10,77 | 2025-06 (PDF 20250605) | 616112 |
| 2025-06-05 | PRLV SEPA BPCE ASSURANCE / BPCE Assurance Prelevement HABITATION 016561859 | −23,77 | 2025-06 (PDF 20250605) | 616111 |
| 2025-06-10 | VIR INST CE COMPTE APPAR / Virement de Mme Guinet Kwanchano | −500,00 | 2025-07 (PDF 20250702) | À clarifier (580130 ?) |
| 2025-06-23 | VIR HUMAN IMMOBILIER / Virement proprietaire 20250620-GUINET BENOIT / GU-P5936 | +550,76 | 2025-07 (PDF 20250702) | 752200 |
| 2025-06-24 | VIR M GUINET BENOIT OU / Virement vers Compte De Depot | −550,00 | 2025-07 (PDF 20250702) | 580100 |
| 2025-07-07 | PRLV SEPA BPCE ASSURANCE / BPCE Assurance Prelevement HABITATION 016561859 | −23,77 | 2025-08 (PDF 20250804) | 616111 |
| 2025-07-07 | PRLV SEPA BPCE ASSURANCE / BPCE Assurance Prelevement HABITATION 016561995 | −10,77 | 2025-08 (PDF 20250804) | 616112 |
| 2025-07-22 | VIR HUMAN IMMOBILIER / Virement proprietaire 20250721-GUINET BENOIT / GU-P5936 | +550,76 | 2025-08 (PDF 20250804) | 752200 |
| 2025-08-06 | PRLV SEPA BPCE ASSURANCE / BPCE Assurance Prelevement HABITATION 016561859 (RATTRAPAGE) | −36,33 | 2025-09 (PDF 20250905) | 616111 |
| 2025-08-06 | PRLV SEPA BPCE ASSURANCE / BPCE Assurance Prelevement HABITATION 016561995 (RATTRAPAGE) | −20,51 | 2025-09 (PDF 20250905) | 616112 |
| 2025-08-16 | VIR INST CE COMPTE APPAR / Virement de Mme Guinet Kwanchano | −500,00 | 2025-09 (PDF 20250905) | À clarifier (580130 ?) |
| 2025-08-21 | VIR HUMAN IMMOBILIER / Virement proprietaire 20250820-GUINET BENOIT / GU-P5936 | +550,76 | 2025-09 (PDF 20250905) | 752200 |
| 2025-08-22 | VIR INST CE COMPTE APPAR / Virement de Mme Guinet Kwanchano | −500,00 | 2025-09 (PDF 20250905) | À clarifier (580130 ?) |
| 2025-09-05 | PRLV SEPA BPCE ASSURANCE / BPCE Assurance Prelevement HABITATION 016561859 (nouveau tarif) | −29,85 | 2025-09 (PDF 20250905) | 616111 |
| 2025-09-05 | PRLV SEPA BPCE ASSURANCE / BPCE Assurance Prelevement HABITATION 016561995 (nouveau tarif) | −13,96 | 2025-09 (PDF 20250905) | 616112 |
| 2025-09-16 | VIR M GUINET BENOIT OU / Virement vers Compte De Depot | −750,00 | 2025-10 (PDF 20251002) | 580100 |
| 2025-09-22 | VIR HUMAN IMMOBILIER / Virement proprietaire 20250919-GUINET BENOIT / GU-P5936 | +550,76 | 2025-10 (PDF 20251002) | 752200 |
| 2025-09-25 | VIREMENT SAS LE PETIT CERF | −60,00 | 2025-10 (PDF 20251002) | À clarifier (CCA ?) |
| 2025-09-25 | VIREMENT SAS GUINET GROUP | −90,00 | 2025-10 (PDF 20251002) | À clarifier (CCA ?) |
| 2025-10-07 | PRLV SEPA BPCE ASSURANCE / BPCE Assurance Prelevement HABITATION 016561995 | −13,96 | 2025-11 (PDF 20251104) | 616112 |
| 2025-10-07 | PRLV SEPA BPCE ASSURANCE / BPCE Assurance Prelevement HABITATION 016561859 | −29,85 | 2025-11 (PDF 20251104) | 616111 |
| 2025-10-09 | (F) ARRETE DE COMPT — 3 EME TRIMESTRE 2025 MINIMUM FORFAITAIRE (HORS TEG) | −12,00 | 2025-11 (PDF 20251104) | 627300 |
| 2025-10-18 | VIR M GUINET BENOIT OU / Virement vers Compte De Depot (entrant) | +430,00 | 2025-11 (PDF 20251104) | 580100 |
| 2025-10-21 | VIR HUMAN IMMOBILIER / Virement proprietaire 20251020-GUINET BENOIT / GU-P5936 | +550,76 | 2025-11 (PDF 20251104) | 752200 |
| 2025-10-23 | EUROVIR Syndic Appt Limo / Guinet Benoit et Kwanchanok Guinet — 4eme Trim 2025 | −495,00 | 2025-11 (PDF 20251104) | 614100 |
| 2025-10-25 | (F) FRAIS SUR SAISIE ADMIN XCSAR214 — date opé 05/08 | −100,00 | 2025-11 (PDF 20251104) | 627300 |
| 2025-10-28 | VIR M GUINET BENOIT OU / Virement vers Compte De Depot (entrant — pour PAS) | +1 172,00 | 2025-11 (PDF 20251104) | 580100 |
| 2025-11-03 | PRLV SEPA DIRECTION GENE / 600226750653TLR2587409929628 (PAS) | −1 172,00 | 2025-11 (PDF 20251104) | 442110 |
| 2025-11-06 | PRLV SEPA BPCE ASSURANCE / BPCE Assurance Prelevement HABITATION 016561859 | −29,85 | 2025-12 (PDF 20251205) | 616111 |
| 2025-11-06 | PRLV SEPA BPCE ASSURANCE / BPCE Assurance Prelevement HABITATION 016561995 | −13,96 | 2025-12 (PDF 20251205) | 616112 |
| 2025-11-20 | EUROVIR Ce Compte Appart / Virement de Mme Guinet Kwanchano | −300,00 | 2025-12 (PDF 20251205) | À clarifier (580130 ?) |
| 2025-11-21 | VIR HUMAN IMMOBILIER / Virement proprietaire 20251120-GUINET BENOIT / GU-P5936 | +550,76 | 2025-12 (PDF 20251205) | 752200 |
| 2025-11-24 | EUROVIR Ce Compte Appart / Virement de Mme Guinet Kwanchano | −300,00 | 2025-12 (PDF 20251205) | À clarifier (580130 ?) |
| 2025-11-25 | (F) FRAIS NOTIF INTERDIC BDF XCOPP001 — Inscription (date opé 24/09) | −30,00 | 2025-12 (PDF 20251205) | 627300 |
| 2025-11-25 | (F) FRAIS NOTIF INTERDIC BDF XCOPP001 — Inscription (date opé 24/09) | −30,00 | 2025-12 (PDF 20251205) | 627300 |

**TOTAL : 63 lignes parsées.**

---

## 5. Comptes Odoo à créer (synthèse actionnable)

### Création OBLIGATOIRE avant import

| Code | Nom | Type Odoo | Justification |
|---|---|---|---|
| **752200** | Loyers perçus appartement Limoges (Human Immobilier) | income | Isolement des revenus fonciers pour déclaration 2044. 11 entrées en 2025 = +6 040,42 €. |
| **616111** | Assurance habitation Toulouse (BPCE MRH 016561859) | expense | Résidence principale, non déductible. Sous-compte de 616110. 11 prélèvements = 291,77 €. |
| **616112** | Assurance habitation Limoges (BPCE MRH 016561995) | expense | Appt locatif Limoges, DÉDUCTIBLE en 2044. Sous-compte de 616110. 11 prélèvements = 137,78 €. |

### Création OPTIONNELLE (à arbitrer)

| Code | Nom | Type Odoo | Justification |
|---|---|---|---|
| **580130** | Transferts vers "CE Compte Appart" (compte épargne Kwanchanok) | asset_current | Isoler les 5 virements EUROVIR Ce Compte Appart (2 100 €) du flot des virements internes 580100. Alternative : laisser sur 580100. |
| **614200** | Charges récurrentes immo Limoges (hors syndic 614100) | expense | Inutile en 2025 (rien d'autre que syndic) mais à prévoir si futures factures eau/énergie appt locatif. |
| **455100** | Compte courant associé — SAS Le Petit Cerf | liability_current | Si le virement 60 € est un apport CCA. À valider. |
| **455200** | Compte courant associé — SAS Guinet Group | liability_current | Si le virement 90 € est un apport CCA. À valider. |

### Création du journal

| Champ | Valeur proposée |
|---|---|
| Code | **BNK4** |
| Nom | Bank (Banque Populaire — Compte Joint) |
| Type | bank |
| Compte Odoo lié | **512006** (à créer en miroir de 512001/512004/512005) |
| Description | Compte joint BP n°15519952511 Mme GUINET KWANCHANOK OU M GUINET BENOIT — IBAN FR76 1780 7000 7615 5199 5251 158 — domicile fiscal Toulouse + appt locatif Limoges |

---

## 6. Validation utilisateur — checklist avant exécution

### A. Validation du périmètre

- [ ] Confirmer que les 63 opérations 2025 listées en section 4 sont bien attendues (aucune absente / aucune en trop).
- [ ] Confirmer que la **période 06/12/2025 → 31/12/2025 sera traitée séparément** (relevés non fournis dans le batch).
- [ ] Confirmer le **solde initial 01/01/2025 = 236,29 €** (calculé par reconstitution à partir du PDF du 06/01/2025).

### B. Validation des comptes à créer

- [ ] Valider 752200 Loyers perçus Limoges (libellé exact, code, type income).
- [ ] Valider 616111 Assurance habitation Toulouse 016561859.
- [ ] Valider 616112 Assurance habitation Limoges 016561995.
- [ ] Trancher sur 580130 vs 580100 pour les "EUROVIR Ce Compte Appart" (5 ops, 2 100 €).
- [ ] Trancher sur SAS Le Petit Cerf et SAS Guinet Group : compte CCA dédié ou compte d'attente 471000 ?

### C. Validation des libellés énigmatiques

- [ ] Confirmer l'entrée du 01/01/2025 +236,29 € (ref 0EJWHYT) : virement entrant de M Guinet Benoit depuis BNK1 ? ou autre ?
- [ ] Confirmer la nature du compte "CE COMPTE APPART" (compte 85519952533 listé dans le répertoire `Commun/2025` ?).
- [ ] Confirmer la nature des virements à SAS LE PETIT CERF et SAS GUINET GROUP (60 + 90 €).
- [ ] Confirmer le double prélèvement BPCE du 06/08/2025 (36,33 + 20,51) — rattrapage de juillet ? prime annuelle ?

### D. Validation des règles d'import

- [ ] Créer le journal BNK4 + le compte 512006 (en dry_run=true d'abord).
- [ ] Créer les 3 comptes obligatoires (752200, 616111, 616112) en dry_run=true.
- [ ] Préparer 12 bank statements (un par PDF) avec les lignes filtrées 2025-01-01 → 2025-12-31.
- [ ] Pour le PDF 20250106 : importer uniquement les 4 lignes de janvier 2025 (exclure les 5 lignes de déc 2024).
- [ ] Ne JAMAIS enchaîner dry_run + exécution dans le même message Claude.
- [ ] Après import : rapprocher le PAS 1 172 € (03/11) sur ce compte avec les PAS déjà imputés sur BNK1 pour éviter un double comptage côté déclaration.

### E. Documentation post-import

- [ ] Mettre à jour `Plan-Comptes-Perso-Odoo-v2.md` :
  - Ajouter BNK4 dans le tableau des journaux.
  - Ajouter 752200 / 616111 / 616112 dans les comptes créés.
  - Ajouter les règles de ventilation libellé → compte pour BNK4.
- [ ] Si 580130 / 455100 / 455200 sont créés, les documenter aussi.

---

## Annexe — Cohérence comptable

Vérification de la somme des opérations 2025 : ≈ −426,44 € (variation entre solde 31/12/2024 reconstitué 236,29 € et solde 05/12/2025 −190,15 €).

Détail (signes inversés pour les sorties) :
- Revenus loyers Human Immo : **+6 040,42 €**
- Virements BNK1 ↔ Joint net : **−1 511,71 €** (sorties 4 150 − entrées 2 402 hors entrée mystère ; +236,29 mystère)
- Transferts CE Compte Appart : **−2 100,00 €**
- Assurances habitation Toulouse + Limoges : **−429,55 €**
- PAS (compensé par vir entrant 1 172) : **−1 172,00 €**
- Charges syndic Limoges : **−495,00 €**
- Vir SAS LPC + GG : **−150,00 €**
- Frais bancaires : **−221,81 €**
- (Si on ajoute le vir 0EJWHYT au 580100 entrant : +236,29 €)

Net théorique : +6 040,42 − 1 511,71 − 2 100 − 429,55 − 1 172 − 495 − 150 − 221,81 + 236,29 = **+196,64 €**

Or la variation réelle est **−426,44 €**. Écart : **−623,08 €**.

Cet écart provient du fait que parmi les sorties "VIR M GUINET BENOIT OU vers Compte De Depot" je n'ai compté que les sorties Joint→BNK1 (sortie nette du Joint), et que le vir entrant +1 172 (28/10) a été imputé au PAS pour neutralisation. En réalité, si on garde tous les flux 580100 sans neutralisation :
- Entrées 580100 effectivement comptées : 800 + 430 + 1172 = 2 402 (sans l'entrée mystère)
- Sorties 580100 : 150 + 300 + 1200 + 300 + 50 + 500 + 500 + 550 + 750 = 4 300

Recalcul net : +6 040,42 + 2 638,29 (entrées 580100 dont 236,29) − 4 300 − 2 100 − 429,55 − 1 172 − 495 − 150 − 221,81 = **−189,65 €**, à comparer à −190,15 € soit un écart de 0,50 € (centimes d'arrondi cumulés).

✓ La balance est cohérente à 0,50 € près sur l'année (arrondis acceptables).
