---
tags: ["odoo", "perso", "comptabilite", "plan-comptes"]
created: 2026-04-15
---
 
---
tags: ["odoo", "perso", "comptabilite", "plan-comptes"]
created: 2026-04-14
updated: 2026-04-15
---

> ⚠️ **Cette note remplace Plan-Comptes-Perso-Odoo.md** — version consolidée au 15/04/2026

# Plan de comptes perso — Odoo (edu-perso-bguinet.odoo.com)

## Contexte
- Instance : **perso** (Odoo 19)
- Société : **perso-bguinet** (company_id=1, mono-société)
- Objectif : gestion des comptes bancaires personnels, analyse des dépenses
- Ne pas gérer comme les instances Globasoft et Guinet Group
- **ATTENTION Odoo 19** : le champ `company_id` n'existe plus sur `account.account` — utiliser `company_ids` (many2many). Ne jamais passer `company_id` aux outils `get_plan_comptable` ou `search_record` sur `account.account`.

---

## Journaux

### Comptes bancaires
| Code | ID | Nom | Type | Compte Odoo | Description |
|------|-----|-----|------|-------------|-------------|
| BNK1 | 13 | Bank (Banque Populaire) | bank | 512001 | Compte principal BP, 459 écritures importées (avr 2025 → avr 2026). Import PDF le 14/04/2026 via Claude Code (380 nouvelles + 79 existantes saisies manuelles janv-avr 2026) |
| BNK2 | 17 | REVOLUT COMPTE JOINT | bank | 512004 | Compte joint Revolut Benoit & Kwanchanok. Dépenses courantes du ménage (courses, resto, shopping, loisirs). Import déc 2025 → janv 2026 |
| BNK3 | 18 | REVOLUT PERSO BEN | bank | 512005 | Compte perso Revolut de Benoit. Sert principalement de **transit** : reçoit la rémunération dirigeant SARL Globasoft puis transfère vers BNK2 (compte joint). Import déc 2025 → mars 2026 |

### Journaux CB
| Code | ID | Nom | Type | Compte transit | Description |
|------|-----|-----|------|----------------|-------------|
| CBK | 15 | CB Kwanchanok (4561) | bank | 511111 | Dépenses carte CB*4561 K.GUINET. Import fév 2024 → avr 2026 |
| CBB | 16 | CB Benoit (7276) | bank | 511112 | Dépenses carte CB*7276 B.GUINET. Import fév 2024 → avr 2026 |

### Flux inter-journaux typiques
```
SARL Globasoft (rémunération)
    → BNK3 (Revolut Perso) [758110]
        → BNK2 (Revolut Joint) [580100]
            → dépenses courantes (alimentation, shopping, santé…)

BNK1 (Banque Populaire)
    ↔ BNK2 (Revolut Joint) [580100] — virements internes
    → charges fixes (loyer, prêt, énergie, assurances, crèche…)
    ← revenus (salaire via BP, CAF, crédits d'impôt, SNC Diamant)
```

---

## Comptes créés

### Charges fixes — logement et immobilier
| Code | Nom | Type | ID Odoo |
|------|-----|------|---------|
| 613100 | Loyer habitation principale | expense | 708 |
| 164100 | Prêt immobilier (CE Auvergne) | liability_current | 709 |
| 614100 | Charges copropriété (appt Limoges) | expense | 739 |

### Charges fixes — énergie et telecom
| Code | Nom | Type | ID Odoo |
|------|-----|------|---------|
| 606110 | Electricité / gaz (TotalEnergies) | expense | 710 |
| 626100 | Téléphone mobile (SFR) | expense | 711 |
| 626200 | Internet / box (SFR) | expense | 712 |

### Charges fixes — assurances et abonnements
| Code | Nom | Type | ID Odoo |
|------|-----|------|---------|
| 616110 | Assurance habitation (BPCE MRH) | expense | 713 |
| 616120 | Assurance vie / prévoyance (SwissLife) | expense | 714 |
| 618200 | Abonnements (Fnac Darty+, Netflix, Uber One, Amazon Music, etc.) | expense | 715 |

### Charges variables — vie courante
| Code | Nom | Type | ID Odoo |
|------|-----|------|---------|
| 625200 | Alimentation / restauration | expense | 722 |
| 625800 | Crèche / garde enfant | expense | 716 |
| 624600 | Péage autoroute | expense | 717 |
| 627300 | Frais bancaires / cotisation compte | expense | 718 |
| 658110 | Stockinvest / Locabox (stockage) | expense | 720 |
| 623810 | Dons et œuvres (Croix-Rouge) | expense | 721 |
| 580200 | Retraits espèces | asset_current | 723 |

