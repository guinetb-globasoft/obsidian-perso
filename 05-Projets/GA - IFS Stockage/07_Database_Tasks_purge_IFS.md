# 🛠️ Database Tasks IFS de purge — accessibles sans DBA

> **Contexte** : Complément au [[06_Referentiel_SQL]]. IFS Cloud expose un catalogue de **Database Tasks** (procédures PL/SQL planifiables) accessibles depuis l'UI Aurena. Plusieurs sont dédiées à la purge / cleanup et permettent de **gagner de l'espace sans privilèges DBA**, contrairement aux requêtes `DELETE` / `ALTER` brutes du référentiel SQL.
>
> **Date d'analyse** : 2026-05-20
> **Version IFS** : 25R2 (Cloud)
> **Source** : Catalogue `DatabaseTaskHandling.svc/SchedulableMethods` côté CFG.

---

## 🎯 Pourquoi les Database Tasks plutôt que SQL direct ?

| Aspect | Quick Report SQL | Database Task IFS |
|---|---|---|
| `SELECT` simple | ✅ | ✅ (via la méthode) |
| `DELETE` / `DROP` / `ALTER` | ❌ Bloqué | ✅ Encapsulé dans la procédure |
| Privilèges nécessaires | Quick Report user | Solution Manager user |
| Audit / traçabilité | Pas natif | ✅ Job ID + Started/Executed timestamp |
| Planification récurrente | Manuelle | ✅ Schedule natif (jour/semaine/mois) |
| Risque accidentel | Élevé (manipulation directe) | Faible (logique IFS validée) |

→ **Toujours préférer les Database Tasks quand elles existent.** Les requêtes brutes du référentiel SQL restent utiles pour le **diagnostic / mesure**, mais l'exécution de la purge passe par ces tâches.

---

## 📋 Catalogue des Database Tasks de cleanup utiles

### Top prioritaires (gain attendu)

| # | MethodName | Description | Gain attendu | Cible (table / objet) |
|---|---|---|---|---|
| 1 | **`IAM_LOGIN_EVENT_API.REMOVE_EVENT_DETAILS`** | Remove Event Details | **~4 Go** | `IAM_LOGIN_EVENT_DETAIL_TAB` |
| 2 | **`HISTORY_LOG_API.REMOVE_OLDER_THAN__`** | Remove Older Than | ~2-3 Go | `HISTORY_LOG_TAB` |
| 3 | **`HISTORY_LOG_UTIL_API.CLEANUP__`** | Cleanup général | ~1-2 Go | History log |
| 4 | **`FR_AUDIT_REPORTING_UTIL_API.CLEANUP_FEC_EXT_FILE_TRANS`** | Cleanup Fec Ext File Trans | ~1.5 Go | `EXT_FILE_TRANS_TAB` (FEC) |
| 5 | **`AUDIT_STORAGE_API.CLEANUP_AUDIT_STORAGE`** | Cleanup Audit Storage | ~1 Go (variable) | Audit storage |
| 6 | **`AUDIT_BATCH_FILE_INFO_API.CLEANUP`** | Cleanup audit batch | quelques 100 Mo | Audit batch |
| 7 | **`FND_TEMP_LOB_STORE_API.REMOVE_OLD_TEMP_LOBS_`** | Remove Old Temp Lobs | 100 Mo à 1 Go | `FND_TEMP_LOB_STORE` |
| 8 | **`FND_ZIP_FILE_TEMP_API.CLEANUP_`** + `.DELETE_ZIP_FILES_` | Cleanup zip temp | 100 Mo à 1 Go | `FND_ZIP_FILE_TEMP` |
| 9 | **`FNDSCH_TEMP_LOB_STORE_API.REMOVE_OLD_TEMP_LOBS_`** | Remove Old Temp Lobs (sch) | 100-500 Mo | scheduler temp |
| 10 | **`FND_CLIENT_LOGON_API.REMOVE_SESSION`** | Remove Session | quelques 10 Mo | sessions expirées |
| 11 | **`FND_OBJ_SUBSCRIPTION_UTIL_API.CLEANUP_SUBSCRIPTIONS_`** | Cleanup Subscriptions | variable | object subscriptions |
| 12 | **`FND_STREAM_API.CLEANUP_MESSAGES_`** | Cleanup Messages | 100-500 Mo | IFS streams |
| 13 | **`IN_MESSAGE_UTIL_API.CLEANUP`** | Cleanup IFS Connect | variable | IFS Connect messages |
| 14 | **`IS_MV_REFRESH_LOG_API.CLEANUP_TRACE_DATA__`** | Cleanup Trace Data (BI) | quelques 100 Mo | trace data BI |
| 15 | **`XLR_TEMPLATE_UTIL_API.CLEANUP_TRACE_DATA__`** | Cleanup Trace Data | quelques 100 Mo | trace data XLR |
| 16 | **`INTFACE_EXCEL_CONNECT_API.CLEANUP_TABLES`** / `.CLEANUP_EXECUTION_INFORMATION` | Cleanup Excel Connect | quelques 100 Mo | Data migration |
| 17 | **`CUSTOM_OBJ_UTIL_API.CLEANUP_WITH_DELIVERY_SUCCESS_`** | Cleanup Custom Obj | variable | custom objects livrés |

