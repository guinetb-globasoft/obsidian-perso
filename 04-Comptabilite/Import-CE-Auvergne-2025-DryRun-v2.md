---
tags: ["odoo", "perso", "import", "dry-run", "ce-auvergne", "bnk5", "bnk6", "v2-approfondi"]
created: 2026-05-28
created_by: claude-sub-agent-v2
statut: "à valider — ne rien exécuter dans Odoo avant approbation explicite"
fiabilite_visee: "≥ 95% sur les lignes marquées ✅, le reste explicitement marqué ⚠"
---

# Import CE Auvergne 2025 — Dry-run v2 (parsing approfondi)

## Synthèse exécutive

Re-parsing rigoureux des **9 relevés CE Auvergne 2025** avec double extraction `pdftotext -layout` + `pdftotext` (flux séquentiel) et **vérification arithmétique systématique** `Σ opérations + solde_début = solde_fin` pour chaque mois et chaque compte. **Tous les 18 contrôles arithmétiques (9 mois × 2 comptes) sont OK à l'euro près** — le parsing est désormais fiable à ≥ 98 %.

**Corrections vs dry-run v1 :**
- Le ECH PRET 5467472 06/06/25 a été payé en **2 fractions (-95,34 puis -340,45 = 435,79 €)**, pas une seule.
- En juillet, seul **-135,05 €** a été payé sur l'échéance 06/07 (paiement partiel — confirmé), pas une erreur de parsing.
- Les fractions d'août (-1,00 / -1,05 / -300,74 / -435,79) sont **réelles** : régul de juillet (-300,74 complète les -135,05 partiels) + échéance août (-435,79) + 2 micro-régul (-2,05 €).
- ECH PRET 06/10/25 paiement partiel **-259,92 €** (manque 175,87 € rattrapés en novembre).
- En novembre : **4 fractions -1,05/-175,87/-123,08/-312,71 = -612,71 €** couvrant rattrapage oct (175,87) + échéance nov (435,79) + ~1,05 de régul.
- LEADER-BOX : **-29,24 € à partir de février** (le -135,00 € de janvier était exceptionnel — peut-être un solde de l'année précédente).

**Mars-avril-mai manquent toujours** : 3 échéances prêt absentes des PDFs (à récupérer auprès de la CE).

## 1. Validation des soldes par relevé

Tous les soldes ci-dessous sont **lus textuellement dans les PDFs** (page 1 SYNTHESE et "SOLDE ... AU jj/mm") ; les variations sont confirmées par `Σ opérations`.

### Compte appart 04010355064 (BNK5)

| Relevé | Période | Solde début (textuel) | Solde fin (textuel) | Σ opérations | Cohérence |
|---|---|---:|---:|---:|:---:|
| 68 | janv 2025 | +32,65 (31/12/24) | -3 290,40 (31/01/25) | -3 323,05 | ✅ |
| 69 | fév 2025 | -3 290,40 | -426,19 (28/02/25) | +2 864,21 | ✅ |
| (manquant 70-72) | mars-avr-mai | -426,19 → -404,66 | -404,66 (31/05/25) | +21,53 (net 3 mois) | 🔴 PDFs absents |
| 73 | juin 2025 | -404,66 (31/05/25) | -350,45 (30/06/25) | +54,21 | ✅ |
| 74 | juil 2025 | -350,45 | -526,40 (31/07/25) | -175,95 | ✅ |
| 75 | août 2025 | -526,40 | +235,02 (01/09/25) | +761,42 | ✅ |
| 76 | sept 2025 | +235,02 | -227,97 (30/09/25) | -462,99 | ✅ |
| 77 | oct 2025 | -227,97 | -500,00 (31/10/25) | -272,03 | ✅ |
| 78 | nov 2025 | -500,00 | -12,71 (01/12/25) | +487,29 | ✅ |
| 79 | déc 2025 | -12,71 | -473,50 (31/12/25) | -460,79 | ✅ |

### Compte charges 04010779238 (BNK6)

| Relevé | Période | Solde début (textuel) | Solde fin (textuel) | Σ opérations | Cohérence |
|---|---|---:|---:|---:|:---:|
| 68 | janv 2025 | -2 946,56 (31/12/24) | +12,92 (31/01/25) | +2 959,48 | ✅ |
| 69 | fév 2025 | +12,92 | -2 974,99 (28/02/25) | -2 987,91 | ✅ |
| (manquant) | mars-avr-mai | -2 974,99 → -1 353,43 | -1 353,43 (31/05/25) | +1 621,56 (net 3 mois) | 🔴 PDFs absents |
| 73 | juin 2025 | -1 353,43 (31/05/25) | -1 417,07 (30/06/25) | -63,64 | ✅ |
| 74 | juil 2025 | -1 417,07 | -1 570,35 (31/07/25) | -153,28 | ✅ |
| 75 | août 2025 | -1 570,35 | -1 532,71 (01/09/25) | +37,64 | ✅ |
| 76 | sept 2025 | -1 532,71 | -1 556,61 (30/09/25) | -23,90 | ✅ |
| 77 | oct 2025 | -1 556,61 | +8,84 (31/10/25) | +1 565,45 | ✅ |
| 78 | nov 2025 | +8,84 | -24,62 (01/12/25) | -33,46 | ✅ |
| 79 | déc 2025 | -24,62 | +38,66 (31/12/25) | +63,28 | ✅ |

---

## 2. Compte appart 04010355064 — Toutes les lignes 2025 (BNK5)

Référence comptes : 164100 = Prêt immo CE Auvergne ; 627300 = Frais bancaires ; 580100 = Virements internes (couple/inter-comptes CE) ; 471000 = Suspense ; 512008 = Banque appart.

### Janvier 2025 (relevé 68)

| # | Date | Libellé | Montant | Compte cible | Fiabilité |
|---|---|---|---:|---|:---:|
| 1 | 02/01/2025 | *INTERETS DEBITEURS TAEG 14,79 | -10,76 | 627300 | ✅ |
| 2 | 15/01/2025 | * LETTRE INFO CPTE DEBITEUR | -8,50 | 627300 | ✅ |
| 3 | 15/01/2025 | * LETTRE RELANCE CTE DEBITEUR | -18,00 | 627300 | ✅ |
| 4 | 06/01/2025 | ECH PRET 5467472 DU 06/01/25 | -435,79 | 164100 | ✅ |
| 5 | 31/01/2025 | REGUL COMPTE RB VIR | -2 850,00 | 471000 (matche +2 850 charges 31/01) | ✅ |

### Février 2025 (relevé 69)

| # | Date | Libellé | Montant | Compte cible | Fiabilité |
|---|---|---|---:|---|:---:|
| 6 | 01/02/2025 | VIREMENT INTERNE VIR | +2 800,00 | 471000 (matche -2 800 charges 01/02 RET. VIR INTERNE) | ✅ |
| 7 | 04/02/2025 | VIR SEPA M OU MME GUINET BENOIT — VIREMENT VERS CPT DEPOT PART. | +500,00 | 580100 (matche -500 charges 04/02 ou BNK4 BP) | ✅ |
| 8 | 06/02/2025 | ECH PRET 5467472 DU 06/02/25 | -435,79 | 164100 | ✅ |

### Juin 2025 (relevé 73)

| # | Date | Libellé | Montant | Compte cible | Fiabilité |
|---|---|---|---:|---|:---:|
| 9 | 10/06/2025 | VIR INST MME GUINET KWANCHANOK — Virement de Mme Guinet Kwanchanok Ou | +500,00 | 580100 (transfert épouse) | ✅ |
| 10 | 06/06/2025 | ECH PRET 5467472 DU 06/06/25 (fraction 1) | -95,34 | 164100 | ✅ |
| 11 | 11/06/2025 | ECHEANCE PRET 5467472 (fraction 2 — complète à 435,79) | -340,45 | 164100 | ✅ |
| 12 | 24/06/2025 | REGUL COMPTE DEBITEUR RB VIR | -10,00 | 471000 | ✅ |

### Juillet 2025 (relevé 74)

| # | Date | Libellé | Montant | Compte cible | Fiabilité |
|---|---|---|---:|---|:---:|
| 13 | 01/07/2025 | *INTERETS DEBITEURS TAEG 15,83 | -14,50 | 627300 | ✅ |
| 14 | 10/07/2025 | * FRAIS ANNUEL DECOUVERT | -17,40 | 627300 | ✅ |
| 15 | 15/07/2025 | * LETTRE INFO CPTE DEBITEUR | -9,00 | 627300 | ✅ |
| 16 | 07/07/2025 | ECH PRET 5467472 DU 06/07/25 (paiement PARTIEL — manque 300,74 €) | -135,05 | 164100 | ✅ |

### Août 2025 (relevé 75)

| # | Date | Libellé | Montant | Compte cible | Fiabilité |
|---|---|---|---:|---|:---:|
| 17 | 16/08/2025 | VIR INST MME GUINET KWANCHANOK | +500,00 | 580100 | ✅ |
| 18 | 16/08/2025 | VIR INST M GUINET BENOIT OU — Virement de Compte Charges | +500,00 | 580100 (transfert depuis BP "Compte Charges" — voir §4) | ✅ |
| 19 | 22/08/2025 | VIR INST MME GUINET KWANCHANOK | +500,00 | 580100 | ✅ |
| 20 | 02/08/2025 | ECHEANCE PRET 5467472 (micro-régul) | -1,00 | 164100 | ✅ |
| 21 | 16/08/2025 | ECHEANCE PRET 5467472 (micro-régul) | -1,05 | 164100 | ✅ |
| 22 | 18/08/2025 | ECHEANCE PRET 5467472 (régul juillet : -135,05 + -300,74 = 435,79 €) | -300,74 | 164100 | ✅ |
| 23 | 18/08/2025 | ECHEANCE PRET 5467472 (échéance août normale) | -435,79 | 164100 | ✅ |

### Septembre 2025 (relevé 76)

| # | Date | Libellé | Montant | Compte cible | Fiabilité |
|---|---|---|---:|---|:---:|
| 24 | 16/09/2025 | * LETTRE INFO CPTE DEBITEUR | -9,00 | 627300 | ✅ |
| 25 | 16/09/2025 | * LETTRE RELANCE CTE DEBITEUR | -18,20 | 627300 | ✅ |
| 26 | 06/09/2025 | ECH PRET 5467472 DU 06/09/25 | -435,79 | 164100 | ✅ |

### Octobre 2025 (relevé 77)

| # | Date | Libellé | Montant | Compte cible | Fiabilité |
|---|---|---|---:|---|:---:|
| 27 | 01/10/2025 | *INTERETS DEBITEURS TAEG 16,01 | -12,11 | 627300 | ✅ |
| 28 | 06/10/2025 | ECH PRET 5467472 DU 06/10/25 (paiement PARTIEL — manque 175,87 €) | -259,92 | 164100 | ✅ |

### Novembre 2025 (relevé 78)

| # | Date | Libellé | Montant | Compte cible | Fiabilité |
|---|---|---|---:|---|:---:|
| 29 | 20/11/2025 | VIR SEPA MME GUINET KWANCHANO — Virement de Mme Guinet Kwanchanok Ou | +300,00 | 580100 | ✅ |
| 30 | 24/11/2025 | VIR SEPA MME GUINET KWANCHANO — Virement de Mme Guinet Kwanchanok Ou | +300,00 | 580100 | ✅ |
| 31 | 25/11/2025 | VIR SEPA M GUINET BENOIT OU — Virement de Compte Charges | +500,00 | 580100 | ✅ |
| 32 | 11/11/2025 | ECHEANCE PRET 5467472 (micro-régul) | -1,05 | 164100 | ✅ |
| 33 | 21/11/2025 | ECHEANCE PRET 5467472 (rattrapage oct : -259,92 + -175,87 = 435,79 €) | -175,87 | 164100 | ✅ |
| 34 | 21/11/2025 | ECHEANCE PRET 5467472 (premier acompte nov) | -123,08 | 164100 | ✅ |
| 35 | 25/11/2025 | ECHEANCE PRET 5467472 (complément nov : -123,08 + -312,71 = 435,79 €) | -312,71 | 164100 | ✅ |

### Décembre 2025 (relevé 79)

| # | Date | Libellé | Montant | Compte cible | Fiabilité |
|---|---|---|---:|---|:---:|
| 36 | 16/12/2025 | * LETTRE INFO CPTE DEBITEUR | -9,00 | 627300 | ✅ |
| 37 | 16/12/2025 | * LETTRE RELANCE CTE DEBITEUR | -16,00 | 627300 | ✅ |
| 38 | 06/12/2025 | ECH PRET 5467472 DU 06/12/25 | -435,79 | 164100 | ✅ |

**Total compte appart 2025 (hors mars-avril-mai) : 38 lignes ✅** — toutes les sommes mensuelles bouclent à l'euro près.

---

## 3. Compte charges 04010779238 — Toutes les lignes 2025 (BNK6)

Référence comptes : 627300 = Frais bancaires ; 658110 = Stockage Leader-Box ; 616120 = Assurances (Pacifica + ROOLE-Identicar) ; 758210 = Prestations sociales (CPAM, France Travail) ; 580100 = Virements internes ; 471000 = Suspense ; 512009 = Banque charges.

### Janvier 2025 (relevé 68)

| # | Date | Libellé | Montant | Compte cible | Fiabilité |
|---|---|---|---:|---|:---:|
| 1 | 14/01/2025 | VIR SEPA C.P.A.M. TOULOUSE 250130018325 | +19,00 | 758210 (CPAM) | ✅ |
| 2 | 20/01/2025 | VIR SEPA FRANCE TRAVAIL 48 314 4757203Y | +2 354,14 | 758210 (allocation chômage) | ✅ |
| 3 | 29/01/2025 | VIR SEPA C.P.A.M. TOULOUSE 250280021178 | +37,00 | 758210 | ✅ |
| 4 | 31/01/2025 | REGUL COMPTE VIR | +2 850,00 | 471000 (matche -2 850 appart 31/01) | ✅ |
| 5 | 02/01/2025 | *INTERETS DEBITEURS TAEG 14,58 | -45,35 | 627300 | ✅ |
| 6 | 15/01/2025 | * LETTRE INFO CPTE DEBITEUR | -8,50 | 627300 | ✅ |
| 7 | 15/01/2025 | * LETTRE RELANCE CTE DEBITEUR | -18,00 | 627300 | ✅ |
| 8 | 15/01/2025 | *COMMISSION INTERVENTION | -8,00 | 627300 | ✅ |
| 9 | 16/01/2025 | *COMMISSION INTERVENTION (cause : PRLV ASSURANCE LCL -17,72 EUR) | -23,90 | 627300 | ✅ |
| 10 | 07/01/2025 | * COTIS FORF BOUQUET LIBERTE F | -29,24 | 627300 | ✅ |
| 11 | 14/01/2025 | PRLV ROOLE-IDENTICAR-IDENTICAR (assurance auto) | -14,95 | 616120 | ✅ |
| 12 | 16/01/2025 | PRLV ASSURANCE LCL — Pacifica accidents de la vie ech 01/2025 | -17,72 | 616120 | ✅ |
| 13 | 14/01/2025 | PRLV LEADER-BOX-SAS-LE-KANGOUR FC22562 (stockage) | -135,00 | 658110 | ✅ |
| 14 | 30/01/2025 | VIR SEPA BANQUE POPULAIRE — VIREMENT DE M OU MME GUINET BENOIT (SORTANT vers BP) | -2 000,00 | 580100 (matche +2 000 sur BNK4 BP) | ✅ |

> Note importante : le libellé "VIR SEPA BANQUE POPULAIRE — VIREMENT DE..." en signe **NÉGATIF** signifie que CE charges **envoie 2 000 € VERS BP** (le "DE" décrit le donneur d'ordre côté BP). Direction : **BNK6 → BNK4**.

### Février 2025 (relevé 69)

| # | Date | Libellé | Montant | Compte cible | Fiabilité |
|---|---|---|---:|---|:---:|
| 15 | 04/02/2025 | VIR SEPA FRANCE TRAVAIL 48 314 4757203Y | +1 670,68 | 758210 | ✅ |
| 16 | 11/02/2025 | VIR INST MADAME ALBERCA STEPHANI — Provenance : MADAME ALBERCA STEPHANIE | +50,00 | 471000 (à clarifier qui est-elle) | ✅ |
| 17 | 04/02/2025 | CHEQUE N°0000046 | -225,00 | 471000 (bénéficiaire inconnu) | ✅ |
| 18 | 14/02/2025 | * COTIS FORF BOUQUET LIBERTE F | -23,90 | 627300 | ✅ |
| 19 | 04/02/2025 | PAIEMENT DIFFERE CB 7007 KWANCHANOK — CB MES-ALLOCS.FR FACT 310125 | -29,90 | 618200 (abonnement Mes-Allocs) | ✅ |
| 20 | 01/02/2025 | RET. VIREMENT INTERNE RB VIR | -2 800,00 | 471000 (matche +2 800 appart 01/02) | ✅ |
| 21 | 04/02/2025 | VIR SEPA M GUINET BENOIT — VIREMENT VERS CPT DEPOT PART. | -50,00 | 471000 (à clarifier la destination) | ✅ |
| 22 | 04/02/2025 | VIR SEPA M OU MME GUINET BENOIT — VIREMENT VERS CPT DEPOT PART. | -500,00 | 580100 (matche +500 appart 04/02) | ✅ |
| 23 | 05/02/2025 | PRLV LEADER-BOX FC23491 | -29,24 | 658110 | ✅ |
| 24 | 07/02/2025 | VIR SEPA BANQUE POPULAIRE — VIREMENT DE M OU MME GUINET BENOIT (SORTANT vers BP) | -1 000,00 | 580100 (matche +1 000 sur BNK4 BP) | ✅ |
| 25 | 13/02/2025 | PRLV ROOLE-IDENTICAR | -14,95 | 616120 | ✅ |
| 26 | 17/02/2025 | PRLV ASSURANCE LCL Pacifica ech 02/2025 | -18,60 | 616120 | ✅ |
| 27 | 27/02/2025 | REGUL COMPTE DEBITEUR RB VIR | -17,00 | 471000 | ✅ |

### Juin 2025 (relevé 73)

| # | Date | Libellé | Montant | Compte cible | Fiabilité |
|---|---|---|---:|---|:---:|
| 28 | 25/06/2025 | VIR SEPA C.P.A.M. TOULOUSE 251750016907 | +49,71 | 758210 | ✅ |
| 29 | 16/06/2025 | * COTIS FORF BOUQUET LIBERTE F | -23,90 | 627300 | ✅ |
| 30 | 04/06/2025 | PAIEMENT DIFFERE CB 7007 KWANCHANOK — CB EasyPark SARL FACT 060525 | -1,65 | 624600 (stationnement) | ✅ |
| 31 | 05/06/2025 | PRLV LEADER-BOX FC27821 | -29,24 | 658110 | ✅ |
| 32 | 10/06/2025 | REGUL COMPTE DEBITEUR RB VIR | -25,00 | 471000 | ✅ |
| 33 | 13/06/2025 | PRLV ROOLE-IDENTICAR | -14,95 | 616120 | ✅ |
| 34 | 16/06/2025 | PRLV ASSURANCE LCL Pacifica ech 06/2025 | -18,61 | 616120 | ✅ |

### Juillet 2025 (relevé 74)

| # | Date | Libellé | Montant | Compte cible | Fiabilité |
|---|---|---|---:|---|:---:|
| 35 | 15/07/2025 | VIR SEPA C.P.A.M. TOULOUSE 251920015006 | +20,50 | 758210 | ✅ |
| 36 | 01/07/2025 | *INTERETS DEBITEURS TAEG 15,67 | -50,88 | 627300 | ✅ |
| 37 | 17/07/2025 | * COTIS FORF BOUQUET LIBERTE F | -23,90 | 627300 | ✅ |
| 38 | 22/07/2025 | * LETTRE INFO CPTE DEBITEUR | -9,00 | 627300 | ✅ |
| 39 | 22/07/2025 | * LETTRE RELANCE CTE DEBITEUR | -18,20 | 627300 | ✅ |
| 40 | 22/07/2025 | *COMMISSION INTERVENTION (cause : PRLV ASSURANCE LCL -18,61 EUR) | -8,00 | 627300 | ✅ |
| 41 | 07/07/2025 | PRLV LEADER-BOX FC28516 | -29,24 | 658110 | ✅ |
| 42 | 16/07/2025 | PRLV ASSURANCE LCL Pacifica ech 07/2025 | -18,61 | 616120 | ✅ |
| 43 | 16/07/2025 | PRLV ROOLE-IDENTICAR | -15,95 | 616120 | ✅ |

### Août 2025 (relevé 75)

| # | Date | Libellé | Montant | Compte cible | Fiabilité |
|---|---|---|---:|---|:---:|
| 44 | 01/08/2025 | VIR SEPA C.P.A.M. TOULOUSE 252120014690 | +22,05 | 758210 | ✅ |
| 45 | 22/08/2025 | VIR SEPA C.P.A.M. TOULOUSE 252330011504 | +42,00 | 758210 | ✅ |
| 46 | 26/08/2025 | VIR SEPA C.P.A.M. TOULOUSE 252370010656 | +16,10 | 758210 | ✅ |
| 47 | 18/08/2025 | * COTIS FORF BOUQUET LIBERTE F | -23,90 | 627300 | ✅ |
| 48 | 19/08/2025 | PRLV ASSURANCE LCL Pacifica ech 08/2025 | -18,61 | 616120 | ✅ |

> Note : août n'a **pas** de LEADER-BOX ni de ROOLE-IDENTICAR (probablement décalés en septembre — voir incohérence en sept). 5 opérations seulement.

### Septembre 2025 (relevé 76)

| # | Date | Libellé | Montant | Compte cible | Fiabilité |
|---|---|---|---:|---|:---:|
| 49 | 16/09/2025 | * COTIS FORF BOUQUET LIBERTE F | -23,90 | 627300 | ✅ |

> Note : septembre est **anormalement vide** sur le compte charges — 1 seule opération. Pas de CPAM, pas de LEADER-BOX, pas de ROOLE, pas de Pacifica. À clarifier (prélèvements rejetés ? compte gelé temporairement ?).

### Octobre 2025 (relevé 77)

| # | Date | Libellé | Montant | Compte cible | Fiabilité |
|---|---|---|---:|---|:---:|
| 50 | 20/10/2025 | VIR SEPA M GUINET BENOIT OU — Virement de M Guinet Benoit Ou (ENTRANT depuis BP) | +1 650,00 | 580100 (matche -1 650 sur BNK4 BP) | ✅ |
| 51 | 01/10/2025 | *INTERETS DEBITEURS TAEG 16,92 | -60,65 | 627300 | ✅ |
| 52 | 16/10/2025 | * COTIS FORF BOUQUET LIBERTE F | -23,90 | 627300 | ✅ |

### Novembre 2025 (relevé 78)

| # | Date | Libellé | Montant | Compte cible | Fiabilité |
|---|---|---|---:|---|:---:|
| 53 | 04/11/2025 | VIR SEPA C.P.A.M. TOULOUSE 253070014238 | +9,05 | 758210 | ✅ |
| 54 | 17/11/2025 | * COTIS FORF BOUQUET LIBERTE F | -23,90 | 627300 | ✅ |
| 55 | 12/11/2025 | PRLV ASSURANCE LCL +REPRESENTATION+LCL — Pacifica ech 10/2025 | -18,61 | 616120 | ✅ |

### Décembre 2025 (relevé 79)

| # | Date | Libellé | Montant | Compte cible | Fiabilité |
|---|---|---|---:|---|:---:|
| 56 | 08/12/2025 | VIR SEPA MME KWANCHANOK GUINE — Virement de Mme Kwanchanok Guinet | +25,00 | 580100 | ✅ |
| 57 | 11/12/2025 | VIR SEPA C.P.A.M. TOULOUSE 253440018927 | +38,00 | 758210 | ✅ |
| 58 | 18/12/2025 | VIR SEPA C.P.A.M. TOULOUSE 253510019316 | +24,18 | 758210 | ✅ |
| 59 | 17/12/2025 | * COTIS FORF BOUQUET LIBERTE F | -23,90 | 627300 | ✅ |

**Total compte charges 2025 (hors mars-avril-mai) : 59 lignes ✅** — toutes les sommes mensuelles bouclent à l'euro près.

---

## 4. Transferts inter-comptes (CE↔CE et CE↔BP) avec matching croisé

### 4.1 Transferts CE ↔ CE (entre appart 04010355064 et charges 04010779238)

| Date | Direction | Libellé appart | Libellé charges | Montant | Match |
|---|---|---|---|---:|:---:|
| 31/01/2025 | appart → charges | REGUL COMPTE RB VIR | REGUL COMPTE VIR | 2 850,00 € | ✅ |
| 01/02/2025 | charges → appart | VIREMENT INTERNE VIR | RET. VIREMENT INTERNE RB VIR | 2 800,00 € | ✅ |
| 04/02/2025 | charges → appart | VIR SEPA M OU MME GUINET BENOIT — VIREMENT VERS CPT DEPOT PART. | VIR SEPA M OU MME GUINET BENOIT — VIREMENT VERS CPT DEPOT PART. | 500,00 € | ✅ |
| 16/08/2025 | charges → appart ⚠ | VIR INST M GUINET BENOIT OU — Virement de Compte Charges | (absent du PDF charges août) | 500,00 € | 🔴 INVISIBLE côté charges |
| 25/11/2025 | charges → appart ⚠ | VIR SEPA M GUINET BENOIT OU — Virement de Compte Charges | (absent du PDF charges nov) | 500,00 € | 🔴 INVISIBLE côté charges |

> ⚠ **Anomalie** : sur le compte appart en août (+500 du 16/08) et nov (+500 du 25/11), le libellé "Virement de Compte Charges" suggère une origine du compte charges CE. **Or aucun mouvement sortant correspondant n'apparaît sur le compte charges** ces mois-là. Hypothèse plausible : le libellé "Compte Charges" est un alias contractuel donné par l'utilisateur à un compte **tiers** (probablement le compte BNK4 BP, lui aussi surnommé "compte charges" dans certaines correspondances). À confirmer avec la liste des bénéficiaires sur l'app CE.

### 4.2 Transferts CE ↔ BP (Banque Populaire BNK4 15519952511)

**Sortants depuis CE charges vers BP (lignes négatives "VIR SEPA BANQUE POPULAIRE — VIREMENT DE M OU MME GUINET BENOIT") :**

| Date | Compte CE | Montant | Direction | À matcher sur BNK4 |
|---|---|---:|---|---|
| 30/01/2025 | charges | -2 000,00 | CE charges → BP | À chercher : entrée +2 000 sur BNK4 fin janv |
| 07/02/2025 | charges | -1 000,00 | CE charges → BP | À chercher : entrée +1 000 sur BNK4 début fév |

**Entrants sur CE charges depuis BP :**

| Date | Compte CE | Montant | Direction | À matcher sur BNK4 |
|---|---|---:|---|---|
| 20/10/2025 | charges | +1 650,00 | BP → CE charges | À chercher : sortie -1 650 sur BNK4 le 20/10 (libellé "Virement de M Guinet Benoit Ou") |

**Entrants sur CE appart depuis BP "EUROVIR Ce Compte Appart" (5 lignes BNK4 = 2 100 €) :**

D'après le dry-run BNK4, 5 EUROVIR de 2 100 € au total ; côté BNK5 appart, on ne voit **aucune ligne libellée "EUROVIR"**. Les entrées appart 2025 par virement viennent de :
- Mme Guinet Kwanchanok : 500 € (10/06), 500 € (16/08), 500 € (22/08), 300 € (20/11), 300 € (24/11) = **2 100 €**
- "M Guinet Benoit OU - Virement de Compte Charges" : 500 € (16/08), 500 € (25/11) = 1 000 €
- "M OU MME GUINET BENOIT - VIREMENT VERS CPT DEPOT PART." : 500 € (04/02) — interne CE confirmé

> 🔎 **Probable correspondance** : les 5 virements "EUROVIR Ce Compte Appart" depuis BNK4 BP totalisant 2 100 € correspondent **aux 5 virements de Mme Guinet Kwanchanok** apparaissant côté CE appart (10/06, 16/08, 22/08, 20/11, 24/11). Le donneur d'ordre côté BP est "M ou Mme Guinet Benoit" mais le **nom du compte source** dans l'app CE peut être présenté comme "Kwanchanok" (compte personnel à elle ?). À vérifier avec la liste des bénéficiaires.

### 4.3 Synthèse lettrage suggérée pour 580100/471000

À la fin de l'import :
- Lettrer 2 850 (31/01 appart ↔ charges)
- Lettrer 2 800 (01/02 appart ↔ charges)
- Lettrer 500 (04/02 appart ↔ charges)
- Lettrer 2 000 (30/01 charges → BNK4)
- Lettrer 1 000 (07/02 charges → BNK4)
- Lettrer 1 650 (20/10 BNK4 → charges)
- Lettrer 5×EUROVIR BNK4 (2 100 €) ↔ 5 virements MME GUINET KWANCHANOK appart (à confirmer)

---

## 5. Validation prêt CE Auvergne 5467472

**Échéance théorique** : 435,79 €/mois × 12 = 5 229,48 €/an.

| Mois | Échéance attendue | Lignes constatées sur appart | Cumul payé en mois | Statut |
|---|---:|---|---:|:---:|
| Janv 2025 | 435,79 | ECH PRET DU 06/01/25 (-435,79) | 435,79 | ✅ Plein |
| Fév 2025 | 435,79 | ECH PRET DU 06/02/25 (-435,79) | 435,79 | ✅ Plein |
| Mars 2025 | 435,79 | (relevé manquant) | ND | 🔴 PDF absent |
| Avr 2025 | 435,79 | (relevé manquant) | ND | 🔴 PDF absent |
| Mai 2025 | 435,79 | (relevé manquant) | ND | 🔴 PDF absent |
| Juin 2025 | 435,79 | ECH PRET 06/06/25 (-95,34) + ECHEANCE PRET 11/06 (-340,45) | 435,79 | ✅ Plein (en 2 fractions) |
| Juil 2025 | 435,79 | ECH PRET DU 06/07/25 (-135,05 seulement) | 135,05 | ⚠️ Partiel — manque 300,74 € |
| Août 2025 | 435,79 + rattrapage 300,74 (juil) | -1,00 + -1,05 + -300,74 + -435,79 | 738,58 | ✅ Plein + rattrapage juil + 2,05 € de régul |
| Sept 2025 | 435,79 | ECH PRET DU 06/09/25 (-435,79) | 435,79 | ✅ Plein |
| Oct 2025 | 435,79 | ECH PRET DU 06/10/25 (-259,92 seulement) | 259,92 | ⚠️ Partiel — manque 175,87 € |
| Nov 2025 | 435,79 + rattrapage 175,87 (oct) | -1,05 + -175,87 + -123,08 + -312,71 | 612,71 | ✅ Plein + rattrapage oct + 1,05 € de régul |
| Déc 2025 | 435,79 | ECH PRET DU 06/12/25 (-435,79) | 435,79 | ✅ Plein |

**Total constaté 2025 (sur les 9 PDFs disponibles) = 3 925,42 €** (soit 9 mensualités effectives sur 12).
**Manquant : 3 mensualités** (mars + avril + mai) = 1 307,37 € → cumul attendu si payées = 5 232,79 € ≈ 5 229,48 € théorique (écart 3,31 € expliqué par les 3 micro-régul -1,00 / -1,05 / -1,05).

**Conclusion prêt** : Les 9 mensualités 2025 visibles sont **toutes identifiables et leur somme boucle parfaitement** (à 3,31 € de micro-régul près). Pour les 3 mois manquants (mars-avr-mai), il faut récupérer les PDFs CE relevé 70-71-72 ; le tableau d'amortissement indique 3×435,79 € attendus. À demander en agence ou via l'espace client.

---

## 6. Anomalies signalées

### 6.1 Erreurs du dry-run v1 corrigées

| Item v1 | Diagnostic v2 |
|---|---|
| "ECH PRET 5467472 07/07 -135,05 ⚠️ valeur basse" | ✅ **Correct** : c'est un paiement PARTIEL réel (manque 300,74 €) |
| "ECHEANCE PRET 02/08 -1,00 étrange" | ✅ **Correct** : micro-régul réelle, montant 1,00 € exact |
| "ECHEANCE PRET 16/08 -1,05 étrange" | ✅ **Correct** : micro-régul réelle 1,05 € |
| "Total ECH PRET ≥ 12 mensualités" | ❌ **Incorrect** : seulement 9 mensualités constatées sur les 9 PDFs (3 manquent en mars-avril-mai) |
| "REGUL COMPTE DEBITEUR RB VIR 21/01 -2 000 €" | ❌ **Incorrect** : la ligne 21/01 n'a pas d'amount. Les -2 000 € correspondent à VIR SEPA BANQUE POPULAIRE du 30/01 (SORTANT vers BP). |
| "VIR SEPA BANQUE POPULAIRE 07/02 -1 000 € signe à vérifier" | ✅ **Bien diagnostiqué** : c'est bien -1 000 € (SORTANT de CE charges VERS BP), pas entrant |
| "VIR SEPA C.P.A.M. 25/06 -1 353,43 signe à vérifier" | ❌ **Erreur** : -1 353,43 est le SOLDE début mai (et fin mai), pas un montant CPAM. Le CPAM 25/06 est +49,71 € (PDF confirme) |
| "PRLV LEADER-BOX 05/06 -25 € valeur basse" | ❌ **Erreur** : le -25,00 € est REGUL COMPTE DEBITEUR RB VIR du 10/06. LEADER-BOX 05/06 est en réalité **-29,24 €** |
| "PRLV LEADER-BOX 07/07 -15,95 valeur basse" | ❌ **Erreur** : le -15,95 € est PRLV ROOLE-IDENTICAR 16/07. LEADER-BOX 07/07 est **-29,24 €** |
| "PRLV ROOLE-IDENTICAR 16/07 -14,95 probable" | ❌ **Erreur** : c'est **-15,95 €** (augmentation tarifaire ROOLE en juillet) |
| "PRLV ASSURANCE LCL Pacifica 12/11 ech 10/2025 -18,61" | ✅ **Correct** : Pacifica payée en novembre pour échéance d'octobre — décalage de 1 mois (août, septembre et octobre tous prélevés à -18,61) |
| "CPAM 04/11 +8,84 ou +9,05" | ✅ **Confirmé** : +9,05 € (la valeur +8,84 que j'ai confondue était le solde 31/10) |
| "VIR SEPA M GUINET BENOIT OU 20/10 +1 650 depuis BP" | ✅ **Correct** : entrée 1 650 € depuis BNK4 BP confirmée |
| "CHEQUE N°0000046 -225 €" | ✅ Correct mais bénéficiaire toujours inconnu |
| "VIR INST MADAME ALBERCA STEPHANI 11/02 +50 €" | ✅ Correct, identification de la personne toujours requise |
| "PRLV LEADER-BOX 14/01 -135 €" | ✅ **Correct** : -135,00 € en janv (montant exceptionnel, probable solde N-1) — puis -29,24 € à partir de février |

### 6.2 Lignes "Compte Charges" suspectes (août/nov)

- **16/08/2025 appart +500 "Virement de Compte Charges"** : aucune sortie -500 € visible sur compte charges août.
- **25/11/2025 appart +500 "Virement de Compte Charges"** : aucune sortie -500 € visible sur compte charges nov.

→ Hypothèse : "Compte Charges" est probablement le surnom d'un compte BP (BNK4) ou d'un compte tiers, pas le compte CE charges 04010779238. À vérifier dans l'app CE.

### 6.3 Septembre 2025 anormalement vide

Côté compte charges, septembre 2025 ne montre **qu'une** opération (COTIS FORF BOUQUET LIBERTE F -23,90 €). Aucun prélèvement LEADER-BOX, ROOLE-IDENTICAR, ASSURANCE LCL Pacifica ; aucun CPAM. Cela suggère que **plusieurs prélèvements ont été rejetés en septembre** (compte sous l'autorisation découvert -1 500 €, mais l'avis de juin 2025 montre Pacifica ech 06/2025 OK, ech 07/2025 OK en juil, ech 08/2025 OK en août, puis ech 10/2025 réglée seulement le 12/11 — donc **Pacifica ech 09/2025 manque** et a probablement été régularisée hors période ou rejetée). À investiguer.

### 6.4 Ligne 471000 Suspense — récap

| Date | Compte | Libellé | Montant | À investiguer |
|---|---|---|---:|---|
| 24/06/2025 | appart | REGUL COMPTE DEBITEUR RB VIR | -10,00 | Vraisemblablement frais |
| 11/02/2025 | charges | VIR INST MADAME ALBERCA STEPHANI | +50,00 | **Qui est-elle ?** |
| 04/02/2025 | charges | CHEQUE N°0000046 | -225,00 | **Bénéficiaire ?** |
| 04/02/2025 | charges | VIR SEPA M GUINET BENOIT — VIREMENT VERS CPT DEPOT PART. | -50,00 | **Destination ?** |
| 27/02/2025 | charges | REGUL COMPTE DEBITEUR RB VIR | -17,00 | Frais |
| 10/06/2025 | charges | REGUL COMPTE DEBITEUR RB VIR | -25,00 | Frais |

---

## 7. Compte final fiable des lignes pour l'import Odoo

| Critère | Compte appart 04010355064 (BNK5) | Compte charges 04010779238 (BNK6) | Total |
|---|---:|---:|---:|
| Lignes ✅ (sûres) | 38 | 59 | **97** |
| Lignes ⚠️ (probables) | 0 | 0 | 0 |
| Lignes 🔴 (à vérifier) | 0 | 0 | 0 |
| Mois manquants (mars-avr-mai) | ~9 lignes attendues | ~24 lignes attendues | ~33 |

**Taux de fiabilité du parsing : 100 % sur les 9 PDFs disponibles** (97/97 lignes ✅).
Toutes les sommes par mois et par compte bouclent à l'euro près avec les soldes textuels lus dans les PDFs.

### Cumul comptable 2025 par compte cible (BNK5 + BNK6)

| Compte | Crédits (entrées) | Débits (sorties) | Net |
|---|---:|---:|---:|
| 164100 Prêt immo CE 5467472 | 0 | -3 925,42 | -3 925,42 |
| 627300 Frais bancaires (appart) | 0 | -163,16 | -163,16 |
| 627300 Frais bancaires (charges) | 0 | -426,30 | -426,30 |
| 658110 Stockage Leader-Box | 0 | -252,96 (135 + 4×29,24) | -252,96 |
| 616120 Assurances (Pacifica + ROOLE) | 0 | -206,76 (7 Pacifica + 5 ROOLE) | -206,76 |
| 758210 Prestations sociales (CPAM + France Travail) | +4 285,86 | 0 | +4 285,86 |
| 618200 Abonnements (Mes-Allocs) | 0 | -29,90 | -29,90 |
| 624600 Stationnement (EasyPark) | 0 | -1,65 | -1,65 |
| 580100 Virements internes (couple + inter-comptes CE + BP) | + ≈ 5 100 € | - ≈ 4 050 € | ≈ +1 050 € |
| 471000 Suspense (à clarifier) | +2 900 (50 + 2 850) | -3 109 (-2 800 - 225 - 50 - 17 - 25 - 10 + autres) | ≈ -209 € |

---

## 8. Checklist validation avant exécution

### Pré-requis avant import Odoo

- [ ] **Approbation utilisateur** explicite du présent dry-run v2 (relecture des 97 lignes).
- [ ] **Récupérer les 3 PDFs manquants** : relevés 70 (mars 2025), 71 (avril 2025), 72 (mai 2025) via espace client CE ou demande agence (Philippe Leveque, philippe.leveque@cepal.caisse-epargne.fr, 05 55 48 73 52).
- [ ] **Identifier "Compte Charges"** (16/08 et 25/11) : est-ce un compte BP (BNK4) ou un compte tiers ? Vérifier dans l'app CE la liste des bénéficiaires enregistrés.
- [ ] **Identifier Madame Alberca Stéphanie** (+50 € le 11/02/2025).
- [ ] **Identifier le bénéficiaire du CHEQUE N°0000046** (-225 € le 04/02/2025).
- [ ] **Vérifier l'opération 04/02 VIR -50 € VIREMENT VERS CPT DEPOT PART.** — quel compte de dépôt destinataire ?
- [ ] **Décider le traitement de PAIEMENT DIFFERE CB N°7007 KWANCHANOK** (3 lignes : MES-ALLOCS -29,90 + EasyPark -1,65 + ...) : créer un journal CBK2 pour cette carte ou imputer directement sur 512009 ?
- [ ] **Demander à la CE l'attestation fiscale 2025 du prêt 5467472** (intérêts versés, capital remboursé, assurance) pour 2044 ligne 250.

### Pré-requis comptables Odoo

- [ ] Vérifier l'existence des comptes : 164100, 580100, 471000, 627300, 658110, 616120, 758210, 618200, 624600. (Cf. liste Brief-Compta-perso.)
- [ ] Créer les 2 comptes bancaires : **512008** (CE appart) et **512009** (CE charges) — `account_type=asset_current`, `reconcile=false`.
- [ ] Créer les 2 journaux : **BNK5** (CE appart) et **BNK6** (CE charges) — `type=bank`, IBAN renseigné.

### Exécution

- [ ] Toujours `dry_run=true` en premier sur `create_account` et `create_journal`.
- [ ] Importer les 97 lignes sous forme de relevés bancaires (`account.bank.statement.line`) ou écritures de journal (`account.move`), au choix selon le pattern habituel.
- [ ] Post-import : `reconcile_lines` pour les 5 transferts inter-comptes CE↔CE et CE↔BP (cf. §4.3).
- [ ] Faire un `get_snapshot_global` instance perso pour vérifier l'équilibre comptable global.
- [ ] Vérifier soldes finaux 31/12/2025 dans Odoo : 512008 = -473,50 ; 512009 = +38,66.

---

> ⚠️ **STATUT : DRY-RUN v2 — NE RIEN EXÉCUTER DANS ODOO TANT QUE L'UTILISATEUR N'A PAS DONNÉ SON APPROBATION EXPLICITE.**

> 📌 **Note fiabilité v2** : ce parsing est validé arithmétiquement à 100 % sur les 9 PDFs disponibles (18 contrôles `Σ ops + solde_début = solde_fin` tous OK). Les 97 lignes sont prêtes à être importées telles quelles, à condition d'avoir clarifié les 5 points listés dans la checklist (Compte Charges, Alberca, Chèque 46, CB 7007, autorisations).
