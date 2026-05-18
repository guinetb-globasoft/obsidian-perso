---
tags: ["comptabilité", "odoo", "guinet-digital-group", "brief", "bpce-factor", "affacturage"]
created: 2026-05-08
---

---
tags: ["comptabilité", "odoo", "guinet-digital-group", "brief", "bpce-factor", "affacturage"]
created: 2026-04-12
updated: 2026-05-08
---

# Fiche Comptable — Guinet Digital Group (company_id=4) · Odoo `guinet`

> ESN du groupe — affacturage BPCE Factor.

---

## Identité

| Élément | Valeur |
|---|---|
| Forme juridique | SARL |
| SIREN | **985 298 900** |
| Capital social | 1 000 € (1 000 parts × 1 €) |
| Détention | **100 %** par Guinet Group SAS (SIREN 983 391 079) |
| Adresse siège | 6 Place du Président Wilson, 31000 Toulouse |
| Activité IS | Conseil en systèmes et logiciels informatiques |
| Régime | Régime simplifié d'imposition + TVA simplifiée |
| Effectif | 1 salarié + 1 apprenti |
| Gérant | Benoit Guinet (régime TNS — art. 62 CGI) |
| Ancien nom | Globasoft (renommage légal en **août 2025**) |

> ℹ️ Bordereaux BPCE Factor (compte `50890DEUR`) et compte bancaire `512002 GLOBASOFT XX7328` portent encore le nom historique **GLOBASOFT** — ce n'est PAS une erreur du factor, c'est le nom légal historique préservé.
>
> ⚠️ Ne pas confondre avec **Globasoft branche (company_id=2)** dans Odoo, qui est un doublon ou ancien paramétrage à clarifier — pas la même entité que GDG.

### Premier exercice (Super Compteur)

- Période : **01/02/2024 → 31/12/2024** (11 mois)
- Total bilan : **155 561 €**
- CA : **123 600 €**
- Résultat net : **+32 646 €** (bénéfice)
- IS dû : 5 891 €
- Bénéfice imposable : 38 958 €
- Capitaux propres au 31/12/2024 : 33 646 € (capital 1 000 + résultat 32 646)

> Voir [[Exercice 2024/03-Comptes-annuels-GDG-2024]] pour le détail du bilan Super Compteur.

---

## Règles spécifiques GDG

- Toujours `company_id=4` sur tous les appels RPC comptables.
- Sur les écritures FACTO : ligne 411100/401100 → `partner_id` du tiers concerné ; lignes charges/TVA → `partner_id` BPCE Factor (`410`).

---

## Journaux

| ID | Code | Nom | Type | Note |
|----|------|-----|------|------|
| 22 | FAC | Customer Invoices | sale | |
| 23 | FACTU | Vendor Bills | purchase | |
| 24 | OD | Miscellaneous Operations | general | |
| 25 | EXCH | Exchange Difference | general | |
| 26 | CABA | Cash Basis Taxes | general | TVA sur encaissements |
| 27 | BNK1 | Bank (compte principal) | bank | 512001 |
| 28 | CSH1 | Cash | cash | |
| 29 | SLR | Salaries | general | |
| 30 | BNK2 | GLOBASOFT XX7328 | bank | 512002 |
| 31 | BNK3 | Compte TVA | bank | 512003 |
| 50 | GR-GG | Groupe - Guinet Group | general | |
| 52 | STJ | Valorisation des stocks | general | ⏸️ archivé 09/05/2026 (vide, ESN sans stock) |
| 58 | MISC1 | Affacturage (déprécié — utiliser FACTO) | general | ❌ **NE PLUS UTILISER** (renommé 09/05/2026) — 13 moves historiques 2025 conservés (extournes vs FACTO, reconciles actifs) |
| 60 | MISC2 | Opérations de transfert | general | |
| 61 | FACTO | BPCE Factor | general | ✅ **Journal actif affacturage** |

---

## Plan comptable Odoo actuel (codes en place)

### Tiers
| ID | Code | Libellé |
|----|------|---------|
| 1134 | 401100 | Fournisseurs |
| 1149 | 411100 | Clients |
| 1152 | 413000 | Customers - Bills receivable (anciennes ODs MISC1) |
| 1160 | 421000 | Personnel — rémunérations |
| 1171 | 431000 | Sécurité sociale |
| 1215 | 451000 | Groupe (interco) |

