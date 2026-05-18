---
tags: ["methodologie", "plan-classement", "mece", "exhaustivite", "exclusivite"]
created: 2026-05-17
---

# 3. Exhaustivité et exclusivité (MECE)

> Chaque document doit avoir **une et une seule** place logique dans le plan.

## Principe

Le plan doit respecter le principe **MECE** (Mutually Exclusive, Collectively Exhaustive) :
- **Exhaustivité** : tout document produit a une place dans le plan
- **Exclusivité** : il n'a qu'une seule place possible (pas d'ambiguïté)

C'est l'un des critères les plus difficiles à atteindre — et le plus souvent défaillant en pratique.

## Pourquoi c'est critique ?

- Si **plusieurs places possibles** → chacun classe différemment → impossible de retrouver
- Si **aucune place** → "Divers" se remplit → le plan se dégrade
- C'est la condition de fiabilité de la recherche

## Tests à appliquer

### Test d'exhaustivité
Prendre 10-20 documents réels du projet, au hasard. Tenter de les classer dans le plan.
→ Si un document n'a pas de place évidente, **le plan est incomplet**.

### Test d'exclusivité
Pour chacun de ces documents, demander à 3 personnes différentes où elles le classeraient.
→ Si elles divergent, **les libellés sont ambigus** ou **les frontières floues**.

### Test du document hybride
Identifier les documents transverses (ex: un cahier des charges qui couvre fonctionnel ET technique).
→ Comment le plan les traite-t-il ? Doublon ? Lien ? Choix arbitraire documenté ?

## Questions à poser

- [ ] Existe-t-il un dossier "Divers" / "Autres" / "À classer" ? À quel niveau ?
- [ ] Les frontières entre dossiers sont-elles **documentées** (règle de classement explicite) ?
- [ ] Y a-t-il un **guide de classement** qui lève les ambiguïtés ?
- [ ] Les libellés sont-ils **non-recouvrants** sémantiquement ?
- [ ] Comment sont traités les documents multi-thématiques ?

## Signaux d'alerte 🚩

- Présence d'un dossier "Divers" rempli
- Deux dossiers aux libellés proches : "Documentation technique" et "Documentation projet"
- Discussion récurrente "tu l'as mis où ?"
- Documents en doublon dans plusieurs branches (volontairement ou non)
- Absence de guide de classement écrit
- Libellés vagues : "Général", "Documents", "Informations"

## Stratégies pour gérer les documents transverses

### Option 1 : Classement principal + raccourcis
Classer à l'emplacement principal, créer des liens/raccourcis ailleurs.
✅ Adapté aux SI documentaires (SharePoint, GED)
❌ Pas adapté à un système de fichiers classique

### Option 2 : Métadonnées multi-valuées
Un seul classement physique, plusieurs tags / métadonnées de contexte.
✅ Permet la recherche multi-axes
→ Voir [[06-Metadonnees]]

### Option 3 : Règle de priorité documentée
"En cas de doute entre X et Y, toujours classer en X." Explicite, simple, défendable.
✅ Le plus pragmatique en environnement bureautique simple

## Cas concrets à challenger

**Ambiguïté typique : où classer un compte-rendu de COPIL ?**
- Sous `01-Gouvernance/Comptes-rendus` ?
- Sous `02-Pilotage/Reunions` ?
- Sous le projet concerné `05-Projets/.../CR` ?

→ Trancher une fois pour toutes, documenter la règle.

## Lien avec les autres angles

- L'exclusivité s'appuie sur une [[01-Logique-structurante|logique structurante]] saine
- Les ambiguïtés résiduelles peuvent être levées par les [[06-Metadonnees|métadonnées]]
- Le test passe par l'observation des [[07-Adequation-usages|usages réels]]

## Référence

- ISO 15489-1:2016, §9.4 et §9.5
- ISO 16175-1, exigences sur l'unicité du classement
