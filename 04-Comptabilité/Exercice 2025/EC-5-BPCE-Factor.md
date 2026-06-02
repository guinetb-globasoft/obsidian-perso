---
tags: ["comptabilité", "guinet-digital-group", "exercice-2025", "expert-comptable", "affacturage", "bpce-factor"]
created: 2026-05-21
destinataire: Super Compteur
société: Guinet Digital Group
company_id_odoo: 4
---

# Dossier BPCE Factor — Exercice 2025

> Année de démarrage du contrat d'affacturage. 12 bordereaux Sohoft/GA SAS/ONE PINK pour ~118 K€ de créances cédées. Document consolidé : schéma comptable, liste des bordereaux, ODs Odoo correspondantes, écart résiduel à arbitrer.

## 1. Contrat & paramétrage

| Élément | Valeur |
|---|---|
| Affactureur | BPCE FACTOR (Natixis Factor) |
| Partner Odoo | id 410 |
| Démarrage | Juillet 2025 (premier bordereau 0004063731 le 04/07/2025) |
| Nature contrat | Affacturage classique avec fonds de garantie 10 % |
| Tiers cédés | Sohoft Toulouse (id 411xxx), GA SAS Sébastien Thalamy, ONE PINK |
| Limite contrat | Atteinte en T4 2025 → 1 commission "Remise suppl. limite contrat" 308 € HT (FACTO/2025/12/0006) |

## 2. Comptes utilisés

| Code Odoo | ID | Libellé | Usage |
|---|---:|---|---|
| **4671** | 3151 | Compte courant BPCE Factor | Db cession (90 %), Cr décaissement BNK1, Cr commissions et intérêts |
| **4676** | 3152 | Fonds de garantie BPCE Factor | Db constitution (10 % de chaque cession), Cr libération mensuelle |
| **6225** | 3150 | Commissions d'affacturage | Db commission affacturage HT (charge) |
| **661600** | 1443 | Bank and financing interest | Db commission financement (intérêts mensuels, charge) |
| **445660** | 1194 | Deductible VAT on other goods and services | Db TVA déductible sur toutes les commissions |
| **411100** | 1149 | Customers | Cr créance client cédée (sortie du compte client) |
| Journal **FACTO** | 61 | BPCE Factor | Toutes les écritures liées à l'affacturage |

## 3. Schéma comptable

### 3.1 À la cession d'une créance (bordereau)

Pour une créance client Sohoft de 13 986 € TTC (exemple FACTO/2025/07/0002) :

```
Dr 4671 Compte courant Factor    ≈ 12 587 € (90 % brut - commissions HT - TVA)
Dr 4676 Fonds garantie           1 398,60 € (10 %)
Dr 6225 Commission affacturage   X € HT (variable selon contrat)
Dr 445660 TVA déductible         X × 20 %
  Cr 411100 Sohoft Toulouse      13 986 € (créance cédée)
```

