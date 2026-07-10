---
tags: ["comptabilité", "odoo", "brief", "transverse"]
created: 2026-05-08
---

---
tags: ["comptabilité", "odoo", "brief", "transverse"]
created: 2026-05-08
updated: 2026-05-08
---

# Brief Comptable Transverse — Groupe Guinet · Odoo

> Source de vérité pour le projet « Compta » de Claude.

---

## Instances Odoo

| Instance | URL | Version | Usage |
|---|---|---|---|
| `guinet` | https://guinet-group.odoo.com | Odoo 19 | Comptabilité consolidée groupe (Guinet Group + GDG + Le Petit Cerf) |
| `globasoft` | https://globasoft.odoo.com | Odoo 17 | Comptabilité opérationnelle Globasoft ESN — cabinet VP CONSEIL |

---

## Sociétés du groupe

| Société | company_id | SIREN | Détention | Activité | Fiche |
|---|---|---|---|---|---|
| Guinet Group (holding) | **1** | 983 391 079 | — | Holding | [[Brief-Compta-GuinetGroup]] |
| Guinet Digital Group | **4** | 985 298 900 | 100 % Guinet Group | ESN — services numériques, affacturage BPCE Factor | [[Brief-Compta-GDG]] |
| Le Petit Cerf | **7** | 929 808 921 | Guinet Group | Restaurant / commerce | [[Brief-Compta-LePetitCerf]] |
| Globasoft ESN | hors périmètre `guinet` | — | **50 % Guinet Group + 50 % ZM Consulting** | ESN — instance `globasoft` | [[Brief-Compta-Globasoft]] |

> ⚠️ **NE PAS CONFONDRE** :
> - **Guinet Digital Group (GDG)** = anciennement appelée Globasoft, renommée en août 2025. SIREN 985 298 900. 100 % Guinet Group. Instance `guinet`, company_id=4.
> - **Globasoft ESN** = société DISTINCTE, toujours nommée Globasoft. JV 50/50 avec ZM Consulting. Instance `globasoft` (globasoft.odoo.com). Hors périmètre consolidé `guinet`.

### Filiation
- Guinet Group (SAS, holding) détient **100 %** de GDG (SARL). Tous les flux interco passent par 451 (groupe) côté GDG et doivent avoir une contrepartie miroir côté GG.
- Guinet Group détient **50 %** de Globasoft ESN (co-détenu avec ZM Consulting). Voir [[Brief-Compta-Globasoft]].
- **Le Petit Cerf** : non documenté dans la liasse Bepmale Guinet Group 2024 → probablement acquis ou créé après le 31/03/2024. À confirmer.

### Sociétés fantômes Odoo (hors périmètre)

| company_id | Nom | Statut |
|---|---|---|
| 2 | Globasoft branche | Doublon de GDG / ancien paramétrage |
| 3 | Le Petit Cerf Branche | Doublon |
| 8 | Guinet Group - New | Doublon |
| 9 | Le Petit Cerf - Site internet | Doublon |
| 10 | Demain Thaïlande | À clarifier |

> 💡 Ces sociétés fantômes sont probablement à l'origine de bugs multi-société observés sur GDG (par ex. `tax_repartition_line` 566 d'une FAC GDG rattachée à Le Petit Cerf). Vérifier la société active à chaque saisie.

---

## Expert comptable externe

Le groupe utilise **un seul cabinet** opérant sous **deux marques** :

| Marque | Adresse / contact |
|---|---|
| C.E.C. Marc BEPMALE & Associés (entité juridique) | 72 rue Riquet Bâtiment A, 31000 Toulouse · 05 62 27 07 43 |
| Cabinet Super Compteur (marque commerciale) | Toulouse |

| Société | Logiciel | 1ère liasse fiscale |
|---|---|---|
| Guinet Group | SAGE Générations Experts | rédigée sous le nom Bepmale |
| Guinet Digital Group | SAGE Générations Experts | rédigée sous le nom Super Compteur |
| Le Petit Cerf | à préciser | à préciser |

