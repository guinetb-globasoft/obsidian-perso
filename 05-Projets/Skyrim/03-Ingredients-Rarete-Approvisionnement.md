---
projet: Skyrim
type: analyse
tags: ["skyrim", "modding", "cuisine", "ingrédients", "rareté", "approvisionnement"]
created: 2026-07-27
---

# Ingrédients de cuisine — rareté réelle et difficulté d'obtention

> Mesure sur les 33 ingrédients des recettes de [[02-Recettes-Cuisine]] : placements dans le monde, plantes récoltables, dépouilles d'animaux, listes de butin et marchands. **Rareté et difficulté ne se recouvrent pas** : les trois ingrédients les plus durs à obtenir ne sont pas les plus rares, et l'ingrédient le plus rare du jeu tombe d'un ennemi banal.

## La distinction qui compte

Un ingrédient peu nombreux mais **renouvelable** (plante qui repousse, animal qui réapparaît, marchand qui réassortit) est plus facile à obtenir qu'un ingrédient abondant mais **fini**. C'est ce second axe qui décide, pas le décompte brut.

Trois profils ressortent :

| Profil | Ce que ça implique | Exemple |
|---|---|---|
| **Renouvelable** | Stock infini dans le temps | Snowberries (1 676 plants) |
| **Fini** | Ce qui est posé est tout ce qui existe | Eidar Cheese Wheel (337, zéro source) |
| **Conditionnel** | Renouvelable, mais seulement après avoir débloqué la source | Butter (baratte à construire) |

## Les 3 vrais goulots — le four HearthFires

Ce sont les plus durs du jeu, et de loin. **Aucun des trois n'a la moindre liste de butin ni de marchand** : vérifié par balayage exhaustif de toute référence à leur FormID, sur tous les records de tous les plugins actifs.

### 1. Butter — le pire

| Mesure | Valeur |
|---|---|
| Posés dans le monde | **3** |
| Barattes récoltables (`BYOHButterChurn`) | **3** |
| Listes de butin · conteneurs · dépouilles | **0 · 0 · 0** |
| Recettes qui en demandent | **8** |

Trois exemplaires dans tout Bordeciel. La seule source renouvelable est la **baratte**, qui produit bien du beurre (`PFIG → BYOHFoodButter` confirmé) — mais il n'en existe que 3, une par domaine Hearthfire, et **il faut les construire**. Le record `QUST BYOHHouseBuilding` référence le beurre, ce qui confirme le rattachement au chantier de domaine.

> **Tant qu'on n'a pas bâti de domaine avec sa baratte, le beurre est pratiquement introuvable** — et il entre dans 8 des 12 recettes du four.

### 2. Jug of Milk

| Mesure | Valeur |
|---|---|
| Posés dans le monde | **15** |
| Listes de butin · conteneurs · plantes · dépouilles | **0 · 0 · 0 · 0** |
| Recettes qui en demandent | **4** |

Aucune source automatique d'aucune sorte. Les seules références vivantes sont les trois **vaches de domaine** (`BYOHHouse1CowRef`, `BYOHHouse2CowRef`, `BYOHHouse3CowRef`) — donc même logique que le beurre : il faut acheter la vache de son domaine.

### 3. Sack of Flour — le plus sollicité

| Mesure | Valeur |
|---|---|
| Posés dans le monde | **15** |
| Listes de butin | 3 (`BYOHLItemFoodFlour`, `…75`, `…Small`) |
| Recettes qui en demandent | **11 sur 12** |

Le seul des trois à avoir une porte de sortie propre : **la farine se fabrique**. La recette `BYOHRecipeFoodFlour` produit 1 Sack of Flour contre **3× Wheat**, au **moulin à grain** (mot-clé `isGrainMill`).

Et le blé, lui, est abondant : **195 sources** (109 posés + 86 plants récoltables, donc renouvelables). La farine est donc la moins bloquante des trois — mais elle impose une chaîne en deux étapes et l'accès à un moulin.

> [!tip] Conséquence pratique
> Le four Hearthfire est verrouillé derrière son propre écosystème : domaine bâti + baratte + vache + moulin. **Les 12 recettes du four sont inaccessibles en pratique à un personnage sans domaine**, quels que soient ses ingrédients par ailleurs. Le chaudron n'a aucune de ces contraintes.

