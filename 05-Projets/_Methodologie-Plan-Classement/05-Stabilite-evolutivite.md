---
tags: ["methodologie", "plan-classement", "stabilite", "evolutivite", "gouvernance"]
created: 2026-05-17
---

# 5. Stabilité et évolutivité

> Peut-on faire évoluer le plan sans tout casser ?

## Principe

Un bon plan doit être à la fois :
- **Stable** : ne pas changer tous les 6 mois, sinon les utilisateurs ne suivent pas
- **Évolutif** : pouvoir intégrer de nouvelles activités sans refonte totale

C'est un équilibre. Une **codification intelligente** est la clé.

## Pourquoi c'est critique sur un projet IT ?

- Les SI évoluent constamment (nouveaux modules, nouvelles fonctionnalités)
- Les périmètres bougent (reprise d'historique, fusion de projets)
- Les liens / URLs / références cassent si on renomme les chemins
- Les utilisateurs perdent leurs repères → désaffection du plan

## Bonnes pratiques de codification

### Codification numérique avec marges

```
01-Cadrage
02-Conception
03-Realisation
04-Recette
05-Mise-en-production
06-Exploitation
99-Archives
```

Laisser des **trous** dans la numérotation (`05`, puis `10`, puis `15`...) pour insérer plus tard sans tout renuméroter.

### Préfixes sémantiques stables

Les libellés derrière les numéros doivent être **génériques et durables** :
- ✅ `02-Conception` (fonction stable)
- ❌ `02-Specs-equipe-Dupont-2024` (instable)

### Séparer le "stable" du "volatil"

```
01-Cadrage/           ← stable (la fonction)
  └── Projet-X/       ← volatil (instance projet)
```

## Questions à poser

- [ ] Le plan a-t-il une **règle de codification documentée** ?
- [ ] La codification permet-elle l'insertion sans renumérotation ?
- [ ] Y a-t-il une **procédure d'évolution** du plan (qui décide ? comment ?) ?
- [ ] Le plan a-t-il déjà évolué ? Comment cela s'est-il passé ?
- [ ] Les libellés sont-ils **génériques** (résistants au temps) ou **datés** ?
- [ ] Existe-t-il un **historique des versions** du plan ?
- [ ] Y a-t-il un **propriétaire** identifié du plan (qui le maintient) ?

## Signaux d'alerte 🚩

- Numérotation contiguë sans marge (01, 02, 03, 04...)
- Libellés contenant des noms propres, dates, versions logicielles
- Aucune gouvernance du plan (personne ne décide)
- Évolutions sauvages : chacun crée ses dossiers
- Branches "anciennes" / "nouvelles" → témoignent d'une refonte ratée
- Le plan n'a jamais évolué en 5 ans (peut être un signe de sclérose, ou que personne ne le gouverne)

## Anti-patterns à éviter

### ❌ Dater les niveaux hauts
```
2023-Projets/
2024-Projets/
2025-Projets/
```
→ Préférer un classement par activité, et dater au niveau du dossier opérationnel.

### ❌ Versionner dans la structure
```
01-Specifications-v1/
01-Specifications-v2/
```
→ Le versioning se fait au niveau du fichier ou via une GED.

### ❌ Inclure des noms d'outils
```
03-Jira-Tickets/
04-Confluence-Wiki/
```
→ Les outils changent (Jira → Linear, etc.). Préférer "03-Tickets-incidents".

## Gouvernance du plan

Mettre en place :
- **Un propriétaire** (souvent : archiviste, RSSI ou chef de projet pour un projet)
- **Un comité de revue** annuel
- **Une procédure** d'ajout / suppression de catégorie
- **Un journal des évolutions** (changelog du plan)

## Cas concrets à challenger

**Plan d'un projet ERP**
- En cas d'ajout d'un nouveau module métier l'année prochaine, où va-t-il ?
- Si on change d'éditeur ERP dans 3 ans, le plan tient-il ?

**Plan documentaire DWH**
- Les noms de pipelines / tables apparaissent dans la structure ?
- Que se passe-t-il quand un pipeline est renommé / refondu ?

## Lien avec les autres angles

- La stabilité dépend d'une bonne [[01-Logique-structurante|logique structurante]] (les fonctions sont stables)
- L'évolutivité s'appuie sur une [[02-Profondeur-hierarchie|profondeur maîtrisée]]
- Une bonne gouvernance favorise l'[[07-Adequation-usages|adoption durable]]

## 🔄 Versionning sémantique du plan lui-même (enrichissement issu de l'audit DWH)

> Pratique avancée observée sur l'audit DWH Aerotec : appliquer le **versionning sémantique** non seulement aux fiches, mais au **plan de classement lui-même**.

### Le principe

Le plan de classement porte dans son frontmatter une **version semver** (`MAJEURE.MINEURE.PATCH`) et un **historique daté** des évolutions.

```yaml
---
titre: Plan de classement du projet X
version: 1.2.0
date_creation: 2026-01-15
date_revue: 2026-05-16
proprietaire: <nom>
statut: actif
---
```

Et en bas du document :

```markdown
## Historique

| Date | Version | Changement | Auteur |
|---|---|---|---|
| 2026-01-15 | 1.0.0 | Création initiale | ... |
| 2026-03-22 | 1.1.0 | Ajout dossier X, clarification ambiguïté Y | ... |
| 2026-05-16 | 1.2.0 | Reclassification Z suite retour utilisateur | ... |
```

### Règles d'incrément (adaptées au plan)

- **Patch** (1.0.0 → 1.0.1) : reformulation, typo, lien cassé. Aucun impact sur l'usage.
- **Mineure** (1.0.0 → 1.1.0) : ajout de dossier, clarification d'une ambiguïté, nouvelle règle de classement. Compatible avec l'existant.
- **Majeure** (1.0.0 → 2.0.0) : refonte structurelle, renommage de niveau 1, changement de logique. Migration nécessaire.

### Pourquoi cette pratique

- **Méta-gouvernance** : le plan est traité comme un artefact à part entière, pas comme un document mou.
- **Traçabilité des décisions structurantes** : on sait pourquoi le plan a évolué, et quand.
- **Communication** : annoncer "passage en v2.0" alerte tous les utilisateurs qu'une migration est nécessaire.
- **Détection de dérive** : 3 patchs en une journée = signe d'instabilité à surveiller ; 0 évolution en 2 ans = signe de sclérose.

### Signal d'alerte 🚩

- Plan modifié sans incrément de version : pratique à proscrire.
- Pas d'historique daté : impossible de reconstituer l'évolution.
- Versionning incohérent avec celui des fiches (semver pour les fiches, mais pas pour le plan).

## Référence


- ISO 15489-1:2016, §8.4 (Maintenance)
- ISO 30301, §9 (Évaluation et amélioration)