### Impôts et transit CB
| Code | Nom | Type | ID Odoo |
|------|-----|------|---------|
| 442110 | Impôt sur le revenu (PAS) | liability_current | 725 |
| 511110 | Carte bancaire - transit (vers journal CB) | asset_current | 727 |
| 511111 | CB Transit Kwanchanok (4561) | asset_current | 735 |
| 511112 | CB Transit Benoit (7276) | asset_current | 736 |

### Virements et transferts
| Code | Nom | Type | ID Odoo | Usage |
|------|-----|------|---------|-------|
| 580100 | Virements internes | asset_current | 728 | Tous transferts entre BNK1 ↔ BNK2 ↔ BNK3 |
| 580110 | Transferts Wise (devises) | asset_current | 737 | Virements vers compte Wise (devises / Thaïlande) |
| 580120 | Virements famille entrants (Jean Guinet, Maman) | asset_current | 738 | Uniquement Jean Guinet et Maman |

### Revenus et recettes
| Code | Nom | Type | ID Odoo | Usage |
|------|-----|------|---------|-------|
| 758110 | Salaire / revenus activité (Globasoft) | income | 730 | Rémunération dirigeant SARL — arrive sur BNK1 (vir BP) ET sur BNK3 (Revolut Perso) |
| 758210 | CAF / prestations sociales | income | 732 | |
| 758310 | Crédit impôt / remboursement fiscal | income | 733 | |
| 758910 | Autres recettes (chèques, CB entrants) | income | 734 | |
| 752100 | Remboursement ancien loyer (SNC Diamant) | income | 740 | ~1 162 €/mois, avr 2025 → déc 2025 min. Arrive sur BNK1 et BNK2 |

## Codes ajustés (collision PCG standard)
- 658100 déjà pris → **658110**
- 442100 déjà pris → **442110**
- 511100 déjà pris → **511110**
- 758100 déjà pris → **758110**
- 758200 déjà pris → **758210**

---

## Comptes à créer (proposés, non encore validés)

| Code | Nom | Type | Justification |
|------|-----|------|---------------|
| 625300 | Santé / pharmacie / médecin | expense | Dr Guillemette Pierr, pharmacies, psy Breton Emma — vu sur BNK1 et BNK2 |
| 625400 | Shopping / achats divers | expense | Amazon, Fnac, La Grande Recre, Rituals, Centrakor, Gifi, Calzedonia, Dpam, Moulin Roty, H&M, Shein, Stradivarius |
| 625500 | Loisirs / sorties | expense | Fun Parc, Europark, Lumys Photo, Photomaton, Wecandoo |
| 624700 | Transports urbains | expense | Smtc Tisseo, futurs Uber trajet |

---

## Règles de ventilation (mapping libellé bancaire → compte)

### BNK1 (Banque Populaire)
| Mot-clé dans le libellé                             | Compte cible |
| --------------------------------------------------- | ------------ |
| FONCIA TOULOUSE                                     | 613100       |
| CE AUVERGNE                                         | 164100       |
| TotalEnergies (PRLV)                                | 606110       |
| SFR + mobile                                        | 626100       |
| SFR + box                                           | 626200       |
| BPCE Assurance                                      | 616110       |
| SWISSLIFE                                           | 616120       |
| FNAC DARTY (PRLV)                                   | 618200       |
| CRECHE / MINI CRECH                                 | 625800       |
| Autoroutes du                                       | 624600       |
| FRAIS COM / FAMILLE PREMIUM / COTIS FAMILLE PREMIUM | 627300       |
| STOCKINVEST / LOCABOX                               | 658110       |
| Croix-Rouge                                         | 623810       |
| UBER EATS                                           | 625200       |
| CASH SERVICES / CB LCL retrait                      | 580200       |
| DIRECTION GENE / PAS                                | 442110       |
| CARTE FACTURETTES CB                                | 511110       |
| Virement vers / EUROVIR Virement                    | 580100       |
| VIR M BENOIT GUINET (entrant depuis Revolut)        | 580100       |
| VIR INST Kwanchanok & Be (sortant vers BNK2)        | 580100       |
| SARL GLOBASOFT                                      | 758110       |
| CAF DE HAUTE GARONNE                                | 758210       |
| DGFIP CREDIMPOT / TOTALENERGIES rembours.           | 758310       |
| REM CHQ                                             | 758910       |
| EUROVIR Wise / Wise                                 | 580110       |
| VIR INST JEAN GUINET / EUROVIR Jean Guinet          | 580120       |
| VIR INST MAMAN                                      | 580120       |
| LIMOGES SYNDICA                                     | 614100       |
| EUROVIR Snc Diamant / VIR INST SNC DIAMANT          | 752100       |

