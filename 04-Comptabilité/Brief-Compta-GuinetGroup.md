---
tags: ["comptabilité", "odoo", "guinet-group", "brief"]
created: 2026-05-08
---

---
tags: ["comptabilité", "odoo", "guinet-group", "brief"]
created: 2026-05-08
updated: 2026-05-08
---

# Fiche Comptable — Guinet Group (company_id=1)

> Instance Odoo : `guinet` · Holding du groupe.

---

## Identité

| Élément | Valeur |
|---|---|
| Forme juridique | SAS |
| SIREN | **983 391 079** |
| Capital social | 5 000 € (5 000 parts × 1 €) |
| Associé unique | Benoit Guinet (100 %) |
| Adresse siège | 6 Place Pdt Wilson, 31000 Toulouse |
| Activité IS | Conseil pour les affaires et autres conseils de gestion |
| Régime | Régime simplifié d'imposition |
| Effectif | 1 salarié |
| Filiale | **Guinet Digital Group** (ex-Globasoft, SIREN 985 298 900) — détention 100 % — 1 000 € de titres |

> Le Petit Cerf n'apparaît PAS dans la liasse 2024 → soit acquis/créé après mars 2024, soit pas une filiale de la holding. À clarifier.

### Premier exercice (Bepmale)

- Période : **01/01/2024 → 31/03/2024** (3 mois)
- Total bilan : 9 064 €
- CA : 2 267 €
- Résultat net : **−2 207 €** (perte) → déficit reportable
- Capitaux propres au 31/03/2024 : 2 793 € (capital 5 000 − perte 2 207)

> ⚠️ Date de clôture fiscale dans Odoo paramétrée au 31/12 (`res.company.fiscalyear_last_month=12`) alors que Bepmale a clôturé au 31/03/2024. Soit Bepmale fait un exercice court 3 mois puis bascule à 12 mois civils, soit l'exercice est réellement 04→03. À clarifier.

---

## Plan comptable PCG aligné Bepmale (mis en place le 08/05/2026)

22 opérations effectuées en Phase 2 (7 retypages + 15 créations) + 1 création Phase 5 (compte 120000 résultat). Voir [[Exercice 2024/02-Reconstruction-GuinetGroup-Phases2-3-5]].

### Capital & résultat
| Code | ID Odoo | Libellé | Type |
|---|---|---|---|
| 101000 | 1 | Capital social | equity |
| 120000 | 3168 | Résultat de l'exercice | equity |

### Immobilisations & amortissements
| Code | ID Odoo | Libellé | Type |
|---|---|---|---|
| 201100 | 3153 | Frais de constitution | asset_fixed |
| 218300 | 841 | Matériel bureau & informatique | asset_fixed |
| 261100 | 3154 | Titres de participation Globasoft / GDG | asset_fixed |
| 280110 | 3155 | Amort. frais de constitution | asset_fixed |
| 281830 | 3156 | Amort. matériel bureau & informatique | asset_fixed |

### Tiers fournisseurs
| Code | ID Odoo | Libellé | Type | Reconcile |
|---|---|---|---|---|
| 401000 | 3157 | Fournisseurs divers | liability_payable | oui |
| 401100 | 825 | Fournisseurs biens et services | liability_payable | oui |
| 408100 | 3158 | Fournisseurs - Factures non parvenues | liability_payable | oui |

### Tiers clients
| Code | ID Odoo | Libellé | Type | Reconcile |
|---|---|---|---|---|
| 411100 | 3149 | Clients - Ventes de biens et services | asset_receivable | oui |
| 418100 | 3159 | Clients - Factures à établir | asset_receivable | oui |

### Personnel & social
| Code | ID Odoo | Libellé | Type |
|---|---|---|---|
| 421000 | 827 | Personnel - Rémunérations dues | liability_current |
| 428200 | 3160 | Dettes provisionnées congés payés | liability_current |
| 431000 | 826 | Sécurité sociale | liability_current |
| 437000 | 828 | Autres organismes sociaux | liability_current |
| 437200 | 3161 | ARRCO | liability_current |
| 438200 | 3162 | Charges sociales sur congés payés | liability_current |
| 438600 | 3163 | Autres charges à payer | liability_current |

