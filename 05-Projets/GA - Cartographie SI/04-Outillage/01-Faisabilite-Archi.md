---
titre: Faisabilité Archi / ArchiMate
statut: analysé
date: 2026-08-18
tags: [archi, archimate, jarchi, outillage, coarchi]
---

# « Possible avec Archi ? » — oui, et le modèle existe déjà

> Réponse à la question posée par Gildvin. La conclusion n'est pas « il faut choisir un
> outil » mais **« il y a un actif à remettre en service »**.

## Fraîcheur : le modèle est figé depuis le 1er juillet 2024

| Preuve | Valeur |
|---|---|
| Commits dans le dépôt `ga-archi` | **1 seul** — `156d763` « First Commit », **01/07/2024** |
| Working tree | **propre** — aucun travail local non commité |
| Remote | `https://github.com/Globasoft/GA-Archi.git` (branche `master`) |
| Date de tous les fichiers du modèle | 01/07/2024 (= date du checkout) |
| Dernière modif de l'inventaire Excel | **18/08/2026** |
| **Écart** | **≈ 25 mois** |

⚠️ **Limite de la vérification** : `git ls-remote` échoue faute d'authentification non
interactive. Impossible de garantir qu'aucun commit plus récent n'existe côté GitHub.
**À faire : un `git fetch` manuel** sur le dépôt avant de conclure définitivement.

### L'outillage a survécu 7 mois de plus que le modèle

Les scripts jArchi, eux, ont continué d'évoluer bien après le commit unique :