### BNK2 (Revolut Compte Joint)
| Mot-clé dans le libellé | Compte cible |
|--------------------------|--------------|
| From Benoît G | 580100 (entrant BNK3→BNK2) |
| To BENOIT FRANCOIS MICHEL GUINET | 580100 (sortant BNK2→BNK1) |
| Sent from Revolut To M Benoit et Mme Guinet | 580100 (sortant BNK2→BNK1) |
| Benoit Guinet To SNC diamant | 752100 |
| netflix.com / Amazon Music / Uber *one Membership | 618200 |
| Carrefour* / Grand Frais / Monoprix / La Mie Caline / Chez Domi / Boulangerie / Le Rotisseur / Mc Donald's / Starbucks / Upone / Sushi Bea / La Brioche Doree / Black Pig / Distrib Alim / Intermarche / Perlette / Lpalc / Alain Cauquil / carrefour.fr | 625200 |
| Envoyé depuis Revolut To Jean Guinet | 580120 |
| Vinted Payment from Mangopay | 758910 |
| Dr Guillemette Pierr / Pharmacie* / Phcie* / Pharm* | 625300 (à créer) |
| Amazon Payments / Fnac / Rituals / La Grande Recre / Moulin Roty / Centrakor / Gifi / Dpam / Calzedonia / Normal Toulouse / Jeff De Bruges / Mignon / Yoursurprisefr / Midica / Benel / Stephan / Lili-Leone | 625400 (à créer) |
| Sarl Fun Parc / Europark Indoor / Lumys Photo / Photomaton / Wecandoo | 625500 (à créer) |
| Smtc Tisseo | 624700 (à créer) |
| From Kwanchanok G / To KWANCHANOK THONGMAI | ⚠️ à clarifier |
| Kwang Payment from Sas Guinet Group | ⚠️ à clarifier (salaire Kwanchanok ?) |
| Authie Clement | ⚠️ à clarifier |

### BNK3 (Revolut Perso Ben)
| Mot-clé dans le libellé | Compte cible |
|--------------------------|--------------|
| *Payment from Sarl Globasoft / Virement de SARL GLOBASOFT* | 758110 |
| To BENOIT FRANCOIS MICHEL GUINET & KWANCHANOK THONGMAI | 580100 (BNK3→BNK2) |
| From BENOIT FRANCOIS MICHEL GUINET & KWANCHANOK THONGMAI | 580100 (BNK2→BNK3) |
| Wecandoo | 625500 (à créer) |

---

## État de la ventilation du 471000 (Suspense) — au 15/04/2026

### Ventilations effectuées (78 lignes)

| Opération | Journal(x) | Nb lignes | Montant | Compte cible |
|-----------|------------|-----------|---------|--------------|
| SNC Diamant avr→nov 2025 | BNK1 | 8 | 9 296 € | 752100 |
| SNC Diamant déc 2025 | BNK2 | 1 | 1 162 € | 752100 |
| Wise oct→déc 2025 | BNK1 | 6 | 1 150 € | 580110 |
| Jean Guinet + Maman | BNK1 | 4 | 2 040 € | 580120 |
| Copro Limoges | BNK1 | 1 | 395 € | 614100 |
| Salaire Globasoft via Revolut | BNK3 | 17 | 11 630 € | 758110 |
| Virements internes BNK3↔BNK2 | BNK3 | 20 | ~11 535 € net | 580100 |
| Virements internes BNK1↔BNK2 | BNK2 | 11 | ~2 360 € net | 580100 |
| Virements internes BNK1 | BNK1 | 10 | ~3 264 € net | 580100 |

### Solde 471000 restant : **~111 174 €**

### Lignes encore en suspense — à traiter

