---
tags: ["methodologie", "plan-classement", "livrabilite", "cloture-projet"]
created: 2026-05-17
---

# 9. Livrabilité et clôture projet

> Peut-on extraire sans risque d'erreur le périmètre livrable, à tout moment ?

## Principe

Sur un projet IT, la **livraison documentaire** est un cas d'usage structurant : à la fin d'une phase ou du projet, on doit pouvoir extraire **l'ensemble exact** des documents destinés au client, **sans rien oublier** et **sans rien inclure de superflu**.

Un plan de classement peut être parfaitement MECE, parfaitement métier, parfaitement gouverné — et **échouer** sur la livraison si les contenus livrables et internes sont mélangés sans frontière structurelle.

Cet angle évalue la capacité du plan à **distinguer visuellement et opérationnellement** ce qui est livrable de ce qui ne l'est pas.

## Pourquoi c'est critique sur un projet IT

- Les projets IT produisent **massivement des artefacts de travail** (brouillons, supports de réunion, anomalies, échanges) qui ne sont **pas destinés au client**.
- Ils produisent en parallèle des **artefacts de référence** (specs, règles, mapping, exploitation) qui **doivent** être livrés.
- Un mélange des deux dans les mêmes dossiers oblige à un **tri manuel à chaque livraison** → risque d'oubli + risque d'inclusion parasite.
- La livraison documentaire fait souvent partie du **contrat** (CCTP, devis, recette) : un défaut de livraison = un défaut contractuel.
- En fin de projet, la livraison est souvent **massive et urgente** : aucun moment pour faire un tri minutieux.

## Le test ultime

Une question simple : **« Si le client demande aujourd'hui toute la doc du projet, combien de minutes/heures pour préparer la livraison ? »**

| Temps de préparation | Score implicite |
|---|---|
| Quelques secondes (un `cp -r` ciblé) | 3 — livrabilité structurelle |
| Quelques minutes (filtre par métadonnée scripté) | 2 — livrabilité outillée |
| Quelques heures (tri manuel guidé par un index) | 1 — livrabilité documentée mais fragile |
| Plus d'une journée ou risque d'erreur élevé | 0 — livrabilité non maîtrisée |

## Deux familles d'organisation

### École A — Structure par fonction métier + cycle de vie en attribut
Le plan reflète l'activité métier. La livrabilité repose sur **un attribut** (frontmatter `cycle_vie`, `livrable_client`...). La livraison se fait par filtre/script.

✅ Cohérence métier maximale
❌ Livrabilité non visuelle, dépend de la rigueur du frontmatter

### École B — Structure par destination
Le niveau 1 du plan distingue `livrable/` vs `interne/` vs `archives/`. La livraison = une branche entière.

