---
tags: ["skyrim", "modding", "nourriture", "spec", "implementation"]
created: 2026-07-28
---

---
projet: Skyrim
type: spec
tags: ["skyrim", "modding", "nourriture", "spec", "implementation"]
created: 2026-07-28
statut: prêt à saisir
---

# Spec d'implémentation — rééquilibrage de la nourriture

> **19 records `ALCH` en surcharge. Zéro record neuf.** Périmètre : les plats du chaudron de `Skyrim.esm`. Le four HearthFires est hors v1.

## Principe

La nourriture cesse d'être un soin d'appoint pour devenir un **entretien de fond sur la durée**. Les potions gardent l'urgence en combat, la cuisine devient la préparation d'expédition.

**Règle unique : la régénération reflète ce que le plat restaure déjà.** Un plat qui rend santé et vigueur reçoit les deux régénérations, un plat qui ne rend que de la santé n'en reçoit qu'une. Rien à arbitrer au cas par cas.

**Tous les effets instantanés vanilla sont conservés.** La modification est purement additive : on ajoute ou on ajuste la régénération, on porte la durée à 1 080 s.

### La durée : 1 080 s

Les durées `EFIT` sont en secondes réelles, et le `timescale` par défaut vaut 20.

| | Secondes réelles | Heures de jeu |
|---|---:|---:|
| Vanilla | 720 | **4** |
| Cette spec | **1 080** | **6** |

Six heures de jeu — un temps de digestion. Une nuit de sommeil de 8 h consomme intégralement le buff : on se réveille à jeun.

## Les trois `MGEF` à référencer

Aucun à créer. Tous existent dans `Skyrim.esm`.

| EditorID | FormID | Effet |
|---|---|---|
| `FoodRestoreHealthDuration` | `001058A2` | santé, points/seconde |
| `FoodRestoreStaminaDuration` | `001058A3` | vigueur, points/seconde |
| `FoodRestoreMagickaDuration` | `001058A7` | magie, points/seconde |

> [!note] `001058A7` est un effet orphelin
> Défini, nommé, archétype `Value Modifier` sur la valeur d'acteur `Magicka`, structurellement identique à `001058A3` — mais **aucune référence dans tout le load order**. Bethesda l'a créé et ne l'a jamais câblé.
>
> Il devrait fonctionner. Il n'a jamais été testé en conditions réelles. **À vérifier en jeu avant de saisir le reste** : voir la procédure en bas de note.

## Table de saisie

### Ragoûts prolongés — modifier l'existant

| Plat | Régénération cible | Effets instantanés conservés |
|---|---|---|
| **Vegetable Soup** | 3 PV/s · 3 Stam/s | — |
| **Venison Stew** | 3 PV/s · 3 Stam/s | +15 Stamina |
| **Horker Stew** | 3 PV/s · **3 Magicka/s** ⟵ nouvel effet | +15 PV · +15 Stamina |
| ~~Beef Stew~~ | **inchangé** | — |
| ~~Elsweyr Fondue~~ | **inchangée** | — |

Le Horker Stew reçoit une paire `EFID`/`EFIT` supplémentaire pointant vers `001058A7`. C'est le seul plat de la table qui gagne un effet plutôt que d'en voir un ajusté.

### Soupes — ajouter la régénération

**2 PV/s · 2 Stam/s**, durée 1 080.

Apple Cabbage Stew · Cabbage Potato Soup · Clam Chowder · Potato Soup · Tomato Soup

### Viandes — ajouter la régénération

**1 PV/s**, durée 1 080.

Steamed Mudcrab Legs · Cooked Beef · Horker Loaf · Horse Haunch · Leg of Goat Roast · Mammoth Steak · Grilled Chicken Breast · Pheasant Roast · Rabbit Haunch · Salmon Steak · Venison Chop

### Hiérarchie obtenue

| Palier | Débit | Plats |
|---|---|---|
| Ragoûts | 3/s | 3 |
| Soupes | 2/s | 5 |
| Viandes | 1/s | 11 |

Repère : un bandit inflige 10 à 20 par coup, un draugr d'élite 30 à 50. À 3/s on encaisse un adversaire courant sans réagir ; à 1/s on récupère entre deux combats.

## Décisions écartées, et pourquoi

**Beef Stew intouché** — usage personnel nul, aucune raison de le modifier.

**Elsweyr Fondue intouchée** — déjà le meilleur plat du jeu, et son `Eidar Cheese Wheel` est un stock **fini de 337 unités** sans aucune source renouvelable ([[03-Ingredients-Rarete-Approvisionnement]]). La renforcer pousserait à cramer une ressource non reconstituable. Elle sert de plafond.

**Vegetable Soup non pénalisée** — envisagé un temps parce qu'elle est la seule des 33 recettes sans `Salt Pile`. Écarté : elle demande quatre ingrédients comme la Venison Stew, et la Venison Stew garde ses +15 Stamina immédiats. L'écart d'accès relève du style de jeu (ferme contre chasse), pas de la recette.