**BNK1 — à clarifier :**
- VIR MME GUINET KWANCHANOK sortants (IDs 230, 386, 606, 680, 702, 874, 888, 890, 892, 894)
- VIR MME KWANCHANOK GUINE entrant (IDs 224, 472)
- EUROVIR M Guinet Ou Mme (ID 682)
- EUROVIR Aubineau Ezra (IDs 672, 798)
- EUROVIR Justine Aoustin (ID 674)
- EUROVIR Mme Fraga Adela (ID 726)
- VIR INST BRETON EMMA PSY (ID 582) — 180 € → 625300 santé (à créer)
- EUROVIR Ce Compte Appart (ID 796) — 500 € → lié appt Limoges ?
- CB orphelines CB****7276 et CB****4561 sur BNK1

**BNK2 — en attente comptes :**
- ~70 lignes dépenses courantes (alimentation, shopping, santé, loisirs, abonnements)
- From Kwanchanok G / To KWANCHANOK THONGMAI — à clarifier
- Kwang Payment from Sas Guinet Group (ID 7982) — -1 002,23 € à clarifier

**BNK3 :**
- Wecandoo (ID 8110) — 95 € → en attente 625500

---

## Règles de workflow — instance perso

1. **Toujours dry_run=true en premier** pour toute opération (create_account, update_record, reconcile_lines, etc.)
2. **Afficher un tableau récapitulatif clair au dry_run** : lignes concernées, libellé, montant, ancien compte → nouveau compte, total par compte cible
3. **Attendre la confirmation explicite** de l'utilisateur avant de passer en dry_run=false
4. Ne jamais enchaîner dry_run + exécution dans le même message
5. Toutes les lectures et modifications Odoo passent exclusivement par le MCP (odoo:*) — ne jamais utiliser le navigateur




---

## Contexte personnel — Benoit Guinet

### Identité
- **Benoit François Michel Guinet**
- Résidence principale : **Toulouse** (logement en location via Foncia Toulouse)
- Bien immobilier : **appartement à Limoges** (copropriété, syndic Limoges, charges via 614100)
- Ancien logement lié à SNC Diamant (remboursement ancien loyer ~1 162 €/mois)

### Famille et ménage
- **Kwanchanok Thongmai (épouse / conjointe)** — née Guinet par usage
  - Carte CB*4561 (journal CBK)
  - Compte Revolut personnel (virements « From Kwanchanok G » vers BNK2)
  - Revenus propres : « Kwang Payment from Sas Guinet Group » sur BNK2 (à clarifier)
- **Enfant(s)** : Vincent 24/12/2020 autiste, Noah 27/02/2023
- **Jean Guinet** — père, virements entrants réguliers vers BNK1 et sortants depuis BNK2
- **Maman** — virements entrants ponctuels vers BNK1

### Vie professionnelle
- **Dirigeant de SARL Globasoft** (ESN) — rémunération dirigeant versée :
  - Sur BNK1 via virement Banque Populaire (« SARL GLOBASOFT »)
  - Sur BNK3 via Revolut (« Payment from Sarl Globasoft ») — ~11 630 € déc 2025→mars 2026
- **Guinet Group** — structure groupe (holding ?) qui inclut aussi Guinet Digital Group, Le Petit Cerf
- Total rémunération Globasoft sur la période : ~51 680 € (BNK1 + BNK3 cumulés)

### Comptes bancaires personnels
- **Banque Populaire** (BNK1) — compte courant principal, charges fixes, revenus
- **Revolut Perso** (BNK3) — transit rémunération Globasoft → compte joint
- **Revolut Compte Joint** (BNK2) — dépenses courantes du ménage avec Kwanchanok
- **Cartes CB** : CB*4561 Kwanchanok, CB*7276 Benoit
- **Wise** — compte en devises (virements réguliers depuis BNK1, probablement lié Thaïlande / famille Kwanchanok)

### Autres flux identifiés
- **CAF Haute-Garonne** — prestations sociales (~19 033 € sur la période)
- **Prêt immobilier CE Auvergne** — ~210 €/mois
- **Loyer Foncia Toulouse** — ~890 €/mois
- **Crèche** — ~280-350 €/mois
- **SFR** — mobile + box
- **TotalEnergies** — électricité/gaz ~199 €/mois
- **SwissLife** — assurance vie/prévoyance
- **Stockinvest / Locabox** — box de stockage Toulouse
- **Croix-Rouge** — dons mensuels 15 €

