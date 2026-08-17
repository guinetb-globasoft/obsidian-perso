---
projet: Skyrim
type: analyse
tags: ["skyrim", "modding", "conflits", "alchimie", "ordre-de-chargement"]
created: 2026-07-27
---

# Conflits nourriture / ingrédients — qui gagne au final

> Croisement du scan des 33 plugins de `Data` avec l'ordre de chargement réel. **102 records ALCH/INGR/COBJ sont disputés.** Le résultat est globalement sain, mais il repose sur un ordre de chargement fragile — et un mod sur deux du duel principal ne sert plus à rien.

## TL;DR

1. **Aucun record de nourriture vanilla n'est surchargé** par un mod actif. Tout ce que les mods ajoutent côté nourriture, ce sont de *nouveaux* objets. Zéro risque de ce côté.
2. Le seul vrai conflit est sur les **ingrédients d'alchimie** : `lightingredients.esp` et `de rerum dirennis.esp` se disputent **exactement les mêmes 94 ingrédients**.
3. **`de rerum dirennis.esp` gagne**, et c'est le bon résultat : il contient tout ce que fait `lightingredients` (poids à 0) *plus* 11 rééquilibrages d'effets. `lightingredients.esp` est **totalement redondant**.
4. ⚠️ **Ce résultat tient à un fil.** L'ordre dans `plugins.txt` donnerait le gagnant inverse. Voir la section sur l'ordre de chargement — c'est le point à retenir.

## Point de méthode : `plugins.txt` n'est pas l'ordre de chargement

C'est le piège de cette analyse, et il change la réponse.

Sur **Skyrim LE**, `plugins.txt` ne fait que lister *quels* plugins sont actifs. L'**ordre de chargement est déterminé par la date de modification des fichiers `.esp`/`.esm`** sur le disque. (C'est la SE qui a introduit l'ordre par `plugins.txt` avec les préfixes `*`.) Les indices confirmant qu'on est bien en LE sont dans [[00-Index]].

Or ici **les deux ordres divergent sur 25 plugins sur 29**. `plugins.txt` est trié à peu près alphabétiquement, le disque reflète l'ordre d'installation. Extrait des écarts les plus lourds de conséquence :

| Plugin | Rang réel (disque) | Rang dans `plugins.txt` |
|---|---|---|
| `lightingredients.esp` | **6** | 15 |
| `de rerum dirennis.esp` | **11** | 7 |
| `adalmatar.esp` | 18 | 4 |
| `betterdarkbrotherhood.esp` | 28 | 5 |
| `thefrontier.esp` | 9 | 25 |
| `dragonsoulstoperks.esp` | 27 | 10 |

Sur les deux mods d'ingrédients, l'inversion est totale : **en ordre réel DRD gagne, en ordre `plugins.txt` ce serait `lightingredients`**. Comme `lightingredients` ne fait que remettre les poids à 0 sans les rééquilibrages d'effets, ce scénario ferait **perdre silencieusement les 11 buffs d'effets de DRD**.

> [!warning] Conséquence pratique
> Tant que l'ordre repose sur les dates de fichiers, il est à la merci de n'importe quelle opération qui les réécrit : réinstallation, copie, restauration de sauvegarde, `touch` d'un gestionnaire de mods, synchro cloud. Un simple re-téléchargement de `lightingredients.esp` le ferait passer en dernier et annulerait DRD.

### Ordre de chargement réel (dates de fichiers)

```
 0  Skyrim.esm                              15  quest_andtherealmsofdaedra.esp
 1  Update.esm                              16  quest_sorcery.esp
 2  Dawnguard.esm                           17  extra encounters - hsr.esp
 3  HearthFires.esm                         18  adalmatar.esp
 4  moredragonloot.esp                      19  quest_pitfighter.esp
 5  enchanting extraeffect.esp              20  lighter_mining_smithing_materials.esp
 6  lightingredients.esp                    21  weir_weightlessgems.esp
 7  dk_armor_by_hothtrooper44.esp           22  guard dialogue overhaul.esp
 8  more dragons.esp                        23  hg.esp
 9  thefrontier.esp                         24  dragonboneweaponscomplete.esp
10  de rerum dirennis - dawnguard.esp       25  thedomain.esp
11  de rerum dirennis.esp                   26  faster vanilla horses.esp
12  quest_seaofghosts.esp                   27  dragonsoulstoperks.esp
13  quest_thebiggertheyare.esp              28  betterdarkbrotherhood.esp
14  quest_nomercy.esp
```

