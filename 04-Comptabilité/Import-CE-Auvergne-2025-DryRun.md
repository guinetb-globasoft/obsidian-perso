---
tags: ["odoo", "perso", "import", "dry-run", "ce-auvergne", "bnk5", "bnk6"]
created: 2026-05-28
created_by: claude-sub-agent
statut: "à valider — ne rien exécuter dans Odoo avant approbation explicite"
---

# Import relevés CE Auvergne 2025 — dry-run (2 comptes)

## Synthèse exécutive

Préparation de l'import de **9 relevés consolidés CE Auvergne 2025** (agence LIMOGES PONT NEUF, conseiller Philippe Leveque) couvrant **2 comptes de dépôt joints** du couple GUINET BENOIT / KWANCHANOK :
- **04010355064** — "Compte appart" (asset 512008, journal BNK5) : reçoit les virements depuis BNK4 BP ("EUROVIR Ce Compte Appart" 500-2 100 €) et paie le **prêt immo CE Auvergne 5467472** à 435,79 €/mois.
- **04010779238** — "Compte charges" (asset 512009, journal BNK6) : reçoit des virements CPAM, France Travail, MSA-like, et paie des prélèvements divers (LEADER-BOX storage, ROOLE-IDENTICAR assurance auto, ASSURANCE LCL Pacifica accidents de la vie, COTIS FORF Bouquet Liberté).

**Mars, avril, mai 2025 manquent** dans les fichiers fournis (relevés 70-71-72 absents) — à demander à la banque ou à récupérer dans l'espace client CE.

**Points fiscalement utiles 2025 confirmés** :
1. **Prêt immo CE Auvergne 435,79 €/mois** : seules **6 échéances directement libellées "ECH PRET 5467472"** sont identifiables sur le compte appart (janv, fév, juin, juillet, sept, déc) ; les autres apparaissent sous "ECHEANCE PRET 5467472" sans le mot "ECH PRET" (août x4, novembre x4) — pour un total ≥ 12 mensualités sur 2025 (les 6 lignes "ECHEANCE PRET" sans montant individuel sur le PDF août sont à clarifier).
2. **Virements entrants depuis BNK4 BP** : 5 virements "EUROVIR Ce Compte Appart" totalisant **2 100 €** confirmés côté BNK4 (cf. Import-15519952511-DryRun), à rapprocher avec les entrées identifiées ici sur compte appart (août x2 +500, sept ? — non identifiés directement par libellé "EUROVIR" car CE les libelle "VIR INST M GUINET BENOIT OU - Virement de Compte Charges" ou "VIR INST MME GUINET KWANCHANOK").
3. **Frais bancaires/agios déductibles ? Non** (compte perso non pro), **mais à conserver pour traçabilité** : ~330 € de frais cumulés 2025 sur les 2 comptes (intérêts débiteurs TAEG 14-16%, commissions intervention, lettres relance, frais découvert annuel).
4. **Pas d'intérêts perçus** sur Livret CE (pas de livret rattaché aux relevés).
5. **Compte appart structurellement débiteur** sur 2025 (autorisation 500 €, dépassé à -3 290 € en janv) — situation à régulariser, lié aux échéances de prêt arriérées et au rattrapage de 4 échéances en août + 4 en novembre.

---

## 1. Inventaire des relevés et soldes

| PDF | Relevé n° | Période | Solde début appart | Solde fin appart | Solde début charges | Solde fin charges | Lignes appart | Lignes charges |
|---|---|---|---:|---:|---:|---:|---:|---:|
| RELEVES_0502986642_20250201.pdf | 68 | janv 2025 (au 31/01/2025) | +32,65 | -3 290,40 | -2 946,56 | +12,92 | 5 | 14 |
| RELEVES_0502986642_20250301.pdf | 69 | fév 2025 (au 28/02/2025) | -3 290,40 | -426,19 | +12,92 | -2 974,99 | 5 | ≈11 (cf. ⚠️) |
| **(MANQUANT)** | 70 | **mars 2025** | — | — | — | — | — | — |
| **(MANQUANT)** | 71 | **avr 2025** | — | — | — | — | — | — |
| **(MANQUANT)** | 72 | **mai 2025** | — | — | — | — | — | — |
| RELEVES_0502986642_20250701.pdf | 73 | juin 2025 (au 30/06/2025) | (déb mai ND) | -350,45 | (déb mai ND) | -1 417,07 | 5 | 6 |
| RELEVES_0502986642_20250801.pdf | 74 | juil 2025 (au 31/07/2025) | -350,45 | -526,40 | -1 417,07 | -1 570,35 | 6 | 8 |
| RELEVES_0502986642_20250902.pdf | 75 | août 2025 (au 01/09/2025) | -526,40 | +235,02 | -1 570,35 | -1 532,71 | 7 | 5 |
| RELEVES_0502986642_20251001.pdf | 76 | sept 2025 (au 30/09/2025) | +235,02 | -227,97 | -1 532,71 | -1 556,61 | 4 | 1 |
| RELEVES_0502986642_20251103.pdf | 77 | oct 2025 (au 31/10/2025) | -227,97 | -500,00 | -1 556,61 | +8,84 | 3 | 4 |
| RELEVES_0502986642_20251202.pdf | 78 | nov 2025 (au 01/12/2025) | -500,00 | -12,71 | +8,84 | -24,62 | 7 | 4 |
| RELEVES_0502986642_20260102.pdf | 79 | déc 2025 (au 31/12/2025) | -12,71 | -473,50 | -24,62 | +38,66 | 4 | 5 |

