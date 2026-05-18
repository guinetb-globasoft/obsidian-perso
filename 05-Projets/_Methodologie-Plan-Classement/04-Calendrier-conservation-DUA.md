---
tags: ["methodologie", "plan-classement", "dua", "conservation", "rgpd"]
created: 2026-05-17
---
	
# 4. Calendrier de conservation et sort final (DUA)

> Combien de temps conserve-t-on chaque document, et qu'en fait-on ensuite ?

## Principe

Un plan de classement seul est insuffisant. Il doit être associé à un **calendrier de conservation** (ou tableau de gestion) qui définit, pour chaque catégorie :
- **DUA** (Durée d'Utilité Administrative) : durée de conservation active
- **Sort final** : élimination, conservation définitive, tri sélectif

C'est l'articulation **plan de classement ↔ politique de conservation** qui donne sa valeur juridique au dispositif.

## Pourquoi c'est critique sur un projet IT ?

- **RGPD** : on ne peut pas conserver des données personnelles indéfiniment (obligation de purge)
- **Obligations légales** : durées minimales (contrats : 5-10 ans, comptable : 10 ans, etc.)
- **Coûts de stockage** : conserver l'inutile coûte cher (espace, sauvegarde, sécurité)
- **Recherche** : moins de bruit = meilleure pertinence
- **Risque juridique** : conserver trop longtemps expose en cas de litige

## Composantes du calendrier

Pour chaque catégorie du plan :

| Élément | Description | Exemple |
|---------|-------------|---------|
| Type de document | Catégorie au sens du plan | Spécifications fonctionnelles |
| DUA | Durée d'utilité administrative | Durée du projet + 5 ans |
| Point de départ | Quand démarre le décompte | Clôture du projet |
| Référence juridique | Texte qui justifie la durée | Code civil art. 2224 |
| Sort final | Action en fin de DUA | Versement archives / Destruction |
| Responsable | Qui applique le sort final | DSI / Archiviste |

## Questions à poser

- [ ] Existe-t-il un calendrier de conservation **écrit** associé au plan ?
- [ ] Couvre-t-il **toutes** les catégories du plan ?
- [ ] Les durées s'appuient-elles sur des **références juridiques** identifiées ?
- [ ] Le **sort final** est-il défini (pas seulement la DUA) ?
- [ ] Les durées RGPD sont-elles intégrées (données personnelles) ?
- [ ] Existe-t-il un processus de **revue périodique** des durées ?
- [ ] Y a-t-il un mécanisme automatisé d'**alerte / purge** ?

## Signaux d'alerte 🚩

- Pas de calendrier de conservation du tout
- Calendrier qui dit "à conserver" partout sans précision
- Aucune mention RGPD
- Pas de référence juridique sur les durées
- Personne n'a jamais purgé / archivé quoi que ce soit
- Les documents s'accumulent depuis 10 ans sans tri

## Durées typiques sur un projet IT

| Type de document | DUA indicative | Sort final |
|---|---|---|
| Spécifications fonctionnelles | Durée vie SI + 5 ans | Conservation (mémoire) |
| Codes sources / livrables | Durée vie SI + 5 ans | Conservation |
| Comptes-rendus de réunion | Durée projet + 3 ans | Tri sélectif |
| Tickets / incidents | 3 ans | Destruction |
| Logs applicatifs | 6 mois à 1 an (RGPD) | Destruction |
| Contrats prestataires | Fin contrat + 10 ans | Destruction |
| Données personnelles utilisateurs | Selon finalité (RGPD) | Destruction obligatoire |

⚠️ Ces durées sont **indicatives** : à adapter au contexte juridique et sectoriel.

## Articulation avec le plan de classement

Idéalement, le calendrier est **structuré comme le plan** : chaque feuille du plan a sa ligne dans le calendrier.

```
Plan : 03-Conception/03.02-Specifications-fonctionnelles
        ↓
Calendrier : DUA = Vie SI + 5 ans, Sort = Conservation
```

## Cas concrets à challenger

**Cas du projet ERP terminé depuis 5 ans**
- Le plan contient encore les drafts, brouillons, échanges email ?
- A-t-on extrait et archivé les livrables finaux ?
- Qu'est-il prévu pour le code source quand l'ERP sera décommissionné ?

**Cas des données personnelles utilisateurs**
- Quelle finalité ? Quelle base légale RGPD ?
- Durée définie ? Mécanisme de purge automatique ?

## Lien avec les autres angles

- Indissociable de la [[08-Conformite-reglementaire|conformité réglementaire]]
- Soutient la [[05-Stabilite-evolutivite|durabilité]] en évitant l'engorgement
- Permet de mesurer l'[[07-Adequation-usages|usage réel]] (documents jamais ouverts)

## 🔄 Le cycle de vie comme dimension de classification (enrichissement issu de l'audit DWH)

> Insight issu de l'[[../99-annexes/Audit-Plan-Classement-2026-05|audit DWH Aerotec 2026-05]] : sur un projet IT, le cycle de vie est souvent une **dimension orthogonale** à la structure fonctionnelle, qui mérite d'être explicitée.

### Les 4 cycles de vie types

| Cycle | Durée de vie | Comportement attendu |
|---|---|---|
| 🟢 **Pérenne** | Toute la durée du projet | Mise à jour continue, revue périodique. Source de vérité courante. |
| 🟡 **Transition** | Une phase (sprint, recette, MEP, jalon) | Vit pendant la phase, puis figé ou archivé à la clôture. |
| ⚫ **Archive** | Conservé pour traçabilité | Figé, ne se modifie plus. Référence historique (audit, contexte). |
| 🔵 **Livrable** | Externe au système doc | Document produit pour le destinataire final, régénérable depuis le pipeline. |

### Concept-clé : « conteneur pérenne avec contenu archive »

Un dossier peut être **pérenne** (il s'enrichit au fil du temps : nouveaux sprints, nouveaux audits, nouvelles phases) tout en ne contenant que des fichiers **individuellement figés** une fois publiés.

**Exemple** : un dossier `99-annexes/qualite/` accueille un rapport qualité par phase. Chaque rapport est figé à sa publication, mais le dossier vit. À ne pas confondre avec un dossier transition (où la phase entière a une fin et bascule en archive).

Cette nuance est importante pour le MECE ([[03-Exhaustivite-exclusivite]]) : un dossier mixte n'est pas un dossier mal classé, c'est un dossier qui héberge des objets dont le cycle individuel diffère de celui du conteneur.

### Frontmatter cycle de vie

Ajouter aux fiches concernées :

```yaml
cycle_vie: perenne | transition | archive | livrable
phase: <nom de la phase>   # uniquement si transition ou archive
```

### Quand explicitement classer par cycle de vie ?

- Projet **multi-phases** (sprints, MEPs, jalons) où chaque phase produit des artefacts qui survivent à la phase suivante.
- Projet avec **forte exigence d'audit** (traçabilité historique des décisions).
- Projet où la **distinction doc-vivante / doc-figée** est métier-significative (recette terminée vs en cours).

## Référence


- ISO 15489-1:2016, §9.6 (Conservation et sort final)
- Code du patrimoine (secteur public FR)
- RGPD, art. 5 (limitation de la conservation)
- Instruction DAF DPACI/RES/2009/018 (secteur public)
