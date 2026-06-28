---
tags: ["comptabilité", "odoo", "guinet-digital-group", "brief"]
created: 2026-05-09
updated: 2026-05-10 (synthèse clôture)
---

# Fiche Comptable — Guinet Digital Group (company_id=4)

> Instance Odoo : `guinet` · ESN du groupe — affacturage BPCE Factor.

> 🎯 **Tableau de bord clôture 2025** : voir [[Exercice 2025/00-Etat-de-la-situation#🎯 Synthèse exécutive — où en est-on ? (10/05/2026)]]
>
> **Effort restant estimé : ~26 h** (5 paquets SaaS déjà traités au 10/05 — Gandi, GitHub, Miro, Vercel, Google).

---

## Identité

| Élément | Valeur |
|---|---|
| Forme juridique | SARL |
| SIREN | **985 298 900** |
| Capital social | 1 000 € (1 000 parts × 1 €) |
| Détention | 100 % par Guinet Group SAS (SIREN 983 391 079) |
| Adresse siège | 6 Place du Président Wilson, 31000 Toulouse |
| Activité IS | Conseil en systèmes et logiciels informatiques |
| Régime | Régime simplifié d'imposition + TVA simplifiée (sur encaissements) |
| Effectif | 1 salarié + 1 apprenti |
| Gérant | Benoit Guinet (régime TNS — art. 62 CGI) |
| Ancien nom | Globasoft (renommage légal août 2025) |
| Logiciel comptable expert | **SAGE GENERATION EXPERTS** (Super Compteur) |

> ℹ️ Le compte bancaire `512002 GLOBASOFT XX7328` et les bordereaux BPCE Factor portent encore l'ancien nom — ce n'est PAS une erreur.
>
> ⚠️ **NE PAS CONFONDRE avec Globasoft ESN** : société distincte (JV 50 % Guinet Group + 50 % ZM Consulting), instance `globasoft`. GDG s'appelait Globasoft avant août 2025 mais ce sont deux personnes morales différentes. Voir [[Brief-Compta-Globasoft]].
>
> ⚠️ Ne pas confondre avec **Globasoft branche (company_id=2)** dans Odoo — doublon, pas la même entité.

### Premier exercice (Super Compteur)

- Période : **01/02/2024 → 31/12/2024** (11 mois)
- Total bilan : **155 561 €**
- CA : **123 600 €**
- Résultat net : **+32 646 €**
- Capitaux propres au 31/12/2024 : **33 646 €**

> Voir [[Exercice 2024/03-Comptes-annuels-GDG-2024]] pour le détail bilan Super Compteur.

---

## Journaux

| ID | Code | Nom | Type | Compte | Note |
|---|---|---|---|---|---|
| 22 | FAC | Customer Invoices | sale | 411100 | |
| 23 | FACTU | Vendor Bills | purchase | 401100 | |
| 24 | OD | Miscellaneous Operations | general | — | |
| 27 | BNK1 | Bank (compte principal) | bank | 512001 | Connexion bancaire auto — IBAN 55621004634 |
| 30 | BNK2 | GLOBASOFT XX7328 | bank | 512002 | CB différé — imports manuels — IBAN 55621004634 (carte CB) |
| 31 | BNK3 | Compte TVA | bank | 512003 | IBAN 95621009495 — quasi-inactif depuis sept 2025 |
| 61 | FACTO | BPCE Factor | general | — | ✅ Journal actif affacturage |
| 58 | MISC1 | Affacturage (déprécié) | general | — | ❌ NE PLUS UTILISER — conservé pour historique |

---

## Plan comptable Odoo (codes en place)

### Tiers
| ID | Code | Libellé |
|---|---|---|
| 1134 | 401100 | Fournisseurs |
| 1149 | 411100 | Clients |
| 1152 | 413000 | Clients — effets à recevoir (anciennes ODs MISC1) |
| 1160 | 421000 | Personnel — rémunérations |
| 1171 | 431000 | Sécurité sociale |
| 1215 | 451000 | Groupe (interco GDG → GG) |

### TVA
| ID | Code | Libellé |
|---|---|---|
| 1185 | 445200 | TVA intracommunautaire due |
| 1194 | 445660 | TVA déductible autres B&S |
| 1199 | 445710 | TVA collectée |

### Trésorerie
| ID | Code | Libellé |
|---|---|---|
| 1597 | 512001 | Bank — compte principal (BNK1) |
| 1603 | 512002 | GLOBASOFT XX7328 — CB différé (BNK2) |
| 1604 | 512003 | Compte TVA (BNK3) |

### Affacturage
| ID | Code | Libellé |
|---|---|---|
| 3150 | 6225 | Commissions d'affacturage |
| 3151 | 4671 | Compte courant BPCE Factor |
| 1443 | 661600 | Intérêts financement (escompte) |

### Charges (codes en place)
| ID | Code | Libellé | Usage |
|---|---|---|---|
| — | 606100 | Fournitures (eau, énergie) | Carburant, fournitures courantes |
| — | 607100 | Achats de marchandises (groupe A) | ⚠️ Compte par défaut Odoo — à éviter, reclasser |
| 1335 | 613500 | Locations mobilières | Domiciliation Digidom |
| 1340 | 615600 | Maintenance logiciels et abonnements | Abonnements SaaS, domaines, hébergement |
| — | 623400 | Cadeaux à la clientèle | |
| — | 625100 | Voyages et déplacements | |
| — | 625600 | Missions | Déplacements professionnels |
| — | 625700 | Réceptions | Restaurants, sorties clients |
| — | 626000 | Frais postaux et télécommunications | La Poste, frais postaux |
| — | 627000 | Frais bancaires | Frais BPCE |
| 1359 | 622600 | Honoraires (Fees) | Super Compteur — expertise comptable + bulletins de salaires |
| — | 647100 | Indemnités de transport | |

---

## Mapping partenaires → comptes comptables

> Référence pour la saisie des factures fournisseurs. Priorité : 615600 pour tout abonnement numérique, 625700 pour toute réception/restaurant.

### 615600 — Maintenance logiciels et abonnements

| Partenaire | Nature | Montant typ. |
|---|---|---|
| **Gandi** | Noms de domaine, hébergement | 6–18 €/an |
| **Mindeo** | Logiciel (abonnement mensuel) | 22,50–57,50 €/mois |
| **Screencastify** | Extension enregistrement écran | 20 €/an |
| **OpenAI** | API / abonnement IA | variable |
| **GitHub** | Hébergement code | ~17 €/mois |
| **Notion** | Outil de documentation | ~23 €/mois |
| **Adobe** | Suite créative | ~13 €/mois |
| **Miro** | Tableau blanc collaboratif | ~20 €/mois |
| **Vercel** | Hébergement web | ~34 €/mois |
| **Excalidraw / Plus** | Outil diagrammes | ~18 €/mois |
| **Shadow** | PC cloud | ~24 €/mois |
| **iLovePDF** | Outil PDF | ~7 €/an |
| **Patreon** | Abonnement contenu | variable |
| **Whop / Mindeo** | Marketplace logiciel | variable |
| **Microsoft** | Licences 365 | ~12 €/mois |
| **Uber One** | Abonnement Uber | ~6 €/mois |

### 625700 — Réceptions (restaurants, sorties)

| Partenaire | Nature |
|---|---|
| **KYOTO RAMEN** | Restaurant |
| **API RESTAURATION** | Restaurant |
| **SARL SPORT BAR** | Bar/restaurant |
| **BOWLING DU CHATEAU ROUSSILLON** | Sortie client |
| **LA GOUAILLE** | Restaurant |
| **AU POELE DE LA** | Restaurant |
| **DI CAPO** | Restaurant |
| **CASA PERLITA** | Restaurant |
| **LE TIRE BOUCHON** | Restaurant |
| **GAIA** | Restaurant |
| **SUPER U / CARREFOUR** | Courses (si repas professionnel) |

### 625600 — Missions (déplacements pro)

| Partenaire | Nature |
|---|---|
| **EasyPark** | Parking |
| **VELO TOULOUSE** | Vélo en libre-service |

### 625100 — Voyages et déplacements

| Partenaire | Nature |
|---|---|
| **Uber** | Trajets VTC |

### 606100 — Fournitures (carburant, énergie)

| Partenaire | Nature |
|---|---|
| **DYNEFF** | Carburant |
| **Station-service** | Carburant |

### 627000 — Frais bancaires

| Partenaire | Nature |
|---|---|
| BPCE (frais) | Frais de gestion bancaire |

### 626000 — Frais postaux et télécommunications

| Partenaire | Nature |
|---|---|
| **LA POSTE** | Frais postaux (envois, recommandés) |

### À clarifier
| **UP** | 48 € | Nature à confirmer (titre restaurant ou autre ?) |
| **QPF** | 5,50 € | Nature inconnue |
| **JOCH EXPLOIT** | 30–220 €/mois | Nature à confirmer (×6 en déc 2025) |
| **SARL TOUNAJ** | 50–170 € | Nature à confirmer |
| **LFC MONTAUDRAN** | 13,40 € | Nature à confirmer |

---

## Affacturage BPCE Factor

> Contrat sans fonds de garantie — schéma simplifié 4 lignes. Journal : **FACTO (id=61)**.

### 1. Cession des créances

| Sens | Compte | Partenaire | Libellé |
|---|---|---|---|
| Cr | 411100 | Client | Créance cédée TTC |
| Dr | 6225 | BPCE Factor (410) | Commission affacturage HT |
| Dr | 445660 | BPCE Factor (410) | TVA / commission |
| Dr | 4671 | BPCE Factor (410) | Net à recevoir |

### 2. Paiement factor → banque

| Sens | Compte | Libellé |
|---|---|---|
| Cr | 4671 | Compte courant BPCE Factor |
| Dr | 512001 | Banque |

### 3. Commission de financement mensuelle

| Sens | Compte | Partenaire | Libellé |
|---|---|---|---|
| Dr | 661600 | BPCE Factor (410) | Commission financement HT |
| Dr | 445660 | BPCE Factor (410) | TVA / commission |
| Cr | 4671 | BPCE Factor (410) | Compte courant BPCE Factor |

---

## 💸 Transactions sans facture fournisseur (imputation directe)

> Le débit bancaire suffit comme pièce justificative. **Ne PAS créer de BILL** — `update_record` direct sur la ligne BNK pour basculer le compte 471000 (suspense) → compte cible.

### Distinction des 2 cas (CRUCIAL)

| Cas | Description | Pattern Odoo |
|---|---|---|
| **A. Charge directe** | Pas de facture émise par le tiers, charge enregistrée à la date du débit | Bascule 471000 → compte de **classe 6** (charges) |
| **B. Règlement de tiers** | La charge a déjà été comptabilisée via OD paie / OD TVA / OD IS, le débit bancaire est juste le règlement | Bascule 471000 → compte **classe 4** (tiers : 421/431/437/444/445) qui se solde |

> ⚠️ Si tu mets sur compte 6 un débit qui aurait dû solder un compte 4, tu **comptabilises 2× la charge**. Toujours vérifier si une OD préalable existe.

---

### A. Charges directes (BNK1 + BNK2)

#### A1. Frais bancaires BPCE (627000 — sans TVA)

| Pattern texte BNK1 | Compte | Volume 2025 estimé | Notes |
|---|---|---:|---|
| `COMMISSION FACTURETTE CB` | 627000 | ~30 € | Commission par débit CB international |
| `FRAIS COM INTERVENTION` | 627000 | ~50 € | Frais com. mensuels |
| `FRAIS COM ANNUEL ACTU` | 627000 | 17,50 € | Cotisation annuelle compte |
| `FRAIS SCT INST B2B EXT` | 627000 | ~5 € | Frais virement SEPA externe |
| `FRAIS PRELEVEMENT IMPAYE` | 627000 | ~10 € | Rejet prélèvement |
| `VIR BLOCAGE SAISIE` | 627000 | 914,14 € | Frais d'avis à tiers détenteur |
| **Total frais bancaires** | | **~1 030 €** | |

#### A2. Assurances (616100 — sans TVA récupérable)

| Pattern BNK1 | Compte | Volume 2025 | Notes |
|---|---|---:|---|
| `PRLV SEPA BPCE IARD` | 616100 RCP | ~3 332 € (11 × 302,94 €) | Assurance pro mensuelle |
| `PRLV SEPA BPCE Vie PREV` | 616100 ou 616160 | ~72 €/an (12 × 6 €) | "Homme Clé Plus" — assurance dirigeant |

#### A3. Cotisations TNS gérant Benoit (645xxx — sans TVA)

| Pattern BNK1 | Compte | Volume 2025 | Notes |
|---|---|---:|---|
| `COTIS RYTHMEO PRO STE` | 645800 (charges sociales TNS) | ~580 €/an | Prévoyance pro TNS (CONTRAT CNV0008167429) |
| Cotisations URSSAF gérant TNS | 645100 ou 641610 (TNS) | variable | À identifier (probable mensuel) |

> 💡 Ces charges TNS sont propres au gérant Benoit (régime art. 62 CGI), distinctes des cotisations salarié.

#### A4. Restauration / réceptions (BNK2 → 625700 — TVA 10% non récup sans facture)

> Voir section [[#15.2 Restaurants / réceptions (~80 lignes)]]. ~5 600 € à basculer en charge directe.

#### A5. Carburant (BNK2 → 606100 — TVA 20% / 80% récup VP)

| Pattern BNK2 | Compte | Volume |
|---|---|---:|
| `TOTAL FR 31TOULOUSE` | 606100 | ~252 € |
| `CERTAS ESSOF032` | 606100 | 73 € |
| `DYNEFF STLESPIN` | 606100 | 21 € |
| `Total` (Total Energie) | 606100 | 68 € |

#### A6. Déplacements (BNK2 → 625100)

| Pattern | Compte | Volume |
|---|---|---:|
| `EasyPark SARL` (×14) | 625100 | ~228 € |
| `INDIGO 310020` | 625100 | 26 € |
| `RR HORODATEURS` | 625100 | 1 € |
| `VELO TOULOUSE` (×5) | 625100 | 30 € |
| `AIR FRANCE 057` | 625100 | 432 € |
| `RATP FR PARIS` | 625100 | 25 € |

#### A7. Frais postaux (626000 — TVA 20%)

| Pattern | Compte | Volume |
|---|---|---:|
| `LA POSTE 315550` (BNK2) | 626000 | 383 € |

#### A8. Petits achats / supermarché ponctuels

| Pattern | Compte | Volume |
|---|---|---:|
| `CARREFOUR/AUCHAN/SUPER U` (réception traiteur) | 625700 | ~360 € |
| `CARREFOUR EXPRE` (urgent fournitures) | 606300 | ~3 € |
| `SHADOW`, achats divers ponctuels | selon nature | variable |

---

### B. Règlements de comptes tiers (déjà passés en charge ailleurs)

> Ces débits **soldent un compte 4xx** déjà alimenté par une OD précédente. **Ne pas re-passer en charge**.

#### B1. Impôts DGFIP (444000 / 445510 — sans TVA)

| Pattern BNK1 | Compte cible | Volume 2025 | Notes |
|---|---|---:|---|
| `PRLV INT ETS DGFIP IS1-XXXX-2571` | 444000 État IS | ~30 706 € (10 268+3 946+5 891+9 500+1 607) | Acomptes IS ; charge passée en OD IS (695100 ↔ 444000) |
| `EUROVIR TVA YYYY-MM` | 445510 TVA à décaisser | variable | Solde la décl. TVA mensuelle ; charge enregistrée par OD TVA mensuelle (445710 ↔ 445510) |
| `PRLV INT ETS DIRECTION G AMR` | 444000 ou 6358 | variable | Avis Mise en Recouvrement — selon nature |

#### B2. Cotisations sociales salariés (437xxx — sans TVA)

> Ces prélèvements **soldent les comptes tiers alimentés par les ODs de paie mensuelles** (Phase I).

| Pattern BNK1 | Compte cible | Volume 2025 estimé |
|---|---|---:|
| `PRLV SEPA MALAKOFF HUMAN` | 437000 (Mutuelle/Prévoyance autres) | ~1 320 € |
| `PRLV SEPA HUMANIS PREVOY` | 437000 ou compte spécifique Humanis | ~5 030 € |
| `PRLV SEPA GIE KLESIA COT RETRAITE` | 437200 (Klesia retraite) | ~1 100 € |
| Prélèvement URSSAF | 431000 (Sécu) | variable mensuel |

> ⚠️ **Tant que les ODs de paie 2025 ne sont pas saisies (Phase I)**, ces prélèvements ne peuvent pas être lettrés (compte tiers vide). À traiter dans l'ordre : Phase I → puis lettrage règlements ici.

#### B3. Aide apprentissage État (740000 — produit, sans TVA)

| Pattern | Compte | Volume 2025 |
|---|---|---:|
| `VIR DRFIP ILE DE FRANCE ... AIDE UNIQUE` (crédit) | 740000 Subventions État | +2 500 € (5 × 500 €) |

> Spécifique à l'apprentissage. Crédit bancaire = produit direct.

#### B4. Tickets restaurant Up France (647200 — TVA 20% sur commission)

| Pattern | Compte | Notes |
|---|---|---|
| `EUROVIR Up France` ou BNK2 `UP FR 92GENNEVILLI` | 647200 (Tickets restau) | Charge à la date d'émission ; mais aussi 12 BILL Up draft à arbitrer (Phase A) |

---

### C. Virements internes (ne sont pas des "charges")

> Voir [[#⚠️ Règle 451 vs 455 — comptes courants associés]] pour la distinction interco vs personne physique.

| Pattern | Compte | Justification |
|---|---|---|
| `VIR INST/EUROVIR SAS GUINET GROUP` (`partner=Guinet Group`) | 451000 (Group) | Interco filiale → holding |
| `VIR INST/EUROVIR Benoit Guinet` / `MR GUINET BENOIT` | 455010 (C/C Benoit) | Compte courant gérant |
| `RET DAB ...` | 455010 (sauf si justifié pro) | Retrait espèces → C/C Benoit par défaut |
| `CB CASH SERVICES` | 455010 ou 625700 selon nature | À analyser cas par cas |
| `VIR INST SARL GUINET DIGITAL` (auto-virement) | 580001 (virement interne) | Virement entre comptes GDG |
| `EXT RETRO.COTIS.CB FIDELITE` (crédit) | 768000 (produit financier) | Rétrocession bancaire |

---

### D. Cas particuliers à investiguer (BNK1 471000)

| Ligne | Date | Montant | Pattern | Hypothèse |
|---|---|---:|---|---|
| ID 11609 | 30/12/2025 | 127,43 € | `PRLV SEPA SUPER COMPTEUR SC regul` | Régul cabinet — créer BILL Super Compteur ou imputer directement 622600 |
| ID 7619 | 15/10/2025 | 110 € | `EUROVIR Cabinet F 198671` | Honoraires Cabinet F — créer BILL ou direct 622600 |
| ID 7960 | 21/07/2025 | 796,42 € | `EUROVIR Igensia 202503E5` | Igensia (formation/portage ?) — investiguer |
| ID 8268 | 15/05/2025 | 642 € | `EUROVIR 2025-05-08 Justi` | Indemnité justice/avocat ? — investiguer |
| ID 8418 | 22/04/2025 | 100 € | `EUROVIR 2025-04-12 Justi` | Idem |
| ID 7637 | 31/10/2025 | 6 € | `PRLV SARL GUINET DIGITAL N` | Auto-prélèvement — interne |

### Estimation totale "sans BILL" sur l'exercice 2025

| Type | Montant |
|---|---:|
| Charges directes BNK1 (frais bancaires, assurances, TNS) | ~5 010 € |
| Règlements tiers BNK1 (IS, TVA, mutuelle/retraite/prévoyance salarié) | ~37 460 € |
| Virements internes BNK1 (interco + C/C Benoit) | ~50 000 €+ |
| Charges directes BNK2 (restos + déplacements + carburant + La Poste + petits achats) | ~7 200 € |
| **Total estimatif** | **~99 670 €** |

> **Conclusion** : la majorité du volume restant peut être traitée par `update_record` batch direct **sans création de BILL**. La création de BILL est nécessaire uniquement pour : (1) les SaaS récurrents (Phase B, ~6 100 €), (2) les gros prestataires identifiés (Phase E, ~5 500 €), (3) les rares fournisseurs FR pour récupérer la TVA (Copy Top, France Auto, etc.).

---

## ⚠️ Règle 451 vs 455 — comptes courants associés

> Voir règle de groupe complète dans [[Brief-Compta-Transverse#⚠️ Règle de groupe — comptes 451 vs 455 (NE JAMAIS MÉLANGER)]].

### Mapping GDG (company_id=4)

| Type de flux | Compte | ID | Tiers attendu |
|---|---|---:|---|
| **Filiale GDG → Holding GG** (interco) | 451000 Group | 1215 | `Guinet Group` (personne morale, SIREN 983 391 079) |
| **GDG → Benoit Guinet** (rém., retrait perso, apport) | 455010 C/C Benoit Guinet | 3172 | `Benoit Guinet` ou `Guinet Benoit` (personne physique) |

### 🔴 Anomalie détectée 10/05/2026 — comptes "fantômes" à migrer

| Compte source | ID | Lignes 2025 | Montant | Cible | Justification |
|---|---:|---:|---:|---|---|
| **455002** Retrait perso GUINET GROUP SARL | 3138 | **38** | **+33 335 €** | → **451000** (Group) | Tous flux EUROVIR/VIR INST `partner=Guinet Group` (holding SAS) — c'est de l'interco, **pas** du retrait perso |
| **455001** Partners/associates - Principal (copie) | 3137 | **50+** | **+14 774 €** + à-nouveau **43 810 €** | → **455010** (Benoit) | Tous flux libellés "Retrait usage perso (Benoit Guinet)" + à-nouveau 31/12/2024 du C/C Benoit ; compte "(copie)" doublon Odoo |
| **455010** C/C Benoit Guinet | 3172 | 12 | +8 650 € | ✅ correct, à conserver | EUROVIR Benoit + RET DAB |

**Volumétrie totale à migrer : ~88 lignes / ~91 819 €** (en incluant l'à-nouveau 43 810 €).

### Plan de migration (Phase L — comptes courants)

1. **Migrer 455002 → 451000** (38 lignes) : `update_record` batch sur `account_id` 3138 → 1215. Vérifier que `partner_id=Guinet Group` est bien posé sur chaque ligne.
2. **Migrer 455001 (copie) → 455010** (50+ lignes incluant l'à-nouveau) : `update_record` batch sur `account_id` 3137 → 3172. Compléter `partner_id=Benoit Guinet` quand absent.
3. **Vérifier symétrie 451000** : après migration des 33 335 €, le solde 451000 GDG doit avoir augmenté ; doit être miroir avec 451100 GG (id 3179) côté holding. **Probable OD de régularisation côté GG** à créer pour les flux 2025 non encore comptabilisés là-bas.
4. **Archiver 455001 (copie) (id 3137) et 455002 (id 3138)** une fois vidés — `update_record` `active=false`.
5. **Documenter pour Super Compteur** : changement de méthode imputation 451 vs 455 sur l'exercice 2025 (cohérence ouverture future 2026).

> ⚠️ Avant de migrer, vérifier que les lignes 455001 / 455002 ne sont pas déjà lettrées (sinon dé-lettrer puis re-lettrer après migration).

---

## Partenaires clés

| Partenaire | `partner_id` |
|---|---|
| BPCE Factor | 410 |
| GA SAS (Sébastien Thalamy) | 288 |
| ONE PINK | 290 |
| Sohoft Toulouse | 14 |
| Map Technologies | 279 |
| Super Compteur (expert-comptable) | 116 |
| Gandi SAS | 46 |
| GitHub (GitHub Inc.) | 91 |
| Miro (RealtimeBoard Inc./BV) | 415 |
| Vercel Inc. | 416 |
| Google Cloud France SARL | 17 |

---

## Journaux bancaires — état au 10/05/2026

> Voir [[Exercice 2025/01-Audit-Journaux-Bancaires-2025-GDG]] pour l'audit détaillé.

| Journal | État | Remarques |
|---|---|---|
| BNK1 | ✅ **100% complet 2025** | 13 statements, tous `is_complete=oui`, `balance_end=balance_end_real` |
| BNK2 | ✅ **100% complet 2025** | 13 statements, tous `is_complete=oui` · 7 vieux 2024 purgés (10/05/2026) |
| BNK3 | Quasi-inactif | 9 transactions seulement (jan + août) — vérifier si compte fermé |

**Bug à-nouveau corrigé (09/05/2026)** : inversion mapping 512001/512002/512003 dans l'OD/2024/12/A-NOUVEAU (id 5530) corrigée. Voir [[Exercice 2025/01-Audit-Journaux-Bancaires-2025-GDG]].

**BNK1 statements corrigés (09/05/2026)** : 79 lignes en double supprimées + 12 lignes orphelines assignées. Cause : import PDF avait créé des doublons des lignes bank feed. Voir [[Exercice 2025/01-Audit-Journaux-Bancaires-2025-GDG]].

**BNK2 statements corrigés (10/05/2026)** : 5 balances août→nov rectifiées (balance_start=0), statement décembre créé (id 96, 46 lignes, -2 221,30 €), 7 vieux statements 2024 purgés.

**BNK1 statement décembre créé (10/05/2026)** : 31 lignes orphelines assignées, statement id 97 (name 20260105, 31/12/2025, 730,12 €), PDF attaché. BNK1 passe à **13/13 statements** complets.

---

## Comptes à créer (Phase 2 GDG — vérifié 10/05/2026)

> Le terme "SAGE" dans les anciennes notes désignait simplement les codes utilisés par **Super Compteur** dans son logiciel SAGE Generation Experts. Ce sont les codes **PCG français standard** — pas des codes propriétaires SAGE. La liste initiale (11 comptes) était **largement obsolète** : 10/11 existaient déjà ou ont été créés en Phase 2 le 09/05/2026.

### ✅ Existants (vérifié 10/05/2026 — ne pas re-créer)

| Code | Libellé | ID Odoo | Origine |
|---|---|---:|---|
| 101300 | Capital social | 850 | Plan Odoo standard |
| 164100 | Emprunt Citroën C5 | 3169 | Créé Phase 2 (09/05/2026) |
| 218200 | Matériel de transport | 1003 | Plan Odoo standard |
| 281820 | Amort. matériel transport | 3170 | Créé Phase 2 |
| 425000 | Avances acomptes personnel | 1164 | Plan Odoo standard |
| 428200 | Congés à payer | 1167 | Plan Odoo standard |
| 438600 | URSSAF gérant TNS | 1174 | Plan Odoo standard |
| 444000 | État IS | 1184 | Plan Odoo standard |
| 445510 | TVA à décaisser | 1189 | Plan Odoo standard |
| 445660 | TVA déductible autres B&S | 1194 | Plan Odoo standard |
| 455010 | C/C Benoit Guinet | 3172 | Créé Phase 2 |
| 451000 | Group (interco GG) | 1215 | Plan Odoo standard |
| 615600 | Maintenance logiciels | 1340 | Plan Odoo standard ✅ batch SaaS |
| 613200 | Locations immobilières | 1334 | Plan Odoo standard |
| 613500 | Locations mobilières | 1335 | Plan Odoo standard |
| 622600 | Honoraires (Fees) | 1359 | Plan Odoo standard |
| 6225 | Commissions affacturage | 3150 | Custom Phase 2 |
| 4671 | C/C BPCE Factor | 3151 | Custom Phase 2 |
| 661600 | Intérêts financement | 1443 | Plan Odoo standard |
| 437200 | Caisse retraite salarié | 3171 | Créé Phase 2 |
| 616160 | Assurance emprunt | 3173 | Créé Phase 2 |
| 641600 | Rémunération gérant TNS | 3174 | Créé Phase 2 |
| 641610 | URSSAF TNS gérant | 3175 | Créé Phase 2 |
| 647000 | Indemnités de transport | 3176 | Créé Phase 2 |
| 648100 | Tickets restaurants | 3177 | Créé Phase 2 |
| 649100 | Titres restaurants — quote-part employé | 3178 | Créé Phase 2 |

### 🔴 Vraiment à créer (6 comptes)

| Code | Libellé | Type | Pourquoi en avoir besoin |
|---|---|---|---|
| **486000** | Charges constatées d'avance | asset_current | OD CCA fin d'année (RCP, mutuelle pré-payée pluri-mois) |
| **615700** | Entretien matériel/véhicule | expense | France Auto 1 045 € (BNK2 471000) |
| **618500** | Divers — formations | expense | ECOM Blueprint 697 €, Udemy 15 € |
| **623100** | Annonces et insertions | expense | Copy Top 715 € (imprimerie) |
| **626000** | Frais postaux et télécommunications | expense | LA POSTE 383 €, SFR 74 € |
| **647200** | Autres avantages sociaux (titres restau salarié) | expense | Up France 12 BILL drafts (1 656 €) — bascule depuis 6481/6491 |

> 💡 Avant de créer 647200, vérifier la sémantique exacte voulue par Super Compteur : **648100** (Tickets restau employeur, déjà créé id 3177) et **649100** (Quote-part employé, id 3178) couvrent peut-être déjà le besoin. À clarifier avec le cabinet.

### Comptes possiblement à créer plus tard (selon besoins clôture)

| Code | Libellé | Quand |
|---|---|---|
| 681120 | Dot. amort. (déjà id 1472) | ✅ existe — vérifier |
| 109000 | Capital souscrit non appelé | si applicable |
| 110000 | Report à nouveau | OD affectation résultat 2024 |
| 120000 | Résultat de l'exercice | clôture |
| 6358 | Autres droits enregistrement | si AMR DGFIP |
| 758000 | Sundry current operating income | déjà id 1541 ✅ |

---

## Points ouverts — clôture 2025

| # | Action | Détail |
|---|---|---|
| 1 | Reclasser lignes en 607100 | KYOTO RAMEN, API RESTAURATION, SPORT BAR, BOWLING, DYNEFF, LA POSTE |
| ~~2~~ | ~~Statements BNK1 nov+déc 2025~~ | ✅ Corrigé 09/05/2026 |
| ~~3~~ | ~~Statements BNK2 jan→déc 2025~~ | ✅ Corrigé 10/05/2026 — 13 statements complets, 7 vieux purgés |
| ~~6~~ | ~~Statement décembre BNK1~~ | ✅ Créé 10/05/2026 — id 97, 31 lignes, 730,12 € |
| 4 | Phase 2 GDG | Créer les comptes SAGE manquants + saisir à-nouveau 2024 complet |
| 5 | Interco GDG ↔ GG | 451000 GDG = 89 352 € (Super Compteur) vs 56 500 € Odoo → OD complémentaire |
| 7 | Fix ligne 11615 (BNK1/2025/00487) | Compte 471000 → 580001 (CARTE FACTURETTES CB déc 2025) |
| ~~8~~ | ~~Fix statement 76 BNK2~~ | ✅ Déjà correct en Odoo (-2 443,97) — typo dans les notes corrigé |
| ~~9~~ | ~~34 lignes orphelines BNK1 nov~~ | ✅ Toutes supprimées 10/05/2026 — ⚠️ 10 lignes statement 89 à re-lettrer (COMMISSION CB + RYTHMEO + FRAIS SAISIE) |
| ~~10~~ | ~~Digidom 2025-2026~~ | ✅ 17 factures créées (613500), lettrées BNK1, PJ attachées — 10/05/2026 |
| ~~11~~ | ~~Super Compteur 2024-2026~~ | ✅ 11 factures créées (622600), 7 lettrées, 4 partielles/à investiguer — 10/05/2026 |
| 12 | Super Compteur F042517610 | 864 € (mai 2025) — PDF manquant, facture non créée |
| 13 | BNK1 ligne 4177 (-127,43 €) | "SC regul Guinet Digital Consulti" 30/12/2025 — à identifier et lettrer |
| 14 | Bepmale / Guinet Group SAS | 6 factures honoraires sociaux (CEC Bepmale) → à créer dans instance Globasoft |
| ~~15~~ | ~~GitHub 2025~~ | ✅ 15 factures créées (615600), lettrées BNK2, PJ attachées — 10/05/2026. Partner id=91 |
| ~~16~~ | ~~Miro 2025~~ | ✅ 12 factures créées (615600), lettrées BNK2, PJ attachées — 10/05/2026. Partner id=415. Jan–Oct : RealtimeBoard Inc. (USD), Nov–Déc : RealtimeBoard BV (EUR 20€) |
| ~~17~~ | ~~Gandi 2025 (15 débits CB)~~ | ✅ 15 factures créées (615600, TVA 20%), lettrées BNK2, PJ attachées. Partner id=46. H2 (10/05/2026) : FACTU/2025/07/0024–0026, /08/0018–0019, /09/0033, /10/0028–0029, /11/0029–0030, /12/0012. H1 (10/05/2026) : FACTU/2025/02/0007 (7,20€), /05/0018 (115,15€), /06/0024 (71,22€), /06/0025 (29,99€) |
| 18 | Gandi prépayées (14 factures env.) | Payées via solde prépayé Gandi — pas de débit CB. PDFs disponibles. Décider si on crée des factures Odoo. H1 : 05/01, 05/02, 01/03, 05/03, 31/03, 30/04, 05/05, 13/05 (avoir -7,20€), 30/05, 05/06. H2 : 29/06 7,78€, 05/10 18€, 26/11 6,91€, 05/12 18€ |
| 19 | Gandi 460,51€ interco | Facture Jul 09 couvre 9 domaines GUINET GROUP — à régulariser en OD interco GDG→GG (451000). Comptabilisé en 615600 en attente. |
| 20 | Gandi 115,15€ interco (mai) | Facture 2025051100284 (FACTU/2025/05/0018) — 100% domaines le-petit-cerf.* = 100% GUINET GROUP. Comptabilisé en 615600 GDG. OD interco GDG→GG (451000) à créer. |
| ~~21~~ | ~~Vercel 2025 (12 factures CB)~~ | ✅ 12 factures créées (615600, autoliquidation USA), lettrées BNK2, PJ attachées — 10/05/2026. Partner id=416 (Vercel Inc.). Total 406,45€. FACTU/2025/01/0009 → /12/0013. Ignorés : 26B81A85-* ($0), 3B6CFA6A-0012 ($0), 0014-0017 (2026) |
| ~~22~~ | ~~Google Workspace 2025 (10 factures CB)~~ | ✅ 10 factures créées (615600, TVA 20% S FR), 9 lettrées BNK2, PDFs attachés — 10/05/2026. Partner id=17 (Google Cloud France SARL). Total 1 283,78€. FACTU/2025/01/0010 → /10/0031. ⏳ Oct BNK2 nov à importer. En suspens : ID 12719 (déc 2024), ID 9493 (12,10€ GCP?), Google Storage/Play ×4. |

---

## Références

- Brief comptable transversal : [[Brief-Comptable-Odoo]]
- Audit bancaire 2025 : [[Exercice 2025/01-Audit-Journaux-Bancaires-2025-GDG]]
- Comptes annuels 2024 : [[Exercice 2024/03-Comptes-annuels-GDG-2024]]
- Mapping pièces 2024 : [[Exercice 2024/05-Mapping-PJ-Moves-2024-GDG]]