## Le cas à part — Eidar Cheese Wheel

| Mesure | Valeur |
|---|---|
| Posés dans le monde | **337** |
| Listes de butin | **0** |
| Conteneurs | 2 — `QAPotionContainer` et `QAIngredientContainer` |
| Dépouilles · plantes | **0 · 0** |

337 exemplaires, ce qui semble confortable — mais **aucune source renouvelable**. Pas une liste de butin, pas un marchand, pas une dépouille. Les deux seuls conteneurs qui le citent sont des **caisses de test de développement** (préfixe `QA`), situées dans des cellules inaccessibles en jeu : elles ne comptent pas.

C'est donc un **stock strictement fini de 337 unités** pour toute la partie. Et c'est l'ingrédient clé de l'**Elsweyr Fondue**, le meilleur plat du jeu. À ne pas gaspiller.

À côté, le **Moon Sugar** de la même recette (49 posés) est bien plus confortable : il tombe des **corbeuses** (13 variantes de hagravens le portent en dépouille) et apparaît dans des listes marchandes (`LItemMoonsugar75`, listes d'apothicaire, butin de bandits et de Parjures).

## Faux amis — rares au décompte, faciles en réalité

| Ingrédient | Posés | Pourquoi c'est facile |
|---|---|---|
| **Mudcrab Legs** | **3** | Tombe des crabes de vase (`DeathItemMudCrab01/02/03`) — l'un des ennemis les plus communs du jeu |
| **Chicken Breast** | 8 | Poulets de ferme + 5 listes de butin |
| **Mammoth Snout** | 18 | `DeathItemMammoth` **et vendu par Bolis à Markarth** (`MerchantMarkarthBolisChest`) — difficile par le danger, pas par la rareté |
| **Horse Meat** | 36 | Dépouille de n'importe quel cheval (28 variantes) — difficile moralement, pas matériellement |
| **Leg of Goat** | 57 | Chèvres + 8 listes |

**Mudcrab Legs est l'ingrédient le moins présent du jeu (3 exemplaires) et pourtant l'un des plus faciles à obtenir.** C'est l'illustration parfaite de l'écart entre les deux mesures.

## Tableau complet — 33 ingrédients

Trié du plus difficile au plus facile. « Total » = posés + plants récoltables.

| Ingrédient | Posés | Plants | Total | Butin | Recettes | Renouvelable ? |
|---|---:|---:|---:|---:|---:|---|
| Butter | 3 | 3 | **6** | 0 | 8 | ⚠️ baratte de domaine seulement |
| Jug of Milk | 15 | 0 | **15** | 0 | 4 | ⚠️ vache de domaine seulement |
| Sack of Flour | 15 | 0 | **15** | 3 | 11 | ⚠️ fabricable (3× Wheat au moulin) |
| Mudcrab Legs | 3 | 0 | 3 | 3 | 1 | ✅ crabes de vase |
| Chicken Breast | 8 | 0 | 8 | 4 | 2 | ✅ poulets |
| Mammoth Snout | 18 | 0 | 18 | 1 | 1 | ✅ mammouths + 1 marchand |
| Horse Meat | 36 | 0 | 36 | 1 | 1 | ✅ chevaux |
| Moon Sugar | 49 | 0 | 49 | 3 | 2 | ✅ corbeuses + marchands |
| Leg of Goat | 57 | 0 | 57 | 9 | 1 | ✅ chèvres |
| Raw Beef | 63 | 0 | 63 | 4 | 2 | ✅ vaches |
| Horker Meat | 67 | 0 | 67 | 6 | 2 | ✅ horkers |
| Venison | 96 | 0 | 96 | 10 | 2 | ✅ cerfs et élans |
| Chicken's Egg | 139 | 71 | 210 | 2 | 4 | ✅ nids de poules |
| Carrot | 212 | 0 | 212 | 8 | 1 | ✅ listes |
| Ale | 217 | 0 | 217 | 6 | 1 | ✅ 17 listes (soldats, citadins, auberges) |
| **Salt Pile** | 239 | 0 | **239** | 10 | **22** | ✅ mais **très sollicité** |
| **Eidar Cheese Wheel** | 337 | 0 | **337** | **0** | 1 | ❌ **stock fini** |
| Green Apple | 390 | 0 | 390 | 8 | 2 | ✅ |
| Tomato | 397 | 0 | 397 | 7 | 3 | ✅ |
| Pheasant Breast | 59 | 342 | 401 | 5 | 1 | ✅ |
| Leek | 267 | 183 | 450 | 1 | 5 | ✅ |
| Jazbay Grapes | 91 | 379 | 470 | 3 | 1 | ✅ |
| Raw Rabbit Leg | 66 | 571 | 637 | 6 | 1 | ✅ |
| Red Apple | 644 | 0 | 644 | 11 | 3 | ✅ |
| Cabbage | 515 | 238 | 753 | 6 | 3 | ✅ |
| Salmon Meat | 66 | 708 | 774 | 5 | 1 | ✅ |
| Lavender | 270 | 606 | 876 | 7 | 2 | ✅ |
| Clam Meat | 35 | 871 | 906 | 1 | 1 | ✅ |
| Garlic | 388 | 526 | 914 | 5 | 5 | ✅ |
| Bread | 1 006 | 0 | 1 006 | 4 | 1 | ✅ (et fabricable au four) |
| Juniper Berries | 43 | 1 082 | 1 125 | 5 | 1 | ✅ |
| Potato | 1 150 | 307 | 1 457 | 5 | 6 | ✅ |
| Snowberries | 161 | 1 676 | 1 837 | 5 | 2 | ✅ |

## Le cas Salt Pile

239 exemplaires, renouvelable, 10 listes de butin — rien d'alarmant en apparence. Mais il entre dans **22 des 33 recettes**, soit deux fois plus que n'importe quel autre ingrédient. C'est le **goulot d'étranglement par le volume**, pas par la rareté.

D'où l'intérêt déjà noté dans [[02-Recettes-Cuisine]] pour la **Vegetable Soup**, seule recette du jeu qui n'en demande pas, alors qu'elle offre la régénération double sur 12 minutes.

## Annexe — méthode

Quatre mesures croisées, sur les 29 plugins actifs dans l'ordre de chargement réel :

| Mesure | Source | Ce qu'elle dit |
|---|---|---|
| Placements | `REFR` → `NAME` | Combien d'exemplaires posés dans le monde |
| Plants récoltables | `FLOR` / `TREE` → `PFIG` | Sources qui repoussent |
| Butin | `LVLI` → `LVLO`, **listes imbriquées remontées récursivement** | Marchands, coffres, dépouilles |
| Dépouilles | `NPC_` → `INAM` | Quels animaux le laissent |

Le décompte des plants passe par une **double indirection** : un chou dans le monde est un `REFR` pointant vers un record `FLOR` (le plant), dont le champ `PFIG` désigne l'ingrédient produit. Compter les `REFR` de l'ingrédient seul sous-évalue massivement tous les végétaux — Snowberries passerait de 1 837 à 161.

Les listes de butin sont **imbriquées** (`LootBanditIngredients10` contient `LItemIngredientsUncommon` qui contient Moon Sugar). Une remontée récursive est indispensable, sinon la plupart des ingrédients paraissent absents du butin.

> [!warning] Deux vérifications qui ont changé les conclusions
> **Les FormID supposés étaient tous faux.** Une première version de `refs.py` codait en dur les FormID des cibles, de mémoire. Aucun n'était correct (`Butter` supposé à `00F25E`, réel `00353C`). Ils sont désormais relus depuis `rarete.json`, lui-même produit par le scan. À ne jamais supposer.
>
> **L'absence de source a été confirmée par balayage exhaustif.** Conclure « Butter n'a aucun marchand » à partir des seuls `LVLI`/`CONT` serait fragile — un jeu peut distribuer un objet par un mécanisme non regardé. `refs.py` balaye donc **tous les records de tous les plugins** à la recherche du motif binaire du FormID, et rapporte chaque record qui le cite, quel qu'en soit le type. C'est ce balayage qui a révélé la baratte (`FLOR`), les vaches de domaine (`ACHR`) et la recette de farine (`COBJ`) — trois sources qu'aucune des quatre mesures précédentes n'aurait fait apparaître.

Scripts : `annexes/rarete.py` (les quatre mesures), `annexes/sources.py` (traçage des sources), `annexes/refs.py` (balayage exhaustif par FormID). Données : `annexes/rarete.json`, `annexes/sources.json`, `annexes/world.json`.