**Four HearthFires hors périmètre** — les 12 recettes sont verrouillées derrière domaine bâti + baratte + vache + moulin. Les buffer récompenserait un joueur qui n'a plus besoin de rien.

## Répartition des rôles

Deux voies possibles pour produire le plugin. Le choix décide de tout le reste.

| | **Voie manuelle** | **Voie générée** |
|---|---|---|
| Outil | TES5Edit, 19 records à la main | script Python écrivant le `.esp` |
| Durée | 1 à 2 h de saisie | quelques minutes après mise au point |
| Erreurs | fautes de frappe, oublis | systématique — juste ou faux partout |
| Reprise | tout refaire | changer une constante, relancer |
| Validation | l'outil valide en écrivant | ouverture dans TES5Edit obligatoire |

La voie générée est recommandée : la table de cette spec devient un dictionnaire Python, et la table **est** la source de vérité. Un ajustement d'équilibrage après test se fait en changeant un chiffre.

### Ce que fait ce chat

- Arbitrage de conception, spec, ajustements après test
- Écriture et correction des scripts Python (conteneur isolé)
- Écriture dans ce vault
- Lecture des fichiers **texte** du poste, en lecture seule

**Ne peut pas :** rien écrire sur le disque hors vault, ne lit aucun binaire, n'exécute rien sur le poste.

### Ce que fait Claude Code

- **Générer le plugin** — lire les 19 `ALCH` de `Skyrim.esm`, appliquer la table, écrire un `.esp` valide avec `Skyrim.esm` en master
- Sauvegarder `Data/` et le dossier `Saves` avant toute intervention
- Vérifier le résultat avec `skyrim_plugin_scan_v2`
- Désactiver `lightingredients.esp` dans `plugins.txt`
- Réordonner les dates de fichiers — **c'est le mécanisme d'ordre de chargement en LE**
- Itérer sur la table après retour de test

**Ne peut pas :** lancer le jeu, juger un ressenti, piloter l'interface de TES5Edit.

> [!warning] Points de vigilance sur la génération
> **En-tête `HEDR`** — le nombre de records et le prochain FormID disponible doivent être exacts, sinon TES5Edit refuse le fichier.
> **Liste des masters** — calculée, jamais codée en dur. Voir la révision du 28/07 : `Skyrim.esm` **et** `HearthFires.esm`, avec remappage des index sur tous les FormID référencés.
> **Droits d'écriture** — `C:\Program Files (x86)` demande une élévation. Générer ailleurs, copier ensuite.

### Ce que toi seul peux faire

- **Tester en jeu.** Personne d'autre ne peut le faire, et c'est la seule mesure qui compte.
- **Juger l'équilibrage.** 3 PV/s est une hypothèse, pas un résultat. Trop fort, trop faible, bien : seul le jeu répond.
- **Valider dans TES5Edit.** Ouvrir le plugin généré, confirmer que les records s'affichent proprement.
- **Copier dans `Data/`** si l'élévation bloque Claude Code.
- **Trancher.** Toutes les décisions de conception restent les tiennes.

> [!tip] Ce plugin est sûr à ajouter et à retirer en cours de partie
> Uniquement des surcharges `ALCH`, aucun script, aucun record neuf, aucune référence persistante. Rien ne se grave dans la sauvegarde. Tu peux tester, retirer, ajuster, remettre — sans corrompre `Merlin`.
> Sauvegarder le dossier `Saves` reste une précaution de bon sens.

### Enchaînement

1. **Claude Code** — sauvegarde `Data/` et `Saves`
2. **Claude Code** — génère un plugin ne contenant que le Horker Stew
3. **Toi** — valides dans TES5Edit, testes en jeu, vérifies la magie
4. **Claude Code** — génère les 19 records si l'orphelin fonctionne
5. **Toi** — testes, juges l'équilibrage
6. **Ce chat** — ajuste la table selon ton retour
7. **Claude Code** — régénère

L'étape 3 est le point de contrôle. Tant que `001058A7` n'est pas validé en jeu, le reste attend.

## Révision du 28/07 — la couche DLC

Découvert lors de la validation TES5Edit de l'étape 1, invisible au scan.

**`HearthFires.esm` surcharge 6 des 19 plats, et en apporte 4 autres qui n'existent pas dans `Skyrim.esm`.** Ni `Update.esm` ni `Dawnguard.esm` ne touchent aucun de ces records.

| Dernier surchargeur | Plats |
|---|---|
| **HearthFires.esm** — 10 | Vegetable Soup · Venison Stew · Horker Stew · Apple Cabbage Stew · Cabbage Potato Soup · Tomato Soup *(surchargés)* — Clam Chowder · Potato Soup · Steamed Mudcrab Legs · Salmon Steak *(natifs HearthFires)* |
| **Skyrim.esm** — 9 | Cooked Beef · Horker Loaf · Horse Haunch · Leg of Goat Roast · Mammoth Steak · Grilled Chicken Breast · Pheasant Roast · Rabbit Haunch · Venison Chop |

