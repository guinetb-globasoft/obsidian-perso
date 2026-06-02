---
tags: ["comptabilité", "guinet-digital-group", "exercice-2025", "expert-comptable", "plan-comptable"]
created: 2026-05-21
destinataire: Super Compteur
société: Guinet Digital Group
company_id_odoo: 4
---

# Mapping plan comptable Odoo ↔ codes SAGE — Exercice 2025

> Suite du mapping 2024 ([[Exercice 2024/06-Plan-Comptable-GDG-Mapping]]). Au cours de 2025 nous avons utilisé **7 comptes supplémentaires** (création ou activation) au-delà du mapping initial. Le reste du plan 2024 est inchangé.

## 1. Comptes activés ou créés en 2025

### 1.1 Comptes existants dans Odoo, utilisés pour la 1ère fois en 2025

| Code Odoo | Libellé Odoo | ID | Code SAGE équivalent | Usage 2025 |
|---|---|---:|---|---|
| 615200 | Maintenance and repairs on real property items | 1338 | 615200 ou 615500 | Carburant véhicule (TotalEnergies, Certas, Dyneff) — 5 lignes ~252 € |
| 615500 | Maintenance and repairs on movable property items | 1339 | 615500 | Entretien véhicule (France Auto) — 2 lignes 1 045 € |
| 618500 | Colloquium, seminar, conference costs | 1351 | 618500 | Formations (Ecom Blueprint 697 €, Udemy 15 €) |
| 623100 | Announcements and advertisements | 1362 | 623100 | Imprimerie/communication (Copy Top Paris 693 €, Copy Top Toulouse 23 €) |
| 625600 | Missions | 1378 | 625600 | Déjeuners pris seul / en équipe interne (L'arbre Rose, API Newgen, API Restauration, NDF restos) |
| 626000 | Postal and telecommunication costs | 1380 | 626000 | Téléphonie SFR 74 € + La Poste 383 € + Adobe (IE 20% UE) 91 € + Screencastify (US autoliq) 140 € |
| 740000 | Operating grants | 1532 | 740000 | 5 versements DRFIP Île-de-France (aide unique apprentissage) 2 500 € |

### 1.2 Comptes créés en Phase 2 (10/05/2026) spécifiques au dossier Factor

| Code Odoo | Libellé Odoo | ID | Code SAGE équivalent | Usage 2025 |
|---|---|---:|---|---|
| **4671** | Compte courant BPCE Factor | 3151 | 467100 ou compte dédié | Cessions FACTO ↔ décaissements bancaires |
| **4676** | Fonds de garantie BPCE Factor | 3152 | 467600 ou compte dédié | 10 % retenu sur chaque cession, libéré au prorata du mois suivant |
| **6225** | Commissions d'affacturage | 3150 | 622500 ou sous-compte 622 | Commissions affacturage BPCE Factor (~5 436 € total dont une commission sur dépassement limite contrat 308 € HT) |
| **661600** | Bank and financing transaction interest | 1443 | 661xxx | Intérêts de financement BPCE Factor (~751 € HT sur juillet→décembre 2025) |

### 1.3 Sous-comptes TVA spécifiques utilisés en 2025

| Code Odoo | Libellé Odoo | ID | Usage 2025 |
|---|---|---:|---|
| 445660 | Deductible VAT on other goods and services | 1194 | TVA déductible standard (FR + UE classique avec dédouanement) |
| **445662** | Intra-Community deductible VAT | 1195 | TVA déductible **autoliquidation UE** (Adobe IE, Patreon IE, Microsoft 365 IE…) |
| 445710 | VAT collected | 1199 | TVA collectée FAC clients |
| 445740 | VAT collected on unsettled transactions | 1200 | TVA en attente sur prestations non encore réglées (utilisé par MISC2/2025/11/0001 — anomalie résiduelle, voir [[EC-3-Dossiers-A-Arbitrer]] §B) |

## 2. Comptes utilisés en 2025 qui n'apparaissaient pas en 2024 (récapitulatif compact)

> Pour le rapprochement avec votre TB / FEC. Les soldes ci-dessous sont des cumuls 2025 indicatifs (à confirmer sur balance générale d'Odoo).

| Code | Libellé | Lignes 2025 | Cumul HT estimé | Catégorie SAGE |
|---|---|---:|---:|---|
| 606100 | Carburant / fournitures non stockables | 30+ | ~1 600 € | 60 Achats |
| 606300 | Petits équipements | 2 | ~145 € | 60 Achats |
| 606400 | Fournitures administratives | quelques | ~ — | 60 Achats |
| 613200 | Locations immobilières | 14 | 8 022 € | 61 |
| 613500 | Locations mobilières (domiciliation Digidom) | 13 | 590 € | 61 |
| 615200 | Carburant véhicule | 5 | 252 € | 61 |
| 615500 | Entretien véhicule | 2 | 1 045 € | 61 |
| 615600 | Maintenance / abonnements SaaS | ~300+ | ~ — | 61 |
| 616100 | RCP — BPCE IARD | 11 | 3 332 € | 61 |
| 616160 | Assurance emprunt — BPCE Vie | 12 | 72 € | 61 |
| 618500 | Formations | 2 | 712 € | 61 |
| 622600 | Honoraires (Super Compteur, Sohoft sous-traitance, JOCH/Tounaj/Rhesotech) | 30+ | ~ — | 62 |
| 623100 | Annonces / impressions | 4 | 600 € | 62 |
| 623400 | Cadeaux clientèle (Le Tire Bouchon, Wonderbox) | 4 | 290 € | 62 |
| **6225** | Commissions d'affacturage | 14 | 4 686 € | 62 (sous-compte spécifique) |
| 625100 | Déplacements (avion, train, EasyPark, Vélo Toulouse, Uber, Indigo) | 30+ | ~1 050 € | 62 |
| 625600 | Missions (déjeuners solo/équipe) | 16+ | ~284 € | 62 |
| 625700 | Réceptions (repas avec invités) | 70+ | ~3 100 € | 62 |
| 626000 | Postal et télécoms (incl. Adobe/Screencastify) | 10 | 614 € | 62 |
| 627000 | Frais bancaires BPCE | 32 | 2 439 € | 62 |
| 647100 | Indemnités directes (NDF salarié) | 6 | 341 € | 64 |
| 648100 | Tickets restaurants — quote-part employeur (Up France) | 13 | 1 832 € | 64 |
| **661600** | Intérêts financement BPCE Factor | 6 | 751 € | 66 |
| 740000 | Subventions d'exploitation (DRFIP — aide apprenti) | 5 | 2 500 € | 74 (produit) |

## 3. Comptes non utilisés en 2025 (vs. attendu)

| Code | Raison | Statut |
|---|---|---|
| 421000 / 431000 / 437xxx | **Aucune OD de paie 2025 saisie** | 🔴 À reprendre — voir [[EC-3-Dossiers-A-Arbitrer]] §A |
| 641xxx | Idem (salaires bruts) | 🔴 À reprendre |
| 645xxx | URSSAF/Klesia comptabilisés en paiement direct (sans OD de paie miroir) | 🔴 À reprendre |
| 681120 | **Aucune dotation amort. 2025 Citroën C5** | 🔴 6 000 € à passer |
| 110000 | Vide (affectation résultat 2024 non passée) | 🟡 OD AG à passer |
| 491000 | Pas de provision créance Map Tech | 🟡 À arbitrer selon recouvrement |

## 4. Comptes "Suspense" (471000) et transit (580001)

> Ces comptes sont des comptes techniques. Idéalement vide en fin d'exercice.

| Compte | ID | Solde 21/05/2026 | Note |
|---|---:|---:|---|
| **471000** Suspense accounts | 1235 | **BNK1 2025 : 1 ligne 6 € · BNK2 2025 : 3 lignes 14,74 €** | Résiduel mineur — voir [[00-Etat-de-la-situation]] |
| 580001 Liquidity Transfer | 1601 | n/a | Compte de virement interne 512001↔512002 — à utiliser pour la ligne BNK1/2025/00487 (CARTE FACTURETTES CB déc), actuellement bloquée en 471000 |

## 5. Schéma type pour les écritures TVA autoliquidation UE

> Schéma utilisé pour Adobe, Patreon, Microsoft 365, Mindeo (Whop), Render, OpenAI, Notion, Canva, GitHub, Vercel, etc. — voir doc Référentiel partenaires pour la liste exhaustive.

Pour une facture HT de X € en provenance UE (ex. Adobe Ireland 91 €) :

```
FACTU :  Dr 626000 (ou 615600) X € HT
         Dr 445662 X × 20 %   (TVA déductible intra-com)
         Cr 401100 (Adobe)    X € HT (TTC sans TVA française)
         Cr 445710 X × 20 %   (TVA collectée intra-com)
```

Net TVA = 0, mais la déclaration CA3 doit refléter les deux côtés (ligne 02b et 17/19).

L'OD de TVA autoliq mensuelle a été passée le 10/05/2026 pour Adobe (FACTO/2025/12/0006, montant 18,19 € — exemple ponctuel). À industrialiser pour les autres fournisseurs UE — actuellement la TVA autoliq est saisie au niveau de chaque BILL plutôt que par OD mensuelle de synthèse, à arbitrer si vous préférez l'une ou l'autre méthode.

## 6. Schéma type pour les écritures BPCE Factor

> Détail complet : [[EC-5-BPCE-Factor]]

Pour chaque cession de créance Sohoft/GA SAS/ONE PINK :

```
FACTO (à la cession) :
   Dr 4671 (90 % - commissions)     ← compte courant Factor
   Dr 4676 (10 %)                   ← fonds de garantie retenu
   Dr 6225 (commission affacturage HT)
   Dr 445660 (TVA sur commission)
   Cr 411100 (créance client cédée)
```

```
Décaissement BNK1 (J+0 ou J+1) :
   Dr 512001 (BNK1)
   Cr 4671 (90 % - commissions)
```

```
Libération fonds garantie (M+1, calculé prorata) :
   Dr 4671
   Cr 4676
```

```
Commission financement (mensuelle, intérêts différé) :
   Dr 661600
   Dr 445660
   Cr 4671
```

## 7. Plan PCG vs plan Odoo — points de divergence

- Le compte **615510** SAGE (entretien matériel) est mappé sur **615500** Odoo (granularité Odoo plus large). Pas de re-création.
- Le compte **445872** SAGE (TVA collectée en attente) est mappé sur **445740** Odoo (équivalent fonctionnel). Pas de re-création.
- Le compte **627000** existe en double dans Odoo (id 1381 original + id 3136 copie) — utiliser id 3136 par convention. Nettoyage à prévoir.
- Le compte **451000** Odoo est typé `liability_current` (courant) malgré le solde débiteur 171 953 € (créance GDG sur Guinet Group). Odoo gère les deux sens, pas de remap nécessaire.

## 8. Export FEC

L'export FEC 2025 peut être généré directement depuis Odoo (Accounting → Reporting → French Statements). À demander si nécessaire pour intégration SAGE.

## Liens

- Mapping initial 2024 : [[Exercice 2024/06-Plan-Comptable-GDG-Mapping]]
- À-nouveau 2024 : [[Exercice 2024/07-OD-A-Nouveau-31122024-GDG]]
- Référentiel partenaires : [[Referentiel-Partenaires-Comptes-GDG]]
- Dossiers à arbitrer : [[EC-3-Dossiers-A-Arbitrer]]
- Dossier BPCE Factor : [[EC-5-BPCE-Factor]]
