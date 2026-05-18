---
tags: ["comptabilité", "odoo", "le-petit-cerf", "brief"]
created: 2026-05-08
---

---
tags: ["comptabilité", "odoo", "le-petit-cerf", "brief"]
created: 2026-05-08
---

# Fiche Comptable — Le Petit Cerf (company_id=7)

> Instance : `guinet` · Société : Le Petit Cerf · Restaurant / commerce
> Dernière mise à jour : 08/05/2026

---

## Journaux

| ID | Code | Nom | Type | Compte défaut |
|---|---|---|---|---|
| 37 | BQ1 | Bank | bank | Bank |
| 51 | BNK2 | Stripe | bank | CB BP Différé |
| 38 | CSH1 | Cash | cash | Cash |
| 34 | OD | Miscellaneous Operations | general | — |
| 39 | PA | Salaries | general | — |
| 53 | STJ | Valorisation des stocks | general | — |
| 33 | AC | Vendor Bills | purchase | Purchase of goods (or group) A |
| 32 | VE | Customer Invoices | sale | Goods for resale (or group) A |
| 57 | VINTE | Customer Invoices (Vinted) | sale | Goods for resale (or group) A |

> Note : le journal bank principal s'appelle **BQ1** (pas BNK1 comme les autres sociétés).

---

## Comptes clés

### Tiers
| ID | Code | Libellé | Type |
|---|---|---|---|
| 1906 | 411100 | Customers - Sales of goods or services | asset_receivable |
| 1891 | 401100 | Suppliers - Purchase of goods and services | liability_payable |
| 1917 | 421000 | Personnel — Remuneration payable | liability_current |
| 1928 | 431000 | Social security | liability_current |

### TVA
| ID | Code | Libellé |
|---|---|---|
| 1951 | 445660 | Deductible VAT on other goods and services |
| 1956 | 445710 | VAT collected |
| 3148 | 445712 | VAT credit to be carried forward (copie) |
| 1942 | 445200 | Value added tax due within the European Union |

### Interco / associés
| ID | Code | Libellé |
|---|---|---|
| 1972 | 451000 | Group |
| 3127 | 45500100 | Retrait ou dépense pour usage personnel (Benoit Guinet) |
| 3128 | 45500200 | Retrait ou dépense pour usage personnel (GUINET GROUP SARL) |

### Social (comptes spécifiques Le Petit Cerf)
| ID | Code | Libellé |
|---|---|---|
| 3135 | 437001 | Other social agencies (copie) |
| 3143 | 4370200 | Retraite - Klesia |
| 3144 | 43703000 | Prévoyance |
| 3126 | 437200 | Retraite et prévoyance de vos employés |
| 3145 | 43780000 | Autres organismes sociaux |

---

## État du lettrage (au 08/05/2026)

### Clients (411) — 4 lignes ouvertes, 79 €
| Partenaire | Montant | Retard | Détail |
|---|---|---|---|
| (sans partenaire) | -34 € | 100j | BNK1/2026/00003 + OD/2026/01/0001 |
| Pimporn Jawwanikul | 30 € | 31j | VE/2026/00002 |
| Chanyanut Kulartyut | 15 € | 30j | VE/2026/00003 |

### Fournisseurs (401) — 20 lignes ouvertes, 2 292 €

**Principaux soldes :**
| Partenaire | Montant | Nb lignes | Plus ancien |
|---|---|---|---|
| VP CONSEIL | 1 907 € | 9 | 179j — écritures factures + banque mêlées |
| Up France | 208 € | 1 | 181j |
| STICKER MULE ITALY SRL | 46 € | 1 | 172j |
| Banque Populaire Occitane | 41 € | 5 | 161j — frais bancaires |
| Digidom | 41 € | 2 | 162j — domiciliation |
| Gandi | 30 € | 1 | 200j — noms de domaine |
| AMAZON ONLINE FRANCE SAS | 19 € | 1 | 181j |

---

## Points ouverts

| # | Action | Détail |
|---|---|---|
| 1 | VP CONSEIL | 1 907 € — 9 lignes mixtes (factures FACTU + mouvements BNK1). Des montants positifs et négatifs coexistent, signalant un lettrage partiel ou des écritures de paiement non rapprochées. Clarifier. |
| 2 | Clients sans partenaire | -34 € — deux lignes (BNK1 + OD) sans partenaire associé, probablement un ajustement ou une erreur |
| 3 | Plan comptable | PCG français standard importé (comptes 4xxxxx), quelques comptes avec des longueurs de code non standard (4370200, 43703000, 43780000, 45500100, 45500200) à harmoniser |
| 4 | Canaux de vente | Le Petit Cerf a 3 canaux : ventes directes (VE), Vinted (VINTE), Stripe (BNK2). Vérifier que les flux sont bien séparés et lettrés. |

---

## Remarques

- Le plan comptable est le PCG français standard importé par Odoo, beaucoup plus propre que celui de Guinet Group. Quelques comptes custom ont des codes trop longs (7-8 chiffres).
- Les comptes 45500100 et 45500200 (retraits personnels Benoit Guinet et Guinet Group SARL) indiquent que le compte courant d'associé est ventilé par bénéficiaire.
- Le journal Stripe (BNK2) gère les encaissements CB e-commerce.
- Le journal VINTE gère spécifiquement les ventes via la plateforme Vinted.

---

## ⚠️ Anomalie potentielle — compte 45500200 mal nommé

> Voir règle de groupe : [[Brief-Compta-Transverse#⚠️ Règle de groupe — comptes 451 vs 455 (NE JAMAIS MÉLANGER)]].

Le compte **45500200 « Retrait pour usage personnel (GUINET GROUP SARL) »** (id 3128) suit la même convention erronée que le 455002 de GDG (corrigé le 10/05/2026 — voir [[Brief-Compta-GDG#⚠️ Règle 451 vs 455 — comptes courants associés]]).

**Problème** : "GUINET GROUP SARL" est une **personne morale** (la holding SAS, SIREN 983 391 079) — les flux Le Petit Cerf ↔ GG sont de l'**interco**, pas des retraits personnels. Ils devraient être sur **451000 Group (id 1972)**, pas sur un compte 455.

### Action corrective à prévoir

1. Auditer toutes les lignes posted sur 45500200 (id 3128) — combien, quels partenaires, quels montants
2. Si tous les flux ont `partner_id = Guinet Group` (holding) → migrer vers 451000 (id 1972)
3. Vérifier la symétrie côté GG : doit avoir une contrepartie sur 4511xx « C/C Le Petit Cerf »
4. Garder 45500100 (id 3127) pour Benoit Guinet personne physique — c'est le bon usage

> Priorité : Moyenne. À faire avant clôture 2025 LPC pour cohérence avec consolidation groupe.
