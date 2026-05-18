---
tags: ["methodologie", "plan-classement", "normes", "iso", "references"]
created: 2026-05-17
---

# 10. Normes et référentiels

> Catalogue des normes mobilisables pour challenger un plan de classement.

## Vue d'ensemble

| Norme / référentiel | Périmètre | Quand l'utiliser |
|---|---|---|
| **ISO 15489-1** | Records management (principes) | Toujours — norme socle |
| **ISO 23081** | Métadonnées | Quand on challenge la dimension métadonnées |
| **ISO 30300/30301** | Système de management des records | Pour la gouvernance |
| **ISO 16175** | Exigences fonctionnelles SI | Pour challenger un SI / GED |
| **MoReq2010** | Spécifications fonctionnelles européennes | Pour cahier des charges GED/SAE |
| **NF Z42-013 / ISO 14641** | Archivage électronique probant | Pour valeur juridique |
| **R2GA (SIAF)** | Référentiel public français | Secteur public FR |
| **SEDA** | Échange de données archivage | Interopérabilité, secteur public |
| **Vitam** | Standards techniques | Secteur public, projets de masse |
| **PMBOK / PRINCE2** | Management de projet (clôture) | Pour livrabilité et clôture projet |

---

## ISO 15489-1:2016 — La norme socle

**Titre complet** : Information et documentation — Gestion des documents d'activité — Partie 1 : Concepts et principes

### Ce qu'elle dit
- Définit ce qu'est un **records management**
- Principes : **authenticité, fiabilité, intégrité, exploitabilité**
- Décrit le **plan de classification** et ses qualités attendues
- Couvre le **cycle de vie** complet du document

### Articles clés
- §7 : Principes des records authentiques, fiables, intègres, exploitables
- §9.4 : Classification
- §9.5 : Indexation
- §9.6 : Sort final et durée de conservation
- §8.4 : Maintenance des systèmes

### Quand l'utiliser
**Toujours** — c'est la référence de base pour challenger n'importe quel plan.

---

## ISO 23081 — Métadonnées

**Titre** : Information et documentation — Métadonnées pour les documents d'activité

### Parties
- **23081-1:2017** : Principes
- **23081-2:2021** : Concepts et mise en œuvre
- **23081-3:2011** : Méthode d'auto-évaluation

### Ce qu'elle dit
- Quelles métadonnées sont indispensables
- Comment structurer un schéma de métadonnées
- Comment garantir la **persistance** des métadonnées