### Bonus (Reorganize / Recompile, pas de la pure purge mais utile)

| MethodName | Description | Usage |
|---|---|---|
| `IS_CUSTOM_UTIL_API.RECOMPILE_INVALID_CUST_OBJS__` | Recompile Invalid Cust Objs | ✅ TESTÉ — résout les invalid `_CFP` (cf. `docs/IFS_TROUBLESHOOTING/MI_RETRIEVAL_ERROR_package_invalide.md` du repo ifs-env) |
| `INTFACE_REPL_PACKAGE_UTIL_API.COMPILE_PACKAGES` | Compile Packages | compile packages migration |
| `INTFACE_REPL_TRIGGERS_UTIL_API.COMPILE_TRIGGERS` | Compile Triggers | compile triggers migration |

---

## 🔥 Gain potentiel cumulé

**~10-15 Go** récupérables via Database Tasks (sans intervention DBA).

C'est **moins que les ~30 Go** estimés dans le [[03_Plan_purge]] d'origine, car les purges suivantes restent à passer par **DBA / Support IFS** (non exposées comme Database Task) :

- `WRI$_ADV_OBJECTS` (SQL Tuning Advisor) — ~10 Go → DBA
- `BPMN_DEBUG_ACTIVITY_LOG_TAB` — ~4 Go → DBA + désactiver mode debug
- `LANGUAGE_FILE_IMPORT_TAB` — ~1 Go → DBA
- AWR (`WRH$_*`) — ~3 Go → DBA (changement rétention)
- Recyclebin Oracle — variable → DBA
- UNDO resize — ~7 Go → DBA
- Tablespaces inutilisés (MAINTENIX, JASPER) — ~2 Go → DBA

→ **Stratégie en 2 temps** :
1. **Phase 1 (autonome)** : lancer les 17 Database Tasks ci-dessus → **gain immédiat ~10-15 Go**
2. **Phase 2 (avec IFS Support)** : ticket avec demande de purge des 7 postes DBA → gain additionnel ~25 Go

---

## 🚀 Comment lancer une Database Task

### Via l'UI Aurena (méthode standard)

1. Aller sur la page **Database Task** :
   `https://gafr-cfg.ifs.cloud/main/ifsapplications/web/page/DatabaseTaskHandling/DatabaseTask`
   (équivalent : Menu > Solution Manager > Background Processing > Database Tasks)
2. Filtrer sur **`MethodName`** = nom de la méthode (ex. `IAM_LOGIN_EVENT_API.REMOVE_EVENT_DETAILS`)
3. Si la méthode n'est pas dans la liste :
   - Cliquer **"New Database Task"** → sélectionner la méthode depuis le catalogue
   - L'enregistrer (devient une Batch Schedule Method)
4. Sélectionner la ligne → **"Schedule New Database Task"**
5. Choisir :
   - **Execute Now** (one-shot immédiat)
   - **Recurring** : journalier / hebdomadaire / mensuel (recommandé pour automatiser le maintenance)
6. Save → la tâche tourne en arrière-plan
7. Suivre dans **Background Jobs** : `BackgroundJobsHandling/BackgroundJobsDetails`

### Via l'API IFS (programmatique)

Voir le snippet dans `docs/IFS_TROUBLESHOOTING/MI_RETRIEVAL_ERROR_package_invalide.md` (option E) :

