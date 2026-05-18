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