### Quand l'utiliser
Quand on évalue [[06-Metadonnees|l'angle métadonnées]] ou la résistance à la migration.

---

## ISO 30300 / 30301 — Système de management

**Titres**
- 30300 : Information et documentation — Systèmes de gestion des documents d'activité — Principes et terminologie
- 30301 : ... — Exigences (norme certifiable)

### Ce qu'elles disent
- Approche **système de management** (similaire à ISO 9001)
- Politique, objectifs, ressources, surveillance, amélioration continue
- Permet la **certification** d'une organisation

### Quand l'utiliser
Pour challenger la **gouvernance** du dispositif documentaire — pas seulement le plan en lui-même.

---

## ISO 16175 — Exigences fonctionnelles

**Titre** : Information et documentation — Processus et exigences fonctionnelles relatifs aux logiciels gérant les documents d'activité

### Parties
- 16175-1 : Aspects fonctionnels (concepts et principes)
- 16175-2 : Lignes directrices et exigences fonctionnelles
- 16175-3 : Lignes directrices pour environnements particuliers

### Ce qu'elle dit
- **Exigences fonctionnelles** qu'un SI doit remplir pour gérer correctement les records
- Très opérationnelle pour évaluer un outil (GED, SAE, ERP avec module GED)

### Quand l'utiliser
- Pour évaluer un outil candidat
- Pour rédiger un cahier des charges
- Pour challenger un SI existant

---

## MoReq2010

**Titre** : Modular Requirements for Records Systems

### Ce que c'est
Référentiel **européen** de **spécifications fonctionnelles** pour les systèmes d'archivage électronique. Très **détaillé** (plus de 900 exigences testables).

### Structure
- Service Core (cœur du système)
- Modules optionnels (classification, conservation, etc.)
- Exigences numérotées et testables

### Quand l'utiliser
- Rédaction de **CCTP** (cahier des charges techniques)
- **Audit** technique poussé d'un SAE
- **Certification** d'un outil

### Limites
- Très lourd (souvent surdimensionné pour un projet IT classique)
- Pas toujours adapté aux SI hors archivage pur

---

## NF Z42-013 / ISO 14641:2018

**Titre français** : Archivage électronique — Spécifications relatives à la conception et au fonctionnement de systèmes informatiques en vue d'assurer la conservation et l'intégrité des documents stockés dans ces systèmes

### Ce qu'elle dit
- Conditions de **conservation à valeur probante**
- Intégrité (empreintes, signatures, horodatage)
- Traçabilité des opérations
- Restitution lisible dans le temps

### Quand l'utiliser
Quand le projet implique des **documents à valeur probante** (contrats signés électroniquement, archives légales, etc.).

---

## R2GA (Référentiel Général de Gestion des Archives)

**Éditeur** : SIAF (Service interministériel des Archives de France)

### Ce que c'est
- Référentiel **public français**
- Couvre **principes**, **méthodes**, **outils**
- Inclut des **modèles** (tableaux de gestion, instructions)

### Structure
- Partie I : Principes
- Partie II : Méthodes
- Partie III : Outils

### Quand l'utiliser
- Tout projet en **secteur public** français
- Source de modèles pratiques (même pour le privé)

---

## SEDA (Standard d'Échange de Données pour l'Archivage)

### Ce que c'est
- **Standard français** d'échange de données entre producteurs et services d'archives
- Schémas XML normalisés
- Profil d'archivage (ce qu'on attend pour une catégorie de documents)

### Quand l'utiliser
- Échange avec service d'archives public
- Conception de **versements automatisés**
- Définition de **profils d'archivage** par typologie

---

## Programme / Solution Vitam

### Ce que c'est
- Solution **logicielle d'archivage électronique** pour le secteur public français
- Open source, opérée par État + CINES
- Implémente SEDA et NF Z42-013

### Quand l'utiliser
- Projets du secteur public français
- Référence pour benchmarker des outils privés équivalents

---

## PMBOK / PRINCE2 — Management de projet

### Ce que c'est
Référentiels mondiaux de management de projet, qui formalisent notamment la **phase de clôture** d'un projet — incluant la livraison documentaire.

### Ce qu'ils apportent
- Definition of Done incluant la doc livrable
- Processus de clôture (livrables finaux, transfert de connaissance)
- Acceptation formelle par le sponsor / client

### Quand l'utiliser
Pour challenger l'angle [[09-Livrabilite-cloture-projet|Livrabilité et clôture projet]].

---

## Autres normes à connaître

### ISO 27001 — Sécurité de l'information
Indirectement liée : confidentialité, intégrité, disponibilité des records.

### Dublin Core
Jeu minimal de **15 éléments de métadonnées**. Léger, universel, point d'entrée pour des systèmes simples.

### PREMIS
Standard de métadonnées pour la **préservation numérique long terme**.

### OAIS (ISO 14721)
Modèle de référence pour les **systèmes d'archivage numérique pérenne**.

---

## Comment articuler ces normes

```
Stratégie / gouvernance       → ISO 30300/30301
        ↓
Principes records management  → ISO 15489
        ↓
Métadonnées                   → ISO 23081 / Dublin Core
        ↓
Exigences fonctionnelles SI   → ISO 16175 / MoReq2010
        ↓
Archivage probant             → NF Z42-013 / ISO 14641
        ↓
Préservation long terme       → OAIS / PREMIS
        ↓
Secteur public FR             → R2GA / SEDA / Vitam
        ↓
Clôture projet / livrabilité  → PMBOK / PRINCE2
```

## Lien avec les autres angles

Chaque angle d'attaque s'appuie sur une ou plusieurs normes :

| Angle | Normes principales |
|---|---|
| [[01-Logique-structurante]] | ISO 15489, R2GA |
| [[02-Profondeur-hierarchie]] | ISO 15489, MoReq2010 |
| [[03-Exhaustivite-exclusivite]] | ISO 15489, ISO 16175 |
| [[04-Calendrier-conservation-DUA]] | ISO 15489, R2GA, RGPD |
| [[05-Stabilite-evolutivite]] | ISO 15489, ISO 30301 |
| [[06-Metadonnees]] | ISO 23081, Dublin Core |
| [[07-Adequation-usages]] | ISO 15489, ISO 30301 |
| [[08-Conformite-reglementaire]] | RGPD, NF Z42-013, sectoriels |
| [[09-Livrabilite-cloture-projet]] | ISO 15489 §9.6, PMBOK, PRINCE2 |

---

## Retour à l'[[00-Index]]