### TVA
| ID | Code | Libellé |
|----|------|---------|
| 1185 | 445200 | TVA intracommunautaire due |
| 1194 | 445660 | TVA déductible autres B&S |
| 1199 | 445710 | TVA collectée |

### Trésorerie
| ID | Code | Libellé |
|----|------|---------|
| 1597 | 512001 | Bank (compte principal) |
| 1603 | 512002 | GLOBASOFT XX7328 |
| 1604 | 512003 | Compte TVA |

### Affacturage BPCE Factor
| ID | Code | Libellé | Note |
|----|------|---------|------|
| 3150 | 6225 | Commissions d'affacturage | |
| 3151 | 4671 | Compte courant BPCE Factor | ❌ lettrage non activé |
| 3152 | 4676 | Fonds de garantie | ❌ **non utilisé** sur ce contrat |
| 1443 | 661600 | Intérêts financement (escompte) | |

### Partenaires clés
| Partenaire | `partner_id` |
|------------|-------------|
| BPCE Factor | 410 |
| GA SAS (Sébastien Thalamy) | 288 |
| ONE PINK | 290 |
| Sohoft Toulouse | 14 |
| Map Technologies | 279 |

---

## Comptes Super Compteur à mapper / créer dans Odoo

> Pour reconstituer l'à-nouveau 2024, il manque dans Odoo les comptes du PCG SAGE utilisés par Super Compteur. À créer en Phase 2 GDG (équivalent de la Phase 2 Guinet Group déjà faite).

| Compte SAGE | Libellé | Statut Odoo |
|---|---|---|
| 101300 | Capital | à créer (vs 101000 standard) |
| 164100 | Emprunt | à créer |
| 218200 | Matériel de transport | à créer |
| 281820 | Amort. matériel de transport | à créer |
| 411000 | CLIENTS | mapper sur 411100 (ID 1149) |
| 418100 | CLIENTS FACT À ÉTABLIR | à créer |
| 425000 | Avance acompte personnel | à créer |
| 428200 | CONGÉS À PAYER | à créer |
| 437200 | Caisse retraite salarié | à créer (différent de 437000) |
| 438200 | ORG.SOC. CH/CONGES À PAYER | à créer |
| 438600 | URSSAF gérant TNS | à créer |
| 444000 | ETAT IMPOTS S/BÉNÉFICES | à créer |
| 445510 | TVA À DÉCAISSER | à créer |
| 445860 | TVA / factures non parvenues | à créer (≠ 445660 déductible) |
| 445870 | TVA / factures à établir | à créer |
| 445872 | TVA collectée en attente | à créer (≠ 445740 actuel) |
| 455010 | C/C Benoit Guinet | à créer |
| 486000 | Charges constatées d'avance | à créer |
| 512000 | Banque N°4634 | mapper sur 512002 GLOBASOFT XX7328 |
| 512100 | Banque | mapper sur 512001 BNK1 |
| + 30+ comptes charges/produits du compte de résultat | | à créer |

---

## ⚠️ Alertes identifiées par confrontation Super Compteur ↔ Odoo

### 1. Le 451000 Group dans Odoo est figé à 56 500 € depuis sept 2024

Bilan Super Compteur : **451000 Dr 89 352 €** (créance GDG sur GG) au 31/12/2024.
Odoo : 56 500 € depuis septembre 2024.
→ Écart **~33 000 €** : Super Compteur a fait des OD interco fin 2024 jamais reflétées dans Odoo.

### 2. C/C Benoit Guinet 455010 = 43 810 € absent d'Odoo GDG

Le compte 455 n'existe pas dans le plan Odoo GDG. Les apports de Benoit (43 810 € en compte courant) sont éparpillés sur d'autres comptes. Action : créer **455010**.

### 3. Citroën C5 — 30 000 € + emprunt 29 093 € — absent d'Odoo

- Acquisition 29/10/2024 — 218200 Matériel transport 30 000 €
- Amortissement linéaire 5 ans — 281820 Amort. -1 033 €
- Financement emprunt — 164100 Emprunt 29 093 €
→ 3 comptes à créer + à saisir dans l'à-nouveau 2024.

### 4. TVA à décaisser 18 876 € au 31/12/2024

Régime simplifié → **445510 TVA à décaisser**. Grosse dette de TVA à payer en 2025. À vérifier si décaissée.

