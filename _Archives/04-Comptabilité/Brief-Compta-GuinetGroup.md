---
tags: ["comptabilité", "odoo", "guinet-group", "brief"]
created: 2026-05-08
---

---
tags: ["comptabilité", "odoo", "guinet-group", "brief"]
created: 2026-05-08
---

# Fiche Comptable — Guinet Group (company_id=1)

> Instance : `guinet` · Société : Guinet Group · Holding / structure groupe
> Dernière mise à jour : 08/05/2026

---

## Journaux

| ID | Code | Nom | Type | Compte défaut |
|---|---|---|---|---|
| 6 | BNK1 | Bank | bank | 101401 Bank |
| 8 | BNK2 | Compte BP Guinet Group 4463 | bank | 512110 BP Occitane |
| 14 | BNK3 | CB BP 8343 GUINET GROUP | bank | 101406 |
| 7 | CSH1 | Cash | cash | 101501 Cash |
| 3 | MISC | Miscellaneous Operations | general | — |
| 59 | MISC1 | Opérations de transferts | general | — |
| 2 | BILL | Vendor Bills | purchase | 600000 Expenses |
| 1 | INV | Customer Invoices | sale | 400000 Product Sales |

---

## Comptes clés

### Tiers
| ID | Code | Libellé | Type |
|---|---|---|---|
| 3149 | 411100 | BPCE Factor Compte courant | asset_receivable |
| 825 | 401100 | Fournisseurs biens et services | liability_payable |
| 827 | 421000 | Personnel — Rémunérations dues | expense |
| 826 | 431000 | URSSAF 31 | expense |
| 828 | 437000 | Autres organismes sociaux | expense |

### TVA
| ID | Code | Libellé |
|---|---|---|
| 843 | 445660 | TVA déductible |
| 21 | 445710 | TVA collectée |

### Trésorerie
| ID | Code | Libellé |
|---|---|---|
| 43 | 101401 | Bank |
| 822 | 512110 | BP Occitane |
| 56 | 101406 | GUINET GROUP XX8343 |
| 833 | 528000 | VIREMENT DE FONDS |
| 816 | 580000 | Virements internes |

### Charges principales
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

## État du lettrage (au 08/05/2026)

### Clients (411) — 1 ligne ouverte, 1 080 €
| Partenaire | Montant | Retard | Détail |
|---|---|---|---|
| Sohoft Toulouse | 1 080 € | 763j ⚠️ | PBNK2/2024/00001, éch. 05/04/2024 |

### Fournisseurs (401) — 105 lignes ouvertes, 34 405 €

Majoritairement des écritures BNK2/BNK3 de 2024 (fév–juil) jamais lettrées avec les factures fournisseurs correspondantes.

**Principaux soldes :**
| Partenaire | Montant | Nb lignes | Plus ancien |
|---|---|---|---|
| Franco-Thai Chamber of Commerce | 7 155 € | 2 | 687j |
| Globasoft branche | -7 000 € | 1 | 697j |
| Crèche Grand Rond | 6 000 € | 2 | 745j |
| Créche de région | 2 775 € | 2 | 756j |
| Hexeko SRL (UpOne) | 1 988 € | 11 | 785j |
| C&C France | 1 865 € | 2 | 804j |
| Air France | 1 810 € | 6 | 718j |
| CTA Events | 1 053 € | 1 | 749j |
| URSAFF | 1 038 € | 3 | 752j |
| CEC Marc BEPMALE & Associés | 592 € | 7 | 799j |

**Analyse** : le plan comptable Guinet Group est très générique (comptes 101xxx par défaut, noms en anglais). Les 105 lignes non lettrées 401 datent quasiment toutes de 2024 et correspondent à des paiements bancaires (BNK2/BNK3) non rapprochés de factures. Il y a probablement des factures manquantes ou des mouvements bancaires mal affectés.

---

## Points ouverts

| # | Action | Détail |
|---|---|---|
| 1 | Sohoft Toulouse 411 | 1 080 € non lettré, 763j — vérifier si créance ou erreur |
| 2 | Lettrage fournisseurs 401 en masse | 105 lignes (34 405 €) datant de 2024 — gros chantier de rapprochement |
| 3 | Plan comptable à nettoyer | Comptes par défaut Odoo (101xxx), libellés en anglais — envisager migration vers PCG français |
| 4 | Globasoft branche -7 000 € | Écriture débitrice fournisseur, probablement virement interco à reclasser |

---

## Remarques

- Le plan comptable utilise encore la numérotation Odoo par défaut (101xxx, 211000, 400000…) et non le PCG français (512xxx, 401xxx, etc.). À terme, envisager une migration.
- Le compte 411100 est libellé "BPCE Factor Compte courant" ce qui est incorrect pour un compte clients — probablement un reliquat de configuration.
- Les journaux BNK2 (BP 4463) et BNK3 (CB 8343) contiennent la majorité des écritures non lettrées fournisseurs.




---

## Données structurelles (issues du bilan Bepmale 2024)

> Source : `Plaq0324_976.pdf` — comptes annuels au 31/03/2024 établis par CEC Marc Bepmale & Associés (08/10/2024).
> Voir fiche détaillée : [[Exercice 2024/00-Comptes-annuels-GuinetGroup-2024]]