---

## Règles absolues (toutes sociétés)

1. **Toujours `dry_run=true` en premier** → afficher le résultat → attendre confirmation explicite.
2. **Ne jamais inventer ni calculer un montant** — tout vient des documents ou d'Odoo.
3. **Toujours passer `company_id`** sur tous les appels RPC comptables (1, 4 ou 7).
4. **Lectures et écritures Odoo via MCP `odoo:*` exclusivement** — pas de navigateur.
5. **Ne jamais enchaîner dry_run + exécution dans le même message.**
6. **Tableau récap clair au dry_run** : lignes concernées, libellé, montant, ancien compte → nouveau compte.
7. **Jamais d'OD de reclassement** — pour corriger une imputation, modifier directement la ligne via `update_record` sur `account.move.line` (changer `account_id` et/ou `partner_id`), même si posted. Pas d'écriture compensatoire dans le journal OD.
8. **Opérations destructives ou structurantes** (suppression en masse, création de plan de comptes, OD d'à-nouveau) : découper en phases distinctes, chacune avec son propre dry_run et sa propre confirmation. Ne pas enchaîner plusieurs phases destructives dans une même série de tool calls.
9. **Mises à jour des notes Obsidian** : utiliser `edit_note` ou `replace_section` plutôt que des `append_to_note` successifs. Si une note s'est dégradée par accumulation, l'archiver puis la recréer proprement avec `archive_note` + `create_note`.

---

## ⚠️ Règle de groupe — comptes 451 vs 455 (NE JAMAIS MÉLANGER)

> **Erreur fréquente détectée le 10/05/2026 dans GDG** : 38 virements GDG → Guinet Group SAS (33 335 €) imputés à tort sur un compte 455002 « Retrait perso GUINET GROUP SARL », alors qu'ils relèvent du compte **451000 (interco)**. Même type d'erreur potentielle dans Le Petit Cerf (45500200).

### Distinction stricte

| Type de flux | Compte | Tiers | Justification |
|---|---|---|---|
| **Filiale ↔ Holding** (Guinet Group SAS, personne morale, SIREN 983 391 079) | **451 (Group)** | `partner_id = Guinet Group` | Flux **inter-sociétés**, doit avoir une contrepartie miroir côté GG sur compte 451100 (C/C GDG) ou équivalent. Apparaît au bilan en créance/dette de groupe. |
| **Société ↔ Benoit Guinet** (personne physique, gérant/associé) | **455010** ou **45500100** (selon société) | `partner_id = Benoit Guinet` | Compte courant d'associé personne physique. Apport ou retrait de l'associé pour usage privé/rémunération. |

### Test simple à appliquer en saisie

> Le bénéficiaire ou l'émetteur est-il une **personne morale** (SIREN, SAS/SARL) ou une **personne physique** (Benoit) ?
>
> - **Personne morale dans le périmètre** (Guinet Group SAS, GDG SARL, Le Petit Cerf, Globasoft branche…) → **451** (interco)
> - **Personne physique** (Benoit Guinet, Kwang Wis Guinet…) → **455** (C/C associé)
>
> ⚠️ Le libellé du compte ne fait pas foi — un compte « Retrait perso GUINET GROUP SARL » est mal nommé : "GUINET GROUP SARL" est une personne morale, donc 451, pas 455.

### Mapping par société

| Société | 451 (interco) | 455 (C/C personne physique) |
|---|---|---|
| **Guinet Group** (id=1) | 451100 (id 3179) — C/C GDG | 455100 (id 3164) — C/C Benoit |
| **GDG** (id=4) | 451000 (id 1215) — Group | 455010 (id 3172) — C/C Benoit |
| **Le Petit Cerf** (id=7) | 451000 (id 1972) — Group | 45500100 (id 3127) — Benoit |

> Pour **Le Petit Cerf**, 45500200 (id 3128) « Retrait pour GUINET GROUP SARL » suit la même mauvaise convention que 455002 GDG → à reclasser en 451000 idéalement, ou à migrer puis archiver.

### Sources et nuances (vérifiées 10/05/2026)

> ⚠️ La règle « SIREN → 451, nom → 455 » est une **convention professionnelle**, pas une obligation PCG stricte.

**Ce que disent les textes officiels** :

- **PCG** ([pcg.fr](https://www.pcg.fr/classe-45-groupe-et-associes-du-plan-comptable.php)) :
  - 451 : « fonds avancés ou reçus avec les **sociétés du groupe** »
  - 455 : « fonds mis ou laissés temporairement à disposition par les **associés** » — sans préciser personne physique/morale
- **Art. L223-21 C. com.** ([Légifrance](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006223124)) : interdit le C/C débiteur **uniquement** aux gérants/associés **personnes physiques** (et conjoints/ascendants/descendants). Un associé personne morale **peut** avoir un C/C débiteur.
- **Art. L511-7 CMF** ([Légifrance](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049423718)) : dérogation au monopole bancaire pour les opérations de trésorerie entre sociétés liées en capital avec contrôle effectif. Convention écrite + intérêts requis sinon risque de distribution déguisée. **Le groupe Guinet a une convention écrite** ✅.

**Ce qui est un vrai risque** :
- Absence de convention de trésorerie écrite → distribution déguisée requalifiée par le fisc
- C/C débiteur d'une personne physique → abus de biens sociaux (L223-21)

**Ce qui n'est PAS un risque légal** (mais reste une mauvaise pratique) :
- Mettre un flux holding-filiale en 455 au lieu de 451 → simple défaut de lisibilité bilan + complication consolidation, **pas une infraction**

**Pourquoi on reclasse quand même** :
1. Lisibilité bilan pour banquier/EC/fisc
2. Élimination correcte en consolidation (451 oui, 455 non)
3. Doctrine professionnelle des EC
4. Cohérence avec la convention de trésorerie en place

> 📌 Le reclassement 455002 → 451000 est donc une **amélioration qualitative**, pas une correction d'erreur légale.

---

## Contrainte technique Odoo 19

Sur `account.account`, le champ `company_id` n'existe plus — remplacé par `company_ids` (many2many). Ne jamais filtrer par `company_id` directement dans un domain sur ce modèle. Utiliser le paramètre `company_id` de l'outil MCP qui l'injecte via le contexte RPC.

---

## Google Drive — Comptabilité Groupe

Dossier racine : **Comptabilité Groupe** (id `1gYr7sYGc1FCA9quDAe_odf4tMzPlmaAy`)

| Société | Sous-dossier Drive | Compte MCP gdrive |
|---|---|---|
| Globasoft ESN | `Globasoft ESN/` | `globasoft` |
| Guinet Group | `Guinet Group/` | `guinet` |
| Guinet Digital Group | `Guinet Digital Group/` | `digital` |
| Le Petit Cerf | `Le Petit Cerf/` | `petit_cerf` |
| Transversal | `_Groupe/` | `groupe` |

Authentification : OAuth2, compte `guinetb@guinet-group.com` — partagé entre tous les comptes MCP gdrive.

### Raccourcis MCP gdrive (communs)

`racine`, `"2025"`, `"2026"`, `2025_factures_clients`, `2025_factures_fourn`, `2025_releves_bancaires`, `2025_notes_de_frais`, `2025_declarations`, `2026_factures_clients`, `2026_factures_fourn`, `2026_releves_bancaires`, `2026_notes_de_frais`, `2026_declarations`, `juridique`, `social_2025`, `social_2026`, `social`.

---

## Notes Obsidian liées

- Fiche Guinet Group : [[Brief-Compta-GuinetGroup]]
- Fiche Guinet Digital Group : [[Brief-Comptable-Odoo]]
- Fiche Le Petit Cerf : [[Brief-Compta-LePetitCerf]]
- Plan de comptes perso : `04-Comptabilite/Plan-Comptes-Perso-Odoo-v2.md` (instance `perso`, hors périmètre)
