---
projet: Skyrim
type: référence
tags: ["skyrim", "modding", "cuisine", "recettes", "artisanat", "bonus"]
created: 2026-07-27
updated: 2026-07-27
---

# Recettes de cuisine et bonus des plats

> **21 recettes au chaudron** + **12 au four** (HearthFires), soit 33 plats, avec leurs effets réels. Toutes viennent de `Skyrim.esm` et `HearthFires.esm` : **aucun mod actif n'ajoute ni ne modifie de recette ou de plat**. Liste établie sur l'ordre de chargement réel, surcharges résolues.

## Ce qu'il faut retenir

La cuisine se divise en deux familles, et c'est la seule distinction qui compte vraiment :

- **Les plats à effet instantané** — la grande majorité. Ils rendent 2 à 15 points, une fois. Intérêt marginal : une potion mineure fait mieux.
- **Les 5 plats à effet prolongé du chaudron** (720 s = **12 minutes**). Ce sont les seuls qui changent quelque chose. Un effet « 1/s pendant 720 s » représente **≈ 720 points régénérés** sur la durée — sans commune mesure avec le reste.

Le meilleur plat du jeu est l'**Elsweyr Fondue** : +100 Magicka et +25 % de régénération de magie pendant 12 minutes. Pour un mage, c'est l'équivalent d'un buff permanent tant qu'on pense à en cuisiner. Ingrédients rares en revanche (Moon Sugar).

Côté four, **Garlic Bread** est le meilleur rapport qualité/prix : il **soigne les maladies**, coûte trois ingrédients communs et sort **par 2**.

## Au chaudron — 21 recettes

Disponibles à n'importe quel chaudron ou broche de cuisson (mot-clé `CraftingCookpot`), partout en Bordeciel.

### Les 5 plats à effet prolongé — les seuls qui comptent

| Plat | Effets | Ingrédients |
|---|---|---|
| **Elsweyr Fondue** | **+100 Magicka** · **+25 % régén. Magicka** — 12 min | Eidar Cheese Wheel · Moon Sugar · Ale |
| **Beef Stew** | **+25 Stamina** · **+1 Stamina/s** — 12 min | Raw Beef · Carrot · Salt Pile · Garlic |
| **Horker Stew** | +15 PV · +15 Stamina *(instantané)* · **+1 PV/s** — 12 min | Lavender · Tomato · Garlic · Horker Meat |
| **Venison Stew** | +15 Stamina *(instantané)* · **+1 PV/s** · **+1 Stamina/s** — 12 min | Venison · Salt Pile · Potato · Leek |
| **Vegetable Soup** | **+1 PV/s** · **+1 Stamina/s** — 12 min | Cabbage · Potato · Leek · Tomato |

> [!tip] Vegetable Soup — le meilleur choix pratique
> Régénération double (santé **et** vigueur) pendant 12 minutes, et **c'est la seule recette du jeu qui ne demande pas de Salt Pile** : quatre légumes de ferme, tous cultivables et achetables en masse. Le Salt Pile est le goulot d'étranglement de la cuisine (15 recettes sur 21 en consomment), s'en passer change tout pour un usage régulier.
>
> `Venison Stew` fait la même chose en ajoutant +15 Stamina immédiat, mais réclame du Salt Pile et de la venaison.

### Les 16 plats à effet instantané

| Plat | Effets | Ingrédients | Valeur · Poids |
|---|---|---|---|
| Apple Cabbage Stew | +15 Stamina · +10 PV | Salt Pile · Red Apple · Cabbage | 8 · 0,5 |
| Cabbage Potato Soup | +10 PV · +10 Stamina | Potato · Salt Pile · Leek · Cabbage | 5 · 0,5 |
| Clam Chowder | +10 PV · +10 Stamina | Clam Meat · Potato · Jug of Milk · Butter | 5 · 0,5 |
| Potato Soup | +10 PV · +10 Stamina | Potato · Salt Pile | 5 · 0,5 |
| Tomato Soup | +10 PV · +10 Stamina | Tomato · Salt Pile · Garlic · Leek | 5 · 0,5 |
| Steamed Mudcrab Legs | +12 PV | Mudcrab Legs · Butter | 4 · 0,1 |
| Cooked Beef | +10 PV | Salt Pile · Raw Beef | 5 · 0,5 |
| Horker Loaf | +10 PV | Salt Pile · Horker Meat | 4 · 1 |
| Horse Haunch | +10 PV | Salt Pile · Horse Meat | 4 · 2 |
| Leg of Goat Roast | +10 PV | Salt Pile · Leg of Goat | 4 · 1 |
| Mammoth Steak | +10 PV | Salt Pile · Mammoth Snout | 8 · 2 |
| Grilled Chicken Breast | +5 PV | Salt Pile · Chicken Breast | 4 · 0,2 |
| Pheasant Roast | +5 PV | Pheasant Breast · Salt Pile | 4 · 0,2 |
| Rabbit Haunch | +5 PV | Salt Pile · Raw Rabbit Leg | 3 · 0,1 |
| Salmon Steak | +5 PV | Salt Pile · Salmon Meat | 4 · 0,1 |
| Venison Chop | +5 PV | Salt Pile · Venison | 5 · 2 |