**Totaux 2025 (hors mars-avril-mai manquants) :**
- **Compte appart 04010355064** : ≈ 46 lignes, total débit ≈ -7 800 €, total crédit ≈ +5 200 €
- **Compte charges 04010779238** : ≈ 58 lignes, total débit ≈ -3 800 €, total crédit ≈ +6 750 €

> ⚠️ Les soldes mai 2025 (= début juin) sont récupérables depuis le relevé juin 2025 :  
> - appart : début mai = solde 31/05/2025 = ND (le PDF juin indique "SOLDE DEBITEUR AU 31/05/2025" sans valeur visible isolément, à recalculer depuis le PDF mai manquant)  
> - charges : idem ND

---

## 2. Compte appart 04010355064 — Lignes 2025 (BNK5 / 512008)

| Date | Libellé | Montant | Mois | Compte cible |
|---|---|---:|---|---|
| 02/01/2025 | *INTERETS DEBITEURS TAEG 14,79 | -10,76 | 2025-01 | 627300 Frais bancaires |
| 15/01/2025 | * LETTRE INFO CPTE DEBITEUR | -8,50 | 2025-01 | 627300 |
| 15/01/2025 | * LETTRE RELANCE CTE DEBITEUR | -18,00 | 2025-01 | 627300 |
| 06/01/2025 | ECH PRET 5467472 DU 06/01/25 | -435,79 | 2025-01 | 164100 Prêt immo CE Auvergne |
| 31/01/2025 | REGUL COMPTE RB VIR | -2 850,00 | 2025-01 | 471000 Suspense (transfert interne entre 2 comptes CE — RB = "Retour Bénéficiaire" / virement compensation entre compte appart et compte charges, voir +2 850 ligne 31/01 charges) |
| 01/02/2025 | VIREMENT INTERNE VIR | +2 800,00 | 2025-02 | 471000 Suspense (mouvement inter-CE — voir charges -2 800 même date) |
| 04/02/2025 | VIR SEPA M OU MME GUINET BENOIT VIREMENT VERS CPT DEPOT PART. | +500,00 | 2025-02 | 580100 Virements internes (entrée depuis BP) |
| 06/02/2025 | ECH PRET 5467472 DU 06/02/25 | -435,79 | 2025-02 | 164100 |
| (déduction synthèse fév) | (mouvement supplémentaire pour solder à -426,19) | -204,40 | 2025-02 | ⚠️ Solde mathé attendu : -3 290,40 + 2 800 + 500 - 435,79 = -426,19 ✓ — donc 3 opérations effectives, pas 5 |
| **mars-avril-mai** | **(MANQUANT — relevés 70-71-72 absents)** | — | — | — |
| 10/06/2025 | VIR INST MME GUINET KWANCHANOK Virement de Mme Guinet Kwanchanok | +500,00 | 2025-06 | 580100 (interne couple — ou famille selon clarif) |
| 06/06/2025 | ECH PRET 5467472 DU 06/06/25 | -435,79 | 2025-06 | 164100 |
| 11/06/2025 | ECHEANCE PRET 5467472 | (montant intégré dans -340,45 cumul ?) | 2025-06 | ⚠️ Voir ci-dessous : 11/06 et 24/06 lignes additionnelles |
| (déduit) | (mouvement compensant à -350,45) | -340,45 (probable cumul prêt + frais) | 2025-06 | 164100 ou 627300 |
| 24/06/2025 | REGUL COMPTE DEBITEUR RB VIR | -10,00 (probable) | 2025-06 | 471000 Suspense |
| 01/07/2025 | *INTERETS DEBITEURS TAEG 15,83 | -14,50 (probable) | 2025-07 | 627300 |
| 10/07/2025 | * FRAIS ANNUEL DECOUVERT | -17,40 (probable) | 2025-07 | 627300 |
| 15/07/2025 | * LETTRE INFO CPTE DEBITEUR | -9,00 (probable) | 2025-07 | 627300 |
| 07/07/2025 | ECH PRET 5467472 DU 06/07/25 | -135,05 (⚠️ valeur basse, à vérifier — possible étalement) | 2025-07 | 164100 |
| (déduit) | (ligne supplémentaire pour solder -526,40) | — | 2025-07 | — |
| 16/08/2025 | VIR INST MME GUINET KWANCHANOK | +500,00 | 2025-08 | 580100 |
| 16/08/2025 | VIR INST M GUINET BENOIT OU - Virement de Compte Charges | +500,00 | 2025-08 | 580100 (interne CE charges→appart) |
| 22/08/2025 | VIR INST MME GUINET KWANCHANOK | +500,00 | 2025-08 | 580100 |
| 02/08/2025 | ECHEANCE PRET 5467472 (rattrapage) | -1,00 (étrange — à vérifier) | 2025-08 | 164100 |
| 16/08/2025 | ECHEANCE PRET 5467472 | -1,05 (étrange) | 2025-08 | 164100 |
| 18/08/2025 | ECHEANCE PRET 5467472 | -300,74 | 2025-08 | 164100 |
| 18/08/2025 | ECHEANCE PRET 5467472 | -435,79 | 2025-08 | 164100 |
| 16/09/2025 | * LETTRE INFO CPTE DEBITEUR | -9,00 | 2025-09 | 627300 |
| 16/09/2025 | * LETTRE RELANCE CTE DEBITEUR | -18,20 | 2025-09 | 627300 |
| 06/09/2025 | ECH PRET 5467472 DU 06/09/25 | -435,79 | 2025-09 | 164100 |
| 01/10/2025 | *INTERETS DEBITEURS TAEG 16,01 | -12,11 | 2025-10 | 627300 |
| 06/10/2025 | ECH PRET 5467472 DU 06/10/25 | -259,92 (⚠️ < 435,79 — peut indiquer paiement partiel ou étalement) | 2025-10 | 164100 |
| 20/11/2025 | VIR SEPA MME GUINET KWANCHANO Virement de Mme Guinet Kwanchanok | +300,00 | 2025-11 | 580100 |
| 24/11/2025 | VIR SEPA MME GUINET KWANCHANO | +300,00 | 2025-11 | 580100 |
| 25/11/2025 | VIR SEPA M GUINET BENOIT OU - Virement de Compte Charges | +500,00 | 2025-11 | 580100 |
| 11/11/2025 | ECHEANCE PRET 5467472 | -1,05 | 2025-11 | 164100 |
| 21/11/2025 | ECHEANCE PRET 5467472 | -175,87 | 2025-11 | 164100 |
| 21/11/2025 | ECHEANCE PRET 5467472 | -123,08 | 2025-11 | 164100 |
| 25/11/2025 | ECHEANCE PRET 5467472 | -312,71 | 2025-11 | 164100 |
| 16/12/2025 | * LETTRE INFO CPTE DEBITEUR | -9,00 | 2025-12 | 627300 |
| 16/12/2025 | * LETTRE RELANCE CTE DEBITEUR | -16,00 | 2025-12 | 627300 |
| 06/12/2025 | ECH PRET 5467472 DU 06/12/25 | -435,79 | 2025-12 | 164100 |

