---
projet: Base IFS — Monitoring & Datawarehouse
note: Plan de classement
date_maj: 2026-07-10
tags: [gouvernance, plan-classement]
---

# Plan de classement — Base IFS (Monitoring & DWH)

> Conforme à la [[../../_Methodologie-Plan-Classement/00-Index|méthodologie interne d'évaluation des plans de classement]] (ISO 15489).

## Logique structurante (angle 1)

Classement **par fonction / activité**, pas par type de document ni par outil :
- **Comprendre** la base (`01-Connaissance-de-la-base/`)
- **Surveiller** sa santé (`02-Monitoring/`)
- **Alimenter** le DWH (`03-Datawarehouse/`)

## Arborescence

```
GA - Base IFS (Monitoring & DWH)/
├── README.md                          # onboarding (angle 6)
├── 00-Gouvernance/                    # transverses obligatoires (angle 10)
│   ├── 00-Plan-de-classement.md       # cette note
│   ├── 01-Changelog.md                # journal des évolutions structurantes
│   ├── 02-Glossaire-IFS.md            # vocabulaire IFS/Oracle
│   └── decisions-architecture/        # ADR immuables
├── 01-Connaissance-de-la-base/        # COMPRENDRE
│   ├── 01-Environnement-et-acces.md
│   ├── 02-Architecture-IFS-LU.md
│   └── 03-Cartographie-modules.md
├── 02-Monitoring/                     # SURVEILLER
│   ├── 01-Perimetre-et-faisabilite.md
│   ├── 10-Referentiel-SQL-monitoring.md
│   └── runbook.md                     # conditionnel obligatoire (prod)
├── 03-Datawarehouse/                  # ALIMENTER
│   └── 01-Strategie-extraction-Fabric.md
└── 99-Annexes/                        # archives
```

## Couverture des obligatoires transverses (angle 10)

| Obligatoire | Emplacement | Statut |
|---|---|---|
| Dossier gouvernance | `00-Gouvernance/` | ✅ créé |
| ADR | `00-Gouvernance/decisions-architecture/` | ✅ ADR-001 |
| Changelog | `00-Gouvernance/01-Changelog.md` | ✅ créé |
| Glossaire métier | `00-Gouvernance/02-Glossaire-IFS.md` | 🟡 amorcé |
| Archives / annexes | `99-Annexes/` | 🟡 dossier posé |
| README / onboarding | `README.md` | ✅ créé |
| Cartographie d'architecture | `01-.../02-Architecture-IFS-LU.md` (+ schéma à venir) | 🟡 en cours |
| **Runbook** (conditionnel — prod) | `02-Monitoring/runbook.md` | ⬜ à créer quand le monitoring sera défini |
| Cartographie RGPD (conditionnel — données perso) | à évaluer | ⬜ IFS contient des données perso → à traiter avant tout usage DWH |

## Convention de nommage

- Préfixes numériques `NN-` pour l'ordre de lecture ; `00-` = à lire en premier, `99-` = annexes.
- Codes domaine (à établir pour le DWH) alignés doc ↔ SQL ↔ fichiers (cohérence angle 1).
