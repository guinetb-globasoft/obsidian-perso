---
tags: ["skyrim", "modding", "brief", "nourriture"]
created: 2026-07-28
---

---
projet: Skyrim
type: brief
tags: ["skyrim", "modding", "brief", "nourriture"]
created: 2026-07-27
statut: en attente d'arbitrage
---

# Brief — mod de nourriture

> Objectif initial : augmenter les effets des aliments et ajouter des recettes de cuisine. L'analyse préalable est faite ([[01-Conflits-Nourriture-Ingredients]]) : **le terrain est libre.** Ce brief pose le cadre technique et liste les décisions à prendre avant de produire quoi que ce soit.

## Feu vert

Aucun mod actif ne surcharge un record de nourriture vanilla. Les 16 ingestibles ajoutés par les mods installés sont tous **nouveaux**. Un plugin de rééquilibrage alimentaire n'écrasera personne et ne sera écrasé par personne.

## Contraintes techniques imposées par le poste

| Contrainte | Conséquence |
|---|---|
| **Skyrim Legendary Edition** | outil = **TES5Edit**, pas SSEEdit. Creation Kit LE si besoin d'interface. |
| **Pas d'ESL** | format introduit par la SE. Le plugin consommera un slot sur les 255. Sans importance ici (29 actifs). |
| **SKSE absent** | pas de SkyUI, donc **pas de MCM**. Aucun réglage en jeu possible : les valeurs seront figées dans le plugin. |
| **Dragonborn non installé** | ne référencer aucun record Solstheim. |
| **Ordre par dates de fichiers** | voir la remise à plat via LOOT ci-dessous. |
| **Aucun mod de survie/besoins** | la nourriture n'a aujourd'hui qu'un rôle de soin d'appoint. Pas de faim à gérer. |

> [!warning] Levier perdu
> `de rerum dirennis.esp` met **tous les poids d'ingrédients à 0**. L'encombrement ne peut plus servir à équilibrer une recette. Restent la **valeur marchande** et la **rareté des composants**.

## Deux gestes de remise en ordre, avant de coder

1. **Désactiver `lightingredients.esp`** — intégralement écrasé par DRD, qui fait tout ce qu'il fait plus 11 rééquilibrages d'effets. Le retirer ne change rien en jeu et supprime le seul conflit susceptible de s'inverser tout seul.
2. **Passer LOOT une fois** — l'ordre actuel est décidé par les dates de fichiers, or les 28 mods ont été écrits dans une fenêtre de **moins d'une minute** le 14 juillet. L'ordre de chargement est donc celui, arbitraire, dans lequel le décompresseur a vidé l'archive. Personne ne l'a choisi.

## Décisions à arbitrer

### 1. Direction du rééquilibrage

| Option | Idée | Effet de bord |
|---|---|---|
| **Généreux** | la nourriture devient une vraie alternative aux potions | dévalue les potions et l'alchimie |
| **Réaliste** | effets faibles mais longs, régénération plutôt que soin sec | demande de la patience, peu visible en combat |
| **Ciblé** | seuls les plats cuisinés deviennent intéressants, les aliments crus restent faibles | valorise la cuisine, cohérent avec l'ajout de recettes |

### 2. Périmètre

- rééquilibrer l'existant seulement ;
- ajouter des recettes seulement ;
- les deux.

### 3. Master HearthFires ?

Les recettes de four viennent de `HearthFires.esm`. S'appuyer dessus est possible (le DLC est installé) mais ajoute une dépendance. Alternative : tout accrocher au **chaudron de cuisine** vanilla, via le mot-clé d'établi `CraftingCookpot`, sans master supplémentaire.

## Méthode de production retenue

1. Créer le plugin dans TES5Edit à partir de `Skyrim.esm`.
2. Copier en override les `ALCH` marqués du drapeau `Food Item` à modifier, ajuster `ENIT` (valeur) et `EFIT` (magnitude, durée).
3. Créer les `COBJ` des nouvelles recettes : composants `CNTO`, produit `CNAM`, quantité `NAM1`, établi `BNAM`.
4. Vérifier le résultat avec `annexes/skyrim_plugin_scan_v2.md` — le plugin doit montrer des `ALCH` en **surcharge** et des `COBJ` en **nouveau**, rien d'autre.
5. Datation du fichier postérieure aux autres mods pour garantir la priorité, ou remise à plat par LOOT.

## Reste ouvert

- [ ] Arbitrer les 3 décisions ci-dessus.
- [ ] Établir la liste nominative des aliments à toucher et leurs valeurs cibles.
- [ ] Définir les recettes : intitulé, composants, produit.

---

Voir [[00-Index]] · [[01-Conflits-Nourriture-Ingredients]] · [[annexes/skyrim_plugin_scan_v2]]