✅ Livrabilité structurelle, lisible à l'œil
❌ Cohérence métier éclatée (la doc d'une même source peut être dans deux branches)

### École hybride (recommandée pour projets IT structurés)

**Structure par fonction métier** au niveau 1, mais **sous-dossier `_livrable/` dédié** dans chaque branche mixte.

```
05-restitutions/recette-mep2/
├── _livrable/                     ← pérenne, contenu destiné au client
│   ├── MAPPING_LIVRABLE_FACTURES.md
│   ├── REGLES_IMPLEMENTEES_MEP2.md
│   ├── EXPLOITATION_MEP2.md
│   └── RAPPORT_RECETTE_MEP2.md
├── anomalies/                     ← transition, interne
├── evolutions/                    ← transition, interne
├── BROUILLON_MAIL_*               ← transition, interne
└── SUPPORT_REUNION_*              ← transition, interne
```

Avantages :
- Conserve la cohérence métier
- Rend la livrabilité visuelle (`_livrable/` est visible au premier coup d'œil)
- Force la discipline : on ne range pas n'importe quoi dans `_livrable/`
- La livraison devient une opération mécanique : agréger tous les `_livrable/` du vault

## L'index livrable global

Un dispositif clé : une note unique (ex : `00-gouvernance/index-livrables.md`) qui **liste exhaustivement** tous les artefacts livrables du projet.

### Rôle de l'index

- **Vérification d'exhaustivité** : "ai-je oublié quelque chose ?"
- **Vérification d'exclusivité** : "ai-je inclus quelque chose qui ne devrait pas l'être ?"
- **Référentiel partagé** : sponsors, équipe et client savent ce qui est livré
- **Outil de suivi** : statut de chaque livrable (à produire / en cours / livré)

### Structure type

```markdown
# Index des livrables — Projet X

## Livrables par catégorie

### Documentation d'architecture
- [x] Document d'Architecture Technique (DAT)
- [x] Cartographie des flux
- [ ] Vue d'ensemble grand public

### Référentiel métier
- [x] Glossaire métier
- [x] Règles de gestion (×N)
- [x] Indicateurs KPI (×M)

### Spécifications techniques
- [x] Fiches sources (×P)
- [x] Fiches tables silver (×Q)

### Documents par MEP
- MEP 1 (Imputations)
  - [x] MAPPING_LIVRABLE_IMPUTATIONS
  - [x] REGLES_IMPLEMENTEES_MEP1
  - [x] EXPLOITATION_MEP1
  - [x] RAPPORT_RECETTE_MEP1
- MEP 2 (Factures)
  - [x] MAPPING_LIVRABLE_FACTURES
  - [ ] REGLES_IMPLEMENTEES_MEP2 (en cours)
  - ...
```

L'index doit être maintenu **en parallèle de la production** : chaque nouveau livrable ajouté est inscrit, chaque livrable obsolète marqué.

## Questions à poser

- [ ] Le plan distingue-t-il **structurellement** (par dossier) les contenus livrables des contenus internes ?
- [ ] À défaut, existe-t-il un **attribut frontmatter** systématique (`livrable_client`, `cycle_vie`) qui le distingue ?
- [ ] Existe-t-il un **index livrable global** maintenu à jour ?
- [ ] La livraison peut-elle être préparée en **< 5 minutes** par une personne autre que le propriétaire ?
- [ ] Existe-t-il un **script ou une procédure** automatisée pour préparer la livraison ?
- [ ] Les **livrables par phase** sont-ils clairement identifiés (par MEP, par sprint, par jalon) ?
- [ ] Le plan distingue-t-il **livrable récurrent** (mis à jour à chaque MEP) de **livrable one-shot** (produit une fois) ?
- [ ] Existe-t-il un **historique des livraisons** réalisées (qui a reçu quoi, quand) ?
- [ ] Les livrables ont-ils une **version explicite** (vis-à-vis du client) ?

## Signaux d'alerte 🚩

- Aucun moyen rapide d'isoler les livrables → tri manuel à chaque livraison
- Présence de brouillons / supports de réunion / anomalies internes dans les mêmes dossiers que les specs livrables
- Pas d'index livrable global → impossible de vérifier l'exhaustivité
- "On va voir au moment de la livraison" — réponse type d'un projet sans stratégie de livrabilité
- Livraisons précédentes incohérentes (le client n'a pas reçu deux fois les mêmes choses)
- Fichiers internes envoyés par erreur au client (et inversement)
- Pas de version explicite des livrables côté client (versions internes ≠ versions livrées)

## Anti-patterns

### ❌ Le dossier mixte sans frontière
Un dossier `05-restitutions/recette-mep2/` qui contient à la fois `MAPPING_LIVRABLE.md`, `BROUILLON_MAIL.md`, `anomalies/`, `SUPPORT_REUNION.md`. Toute livraison nécessite un tri manuel.

### ❌ Le frontmatter inégalement appliqué
Le projet a un champ `cycle_vie` dans le frontmatter, mais il n'est rempli que sur 60% des fiches. Impossible de fiabiliser un filtre.

### ❌ Le dossier `livrables/` qui dérive
Au début c'était propre. Avec le temps, des choses non livrables s'y sont glissées "parce que c'est plus pratique". La discipline cède.

### ❌ Le livrable produit ad-hoc
Aucune cartographie a priori. À chaque demande client, on improvise un périmètre. Risque d'incohérence d'une livraison à l'autre.

## Bonnes pratiques

### ✅ Dossier `_livrable/` dans chaque branche mixte
Préfixe `_` pour remonter en tête de liste alphabétique. Force la discipline.

### ✅ Index livrable global maintenu vivant
À mettre à jour à chaque création d'un nouveau livrable ; vérifié à chaque livraison.

### ✅ Convention de nommage explicite des livrables
Préfixes systématiques : `LIVR-`, `LIV-`, `_LIVRABLE_`... peu importe, mais une convention.

### ✅ Script de livraison
Même rudimentaire (un `find` qui ramasse tous les `_livrable/` et zippe). Le simple fait d'avoir un script formalise le périmètre.

### ✅ Différencier livrable produit (régénérable) et livrable édité
Un livrable régénérable depuis le pipeline n'a pas le même cycle de vie qu'un livrable édité manuellement.

## Cas concrets à challenger

**Projet ERP avec livraisons par sprint**
- Combien de temps pour préparer la livraison d'un sprint ?
- Y a-t-il une liste de référence des livrables par sprint ?
- Les spécifications sont-elles dans les mêmes dossiers que les comptes-rendus de réunion ?

**Projet DWH avec MEP successives**
- Comment isoler les livrables d'une MEP des artefacts internes (anomalies, briefs) ?
- Le client reçoit-il les mêmes types de documents à chaque MEP ? Si oui, structuration à automatiser.

**Projet de migration avec livraison unique en fin de projet**
- Tout est-il prêt à 100% le jour J ?
- Y a-t-il un dossier `_livrable/` rempli au fur et à mesure, ou tout est mélangé jusqu'à la fin ?

## Articulation avec les autres angles

- **[[01-Logique-structurante]]** : la structure métier doit permettre d'accueillir des sous-dossiers `_livrable/` sans casser la cohérence
- **[[03-Exhaustivite-exclusivite]]** : la livrabilité est un cas particulier de MECE — chaque livrable doit avoir une place unique, l'ensemble des livrables doit être exhaustif
- **[[04-Calendrier-conservation-DUA]]** : le cycle de vie 🔵 livrable est traité ici ; les autres cycles (pérenne, transition, archive) là-bas
- **[[06-Metadonnees]]** : un champ `livrable_client` au frontmatter complète la structure
- **[[07-Adequation-usages]]** : la livraison est un usage à part entière, à tester comme la recherche

## Référence

- ISO 15489-1:2016, §9.6 (Sort final et restitution)
- Bonnes pratiques de management de projet (PMBOK, PRINCE2) — phase de clôture
- Pratiques agiles : Definition of Done incluant la documentation livrable