| Date | Élément |
|---|---|
| 01/07/2024 | **commit unique du modèle** · `Import from Excel File Projet` |
| 18/07 → 09/08/2024 | `lib`, `node_modules`, `Import from Interface File` — snapshot `INVENTAIRE - Applicatifs Métier.xlsx` du **09/08/2024** |
| 28-30/08/2024 | `create-app-group-view`, `create-coop-app-view` |
| 10/09/2024 | `app-business-processes` |
| 11/10/2024 | `Import from RECAP Applications` — snapshot `INVENTAIRE - Applications.xlsx` du **11/10/2024** (235 lignes de flux contre 250 aujourd'hui) |
| 29/11/2024 | `export-whole-model`, `Import from Server File`, `Import from Data Matrix` |
| **05/02/2025** | `Import-Processes` — **dernière trace d'activité** |
| depuis | plus rien |

**Lecture** : des ré-imports ont été *préparés* (snapshots d'inventaire figés à côté des
scripts) mais **jamais reversés dans le modèle**. Le chaînon rompu n'est pas l'outil, c'est
le geste de commit. C'est aussi ce qui explique la désynchronisation des identifiants :
les UUID ont été régénérés côté Excel au fil des ré-imports préparés, sans que le modèle
ne les reçoive.

### Le logiciel Archi lui-même

`C:\Program Files\Archi\Archi.exe` daté du **01/11/2023** ; le modèle déclare le format
`version="5.0.0"`. L'installation a donc ~2,5 ans. Non bloquant pour lire le modèle, mais
à vérifier (Aide > À propos) avant de relancer des scripts jArchi — les compatibilités
jArchi / Archi bougent d'une version majeure à l'autre.

## Ce qui existe : `C:\Users\guinet\Documents\Archi`

Un modèle ArchiMate nommé **« GA »**, au format **coArchi** (dépôt collaboratif, un fichier
XML par élément), version Archi 5.0.0.

| Objet | Compte |
|---|---:|
| Éléments au total | **581** |
| dont `ApplicationComponent` | **156** |
| dont `Device` (serveurs) | 207 |
| dont `Capability` | 104 |
| dont `BusinessActor` | 50 |
| Relations | **570** |
| dont `FlowRelationship` (interfaces) | **178** |
| **Vues (diagrammes)** | **26** |

Le modèle porte deux profils personnalisés (`Entité Juridique` sur `BusinessActor`,
`Groupe d'activité` sur `Grouping`) — ce n'est pas un modèle jetable.

### Les 26 vues existantes

Elles sont massivement **auto-générées par script**, sur le motif
« Applications classées par X et Y » :

- Applications par OS et fonction du serveur (295 objets)
- Applications par site et fonction du serveur (251)
- Applications par service métier propriétaire et responsable applicatif (235)
- Applications par éditeur / intégrateur et importance du processus (211)
- … puis des vues métier ponctuelles : `Processus de gestion du CAE`,
  `Etudes GED - IFS` / `- Sharepoint` / `- Full Mixte`, `GA Orga`, `Activity Map 1/2` et `2/2`,
  `Carte de France avec les usines`, `Fiche serveur : SRVW-SAGE01-P`.

**Aucune vue « domaine fonctionnel » ni « flux Finance autour d'IFS » n'existe** — d'où la
demande. Mais l'ossature (éléments + relations) est là.

### Les scripts jArchi

Dossier `Documents\Archi\scripts` — la chaîne Excel → Archi a déjà été construite (2022-2024) :

| Script | Rôle |
|---|---|
| `Import from apps.ajs` | import des applications depuis l'inventaire |
| `Import from RECAP Applications.ajs` | idem, version antérieure |
| `export-interfaces.ajs` | export des interfaces |
| `create-app-group-view/Create Views and Visual Objects.ajs` | **génération de vues groupées** |
| `Create Views from Servers.ajs` | génération des vues serveurs |
| `Where used.ajs`, `documentation.ajs`, `export-from-view*.ajs` | outillage de restitution |
| `app-business-processes/index.ajs` | rattachement applications ↔ processus |

Les `ApplicationComponent` portent des `properties` reprises des colonnes de l'Excel
(`Progiciel?`, `Importance processus impacté`, `Impact sur le SI`, `Info VM`) — la
synchronisation a bien fonctionné à une époque.

## L'écart avec l'inventaire d'aujourd'hui

C'est **le** constat de l'analyse, et il est contre-intuitif :

### ❌ Le lien est rompu côté applications

**0 identifiant commun** entre les 123 `ID Archi` de l'onglet APPS et les 156
`ApplicationComponent` du modèle. Les UUID ont été **régénérés d'un côté sans être
reportés de l'autre**. La colonne « Identifiant technique pour Archi » de l'Excel ne
pointe donc plus vers rien.

### ✅ Le lien est intact côté flux

**140 des 150** identifiants de l'onglet FLUX correspondent encore à une
`FlowRelationship` du modèle. Le référentiel des interfaces, lui, n'a pas dérivé.

### Le modèle décrit un SI d'avant IFS

Réappariement par **nom** entre l'inventaire et le modèle :

| | Compte |
|---|---:|
| Appariées au nom exact | **102** |
| Appariées après normalisation (`Hercule PRO` ↔ `Hercule Pro`) | 1 |
| **Absentes du modèle, à créer** | **47** |

Les 47 manquantes sont les plus récentes et les plus structurantes : `QDV`, `Exfiles`,
`Sage XRT Trésorerie` / `Com Bancaire` / `Signature`, `Sage Immo`, `Etafi/yourcegid`,
`ICS / Comfact / Spirit`, `Project Monitor`, `Immolead`, `Data Platform`, `Deskare`,
`Microsoft 365`, `GLPI`, `GitHub` / `GitLab`, `Redmine`, `Zeendoc`, `Commande préfa`,
les 5 outils IA…

À l'inverse, le modèle contient **des composants disparus de l'inventaire** :
`Tresorerie`, `Immo`, `Infor`, `FactoryClientele`, `PaieSage (Décomissionné)`, `ZyLab`,
`ZyLabTrans`, `Yammer`, `Everwin`, `Declique`, `Bimmo`, `Kaliti`, `Concept Office`,
`Smartwellcoming`, `BoiteAchantier`, `Jobaffinity`, `Cenareo`, `MindManager`,
`Tableau de bord foncier collaboratif`, `Billetterie / Réservation voyage interne`…
→ matière première pour l'onglet « APPS décommissionnées ».

## Verdict

Produire les deux vues demandées **dans Archi** est faisable. Mais l'effort utile n'est pas
le dessin — c'est la **remise en cohérence référentiel ↔ modèle**. Une fois faite, les vues
se **régénèrent par script** à chaque mise à jour de l'Excel, au lieu d'être redessinées à
la main à chaque demande. C'est la différence entre une carto « livrable » et une carto
« service ».

### Chemin proposé

| # | Étape | Effort | Dépend de |
|---|---|---|---|
| 1 | **Réaligner les identifiants applications** — 103/150 se rapprochent par nom exact, le réappariement est scriptable ; 47 composants à créer | 1 j | — |
| 2 | **Normaliser les 7 alias de flux** dans l'onglet FLUX (`Sage Signature`, `Hercule`, `ICS Compta`, `Proweb`, `API Resto`, `Innovorder`, casse `EXPENSYA`/`PROGIDOC`) | 30 min | — |
| 3 | **Ajouter une colonne « Domaine fonctionnel »** à l'onglet APPS, avec les 12 domaines de [[02-Taxonomie/01-Domaines-fonctionnels]] | 1/2 j | taxonomie validée |
| 4 | **Créer les 2 vues par script jArchi** : vue fonctionnelle par domaine, vue de flux par processus (`Achat/P2P`, `Financier > NdF`, `RH & Pointage & Paie`…) | 1 j | 1 + 3 |
| 5 | **Nettoyer les composants orphelins** du modèle → onglet APPS décommissionnées | 1/2 j | 1 |

**Total ≈ 3,5 j** pour une cartographie régénérable, contre ~1 j pour une carto redessinée
à la main à chaque fois.

## Précaution

Le dépôt `Documents\Archi\model-repository\ga-archi` est un dépôt **coArchi** — donc
partagé/versionné. Toute reprise doit passer par une branche ou une copie, pas par une
édition directe. Vérifier avec Gildvin qui d'autre l'utilise avant d'y écrire.
