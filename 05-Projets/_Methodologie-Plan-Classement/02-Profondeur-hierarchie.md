---
tags: ["methodologie", "plan-classement", "profondeur", "hierarchie"]
created: 2026-05-17
---

# 2. Profondeur et hiérarchie

> Le plan est-il navigable et lisible ?

## Principe

Un plan de classement doit être **profond juste ce qu'il faut**. Trop plat, il devient un fourre-tout. Trop profond, il devient ingérable et personne ne le respecte.

**Règle empirique : 3 à 4 niveaux maximum.**

## Pourquoi limiter la profondeur ?

- **Cognition** : au-delà de 4 niveaux, l'utilisateur se perd
- **Maintenance** : chaque niveau supplémentaire multiplie les arbitrages
- **URLs / chemins** : les chemins deviennent trop longs (limites techniques sur Windows à 260 caractères)
- **Migrations** : un plan profond est très coûteux à faire évoluer

## Structure type recommandée

```
Niveau 1 : Fonction métier        (ex: Gestion commerciale)
  Niveau 2 : Activité             (ex: Contractualisation)
    Niveau 3 : Sous-activité      (ex: Contrats clients)
      Niveau 4 : Dossier opérationnel  (ex: Client X - Projet Y)
```

Au-delà = sous-dossiers libres dans le dossier opérationnel, mais hors plan formel.

## Largeur (nombre d'entrées par niveau)

- **Idéal** : 5 à 9 entrées par niveau (capacité mémoire de travail)
- **Maximum** : 12-15
- **Au-delà** : il faut un sous-niveau intermédiaire OU une refonte

## Questions à poser

- [ ] Combien de niveaux compte le plan ? (compter le niveau le plus profond)
- [ ] Combien d'entrées y a-t-il à chaque niveau ? (au moins 3, au plus 12)
- [ ] Y a-t-il des branches « creuses » (un seul sous-dossier) ?
- [ ] Y a-t-il des branches « obèses » (50+ sous-dossiers) ?
- [ ] Les chemins finaux dépassent-ils 200 caractères ?

## Signaux d'alerte 🚩

- Plus de 5 niveaux dans le plan formel
- Une branche avec 20+ sous-dossiers au même niveau
- Une branche avec un seul sous-dossier (témoigne d'un mauvais découpage)
- Des numérotations à 3 chiffres (`01.02.03.04.05`) → souvent symptôme de sur-structuration
- Des libellés très longs qui se répètent dans le chemin

## Cas concrets à challenger

**Branche obèse (à découper)**
```
03-Specifications/
├── Spec-Module-Achats.docx
├── Spec-Module-Ventes.docx
├── Spec-Module-Stocks.docx
├── ... (38 autres)
```
→ Introduire un niveau intermédiaire par module/domaine fonctionnel.

**Branche creuse (à aplatir)**
```
03-Specifications/
└── 03.01-Fonctionnelles/
    └── 03.01.01-Module-Achats/
        └── Spec.docx
```
→ Aplatir, le sous-niveau ne sert à rien.

## Lien avec les autres angles

- Une profondeur maîtrisée renforce l'[[07-Adequation-usages|adéquation aux usages]]
- Une bonne largeur traduit souvent une bonne [[01-Logique-structurante|logique structurante]]
- L'évolution est facilitée → [[05-Stabilite-evolutivite|stabilité]]

## 🔄 Nuances issues du terrain (audit DWH 2026-05)

### Profondeur 4-5 niveaux : acceptable si...

La règle "3-4 niveaux max" reste un bon point de départ, mais **5 niveaux peuvent être acceptables** si :

- la **largeur** est maîtrisée à chaque niveau (5-12 entrées)
- la **codification** est stable et claire
- les chemins finaux restent **< 200 caractères**
- la profondeur correspond à une **hiérarchie métier naturelle** (ex : domaine → phase → type → instance)

Le drapeau rouge n'est pas la profondeur en soi, mais la profondeur combinée à une largeur déséquilibrée ou une codification incohérente.

### Branche creuse : à nuancer

Une branche avec un seul fichier n'est pas toujours un anti-pattern. Cas légitime :

- **Branche transitoire anticipée** : on crée la sous-structure (par site, par MEP, par module) en prévision de fichiers à venir dans une phase future. Le dossier est creux au moment T mais sera rempli à T+N.

Devient un anti-pattern si :

- la branche est creuse **depuis > 6 mois** sans perspective d'alimentation
- aucune note d'intention ne documente pourquoi la sous-structure existe
- le `README.md` placé pour "garder" le dossier reste vide ou désincarné

**Règle pratique** : branche creuse acceptable si transitoire anticipée et documentée ; à aplatir sinon.

## Référence


- ISO 15489-1:2016, §9.4
- MoReq2010, exigences sur la classification hiérarchique
