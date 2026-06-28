---
tags: ["comptabilité", "odoo", "guinet-group", "exercice-2024-2025", "cloture"]
created: 2026-06-26
société: Guinet Group (company_id=1)
instance: guinet
exercice: 2024-04-01 → 2025-03-31
---

# Guinet Group — Exercice 01/04/2024 → 31/03/2025 — Situation de départ

> État des lieux au **26/06/2026** avant de terminer la compta de l'exercice. Société **Guinet Group** (SAS, SIREN 983 391 079, holding), instance Odoo `guinet`, `company_id=1`.
> Fiche société : [[Brief-Compta-GuinetGroup]].

> [!important] 📊 **Lettrage + ventilation bancaire (au 27/06/2026)**
> • **En lignes : 783 / 1 022 = 76,6 %**
> • **En montant : 374 742 € / 398 376 € = 94,1 %** (reste non lettré : **~23 600 €**, ~239 petites lignes)
> Objectif 100 %. Reste surtout : 8 lignes « aveugles » (besoin du relevé, dont une de 2 090 €), matériel (Darty/Fnac), résidus Bepmale/Odoo, frais BP. Détail : section [[#📊 Indicateur de lettrage bancaire (au 27/06/2026)]] plus bas.

---

## Quel exercice ?

- **1er exercice** (clos par Bepmale) : 08/01/2024 → **31/03/2024** (3 mois) — perte **−2 207 €**, déficit reportable. Liasse C.E.C. Marc BEPMALE. Voir [[Exercice 2024/00-Comptes-annuels-GuinetGroup-2024]].
- **2e exercice (celui à terminer)** : **01/04/2024 → 31/03/2025** (12 mois). À-nouveau ouvert par l'OD `MISC/2024/03/0001` (11 342 € équilibrés).
- Date de clôture à **confirmer avec Bepmale** (31/03/2025 si rythme annuel maintenu — paramétrage Odoo historique au 31/12 à vérifier).

---

## Constat chiffré (au 26/06/2026)

| Indicateur | Valeur | Commentaire |
|---|---|---|
| **CA de l'exercice** | **0 €** | ⚠️ Aucune facture de vente émise sur la période. Anormal pour une holding animatrice (management fees non facturés). |
| **Lignes bancaires non lettrées** | **235** (après purge BNK1) | Mouvements importés mais **non ventilés** sur les comptes PCG (charges/produits/tiers). Cœur du travail restant. |
| **⚠️ Trou d'import bancaire** | **05/12/2024 → 31/03/2025 manquant** | L'import s'arrête au **04/12/2024** (BNK2) — les ~4 derniers mois de l'exercice ne sont PAS importés. **Bloquant pour la clôture.** |
| **Trésorerie (cumul actuel)** | **−8 989 €** | Comptes 101401 (−5 121) et 101406 GUINET GROUP XX8343 (−10 764) négatifs ; 101405 BP +6 896. Reflet du doublon + non-lettrage. |
| **Créances clients** | 2 760 € | = uniquement la facture `INV/2026/00001` GLOBASOFT créée le 26/06/2026 (**hors exercice**, datée 2026). |
| **Dettes fournisseurs** | 153 € | Quelques notes de frais Benoit Guinet (18 + 4 € de 2024, 52 + 15 + 64 € de 2026). |
| **Compte d'attente 471000** | ~82 352 € (interco) | OD provisoire interco GG↔GDG au 31/12/2024 — à reclasser avec Bepmale. |

---

## Problèmes structurels identifiés

1. **Journal bancaire en doublon** — `BNK1 "Bank"` (compte générique Odoo **101401**) double `BNK2 "Compte BP Guinet Group 4463"` (réel, **512110 BP Occitane**) : mêmes montants, mêmes dates. **BNK1 à purger** (même opération que pour GDG en mai 2026). `BNK3` = CB BP 8343 (réel).
2. **Journaux INV / BILL sur comptes par défaut** — INV → 400000 Product Sales, BILL → 600000 Expenses. À reconfigurer vers 706xxx / charges PCG.
3. **Aucun produit comptabilisé** — la holding a forcément des produits sur l'exercice (management fees vers GDG/Globasoft, refacturations). À facturer / régulariser.
4. **291 lignes bancaires sur compte d'attente** — à ventiler (charges 6x, produits 7x, C/C associé **455100**, interco **451100**, TVA).

---

## Travaux pour terminer l'exercice (checklist)

- [ ] **Caler avec Bepmale** : date de clôture (31/03/2025 ?), récupérer la liasse N-1 et les consignes interco.
- [x] **Purger le journal doublon BNK1** (101401) — ✅ 26/06/2026 : 56 lignes doublons (avr→juin 2024, toutes non lettrées, jumelles exactes de BNK2) supprimées, journal **archivé**.
- [x] **Importer le compte principal BNK2 du trou** — ✅ 26/06/2026 : déc 2024 → mars 2025 saisis (120 lignes), chaque relevé équilibré au centime sur les soldes BP. **Solde BP réel au 31/03/2025 = 118,42 €** (relevé n°3). Source : `docs BP Guinet Group 2025`.
- [x] **Importer la CB (BNK3)** — ✅ 26/06/2026 : 12 relevés `CB-8343-AAAA-MM` (id 110-121, cycles déc 2024 → nov 2025), regroupés en statements + **PDF attaché**. Le total de chaque cycle CB **correspond exactement** au « CARTE FACTURETTES CB » du compte principal le mois suivant (contrôle croisé OK). La CB Odoo reprend au 29/11/2024, pile après l'existant (28/11).
- [x] **Import BNK2 complet déc 2024 → nov 2025** — ✅ 26/06/2026 : 12 relevés `BP-Main-AAAA-MM` (id 98-109), regroupés en `account.bank.statement` avec soldes d'ouverture/clôture **équilibrés au centime**, **PDF du relevé attaché** sur chaque (modèle Globasoft). Couvre la fin de l'exercice 2024-2025 ET le début de 2025-2026.
- [x] **Import CB / BNK3** (détail carte 8343) déc 2024 → nov 2025 — ✅ voir ligne ci-dessus (id 110-121).
- [x] **Catégorisation partenaires des lignes bancaires** — ✅ 26/06/2026 : **~855 lignes** (neuves + anciennes sans tiers) affectées par motif sur `payment_ref` ; **26 partenaires créés** (Shopify, AutoDS, Productly, CapCut, Shutterstock, Meta, Rythméo, Up Coop, Malakoff Humanis, Franco-Thai CC, Ricaud, SeDomicilier, Qonto, Vélo Toulouse, Uber, Kandbaz, Maisons du Monde, Fnac, Tisséo, Waalaxy, LinkedIn, InterNations, OpenAI…). Restent **~106 sans tiers** : ~25 « CARTE FACTURETTES CB » (transferts internes carte ↔ compte, normal), 7 lignes déjà lettrées (verrouillées — délettrage requis), ~74 achats one-off 2024 (restos/voyages/magasins). ⚠️ Lot incluant une ligne lettrée → Odoo bloque tout le lot ; isoler les lettrées.
- [ ] **Affecter les comptes PCG** (ventilation 6x charges / 7x produits / 455100 C/C / 451100 interco / 47x TVA) sur les lignes bancaires — partenaires faits, comptes restants.
- [x] **Importer les factures fournisseur depuis les mails** (boîte `guinetb-pro` = guinetb@guinet-group.com) — exercice 2024-2025 — ✅ 27/06/2026 : **69 factures créées+postées+PDF** + 1 OD (détail § Mise à jour 27/06/2026). Reste « **et après** » (avr 2025 → juin 2026) à faire.
- [ ] **Reconfigurer journaux** INV (→ 706xxx) et BILL (→ charges PCG).
- [ ] **Ventiler les 291 lignes bancaires** non lettrées sur comptes PCG (par `update_record` direct, cf. méthode GDG/perso).
- [ ] **Comptabiliser les produits de l'exercice** (management fees, refacturations interco) — résoudre le CA = 0.
- [ ] **Reclasser le compte d'attente 471000** (interco 82 352 € + suspens bancaire) avec le détail Bepmale.
- [ ] **Immobilisations & amortissements** de l'exercice (dotations : frais constitution, iPad, etc.).
- [ ] **TVA** : vérifier collecte/déduction et déclarations de l'exercice.
- [ ] **Rapprochements bancaires** des 3 comptes + lettrage tiers.
- [ ] **OD de clôture** (CCA/PCA, charges à payer, FNP) et **arrêté** au 31/03/2025.

---

## Mise à jour 27/06/2026 — Import factures fournisseur + lettrage

> Source : boîte mail **`guinetb-pro`** (guinetb@guinet-group.com). Méthode : fournisseur par fournisseur, vérification du **« Facturé à »** sur chaque PDF (la boîte est transversale GG / Le Petit Cerf / GDG), création `account.move` in_invoice (journal achat **id 2**, compte fournisseur défaut **211000**), PDF joint, pièce postée, puis lettrage banque.

### Factures comptabilisées (69) — exercice 01/04/2024 → 31/03/2025

| Fournisseur | Nb | Compte charge | TVA | Note |
|---|---|---|---|---|
| **Odoo S.A.** | 15 | 6135 (id 808) | autoliquidation intracom (sans TVA FR) | belge ; « already paid » par carte |
| **Google Workspace** (Google Cloud France SARL) | 12 | 6135 (808) | 20 % déductible (tax id 7) | facturier **français** → TVA FR ; partner id 17 |
| **UpOne / Hexeko** (titres-resto) | 19 | 648000 (806) | TVA **belge** (non récup.) → TTC sans taxe | partner id 15 |
| **People & Baby** (crèche) | 6 | 648000 (806) | 20 % | dont 1 acompte exonéré (3 000) + 1 avoir (−1 500) ; partner id 173 |
| **CEC Marc Bepmale** (honoraires) | 2 | 622601 (830) | 20 % | partner id 32 |
| **Prevaly** (médecine travail) | 2 | 647000 (815) | 20 % | partner id 524 |
| **Productly** (SaaS UK) | 3 | 6135 (808) | — | facturé au nom perso B. Guinet, rattaché GG ; partner id 503 |
| **Franco-Thai CC (FTCC)** | 10 | 604 (807) | TVA **thaïe** (non récup.) | partner id 88 — voir § FTCC |
| **Banque Populaire Occitane** (factures pro = frais bancaires) | 12 | 620000 (id 35) | **exonéré** (frais bancaires non soumis TVA) | partner id 22 ; PDF locaux `docs BP Guinet Group 2024/2025` ; total 1 620,48 € |
| **SFR** (mobile) | 23 | 626000 (id 3192, créé) | 20 % + part Cafeyn 2,1 % non isolée | partner id 23 ; PDF locaux `Guinet Group SFR` ; total 1 470,89 € ; **couvre 2024 ET 2025-2026** (move 7213-7235) |

→ **104 factures fournisseur** au total + **OD SB042** (MISC, 27/03/2025 : 604 ↔ caution). Comptes créés au passage : **275000** (caution, id 3191), **626000** (télécom, id 3192).

> ℹ️ **SFR** : chaque facture = ligne télécom (HT + TVA 20 %) + ligne « facilité de paiement » du téléphone (sans TVA) = net prélevé. Option presse **Cafeyn à TVA 2,1 %** (~0,16 €/mois, ~3,2 € total) passée en charge **sans TVA isolée** (taux 2,1 % absent du plan) — reventilable si on crée une taxe achat 2,1 %.

> ⚠️ **Frais bancaires — éviter le double compte** : la charge des frais BP est désormais portée par ces 12 factures pro (620000). Les **lignes bancaires individuelles** correspondantes (COMMISSION FACTURETTE CB, FRAIS COM INTERVENTION, ABON CYBERPLUS, COTIS PLATIN/SECURIPRO/RYTHMEO, FRAIS VIRT INTERNATIONAL…) doivent être **lettrées contre ces factures**, et **non** re-ventilées en charge 620000 (sinon double comptabilisation).

### Cas FTCC (portage salarial collaboratrice Thaïlande, devise THB)
- Comptabilisé **au montant EUR réellement débité en banque** (méthode devise étrangère). 10 factures = **19 547,45 €**.
- **Dépôt de garantie** (115 500 THB dans SB098) isolé en **caution actif 275000 (id 3191, créé le 27/06/2026)** = 2 963,50 €. SB098 saisie en 2 lignes (caution + charge service).
- **SB042/02/2025 (mars)** : pas de débit (soldée par le dépôt) → **OD** débit 604 1 776 € / crédit 275000 1 776 €. **Caution résiduelle ≈ 1 187,50 €** à clarifier à la clôture (remboursement ou imputation).
- **Virement Wise 5 471,19 € (28/05/2024, stmt 45)** : non identifié → **laissé en suspens** (à élucider).

### Exclusions (entités ≠ Guinet Group — NE PAS comptabiliser ici)
- **GDG / ex-Globasoft** (SIREN 985 298 900) : **Etincelle Coworking**, **Regus**, **Super Compteur** (×2 dont la grosse 2 073,60 €).
- **Le Petit Cerf** (SIREN 929 808 921) : **Dougs** (130,80 €/mois), **Gandi**, **PGPS**, **Malakoff Humanis**, **Shopify Rosari**, **6 factures UpOne** (réf client 5776).
- ⚠️ **Piège adresse** : Etincelle/Regus/Super Compteur portent l'adresse Wilson mais sont au **nom « Globasoft » / SIREN GDG** → distinguer par **nom + SIREN**, jamais par l'adresse seule.

### Lettrage
- **People & Baby** : 3 (PRLV SEPA, n° facture dans le libellé).
- **UpOne** : 11 (réf UPONE dans le libellé bancaire).
- **Prevaly** : 2 (PRLV SEPA).
- **FTCC** : **10/10 lettrées** (8 via virements VIRT NON SEPA + 2 dernières — SB098/SB112 — via `reconcile_lines` après bascule des factures de 211000 → 401100).
- **Frais bancaires BP** : **11 mois sur 12 soldés** ✅ (mécanisme **mixte** : `reconcile_bank_line` pour les frais en suspens 101402 + `reconcile_lines` pour ceux déjà posés sur 401100). **Seul avril reste à −27,22 €** (anomalie cotis Platin 16,88 € jamais débitée + split découvert atypique 39,66/10,34) → régularisation manuelle.
- **Paiements carte CB (journal 14)** : **15 lettrés** (9 Odoo + 6 Google) — après **posting de 8 écritures CB Odoo restées en brouillon**. ⚠️ **Bug `reconcile_bank_line` sur le journal carte** (dry-run OK, échec à l'exécution : « doit comporter exactement une écriture du compte bancaire ») → **contourné** par bascule de la contrepartie suspens 101402 → compte fournisseur de la facture (+ tiers) puis `reconcile_lines`. **Méthode à réutiliser pour le reste des paiements carte.**
- Mécanisme général : `reconcile_bank_line` (substitue le suspens 101402 → compte tiers) **sauf journal carte 14** (bug → bascule compte + `reconcile_lines`).

### ✅ Correctif « trou d'import » — il n'y a PAS de trou (vérifié 27/06/2026)
Le doute initial sur des lignes de frais manquantes a été levé : **les 6 mois avr→nov 2024 du relevé principal (journal 8) sont COMPLETS** — chaque `Extrait de compte` **boucle au centime** (somme des opérations = variation de solde) et chaque opération a sa ligne dans Odoo. **0 ligne à ajouter, 0 doublon.** Les 7 seules vraies omissions (FRAIS AUTO DECOUVERT/INSTANTANE/COMMISSION FACTURETTE/COTIS RYTHMEO) avaient déjà été ajoutées et confirmées sur extrait.
Le **vrai blocage** des 6 mois BP = les lignes de frais existent mais dans des **états mélangés** (certaines en suspens 101402, d'autres déjà posées sur 401100 avec des tiers marchands) → il faut **combiner** `reconcile_bank_line` (suspens) et `reconcile_lines` (écriture-à-écriture sur 401100), opération fine restant à faire. Le cas **avril** a une anomalie structurelle (cotis Platin 16,88 jamais débitée séparément) → régularisation manuelle.

### Ventilation directe (lignes sans facture — méthode `update_record` sur la contrepartie suspens 101402)
Lignes qui n'auront **jamais de justificatif fournisseur** → reclassées directement du suspens vers leur compte (décision Benoit 27/06/2026). **72 lignes ventilées** :
- **Salaires** Kwanchanok (17 lignes, net) → **641110** (id 37). ⚠️ **PPV** (Prime de Partage de la Valeur, 3 000 € du 21/11/2025) **isolée** → compte dédié **641800** (id 3196, créé).
- **URSSAF** (20) → **645000** (id 820).
- **Klesia retraite** (23) → **645000** (id 820).
- **CARTE FACTURETTES CB** (21, transfert interne carte) → **101406** (id 56, compte du journal CB BP 8343) — **méthode Le Petit Cerf** : la ligne s'y neutralise avec les opérations CB du journal 14 (équivalent du « CB BP Différé » de Petit Cerf).
- **Interco — FAIT** : avances **Le Petit Cerf → 451000** (id 3193, 22 lignes), **Benoit Guinet → 455000** (id 3194, 3 lignes), **dépôt de capital Le Petit Cerf 500 € → 261000 titres** (id 3195, GG associé). ⚠️ **GDG (≈ 175 235 €) traité à part** → [[Remontees-GDG-Dividendes-vs-ManagementFees]].
- **Tout le reste** (SaaS, fournisseurs, honoraires, déplacements, restauration, magasins, prévoyance, agios…) : **conservé pour lettrage/justificatif** (Benoit : « on peut avoir des justificatifs »).

> **Comptes créés (27/06/2026)** : 275000 caution (3191), 626000 télécom (3192), 451000 C/C groupe (3193), 455000 C/C associés (3194), 261000 titres de participation (3195), 641800 PPV (3196).

### 📊 Indicateur de lettrage bancaire (au 27/06/2026)
- **Total lignes bancaires (3 journaux, company 1) : 1 022** (1 015 + 7 lignes de frais ajoutées)
- **En lignes : 783 / 1 022 = 76,6 %** (16,1 → 25,0 → 32,4 → 37,0 → 39,5 → 60,7 → 67,8 → **76,6 %**)
- **En montant : ~374 742 € / 398 376,17 € = 94,1 %** — reste non lettré **~23 600 €** (~239 lignes)
- **Dossiers H: (Digidom, Google) + zip « Nouvelles factures »** traités (27/06) : **Digidom** 34,80 → 613200 GG, le **46,80 parallèle 08/24-09/25 → 451100 GDG** (à confirmer) ; **Google** résidus (2e abo + après-exercice) → 6135 ; **Investir + InterNations → 628100** (cotisations/abonnements, créé) ; **Storefront → 613200** ; croisière → 625700. **Vimeo** = facture sans flux GG.
- **Inter-co « payé pour le compte de »** : **Dougs → 451000** (Le Petit Cerf) ; **API NewGen** (restaurant) **→ 451100** (GDG) ; **Ricaud** (avocat) → 451200 (Globasoft ESN). **Google Play → 6135 GG**. **Etincelle** : wash 1000/−1000 → 580, location 336 → 613200 (on n'a que la facture F202406-0153).
- **Partenaires attribués** aux lignes « sans tiers » : **33/42** (20 partenaires créés). Restent **8 lignes aveugles** (libellé vide, −28 à −2 090 €, besoin du relevé) + solde d'ouverture synchro (796, +744,54) à neutraliser.
- **GDG → 451100** (27/06) : 72 lignes (remontées + avances, ~148 k€) en C/C Guinet Digital Group ; Qonto 500 € → 261 (capital Globasoft ESN). ⚠️ C'est de l'**interim** : à la clôture, sortir du C/C la part **management fees (~15 k)** + **dividende (≤ 33 k)** — voir [[Remontees-GDG-Dividendes-vs-ManagementFees]].
- Objectif : 100 %. Gisements restants : **remontées GDG (~76 lignes, +148 k€)** à loger en C/C 451 puis arbitrer MF/dividendes ; **SaaS/fournisseurs avec facture à récupérer** (Apple, AutoDS, Meta, Shopify, Digidom, CHUBB, Up Coop, Natixis…) ; **matériel/équipement** (Darty, Fnac, Maisons du Monde…) ; résidus (avril BP −27,22, Odoo sept/oct, Google partiels).

### Récap par thématique — lignes lettrées / ventilées (session 27/06/2026)
| Thématique | Nb lignes | Méthode |
|---|---|---|
| Frais bancaires BP (11 mois) | ~80 | lettrage mixte vs 12 factures pro |
| Interco (451 Petit Cerf 22 / 455 Benoit 3 / 261 capital 1) | 26 | ventilation directe |
| Klesia retraite | 23 | ventilation → 645000 |
| CARTE FACTURETTES CB | 21 | ventilation → 101406 |
| URSSAF | 20 | ventilation → 645000 |
| Salaires Kwanchanok (+ PPV) | 18 | ventilation → 641110 / 641800 |
| Paiements carte (Odoo 9 + Google 6) | 15 | lettrage vs factures |
| UpOne (titres-resto) | 11 | lettrage vs factures |
| FTCC | 10 | lettrage vs factures |
| People & Baby | 3 | lettrage vs factures |
| Prevaly | 2 | lettrage vs factures |

> ℹ️ Nuance : « lettrer » au sens strict (ligne banque ↔ facture) ne concerne que les lignes ayant une facture en face. Beaucoup des 1 022 lignes sont des dépenses directes (salaires, charges sociales, transferts, achats one-off) qui se soldent par **ventilation en compte** (pas par lettrage). Le 25,0 % mesure les lignes déjà réconciliées OU ventilées (suspens 101402 vidé).

### Reste à lettrer / à finir
- **Paiements carte (CB 8343)** : Odoo (14), Google (12), Productly (3), 8 UpOne début 2024 → **non lettrables 1:1** car noyés dans les **totaux de cycle « CARTE FACTURETTES CB »**. À traiter au niveau du relevé CB groupé.
- **Bepmale** ×2 (82,80 €) : pas de ligne bancaire exacte (carte ?).
- **People & Baby** : acompte 64336 / avoir 65578 / 66844 (virements groupés crèche « Grand Rond » / « de région ») — matching à reprendre.
- **FTCC 1269 (SB098) & 1372 (SB112)** : déjà réconciliés manuellement sur **401100** lors de l'import → annuler la réconciliation (button_undo_reconciliation) puis relettrer vers factures **7183 / 7184**.
- **« Et après »** : factures fournisseur avr 2025 → juin 2026 pas encore importées.

---

## Mise à jour (suite) 27/06/2026 — factures manquantes, Wise/Malakoff, dossiers Drive, ventilation justificatifs

### Factures GG manquantes retrouvées (dossier `H:\Mon Drive\Factures Fournisseurs 2024`)
**13 factures fournisseur de l'exercice créées+postées+PDF** (≈ 3 168 € TTC) : CTA Events (1 052,90), Air France (854,07), Centrale Voyages (348), Allocab ×2 (250,34), Bepmale F042416722 (159,60), Etincelle F202406-0153 (168), Digidom ×2 (69,60), Gandi (38,94), Dougs 596058 (96), Uber EAAHBDCF (34,88, payé GG). Comptes : voyages→625100, honoraires→622601, domiciliation/loc→613200, domaine→651.
**2 OD « C/C Benoit »** (payés perso, pas de ligne banque) : Uber GCJBEGHA (53,80) + Airbnb Paris (2 090,40) → débit 625600 / crédit 455 Benoit. **5 Airbnb N-1 exclus.**
> **N-1 laissés de côté** (hors exercice, pour dossier 2023-2024) : C&C France 1 716, Bepmale F022416622 1 008, UpOne-6082, Google 0005459276, Digidom ×2 (333264/333267), Gandi 2024020901498, AB Corporate 3 000 (2023).

### Dossiers Drive — quelle entité ?
- `D:\GoogleDrive\Factures 2024` = **dépôt GDG** (~90 % « GLOBASOFT »/SIREN 985 298 900) → à booker dans l'Odoo **GDG**, pas GG.
- `H:\Mon Drive\Factures Fournisseurs 2024` = **dépôt GG** (factures + tickets one-off).
- ⚠️ **Digidom et Gandi ont des factures GG ET GDG** → trancher par **SIREN**, pas par fournisseur.
- `Scan nouveau\` (37 tickets restos/stations 2024-2025) = **justificatifs** des lignes banque one-off (ventilées ci-dessous).

### Wise & Malakoff
- **Wise** (−5 471,19 le 28/05 ↔ +5 471,19 le 05/06) = aller-retour → ventilé en **580000 Virements internes** (s'annule à 0, pas de charge).
- **Malakoff Humanis Prévoyance** (7 lignes) → compte **437020 Prévoyance** (créé, reproduit du 4370200 Globasoft).

### Ventilation des justificatifs (restos / déplacements / carburant / DAB)
Lignes one-off justifiées ventilées directement (méthode `update_record` sur la contrepartie suspens 101402) :
- **Restauration → 625700 Réceptions** (créé) : restaurants, cafés, sushi/ramen, boulangeries, supermarchés alim.
- **Carburant → 606600 Carburants** (créé) : stations (Dyneff, Avia, Total…).
- **Déplacements → 625100** : péages, parkings, Tisséo, Vélo, Uber, autoroutes.
- **Retraits DAB → 455 C/C Benoit**.
- **Laissés** : matériel/équipement (Darty, Fnac, Maisons du Monde, Boulanger) + ambigus → arbitrage.

### UpOne 2025-26, Ricaud (inter-co Globasoft), salaire & Petit Cerf
- **UpOne / Up Coop (= même fournisseur)** : les 22 virements `UPONE-xxxxx` de 2025-2026 (post-exercice) ont été **récupérés dans Gmail, comptabilisés et lettrés** (19 factures, 6 712 €, partner Hexeko 15, compte 648000). **2 anomalies** : `UPONE-72740` (introuvable, probable Le Petit Cerf) ; `UPONE-62370` (le PDF trouvé = facture **Le Petit Cerf** 96 € ≠ virement 401,50 € → communication bancaire douteuse) → à investiguer.
- **Justine Ricaud (avocat, 3 lignes, 2 600,10 €)** : ⚠️ ce sont des **avocats payés par GG POUR LE COMPTE DE Globasoft ESN** → **pas une charge GG**. Ventilés en **451200 « Compte courant - Globasoft ESN »** (créance de GG sur Globasoft, à recharger). Miroir : Globasoft porte la charge en 622602. **Schéma à repérer sur d'autres lignes** (dépenses GG pour compte de Globasoft → 451200).
- **Salaire Kwanchanok oublié** (1 042,34, libellé tronqué) → 641110. **Le Petit Cerf** 2 lignes restantes (200+300) → 451000.

### SaaS — entité & ventilation (⚠️ la plupart ne sont PAS des charges GG)
- 🔎 **Les factures SaaS ne sont pas dans le Gmail `guinetb-pro`** — elles sont dans le **coffre TotalCloud** (consigne Bepmale : éviter les drives US). Donc booking « depuis Gmail » impossible pour ces postes.
- **Shopify (30) + AutoDS (34) + Meta/Facebook (38) + CapCut (12) + Shutterstock (12)** = activité **e-commerce/pub (boutiques Guashaluxe, Biblelish, demainthailande… portées par Le Petit Cerf)** → **créance inter-co → 451000 (C/C Le Petit Cerf)**. (146 lignes.) ⚠️ Exclure les « COMMISSION FACTURETTE CB » de ces recherches (= frais BP).
- **Apple (68)** = usage pro iPad/iCloud Benoit → **charge GG 6135**.
- **CHUBB (20)** = assurance privée (≠ prévoyance organisme) → **616101 Assurance pro**. **Natixis épargne salariale (2)** → **647000**.
- Restent à traiter (vrais SaaS GG potentiels, factures dans TotalCloud) : Odoo/Google **résidus**, Productly, OpenAI, LinkedIn, Waalaxy, Investir, Qonto, SeDomicilier, Rythméo, SFR résidus, Digidom/Dougs/Bepmale résidus, Etincelle (tri GG/GDG), matériel (Darty/Fnac/MdM).

> **Comptes créés (suite)** : 437020 Prévoyance (3197), 625700 Réceptions (3199), 606600 Carburants (3200), **451200 C/C Globasoft ESN (3203)**. (+ 580000 Virements internes id 816, déjà existant ; 451100 = C/C **GDG** id 3179, déjà existant.) Compte 622602 « Avocate » créé par erreur puis **supprimé** (Ricaud = inter-co, pas charge GG).

---

## Points à caler avec Bepmale / l'expert

- Date de clôture exacte du 2e exercice (31/03/2025 vs 31/12/2024).
- Détail des flux interco GG ↔ GDG (pour solder le 471000 — 82 352 €). **Remontées GDG ≈ 175 235 € (dont 105 000 € sur l'exercice)** à répartir dividendes / management fees → analyse dédiée : [[Remontees-GDG-Dividendes-vs-ManagementFees]].
- Politique de facturation des management fees (montant, périodicité) — base de la facture Globasoft 2026 déjà initiée (2 000 € présidence + 300 € TMA, cf. instance `guinet` facture 6501).
- Traitement des produits exceptionnels (3 500 € observés sur l'exercice N-1).

---

## Références

- Fiche société : [[Brief-Compta-GuinetGroup]]
- Liasse N-1 (Bepmale 31/03/2024) : [[Exercice 2024/00-Comptes-annuels-GuinetGroup-2024]]
- Reconstruction plan comptable : [[Exercice 2024/02-Reconstruction-GuinetGroup-Phases2-3-5]]
- Méthode transverse (règles, 451 vs 455) : [[Brief-Compta-Transverse]]