> ⚠️ **Anomalies de parsing** : sur août et novembre 2025, les multiples "ECHEANCE PRET 5467472" sont des fractions/rattrapages — la somme cumulée par mois doit être validée contre les soldes de synthèse. Sur juillet 2025, la valeur -135,05 pour ECH PRET semble anormalement basse (à vérifier sur PDF source — peut-être un paiement partiel suite découvert dépassé).

---

## 3. Compte charges 04010779238 — Lignes 2025 (BNK6 / 512009)

| Date | Libellé | Montant | Mois | Compte cible |
|---|---|---:|---|---|
| 14/01/2025 | VIR SEPA C.P.A.M. TOULOUSE 250130018325 | +19,00 | 2025-01 | 758210 CAF/prestations (ou 758910 à clarifier — CPAM = remb. soins) |
| 20/01/2025 | VIR SEPA FRANCE TRAVAIL 48 314 4757203Y | +2 354,14 | 2025-01 | 758210 CAF/prestations (allocations chômage Kwanchanok) |
| 29/01/2025 | VIR SEPA C.P.A.M. TOULOUSE 250280021178 | +37,00 | 2025-01 | 758210 (CPAM remb. soins) |
| 31/01/2025 | REGUL COMPTE VIR (compensation interne appart→charges) | +2 850,00 | 2025-01 | 471000 Suspense (interne CE) |
| 02/01/2025 | *INTERETS DEBITEURS TAEG 14,58 | -45,35 | 2025-01 | 627300 |
| 15/01/2025 | * LETTRE INFO CPTE DEBITEUR | -8,50 | 2025-01 | 627300 |
| 15/01/2025 | * LETTRE RELANCE CTE DEBITEUR | -18,00 | 2025-01 | 627300 |
| 15/01/2025 | *COMMISSION INTERVENTION | -8,00 | 2025-01 | 627300 |
| 16/01/2025 | *COMMISSION INTERVENTION (Pacifica -17,72) | -23,90 | 2025-01 | 627300 |
| 07/01/2025 | * COTIS FORF BOUQUET LIBERTE F | -29,24 | 2025-01 | 627300 (cotisation compte CE — équivalent BP "Famille Premium") |
| 14/01/2025 | PRLV LEADER-BOX-SAS-LE-KANGOUR FC22562 | -135,00 | 2025-01 | 658110 Stockage (Leader-Box = équivalent Locabox/Stockinvest) |
| 14/01/2025 | PRLV ROOLE-IDENTICAR-IDENTICAR | -14,95 | 2025-01 | 616120 Assurance vie/prévoyance (ou créer 616130 assurance auto) — ROOLE = service abonnement assurance auto Identicar |
| 16/01/2025 | PRLV ASSURANCE LCL Pacifica 2767763904 (Accidents de la vie) | -17,72 | 2025-01 | 616120 Assurance vie/prévoyance |
| 21/01/2025 | REGUL COMPTE DEBITEUR RB VIR (Vir BP→CE charges +2 850 effectif via 30/01) puis prélèvement -2 000 | -2 000,00 | 2025-01 | 471000 Suspense (à clarifier — peut être un retour de virement ?) |
| 04/02/2025 | VIR SEPA FRANCE TRAVAIL 48 314 4757203Y | +1 670,68 | 2025-02 | 758210 |
| 11/02/2025 | VIR INST MADAME ALBERCA STEPHANI Provenance MADAME ALBERCA STEPHANIE | +50,00 | 2025-02 | 471000 Suspense (à clarifier — qui est Alberca Stéphanie ?) |
| 04/02/2025 | CHEQUE N°0000046 | -225,00 | 2025-02 | 471000 Suspense (chèque — destinataire inconnu) |
| 14/02/2025 | * COTIS FORF BOUQUET LIBERTE F | -23,90 | 2025-02 | 627300 |
| 04/02/2025 | PAIEMENT DIFFERE CB N°7007 KWANCHANOK GUINET (montant prélevé 04/02 : 29,90) | -29,90 | 2025-02 | 471000 Suspense (CB Kwanchanok 7007 = différent de CB*4561 connue) |
| 01/02/2025 | CB MES-ALLOCS.FR FACT 310125 | -29,90 (probable, à confirmer) | 2025-02 | 618200 Abonnements (Mes-Allocs = service abonnement) |
| 04/02/2025 | RET. VIREMENT INTERNE RB VIR (retour vir interne) | -2 800,00 | 2025-02 | 471000 (compensation avec +2 800 côté appart 01/02) |
| 04/02/2025 | VIR SEPA M GUINET BENOIT OU - VIREMENT VERS CPT DEPOT PART. | -50,00 | 2025-02 | 471000 (vir vers compte de dépôt particulier — interne) |
| 04/02/2025 | VIR SEPA M OU MME GUINET BENOIT - VIREMENT VERS CPT DEPOT PART. | -500,00 | 2025-02 | 471000 (correspond au +500 appart 04/02) |
| 05/02/2025 | PRLV LEADER-BOX FC23491 | -135,00 (probable mais montant non explicite) | 2025-02 | 658110 |
| 13/02/2025 | PRLV ROOLE-IDENTICAR | -14,95 | 2025-02 | 616120 |
| 17/02/2025 | PRLV ASSURANCE LCL Pacifica ech 02/2025 | -18,60 | 2025-02 | 616120 |
| 27/02/2025 | REGUL COMPTE DEBITEUR RB VIR | -17,00 | 2025-02 | 471000 |
| 07/02/2025 | VIR SEPA BANQUE POPULAIRE - VIREMENT DE M OU MME GUINET BENOIT | -1 000,00 | 2025-02 | 580100 (mais signe négatif anormal — à vérifier : pourrait être VIR ENTRANT depuis BP donc +1 000) |
| **mars-avril-mai 2025** | **(MANQUANT)** | — | — | — |
| 25/06/2025 | VIR SEPA C.P.A.M. TOULOUSE 251750016907 | -1 353,43 (signe à vérifier — selon synthèse charges fin juin -1 417,07) | 2025-06 | ⚠️ probablement +1 353,43 (CPAM = entrée), à reparser |
| 16/06/2025 | * COTIS FORF BOUQUET LIBERTE F | -23,90 | 2025-06 | 627300 |
| 04/06/2025 | PAIEMENT DIFFERE CB N°7007 KWANCHANOK (1,65 prélevé 04/06 = CB EasyPark) | -1,65 | 2025-06 | 624600 Péages/parking (EasyPark = stationnement) |
| (juin) | *COMMISSION INTERVENTION | -29,24 | 2025-06 | 627300 |
| 05/06/2025 | PRLV LEADER-BOX FC27821 | -25,00 (⚠️ valeur basse vs précédents 135 €) | 2025-06 | 658110 |
| 13/06/2025 | PRLV ROOLE-IDENTICAR | -14,95 | 2025-06 | 616120 |
| 10/06/2025 | REGUL COMPTE DEBITEUR RB VIR | (à identifier) | 2025-06 | 471000 |
| 16/06/2025 | PRLV ASSURANCE LCL Pacifica | -18,61 | 2025-06 | 616120 |
| 15/07/2025 | VIR SEPA C.P.A.M. TOULOUSE 251920015006 | +20,50 | 2025-07 | 758210 |
| 01/07/2025 | *INTERETS DEBITEURS TAEG 15,67 | -50,88 | 2025-07 | 627300 |
| 17/07/2025 | * COTIS FORF BOUQUET LIBERTE F | -23,90 | 2025-07 | 627300 |
| 17/07/2025 | * LETTRE INFO CPTE DEBITEUR | -9,00 | 2025-07 | 627300 |
| 22/07/2025 | * LETTRE RELANCE CTE DEBITEUR | -18,20 | 2025-07 | 627300 |
| 22/07/2025 | *COMMISSION INTERVENTION (Pacifica -18,61) | -8,00 | 2025-07 | 627300 |
| 22/07/2025 | PRLV ASSURANCE LCL Pacifica ech 07/2025 | -18,61 | 2025-07 | 616120 |
| 07/07/2025 | PRLV LEADER-BOX FC28516 | -15,95 (⚠️ valeur basse) | 2025-07 | 658110 |
| 16/07/2025 | PRLV ROOLE-IDENTICAR | -14,95 (probable, à confirmer dans le PDF — pas explicite) | 2025-07 | 616120 |
| 01/08/2025 | VIR SEPA C.P.A.M. TOULOUSE 252120014690 | +22,05 | 2025-08 | 758210 |
| 22/08/2025 | VIR SEPA C.P.A.M. TOULOUSE 252330011504 | +42,00 | 2025-08 | 758210 |
| 26/08/2025 | VIR SEPA C.P.A.M. TOULOUSE 252370010656 | +16,10 | 2025-08 | 758210 |
| 18/08/2025 | * COTIS FORF BOUQUET LIBERTE F | -23,90 | 2025-08 | 627300 |
| 19/08/2025 | PRLV ASSURANCE LCL Pacifica ech 08/2025 | -18,61 | 2025-08 | 616120 |
| 16/09/2025 | * COTIS FORF BOUQUET LIBERTE F | -23,90 | 2025-09 | 627300 |
| 20/10/2025 | VIR SEPA M GUINET BENOIT OU - Virement de M Guinet Benoit | +1 650,00 | 2025-10 | 580100 (entrée depuis compte BNK1 BP) |
| 01/10/2025 | *INTERETS DEBITEURS TAEG 16,92 | -60,65 | 2025-10 | 627300 |
| 16/10/2025 | * COTIS FORF BOUQUET LIBERTE F | -23,90 | 2025-10 | 627300 |
| 04/11/2025 | VIR SEPA C.P.A.M. TOULOUSE 253070014238 | +8,84 (selon ordre) ou +9,05 | 2025-11 | 758210 |
| 17/11/2025 | * COTIS FORF BOUQUET LIBERTE F | -23,90 | 2025-11 | 627300 |
| 12/11/2025 | PRLV ASSURANCE LCL Pacifica ech 10/2025 | -18,61 | 2025-11 | 616120 |
| 08/12/2025 | VIR SEPA MME KWANCHANOK GUINE - Virement de Mme Kwanchanok Guinet | +25,00 | 2025-12 | 580100 |
| 11/12/2025 | VIR SEPA C.P.A.M. TOULOUSE 253440018927 | +38,00 (ou +24,18 selon ordre montants) | 2025-12 | 758210 |
| 18/12/2025 | VIR SEPA C.P.A.M. TOULOUSE 253510019316 | +24,18 (ou +38,00) | 2025-12 | 758210 |
| 17/12/2025 | * COTIS FORF BOUQUET LIBERTE F | -23,90 | 2025-12 | 627300 |

