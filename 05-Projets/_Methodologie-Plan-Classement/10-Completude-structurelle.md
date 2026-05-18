---
tags: ["methodologie", "plan-classement", "completude", "obligatoires", "transverses"]
created: 2026-05-17
---

# 10. Complétude structurelle

> Le plan contient-il tous les artefacts transverses obligatoires d'un projet IT ?

## Principe

Un plan de classement peut être parfaitement structuré, MECE, métadonné, livrable — et néanmoins **incomplet** s'il manque les artefacts transverses indispensables à tout projet IT : dossier de gouvernance, ADR, changelog, glossaire métier, etc.

Cet angle évalue la **présence** (pas la qualité — c'est le rôle des autres angles) des éléments structurants attendus dans tout plan de classement IT mûr.

## Pourquoi c'est critique sur un projet IT

- Un projet IT sans gouvernance documentaire formalisée perd la mémoire en 6 mois.
- Sans ADR, les décisions structurantes deviennent du folklore oral, impossibles à challenger.
- Sans glossaire métier, "facture", "projet", "imputation" ont N sens selon les interlocuteurs.
- Sans cartographie d'architecture, l'écosystème reste dans la tête du tech lead — risque opérationnel direct.
- Sans index des livrables, la livraison devient un tri manuel risqué (cf. [[09-Livrabilite-cloture-projet]]).

Ces manques sont des **points aveugles** classiques des projets IT : on investit massivement dans le code, peu dans la méta-doc. La complétude structurelle est l'angle qui révèle ces angles morts.

## Les 7 obligatoires transverses

Tout plan de classement de projet IT doit contenir ces 7 éléments. Leur **absence** est un défaut, indépendamment du reste.

### 1. Dossier de gouvernance documentaire

**Statut** : obligatoire

**Rôle** : centralise la méta-doc du projet (charte, conventions, statuts, rôles, schéma de métadonnées, plan de classement lui-même).

**Forme typique** : un dossier dédié au niveau 1 du plan, souvent nommé `00-gouvernance/`, `_gouvernance/`, `gouvernance/`...

**Contenu minimal attendu** :
- Plan de classement (le document qu'on évalue)
- Charte de documentation (qui documente quoi, comment, à quelle fréquence)
- Conventions de nommage (codification fichiers, codes, références)
- Référentiel des statuts (vocabulaire contrôlé des états)
- Rôles et responsabilités (qui valide quoi)
- Schéma de métadonnées (frontmatters autorisés par type de fiche)

**Signal d'alerte 🚩** : pas de dossier dédié, la gouvernance est diluée dans d'autres dossiers ou n'existe pas du tout.

### 2. Décisions d'architecture (ADR)

**Statut** : obligatoire

**Rôle** : tracer les décisions structurantes du projet — pourquoi tel choix d'architecture, pourquoi tel domaine fonctionnel, pourquoi telle convention.

**Forme typique** : un dossier `decisions-architecture/`, `adr/`, `architecture-decisions/`, généralement dans le dossier annexes ou gouvernance.

**Contenu minimal attendu** :
- Au moins **1 ADR par décision structurante**.
- ADR **immuables** (supersedables mais jamais modifiées).
- Chaque ADR porte un statut (proposée / acceptée / dépréciée / supersedée).

**Signal d'alerte 🚩** : aucune ADR, ou ADR modifiées rétroactivement, ou décisions structurantes orales non tracées.

### 3. Changelog projet

**Statut** : obligatoire

**Rôle** : journal des évolutions structurantes du projet (différent du Git log trop fin, et du planning orienté futur).

**Forme typique** : fichier `changelog.md` à la racine du projet ou dans le dossier annexes.

**Contenu minimal attendu** :
- Une entrée par évolution structurante (nouvelle MEP, refonte, changement de règle métier majeure...).
- Datée et auteurisée.
- Format reconnu (souvent inspiré de [Keep a Changelog](https://keepachangelog.com)).

**Signal d'alerte 🚩** : pas de changelog ; ou changelog vide ; ou changelog qui se résume aux commits Git.

### 4. Glossaire métier

**Statut** : obligatoire

**Rôle** : vocabulaire commun entre tech et métier pour éviter les malentendus sémantiques.

**Forme typique** : fichier `glossaire.md`, `glossary.md`, généralement dans le dossier métier.

**Contenu minimal attendu** :
- Une entrée par terme métier ambigu (chaque "facture", "projet", "imputation"… défini).
- Définition stable, partagée avec le métier.

**Signal d'alerte 🚩** : pas de glossaire, ou glossaire-stub jamais alimenté, ou glossaire purement technique sans dimension métier.

### 5. Dossier d'archives / annexes

**Statut** : obligatoire

**Rôle** : accueillir les artefacts ayant eu une utilité ponctuelle et conservés pour traçabilité, sans polluer la doc vivante.

**Forme typique** : dossier `99-annexes/`, `archives/`, `_archives/`...

**Contenu minimal attendu** :
- Au moins une sous-organisation cohérente (par phase, par sprint, par type).
- Règle d'archivage documentée (quand un artefact bascule en archive).

**Signal d'alerte 🚩** : pas de dossier dédié ; les artefacts ponctuels restent dans les dossiers vivants ; ou tout est supprimé (perte de mémoire).

### 6. README / Vue d'ensemble / Onboarding

**Statut** : obligatoire

**Rôle** : porte d'entrée pour un nouvel arrivant — comprendre le projet en 10 minutes.

**Forme typique** : `README.md` à la racine du repo / vault ; éventuellement complété par une note `vue-ensemble.md` dans le dossier architecture.

**Contenu minimal attendu** :
- Objectif du projet (1 paragraphe).
- Pointeurs vers les ressources clés (plan de classement, charte, glossaire, cartographie).
- Comment contribuer / par où commencer.

**Signal d'alerte 🚩** : pas de README ; ou README générique non maintenu ; ou doc d'onboarding éclatée sans porte d'entrée claire.

### 7. Cartographie d'architecture / flux

**Statut** : obligatoire (pour projets IT)

**Rôle** : représentation visuelle de l'architecture cible — composants, flux de données, dépendances.

**Forme typique** : note `cartographie-flux.md`, `architecture.md`, `vue-ensemble.md` dans le dossier architecture, idéalement avec un schéma (Mermaid, Excalidraw, image).

**Contenu minimal attendu** :
- Schéma visuel des composants et flux principaux.
- Légende explicite.
- Mise à jour à chaque évolution structurelle.

**Signal d'alerte 🚩** : pas de cartographie ; ou cartographie texte uniquement sans schéma ; ou cartographie obsolète.

## Les obligatoires conditionnels

Ces éléments sont **obligatoires si la condition est remplie**, recommandés sinon.

### 8. Calendrier de conservation

**Statut** : conditionnellement obligatoire

**Condition** : projet soumis à obligations réglementaires (RGPD, code de commerce, code de la santé publique, secteur réglementé).

**Forme typique** : note `calendrier-conservation.md` ou tableau intégré au plan de classement.

**Lien avec autre angle** : sortie de l'[[04-Calendrier-conservation-DUA]]. La présence est évaluée ici, la qualité dans l'angle 4.

### 9. Cartographie RGPD

**Statut** : conditionnellement obligatoire

**Condition** : projet manipule des données à caractère personnel (RGPD art. 4).

**Forme typique** : note `cartographie-rgpd.md` ou fiches dédiées par traitement.

**Contenu minimal** : pour chaque traitement, finalité / base légale / durée de conservation / droits des personnes.

**Lien avec autre angle** : sortie de l'[[08-Conformite-reglementaire]].

### 10. Index des livrables

**Statut** : conditionnellement obligatoire

**Condition** : projet avec livraisons documentaires structurantes (contractuelles ou récurrentes).

**Forme typique** : note `index-livrables.md` dans le dossier gouvernance.

**Lien avec autre angle** : sortie de l'[[09-Livrabilite-cloture-projet]].

### 11. Runbook / Guide d'exploitation

**Statut** : conditionnellement obligatoire

**Condition** : projet en production (ou destiné à y passer).

**Forme typique** : note `runbook.md`, `exploitation.md`, ou par MEP/release.

**Contenu minimal** : procédures de démarrage, monitoring, incidents courants, contacts d'astreinte.

## Grille de scoring

L'angle 10 utilise une **logique de couverture** plutôt qu'une appréciation qualitative :

| Score | Critère |
|---|---|
| **3** | Les 7 obligatoires sont présents **et** tous les conditionnels applicables sont présents |
| **2** | Les 7 obligatoires sont présents, certains conditionnels applicables manquent |
| **1** | 1 ou 2 obligatoires manquent |
| **0** | 3 obligatoires ou plus manquent |

Une couverture binaire (présent / absent) suffit pour le scoring — la qualité de chaque artefact est évaluée dans les angles correspondants.

## Checklist d'audit

À cocher pour chaque projet :

### Obligatoires
- [ ] Dossier de gouvernance documentaire
- [ ] Décisions d'architecture (ADR)
- [ ] Changelog projet
- [ ] Glossaire métier
- [ ] Dossier d'archives / annexes
- [ ] README / Vue d'ensemble
- [ ] Cartographie d'architecture

### Conditionnels (cocher uniquement si la condition s'applique)
- [ ] Calendrier de conservation *(si soumis à obligations réglementaires)*
- [ ] Cartographie RGPD *(si données personnelles)*
- [ ] Index des livrables *(si livraisons structurantes)*
- [ ] Runbook / Guide d'exploitation *(si projet en production)*

## Questions à poser

- [ ] Existe-t-il un **dossier dédié** à la gouvernance documentaire ?
- [ ] Les **décisions structurantes** sont-elles formalisées en ADR ?
- [ ] Un **changelog** projet est-il maintenu ?
- [ ] Un **glossaire métier** est-il accessible et utilisé ?
- [ ] Existe-t-il un **dossier d'archives** avec règle de bascule documentée ?
- [ ] Le projet a-t-il un **README** ou une **vue d'ensemble** claire pour un arrivant ?
- [ ] Existe-t-il une **cartographie d'architecture visuelle** ?
- [ ] Si conditions applicables : DUA / RGPD / livrables / runbook sont-ils couverts ?

## Anti-patterns

### ❌ La gouvernance diluée
Pas de dossier dédié — la charte est dans un dossier "doc", les conventions dans un wiki, les rôles dans un Notion. Personne ne trouve.

### ❌ Les ADR-postiches
Un dossier `adr/` existe mais ne contient que la première décision faite il y a 2 ans. Plus rien depuis.

### ❌ Le changelog Git
"Notre changelog c'est `git log`." Trop fin, illisible, pas filtré par criticité.

### ❌ Le glossaire technique sans métier
Glossaire qui définit "Kubernetes" et "CI/CD" mais pas "client", "commande", "facture".

### ❌ Le README orphelin
Un README généré au scaffolding du projet, jamais mis à jour, qui dit "TODO: write description".

### ❌ La cartographie texte
"L'architecture est documentée." Oui, mais sous forme de 12 paragraphes sans schéma. Personne ne la lit.

## Bonnes pratiques

### ✅ Dossier `00-gouvernance/` au tout début du plan
Préfixe `00-` pour signaler "à lire en premier". Visible immédiatement.

### ✅ Modèle d'ADR standardisé
Un template (`_template-adr.md`) qui force le format : contexte / décision / conséquences / historique.

### ✅ Glossaire vivant avec backlinks
Chaque terme du glossaire est wikilinké depuis les fiches qui l'utilisent.

### ✅ README court et pointeurs
Le README ne raconte pas tout — il pointe vers les bonnes ressources (charte, plan de classement, cartographie).

### ✅ Cartographie auto-générée si possible
Schéma Mermaid versionné dans Git, mis à jour comme du code.

## Articulation avec les autres angles

- **[[01-Logique-structurante]]** : la complétude soutient la structure (un dossier gouvernance bien placé = première manifestation d'une logique claire).
- **[[03-Exhaustivite-exclusivite]]** : la complétude est un cas particulier d'exhaustivité — tout doc obligatoire doit avoir sa place.
- **[[04-Calendrier-conservation-DUA]]** : la présence du calendrier est évaluée ici, sa qualité là-bas.
- **[[05-Stabilite-evolutivite]]** : les ADR et le changelog sont des outils de stabilité.
- **[[08-Conformite-reglementaire]]** : présence de la cartographie RGPD ici, qualité de la couverture RGPD là-bas.
- **[[09-Livrabilite-cloture-projet]]** : présence de l'index livrables ici, qualité de la stratégie livrabilité là-bas.

## Référence

- ISO 15489-1:2016, §8 (Exigences pour un système de gestion des records)
- R2GA, partie II — outils et modèles
- Bonnes pratiques ADR : Michael Nygard (2011) — *Documenting Architecture Decisions*
- Keep a Changelog (standard de facto) : keepachangelog.com
