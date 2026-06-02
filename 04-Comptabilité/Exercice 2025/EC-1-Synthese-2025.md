---
tags: ["comptabilité", "guinet-digital-group", "exercice-2025", "expert-comptable", "synthese"]
created: 2026-05-21
destinataire: Super Compteur
société: Guinet Digital Group (SARL)
siren: 985 298 900
company_id_odoo: 4
exercice: 2025-01-01 → 2025-12-31 (12 mois)
---

# Synthèse exercice 2025 — Guinet Digital Group

> Note exécutive pour Super Compteur, snapshot Odoo au 21/05/2026. Document de cadrage : permet de balayer rapidement les chiffres-clés, identifier les points qui sortent du standard et localiser les sujets à arbitrer.

## 1. Identité & cadre

| Élément | Valeur |
|---|---|
| Société | **Guinet Digital Group** (ex-Globasoft jusqu'à août 2025) |
| Forme | SARL — gérant majoritaire Benoit Guinet |
| SIREN | 985 298 900 |
| Holding | 100 % filiale de Guinet Group (SAS) — SIREN à confirmer |
| Période exercice | **01/01/2025 → 31/12/2025** (12 mois) |
| Exercice précédent | 2024 court (01/02→31/12, 11 mois) — bilan Super Compteur disponible |
| À-nouveau au 01/01/2025 | OD/2024/12/A-NOUVEAU (Odoo id 5530, 156 595 €, posted, corrigée 09/05/2026 pour bug mapping 512001/512002/512003) |

## 2. Chiffres-clés 2025

| Métrique | 2025 | 2024 (rappel) | Évol. |
|---|---:|---:|---:|
| **CA HT** | **201 178 €** | 123 600 € | **+63 %** |
| dont Services (706000) | 200 949 € (99,9 %) | n/a | — |
| dont Goods (707xxx) | 230 € (0,1 %) | n/a | — |
| Subventions État (740000 — aide apprenti) | 2 500 € | n/a | nouveau |
| FAC clients postées | 39 (séquence 00001→00039, intacte) | 23 | +70 % |
| FACTU fournisseurs postées | 394 | ~70 | +463 % |
| Bordereaux affacturage (FACTO) | 29 ODs | 0 | nouveau |

### Top 5 clients 2025

| Rang | Client | CA 2025 |
|---|---|---:|
| 1 | Sohoft Toulouse | 149 970 € |
| 2 | GA SAS / Sébastien Thalamy | 27 004 € |
| 3 | AEROTEC & CONCEPT | 13 730 € |
| 4 | PINK SAS | 4 725 € |
| 5 | Map Technologies | 4 400 € ⚠️ (bloqué, voir §5) |

## 3. Trésorerie & tiers au 21/05/2026

> Soldes Odoo, lecture instantanée. Les balances comptables au 31/12/2025 figurent dans le grand livre joint séparément.

### Banque

| Compte | Type | Solde Odoo 21/05 | Note |
|---|---|---:|---|
| 512001 (BPCE 55621004634) | Compte courant principal | n/a (snapshot quotidien) | 13/13 statements 2025 complets et équilibrés |
| 512002 (BPCE CB 7328) | CB différé liée au 512001 | 0 € (compte de transit) | 13/13 statements 2025 complets et équilibrés |
| 512003 (BPCE 95621009495) | Compte annexe TVA | ~+6 309 € (à-nouveau corrigé) | Quasi-inactif depuis 08/2025 — voir §5 |

### Tiers

| Compte | Lignes ouvertes | Solde | Note |
|---|---:|---:|---|
| **411100 Clients** | 4 | **29 148 €** dont 17 052 € échu | Toutes 2026 — encaissement normal en cours (AEROTEC 16 476 + Sohoft 12 096 + ONE PINK 576) |
| **401100 Fournisseurs** | 115 | **8 026 €** échu | ~50 lignes Guinet Benoit (NDF) à apurer par OD vers 455010, voir §5 |
| **451000 Groupe (vers Guinet Group)** | ~49 | ~171 953 € débit | À-nouveau 89 352 € + flux 2025 reclassés (Phase L.1 10/05/2026) |
| **455010 C/C Benoit Guinet** | ~73 | ~4 344 € débit | Tampon pour avances/refacturations perso (NDF) |
| **4671 Compte courant BPCE Factor** | 48 | **-7 622 €** net créditeur | Décaissements > cessions à fin 2025 — voir dossier Factor joint |
| **4676 Fonds garantie BPCE Factor** | 22 | +9 341 € débit | 10 % retenu sur cessions, libérations mensuelles tracées |

## 4. Cohérence comptable

| Contrôle | Statut | Détail |
|---|---|---|
| Séquence FAC | ✅ Intacte | 00001→00039, pas de trou |
| Statements BNK1 | ✅ 13/13 équilibrés | `balance_end = balance_end_real` partout |
| Statements BNK2 | ✅ 13/13 équilibrés | corrigé 10/05/2026 |
| Drafts résiduels 2025 | ⚠️ 2 pièces | OD `VAT Juin` 62 € (Odoo id 5277) + BNK2/2025/00255 Up France 208 € (Odoo id 5005) |
| Comptes d'attente 471000 résiduels (2025) | ✅ Quasi-clos | 1 ligne BNK1 (6 €) + 3 lignes BNK2 (14,74 €) |
| Cohérence CA Odoo vs FAC | ⚠️ Écart à éclaircir | `get_chiffre_affaires` 201 178 € vs somme FAC HT 241 414 € — probablement ventilation 706/707 + dates de facturation |
| TVA `tax_repartition_line_id` | ⚠️ 1 anomalie | FAC/2025/00007 (Map Tech) pointe vers société "Le Petit Cerf" au lieu de GDG (id 566 vs 258 attendu) — voir §5 |

## 5. Sujets à arbitrer — vue résumée

> Détail complet dans le doc joint [[EC-3-Dossiers-A-Arbitrer]].

| # | Sujet | Montant | Type | Urgence |
|---|---|---:|---|---|
| A | **ODs de paie 2025** non saisies (12 mois) | salaires nets ~21 K€ déjà payés | Saisie compta paie | 🔴 Bloquant |
| B | **Bug TVA Map Tech** (FAC/2025/00007) | 5 280 € | Correction + lettrage encaissement | 🟡 |
| C | **Amortissement Citroën C5 2025** | 6 000 € (12 × 500) | Dotation manquante | 🔴 |
| D | **Affectation résultat 2024** | 32 646 € | OD AG (120000 → 110000) | 🟡 |
| E | **CCA inventaire 2025** | à chiffrer | RCP/IARD/mutuelle prépayées | 🟡 |
| F | **Solde 512003 Compte TVA** | +9 574 € | OD régul ou ré-imputation | 🟡 |
| G | **NDF Guinet Benoit 2026** (~50 lignes) | ~4 100 € | OD apurement 401 → 455010 | 🟢 hors exercice mais visible au bilan |
| H | **Lettrage 4671 BPCE Factor** | -7 622 € net cr | Lettrage paires complexes | 🟡 |

## 6. Documents joints

- [[EC-2-Mapping-Comptes-2025]] — Mapping comptes Odoo ↔ codes SAGE attendus (plan 2025 = plan 2024 + 7 comptes ajoutés)
- [[EC-3-Dossiers-A-Arbitrer]] — Détail des 8 sujets ci-dessus avec proposition de traitement
- [[EC-5-BPCE-Factor]] — Dossier consolidé affacturage : 12 bordereaux + 12 OD régularisations + commissions + libérations fonds garantie + écart résiduel
- [[Referentiel-Partenaires-Comptes-GDG]] — Référentiel 165 partenaires → comptes utilisés en 2025

## 7. Particularités méthodologiques 2025

> Points qui s'écartent du standard et qui valent la peine d'être signalés avant que vous ne les découvriez.

### a) GDG = ex-Globasoft (renommage social août 2025)
Le SIREN 985 298 900 apparaît dans le plan Bepmale 2024 sous le nom `GLOBASOFT`. Toutes les factures fournisseurs adressées à "Globasoft" jan-sep 2025 sont à imputer GDG sans réserve (même entité juridique).

### b) BNK2 (512002) = CB différé, pas un compte autonome
Le journal BNK2 reflète le détail des achats CB qui sont ensuite débités globalement en fin de mois sur BNK1 via la ligne `CARTE FACTURETTES CB`. `balance_start=0` à chaque statement. Ce n'est **pas** un second compte bancaire à part entière.

### c) Convention 451 vs 455
- **451000** = compte courant **inter-sociétés** (GDG ↔ Guinet Group SAS holding)
- **455010** = compte courant **associé personne physique** (Benoit Guinet, NDF, avances perso)

Le compte 455001 (copie historique) et 455002 (retraits perso GG) ont été migrés/archivés en mai 2026 (Phases L.1/L.2). Cf. journal de session dans [[00-Etat-de-la-situation]].

### d) Bug d'à-nouveau 2024 corrigé
L'à-nouveau OD/2024/12/A-NOUVEAU avait inversé les soldes 512001 et 512003 (6 309 € posté sur le compte principal au lieu du compte TVA, et -36 € posté sur la CB au lieu du compte principal). Corrigé le 09/05/2026 — détail dans [[Exercice 2024/07-OD-A-Nouveau-31122024-GDG]].

### e) Charges sociales saisies en 645xxx au paiement direct (sans OD de paie)
12 prélèvements URSSAF (~4 048 €) et 11 prélèvements Klesia (~904 €) ont été comptabilisés directement en 645100/645300 au moment du débit BNK1, sans contrepartie 431000/437200. Si vous préférez le schéma "OD de paie mensuelle / dette 431-437 / extinction par la banque", il faut reprendre — cf. dossier A.

### f) Affacturage BPCE Factor — 1ère année
Le contrat affacturage a démarré en 2025. 12 bordereaux Sohoft/GA SAS/ONE PINK (cession ~118 K€). Compte courant 4671 + fonds garantie 4676 (10 %) + commissions 6225 (affacturage) + 661600 (financement). Voir [[EC-5-BPCE-Factor]].

## 8. Accès Odoo

- Instance : `https://guinet-group.odoo.com` (le nom de domaine date d'avant le renommage)
- Société : sélectionner **Guinet Group** (= GDG dans le menu) — company_id=4
- Journal des sessions et historique des décisions : [[00-Etat-de-la-situation]] (document interne, 1787 lignes — pas nécessaire à votre analyse)
- Référentiel partenaires : [[Referentiel-Partenaires-Comptes-GDG]]

---

**Contact** : Benoit Guinet — disponible pour répondre aux questions par retour avant le rendez-vous.
