---
tags: ["comptabilité", "odoo", "affacturage", "bpce-factor"]
created: 2026-04-12
---

# Brief — Comptabilité Guinet Digital Group · Odoo `guinet`

> Dernière mise à jour : 12/04/2026

---

## Règles absolues
- Toujours `dry_run=true` en premier → montrer le résultat → attendre confirmation explicite
- Ne jamais inventer ni calculer de montant — tout doit être lu directement dans les documents
- Toujours `company_id=4` sur tous les appels RPC comptables
- Ligne 411100/401100 → `partner_id` du tiers concerné ; lignes charges/TVA → `partner_id` BPCE Factor (410)

---

## Instance & société

| Élément | Valeur |
|---------|--------|
| Instance Odoo | `guinet` |
| Société cible | Guinet Digital Group |
| `company_id` | **4** |

> ℹ️ **Guinet Digital Group EST l'ancien Globasoft** — la SARL a été renommée mais le SIREN 985 298 900 est conservé (cf. liasse Bepmale 2024 où GDG figure sous le nom "GLOBASOFT" comme filiale 100 % de Guinet Group). Conséquence : les bordereaux BPCE Factor affichent toujours le nom **"GLOBASOFT"** (compte 50890DEUR) — ce n'est PAS une erreur du factor, c'est le nom historique. Le compte bancaire `512002 GLOBASOFT XX7328` porte aussi l'ancien nom.
>
> ⚠️ Ne pas confondre avec **Globasoft branche (company_id=2)** dans Odoo, qui est probablement un doublon ou un ancien paramétrage à clarifier — pas la même entité que GDG.
>
> 🏢 GDG est détenue à **100 %** par Guinet Group (holding, company_id=1). Tous les flux interco doivent transiter par **451 Groupe** avec contrepartie miroir dans Guinet Group.

---

## Journaux

| ID | Code | Nom | Type | Note |
|----|------|-----|------|------|
| 22 | FAC | Customer Invoices | sale | |
| 23 | FACTU | Vendor Bills | purchase | |
| 24 | OD | Miscellaneous Operations | general | |
| 25 | EXCH | Exchange Difference | general | |
| 26 | CABA | Cash Basis Taxes | general | |
| 27 | BNK1 | Bank (compte principal) | bank | |
| 28 | CSH1 | Cash | cash | |
| 29 | SLR | Salaries | general | |
| 30 | BNK2 | GLOBASOFT XX7328 | bank | |
| 31 | BNK3 | Compte TVA | bank | |
| 50 | GR-GG | Groupe - Guinet Group | general | |
| 52 | STJ | Valorisation des stocks | general | |
| 58 | MISC1 | Affacturage | general | ❌ **NE PLUS UTILISER** |
| 60 | MISC2 | Opérations de transfert | general | |
| 61 | FACTO | BPCE Factor | general | ✅ **Journal actif** affacturage |

---

## Comptes clés

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

---

## Partenaires clés

| Partenaire | `partner_id` |
|------------|-------------|
| BPCE Factor | 410 |
| GA SAS (Sébastien Thalamy) | 288 |
| ONE PINK | 290 |
| Sohoft Toulouse | 14 |

---

## Règles de comptabilisation de l'affacturage

