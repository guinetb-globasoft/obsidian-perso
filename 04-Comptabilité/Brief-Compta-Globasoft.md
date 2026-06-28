---
tags: ["comptabilité", "odoo", "globasoft", "brief"]
created: 2026-06-25
---

# Fiche Comptable — Globasoft ESN

> Instance Odoo : `globasoft` (https://globasoft.odoo.com)

> ⚠️ **NE PAS CONFONDRE avec Guinet Digital Group (GDG)** : GDG était anciennement appelée Globasoft (avant août 2025), mais c'est une personne morale distincte. GDG est dans l'instance `guinet`. Voir [[Brief-Compta-GDG]].

---

## Identité

| Élément | Valeur |
|---|---|
| Raison sociale | GLOBASOFT (SAS) |
| SIREN | **990 641 235** |
| SIRET (siège) | 990 641 235 00017 |
| N° TVA intra | **FR81 990641235** |
| Détention | **50 % Guinet Group + 50 % ZM Consulting** |
| Adresse siège | 8 Place Roger Salengro, 31000 Toulouse |
| Activité | ESN |
| Régime TVA | TVA sur encaissements |

> Source : `res.company` / `res.partner` ID 1 instance `globasoft` (relevé 25/06/2026). Forme juridique **SAS** confirmée par facture SEDOMICILIER (« Globasoft SAS »).

> ⚠️ **Identification d'entité sur facture fournisseur** — la boîte mail `globasoft-perso` (guinet.benoit@globasoft.fr) est transversale et reçoit aussi les factures de GDG. Toujours vérifier le « Bill to » avant de comptabiliser :
> - **Globasoft ESN** : TVA **FR81990641235** · adresse **8 Place Roger Salengro**
> - **GDG** (instance `guinet`, à ne pas mettre ici) : TVA **FR95985298900** · adresse **6 Place du Président Wilson**
> - Fournisseurs récurrents qui sont en réalité GDG (vus juin 2026) : **Gandi, Miro, Vercel, Screencastify**.

---

## Instance Odoo

| Paramètre | Valeur |
|---|---|
| Clé MCP | `globasoft` |
| URL | https://globasoft.odoo.com |
| Journal achats | Vendor Bills |
| Compte fournisseurs | 401100 |

---

## Règles TVA achats (tous fournisseurs)

Globasoft ESN est en **TVA sur les encaissements**. Cette règle s'applique à **tous les fournisseurs** sans exception.

| Paramètre | Valeur |
|---|---|
| Taxe à utiliser sur toutes les lignes d'achat | **20% S** (ID **27**) |
| Compte TVA déductible généré | 445640 Deductible VAT on unsettled transactions |

---

## Mapping fournisseurs → comptes de charge

> Relevé de l'existant Odoo au 25/06/2026 (factures `in_invoice` postées). À réutiliser pour toute nouvelle facture du même fournisseur.

| Fournisseur | Compte | Nature |
|---|---|---|
| VP CONSEIL | **622600** Fees | Expert-comptable (cf. section dédiée) |
| RICAUD JUSTINE | **622602** Avocate | Honoraires avocat |
| GUICHARD ANNE GERALDINE THI-THAI | **622600** Fees | Honoraires |
| SEDOMICILIER SAS | **613200** Real property rental | Domiciliation |
| REVOLUT BANK, UAB | **627000** Comptes bancaires | Abonnement / frais compte pro |
| Render | **615600** Maintenance informatique | Hébergement infra |
| Mailgun Technologies | **615600** Maintenance informatique | Service emailing |
| Google Cloud France | **6135000** Location logiciels informatiques | Workspace / Cloud |
| Odoo S.A. | **6135000** Location logiciels informatiques | Abonnement ERP |
| Canva PTY LTD | **6135000** Location logiciels informatiques | SaaS design |
| Excalidraw s.r.o. | **6135000** Location logiciels informatiques | SaaS |
| Bytedance PTE (CapCut) | **6135000** Location logiciels informatiques | SaaS |
| SnackThis (Jitter) | **6135000** Location logiciels informatiques | SaaS |
| UP COOP | **437800** Tickets restaurants (valeur faciale) + **604000** Achats prestations (commission) | Titres-restaurant — 2 lignes |
| PREVALY | **647500** Médecine du travail, pharmacie | Médecine du travail |

> **Nuance 615600 vs 6135000** : les abonnements logiciels SaaS « classiques » (Google, Odoo, Canva, Excalidraw, CapCut, Jitter) vont en **6135000 Location logiciels informatiques** ; l'hébergement applicatif (Render) et le service emailing (Mailgun) sont historiquement en **615600 Maintenance informatique**. Conserver la cohérence par fournisseur.

> **Cas UP COOP (titres-restaurant)** : la facture se ventile en 2 lignes — la valeur faciale des titres en **437800** (compte de tiers, pas une charge) et la commission UP en **604000**.

---

## Cabinet comptable — VP CONSEIL

VP CONSEIL assure la comptabilité courante de Globasoft ESN (expertise comptable, assistance sociale, bulletins de paie stagiaires).

| Paramètre | Valeur |
|---|---|
| Partenaire Odoo | VP CONSEIL (ID **361**) |
| SIRET | 93392457300019 · TVA FR26933924573 |
| Compte de charge | 622600 Fees (ID **430**) |

### Règles de saisie des factures VP CONSEIL

1. **Date comptable = date de la facture** (pas la date d'échéance, pas aujourd'hui).
2. **Libellé de la ligne TVA** = `VP CONSEIL {numéro_facture}` (ex. `VP CONSEIL F-26060481`).
3. Joindre le PDF à la facture Odoo après création.

### Prestations récurrentes et montants

| Prestation | Compte | PU | Qté | Remise | HT | TTC |
|---|---|---|---|---|---|---|
| Consultation — validation écritures mensuelles | 622600 | 100 € | 1 | 50 % | 50,00 € | 60,00 € |
| Expertise comptable (exercice en cours) | 622600 | 196,47 € | 1 | 0 % | 196,47 € | 235,76 € |
| Assistance matière sociale (exercice en cours) | 622600 | 33,00 € | 1 | 0 % | 33,00 € | 39,60 € |

> ⚠️ **Bug affichage PDF (ancien format `F-YYMM####`)** : la ligne consultation affiche HT = 125 € dans le PDF (PU 250 × 0,5 unité × remise 60 % fictive). La TVA (10 €) et le TTC (60 €) font foi. Saisir PU = 100, qty = 1, discount = 50 %.

### Deux formats de numérotation VP CONSEIL

| Format | Exemple | Caractéristiques |
|---|---|---|
| Ancien | `F-YYMM####` (ex. `F-26060481`) | Un fichier par prestation — bug d'affichage des montants HT |
| Nouveau | `F-2026-XXXXX` (ex. `F-2026-06490`) | Un fichier peut regrouper plusieurs prestations — montants fiables |

### Rapprochement bancaire mensuel

- Libellé du prélèvement : `COMPTA+SOCIAL MENSUEL Vp Conseil`
- Montant habituel : **−335,36 €** (consultation 60 + expertise+social 275,36)
- Outil : `reconcile_bank_line` avec les IDs des lignes `account_type = liability_payable` (401100) des deux factures concernées.

---

## Ventes — clients, produits et comptes de produit

> Relevé de l'existant Odoo au 25/06/2026 (factures `out_invoice` postées). Journal **Customer Invoices**, compte clients **411100**.

### Comptes de produit (classe 70) selon la nature de la prestation

| Compte | Libellé | Usage observé |
|---|---|---|
| **706000** | Services supplied | Modules / prestations de services génériques |
| **706100** | Ventes de prestations de services - Projet | Forfaits projet, acomptes projet, recette |
| **706200** | Ventes de prestations de services - TMA | TMA au temps passé (régie) |
| **706300** | Ventes de prestations de services - AT | Assistance technique |
| **706400** | Ventes SaaS MCP IFS | Abonnement SaaS MCP IFS |
| **707000** | Sales of goods | Développement livré, garantie |

### Clients récurrents

| Client | Prestations typiques | Comptes |
|---|---|---|
| **ONE PINK** | Modules IFS, projets, AT, développement | 706000 / 706100 / 706300 / 707000 |
| **GA SAS** | TMA développement régie (60 €/h) | 706200 |

### Produits (catalogue `product.template`)

> La plupart des produits n'ont **pas** de compte de produit forcé (`property_account_income_id` vide) : le compte est choisi **sur la ligne de facture** selon la nature (table ci-dessus). Deux exceptions ont un compte câblé sur le produit.

| Produit | Prix catalogue | Compte de produit forcé |
|---|---|---|
| **Développement** (ID 25) | 60 €/h | — (mettre 706200 TMA ou 707000 selon contexte) |
| **MCP IFS — Abonnement annuel** (ID 37) | 3 000 € | **706400** Ventes SaaS MCP IFS |
| **MCP IFS — Essai 30 jours** (ID 36) | 0 € | **706400** Ventes SaaS MCP IFS |
| **Management de projet, qualité** (ID 5) | — | **706000** Services supplied |
| **Formation** (ID 15) | 2 250 € | — |
| Autres (Recette, Garantie 3 mois, Datawarehouse, Dashboards PowerBI, Extracteurs, modules IFS…) | variable | — (compte choisi sur la ligne) |

> Produit générique le plus utilisé : **Développement** (60 €/h) pour la régie/TMA → ligne en **706200**.
