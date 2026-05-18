---
tags: ["comptabilité", "odoo", "brief", "transverse"]
created: 2026-05-08
---

---
tags: ["comptabilité", "odoo", "brief", "transverse"]
created: 2026-05-08
---

# Brief Comptable Transverse — Groupe Guinet · Odoo

> Source de vérité pour le projet "Compta" de Claude.
> Dernière mise à jour : 08/05/2026

---

## Instance Odoo

| Élément | Valeur |
|---|---|
| Instance | `guinet` |
| URL | https://guinet-group.odoo.com |
| Version | Odoo 19 |

---

## Sociétés gérées

| Société | company_id | SIREN | Activité | Fiche détaillée |
|---|---|---|---|---|
| Guinet Group (holding) | **1** | 983 391 079 | Holding · détient 100 % de GDG | [[Brief-Compta-GuinetGroup]] |
| Guinet Digital Group (ex-Globasoft) | **4** | 985 298 900 | ESN — services numériques, affacturage BPCE Factor | [[Brief-Comptable-Odoo]] |
| Le Petit Cerf | **7** | 929 808 921 | Restaurant / commerce | [[Brief-Compta-LePetitCerf]] |

> ⚠️ **Guinet Digital Group EST l'ancien Globasoft renommé** (même SIREN 985 298 900). Le **renommage légal date d'août 2025**. Tous les bordereaux affacturage BPCE Factor, le compte bancaire `512002 GLOBASOFT XX7328`, et la liasse fiscale 2024 (établie en 2025) portent encore le nom historique "Globasoft" — c'est normal, pas une erreur.

> ⚠️ **Filiation** : Guinet Group (holding, company_id=1, SAS) détient 100 % de Guinet Digital Group (ex-Globasoft, company_id=4, SARL). Tous les flux interco passent par 451 (groupe) côté GDG et doivent avoir une contrepartie miroir dans Guinet Group.

> ⚠️ **Statut Le Petit Cerf** dans la holding : non documenté dans la liasse Bepmale 2024 — Petit Cerf serait acquis ou créé après le 31/03/2024. À vérifier.

## Experts comptables externes

Le groupe utilise un **seul cabinet d'expertise comptable** qui opère sous deux marques :
- **Cabinet Super Compteur** (Toulouse) — marque commerciale
- **C.E.C. Marc BEPMALE & Associés** (72 rue Riquet, Toulouse) — entité juridique

→ C'est la **même société** d'expertise comptable. Bepmale et Super Compteur ne sont pas deux cabinets distincts mais deux noms du même prestataire. Cohérent avec leur présence simultanée sur la liasse fiscale GDG (Super Compteur en rédacteur, Bepmale en zone "conseil").

| Société | Logiciel utilisé | Rédacteur 1ère liasse |
|---|---|---|
| Guinet Group | SAGE Générations Experts | sous nom Bepmale |
| Guinet Digital Group | SAGE Générations Experts | sous nom Super Compteur |
| Le Petit Cerf | À préciser | À préciser |

### Sociétés présentes mais hors périmètre (ne pas toucher sauf instruction explicite)
| Société | company_id | Statut probable |
|---|---|---|
| Globasoft branche | 2 | Doublon de GDG ou ancien paramétrage (à clarifier) |
| Le Petit Cerf Branche | 3 | Doublon |
| Guinet Group - New | 8 | Doublon |
| Le Petit Cerf - Site internet | 9 | Doublon |
| Demain Thaïlande | 10 | À clarifier |

> 💡 La présence de ces sociétés "fantômes" est probablement la cause de **bugs multi-société** observés dans la compta GDG (ex : `tax_repartition_line` 566 d'une FAC GDG rattachée à Le Petit Cerf au lieu de GDG). À chaque saisie, vérifier la société active.

---

## Règles absolues (toutes sociétés)

1. **Toujours `dry_run=true` en premier** → afficher le résultat → attendre confirmation explicite.
2. **Ne jamais inventer ni calculer de montant** — tout doit être lu directement dans les documents ou Odoo.
3. **Toujours passer `company_id`** sur tous les appels RPC comptables (1, 4 ou 7 selon la société).
4. **Toutes les lectures et modifications Odoo passent exclusivement par MCP `odoo:*`** — ne jamais utiliser le navigateur pour lire ou écrire des données comptables.
5. **Ne jamais enchaîner dry_run + exécution dans le même message.**
6. **Afficher un tableau récapitulatif clair au dry_run** : lignes concernées, libellé, montant, ancien compte → nouveau compte.
7. **Jamais d'OD de reclassement** — pour corriger une imputation comptable erronée, modifier directement la ligne concernée via `update_record` sur `account.move.line` (changer `account_id` et/ou `partner_id`), même si l'écriture est posted. Ne pas passer d'écriture compensatoire dans le journal OD.
8. **Pour toute opération destructive ou structurante** (suppression d'écritures en masse, création de plan de comptes, OD d'à-nouveau), découper en phases distinctes, chacune avec son propre dry_run et sa propre confirmation. Ne jamais enchaîner plusieurs phases destructives dans une même série de tool calls.

---

## Contrainte technique Odoo 19

Le champ `company_id` n'existe plus sur `account.account` — il a été remplacé par `company_ids` (many2many). Ne jamais passer `company_id` directement dans un domain sur `account.account`. Utiliser plutôt le paramètre `company_id` de l'outil MCP qui l'injecte via le contexte RPC.

---

## Google Drive — Comptabilité Groupe

Dossier racine : **Comptabilité Groupe** (id: `1gYr7sYGc1FCA9quDAe_odf4tMzPlmaAy`)

| Société | Sous-dossier Drive | Compte MCP gdrive |
|---|---|---|
| Globasoft ESN | `Globasoft ESN/` | `globasoft` |
| Guinet Group | `Guinet Group/` | `guinet` |
| Guinet Digital Group | `Guinet Digital Group/` | `digital` |
| Le Petit Cerf | `Le Petit Cerf/` | `petit_cerf` |
| Transversal | `_Groupe/` | `groupe` |

**Authentification** : OAuth2, compte `guinetb@guinet-group.com` — partagé entre tous les comptes MCP gdrive.

### Raccourcis MCP gdrive (communs à chaque société)

`racine`, `"2025"`, `"2026"`, `2025_factures_clients`, `2025_factures_fourn`, `2025_releves_bancaires`, `2025_notes_de_frais`, `2025_declarations`, `2026_factures_clients`, `2026_factures_fourn`, `2026_releves_bancaires`, `2026_notes_de_frais`, `2026_declarations`, `juridique`, `social_2025`, `social_2026`, `social`.

---

## Notes Obsidian liées

- **Fiche Guinet Group** : `04-Comptabilité/Brief-Compta-GuinetGroup.md`
- **Fiche Guinet Digital Group** : `04-Comptabilité/Brief-Comptable-Odoo.md` (fiche historique, la plus complète)
- **Fiche Le Petit Cerf** : `04-Comptabilité/Brief-Compta-LePetitCerf.md`
- **Plan de comptes perso** : `04-Comptabilite/Plan-Comptes-Perso-Odoo-v2.md` (instance `perso`, hors périmètre de ce brief)