*(source : https://www.compta-facile.com/comptabilisation-de-l-affacturage/)*

### 1. Cession des créances — journal FACTO (id=61)
Date : date de remise du bordereau

| Sens | Compte | Partenaire | Libellé |
|------|--------|-----------|---------|
| Cr | 411100 | client | Créance cédée TTC |
| Dr | 6225 | BPCE Factor (410) | Commission affacturage HT |
| Dr | 445660 | BPCE Factor (410) | TVA / commission affacturage |
| Dr | 4671 | BPCE Factor (410) | Net à recevoir (= Total − com. HT − TVA) |

> 4676 fonds de garantie **non utilisé** sur ce contrat — schéma à 4 lignes uniquement.

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

**3 bis. Remboursement du fonds de garantie**
En fin de contrat ou libération

| Sens | Compte | Libellé           |
| ---- | ------ | ----------------- |
| Cr   | 4676   | Fonds de garantie |
| Dr   | 512001 | Banque            |

> Non applicable sur ce contrat (4676 non utilisé) — documenté pour référence générale.
---

## État affacturage BPCE Factor — Juillet 2025 → Mars 2026

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

| FAC(s)                | FACTO id | full_reconcile |
| --------------------- | -------- | -------------- |
| FAC/00016 + FAC/00017 | 5459     | 627            |
| FAC/00019 + FAC/00020 | 5463     | 632            |
| FAC/00021 + FAC/00022 | 5467     | 637            |
| FAC/00023             | 5470     | 640            |
| FAC/00024             | 5473     | 645
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

**3 lignes ouvertes — aucun problème d'affacturage :**

| Facture | Partenaire | Montant | Statut |
|---------|-----------|---------|--------|
| FAC/2026/00010 | Aerotec & Concept | 16 476€ | Normal — éch. 02/05/2026, pas encore due |
| FAC/2026/00003 | ONE PINK | 576€ | En retard 72j — à relancer |
| FAC/2025/00007 | Map Technologies | 5 280€ | ⚠️ En retard **404 jours** — recouvrement requis |

---

## Google Drive — Comptabilité Groupe

Dossier racine : **Comptabilité Groupe** (`1gYr7sYGc1FCA9quDAe_odf4tMzPlmaAy`)

```
Comptabilité Groupe/
├── _Groupe/                              ← compte MCP: groupe
├── Globasoft ESN/                        ← compte MCP: globasoft
│   ├── 2025/
│   │   ├── Affacturage BPCE Factor/      ID: 1uVRqJu6a9UbVrMwCMH67lCQZnzB0lX7v
│   │   │   ├── Octobre 2025/             ID: 16fk1RNezQvQMi7w6VbzYufABjYjlDPdz  ✅ 4 fichiers
│   │   │   ├── Décembre 2025/            ID: 1oPJO3a8Gmjwqe6uIkndFf8TnQZceqaYk  ✅ 3 fichiers
│   │   │   ├── Juillet 2025/             ⏳ à créer
│   │   │   ├── Août 2025/                ⏳ à créer
│   │   │   └── Septembre 2025/           ⏳ à créer
│   │   ├── Factures Clients/
│   │   ├── Factures Fournisseurs/
│   │   ├── Relevés Bancaires/
│   │   ├── Notes de Frais/
│   │   └── Déclarations Fiscales/
│   └── 2026/  (même structure)
├── Guinet Group/                         ← compte MCP: guinet
├── Guinet Digital Group/                 ← compte MCP: digital
└── Le Petit Cerf/                        ← compte MCP: petit_cerf
```

### Comptes MCP gdrive

| Compte MCP | Société |
|---|---|
| `globasoft` | Globasoft ESN |
| `guinet` | Guinet Group |
| `digital` | Guinet Digital Group |
| `petit_cerf` | Le Petit Cerf |
| `groupe` | Transversal groupe |

### Raccourcis MCP gdrive

| Raccourci                                              | Contenu                             |
| ------------------------------------------------------ | ----------------------------------- |
| `racine`                                               | Dossier racine de la société        |
| `"2025"` / `"2026"`                                    | Année                               |
| `2025_factures_clients`                                | Factures clients 2025               |
| `2025_factures_fourn`                                  | Factures fournisseurs 2025          |
| `2025_releves_bancaires`                               | Relevés bancaires 2025              |
| `2025_notes_de_frais`                                  | Notes de frais 2025                 |
| `2025_declarations`                                    | Déclarations fiscales 2025          |
| `2026_factures_clients` · `2026_factures_fourn` · etc. | Idem 2026                           |
| `juridique`                                            | Statuts, Kbis, PV d'AG, baux        |
| `social_2025` / `social_2026`                          | Fiches de paie, contrats            |
| `2026_releves_bancaires`                               | Relevés bancaires 2026              |
| `2026_notes_de_frais`                                  | Notes de frais 2026                 |
| `2026_declarations`                                    | Déclarations fiscales 2026          |
| `social`                                               | Dossier Social parent (2025 + 2026) |


> ⏳ Raccourci `2025_affacturage` à ajouter (ID : `1uVRqJu6a9UbVrMwCMH67lCQZnzB0lX7v`)

### Authentification
OAuth2 Desktop — token : `C:/Users/Shadow/secrets/gdrive_token.json`
Compte : `guinetb@guinet-group.com` — tous les comptes MCP partagent le même token.

### Nommage bordereaux sur Drive
`Bordereau de remise factures ou avoirs [Mois] [Année]_[N].pdf`
Sources locales : `C:/Users/Shadow/Downloads/Factor BPCE/`

### Anciens dossiers (hors hiérarchie)
`Factures Fournisseurs 2024` · `Factures clients 2024` · `Scans` · `Scans faits` · `Documents banque` · `A comptabilisé` / `Dans Odoo`

---

## Points ouverts (au 12/04/2026)

| #   | Statut | Action                                 | Détail                                                                                                             |
| --- | ------ | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| 2   | ⏳      | **Lettrage 4671**                      | Lignes non lettrées : id=5430 (13 928,35€) et id=5435 (12 125,86€)                                                 |
| 3   | ⏳      | **Pièces jointes Odoo — 12 ODs FACTO** | Attacher bordereaux aux ids **5448–5454** (sur Drive) et **5459, 5463, 5467, 5470, 5473** (déposer Drive d'abord)  |
| 4   | ⏳      | **Dépôt Drive Juil/Août/Sept 2025**    | Créer dossiers sous `Affacturage BPCE Factor` puis déposer 5 bordereaux (`C:/Users/Shadow/Downloads/Factor BPCE/`) |
| 5   | ⏳      | **Raccourci `2025_affacturage`**       | Ajouter dans config MCP gdrive (ID : `1uVRqJu6a9UbVrMwCMH67lCQZnzB0lX7v`)                                          |
| 6   | ⚠️     | **Map Technologies FAC/2025/00007**    | 5 280€ impayé 404 jours (éch. 03/04/2025) — relance contentieux ou provisionnement                                 |


---



- Toutes les lectures et modifications dans Odoo passent **exclusivement par le MCP** (`odoo:*`) — ne jamais utiliser le navigateur pour lire ou écrire des données comptables




---

## Données structurelles (issues du bilan Super Compteur 2024)

> Source : `Plaq1224_9215.pdf` — comptes annuels au 31/12/2024 établis par **Cabinet Super Compteur** (déposé en 2025 sous le nom GLOBASOFT à la DGFiP).
> Voir fiche détaillée : [[Exercice 2024/03-Comptes-annuels-GDG-2024]]

### Identité

| Élément | Valeur |
|---|---|
| Forme juridique | SARL |
| SIREN | **985 298 900** |
| Capital social | 1 000 € (1 000 parts × 1 €) |
| Détention | **100 %** par GUINET GROUP SAS (SIREN 983391079) |
| Adresse siège | 6 Place du Président Wilson, 31000 Toulouse |
| Activité IS | Conseil en systèmes et logiciels informatiques |
| Régime | Régime simplifié d'imposition + TVA simplifiée |
| Effectif | 1 salarié + 1 apprenti |
| Gérant | Benoit Guinet (régime TNS — art. 62 CGI) |
| Renommage | Globasoft → Guinet Digital Group en **août 2025** |

### Experts comptables

| Cabinet | Rôle | Adresse |
|---|---|---|
| **Cabinet Super Compteur** | **Rédacteur des comptes annuels** | Toulouse |
| **CEC Marc BEPMALE & Associés** | "Conseil" (cité en zone 2065-SD) — par ailleurs rédacteur des comptes Guinet Group | 72 rue Riquet, Toulouse |

→ ⚠️ **Deux cabinets interviennent**. À clarifier qui sera le rédacteur principal pour 2025.

### Premier exercice (constitution)

- **01/02/2024 → 31/12/2024 (11 mois)**
- Total bilan : **155 561 €**
- CA : **123 600 €**
- Résultat net : **+32 646 €** (bénéfice)
- IS dû : 5 891 €
- Bénéfice imposable : 38 958 €

### Capitaux propres au 31/12/2024
- Capital : 1 000 €
- Résultat exercice : +32 646 €
- **Total : 33 646 €**

---

## ⚠️ Alertes identifiées par confrontation Super Compteur ↔ Odoo

### 1. Le 451000 Group dans Odoo est figé à 56 500 € depuis sept 2024

Le bilan Super Compteur affiche un **451000 C/C Guinet Group à 89 352 €** au 31/12/2024 (créance GDG sur la holding). Écart de **~33 000 €** : Super Compteur a saisi des opérations interco fin 2024 qui n'ont jamais été reflétées dans Odoo.

### 2. C/C Benoit Guinet 455010 = 43 810 € absent d'Odoo GDG

Le compte 455 (apport associé personne physique) ne semble pas exister dans le plan Odoo GDG. Comme pour Guinet Group avant alignement, les flux Benoit ↔ GDG sont probablement éparpillés sur d'autres comptes.

### 3. Citroën C5 — 30 000 € + emprunt 29 093 € — probablement absent d'Odoo

- Acquisition 29/10/2024 — **218200 Matériel de transport 30 000 €**
- Amortissement linéaire 5 ans — **281820 Amort. -1 033 €**
- Financement par emprunt — **164100 Emprunt 29 093 €**

Aucun de ces 3 comptes n'apparaît dans le brief Odoo GDG actuel. À créer + saisir dans l'à-nouveau 2024.

### 4. TVA à décaisser 18 876 € au 31/12/2024

Régime simplifié → **445510 TVA à décaisser** = grosse dette de TVA à payer en 2025. À vérifier si elle a été décaissée.

### 5. URSSAF gérant TNS 18 776 € au 31/12/2024

Dette **438600** importante. Le brief observait "431 URSSAF -39 €" en 2025 — incohérent, à investiguer.

### 6. Plan comptable Super Compteur (codes SAGE 6 chiffres)

Comptes utilisés par Super Compteur **probablement absents** d'Odoo GDG (à vérifier et créer pour l'à-nouveau) :
- 101300 Capital (vs 101000)
- 164100 Emprunt
- 218200 Matériel transport
- 281820 Amort. matériel transport
- 411000 CLIENTS (vs 411100)
- 418100 CLIENTS FACT À ÉTABLIR
- 425000 Avance acompte personnel
- 428200 CONGÉS À PAYER
- 437200 Caisse retraite salarié (différent de 437000)
- 438200 ORG.SOC. CH/CONGES À PAYER
- 438600 URSSAF gérant TNS
- 444000 ETAT IMPOTS S/BÉNÉFICES
- 445510 TVA À DÉCAISSER
- 445860 TVA / factures non parvenues (différent de 445660 TVA déductible)
- 445870 TVA / factures à établir
- 445872 TVA collectée en attente
- 455010 C/C Benoit Guinet
- 486000 Charges constatées d'avance
- 512000 Banque N°4634 (à mapper sur 512002 GLOBASOFT XX7328)
- 512100 Banque (à mapper sur 512001 BNK1)
- + nombreux comptes de charges/produits du compte de résultat