### Personnes tierces dans les relevés (à clarifier)
- **Aubineau Ezra** — virements entrants récurrents (44,50 €, 148 €) — colocataire ? remboursement ?
- **Justine Aoustin** — virement entrant ponctuel (140 €)
- **Mme Fraga Adela** — virement entrant ponctuel (160 €)
- **Breton Emma** — psychologue (180 €)
- **Authie Clement** — achat ponctuel (27,70 €) sur BNK2
- **Stephan** — achat ponctuel (77 €) sur BNK2




---

## ⚠️ Contrainte technique Claude / Obsidian — à retenir

Claude **ne peut pas modifier** une note existante dans Obsidian. Il peut uniquement :
- **Ajouter du contenu en fin de note** (`append_to_note`)
- **Créer une nouvelle note** (`create_note`)

Ne jamais demander à Claude de "mettre à jour" ou "corriger" une section existante d'une note — il faut soit créer une note complémentaire, soit ajouter un addendum en bas.

---

## Soins Vincent (autisme) — scan complet au 15/04/2026

### Nature des virements — correction d'analyse

Tous les virements vers les prestataires soins Vincent sont des **sorties d'argent** (dépenses).
Dans Odoo, ils apparaissent en `credit` sur le compte banque (512001 ou 512004) = l'actif diminue = sortie.
Ne pas confondre avec des entrées.

### Prestataires identifiés dans les relevés

| Prestataire                 | Rôle                   | Journal(x)  | Nb virements | Total trouvé |
| --------------------------- | ---------------------- | ----------- | ------------ | ------------ |
| Justine Aoustin             | Équithérapie           | BNK1        | 2            | 245,00 €     |
| Mme Fraga Adela             | Psychomotricienne      | BNK1 + BNK2 | 7            | 760,00 €     |
| Tiphaine Porcher Labreuille | Musicothérapie         | BNK2        | 4            | 655,00 €     |
| Aubineau Ezra               | Educatrice spécialisée | BNK1        | 2            | 192,50 €     |


**Total dépenses soins identifiées : 2 032,50 €**



---

## Comptes soins Vincent — créés le 15/04/2026

| Code | Nom | Type | ID Odoo |
|---|---|---|---|
| 625350 | Soins accompagnement Vincent — global | expense | 743 |
| 625351 | Équithérapie | expense | 744 |
| 625352 | Psychomotricité | expense | 745 |
| 625353 | Musicothérapie | expense | 746 |
| 625354 | Éducatrice spécialisée | expense | 747 |

### Mapping prestataires → comptes (au 15/04/2026)
| Prestataire | Compte |
|---|---|
| Justine Aoustin | 625351 Équithérapie |
| Mme Fraga Adela | 625352 Psychomotricité |
| Tiphaine Porcher Labreuille | 625353 Musicothérapie |
| Aubineau Ezra | 625354 Éducatrice spécialisée |
| Breton Emma PSY | 625300 Santé (à créer) |


---


## ✅ Addendum 28/05/2026 — Journal BNK4 (Compte joint BP 15519952511)

### Découverte initiale

Le compte joint BP **15519952511** (Mme GUINET KWANCHANOK OU M GUINET BENOIT, IBAN FR76 1780 7000 7615 5199 5251 158, agence Toulouse Dupuy) n'était pas dans Odoo perso. C'est un compte distinct de BNK1 (= 65519354452). Il porte notamment :
- les **loyers perçus de l'appartement Limoges** (locataire MARTINEZ QUENTIN, agence Human Immobilier, ~550 €/mois)
- les **2 contrats d'assurance habitation BPCE** (Toulouse 016561859 + Limoges 016561995)
- le **PAS** prélevé en novembre 2025 (financé par virement BNK1)
- les charges **syndic Limoges** (4T2025)
- les virements vers le compte **CE Auvergne** qui alimente le prêt immo Limoges
- diverses sorties vers BNK1 ("Virement vers Compte De Depot")

→ **Compte critique pour la déclaration de revenus** (revenus fonciers 2044).

### Nouveau journal

| Code | ID | Nom | Type | Compte | IBAN |
|------|-----|-----|------|--------|------|
| **BNK4** | 19 | Bank (Banque Populaire — Compte Joint) | bank | 512006 | FR76 1780 7000 7615 5199 5251 158 |

### Nouveaux comptes créés (28/05/2026)

