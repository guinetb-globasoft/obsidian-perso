---
projet: Base IFS — Monitoring & Datawarehouse
note: Environnement & accès
date_maj: 2026-07-10
tags: [ifs, oracle, environnement, acces, monitoring]
---

# Environnement & accès

## Connexion (relevé 2026-07-10 — salve 1)

| Élément | Valeur |
|---|---|
| Compte / schéma | `IFSDBREADONLY` (lecture seule dédié ; son schéma propre est vide) |
| Base | `PISAPRD1_1` — **PRODUCTION** |
| Serveur | `pisa-u1-prd-db1` |
| Oracle | Database **19c** Enterprise Edition — 19.29.0.0.0, Production |

> ⚠️ **Production** → lecture stricte, éviter les requêtes lourdes (full scans, tri sur BLOB…).

## Périmètre d'objets visibles (`all_objects` par owner)

| Owner | Nb objets | Note |
|---|---:|---|
| **IFSAPP** | **128 977** | Schéma applicatif IFS unique — tout le métier est là |
| SYS | 40 272 | Dictionnaire / système Oracle |
| PUBLIC | 8 616 | Synonymes publics |
| XDB | 202 | Oracle XML DB |
| CTXSYS | 110 | **Oracle Text** (recherche plein-texte utilisée par IFS) |
| WMSYS | 55 | Oracle Workspace Manager |
| GSMADMIN_INTERNAL | 30 | Global Service Manager |
| SYSTEM | 9 | — |

- `IFSAPP` porte l'essentiel → c'est là qu'on requête.
- **`IFSIAMSYS` absent** → aucun droit sur l'Identity & Access Management IFS (angle mort auth/login).

## Périmètre de droits système (salve 2 — 2026-07-10) ✅ **MONITORING FAISABLE**

| Vue testée | Résultat | Accès |
|---|---:|:--:|
| `v$session` | 211 | ✅ |
| `dba_segments` | 10 975 | ✅ |
| `dba_data_files` | 16 | ✅ |
| `dba_free_space` | 890 | ✅ |
| `dba_tablespaces` | 15 | ✅ |
| `dba_scheduler_jobs` | 73 | ✅ |
| `dba_scheduler_job_run_details` | 1 932 268 | ✅ |
| `v$sysmetric` | ORA-00942 | ❌ |
| `ifsapp.transaction_sys_local_tab` (Background Jobs) | _en attente_ | ⬜ |
| `ifsapp.application_message_tab` (intégrations) | _en attente_ | ⬜ |

**Lecture :**
- Le compte dispose des vues `DBA_*` d'**espace** (segments/datafiles/free_space/tablespaces) et de **jobs** (scheduler + historique) → surveillance saturation disque et jobs en échec **directement faisable**.
- `v$session` accessible → sessions temps réel, sessions bloquées, comptage connexions **OK**.
- Certaines vues `V$` de perf pure (`v$sysmetric`) sont **refusées** → contourner via `v$` accessibles (`v$sysstat`, `v$session_wait`… à tester) ou via `DBA_HIST_*` (AWR, à tester).
- Profil probable : grants ciblés + `SELECT_CATALOG_ROLE` partiel. À cartographier finement (voir prochaine salve : `SESSION_PRIVS` / `SESSION_ROLES`).

## Note de contexte inter-projets

Le référentiel SQL de `GA - IFS Stockage` a été établi via l'outil **« Rapport Rapide IFS »** (restrictions tool-level : pas de GROUP BY/JOIN/sous-requête). **Ici on est dans DBeaver = vrai client Oracle** → ces restrictions SQL ne s'appliquent pas ; seuls comptent les **privilèges** de `IFSDBREADONLY`.

## Prochaines étapes

1. Confirmer les 2 sondes IFS (Background Jobs, Application Messages).
2. Lister précisément rôles et privilèges du compte (`SESSION_ROLES`, `SESSION_PRIVS`).
3. Tester les `V$`/`DBA_HIST_*` de perf pour combler le trou `v$sysmetric`.
