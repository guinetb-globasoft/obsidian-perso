---
projet: Skyrim
type: index
tags: ["skyrim", "modding", "index"]
created: 2026-07-27
---

# Skyrim — Index du projet

> Projet de suivi du modding Skyrim : analyse des plugins installés, conflits entre mods, ordre de chargement.

## Contexte technique

| Élément | Valeur |
|---|---|
| Jeu | **Skyrim Legendary Edition** (dit « Oldrim », 2011) — *pas* Special Edition |
| Dossier `Data` | `C:\Program Files (x86)\Steam\steamapps\common\Skyrim\Data` |
| Fichier des actifs | `C:\Users\Shadow\AppData\Local\Skyrim\plugins.txt` |
| Plugins sur le disque | 36 (`.esp` / `.esm`) |
| Plugins actifs | 29 (dont 4 vanilla) |
| Plugins inactifs | 7 |
| DLC installés | Dawnguard, HearthFires (**pas** Dragonborn) |

### Comment on sait que c'est la LE et pas la SE

Cinq indices concordants, tous vérifiés sur le poste :

1. `plugins.txt` n'a **aucun préfixe `*`** — la SE l'exige pour marquer les plugins actifs ;
2. **aucun fichier `.esl`** dans `Data` — format exclusif à la SE ;
3. `Skyrim.esm` et `Update.esm` sont **absents** de `plugins.txt` — convention LE (actifs implicitement) ;
4. présence de `HighResTexturePack01/02/03.esp` — DLC HD officiel LE, intégré d'office dans la SE ;
5. chemin `steamapps\common\Skyrim` et non `Skyrim Special Edition`.

Cette distinction n'est pas cosmétique : **elle change la règle qui détermine l'ordre de chargement**, donc qui gagne un conflit. Voir [[01-Conflits-Nourriture-Ingredients]].

## Outillage

- `C:\Users\Shadow\Downloads\skyrim_plugin_scan.py` — parseur TES4/TES5 sans dépendance, inventorie les records par plugin et détaille ALCH / INGR / COBJ / MISC.
- Scripts d'appoint dans `annexes/`, réutilisables tels quels :
  - `crossref.py` — rejoue le scan et résout chaque record en clé canonique `master:id_local` + calcule l'ordre de chargement réel ;
  - `analyse.py` — sort la liste des conflits et le gagnant de chacun ;
  - `pairs.py` — overlaps mod-contre-mod et contrôle des dépendances de masters ;
  - `diff_ingr.py` — comparaison fine poids / valeur / effets entre deux mods d'ingrédients ;
  - `cuisine.py` — recettes filtrées par poste de travail, noms résolus, surcharges tranchées ;
  - `bonus.py` — jointure `COBJ → ALCH → MGEF` : ce que chaque plat apporte réellement ;
  - `diff_hf.py` — compare les plats vanilla à leur version surchargée par HearthFires ;
  - `bsa.py` — lecteur d'archives BSA v104, pour extraire les `.STRINGS` des DLC.

### Deux pièges à connaître (valables pour toute analyse future)

1. **Les FormID ne sont pas comparables entre plugins** — ils sont relatifs à la liste de masters de chaque fichier. Toujours passer par une clé `master_origine:id_local` (voir `crossref.py`).
2. **Les identifiants de chaîne sont locaux à chaque plugin** — fusionner les tables `.STRINGS` produit des noms faux et crédibles, donc difficiles à repérer. Une table par plugin (voir `cuisine.py`). Les tables des DLC ne sont pas dans `Data\Strings` mais dans leur `.bsa`.

## Notes du projet

- [[01-Conflits-Nourriture-Ingredients]] — qui surcharge quoi côté nourriture / ingrédients / recettes, et qui gagne au final.
- [[02-Recettes-Cuisine]] — les 33 recettes de cuisine du jeu (21 au chaudron, 12 au four) et le bonus de chaque plat.
- [[03-Ingredients-Rarete-Approvisionnement]] — rareté mesurée des 33 ingrédients et difficulté réelle d'obtention.

## Annexes

- `annexes/scan-brut-skyrim_plugin_scan.txt` — sortie complète du scan (33 plugins).
- `annexes/conflits-detail-102-records.txt` — les 102 conflits, un par un, avec le gagnant.
- `annexes/scan-brut-cobj-skyrim-esm.txt` — scan `COBJ` de `Skyrim.esm`.
- `annexes/cuisine.json` — les recettes de cuisine en JSON exploitable.

## À faire / pistes

- [ ] Étendre l'analyse à d'autres types de records (armes `WEAP`, armures `ARMO`, `LVLI` listes de butin) — plusieurs mods d'équipement cohabitent.
- [ ] Décider du sort des 7 plugins inactifs (désinstaller ou activer).
- [ ] Statuer sur `lightingredients.esp`, redondant en l'état.