### Compte courant associé
| Code | ID Odoo | Libellé | Type | Reconcile |
|---|---|---|---|---|
| 455100 | 3164 | Comptes courants associés - Benoit Guinet | liability_current | oui |

### TVA
| Code | ID Odoo | Libellé | Type |
|---|---|---|---|
| 445660 | 843 | TVA déductible | asset_current |
| 445710 | 21 | TVA collectée | liability_current |

### Charges/produits constatés
| Code | ID Odoo | Libellé | Type |
|---|---|---|---|
| 486000 | 3165 | Charges constatées d'avance | asset_current |
| 487000 | 3166 | Produits constatés d'avance | liability_current |

### Produits exceptionnels
| Code | ID Odoo | Libellé | Type |
|---|---|---|---|
| 778800 | 3167 | Produits exceptionnels divers | income_other |

---

## Journaux

| ID | Code | Nom | Type | Compte défaut | Note |
|---|---|---|---|---|---|
| 1 | INV | Customer Invoices | sale | 400000 Product Sales | ⚠️ compte par défaut Odoo, à reconfigurer |
| 2 | BILL | Vendor Bills | purchase | 600000 Expenses | ⚠️ compte par défaut Odoo, à reconfigurer |
| 3 | MISC | Miscellaneous Operations | general | — | utilisé pour OD à-nouveau |
| 6 | BNK1 | Bank | bank | 101401 Bank | ⚠️ à reconfigurer vers 512xxx |
| 7 | CSH1 | Cash | cash | 101501 Cash | |
| 8 | BNK2 | Compte BP Guinet Group 4463 | bank | 512110 BP Occitane | ✅ |
| 14 | BNK3 | CB BP 8343 GUINET GROUP | bank | 101406 GUINET GROUP XX8343 | |
| 59 | MISC1 | Opérations de transferts | general | — | |

---

## Trésorerie & comptes par défaut Odoo

| ID | Code | Libellé | Statut |
|---|---|---|---|
| 43 | 101401 | Bank | compte par défaut Odoo, à terme à supprimer |
| 822 | 512110 | BP Occitane | compte principal |
| 56 | 101406 | GUINET GROUP XX8343 | CB BP 8343 |
| 833 | 528000 | VIREMENT DE FONDS | |
| 816 | 580000 | Virements internes | |

---

## Charges (codes en place)

| ID | Code | Libellé |
|---|---|---|
| 807 | 604 | Achat d'études et prestations de services |
| 818 | 6064 | Fournitures administratives |
| 819 | 613200 | Locations immobilières |
| 808 | 6135 | Services informatiques |
| 830 | 622601 | Honoraires |
| 817 | 624 | Transports |
| 835 | 625100 | Frais déplacements divers |
| 838 | 625600 | Missions |
| 836 | 616101 | Assurance pro ST |
| 837 | 616102 | Assurance pro STE |

---

## Exercice 2024 — Reconstruction Odoo

> Voir [[Exercice 2024/00-Comptes-annuels-GuinetGroup-2024]] et [[Exercice 2024/02-Reconstruction-GuinetGroup-Phases2-3-5]].

| Phase | Statut au 08/05/2026 |
|---|---|
| 1. Diagnostic Odoo vs Bepmale | ✅ |
| 2. Plan comptable (7 retypages + 16 créations) | ✅ |
| 3. Suppression 44 moves ≤ 31/03/2024 | ✅ |
| 4. Reconfig journaux INV / BILL / BNK1 | ⏳ à faire |
| 5. OD d'à-nouveau MISC/2024/03/0001 (11 342 € équilibrés) | ✅ |

### À faire pour la clôture 31/12/2024 GG

- ~~Récupérer ou reconstruire le bilan Bepmale Guinet Group au 31/12/2024~~ → ✅ pour la partie interco (09/05/2026)
- ~~Créer un compte miroir **451100 C/C Guinet Digital Group** dans le plan GG~~ → ✅ id 3179, type `liability_current`, reconcile activé
- ~~Saisir une OD complémentaire d'à-nouveau au 31/12/2024~~ → ✅ MISC/2024/12/INTERCO-GDG (id 5537)

### Statut interco GG ↔ GDG au 31/12/2024 (09/05/2026)