### Identité

| Élément | Valeur |
|---|---|
| Forme juridique | SARL |
| SIREN | **983 391 079** |
| Capital social | 5 000 € (5 000 parts × 1 €) |
| Associé unique | **Benoit Guinet** (100 %) |
| Adresse siège | 6 Place Pdt Wilson, 31000 Toulouse |
| Activité IS | Conseil pour les affaires et autres conseils de gestion |
| Régime | Régime simplifié d'imposition |
| Effectif | 1 salarié |

### Filiale

| Filiale | SIREN | Détention | Valeur titres |
|---|---|---|---|
| **Guinet Digital Group (ex-Globasoft)** | 985 298 900 | 100 % | 1 000 € |

> Le Petit Cerf n'apparaît PAS dans la liasse 2024 de Guinet Group → soit acquis/créé après mars 2024, soit pas une filiale de la holding. À clarifier.

### Expert comptable

- **C.E.C. Marc BEPMALE & Associés**
- 72, rue Riquet Bâtiment A, 31000 Toulouse
- T. 05 62 27 07 43
- Logiciel : SAGE Générations Experts

### Premier exercice (constitution)

- **01/01/2024 → 31/03/2024 (3 mois)**
- Total bilan : 9 064 €
- CA : 2 267 €
- Résultat net : **−2 207 €** (perte)
- **Déficit reportable** : 2 207 €

### Capitaux propres au 31/03/2024

- Capital : 5 000 €
- Report à nouveau : 0 €
- Résultat : −2 207 €
- **Total : 2 793 €**

---

## ⚠️ Alertes identifiées par confrontation Bepmale ↔ Odoo

### 1. Compte courant associé absent dans Odoo

Le bilan Bepmale au 31/03/2024 mentionne **C/C GUINET BENOIT 455100 = 1 473 € créditeur**.
**Aucun compte 455xxx ou 108xxx n'existe dans le plan comptable Odoo Guinet Group.**

→ Tous les flux personnels Benoit ↔ société sont actuellement mal imputés (471 Suspense ou éparpillés).
→ Action : créer **455100 Comptes courants d'associés - Benoit Guinet** (type liability_current).

### 2. Date de clôture fiscale Odoo incohérente avec Bepmale

| Source | Clôture |
|---|---|
| Bepmale (1er ex.) | **31/03/2024** |
| Odoo `res.company.fiscalyear_last_month` | **31/12** |

→ Soit Bepmale fait un exercice court 3 mois puis bascule à 12 mois civils, soit l'exercice est réellement 04→03. À clarifier avec Benoit avant clôture 2025.

### 3. 105 lignes 401 non lettrées datent toutes de 2024

Cohérent avec un démarrage début 2024 où les rapprochements bancaires n'ont jamais été faits. La ligne mystère "Globasoft branche -7 000 €" est très probablement un flux interco vers Guinet Digital Group à reclasser sur 451 (Groupe).

### 4. Plan comptable Odoo en anglais avec codes 101xxx

Le plan comptable utilise des codes Odoo par défaut (101401 Bank, etc.) au lieu du PCG français standard. Bepmale travaille avec un plan SAGE classique (512100 Banque, 401000 Fournisseurs divers, 408100 Fournisseurs FNP, 421000 Personnel, 431000 Sécu, 437200 ARRCO, 455100 C/C, 486000 CCA, 487000 PCA…). À l'export pour clôture annuelle, **mapping nécessaire** ou **migration** du plan comptable Odoo.

### 5. Comptes utilisés par Bepmale mais probablement absents/mal nommés dans Odoo

| Compte SAGE | Libellé Bepmale | Solde 31/03/2024 | Présent dans Odoo ? |
|---|---|---|---|
| 401000 | Fournisseurs divers | 1 778 Cr | ≈ 401100 (équivalent) |
| 408100 | Fournisseurs FNP | 412 Cr | À vérifier |
| 418100 | Clients factures à établir | 3 000 Dr | À vérifier |
| 421000 | Personnel | 1 298 Cr | ✅ existe (827) |
| 428200 | Dettes prov. CP | 177 Cr | À vérifier |
| 431000 | Sécurité sociale | 306 Cr | ✅ existe (826) |
| 437200 | ARRCO | 71 Cr | ≈ 437000 (828) |
| 438200 | Charges sociales sur CP | 3 Cr | À vérifier |
| 438600 | Autres charges à payer | 21 Cr | À vérifier |
| 455100 | **C/C Guinet Benoit** | 1 473 Cr | ❌ ABSENT |
| 486000 | Charges constatées d'avance | 1 680 Dr | À vérifier |
| 487000 | Produits constatés d'avance | 733 Cr | À vérifier |
| 778800 | Produits exceptionnels divers | 3 500 Cr | À vérifier |




---

## Plan comptable PCG aligné Bepmale (mis en place le 08/05/2026)

> Comptes créés ou retypés pour aligner Odoo sur le plan SAGE utilisé par Bepmale.

### Capital & immobilisations
| Code | ID Odoo | Libellé | Type |
|---|---|---|---|
| 101000 | 1 | Capital social | equity |
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