### 5. URSSAF gérant TNS 18 776 € au 31/12/2024

Dette **438600** importante. Le brief observait "431 URSSAF -39 €" en 2025 — incohérent. À investiguer.

### 6. TVA cash basis (CABA) active

GDG est en TVA sur encaissements. À chaque paiement client, Odoo crée une écriture CABA qui transfère la TVA de **445740 "VAT collected on unsettled"** vers **445710 "VAT collected"** définitif. Le mécanisme fonctionne — testé sur FAC/2024/00001.

---

## Comptabilisation de l'affacturage BPCE Factor

> Source : https://www.compta-facile.com/comptabilisation-de-l-affacturage/
> Sur ce contrat, **4676 fonds de garantie non utilisé** — schéma simplifié à 4 lignes.

### 1. Cession des créances — journal FACTO (id=61)
Date : date de remise du bordereau

| Sens | Compte | Partenaire | Libellé |
|------|--------|-----------|---------|
| Cr | 411100 | client | Créance cédée TTC |
| Dr | 6225 | BPCE Factor (410) | Commission affacturage HT |
| Dr | 445660 | BPCE Factor (410) | TVA / commission affacturage |
| Dr | 4671 | BPCE Factor (410) | Net à recevoir (= Total − com. HT − TVA) |

### 2. Paiement du factor → banque
Règle de rapprochement bancaire id=42 (déclencheur : libellé contient "FACTOR")

| Sens | Compte | Libellé |
|------|--------|---------|
| Cr | 4671 | Compte courant BPCE Factor |
| Dr | 512001 | Banque |

### 3. Commission de financement mensuelle
Date : dernier jour du mois — source : décompte BPCE Factor

| Sens | Compte | Partenaire | Libellé |
|------|--------|-----------|---------|
| Dr | 661600 | BPCE Factor (410) | Commission financement HT |
| Dr | 445660 | BPCE Factor (410) | TVA / commission financement |
| Cr | 4671 | BPCE Factor (410) | Compte courant BPCE Factor |

### 3 bis. Remboursement du fonds de garantie (théorique — non applicable)
| Sens | Compte | Libellé |
|------|--------|---------|
| Cr | 4676 | Fonds de garantie |
| Dr | 512001 | Banque |

> Documenté pour référence générale, non utilisé sur ce contrat.

---

## Historique affacturage BPCE Factor — Juillet 2025 → Mars 2026

### Juillet – Septembre 2025

| id | Type | Bordereau | Date | Contenu | Statut |
|----|------|-----------|------|---------|--------|
| 5458 | Extourne | — | 04/07/2025 | Annulation MISC1/2025/07/0001 — Sohoft | ✅ posted |
| **5459** | OD FACTO | 0004063731 | 04/07/2025 | Sohoft 13 986€ · com. 750 · TVA 150 · net 13 086 | ✅ posted |
| 5462 | Extourne | — | 01/08/2025 | Annulation MISC1/2025/08/0001 — Sohoft | ✅ posted |
| **5463** | OD FACTO | 0004083820 | 01/08/2025 | Sohoft 13 230€ · com. 390,29 · TVA 78,06 · net 12 761,65 | ✅ posted |
| 5466 | Extourne | — | 01/09/2025 | Annulation MISC1/2025/09/0003 — Sohoft | ✅ posted |
| **5467** | OD FACTO | 0004100394 | 01/09/2025 | Sohoft 8 694€ · com. 256,47 · TVA 51,29 · net 8 386,24 | ✅ posted |
| 5469 | Extourne | — | 04/09/2025 | Annulation MISC1/2025/09/0002 — GA SAS | ✅ posted |
| **5470** | OD FACTO | 0004103730 | 04/09/2025 | GA SAS 2 484€ · com. 73,28 · TVA 14,66 · net 2 396,06 | ✅ posted |
| 5472 | Extourne | — | 29/09/2025 | Annulation MISC1/2025/09/0001 — GA SAS | ✅ posted |
| **5473** | OD FACTO | 0004120366 | 29/09/2025 | GA SAS 6 880,20€ · com. 202,97 · TVA 40,59 · net 6 636,64 | ✅ posted |