```python
import requests
H_JSON = {**HEADERS, 'Content-Type': 'application/json', 'If-Match': '*'}
BASE = "https://gafr-cfg.ifs.cloud/main/ifsapplications/projection/v1/DatabaseTaskHandling.svc"

# 1. Créer la définition
r = requests.post(f"{BASE}/NewDatabaseTaskVirtuals", headers=H_JSON, json={
    'MethodName': 'IAM_LOGIN_EVENT_API.REMOVE_EVENT_DETAILS',
    'Module': 'FNDBAS',                # à adapter selon le module
    'ArgumentType': 'NoParameter',     # ou 'StringParameter' / 'DateParameter' selon la méthode
    'SingleExecution': True,
})
objkey = r.json()['Objkey']

# 2. Action _Finish (enregistre dans BatchScheduleMethod)
requests.post(
    f"{BASE}/NewDatabaseTaskVirtuals(Objkey='{objkey}')"
    f"/IfsApp.DatabaseTaskHandling.NewDatabaseTaskVirtual_Finish",
    headers=H_JSON, json={}
)

# 3. L'exécution immédiate doit passer par l'UI (POST DeferredJobs renvoie ODP_ILLEGAL_STATE en API)
```

---

## ⚠️ Précautions

1. **Tester en CFG d'abord, puis UAT, puis PROD.**
2. Certaines méthodes ont des **paramètres** (date pivot, mode dry-run). Vérifier la signature dans l'UI **avant** Execute Now.
3. Les **dates de rétention** par défaut sont parfois conservatrices (30j, 90j). Si on veut purger plus aggressif, paramétrer la date dans le formulaire IFS.
4. **Avant/après** : faire un `SELECT COUNT(*)` sur la table cible (depuis Quick Report) pour mesurer le gain réel.
5. Pour les méthodes `CLEANUP_TRACE_DATA__` : confirmer que le mode trace est **désactivé** (sinon, on purge mais ça se remplit aussitôt).

---

## 📊 Process recommandé pour gagner les ~10-15 Go

### Étape 1 — Mesure avant (Quick Report)

Pour chaque cible, lancer le SELECT correspondant dans le [[06_Referentiel_SQL]]. Noter la taille.

### Étape 2 — Lancement progressif

1. Commencer par **#1 `IAM_LOGIN_EVENT_API.REMOVE_EVENT_DETAILS`** (~4 Go) — gros gain certain
2. Puis **#2-3 History log** (~3-5 Go)
3. Puis **#4 FEC Ext File** (~1.5 Go)
4. Enchaîner les autres par ordre de gain estimé

### Étape 3 — Planification récurrente

Pour les tâches qui ont vocation à tourner régulièrement (logs, sessions, temp lobs), les **scheduler en récurrent** :

| Task | Fréquence recommandée |
|---|---|
| `IAM_LOGIN_EVENT_API.REMOVE_EVENT_DETAILS` | Mensuel |
| `HISTORY_LOG_API.REMOVE_OLDER_THAN__` | Hebdomadaire |
| `FND_TEMP_LOB_STORE_API.REMOVE_OLD_TEMP_LOBS_` | Quotidien |
| `FND_ZIP_FILE_TEMP_API.CLEANUP_` | Quotidien |
| `FND_CLIENT_LOGON_API.REMOVE_SESSION` | Quotidien |
| `IN_MESSAGE_UTIL_API.CLEANUP` | Hebdomadaire |
| `FR_AUDIT_REPORTING_UTIL_API.CLEANUP_FEC_EXT_FILE_TRANS` | Mensuel (après clôture mensuelle) |
| Trace data (IS_MV / XLR) | Mensuel |

→ Ce planning évite la dérive de stockage à long terme.

### Étape 4 — Mesure après (Quick Report)

Re-lancer les mêmes SELECTs → diff = gain réel.

### Étape 5 — Mise à jour de la négociation

Si gain réel ≥ 10 Go : **ajuster l'argumentaire de négociation IFS** ([[04_Argumentaire_negociation_IFS]]) en démontrant qu'on a déjà appliqué les bonnes pratiques côté client, et que le reste relève d'eux (purges DBA, framework, AWR…).

---

## 🔗 Liens vers le travail amont

- [[00_Synthese_executive]] — Synthèse pour négo
- [[01_Analyse_volumetrie_complete]] — Volumétrie par tablespace
- [[02_Responsabilite_volumes]] — Qui génère quoi
- [[03_Plan_purge]] — Plan de purge originel (référence pour les gains DBA)
- [[04_Argumentaire_negociation_IFS]] — Arguments négociation
- [[05_Analyse_documents_DocMan]] — Documents EDM
- [[06_Referentiel_SQL]] — Requêtes SQL (Quick Report)

## 🔗 Liens vers le repo `ifs-env`

- `docs/IFS_TROUBLESHOOTING/MI_RETRIEVAL_ERROR_package_invalide.md` — Pattern API pour lancer une Database Task (cas pratique avec `RECOMPILE_INVALID_CUST_OBJS__`)
