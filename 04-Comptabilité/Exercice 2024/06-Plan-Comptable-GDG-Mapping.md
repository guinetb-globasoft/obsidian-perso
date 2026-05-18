---
tags: ["comptabilité", "guinet-digital-group", "exercice-2024", "plan-comptable", "phase2"]
created: 2026-05-09
---

---
tags: ["comptabilité", "guinet-digital-group", "exercice-2024", "plan-comptable", "phase2"]
created: 2026-05-09
updated: 2026-05-09
---

# Phase 2 — Mapping plan comptable SAGE Super Compteur ↔ Odoo GDG

> Confrontation des comptes utilisés dans la liasse Super Compteur 2024 et plan Odoo GDG existant. Objectif : préparer l'à-nouveau Phase 5.

## Décision méthodologique

Le brief initial estimait "30+ comptes à créer". En réalité, **le plan Odoo français standard couvre déjà la majorité** des comptes SAGE utilisés. Seuls **10 comptes spécifiques** ont été créés (sous-comptes pour distinctions fines et comptes sociétés-spécifiques).

## Mapping détaillé

### Comptes existants dans Odoo (mapping 1:1)

| Compte SAGE | Libellé SAGE | Compte Odoo | ID Odoo |
|---|---|---|---|
| 101300 | Capital | 101300 (Subscribed capital - called up, paid) | 850 |
| 218200 | Matériel transport | 218200 (Intangible fixed assets - Transport equipment) | 1003 |
| 411000 | CLIENTS | **411100** (Clients) | 1149 |
| 418100 | CLIENTS FAE | 418100 (Customers - Invoices to be made out) | 1154 |
| 425000 | Avance acompte personnel | 425000 (Personnel - Payments on account) | 1164 |
| 428200 | Congés à payer | 428200 (Personnel - Accrued charges payable for holiday pay) | 1167 |
| 438200 | ORG.SOC. CH/CONGES | 438200 (Contributions for holiday pay) | 1173 |
| 438600 | URSSAF gérant TNS | 438600 (Other accrued charges payable) | 1174 |
| 444000 | ETAT IS | 444000 (State - Income tax) | 1184 |
| 445510 | TVA à décaisser | 445510 (VAT to be paid) | 1189 |
| 445860 | TVA / FNP | 445860 (Turnover taxes on non-received invoices) | 1207 |
| 445870 | TVA / FAE | 445870 (Turnover taxes on invoices to be issued) | 1208 |
| **445872** | TVA collectée en attente | **445740** (VAT collected on unsettled) — équivalent fonctionnel | 1200 |
| 486000 | CCA | 486000 (Prepayments) | 1248 |
| 512000 | Banque N°4634 | 512002 (GLOBASOFT XX7328) | 1603 |
| 512100 | Banque | 512001 (Bank principal) | 1597 |
| 451000 | C/C Guinet Group | 451000 (Group) | 1215 |
| 615510 | Entretien matériel | **615500** (Maintenance and repairs on movable property) — sous-compte plus large | 1339 |
| 606100 | Carburant | 606100 (Non-inventoriable supplies) | 1317 |
| 606300 | Petits équipements | 606300 (Maintenance and minor equipment supplies) | 1318 |
| 606400 | Fournitures admin | 606400 (Administrative supplies) | 1319 |
| 613200 | Locations immo | 613200 (Real property rental) | 1334 |
| 615600 | Maintenance | 615600 (Maintenance) | 1340 |
| 616100 | RCP | 616100 (Comprehensive risk) | 1341 |
| 622600 | Honoraires | 622600 (Fees) | 1359 |
| 622700 | Frais actes | 622700 (Legal and litigation fees) | 1360 |
| 623400 | Cadeaux clientèle | 623400 (Gifts to customers) | 1365 |
| 625100 | Voyages | 625100 (Travels and journeys) | 1376 |
| 625700 | Restaurants | 625700 (Receptions) | 1379 |
| 627000 | Frais bancaires | 627000 (Securities costs) — copie | 3136 |
| 635140 | TVS | 635140 (Tax on company vehicles) | 1403 |
| 641100 | Salaires | 641100 (Salaries, emoluments) | 1412 |
| 641200 | Congés payés | 641200 (Holiday pay) | 1413 |
| 645100 | URSSAF salarié | 645100 (URSSAF contributions) | 1418 |
| 645300 | Cotisations retraite | 645300 (Pension fund contributions) | 1420 |
| 645800 | Charges sur CP | 645800 (Contributions to other social agencies) | 1422 |
| 658000 | Charges div gestion | 658000 (Sundry current operating charges) | 1438 |
| 661160 | Intérêts emprunts | 661160 (Loans and similar debts payable) | 1439 |
| 681120 | Dot. amort. | 681120 (Appropriations to depreciation - Tangible) | 1472 |
| 695100 | IS | 695100 (Income tax due in France) | 1491 |
| 706000 | Prestations de services | 706000 (Services supplied) | 1505 |
| 740000 | Aides apprenti | 740000 (Operating grants) | 1532 |
| 758000 | Produits divers | 758000 (Sundry current operating income) | 1541 |
| 768000 | Produits financiers | 768000 (Other financial income) | 1555 |

### Comptes créés en Phase 2 (09/05/2026)

| Code | Libellé | Type | ID Odoo |
|---|---|---|---|
| 164100 | Emprunt Citroën C5 | liability_current | 3169 |
| 281820 | Amort. matériel de transport | asset_non_current | 3170 |
| 437200 | Caisse retraite salarié | liability_current | 3171 |
| 455010 | C/C Benoit Guinet | liability_current | 3172 |
| 616160 | Assurance emprunt | expense | 3173 |
| 641600 | Rémunération du gérant TNS | expense | 3174 |
| 641610 | Cotisations URSSAF TNS gérant | expense | 3175 |
| 647000 | Indemnités de transport | expense | 3176 |
| 648100 | Tickets restaurants | expense | 3177 |
| 649100 | Titres restaurants - Quote-part employé | expense | 3178 |

## Notes techniques

- Type Odoo `asset_fixed` non exposé par l'outil MCP `create_account` → utilisé `asset_non_current` à la place pour 281820 (équivalent fonctionnel).
- Le compte 451000 Group reste typé `liability_current` malgré le solde débiteur 89 352 € (créance GDG sur GG) — Odoo accepte les soldes des deux sens.
- 615510 mappé sur 615500 plutôt que créé (granularité SAGE plus fine, granularité Odoo suffisante).
- 627000 existe en double (1381 original + 3136 copie). Préférer 3136 ou nettoyer ultérieurement.

## Liens

- Bilan Super Compteur : [[03-Comptes-annuels-GDG-2024]]
- Brief GDG : [[../Brief-Comptable-Odoo]]
- Diagnostic : [[04-Diagnostic-GDG-Odoo-vs-SuperCompteur]]