| FAC(s) | FACTO id | full_reconcile |
|---|---|---|
| FAC/00016 + FAC/00017 | 5459 | 627 |
| FAC/00019 + FAC/00020 | 5463 | 632 |
| FAC/00021 + FAC/00022 | 5467 | 637 |
| FAC/00023 | 5470 | 640 |
| FAC/00024 | 5473 | 645 |

### Octobre 2025

| id | Type | Bordereau | Date | Contenu | Statut |
|----|------|-----------|------|---------|--------|
| 5444–5447 | Extournes | — | Oct 2025 | Annulation MISC1/2025/10/0001 à 0004 | ✅ posted |
| **5448** | OD FACTO | 0004122927 | 02/10/2025 | Sohoft 16 254€ | ✅ posted |
| **5449** | OD FACTO | 0004129637 | 08/10/2025 | GA SAS 5 112€ | ✅ posted |
| **5450** | OD FACTO | 0004130032 | 08/10/2025 | ONE PINK 1 620€ | ✅ posted |
| **5451** | OD FACTO | 0004146709 | 31/10/2025 | Sohoft 15 876€ | ✅ posted |

### Décembre 2025

| id | Type | Bordereau | Date | Contenu | Statut |
|----|------|-----------|------|---------|--------|
| **5452** | OD FACTO | 0004168484 | 01/12/2025 | GA SAS 6 624€ + Sohoft 13 230€ | ✅ posted |
| **5453** | OD FACTO | 0004181963 | 16/12/2025 | GA SAS 7 128€ | ✅ posted |
| **5454** | OD FACTO | 0004188700 | 24/12/2025 | Sohoft 13 230€ | ✅ posted |

### Janvier – Mars 2026

| id | Type | Bordereau | Date | Contenu | Statut |
|----|------|-----------|------|---------|--------|
| **5429** | OD FACTO | 0004199395 | 13/01/2026 | ONE PINK 1 368€ | ✅ posted |
| **5430** | OD FACTO | 0004211031 | 30/01/2026 | ONE PINK 1 512€ + Sohoft 14 553€ | ✅ posted |
| **5437** | Com. fin. | — | 31/01/2026 | Commission financement janv. 139,44€ HT | ✅ posted |
| **5435** | OD FACTO | 0004232662 | 27/02/2026 | Sohoft 13 986€ | ✅ posted |
| **5438** | Com. fin. | — | 28/02/2026 | Commission financement févr. 130,52€ HT | ✅ posted |
| **5427** | OD FACTO | 0004244959 | 13/03/2026 | GA SAS 4 176€ | ✅ posted |
| **5436** | OD FACTO | 0004256434 | 31/03/2026 | Sohoft 15 876€ | ✅ posted |
| **5439** | Com. fin. | — | 31/03/2026 | Commission financement mars 137,17€ HT | ✅ posted |

---

## État du lettrage 411 (au 12/04/2026)

| Facture | Partenaire | Montant | Statut |
|---|---|---|---|
| FAC/2026/00010 | Aerotec & Concept | 16 476 € | Normal — éch. 02/05/2026 |
| FAC/2026/00003 | ONE PINK | 576 € | En retard 72j — à relancer |
| FAC/2025/00007 | Map Technologies | 5 280 € | ⚠️ En retard **404 jours** — recouvrement requis |

---

## Google Drive — Comptabilité Globasoft ESN

```
Comptabilité Groupe/
└── Globasoft ESN/                        ← compte MCP: globasoft
    ├── 2025/
    │   ├── Affacturage BPCE Factor/      ID: 1uVRqJu6a9UbVrMwCMH67lCQZnzB0lX7v
    │   │   ├── Octobre 2025/             ID: 16fk1RNezQvQMi7w6VbzYufABjYjlDPdz  ✅ 4 fichiers
    │   │   ├── Décembre 2025/            ID: 1oPJO3a8Gmjwqe6uIkndFf8TnQZceqaYk  ✅ 3 fichiers
    │   │   ├── Juillet 2025/             ⏳ à créer
    │   │   ├── Août 2025/                ⏳ à créer
    │   │   └── Septembre 2025/           ⏳ à créer
    │   ├── Factures Clients/
    │   ├── Factures Fournisseurs/
    │   ├── Relevés Bancaires/
    │   ├── Notes de Frais/
    │   └── Déclarations Fiscales/
    └── 2026/  (même structure)
```

> ⏳ Raccourci `2025_affacturage` à ajouter (ID `1uVRqJu6a9UbVrMwCMH67lCQZnzB0lX7v`).