## Le duel principal : 94 ingrédients

`lightingredients.esp` (#6) et `de rerum dirennis.esp` (#11) surchargent **le même jeu de 94 ingrédients vanilla**, ni plus ni moins. Comparaison champ par champ :

| Critère | Résultat |
|---|---|
| Poids identiques | **94 / 94** (les deux mettent tout à `0`) |
| Valeurs marchandes identiques | **94 / 94** |
| Effets identiques | 83 / 94 |
| Effets où DRD s'écarte du vanilla | **11** |

Autrement dit, sur les 11 ingrédients qui les séparent, `lightingredients` recopie les effets vanilla tandis que DRD les rééquilibre. Exemples (`MGEF`, magnitude, durée) :

| Ingrédient | Effet modifié | Vanilla & `lightingredients` | `de rerum dirennis` |
|---|---|---|---|
| `DaedraHeart` | `00073F20` | magnitude **1.0** / 30 s | magnitude **4.0** / 30 s |
| `FalmerEar` | `00073F29` | magnitude **1.0** / 10 s | magnitude **4.0** / 10 s |
| `HagravenFeathers` | `00073F29` | magnitude **1.0** / 10 s | magnitude **4.0** / 10 s |
| `TrollFat` | `00073F29` | magnitude **1.0** / 10 s | magnitude **4.0** / 10 s |

**DRD est un sur-ensemble strict de `lightingredients`.** Il gagne, rien n'est perdu, et `lightingredients.esp` ne contribue plus rien au jeu final : ses 94 records sont tous écrasés par des données identiques ou meilleures.

## Bilan des gagnants

| Plugin | Records remportés | Détail |
|---|---|---|
| `de rerum dirennis.esp` (#11) | **96** | `INGR` = 94, `ALCH` = 2 |
| `de rerum dirennis - dawnguard.esp` (#10) | **5** | `INGR` = 5 |
| `quest_thebiggertheyare.esp` (#13) | **1** | `COBJ` = 1 |

### Les 2 `ALCH` disputés — sans enjeu

Les seuls ingestibles vanilla surchargés sont deux records techniques, pas de la vraie nourriture. DRD y ramène juste le poids de `0.5` à `0` :

- `DefaultPoison` — `skyrim.esm:05629E`
- `Unknown Potion` — `skyrim.esm:05661F`

### Les 5 `INGR` Dawnguard

`de rerum dirennis - dawnguard.esp` surcharge 5 ingrédients de `Dawnguard.esm`, **sans concurrent** (`lightingredients` n'a pas Dawnguard en master, il ne peut pas les toucher) :

`DLC1MountainFlower01Yellow` · `DLC01PoisonBloom` · `DLC01ChaurusHunterAntennae` · `DLC01GlowPlant01Ingredient` · `DLC01MothWingAncestor`

> [!note] Fausse alerte vérifiée
> Ce patch Dawnguard charge en #10, *avant* `de rerum dirennis.esp` en #11 — ce qui ressemble à un patch mal placé. Vérification faite sur ses masters : ils valent `Skyrim.esm, Update.esm, Dawnguard.esm`, **sans** `de rerum dirennis.esp`. Les deux plugins sont indépendants et ne se recouvrent sur aucun record. Leur ordre relatif est donc sans effet. Aucune dépendance de master n'est violée dans tout le load order.

### Le seul `COBJ` disputé

`TemperWeaponSkyforgeGreatsword` (`skyrim.esm:000E4B`) — `quest_thebiggertheyare.esp` (#13) surcharge la recette d'amélioration vanilla. Aucun autre mod ne la touche.

## Nourriture : aucun conflit, que des ajouts

Aucun mod actif ne surcharge un record de nourriture vanilla. Les 16 ingestibles/ingrédients ajoutés par les mods sont tous **nouveaux** :

| Plugin | Type | Objet | Valeur |
|---|---|---|---|
| `quest_seaofghosts.esp` (#12) | nourriture | `tos_Sujamma` | 100 |
| | potion | `tos_PadomaicFlowerEssence01` / `03` | 30 |
| | médicament | `tos_PadomaicFlowerEssence02` | 30 |
| `quest_thebiggertheyare.esp` (#13) | poison | `tos_GiantPoison` | 512 |
| `hg.esp` (#23) | nourriture | `FoodAnvilRivercrabmeat` | 3 |
| | nourriture | `Food_Anvil_hyenaMeat` | 3 |
| | poison | `Anvil_PoisonbiteVenom` | 1249 |
| | poison | `Food_Anvil_hyenaMeatpoison` | 3 |
| | ingrédient | `AnvilGuartooth`, `Anvil_rivercrabChitin`, `Anvil_siligonder_egg`, `anvilGuareyeball` | 2 – 23 |
| `betterdarkbrotherhood.esp` (#28) | nourriture | `BDBFoodApplePoison` | 300 |
| | nourriture | `FoodRum` | 420 |
| | potion | `BDBHumanBlood` | 1 |

## Plugins installés mais inactifs

Sept plugins sont dans `Data` mais absents de `plugins.txt` : **ils ne chargent pas et n'ont aucun effet en jeu.**

| Plugin | Taille | Ce qu'on perd |
|---|---|---|
| `shenkthieveryoverhaul.esp` | 1,0 Mo | 9 779 records dont **407 surcharges** — refonte complète du vol, inactive |
| `improvedskillbooks.esp` | 680 Ko | 90 records, **90 surcharges** — inactif |
| `silencers vestments.esp` | 6,0 Ko | 22 records (tous nouveaux) |
| `HighResTexturePack01/02/03.esp` | 66 o chacun | DLC textures HD officiel |
| `lockpickvision.esp` | 66 o | — |

Les deux premiers sont des mods substantiels installés pour rien. À activer ou à désinstaller — mais **attention** : activer `shenkthieveryoverhaul.esp` (407 surcharges) demanderait de refaire cette analyse, il touche beaucoup de records.

## Recommandations

1. **Fiabiliser l'ordre de chargement.** C'est le point critique. Passer par LOOT (qui réécrit les timestamps dans un ordre cohérent) plutôt que de dépendre de dates d'installation fortuites. Sans ça, le résultat actuel peut s'inverser à la prochaine manipulation de fichiers.
2. **Désactiver `lightingredients.esp`.** Il est intégralement écrasé par DRD, qui fait tout ce qu'il fait en mieux. Le retirer ne change rien en jeu, supprime un slot de plugin, et surtout **élimine le risque d'inversion** décrit plus haut. C'est le geste le plus rentable de la liste.
3. **Statuer sur les 7 plugins inactifs**, en particulier les deux gros.
4. **Étendre le scan** aux `WEAP` / `ARMO` / `LVLI` : plusieurs mods d'équipement et de butin cohabitent (`dragonboneweaponscomplete`, `dk_armor_by_hothtrooper44`, `moredragonloot`, `thedomain`…) et n'ont pas été croisés ici.

## Annexe — méthode

Scan de référence lancé comme demandé :

```
python skyrim_plugin_scan.py "C:\Program Files (x86)\Steam\steamapps\common\Skyrim\Data" \
    --skip-vanilla --details ALCH,INGR,COBJ
```

33 plugins parsés, **aucune erreur de lecture**.

Deux limites du script ont dû être contournées pour le croisement :

- **Les FormID affichés ne sont pas comparables entre plugins.** Ils sont relatifs à la liste de masters de chaque plugin (l'octet de poids fort est un index dans cette liste). `scan_plugin()` résout bien le master d'origine dans `info["source"]`, mais `format_details()` ne l'imprime jamais. Le croisement a donc été refait en réutilisant le parseur pour reconstruire une clé canonique `master_origine:id_local`.
- **`--skip-vanilla` exclut les records de référence.** Les quatre `.esm` vanilla ont été re-scannés séparément pour disposer des valeurs de base à comparer.

La détection « nourriture » repose sur le drapeau `ENIT_FOOD_ITEM` (`0x02`) des records `ALCH`, qui est bien le mécanisme vanilla : dans Skyrim la nourriture n'est pas un type de record distinct, c'est un ingestible marqué par ce drapeau.