HearthFires n'y touche **ni les effets, ni la valeur, ni le poids** — aucun impact sur l'équilibrage. Il ajoute deux champs :

| Champ | Skyrim.esm | HearthFires |
|---|---|---|
| `OBND` volume de collision | non défini | `(-6,-6,-3)` → `(6,6,2)` |
| `MODS` jeu de textures | absent | un `TXST` par plat, emplacement `Stew:10` |

C'est cohérent avec le DLC : Hearthfire pose de la nourriture en décor dans les domaines, il fallait que les plats se distinguent visuellement et aient un volume pour tenir sur une table.

> [!danger] La régression évitée
> Le premier plugin partait de la version `Skyrim.esm` et se chargeait après HearthFires — il **effaçait** volume de collision et texture. Invisible au scan, qui ne compare pas les champs entre versions. Seule la vue en colonnes de TES5Edit l'a montré.

### Trois règles qui en découlent

**Source = dernier surchargeur**, résolu par l'ordre de chargement. Jamais `Skyrim.esm` par défaut.

**Masters calculés.** Le générateur collecte les origines des records et de tout FormID référencé (`YNAM`, `ZNAM`, `EFID`, `KWDA`, `ENIT`, `MODS`), puis déclare la liste. Ici : `['Skyrim.esm', 'HearthFires.esm']`. Les `TXST` de HearthFires ne sont pas seulement souhaitables — sans le master, la référence est **inexprimable**.

**Identification par la recette gagnante, pas par le nom.** Deux records distincts s'appellent « Salmon Steak » : `skyrim.esm:064B3B` et `hearthfires.esm:003541`. Une seule recette produit un saumon, celle de HearthFires, et elle produit le second. Le générateur s'arrête sur erreur si un nom est ambigu plutôt que de trancher. Le passage `--all` étant passé sans erreur, aucun autre doublon n'existe parmi les 19.

### Conséquence sur le périmètre

L'argument qui écartait les 12 recettes du four en v1 était le **coût du master HearthFires**. Ce coût est désormais payé. Il ne reste que l'argument d'accessibilité — elles sont verrouillées derrière domaine bâti, baratte, vache et moulin. C'est un choix de conception, plus une contrainte technique.

## Procédure

### 1. Tester l'effet orphelin d'abord

Avant de saisir 19 records, valider `001058A7` sur un seul plat.

1. Créer le plugin, surcharger **Horker Stew** seul, y ajouter la paire pointant vers `001058A7`, magnitude 3, durée 1 080.
2. En jeu : cuisiner un Horker Stew, le manger, vider sa magie, observer la remontée.
3. Attendu : environ 3 points par seconde pendant 18 minutes réelles.

Si ça ne remonte pas, l'orphelin est cassé — repli sur le modèle en pourcentage de la Fondue (`FoodFortifyMagickaRate`, `001058A6`).

### 2. Relever le gabarit

Ouvrir **Vegetable Soup** dans TES5Edit. Ses deux paires `EFID`/`EFIT` sont le modèle exact à recopier. Confirmer au passage le FormID santé/durée (`001058A2`).

### 3. Saisir

Pour chaque plat : copier en override depuis `Skyrim.esm`, ajuster ou ajouter les paires `EFID`/`EFIT`, magnitude selon la table, **durée 1 080 partout**.

### 4. Vérifier

```
python skyrim_plugin_scan.py "C:\Program Files (x86)\Steam\steamapps\common\Skyrim\Data" --only <plugin>.esp --details ALCH
```

Attendu : **19 `ALCH` en surcharge, 0 en nouveau, aucun autre type de record.** L'apparition d'un `COBJ`, d'un `MGEF` ou d'un record neuf signale une création accidentelle.

### 5. Ordre de chargement

Aucun mod actif ne surcharge un plat vanilla ([[01-Conflits-Nourriture-Ingredients]]) : la position est indifférente. Passer LOOT une fois pour remettre à plat l'ordre général, qui est aujourd'hui celui, arbitraire, du décompresseur.

## Contexte technique

| Contrainte | Conséquence |
|---|---|
| Skyrim LE | **TES5Edit**, pas SSEEdit |
| Pas d'ESL | un slot consommé sur 255 (29 actifs) |
| SKSE absent | pas de MCM — valeurs figées dans le plugin |
| Dragonborn absent | ne référencer aucun record Solstheim |
| Poids des ingrédients à 0 (DRD) | l'encombrement n'est plus un levier d'équilibrage |

## Pistes v2

- Les 12 recettes du four HearthFires (demande d'ajouter `HearthFires.esm` en master).
- Les plats orphelins — objets existants sans recette, comme la `Cabbage Soup` dont la recette vit dans Dragonborn.
- Ajout de nouvelles recettes (`COBJ`), écarté de la v1 pour n'avoir que des surcharges.

---

Voir [[00-Index]] · [[02-Recettes-Cuisine]] · [[03-Ingredients-Rarete-Approvisionnement]] · [[annexes/skyrim_plugin_scan_v2]]
