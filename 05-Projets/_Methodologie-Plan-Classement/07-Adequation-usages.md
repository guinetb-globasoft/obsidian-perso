---
tags: ["methodologie", "plan-classement", "usages", "adoption", "ux"]
created: 2026-05-17
---

# 7. Adéquation aux usages

> Les utilisateurs s'y retrouvent-ils réellement ?

## Principe

Un plan de classement n'a de valeur que s'il est **utilisé** correctement. La meilleure structure théorique échoue si les utilisateurs la contournent.

L'évaluation passe par l'**observation des pratiques réelles**, pas seulement par l'analyse théorique du plan.

## Pourquoi c'est critique sur un projet IT ?

- Un projet IT mobilise des profils variés (MOA, MOE, dev, ops, métier) avec des besoins de recherche différents
- Les documents sont produits et consultés sous **pression** (échéances, tickets, livraisons) → la friction de classement amène au contournement
- L'usage évolue dans la vie du projet (cadrage → conception → run)

## Comment mesurer l'adéquation aux usages

### 1. Observation directe
- Demander à 5-10 utilisateurs de **classer 5 documents** réels
- Observer où ils vont spontanément
- Noter les hésitations, les questions

### 2. Test de recherche
- Demander à des utilisateurs de **retrouver 5 documents** dont on connaît l'emplacement
- Chronométrer
- Noter les chemins empruntés

### 3. Analyse des données d'usage
- Logs d'accès aux dossiers (si SharePoint, GED)
- Fréquence d'accès par branche
- Dossiers jamais consultés / jamais alimentés
- Documents stockés ailleurs (Bureau, OneDrive perso, mails)

### 4. Enquête / entretiens
- Comment vous y prenez-vous pour retrouver un doc ?
- Y a-t-il des choses que vous classez **en dehors** du plan ? Pourquoi ?
- Qu'est-ce qui vous fait perdre du temps ?

## Questions à poser

- [ ] Le plan a-t-il été **conçu avec les utilisateurs** ou pour eux ?
- [ ] Existe-t-il un **guide utilisateur** du plan ?
- [ ] Y a-t-il une **formation** / un onboarding au plan ?
- [ ] Quel est le **taux d'adoption** estimé ?
- [ ] Quels sont les **chemins parallèles** (drives perso, mails, partages ad hoc) ?
- [ ] Y a-t-il un **canal de retour** pour signaler les difficultés ?
- [ ] Le plan est-il **différent selon les profils** d'utilisateurs (vues, raccourcis) ?

## Signaux d'alerte 🚩

- "Tout le monde envoie ses docs par mail"
- "Je préfère garder ma copie locale"
- "Personne ne sait où trouver X"
- "C'est plus rapide de redemander que de chercher"
- Le dossier "Inbox" / "À classer" est plein
- Les documents critiques sont ailleurs que dans le plan
- Doublons massifs entre branches
- Un sous-groupe utilise sa propre structure parallèle

## Indicateurs quantitatifs à suivre

| Indicateur | Bon | Alerte |
|---|---|---|
| Temps moyen de classement | < 30 sec | > 2 min |
| Temps moyen de recherche | < 1 min | > 3 min |
| Taux de docs au bon endroit (audit aléatoire) | > 80% | < 60% |
| Volume "Inbox" / non classé | < 5% | > 20% |
| Documents en doublon | < 5% | > 15% |
| Branches sans accès depuis 1 an | < 10% | > 30% |

## Pièges classiques

### Plan conçu par l'archiviste seul
Le plan est conforme aux normes mais incompréhensible pour les utilisateurs métier.
→ **Co-construction obligatoire.**

### Plan conçu par les utilisateurs sans cadre
Trop pragmatique, ne respecte aucun principe. Tient 6 mois puis explose.
→ **Cadrage méthodologique nécessaire.**

### Plan correct, formation absente
Le plan existe sur le papier, personne ne sait l'utiliser.
→ **Onboarding et documentation indispensables.**

### Plan théorique vs pratique
La structure officielle existe, mais les vrais documents sont dans Teams, mails, drives perso.
→ **Mesurer le shadow IT documentaire.**

## Cas concrets à challenger

**Sur un projet ERP en cours**
- Combien de documents sont dans le SharePoint officiel vs Teams vs mails ?
- Les développeurs utilisent-ils le plan ou leur propre repo ?
- Le métier sait-il où aller chercher la spec de SON module ?

**Sur un projet DWH**
- Les data engineers stockent-ils tout dans Git ? Confluence ? Drive ?
- Les sponsors trouvent-ils les livrables ?

## Lien avec les autres angles

- L'adéquation est facilitée par une [[01-Logique-structurante|logique métier]]
- Et par une [[02-Profondeur-hierarchie|profondeur maîtrisée]]
- Les [[06-Metadonnees|métadonnées]] aident la recherche
- L'usage réel est un indicateur de [[05-Stabilite-evolutivite|durabilité]]

## Référence

- ISO 15489-1:2016, §6.3 (Évaluation et amélioration)
- ISO 30301, §9.1 (Surveillance, mesure, analyse)
- Bonnes pratiques UX / Design d'information