Les viandes simples suivent toutes le même schéma `Salt Pile + viande crue` pour +5 ou +10 PV. **Aucun intérêt hors dépannage** : `Potato Soup` rend autant de PV *et* 10 Stamina pour deux ingrédients de ferme. Noter que `Mammoth Steak`, `Horse Haunch` et `Venison Chop` pèsent **2 unités** pour un effet identique aux versions à 0,1 — à ne pas transporter.

## Au four — 12 recettes

⚠️ **Nécessite HearthFires et un four construit.** Le four n'existe que dans les maisons Hearthfire (Lakeview Manor, Windstad Manor, Heljarchen Hall) : il faut d'abord bâtir l'aile intérieure correspondante. Ces recettes sont **invisibles au chaudron**, elles ont leur propre station (`BYOHCraftingOven`).

| Plat | Effets | Ingrédients |
|---|---|---|
| **Garlic Bread (×2)** | +1 PV · **Soigne les maladies** | Garlic · Butter · Bread |
| **Lavender Dumpling** | +5 PV · **+10 Magicka** · **+10 % résist. magie** — 60 s | Moon Sugar · Sack of Flour · 2× Snowberries · Lavender |
| **Chicken Dumpling** | +15 PV · **+1 PV/s** — 120 s | Salt Pile · Sack of Flour · Chicken Breast · Garlic · Leek |
| Snowberry Crostata | +10 PV · +4 % résist. feu — 60 s | Butter · 2× Snowberries · Sack of Flour |
| Jazbay Crostata | +10 PV · +4 Magicka — 60 s | Butter · 2× Jazbay Grapes · Sack of Flour |
| Juniper Berry Crostata | +4 PV · +2 PV/s — 60 s | Butter · 3× Juniper Berries · Sack of Flour |
| Apple Dumpling | +5 PV · +5 Archerie — 60 s | Sack of Flour · Green Apple · Red Apple |
| Braided Bread | +2 PV · +5 Charge — 30 s | Salt Pile · Sack of Flour |
| Apple Pie | +10 PV | Salt Pile · Sack of Flour · Butter · Chicken's Egg · 2× Green Apple · 2× Red Apple |
| Sweet Roll | +5 PV | Salt Pile · Jug of Milk · Sack of Flour · Butter · Chicken's Egg |
| Potato Bread | +3 PV | Salt Pile · Jug of Milk · Sack of Flour · Potato · Chicken's Egg |
| Bread | +2 PV | Salt Pile · Jug of Milk · Sack of Flour · Chicken's Egg |

Le four est la **seule source d'effets exotiques** de toute la cuisine : soin des maladies, résistance magique, résistance au feu, bonus d'archerie, bonus de charge. Le chaudron ne fait que santé, vigueur et magie.

En contrepartie les durées sont courtes (30 à 120 s contre 720 s au chaudron) et les ingrédients spécifiques — **Sack of Flour**, **Butter**, **Jug of Milk** — s'achètent chez les marchands d'alimentation ou se trouvent dans les fermes, ils ne sont **pas ramassables dans la nature**.

`Apple Pie` et `Sweet Roll` demandent 5 à 7 ingrédients pour +10 et +5 PV : à ignorer, ce sont des recettes de décor.

**Chaînage :** `Bread` (four) → `Garlic Bread` (four). C'est la seule recette qui consomme le produit d'une autre, et la seule qui produit 2 unités.

### Construire le four

Ce n'est pas une recette de cuisine mais elle vit dans la même table (`COBJ`) :

| Élément | Matériaux |
|---|---|
| Oven (aile intérieure Hearthfire) | 2× Clay · 3× Quarried Stone |

## L'effet manquant : pourquoi aucun plat ne régénère la magie au point/seconde

Santé et vigueur ont chacune un effet de régénération **par point et par seconde** utilisé par les ragoûts. La magie, non — et ce n'est pas un oubli de conception : **l'effet existe, il n'a simplement jamais été branché.**

| EditorID | FormID | Archétype | Valeur d'acteur | Utilisé par |
|---|---|---|---|---|
| `FoodRestoreHealthDuration` | `001058A2` | Peak Value Modifier | *(AV 155)* | 8 records |
| `FoodRestoreStaminaDuration` | `001058A3` | Value Modifier | Stamina | 6 records |
| `FoodFortifyMagickaRate` | `001058A6` | Peak Value Modifier | *(AV 156)* | 3 records |
| **`FoodRestoreMagickaDuration`** | **`001058A7`** | **Value Modifier** | **Magicka** | **aucun — 0 référence** |
| `FoodFortifyMagicka` | `001058A8` | Peak Value Modifier | Magicka | 3 records |