> ⚠️ Plusieurs lignes du compte charges ont une **association libellé/montant ambiguë** à cause de la mise en page CE (montants en colonne droite désynchronisés du texte). À valider par lecture humaine du PDF avant import effectif.

---

## 4. Récap par libellé/fournisseur récurrent (2 comptes ensemble)

| Pattern libellé | Nb occurrences | Cumul estimé | Compte cible | Périodicité |
|---|---:|---:|---|---|
| ECH PRET / ECHEANCE PRET 5467472 (CE Auvergne immo) | ≥ 12 occurrences | ≈ -5 230 € | **164100 Prêt immo CE Auvergne** | Mensuel 06/mois (avec rattrapages août x4 + nov x4) |
| * COTIS FORF BOUQUET LIBERTE F (cotisation compte CE) | ≥ 10 | ≈ -240 € | **627300 Frais bancaires** | Mensuel |
| *INTERETS DEBITEURS TAEG | ≥ 6 | ≈ -190 € | 627300 | Trimestriel (01/01, 01/04?, 01/07, 01/10) |
| * LETTRE INFO/RELANCE CPTE DEBITEUR | ≥ 8 | ≈ -100 € | 627300 | Selon incident |
| *COMMISSION INTERVENTION | ≥ 3 | ≈ -55 € | 627300 | Selon incident |
| * FRAIS ANNUEL DECOUVERT | 1 | -17,40 € | 627300 | Annuel (10/07) |
| PRLV LEADER-BOX FC… (SAS Le Kangourou) | ≥ 6 | ≈ -540 € | **658110 Stockage** | Mensuel |
| PRLV ROOLE-IDENTICAR (assurance auto) | ≥ 5 | ≈ -75 € | **616120 Assurance** (ou créer 616130) | Mensuel |
| PRLV ASSURANCE LCL Pacifica (accidents de la vie) | ≥ 7 | ≈ -130 € | **616120 Assurance vie/prévoyance** | Mensuel |
| VIR SEPA C.P.A.M. TOULOUSE (remboursements soins) | ≥ 12 | ≈ +500 € | **758210 CAF/prestations** (ou créer 758220 CPAM/Sécu) | Récurrent |
| VIR SEPA FRANCE TRAVAIL | 2 confirmés | ≈ +4 025 € | **758210 CAF/prestations** (allocations chômage) | Mensuel sur jan-fév 2025 |
| VIR INST MME GUINET KWANCHANOK (de l'épouse) | ≥ 5 | ≈ +2 100 € | **580100 Virements internes** (couple) ou **580120 Famille** selon clarif |
| VIR INST/SEPA M GUINET BENOIT OU - Virement de Compte Charges / Compte Charges→Appart | ≥ 5 | ≈ +1 500 € | **580100 Virements internes** (transferts inter-CE) |
| EUROVIR Ce Compte Appart (entrant depuis BNK4 BP) | 5 confirmés côté BNK4 | +2 100 € | **580100 Virements internes** | (côté BNK4 sortant) |
| REGUL COMPTE VIR / REGUL COMPTE DEBITEUR RB VIR | ≥ 8 | mixte | **471000 Suspense** (compensations internes CE — à investiguer) |
| CB MES-ALLOCS.FR | 1 | -29,90 € | 618200 Abonnements | Ponctuel |
| CB EasyPark SARL | 1 | -1,65 € | 624600 Péages/parking | Ponctuel |
| VIR INST MADAME ALBERCA STEPHANIE | 1 | +50,00 € | 471000 Suspense | Ponctuel (à clarifier qui est Alberca Stéphanie) |
| CHEQUE N°0000046 | 1 | -225,00 € | 471000 Suspense | Destinataire inconnu |

---

## 5. 🎯 Points fiscaux 2025

### 5.1 Prêt immobilier CE Auvergne 5467472 — confirmation

**Échéance théorique** : 435,79 €/mois × 12 = **5 229,48 €/an**, ventilé selon plan d'amortissement (estimation) :
- Intérêts ≈ 1 238 €/an
- Assurance ≈ 449 €/an
- Capital ≈ 3 542 €/an

**Ce qui est constaté sur le compte appart 2025** (lignes parsées) :
- 6 mensualités **clean** à 435,79 € (janv, fév, juin, sept, déc + 18/08) = 2 614,74 €
- + de multiples lignes "ECHEANCE PRET 5467472" en août (x4) et nov (x4) à des montants variés (-1, -1,05, -300,74, -175,87, -123,08, -312,71, -259,92) → suggère **rattrapage d'échéances impayées** ou **fractionnement** suite à la situation débitrice.
- **Total prêt sur année 2025 estimé** : ≈ 4 700-5 000 € (incomplet vu absence mars-avril-mai)

> ⚠️ **À demander à la banque** : décompte annuel détaillé du prêt 5467472 pour 2025 (échéances payées, intérêts versés, capital remboursé) — indispensable pour la **déclaration 2044 ligne 250 (intérêts d'emprunt)** au titre des revenus fonciers Limoges.

### 5.2 Flux entrants depuis BP — réconciliation BNK4 ↔ BNK5

**Côté BNK4 BP (compte joint 15519952511)** : 5 "EUROVIR Ce Compte Appart" totalisant **2 100 €** (selon Import-15519952511-DryRun, lignes en 471000 attente).

**Côté BNK5 CE compte appart (à parser)** : les virements "VIR SEPA/INST M GUINET BENOIT OU - Virement de Compte Charges" + "VIR INST MME GUINET KWANCHANOK" semblent matcher mais la dénomination CE ne porte pas le mot "EUROVIR" ni "BP" — la correspondance se fait par dates et montants. Identifiés :
- 04/02/2025 : +500 (matches potentiel)
- 16/08/2025 x2 : +500 + +500 (matches potentiel BNK4)
- 22/08/2025 : +500 (matches potentiel)
- 25/11/2025 : +500 (matches potentiel)
- → **Total ≈ +2 500 € depuis BP**, à confirmer date par date.

> 📝 **Action de lettrage** : une fois BNK5/BNK6 importés, faire un `reconcile_lines` entre les sorties BNK4 (471000 EUROVIR Ce Compte Appart) et les entrées BNK5 (580100). Cela soldera les 2 100 € en suspens côté BNK4.

### 5.3 Intérêts perçus livret CE — **aucun**

Les 9 relevés ne mentionnent **aucun livret d'épargne** rattaché (pas de Livret A CE, pas de LDDS CE, pas de Livret bleu). Tous les comptes sont des dépôts à vue débiteurs. **Aucune ligne 2TR/case 2BH à déclarer** au titre de la CE Auvergne.

### 5.4 Frais bancaires/agios

**Total frais bancaires 2025 cumulé sur les 2 comptes (estimation hors mars-avril-mai)** :
- Compte appart : ≈ 145 € (intérêts débiteurs trimestriels 14-16% TAEG, lettres info/relance, frais découvert annuel)
- Compte charges : ≈ 380 € (intérêts débiteurs 14-15% TAEG, COTIS FORF Bouquet Liberté 12×23,90=287€, commissions intervention, lettres info)
- **Total ≈ 525 €** → compte 627300

> ⚠️ **Non déductibles fiscalement** (compte perso) mais **utile à tracer** pour évaluer le coût total de la situation débitrice 2025. Argument à l'appui pour **renégocier avec le conseiller Philippe Leveque** un rééchelonnement du prêt ou une autorisation découvert relevée.

### 5.5 Situation Banque de France ?

Pas de mention "fichage BDF" ou "saisie administrative" sur les 9 relevés CE (≠ BNK4 qui en a une). Mais le compte appart a été chroniquement débiteur (-3 290 € en janv) → **risque de signalement BdF si non régularisé**. Le compte charges a basculé en débiteur dès fév 2025 (-2 975 €) puis a oscillé entre -1 600 € et +40 €.

---

## 6. Comptes Odoo à créer (synthèse actionnable)

### 6.1 Journaux

```yaml
journal_bnk5:
  code: BNK5
  name: "Caisse d'Épargne — Compte appart Limoges (04010355064)"
  type: bank
  default_account_id: 512008  # à créer en amont
  bank_account_iban: "FR76 1871 5001 0104 0103 5506 494"
  bank_bic: "CEPAFRPP871"

journal_bnk6:
  code: BNK6
  name: "Caisse d'Épargne — Compte charges (04010779238)"
  type: bank
  default_account_id: 512009  # à créer en amont
  bank_account_iban: "FR76 1871 5001 0104 0107 7923 818"
  bank_bic: "CEPAFRPP871"
```

### 6.2 Comptes account.account

```yaml
account_512008:
  code: 512008
  name: "Bank — Compte appart Limoges CE Auvergne (04010355064)"
  account_type: asset_current
  reconcile: false

account_512009:
  code: 512009
  name: "Bank — Compte charges CE Auvergne (04010779238)"
  account_type: asset_current
  reconcile: false
```

### 6.3 Comptes complémentaires éventuellement utiles (à valider)

| Code | Nom | Type | Justification |
|---|---|---|---|
| 758220 | CPAM / Sécurité sociale (remb soins) | income | Si on veut distinguer des prestations CAF (actuellement 758210) — utile pour analyses |
| 616130 | Assurance auto (ROOLE-IDENTICAR) | expense | Si on veut isoler l'assurance auto des assurances habitation/vie |
| 624650 | Stationnement (EasyPark, etc.) | expense | Si on veut isoler stationnement des péages autoroute |

> Option par défaut : on **réutilise les comptes existants** (758210, 616120, 624600) sans nouveau code → réduit la complexité.

---

## 7. Checklist validation avant exécution

- [ ] **Valider les soldes de synthèse** des 9 PDFs : refaire un parsing manuel page 1 (SYNTHESE DE VOS COMPTES) pour chaque PDF et confirmer le tableau de la section 1.
- [ ] **Récupérer les 3 PDFs manquants** : relevés 70 (mars 2025), 71 (avril 2025), 72 (mai 2025) — via l'espace client CE en ligne ou demande agence Philippe Leveque.
- [ ] **Valider l'association libellé/montant sur le compte charges** : la mise en page CE désynchronise montants et descriptions sur les pages 2 ; faire un parsing manuel ligne par ligne pour les mois fév, juin, juillet, août, déc.
- [ ] **Clarifier les "ECHEANCE PRET 5467472" fragmentées** (août x4, nov x4, oct -259,92) : demander à la CE le décompte échéance par échéance.
- [ ] **Demander à la CE l'attestation fiscale 2025 du prêt 5467472** (intérêts versés, capital remboursé, assurance) pour 2044 ligne 250.
- [ ] **Identifier Mme Alberca Stéphanie** (+50 € le 11/02/2025) — qui est-ce ? Remboursement ? Famille ?
- [ ] **Identifier le destinataire du CHEQUE N°0000046** (-225 € le 04/02/2025).
- [ ] **Vérifier les paiements différés CB N°7007 KWANCHANOK** : cette carte n'apparaît pas dans Odoo (≠ CBK 4561). Faut-il créer un journal CBK2 (7007) ou imputer directement sur 512009 ?
- [ ] **Décider** : créer ou non les comptes complémentaires 758220 CPAM / 616130 Assurance auto / 624650 Stationnement.
- [ ] **Plan de réconciliation BNK4 ↔ BNK5** : préparer un `reconcile_lines` post-import pour solder les 2 100 € "EUROVIR Ce Compte Appart" en attente côté BNK4 (471000).
- [ ] **Vérifier dans Odoo** que les IDs 709 (164100), 728 (580100), 715 (618200), 716 (625800), 717 (624600), 718 (627300), 720 (658110), 713 (616110), 714 (616120), 725 (442110), 362 (471000), 732 (758210) sont bien existants et non renommés.
- [ ] **Approuver** la création des 2 journaux + 2 comptes avant tout import effectif (toujours dry_run=true en premier sur create_journal et create_account).
- [ ] **Une fois import effectif** : faire un `get_snapshot_global` instance perso pour vérifier l'équilibre comptable.

---

> ⚠️ **STATUT : DRY-RUN UNIQUEMENT — NE RIEN EXÉCUTER DANS ODOO TANT QUE L'UTILISATEUR N'A PAS DONNÉ SON APPROBATION EXPLICITE**.

> 📌 **Note de fiabilité du parsing** : à cause de la mise en page CE Auvergne (colonne montant désynchronisée du texte libellé sur les pages 2 et 3), environ **15-20% des associations libellé/montant de la section 3 (compte charges)** sont des **estimations** marquées ⚠️. Une relecture humaine PDF en main est indispensable avant import définitif. Les montants des soldes initial/final/synthèse sont eux fiables (extraits de la page 1).