### Nommage bordereaux sur Drive
`Bordereau de remise factures ou avoirs [Mois] [Année]_[N].pdf`
Sources locales : `C:/Users/Shadow/Downloads/Factor BPCE/`

### Anciens dossiers (hors hiérarchie)
`Factures Fournisseurs 2024` · `Factures clients 2024` · `Scans` · `Scans faits` · `Documents banque` · `A comptabilisé` / `Dans Odoo`

> Les comptes MCP gdrive et leurs raccourcis communs sont décrits dans [[Brief-Compta-Transverse]].

---

## Exercice 2024 — Reconstruction Odoo (à venir)

Stratégie validée : reconstruction complète identique à Guinet Group. Voir [[Exercice 2024/04-Diagnostic-GDG-Odoo-vs-SuperCompteur]].

| Phase | Statut au 08/05/2026 |
|---|---|
| 1. Diagnostic Odoo vs Super Compteur | ✅ |
| 2. Plan comptable (~30 comptes à créer) | ✅ 09/05/2026 — 10 comptes créés (164100, 281820, 437200, 455010, 616160, 641600, 641610, 647000, 648100, 649100), reste mappé 1:1 sur Odoo standard. Voir [[Exercice 2024/06-Plan-Comptable-GDG-Mapping]] |
| 3. Suppression 416 moves ≤ 31/12/2024 | ✅ 09/05/2026 — 425 moves supprimés au total, 0 restant, 71 PJ préservées (voir [[Exercice 2024/05-Mapping-PJ-Moves-2024-GDG]]) |
| 4. Reconfig journaux | ✅ 09/05/2026 — MISC1 renommé "Affacturage (déprécié)", STJ archivé |
| 5. OD d'à-nouveau au 31/12/2024 (~30+ lignes, total bilan 156 595 €) | ✅ 09/05/2026 — OD `OD/2024/12/A-NOUVEAU` (id 5530, journal OD), 25 lignes, 156 595 € équilibrés, posted. Résultat 32 646,67 € sur 120000. |

### Volumétrie observée
- 416 moves posted ≤ 31/12/2024
- 199 lignes lettrées (88 reconciles uniques)
- 5 reconciles bridges 2024↔2025 identifiés (Sohoft 13 680 € + Gandi 18 € + Dicapo 27 € + frais BPCE 6 € négligeables)
- 83 reconciles 2024-only (à dissoudre automatiquement par passage en draft)

---

## Points ouverts

