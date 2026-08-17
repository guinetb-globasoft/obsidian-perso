---
titre: Taxonomie des domaines fonctionnels GA
statut: proposé
date: 2026-08-13
tags: [taxonomie, domaines-fonctionnels, urbanisation, archimate]
---

# Domaines fonctionnels — taxonomie retenue

## Le problème à résoudre

L'inventaire ne porte **pas** de domaine fonctionnel. Il porte une colonne
`RACI.Propriétaire_Métier.Nom_Service`, qui est **organisationnelle** (`DAF > COMPTA`,
`INGENIERIE > Bureau d'étude`, `Industrie > EQUILAB`…) et compte **48 valeurs distinctes**,
dont des variantes de casse (`DAF > COMPTA` / `DAF > Compta`) et des `????`.

Or la strate fonctionnelle répond au **« quoi »**, pas au **« qui »** (cf. slide 3 du support).
Un organigramme n'est pas une cartographie fonctionnelle : il change à chaque réorganisation,
alors que les fonctions métier d'un constructeur-promoteur, elles, ne bougent pas.

## Principe retenu

Découpage par **chaîne de valeur du groupe** (de la prospection foncière à l'exploitation du
bâtiment), + les fonctions support, + deux **strates transverses** représentées en bandeaux :

```
              ┌──────────── PILOTAGE & DÉCISIONNEL ────────────┐   ← consomme tout
              │  Développement&Commerce  Études  Ingénierie…   │
              │            ▼        ERP IFS        ▼           │   ← cœur
              │  Industrie   Travaux   Services   QSE          │
              └──────────── SOCLE NUMÉRIQUE & COLLAB. ─────────┘   ← porte tout
```

C'est la lecture d'urbanisation classique (quartiers métier / zone d'échange / socle) et elle
répond à la demande « IFS au centre, satellites autour regroupés par domaine ».

## Les 12 domaines + le cœur

| Code | Domaine | Périmètre | Apps |
|---|---|---|---:|
| `DEV_COM` | **Développement & Commerce** | Prospection foncière, CRM, appels d'offres, sites vitrine | 7 |
| `ETU_CHIF` | **Études & Chiffrage** | Études de prix, devis, nomenclatures | 8 |
| `ING_BIM` | **Ingénierie & BIM** | Conception, calcul de structure, maquette numérique | **43** |
| `ACH_APP` | **Achats & Approvisionnement** | Sourcing, commandes, conformité fournisseurs | 9 |
| `FIN_JUR` | **Finance, Gestion & Juridique** | Comptabilité, trésorerie, fiscalité, contrats | **19** |
| `RH_PAIE` | **RH & Paie** | SIRH, paie, pointages, temps | 6 |
| `IND_PROD` | **Industrie & Production** | ERP usines, GPAO/MES, stocks, machines | 11 |
| `TRV_CHT` | **Travaux & Chantiers** | Pilotage de chantier, réserves, matériel | 5 |
| `SRV_EXP` | **Services & Exploitation** | Gestion immobilière, SAV, GTB / smart building | 9 |
| `QSE` | **QSE & Prévention** | Qualité, sécurité, habilitations, environnement | 5 |
| `PILOT` | **Pilotage & Décisionnel** *(bandeau haut)* | BI, reporting, portefeuille projets | 3 |
| `SOCLE` | **Socle numérique & collaboratif** *(bandeau bas)* | Bureautique, identité, ITSM, intégration, IA, dev | 24 |
| `ERP` | **ERP Groupe IFS** *(cœur)* | Finance, Commerce, Achats — et lot 5 à venir | 1 |

**150 / 150 applications affectées, zéro non classée.**

## Ce que la répartition révèle

- **Ingénierie & BIM = 43 apps, soit 29 % du parc** pour un domaine qui ne porte
  quasi aucun flux inter-applicatif structurant. C'est un **parc d'outils de poste de travail**
  (calcul, CAO, rendu), pas un système d'information intégré. Conséquence de carto : ce domaine
  doit être **représenté en volume mais pas détaillé** — sinon il écrase visuellement la carte.
- **Finance & Juridique = 19 apps** mais **concentre l'essentiel des flux** (voir
  [[03-Cartographies/02-Vue-applicative-Finance]]). Densité de flux ≠ nombre d'apps :
  c'est exactement pourquoi il faut **deux vues** et pas une.
- Le **socle (24 apps)** est le second poste. Il est invisible du métier mais porte tout.

## Arbitrages assumés (à valider par Gildvin)

| Arbitrage | Choix | Motif |
|---|---|---|
| Les **pointages** (`PaieGRH`, `PlanningChantier`, `PlanningBE`) | → **RH & Paie**, pas Travaux | La finalité est la paie et la refacturation, pas le pilotage de chantier |
| Les **sites web vitrine** | → **Développement & Commerce** | Ce sont des outils d'acquisition commerciale (ROOJ.fr est lié au CRM Immolead) |
| `Deskare`, `ReservationSdR` | → **Socle** | Environnement de travail, pas services aux clients |
| `GTC Conso`, `iControl`, `MyGapéo` | → **Services & Exploitation** | Exploitation du bâtiment livré (offre smart building Equilab) |
| Les **outils IA** (`Claude`, `ChatGPT`, `Leexi`, `Perplexity`) | → **Socle**, sauf `Batisia` → Études | Batisia est un outil métier de chiffrage, les autres sont transverses |
| `DocuSign` / `YouSign` | → **Finance, Gestion & Juridique** | Propriétaire = DAF > Juridique |
| `Divalto` (Ossabois) | → **Industrie & Production** | Cohérent avec le périmètre « SI Ossabois » distingué slide 6 |

## Fichier d'implémentation

La table d'affectation est du code, pas un tableau à recopier :
`scratchpad/domaines.py` → dictionnaire `AFFECTATION` (nom exact de l'inventaire → code domaine).
Elle est **rejouée à chaque régénération** des cartos et **échoue si une app n'est pas classée**,
ce qui garantit que l'ajout d'une app dans l'Excel ne passe pas silencieusement à la trappe.