| Société | Compte | Sens | Montant |
|---|---|---|---:|
| GDG (id=4) | 451000 (id 1215) | Débit (créance) | 89 352,00 € |
| GG (id=1) | 451100 (id 3179) | Crédit (dette) | 89 352,00 € |

**Symétrie parfaite** ✅

Décomposition côté GG :
- 7 000 € : ligne 610 historique BNK2/2024/00053 du 10/06/2024 (initialement sur 401100, reclassée en 451100)
- 82 352 € : OD MISC/2024/12/INTERCO-GDG du 31/12/2024 (contrepartie sur 471000 Compte d'attente)

⚠️ **Le compte 471000 (id 3180) porte un débit de 82 352 €** qui devra être réparti entre comptes de charges/produits/résultat exceptionnel selon la nature réelle des flux interco. **À traiter avec Bepmale** quand on aura le détail des mouvements.

---

## Points ouverts (post-Phase 5 GG)

| # | Action | Détail |
|---|---|---|
| 1 | Reconfig journaux | INV → 706xxx · BILL → 6xxxxx PCG · BNK1 → compte bancaire réel |
| 2 | Lettrage fournisseurs 401 post-31/03/2024 | nombre de lignes à recompter après l'à-nouveau |
| 3 | Sohoft Toulouse 411 | 1 080 € éventuellement déjà absorbé dans à-nouveau (à vérifier) |
| 4 | ✅ | Globasoft branche -7 000 € | Résolu 09/05/2026 — ligne 610 (BNK2/2024/00053) reclassée du 401100 vers 451100 (Compte courant GDG). Voir [[#Statut interco GG ↔ GDG au 31/12/2024 (09/05/2026)]] |

---

## Référence rapide

- Tous les retypages et créations sont consignés dans [[Exercice 2024/02-Reconstruction-GuinetGroup-Phases2-3-5]]
- Synthèse de la liasse Bepmale : [[Exercice 2024/00-Comptes-annuels-GuinetGroup-2024]]
- Diagnostic d'écart initial : [[Exercice 2024/01-Diagnostic-Odoo-vs-Bepmale]]




---

## Détails liasse Bepmale 2024 GG (vérifiés 09/05/2026)

> Source : PDF Plaq0324_976.pdf, mission C.E.C. Marc BEPMALE & Associés, 24 pages, daté 08/10/2024

### Identité fiscale
- SIREN : **983 391 079** (cohérent brief)
- Capital social : **5 000 €** (5 000 parts × 1 €) — note : le brief mentionnait 5 000 €, c'est confirmé. La date d'effet pourrait avoir évolué depuis (capital actuel à vérifier).
- Forme juridique : SAS, IS, régime simplifié
- Activité : Conseil pour les affaires et autres conseils de gestion
- Premier exercice : **01/01/2024 → 31/03/2024 (3 mois)** ⚠️
- Associé unique : Benoit GUINET (100 %), né 12/05/1989 à Paris, dom. 49 Impasse de la Baraquette Apt C12, 31400 TOULOUSE
- Cabinet : C.E.C. Marc BEPMALE & Associés (SELARL 250 000 €, 72 rue Riquet 31000 Toulouse, **SIREN 487 737 041**)
- Logiciel comptable : **SAGE GENERATIONS EXPERTS**

### Chiffres-clés liasse 31/03/2024
| Item | Valeur exacte |
|---|---:|
| Total bilan | **9 064,30 €** |
| CA (3 mois) | **2 266,67 €** |
| Résultat net | **−2 207,22 €** (perte) |
| Effectif moyen | 1,00 |
| Déficit reportable au 31/03/2024 | **2 207 €** ✅ |

### Filiale
- **GLOBASOFT** (SIREN 985 298 900) : 100 % détenu, valeur brute 1 000 € (page 14 liasse — tableau des filiales et participations)

### Structure du résultat 01/01→31/03/2024 (page 6 Bepmale)
- Production vendue services (706000) : **2 266,67 €**
- Charges externes : 5 673 € (dont honoraires 2 267 + 251 = 2 518, voyages 2 000, réceptions 429, services bancaires 36, **frais d'actes et contentieux 206**)
- Rémunérations : 2 198 € (salaires 1 767, congés payés 177, **avantages salariés 254**)
- Charges sociales : 12 € (URSSAF 9, mutuelles 3) — extrêmement faible
- DOT amort : 70 € (incorporelles 21, corporelles 49)
- **Produits exceptionnels 3 500 €** (778800) — à investiguer (apport en compte courant ? subvention création ?)
- Pas de produits financiers, pas de charges financières
- Pas d'IS (déficit)

### Détails immo 2024
- Frais de constitution 708 € acquis 08/02/2024, amort linéaire 5 ans (20 %), 21 € amort 3 mois ✅
- iPad avec clavier 1 716 € acquis 29/02/2024, amort linéaire 3 ans (33,33 %), 49 € amort 3 mois ✅
- Parts Globasoft : 1 000 € acquis 12/02/2024 (création de la filiale), pas d'amortissement

### Question d'exercice
⚠️ **Bepmale a clôturé GG au 31/03/2024.** La déclaration IS 2065-SD page 23 confirme : exercice ouvert le **08/01/2024**, clos le **31/03/2024**. 
- L'exercice 2 (01/04/2024 →) est en cours dans Odoo
- **Pas de bilan officiel GG au 31/12/2024** : Bepmale clôturera son prochain exercice à une date à confirmer (probablement 31/03/2025 si rythme annuel maintenu, ou 31/12/2024 si bascule sur année civile)
- **L'OD MISC/2024/12/INTERCO-GDG (id 5537) est donc provisoire** côté GG, en attendant l'arrêté Bepmale
- Le compte 471000 (id 3180) avec 82 352 € en débit reste à reclasser quand Bepmale aura le détail des flux interco

### Détail charges à payer (page 12 liasse Bepmale)
- 408100 Fournisseurs FNP : 412 €
- 428200 Provisions CP : 177 €
- 438200 Charges sociales sur CP : 3 €
- 438600 Autres charges à payer : 21 €
- **Total charges à payer = 612 €** ✅ (cohérent avec OD à-nouveau Odoo)

### Charges/Produits constatés d'avance (page 12)
- 486000 CCA : 1 680 €
- 487000 PCA : 733 €

---

## Mise à jour 26/06/2026 (session import/catégorisation banque)

> Détail du chantier de clôture : [[Exercice 2024-2025 GG/00-Situation-de-depart]].

- **BNK1 (journal 6, 101401) purgé et archivé** : c'était un doublon partiel de BNK2 (56 lignes avr→juin 2024). Ne plus l'utiliser.
- **Import bancaire complet déc 2024 → nov 2025** sur **BNK2** (journal 8, compte réel BP 512110) et **BNK3 / CB 8343** (journal 14) : 24 relevés `account.bank.statement` (`BP-Main-AAAA-MM` id 98-109, `CB-8343-AAAA-MM` id 110-121), soldes équilibrés au centime, **PDF du relevé attaché** sur chaque (modèle Globasoft). Sources : dossiers `docs BP Guinet Group 2024/2025` (racine du repo `scripts-divers-autres`). **Solde BP au 31/03/2025 = 118,42 €**. Chaque cycle CB = le « CARTE FACTURETTES CB » du compte principal (contrôle croisé).
- **Catégorisation partenaire** des lignes bancaires faite (~855 lignes, 26 partenaires créés). Restent ~106 sans tiers : transferts internes « CARTE FACTURETTES CB », 7 lignes déjà lettrées (verrouillées), achats one-off 2024. ⚠️ Modifier le tiers d'une ligne **lettrée** échoue (« écriture validée ») → un lot batch contenant une ligne lettrée est rejeté en entier ; isoler les lettrées (filtrer `is_reconciled`).
- **Compte 706000 « Prestations de services »** : Guinet Group n'en avait pas. Compte créé (id **3189**) mais **bloqué au code 706999** : le code 706000 est verrouillé sur tout l'arbre de branches {company 1 + branches « Globasoft branche » (2) + « Le Petit Cerf Branche » (3)}, et la société fantôme **« Globasoft branche » (company 2) est inaccessible à l'utilisateur API** → impossible de libérer 706000 par RPC. À régler en nettoyant les sociétés fantômes ou via l'UI admin. Utilisé sur la facture client `INV/2026/00001` (mgmt fees 2 000 € présidence + 300 € TMA, move id 6501).
- Compte client de **GLOBASOFT** (partner 500) recâblé sur **411100** (id 3149) / fournisseur **401100** (id 825).
