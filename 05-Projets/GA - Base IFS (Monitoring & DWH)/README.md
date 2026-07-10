---
projet: Base IFS — Monitoring & Datawarehouse
statut: en-cours
date_creation: 2026-07-10
tags: [ifs, oracle, monitoring, dwh, fabric, onelake, readme]
---

# Base IFS — Monitoring & Datawarehouse

> **Porte d'entrée du projet.** À lire en premier (angle 6 — onboarding).

## Objectif

Apprendre la structure de la base **Oracle IFS** (production `PISAPRD1`, accès DBeaver) pour deux finalités :

1. **Monitorer** la base — priorité **santé technique** (tablespaces, sessions, jobs, perf).
2. Construire à terme un **datawarehouse qui s'abreuve d'IFS** — cible **Microsoft Fabric / OneLake**.

> ⚠️ Base de **PRODUCTION** → lecture seule stricte, pas de requête lourde. Compte `IFSDBREADONLY`.
> ⚠️ **Aucun lien avec le projet DWH-Aerotec** (celui-ci s'abreuve de CLIPPER, pas d'IFS).

## Méthode de travail

Claude propose les requêtes SQL → Benoît les exécute dans DBeaver → colle les résultats → Claude documente ici, au fil de l'eau. Benoît ne connaît pas la base au départ ; l'objectif est un apprentissage cumulatif tracé.

## Plan de classement (logique fonctionnelle — ISO 15489)

| Dossier | Fonction / activité | Contenu |
|---|---|---|
| `00-Gouvernance/` | Méta-doc du projet | Plan de classement, changelog, glossaire, ADR |
| `01-Connaissance-de-la-base/` | **Comprendre** IFS | Environnement, architecture LU, cartographie modules |
| `02-Monitoring/` | **Surveiller** la santé technique | Périmètre de droits, référentiel SQL monitoring, runbook |
| `03-Datawarehouse/` | **Alimenter** le DWH Fabric | Stratégie d'extraction, modèle cible, mapping sources |
| `99-Annexes/` | Archives | Artefacts ponctuels conservés pour traçabilité |

## Par où commencer

1. [[00-Gouvernance/00-Plan-de-classement]] — comment ce dossier est organisé
2. [[01-Connaissance-de-la-base/01-Environnement-et-acces]] — l'état des lieux technique
3. [[00-Gouvernance/01-Changelog]] — le fil des avancées

## Ressource connexe (autre projet)

- `GA - IFS Stockage/06_Referentiel_SQL.md` — requêtes volumétrie IFS déjà éprouvées (contexte outil « Rapport Rapide IFS », version 25R2). À réutiliser/adapter pour le monitoring d'espace.