`FoodRestoreMagickaDuration` est **structurellement identique** à `FoodRestoreStaminaDuration` : même archétype `Value Modifier`, même mécanique à durée, la valeur d'acteur près. Or ce dernier produit bien du 1 point/seconde dans `Vegetable Soup`, `Venison Stew` et `Beef Stew`.

Mais un balayage exhaustif de toute référence à son FormID, sur les 29 plugins actifs, ne remonte **zéro record** — ni `ALCH`, ni `SCRL`, ni quoi que ce soit. C'est un effet orphelin.

Les FormID sont consécutifs (`…A2`, `…A3`, `…A6`, `…A7`, `…A8`) : le bloc a été créé d'un seul tenant, et `…A7` est le seul à n'avoir jamais été câblé. À la place, l'`Elsweyr Fondue` utilise `FoodFortifyMagickaRate`, une régénération **en pourcentage**, pas en points.

> [!note] Exploitable pour un mod
> Un mod voulant un plat « +1 Magicka/s pendant 12 min », symétrique des ragoûts existants, n'a **pas besoin de créer un nouveau `MGEF`** : il suffit de référencer `001058A7` dans un `ALCH`. L'effet est déjà défini, nommé (« Restore Magicka ») et fonctionnel.

## Portée et vérifications

- **Aucun mod n'intervient.** Sur les 29 plugins actifs, aucun n'ajoute ni ne surcharge une recette de cuisine ou un plat. `hg.esp` et `quest_seaofghosts.esp` ajoutent bien de la nourriture ([[01-Conflits-Nourriture-Ingredients]]), mais en objets ramassables ou marchands, **sans recette associée**.
- **HearthFires surcharge 9 plats vanilla** (`Cooked Beef`, `Salmon Steak`, etc.) — vérification faite champ par champ : **il en recopie les effets, valeurs et poids à l'identique**. Aucun impact sur les chiffres ci-dessus.
- **`Salmon Steak` est la seule recette en conflit** : `Skyrim.esm` et `HearthFires.esm` définissent tous deux `RecipeFoodSalmonCooked`. HearthFires charge après et l'emporte, mais les deux versions sont identiques. Elle n'apparaît qu'une fois au chaudron.
- **Dragonborn n'est pas installé**, donc pas de recettes Solstheim (Ash Yam, etc.).
- Sur les **1 274 recettes `COBJ`** du jeu, seules 34 relèvent d'une station de cuisine (33 plats + le four à construire). Le reste est forge, tannerie, établi et fabrication de maisons Hearthfire.

## Annexe — méthode

Scan de référence lancé comme demandé :

```
python skyrim_plugin_scan.py "C:\Program Files (x86)\Steam\steamapps\common\Skyrim\Data" \
    --only skyrim.esm --details COBJ
```

Ce scan seul ne suffit pas, pour quatre raisons — d'où les scripts `annexes/cuisine.py` et `annexes/bonus.py` :

1. **Le poste de travail n'est pas affiché.** `describe_cobj()` lit bien `BNAM` dans `out["bench"]`, mais `format_details()` ne l'imprime jamais. Sans lui, les 1 274 `COBJ` sortent en vrac, impossible de distinguer cuisine et forge. Le filtrage se fait sur les mots-clés `CraftingCookpot` / `BYOHCraftingOven`, repérés dynamiquement parmi les `KYWD` plutôt que codés en dur.
2. **`--only skyrim.esm` rate la moitié des recettes.** 16 des 33 viennent de `HearthFires.esm`, dont les 12 recettes de four.
3. **Les noms d'objets ne sont pas résolus** : le scan affiche `<localise>` ou des FormID bruts.
4. **Les bonus ne sont pas dans la recette.** Une `COBJ` ne dit que « tel objet est produit ». Les effets vivent dans le record `ALCH` du plat, qui pointe lui-même vers des records `MGEF` pour le nom de l'effet. Il faut donc une triple jointure `COBJ → ALCH → MGEF`, les trois avec résolution de surcharge.

> [!warning] Piège de résolution des noms — vérifié et corrigé
> Les identifiants de chaîne sont **locaux à chaque plugin**. Une première passe fusionnant les tables produisait des absurdités crédibles : *Clam Chowder* apparaissait avec « Orcish Shield of Dwindling Fire » en ingrédient, *Potato Soup* s'appelait « The Kinect has failed to initialize ». Il faut une table **par plugin**, jamais fusionnée.
>
> Complication supplémentaire : `Data\Strings` ne contient que `Skyrim_English` et `Update_English`. Les tables de Dawnguard et HearthFires sont **empaquetées dans leur `.bsa`** — d'où le lecteur d'archives `annexes/bsa.py` (format BSA v104), qui les extrait à la volée.

Les magnitudes et durées sont lues telles quelles dans les sous-records `EFIT` (magnitude `float`, durée en secondes). Un effet de type `FoodRestoreHealthDuration` de magnitude 1 sur 720 s correspond à 1 point par seconde ; le total de ≈ 720 points cité plus haut est une déduction de cette lecture, pas une valeur stockée dans le fichier.
