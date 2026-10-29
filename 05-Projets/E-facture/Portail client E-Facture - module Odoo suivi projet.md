---
tags: ["e-facture", "odoo", "portail", "module", "suivi-projet", "GLPI", "GA"]
created: 2026-08-16
status: cadrage
---

# Portail client E-Facture — module Odoo de suivi projet

Module Odoo custom (site / portail client) destiné à **GA SAS**, donnant une **vision claire de l'avancement des interfaces E-Facture** (en priorité **INT 280** et **INT 281**), au niveau des **sous-tâches** et des **aller-retour GLPI** — **sans aucune donnée financière**.

## Le besoin

Le client veut suivre **où en est chaque interface** : ce qui est fait, ce qui est en recette, ce qui bloque, et les échanges associés. Aujourd'hui cette information vit dans GLPI (côté client) et dans le projet interne Odoo (côté Globasoft), sans vue consolidée lisible pour GA.

Ce portail est du **suivi projet pur**. Il ne montre **ni commandes, ni factures, ni temps/taux** — ce volet reste traité à part (cf. le tableau de bord de pilotage financier, livrable curé).

## Décisions structurantes

1. **On ne touche PAS au projet interne.** L'E-Facture reste noyée dans le **projet 16 (GA TMA Talend)**, mélangée aux tickets TMA/run. **Pourquoi :** l'organisation actuelle convient mieux à l'équipe ; on ne va pas la refondre pour les besoins d'affichage client.
2. **Le module porte la couche de traduction.** C'est le site/module qui **filtre et remappe** l'interne (désordonné, mélangé) vers une **vue client propre par interface**. Toute la « différence » interne ↔ client est gérée là, pas dans les données de production.
3. **Pas de financier.** Ni `sale.order`, ni `account.move`, ni heures/taux exposés. **Pourquoi :** besoin = avancement ; et le volet commande/facturation est commercialement sensible, on en garde la maîtrise dans un livrable curé.
4. **Module custom, pas le portail natif.** Le partage de projet natif exposerait **tout le projet 16** (donc la TMA) et ne sait **pas regrouper par interface**. Le custom permet de scoper à l'E-Facture et de structurer la vue.
5. **Build sur l'environnement de test** (en cours de montage).

## Périmètre fonctionnel

**Ce que GA voit** (une entrée par interface) :
- **INT 185, INT 187/188, INT 222, INT 280, INT 281**, etc. — libellé client, statut synthétique (ex. *En dev → En recette client → Validé*).
- Le **détail des sous-tâches / points de contrôle** de chaque interface et leur état.
- Les **échanges GLPI** rattachés (aller-retour), ou a minima le lien vers le ticket GLPI.
- Éventuellement des **jalons** (livraison, recette, MEP) par interface.

**Ce que GA ne voit PAS :**
- les tickets **TMA/run** du projet 16,
- les **montants, taux, heures**, commandes, factures,
- les autres clients / projets.

## Architecture technique (module Odoo)

- **Modèle de mapping** (`x_efacture_interface` ou table de config) : pour chaque **interface client**, la liste des **tâches/sous-tâches internes** qui la composent, l'ordre d'affichage, le **libellé client**, et la **règle de dérivation du statut client** à partir de l'étape interne. C'est le cœur du module — le point de vérité de la traduction interne → client.
- **Controller portail** : routes `/my/efacture` (liste des interfaces) et `/my/efacture/<interface>` (détail sous-tâches + échanges). Hérite du portail Odoo (`portal.mixin`), donc auth portail standard.
- **Templates QWeb** : réutiliser le **style du tableau de bord** (charte Globasoft : plum-black `#1B1319`, bleu `#2340E6`, ciel `#60B1E5`, blanc cassé `#F6F5F4`) pour une continuité visuelle.
- **Contrôle d'accès** : utilisateurs **portail de GA uniquement**, via `res.groups` + record rules ; ne remonter que les tâches référencées dans le mapping (jamais un partage de projet en direct).

### Remontée des échanges GLPI — 3 niveaux d'effort
- **Simple** — **alias e-mail** sur les tâches/interfaces : les notifications GLPI arrivent dans le **chatter** de la bonne tâche → affichées dans le portail.
- **Léger** — champ **« N° GLPI »** + lien sortant sur chaque tâche/interface, sans rapatrier le contenu.
- **Lourd** — **synchro API GLPI ↔ Odoo** (bidirectionnelle).

> Recommandation : démarrer en **léger** (réf. + lien) voire **simple** (alias mail), garder l'API pour plus tard si le besoin de bidirectionnel se confirme.

## État actuel des données (au 16/08/2026)

- **INT 280** — Données de paiement : **1 tâche Odoo, ID 878** (projet 16), **70 / 180 h**, étape *En cours*, **aucune sous-tâche**.
- **INT 281** — Contrôle de conformité / facture instantanée vs projet : **pas de tâche Odoo dédiée**, mais **flux très avancé côté technique** (contrôle EN16931, défaut `#BAR#`, multi-fichiers…) — voir [[2026-07-31 INT_281 - Controle de conformite facture instantanee et projet]] et [[Brief IFS - Questions ouvertes flux INT_281]].
- **E-Facture** = sous-ensemble du **projet 16**, sans regroupement par interface natif.
- Correspondance **CRIM ↔ Redmine ↔ GLPI** : table dans [[CRIM_E-Facture_base]].

## Le vrai enjeu à trancher

La clarté du portail dépend d'une **donnée qui n'existe pas encore structurée** (sous-tâches par interface, statut de recette). Le module ne peut pas « inventer » un avancement fin. Deux voies :
- **Dériver un statut synthétique** à partir du peu qui existe (étape + heures conso), grossier mais automatique ;
- ou **tenir une saisie légère en parallèle** : le mapping + un **statut client par interface** maintenu à la main (quelques champs), découplé de l'organisation interne.

→ À arbitrer : jusqu'où on veut du **fin** (sous-tâches réelles) vs du **synthétique tenu à la main**.

## Points ouverts

- Créer **INT 281** comme interface du portail : quel découpage de sous-tâches / points de contrôle exposer côté client ? (ne rien inventer — partir des notes techniques existantes).
- Liste **exhaustive et figée** des interfaces à exposer + leur libellé client.
- Cycle de vie / étapes **client** (vocabulaire à valider avec GA).
- Niveau d'intégration GLPI retenu.

## Prochaines étapes

1. Finaliser le **montage de l'environnement de test** (en cours).
2. Définir le **modèle de mapping** (interface → tâches internes → statut client).
3. Prototyper le **controller + template** `/my/efacture` avec 2 interfaces pilotes : **INT 280** et **INT 281**.
4. Choisir et brancher le **niveau GLPI**.
5. Restreindre l'accès aux **portail users GA** et tester le cloisonnement (aucune fuite TMA/financier).

---

**Notes liées :** [[CRIM_E-Facture_base]] · [[2026-07-31 INT_281 - Controle de conformite facture instantanee et projet]] · [[Brief IFS - Questions ouvertes flux INT_281]] · [[Talend 8 - Pieges techniques et regles apprises]]
