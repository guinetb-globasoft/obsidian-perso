---
tags: ["elevo", "objectifs", "mapping", "GA", "import"]
projet: GA - API Nibelis
type: mapping-implémenté
cible: Elevo — Importation en masse des objectifs personnels
source: Liste des objectifs (export campagne entretien annuel)
created: 2026-07-24
updated: 2026-07-24
---

# Import objectifs Elevo — Mapping

> Transformation de la **liste des objectifs** (export campagne « Entretien annuel d'évaluation Cadres / Etams 2025 ») vers le **template Elevo d'import en masse des objectifs personnels**.
> ⚠️ **Aucune donnée inventée** : les champs absents de la source (`due_date`, `completion`, KPIs) sont laissés **vides**.

## Fichiers

| Rôle | Fichier |
|---|---|
| **Source** | `Downloads/Elevo-Objectifs/ListeEtatGeneriqueCJaubertcelieGASAS20260710105542.xlsx` (onglet « Feuille 1 », en-tête ligne 2) |
| **Template cible** | `Downloads/Elevo-Objectifs/Elevo - FR Importation en masse des objectifs personnels.xlsx` (onglet « Objectifs (FR) », noms machine ligne 4) |
| **Sortie générée** | `Downloads/Elevo-Objectifs/Elevo - Objectifs personnels (à importer).xlsx` |

## Volume

- **1469 objectifs** / **404 collaborateurs** (403 matricules).
- Campagne unique : *Entretien annuel d'évaluation Cadres / Etams 2025* ; tous « Futurs objectifs individuels ».
- **Pondération = 0.0 partout** → onglet **simple « Objectifs (FR) »** (pas la variante « avec poids »).

## Mapping des colonnes

Cible = onglet « Objectifs (FR) », **20 colonnes machine** (`login` → `kpi_3.current_value`). Seules 3 sont alimentées ; le reste est vide (non présent dans la source).

| Colonne Elevo | Source (liste) | Transformation | Obligatoire |
|---|---|---|---|
| `login` | `Matricule` → **email pro** | résolution `matricule` → `mail_conge` (fallback `mail_01`) via `fiches_all.json` ; **fallback = matricule** si non résolu | ✅ |
| `title` | `Libellé` | `str().strip()` | ✅ |
| `description` | `Description` + `Mesure` | `Description`, puis « `Mesure : …` » ajouté en dessous (`\n\n`) si `Mesure` présente | — |
| `due_date` | — | **vide** (aucune échéance dans la source) | — |
| `completion` | — | **vide** (objectifs « Futurs », non chiffrés) | — |
| `kpi_1..3.*` | — | **vide** (pas de KPI chiffré dans la source) | — |

### Décisions (validées)
- **`login`** = email pro (`mail_conge`) sinon matricule → **1338** via email, **131** via matricule (fallback).
- **`Mesure`** = ajoutée à la **description** (pas en KPI), pour ne pas créer de KPI à moitié vide.

### Colonnes source NON reprises
`Campagne`, `Établissement`, `Département`, `Service`, `Objectifs`, `Origine`, `Pondération` (0.0), `Note collaborateur`, `Commentaire collaborateur`, `Note Responsable`, `Commentaire Responsable`, `Famille d'objectifs` — hors périmètre du template Elevo (objectif = login/titre/description/échéance/complétion/KPI).

## Points de vigilance

- **131 objectifs** ont `login` = matricule (collaborateur sans email pro résolu, dont **25 matricules absents** de `fiches_all.json` = probablement sortis / hors sociétés en cache). ➡️ ces lignes ne s'importeront dans Elevo que si l'utilisateur existe avec cet identifiant.
- **1 objectif sans `Libellé`** → `title` vide (non inventé). Elevo **rejettera** cette ligne (titre obligatoire) — à compléter à la main si besoin.
- **`due_date` / `completion` vides** : volontaire (données absentes). À renseigner par RH si l'échéance de campagne doit être posée.
- Avant import Elevo : le template officiel demande de **supprimer les lignes/colonnes jaunes** (documentation) — le fichier de sortie ne contient déjà **que** la ligne d'en-tête machine + les données.

## Génération (technique)
À la génération du `.xlsx` (openpyxl), **2 assainissements obligatoires** sinon Excel affiche « problème dans le contenu » :
1. **Caractères de contrôle illégaux** (XML) dans les textes libres → retirés via `ILLEGAL_CHARACTERS_RE`.
2. **Textes commençant par `=`** (ex. une description « => … ») → openpyxl les écrit en **formule** invalide. Correctif : repasser ces cellules en `data_type="s"` (texte) après écriture, **sans modifier le contenu**. (`-`, `+`, `@` en tête ne posent pas problème.)

## Procédure d'import (doc officielle Elevo)

> Source : *Importer des objectifs en cours au déploiement d'Elevo* (doc Elevo/Assessio) — `Downloads/Elevo-Objectifs/doc/`.

- **Canal** : remplir le modèle (1 objectif/ligne) puis **l'envoyer à `support@elevo.io`** (import réalisé par le support, pas de self-service).
- **Conditions** : être en **phase de déploiement** Elevo + avoir **≥ 100 objectifs** à importer (ici **1469** ✅).
- **Période en cours uniquement** : cet import ne prend **pas** les objectifs de périodes précédentes (N-1). Notre source = campagne « Futurs objectifs 2025 » = période en cours ✅.
- **KPI** : jusqu'à **20 KPI** par objectif (on n'en renseigne aucun, faute de données chiffrées).

### Confirmation du mapping par la doc
| Clé interne | Statut | Notre source |
|---|---|---|
| `login` | **[obligatoire]** email **ou identifiant** | email pro, fallback matricule ✅ (les deux sont acceptés) |
| `title` | **[obligatoire]** intitulé | `Libellé` ✅ |
| `description` | [optionnel] | `Description` (+ `Mesure`) ✅ |
| `due_date` | [optionnel] ISO 8601 | vide (absent source) ✅ |
| `completion` | [optionnel] nombre | vide ✅ |
| `kpi_*` | [optionnel] | vide ✅ |

## Liens
- [[05-Import salariés Elevo - Mapping champs]] — import des utilisateurs (prérequis : les `login` doivent exister)
- [[02-Mapping-Elevo-Nibelis]]
