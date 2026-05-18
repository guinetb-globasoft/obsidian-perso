---
tags: ["methodologie", "plan-classement", "records-management", "index", "iso-15489"]
created: 2026-05-17
---

# Méthodologie d'évaluation des plans de classement

> Référentiel interne pour challenger les plans de classement et les documents produits sur nos projets informatiques.

## Objectif

Disposer d'une grille d'analyse réutilisable pour juger :
- **La pertinence** d'un plan de classement (structure, logique)
- **La position** d'un document dans le plan (au bon endroit ?)
- **La durabilité** du dispositif (résistance dans le temps)
- **La conformité** aux normes et obligations

## Les 10 angles d'attaque

| # | Angle | Question clé |
|---|-------|--------------|
| 1 | [[01-Logique-structurante]] | Sur quoi repose la structure du plan ? |
| 2 | [[02-Profondeur-hierarchie]] | Le plan est-il navigable ? |
| 3 | [[03-Exhaustivite-exclusivite]] | Chaque doc a-t-il une et une seule place ? |
| 4 | [[04-Calendrier-conservation-DUA]] | Combien de temps, et après ? |
| 5 | [[05-Stabilite-evolutivite]] | Peut-on évoluer sans tout casser ? |
| 6 | [[06-Metadonnees]] | Que sait-on de chaque document ? |
| 7 | [[07-Adequation-usages]] | Les utilisateurs s'y retrouvent-ils ? |
| 8 | [[08-Conformite-reglementaire]] | Sommes-nous en règle ? |
| 9 | [[09-Livrabilite-cloture-projet]] | Peut-on extraire sans risque le périmètre livrable ? |
| 10 | [[10-Completude-structurelle]] | Tous les artefacts transverses obligatoires sont-ils présents ? |

## Référentiels normatifs

Voir [[11-Normes-references]] pour le détail.

Normes principales mobilisées :
- **ISO 15489-1:2016** — Records management (norme mère)
- **ISO 23081** — Métadonnées
- **ISO 16175** — Exigences fonctionnelles environnement électronique
- **ISO 30300/30301** — Système de management
- **MoReq2010** — Référentiel européen
- **NF Z42-013 / ISO 14641** — Archivage électronique
- **R2GA** — Référentiel SIAF (secteur public FR)
- **PMBOK / PRINCE2** — Management de projet (livrabilité, clôture)
- **ADR (Nygard 2011) / Keep a Changelog** — Pratiques IT (complétude)

## Grille de notation synthétique

Pour chaque projet évalué, scorer de 0 à 3 sur chaque angle :
- **0** = absent ou bloquant
- **1** = présent mais insuffisant
- **2** = conforme aux attentes
- **3** = exemplaire

| Angle | Score | Constat | Action corrective |
|-------|-------|---------|-------------------|
| 1. Logique structurante | | | |
| 2. Profondeur | | | |
| 3. Exhaustivité/exclusivité | | | |
| 4. DUA / sort final | | | |
| 5. Stabilité/évolutivité | | | |
| 6. Métadonnées | | | |
| 7. Adéquation usages | | | |
| 8. Conformité | | | |
| 9. Livrabilité / clôture | | | |
| 10. Complétude structurelle | | | |
| **Total / 30** | | | |

## Usage

1. À la **revue initiale** d'un projet : passer chaque angle en revue
2. En cours de projet : challenger les nouveaux documents ajoutés
3. À la **clôture** : vérifier que le plan reste cohérent et exploitable
4. Lors d'**audits internes** : utiliser comme grille d'audit

## Ressources complémentaires

- 📋 [[Template-Audit-Projet]] — Template à dupliquer dans chaque projet pour conduire un audit
- 📖 [[11-Normes-references]] — Catalogue complet des normes mobilisables
- 📚 [[12-Glossaire]] — Vocabulaire commun (DUA, MECE, SAE, GED, R2GA, ADR, livrabilité, complétude...)

## Audits réalisés (cas tests)

| Date | Projet | Score | Apprentissages méthodo |
|---|---|---|---|
| 2026-05-17 | DWH Aerotec (vault `dwh`) | 18/27 → re-scoré /30 | Cycle de vie comme dimension orthogonale · cohérence doc↔code · versionning sémantique du plan · nuances profondeur · création angle 9 Livrabilité · **création angle 10 Complétude structurelle** |