> Variante bordereau 04/07/2025 (FACTO/2025/07/0002) — exception : commission affacturage HT 412,59 € initialement saisie comme frais dossier 750 € → corrigée le 10/05/2026 (button_draft → modify → post via tool MCP `unpost_journal_entry` créé pour l'occasion).

### 3.2 Décaissement BNK1 (J+0 à J+1)

```
Dr 512001 BNK1     ≈ 12 587 €
  Cr 4671 Compte courant Factor  ≈ 12 587 €
```

### 3.3 Libération mensuelle fonds de garantie (M+1)

Calculée par BPCE Factor au prorata. Exemple août 2025 :

```
Dr 4671 Compte courant Factor    1 398,60 €
  Cr 4676 Fonds garantie         1 398,60 €
```

### 3.4 Commission de financement (intérêts mensuels)

Décomptes adressés en fin de mois par BPCE Factor :

```
Dr 661600 Intérêts financement    X € HT
Dr 445660 TVA déductible          X × 20 %
  Cr 4671 Compte courant Factor   X € TTC
```

### 3.5 Lettrage final

Chaque bordereau dispose d'une **paire** (Db cession 4671 ↔ Cr décaissement 4671) à lettrer formellement via `reconcile_lines` Odoo (full_reconcile_id). Sur l'année, on a aussi des paires complexes où plusieurs cessions sont décaissées en un seul virement BNK1.

## 4. Liste des bordereaux et ODs 2025

> 29 OD postées dans le journal FACTO en 2025 (29 OD côté FACTO, vs 17 lors du diagnostic 09/05/2026 — Phase D du 10/05 a complété les régularisations).

### 4.1 Cessions par mois

| Date | Bordereau BPCE | Tiers cédé | Montant TTC | OD Odoo | Paire Db/Cr |
|---|---|---|---:|---|---|
| 04/07/2025 | 0004063731 | Sohoft | 13 986,00 € | FACTO/2025/07/0001 (extourne MISC1) + FACTO/2025/07/0002 (cession) | id 5458 + 5459 |
| 01/08/2025 | 0004083820 | Sohoft | 13 230,00 € | FACTO/2025/08/0001 + 08/0002 | id 5462 + 5463 |
| 01/09/2025 | 0004100394 | Sohoft | 8 694,00 € | FACTO/2025/09/0001 + 09/0002 | id 5466 + 5467 |
| 04/09/2025 | 0004103730 | GA SAS | 2 484,00 € | FACTO/2025/09/0003 + 09/0004 | id 5469 + 5470 |
| 29/09/2025 | 0004120366 | GA SAS | 6 880,20 € | FACTO/2025/09/0005 + 09/0006 | id 5472 + 5473 |
| 02/10/2025 | 0004122927 | Sohoft | 16 254,00 € | FACTO/2025/10/0001 | id 5448 |
| 08/10/2025 | 0004129637 | GA SAS | 5 112,00 € | FACTO/2025/10/0002 | id 5449 |
| 08/10/2025 | 0004130032 | ONE PINK | 1 620,00 € | FACTO/2025/10/0003 | id 5450 |
| 31/10/2025 | 0004146709 | Sohoft | 15 876,00 € | FACTO/2025/10/0004 | id 5451 |
| 01/12/2025 | 0004168484 | GA SAS + Sohoft | 19 854,00 € | FACTO/2025/12/0001 | id 5452 |
| 16/12/2025 | 0004181963 | GA SAS | 7 128,00 € | FACTO/2025/12/0002 | id 5453 |
| 24/12/2025 | 0004188700 | Sohoft | 13 230,00 € | FACTO/2025/12/0003 | id 5454 |
| **TOTAL cessions 2025** | | | **~124 K€** | | |

### 4.2 Commissions de financement mensuelles

| Mois | OD Odoo | Montant TTC |
|---|---|---:|
| Juillet | FACTO/2025/07/0003 (id 6228) | 89,41 € |
| Août | FACTO/2025/08/0003 (id 6229) | 110,15 € |
| Septembre | FACTO/2025/09/0007 (id 6230) | 94,97 € |
| Octobre | FACTO/2025/10/0005 (id 6231) | 193,63 € |
| Novembre | FACTO/2025/11/0001 (id 6232) | 197,53 € |
| Décembre | FACTO/2025/12/0004 (id 6233) | 215,09 € |
| **Total commissions financement** | | **900,78 € TTC** (~750,65 € HT + ~150,13 € TVA) |

### 4.3 Libérations fonds garantie mensuelles

| Mois | OD Odoo | Montant |
|---|---|---:|
| Août | FACTO/2025/08/0004 (id 6234) | 1 398,60 € |
| Septembre | FACTO/2025/09/0008 (id 6235) | 1 323,00 € |
| Octobre | FACTO/2025/10/0006 (id 6236) | 606,60 € |
| Novembre | FACTO/2025/11/0002 (id 6237) | 2 313,42 € |
| Décembre | FACTO/2025/12/0005 (id 6238) | 2 599,20 € |
| **Total libérations FG 2025** | | **8 240,82 €** |

### 4.4 Commissions diverses

| Type | OD Odoo | Montant TTC |
|---|---|---:|
| Remise suppl. dépassement limite contrat | FACTO/2025/12/0006 (id 6239) | 369,60 € (308 € HT + 61,60 € TVA) |

## 5. Soldes au 21/05/2026

| Compte | Lignes non lettrées | Net | Interprétation |
|---|---:|---:|---|
| 4671 Compte courant BPCE Factor | 48 | **-7 622 € créditeur** | Décaissements et commissions > cessions à fin 2025 (mais cession contre-FAC déjà constatée, donc compensé partiellement) |
| 4676 Fonds garantie | 22 | **+9 341 € débit** | 17 582 € retenu - 8 241 € libéré au prorata |

## 6. Lettrage réalisé / restant

### 6.1 ✅ Réalisé au 10/05/2026 (Phase D)
- 7 paires lettrées (~70 K€) :
  - 3 paires Factor 2026 (FACTO 01/02/03)
  - 3 paires Factor 2025 simples : juillet 11 192 € + septembre 5 949 € + décembre 11 470 €
  - 1 paire Factor 2025 complexe août : FACTO cession + libération FG juillet + commission financement juillet ↔ BNK1 = 12 837 €
- 24 OD créées/modifiées (12 régul FACTO + 6 commissions financement + 5 libérations FG + 1 commission diverse)

### 6.2 🟡 Restant à faire (~1-2h)
- **Paires complexes restantes** : septembre (Sohoft + GA SAS), octobre (4 bordereaux), novembre, décembre — décaissements partiels et libérations entremêlées
- **Décaissement spécial 03/11/2025** (6 466,36 € BNK1 ↔ 4671) : déjà comptabilisé côté BNK1, à inclure dans le lettrage global
- **Identifier l'écart résiduel ~511 €** sur compte 4676 (notre calc 4 194 € vs relevé Factor 3 682,80 €)

## 7. Question à votre intention

### Écart résiduel 4676 ~511 €
Nous avons un écart de calcul entre :
- Solde Odoo 4676 au 21/05/2026 : **+9 341 € débit**
- Cumul théorique selon nos suivis : ~10 % × 124 K€ - libérations 8 241 € = **+12 159 €**

L'écart de ~2 818 € s'explique probablement par :
- des cessions ré-évaluées (avoirs partiels par BPCE Factor)
- ou des taux de retenue variables selon le tiers cédé

→ Votre validation sur **la méthode de calcul du fonds garantie** (10 % flat vs taux variable) éviterait des heures de rapprochement bordereau par bordereau.

### Schéma comptable 6225 vs 622500
Nous avons créé un **sous-compte 6225 spécifique** "Commissions d'affacturage" plutôt que d'utiliser 622500 standard (Études et recherches). Préférez-vous :
- **Option 1** : conserver 6225 (lecture comptable directe)
- **Option 2** : reclasser tout en 622500 et créer une analyse interne pour le détail

### Commissions financement en 661600 vs 627800
Nous utilisons 661600 (intérêts bancaires) pour la commission de financement BPCE Factor. Certains cabinets préfèrent 627800 (autres services bancaires). À votre convenance.

## 8. PDFs disponibles localement

`C:\Users\Shadow\Downloads\Factor BPCE\` contient 32 PDFs :
- 12 bordereaux d'achat
- 12 relevés CC affacturage mensuels (juil→déc 2025 + jan→avr 2026)
- 8 décomptes de commissions

Disponibles sur demande pour audit / contrôle. Pas tous attachés à Odoo aujourd'hui (à industrialiser).

## Liens

- Synthèse 2025 : [[EC-1-Synthese-2025]]
- Mapping comptes : [[EC-2-Mapping-Comptes-2025]]
- Dossiers à arbitrer : [[EC-3-Dossiers-A-Arbitrer]]
- État de la situation interne (détail méthodologique du nettoyage Factor — section 9 du doc principal) : [[00-Etat-de-la-situation]]
