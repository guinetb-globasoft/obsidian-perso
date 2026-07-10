---
projet: Base IFS — Monitoring & Datawarehouse
note: Changelog
date_maj: 2026-07-10
tags: [gouvernance, changelog]
---

# Changelog — Base IFS (Monitoring & DWH)

> Journal des évolutions **structurantes** (≠ historique fin des requêtes). Format inspiré de Keep a Changelog.

## 2026-07-10 — Démarrage

- Création du projet et du plan de classement fonctionnel (suivant la méthodologie interne).
- **Salve 1 exécutée** — relevé de l'environnement :
  - Compte `IFSDBREADONLY` (lecture seule), base **production** `PISAPRD1_1`, serveur `pisa-u1-prd-db1`.
  - Oracle 19c Enterprise Edition (19.29).
  - `IFSAPP` = 128 977 objets accessibles ; `IFSIAMSYS` inaccessible à ce compte.
- Décision cadre tracée en [[decisions-architecture/ADR-001-cadre-projet|ADR-001]].
- **En attente** : résultats salve 2 (cartographie des droits `DBA_*`/`V$` vs tables `IFSAPP`) → conditionne la faisabilité du monitoring technique.