| Code | ID | Nom | Type |
|------|-----|-----|------|
| 512006 | 749 | Bank — Compte joint BP 15519952511 | asset_current |
| 512007 | 750 | Caisse d'Épargne — Compte appartement Limoges (transit prêt) | asset_current |
| 752200 | 751 | Loyers perçus appartement Limoges (Human Immobilier) | income |
| 616111 | 752 | Assurance habitation Toulouse (BPCE MRH 016561859) | expense |
| 616112 | 753 | Assurance habitation Limoges (BPCE MRH 016561995) | expense |
| 455110 | 756 | C/C associé — SAS Le Petit Cerf | liability_current |
| 455200 | 755 | C/C associé — SAS Guinet Group | liability_current |

> Note collision : 455100 voulait être utilisé pour Le Petit Cerf mais collision avec compte PCG standard (id 344 "Partners/associates - Current accounts - Principal"). 455110 utilisé comme sous-compte.

### Règles de ventilation BNK4 (libellé bancaire → compte)

| Mot-clé dans le libellé | Compte cible | Sûreté |
|---|---|---|
| VIR HUMAN IMMOBILIER / Virement proprietaire | 752200 (Loyers Limoges) | ✅ |
| PRLV SEPA BPCE ASSURANCE HABITATION 016561859 | 616111 (Toulouse) | ✅ |
| PRLV SEPA BPCE ASSURANCE HABITATION 016561995 | 616112 (Limoges) | ✅ |
| EUROVIR Syndic Appt Limo | 614100 (Charges copro Limoges) | ✅ |
| PRLV SEPA DIRECTION GENE | 442110 (PAS) | ✅ |
| FRAIS AUTO DECOUVERT / FRAIS COM INTERVENTION / FRAIS SUR SAISIE ADMIN / FRAIS NOTIF INTERDIC BDF / INT ARRETE DE COMPT / ARRETE DE COMPT MINIMUM FORFAITAIRE | 627300 (Frais bancaires) | ✅ |
| VIREMENT SAS LE PETIT CERF | 455110 | ✅ |
| VIREMENT SAS GUINET GROUP | 455200 | ✅ |
| **VIR M GUINET BENOIT OU / Virement vers Compte De Depot** | 471000 (compte d'attente) | ⚠️ Vir internes Joint↔BNK1 — à clarifier au rapprochement BNK1 |
| **VIR INST CE COMPTE APPAR / EUROVIR Ce Compte Appart** | 471000 (compte d'attente) | ⚠️ Vir vers CE Auvergne — à clarifier quand relevés CE importés |
| **VIR M GUINET BENOIT OU / Virement vers Compte Charges** | 471000 (compte d'attente) | ⚠️ 1 ligne 26/12/2025 — libellé inhabituel |

### Import 2025 réalisé le 28/05/2026

- **65 lignes** importées (jan→déc 2025), source : 13 PDFs (12 relevés mensuels 2025 + relevé n°12 2026 pour les jours 06-31/12/2025)
- **46 lignes ventilées** :
  - 12 loyers Human Immo → 752200 = **+6 591,18 €**
  - 11 BPCE Habit Toulouse → 616111 = -291,77 €
  - 11 BPCE Habit Limoges → 616112 = -137,78 €
  - 8 frais bancaires → 627300 = -221,81 €
  - 1 PAS → 442110 = -1 172 €
  - 1 Syndic → 614100 = -495 €
  - 1 vir SAS Le Petit Cerf → 455110 = -60 €
  - 1 vir SAS Guinet Group → 455200 = -90 €
- **19 lignes en attente sur 471000** :
  - 1 entrée mystère ref 0EJWHYT (01/01) +236,29 €
  - 12 virements internes "Vir vers Compte De Depot" (9 sorties + 3 entrants)
  - 5 virements "CE COMPTE APPAR" -2 100 €
  - 1 "Vir vers Compte Charges" 26/12 -125 €

### Source de référence
Dry-run détaillé (parsing des 12 PDFs) conservé dans : [[Import-15519952511-DryRun]]

### Période manquante
3 lignes du 05/01/2026 (BPCE 27,92 + 59,70 + débit 62 €) sont sur l'exercice 2026 et seront importées dans une future session.

### Points de vigilance fiscaux pour la déclaration 2025

| Sujet | Donnée | Action |
|---|---|---|
| **Loyers Limoges 2025** | 6 591,18 € (12 vir Human Immo encaissés) — **Human Immobilier** (gérant Limoges) annonce 5 923 € de loyers bruts | **Décision retenue : 5 923 €** en ligne 211 de la 2044 (chiffre engagé par Human Immo, plus avantageux fiscalement de ~315 € au TMI 30 %). Les 668 € d'écart représentent vraisemblablement un loyer 2024 perçu en janv 2025 + régul, à laisser hors 2025. |
| **Charges déductibles 2044** | Assur Limoges 137,78 € + Syndic 495 € + frais gestion Human Immobilier 672 € (652 admin + 20 autres) + intérêts CE Auvergne (à récupérer) + taxe foncière (à récupérer) | Compléter le dossier 2044 avec les justificatifs externes. |
| **Dons Croix-Rouge 165 €** | Reçu fiscal art. 200 CGI | Case **7UD** (réduction 75%, plafond 1 000 €) |
| **Don 15 € (asso non identifiée n°donateur 4144135)** | Reçu fiscal cumul 2025 | Case 7UD ou 7UF selon nature à identifier |
| **Don 10 € Diocèse Toulouse** | Daté **06/02/2026** | ⚠️ **Pas pour la déclaration 2025** — pour la 2026 (déposée en 2027) |
| **PAS prélevé sur compte joint** | 1 172 € le 03/11/2025 | À rapprocher du PAS BNK1 pour éviter double comptage |
| **Compte CE Auvergne (512007)** | 2 100 € envoyés en 2025 depuis le joint | Compte non importé dans Odoo — solde 512007 unilatéral pour l'instant |
| **Lignes BDF / OCF / saisie admin** | -100 € saisie + 2×30 € notif BDF | Situation Banque de France notifiée 24/09/2025 — à suivre avec conseiller |

---

## ✅ Addendum 28/05/2026 (suite) — Clarifications BNK1 + Import T1 2025 + nouveaux comptes utilisés

### Renommage BNK1 → "Compte Charges - BP"

Le journal **BNK1 (id 13)** a été renommé `Bank` → `Compte Charges - BP`. Conséquence du fait que le compte BP 65519354452 (Benoit titulaire principal, Kwanchanok co-titulaire) sert principalement à payer les charges récurrentes du ménage (loyer Foncia Toulouse, prêt CE Auvergne, énergie, télécom, assurances, crèche…).

### Cartographie complète des 2 comptes joints BP (au 28/05/2026)

| Compte BP | Titulaire principal | Co-titulaire | Journal Odoo | IBAN | Rôle |
|---|---|---|---|---|---|
| **65519354452** | M GUINET BENOIT | MME GUINET KWANCHANOK | **BNK1 (id 13)** "Compte Charges - BP" | FR76 1780 7000 7665 5193 5445 267 | Compte principal du ménage — charges récurrentes, revenus Globasoft + Guinet Group |
| **15519952511** | MME GUINET KWANCHANOK | M GUINET BENOIT | **BNK4 (id 19)** "Bank (Banque Populaire — Compte Joint)" | FR76 1780 7000 7615 5199 5251 158 | Compte secondaire — loyers Limoges (Human Immobilier) + 2 assurances habitation BPCE + virements vers CE Auvergne (prêt Limoges) |

### Comptes annexes BP (épargne / dépôt — pas de journal opérationnel)

| Compte BP | Type | IBAN | Notes |
|---|---|---|---|
| 85519952533 | Compte de dépôt secondaire Benoit | FR76 1780 7000 7685 5199 5253 330 | Très peu d'activité, ~12 € au 02/04/2025 |
| 85583952624 | **LDDS** Benoit | — | Solde ~10 €, intérêts exonérés |
| 95597988234 | **Livret A** Benoit | — | Solde ~10 €, intérêts exonérés |
| 75555354804 | **PEA / Compte titres** | — | Relevé annuel séparé, IFU à intégrer pour déclaration |

Ces comptes ne sont **pas importés** dans Odoo perso comme journaux opérationnels (volumes trop faibles). À tracer comme actifs au 31/12 si nécessaire.

### Import T1 2025 BNK1 — 28/05/2026

- **62 lignes** importées sur la période 01/01/2025 → 04/03/2025 (3 PDFs Banque Populaire)
- Source détaillée : [[Import-65519354452-T1-2025-DryRun]]
- **Couverture BNK1 désormais complète** sur 2025 (T1 + avr→déc) ✅

### 🎯 Prélèvements crèche Mini Crèche du Grand Rond identifiés sur BNK1

| Période | Nb prélèvements | Cumul € | Source |
|---|---:|---:|---|
| T1 2025 (janv-fév) | 2 | 556,00 € | Import T1 28/05/2026 |
| Avr→Déc 2025 | 8 | 2 883,91 € | BNK1 historique |
| **Total annuel 2025 (Noah)** | **10** | **3 439,91 €** | → Crédit 7GA estimé **1 720 €** |

### Règles de ventilation BNK1 (mise à jour)

Ajouts par rapport à la version v2 initiale :
- **PRLV SEPA ASS MINI CRECH** (Crèche Mini Crèche du Grand Rond) → **625800** Crèche / garde enfant (id 716) — utilisé en 2025 pour Noah
- **EUROVIR Mme Fraga Adela** → **625352** Psychomotricité Vincent (id 745) — paiement direct à la psychomotricienne (vs prestations Foncia Toulouse)
- **VIR SAS GUINET GROUP** (entrant ~997 €/mois) → **758120** Salaire Kwanchanok (id 748) — distinguer de 758110 Salaire Globasoft (Benoit)
- **PRLV SEPA SAS MULTI IMPA** → **616120** Assurance vie/prévoyance (à confirmer — assurance prêt ou autre)
- **PRLV SEPA MEDECINS DU MO** → **623810** Dons (= Médecins du Monde, n° donateur C4144135 vu sur les reçus fiscaux 2025)

### Lignes laissées en 471000 (Suspense) sur BNK1 T1

| Libellé | Montant | Motif |
|---|---|---|
| PRLV SEPA CA CONSUMER FI | -15,00 € | Origine du contrat à identifier |
| PRLV SEPA CREATIS | -1 029,52 € | Crédit conso à identifier (probablement Cofidis/Sofinco) |

→ À clarifier ultérieurement avec le user.

### IDs comptes Odoo perso utiles (récap)

| Code | Libellé | ID Odoo |
|---|---|---|
| 164100 | Prêt immobilier (CE Auvergne) | 709 |
| 442110 | Impôt sur le revenu (PAS) | 725 |
| 471000 | Suspense accounts | 362 |
| 511110 | Carte bancaire - transit | 727 |
| 580100 | Virements internes | 728 |
| 580110 | Transferts Wise (devises) | 737 |
| 580120 | Virements famille entrants | 738 |
| 580200 | Retraits espèces | 723 |
| 606110 | Électricité/gaz (TotalEnergies) | 710 |
| 613100 | Loyer habitation principale | 708 |
| 616110 | Assurance habitation (BPCE MRH) | 713 |
| 616120 | Assurance vie/prévoyance (SwissLife) | 714 |
| 618200 | Abonnements | 715 |
| 623810 | Dons et œuvres | 721 |
| 624600 | Péages autoroute | 717 |
| 625351 | Équithérapie Vincent | 744 |
| 625352 | Psychomotricité Vincent | 745 |
| 625353 | Musicothérapie Vincent | 746 |
| 625354 | Éducatrice spécialisée Vincent | 747 |
| 625800 | Crèche / garde enfant | 716 |
| 626100 | Téléphone mobile (SFR) | 711 |
| 626200 | Internet/box (SFR) | 712 |
| 627300 | Frais bancaires | 718 |
| 658110 | Stockage (Stockinvest/Locabox) | 720 |
| 752100 | Remboursement SNC Diamant | 740 |
| 758110 | Salaire/revenus Globasoft (Benoit) | 730 |
| 758120 | Salaire Kwanchanok (Guinet Group) | 748 |
| 758210 | CAF / prestations sociales | 732 |
| 758310 | Crédit impôt / remb fiscal | 733 |
| 758910 | Autres recettes | 734 |

### Découvertes parallèles (28/05/2026)

- **Crèche actuelle = Mini Crèche du Grand Rond** (Toulouse), pas Pomme de Reinette (= contrat W4711 dans `A classer\`, probablement ancien)
- **Pas de prélèvement Pajemploi/URSSAF en 2025** sur Odoo perso → pas de garde à domicile active → pas de case 7DB pour la déclaration 2025
- **Bulletins Kwang 2025** : 12/12 disponibles → net imposable annuel **14 496,36 €** (case 1BJ)
- **Décisions MDPH Vincent** : taux 50-80 %, **pas de demi-part fiscale supplémentaire** (nécessiterait ≥ 80 %)
- **Attestations CAF 2025** : AEEH + Alloc Fam + PAJE → **aucune prestation imposable**
- **Reçus fiscaux dons 2025** : Croix-Rouge 165 € + Médecins du Monde 15 € (case 7UD)