| # | Statut | Action | Détail |
|---|---|---|---|
| 1 | ⏸️ | Lettrage 4671 | Reporté 09/05/2026 — 50 lignes non-lettrées sur le 4671. À faire ultérieurement avec les bordereaux Factor détaillés sous les yeux pour tracer commissions, virements, fonds de garantie. Lignes prioritaires : id=12178 (13 928,35€) et id=12295 (12 125,86€). |
| 2 | ✅ | Pièces jointes Odoo — 12 ODs FACTO | Vérifié 09/05/2026 — toutes les PJ sont rattachées (ids 5448-5454 + 5459, 5463, 5467, 5470, 5473) |
| 3 | ✅ | Dépôt Drive Juil/Août/Sept 2025 | Vérifié 09/05/2026 — les 6 sous-dossiers existent (Juillet→Décembre 2025) avec bordereaux + relevés de compte présents |
| 4 | ⏳ | Raccourci `2025_affacturage` | À ajouter manuellement dans config MCP gdrive (ID `1uVRqJu6a9UbVrMwCMH67lCQZnzB0lX7v`). Pas une action Odoo. |
| 5 | ✅ | Map Technologies FAC/2025/00007 | **Découvert 09/05/2026 : la facture EST PAYÉE** (BNK1/2025/00293 du 09/04/2025, 5 280 €). Le statut `not_paid` dans Odoo est dû au bug TVA (point #7) qui empêche le lettrage automatique. Pas de recouvrement à faire. |
| 6 | ✅ | Reconstruction Odoo 2024 | Phases 1-5 GDG terminées + bilan miroir GG 09/05/2026 — voir [[Exercice 2024/07-OD-A-Nouveau-31122024-GDG]] et [[Brief-Compta-GuinetGroup#Statut interco GG ↔ GDG au 31/12/2024 (09/05/2026)]] |
| 7 | ⏸️ | Bug TVA Map Technologies (lettrage) | Investigué 09/05/2026 — la facture FAC/2025/00007 a été **payée** par BNK1/2025/00293 le 09/04/2025. Lettrage bloqué par contrôle multi-société d'Odoo : tax_repartition_line 566 corrigé en 258, tax_line_id forcé à 60, tax_ids réécrit, mais erreur "tax_ids: '20% S', '20% S' appartient à une autre société" persiste. **Décision** : laisser le bug ouvert. Map Tech reste `not_paid` dans Odoo mais factuellement payé. À résorber par OD de compensation 411 si besoin de cleaner les rapports. |




---

## Détails liasse SC 2024 GDG (vérifiés 09/05/2026)

> Source : [[Exercice 2024/03-Comptes-annuels-GDG-2024]] (PDF Plaq1224_9215.pdf, mission Cabinet Super Compteur, 18 pages, daté 12/04/2025)

### Identité fiscale
- SIREN/SIRET : **985 298 900 00012** (établissement principal)
- Forme juridique : SARL
- Régime IS : simplifié d'imposition
- Activité : Conseil en systèmes et logiciels informatiques (NAF voisin)
- Premier exercice : **01/02/2024 → 31/12/2024 (11 mois)**
- Cabinet : Super Compteur (SARL au capital 10 000 €, 72 rue Riquet 31000 Toulouse, RCS Toulouse 834 394 660)
- Pas d'exercice précédent (création 02/2024)
- Logiciel comptable : **SAGE GENERATION EXPERTS**
- Capital social : 1 000 € (1 000 parts × 1 €)
- Associé unique : **GUINET GROUP** (SIREN 983 391 079, 100 % détention) ✅

### Chiffres-clés liasse
| Item | Valeur exacte |
|---|---:|
| Total bilan | **155 561,27 €** |
| CA | **123 600,00 €** |
| Résultat net | **32 646,14 €** |
| Effectif moyen | 1,00 (+ 1 apprenti) |
| TVA collectée annuelle | 20 040 € |
| TVA déductible annuelle | 1 288 € |
| Résultat fiscal | 39 147 € (réintégrations TVS 207 + amort. non déductibles 403 = 610 €) |

### Structure du résultat 2024 (synthèse compte de résultat, page 6 SC)
- Production vendue services (706000) : **123 600 €**
- Subventions (740000 Aide apprenti) : **1 500 €**
- Charges externes : 13 911 € (dont honoraires 2 478, voyages 2 222, restaurants 2 114, RCP 469, maintenance 3 104, locations 1 951)
- **Rémunérations 80 069 €** (salaires 13 598, congés payés 543, **rémunération gérant 46 305**, **URSSAF TNS 17 471**, tickets restaurants 2 152)
- Charges sociales nettes -1 001 € (URSSAF salarié 37, retraite 1, charges CP 4, indemnités transport 13, **titres restau remboursés -1 056**)
- DOT amort 1 033 €
- TVS : 207 € (635140)
- **Produits financiers 7 852 € (768000) — à investiguer (intérêts ? interco non identifiée ?)**
- Charges financières : 197 € (661160 intérêts emprunt Citroën C5)
- IS : 5 891 € (6 951 calcul théorique − ?, à vérifier la liasse 2065-SD)

### Détails immo 2024
- Citroën C5 acquis 29/10/2024 pour 30 000 € HT, amort linéaire 5 ans (20 %), taux mensuel 500 €, 2 mois d'amort = 1 033,33 €
- Emprunt 29 093 € capital restant dû au 31/12/2024 (intérêts payés 197 €)
- Pas d'autres immobilisations

### Écarts de centimes connus (à investiguer si besoin du détail)
| Compte | Bilan SC arrondi | Centimes connus |
|---|---:|---:|
| 281820 amort. matériel transport | 1 033 | **1 033,33** (liasse immos page 9) |
| Résultat exercice | 32 646 | **32 646,14** (attestation page 1) |
| Total bilan | 155 561 | **155 561,27** (attestation page 1) |

→ Reconstruction : actif net = 155 561,67 € ; passif = 155 561,14 € ; **écart 0,53 €** dont l'origine est probablement les centimes d'un compte du passif (URSSAF 18 776, TVA 18 876, ou C/C Benoit 43 810 — sans la balance détaillée Bepmale on ne sait pas lequel).
