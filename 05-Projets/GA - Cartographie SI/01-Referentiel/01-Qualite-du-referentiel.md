---
titre: Qualité du référentiel applicatif
statut: analysé
date: 2026-08-13
tags: [referentiel, qualite-donnees, inventaire, cartographie]
---

# Qualité du référentiel — `INVENTAIRE - Applicatifs Métier.xlsx`

> **Conclusion en une phrase** : le référentiel est **assez riche pour produire les deux
> cartos demandées**, mais **pas assez réconcilié pour les générer automatiquement**
> sans une passe de nettoyage. Les 3 chantiers ci-dessous sont le prix à payer pour
> passer d'une carto « dessinée à la main » à une carto **régénérable**.

## 1. Volumétrie réelle

| Objet | Compte | Commentaire |
|---|---|---|
| Applications inventoriées | **150** | cohérent avec l'onglet `STATS` |
| Lignes de flux | **250** | ≠ 250 interfaces : une interface = souvent plusieurs lignes (une par donnée transmise) |
| Flux **actifs** | **61** | valeur affichée dans `STATS`, reprise slide 6 du support |
| Flux **vivants** (actifs + à venir + en construction) | **132** | 61 actifs + 36 « actif, à disparaître » + 28 « à venir » + 5 « en construction » + 2 « à prévoir » |
| Flux décommissionnés | 47 | à exclure des cartos |
| Lignes **sans statut** | 70 | angle mort : ni actives ni décommissionnées |

> ⚠️ **Le chiffre « ≈60 flux » de la slide 6 sous-estime la réalité vue du projet ERP.**
> 61 = les flux *actifs aujourd'hui*. Le SI cible en compte **132 vivants**, dont
> 28 « à venir » majoritairement portés par le lot 4 IFS (Infor Syteline → IFS, Nibelis → IFS,
> Expensya → IFS…). À arbitrer avec Gildvin : communiquer 61 (photo) ou 132 (trajectoire).

## 2. Complétude des colonnes (sur 150 apps)

| Colonne | Renseignée | Impact carto |
|---|---|---|
| `ID Archi` | 140/150 | **26 identifiants non conformes** au format `id-<uuid>` (voir §4) |
| Description | 138/150 | libellés de carto |
| Responsable applicatif DSI | 141/150 | vue RACI (slides 7/15) |
| Service métier propriétaire | 130/150 | **base de la strate fonctionnelle** |
| Type d'hébergement | 124/150 | vue technique (hors périmètre) |
| Éditeur / intégrateur | 127/150 | — |
| **Statut d'utilisation** | **64/150** | ⚠️ le plus lacunaire : impossible de distinguer sûrement ce qui est vivant de ce qui est mort |

Côté flux (sur les 132 vivants), les colonnes techniques sont très peu remplies :
protocole **26/132**, mode de déclenchement **32/132**, format **21/132**, fréquence **19/132**.
→ **Une vue applicative détaillée (protocole/fréquence par flux) n'est pas produisible
aujourd'hui.** La vue applicative se limite donc à : *qui échange quoi avec qui, dans quel sens,
avec quel statut*.

## 3. Réconciliation FLUX ↔ APPS — le point bloquant

Les onglets `APPS` et `FLUX` **ne partagent pas le même référentiel de noms**. Sur les flux vivants :

**14 libellés d'extrémité n'existent pas dans l'inventaire applicatif :**

`Sage Signature` (4×) · `SAV` (2×) · `IntraNews & MyGapeo` (2×) · `ViaReport` · `InfoLégal` ·
`Proweb` · `Deplacements` · `Portail RH benify` · `ZyLab (ZyScan, ZyTimer, ZyIndex)` · `Excel` ·
`Hercule` · `ICS Compta` · `Innovorder` · `API Resto`

Trois cas distincts, trois traitements :

1. **Alias d'une app existante** → à normaliser dans l'Excel :
   `Sage Signature` = `Sage XRT Signature` · `Hercule` = `Hercule PRO` ·
   `ICS Compta` = `ICS / Comfact / Spirit` · `Proweb` = `portail CSE-ga.fr - Proweb` ·
   `API Resto`/`Innovorder` = `API Resto + Innovorder`
2. **App réellement absente de l'inventaire** → à créer :
   `ViaReport` (consolidation — pourtant cible du flux INT-003 depuis IFS), `Deplacements`,
   `Portail RH benify`, `InfoLégal`, `ZyLab`
3. **Non-applications** → à requalifier : `Excel` (flux INT-191 = import manuel), `SAV`

**2 écarts rattrapables automatiquement** (casse) : `EXPENSYA`→`Expensya`, `PROGIDOC`→`Progidoc`.

## 4. Identifiants Archi manquants

26 applications n'ont pas d'`ID Archi` conforme — et ce sont, pour l'essentiel,
**les plus récentes et les plus structurantes** :

`IFS` (a un ID), mais : `QDV` · `Project Monitor` · `Immolead` · `Data Platform` ·
`Microsoft 365` · `GLPI` · `GitHub` / `GitLab` · `Redmine` · `Deskare` · `Tamtam` ·
`Exchanges` · `Flow By GA` · `Galaxy Access` · `API Resto + Innovorder` · `Zeendoc` ·
`GAIA` · les 3 serveurs `WinDev` · les 4 outils IA (`Claude`, `ChatGPT`, `Leexi`, `Batisia`, `Perplexity`).

Côté flux : **52 des 132 flux vivants sont sans ID Archi**.

> La colonne `Identifiant technique pour Archi` prouve que l'inventaire a **été conçu pour
> alimenter Archi**. L'intention est bonne, l'exécution est à 83 %. Compléter ces 26 + 52 IDs
> est le prérequis n°1 d'un modèle ArchiMate synchronisable.

## 5. Applications structurantes absentes de l'inventaire

Deux briques majeures ne figurent **pas** dans les 150 :

- **Talend** — l'orchestrateur de toutes les interfaces IFS (12 flux vivants portent
  explicitement « géré avec Talend = Oui »). Absent en tant qu'application.
- **Power BI** — cité slide 9 du support comme outil de pilotage Finance, absent de l'inventaire
  (seul `Qlik Sense` y figure).

Un doublon confirmé : `DwgTrueview` / `AutoDesk DwgTrueview`. Trois autres paires sont à
vérifier (`AEC`/`AutoDesk AEC`, `AutoCAD-LT`/`AutoDesk AutoCAD-LT`, `Vault`/`AutoDesk Vault`) —
elles gonflent artificiellement le compteur « > 100 applications ».

## Actions proposées à la DDSI

| # | Action | Effort | Gain |
|---|---|---|---|
| A1 | Normaliser les 7 alias + 2 écarts de casse dans l'onglet FLUX | 30 min | Réconciliation FLUX↔APPS à ~95 % |
| A2 | Créer les 5 apps manquantes + Talend + Power BI | 1 h | Carto applicative complète |
| A3 | Compléter les 26 `ID Archi` apps + 52 flux | 2 h | **Modèle Archi régénérable** |
| A4 | Remplir `Statut Utilisation` sur les 86 apps vides | 1/2 j (métier) | Distinguer SI vivant / SI résiduel |
| A5 | Fusionner les 4 doublons AutoDesk | 15 min | Compteur d'apps fiable |

Voir [[02-Taxonomie/01-Domaines-fonctionnels]] pour la suite.
