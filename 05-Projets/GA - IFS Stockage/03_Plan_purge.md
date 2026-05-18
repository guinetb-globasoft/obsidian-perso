# 🧹 Plan de purge — Gains potentiels ~30 Go

> **Objectif** : Identifier les actions concrètes de purge et de réorganisation permettant de réduire l'empreinte de la base sans toucher à aucune donnée métier.
>
> **Gain potentiel total estimé : ~30 Go** (passage de 122 Go à ~90 Go).

---

## 1. Vue d'ensemble des actions

| Priorité | Action | Gain | Responsable | Risque | Délai |
|----------|--------|------|-------------|--------|-------|
| 🥇 P1 | Purge `WRI$_ADV_OBJECTS` | ~10,9 Go | DBA IFS Cloud | Faible | Immédiat |
| 🥇 P1 | Resize `UNDOTBS1` | ~7 Go | DBA IFS Cloud | Faible | Immédiat |
| 🥇 P1 | Désactiver debug BPMN + purge logs | ~3,9 Go | Admin IFS | Aucun | Immédiat |
| 🥈 P2 | Politique de rétention IAM (90j) | ~4 Go | Admin IFS | Faible | 1-2 semaines |
| 🥈 P2 | Réduction rétention AWR (à 14j) | ~3 Go | DBA IFS Cloud | Aucun | Immédiat |
| 🥉 P3 | Purge `LANGUAGE_FILE_IMPORT_TAB` | ~1 Go | Admin IFS | Aucun | Immédiat |
| 🥉 P3 | Purge `EXT_FILE_TRANS_TAB` ancien | ~1,5 Go | Admin IFS | Faible | Immédiat |
| 🥉 P3 | `PURGE DBA_RECYCLEBIN` | Variable | DBA IFS Cloud | Aucun | Immédiat |
| 🥉 P3 | Suppression tablespaces vides (`MAINTENIX`, `JASPER`) | ~2 Go | DBA IFS Cloud | Faible | À vérifier |
| 🏅 P4 | Ticket IFS Support cleanup `FND_MODEL_*` | Variable | IFS Support | Faible | Selon retour IFS |
| 🥇 **P1** | **Activer `Cloud File Storage` IFS + migrer EDM via Web Assistant** (feature standard IFS Cloud, Azure Blob, doc officielle, outil de migration fourni) | **~10 Go immédiat + croissance évitée (~36 Go/an)** | Admin IFS | **Faible** | **Court terme** |

---

## 2. Détail des actions Priorité 1 (P1)

### 2.1 🥇 Purge de `WRI$_ADV_OBJECTS` (gain ~10,9 Go)

**Contexte** : La table `WRI$_ADV_OBJECTS` et ses 3 index occupent **10,9 Go** dans le schéma SYS. Elle stocke les recommandations du **SQL Tuning Advisor / SQL Access Advisor**. Sur une base bien administrée, elle fait quelques Mo.

**Origine** : Bug Oracle documenté — le job auto-cleanup peut être désactivé ou défaillant. Références Oracle :
- Note 1281703.1 — "WRI$_ADV_OBJECTS Grows Large"
- Note 2030447.1 — "Auto SQL Tuning Advisor Task Cleanup"

**Action à demander à IFS** :
```sql
-- 1. Identifier les tâches advisor à supprimer
SELECT task_id, task_name, status, created
FROM dba_advisor_tasks
ORDER BY created;

-- 2. Supprimer les tâches auto-tuning anciennes
EXEC DBMS_AUTO_SQLTUNE.SET_AUTO_TUNING_TASK_PARAMETER('AUTOMATIC', 'ALL');
-- ou bien dropper les tâches manuellement
EXEC DBMS_ADVISOR.DELETE_TASK('SYS_AUTO_SQL_TUNING_TASK');

-- 3. Réorganiser la table après purge
ALTER TABLE SYS.WRI$_ADV_OBJECTS MOVE;
ALTER INDEX SYS.WRI$_ADV_OBJECTS_PK REBUILD;
ALTER INDEX SYS.WRI$_ADV_OBJECTS_IDX_01 REBUILD;
ALTER INDEX SYS.WRI$_ADV_OBJECTS_IDX_02 REBUILD;
```

**Risque** : Très faible. La purge des tâches advisor anciennes n'affecte pas le fonctionnement applicatif.

**Responsable** : DBA IFS Cloud (nécessite privilèges SYS).

---

### 2.2 🥇 Resize de `UNDOTBS1` (gain ~7 Go)

**Contexte** : Le tablespace UNDO est alloué à 8,7 Go mais utilisé à seulement 0,4 Go (95 % vide).

**Action à demander à IFS** :
```sql
-- Réduire la taille du tablespace UNDO
ALTER DATABASE DATAFILE '<path>/undotbs01.dbf' RESIZE 2G;
-- ou créer un nouveau UNDO et basculer
```

**Risque** : Faible si la rétention UNDO et les longs transactions sont bien analysés au préalable.

**Responsable** : DBA IFS Cloud.

---

### 2.3 🥇 Désactivation du mode debug BPMN + purge des logs (gain ~3,9 Go)

**Contexte** : La table `BPMN_DEBUG_ACTIVITY_LOG_TAB` contient 3,9 Go de logs de **debug** de workflows BPMN. Le mode debug a probablement été activé à la mise en service puis oublié.

**À clarifier d'abord avec IFS** : le paramètre de niveau de log BPMN se trouve-t-il côté admin client (Solution Manager › Background Processing / Workflow settings, accessible à nous) ou côté IFS Cloud Ops ? Si c'est côté client, c'est à nous de le désactiver — la purge effective des 3,9 Go reste à demander à IFS (privilèges DBA `IFSAPP`).

**Action** :
1. **Demander à IFS** le chemin exact pour vérifier/modifier le paramètre BPMN debug.
2. **Désactiver le mode debug en production** (côté client si accessible, sinon ticket IFS).
3. Purger les logs existants (requiert privilèges DBA IFS Cloud) :
```sql
-- (À exécuter sous compte IFSAPP avec validation IFS)
DELETE FROM IFSAPP.BPMN_DEBUG_ACTIVITY_LOG_TAB
WHERE created_date < SYSDATE - 30;
COMMIT;

-- Puis réorganisation
ALTER TABLE IFSAPP.BPMN_DEBUG_ACTIVITY_LOG_TAB MOVE LOB(variables) STORE AS (TABLESPACE IFSAPP_LOB);
```

**Risque** : Aucun (logs de debug uniquement).

**Responsable** : Admin IFS (config) + DBA IFS Cloud (purge effective).

---

## 3. Détail des actions Priorité 2 (P2)

### 3.1 🥈 Politique de rétention IAM (gain ~4 Go)

**Contexte** : Les tables d'audit IAM accumulent les événements de connexion sans politique de rétention claire :
- `EVENT_ENTITY` (IFSIAMSYS) — 3,8 Go
- `IAM_LOGIN_EVENT_DETAIL_TAB` + indexes — 1,5 Go

**Action** : Demander à IFS de mettre en place une rétention de 90 jours (à ajuster selon obligations légales — RGPD, sectorielles).

```sql
-- Exemple (à valider avec IFS Support)
DELETE FROM IFSIAMSYS.EVENT_ENTITY
WHERE event_time < SYSTIMESTAMP - INTERVAL '90' DAY;

DELETE FROM IFSAPP.IAM_LOGIN_EVENT_DETAIL_TAB
WHERE event_time < SYSTIMESTAMP - INTERVAL '90' DAY;
```

**Risque** : Faible si la politique de rétention est documentée et conforme.

**Responsable** : Admin IFS + RSSI / DPO côté client (validation conformité).

---

### 3.2 🥈 Réduction rétention AWR (gain ~3 Go)

**Contexte** : L'AWR (Automatic Workload Repository) conserve les statistiques de performance Oracle. Par défaut 8 jours, souvent paramétré à 30 jours ou plus.

**Action à demander à IFS** :
```sql
-- Réduire la rétention AWR à 14 jours
EXEC DBMS_WORKLOAD_REPOSITORY.MODIFY_SNAPSHOT_SETTINGS(retention => 14*24*60);

-- Purger les snapshots anciens
SELECT DBMS_WORKLOAD_REPOSITORY.DROP_SNAPSHOT_RANGE(
    low_snap_id => <min>,
    high_snap_id => <max>
) FROM dual;
```

**Risque** : Aucun (l'AWR est uniquement utilisé pour le diagnostic de performance).

**Responsable** : DBA IFS Cloud.

---

## 4. Détail des actions Priorité 3 (P3)

### 4.1 🥉 Purge `LANGUAGE_FILE_IMPORT_TAB` (gain ~1 Go)

**Contexte** : Cette table conserve les fichiers d'import de traductions après import. Une fois les langues importées, les fichiers ne servent plus.

**Action** :
```sql
-- À valider avec IFS Support avant exécution
DELETE FROM IFSAPP.LANGUAGE_FILE_IMPORT_TAB
WHERE import_date < SYSDATE - 90;
COMMIT;
```

---

### 4.2 🥉 Purge `EXT_FILE_TRANS_TAB` ancien (gain ~1,5 Go)

**Contexte** : Historique des transferts de fichiers externes.

**Action** :
```sql
DELETE FROM IFSAPP.EXT_FILE_TRANS_TAB
WHERE created_date < SYSDATE - 180
  AND status IN ('COMPLETED', 'FAILED');
COMMIT;
```

---

### 4.3 🥉 Purge de la recyclebin Oracle (gain variable)

**Contexte** : La recyclebin Oracle conserve les objets supprimés.

**Action à demander à IFS** :
```sql
PURGE DBA_RECYCLEBIN;
```

**Risque** : Aucun.

---

### 4.4 🥉 Suppression des tablespaces vides (gain ~2 Go)

**Contexte** : Les tablespaces `MAINTENIX` (1 Go) et `JASPER` (1 Go) sont alloués mais vides. Probablement des modules non activés.

**Action à demander à IFS** :
1. Vérifier qu'aucun objet n'est dans ces tablespaces.
2. Si modules effectivement non utilisés, supprimer les tablespaces.

```sql
DROP TABLESPACE MAINTENIX INCLUDING CONTENTS AND DATAFILES;
DROP TABLESPACE JASPER INCLUDING CONTENTS AND DATAFILES;
```

**Risque** : À évaluer avec IFS — s'assurer que ces modules ne seront pas activés.

---

## 5. Détail des actions Priorité 4 (P4) — Long terme

### 5.1 🏅 Cleanup framework `FND_MODEL_*` (gain potentiel ~5 Go)

**Contexte** : Les tables `FND_MODEL_DESIGN_TAB` (5,5 Go), `FND_MODEL_API_DOC_TAB` (3,1 Go) et `FND_MODEL_DESIGN_DATA_TAB` (3 Go) totalisent 11,6 Go. Elles contiennent les modèles UI Aurena et la doc API.

**Action** : Ouvrir un **ticket IFS Support** demandant la procédure de cleanup officielle pour la version **25R2**.

**Questions à poser à IFS Support** :
1. Existe-t-il une API ou un job de cleanup sur `FND_MODEL_*` ?
2. Les anciennes versions de modèles sont-elles purgées automatiquement ?
3. La doc API peut-elle être régénérée à la demande plutôt que stockée intégralement ?
4. Quel est le ratio attendu sur ces tables pour une base de notre profil ?

---

### 5.2 🥇 Activation `Cloud File Storage` IFS — repositionnée P1 court terme (gain ~10 Go + trajectoire évitée)

**⚠️ Contexte révisé (mai 2026)** : l'analyse documentaire détaillée (cf. `05_Analyse_documents_DocMan.md` section 7) a établi que **88 % des 10 Go d'EDM viennent de deux contributeurs principaux** : **Talend (78 %)** qui dépose automatiquement les PJ factures fournisseurs depuis mars 2026 (obligation légale 10 ans → impurgeable), et **NELGRA (10 %)** qui dépose manuellement les factures clients depuis avril 2025 (~100 docs/mois).

**Trajectoire** : Talend ajoute ~3 Go/mois en croisière, soit **+36 Go/an, +180 Go sur 5 ans, +360 Go sur 10 ans**. Sans action, le poste EDM dominera l'évolution du stockage IFS.

**Solution standard IFS, déjà documentée et disponible** : le service `Cloud File Storage` (Solution Manager User Guide › Additional IFS Cloud Configuration › Cloud File Storage) permet de stocker les documents sur **Azure Blob Storage** au lieu de la BDD Oracle, **nativement en mode Cloud SaaS**. Citation directe de la doc IFS :

> *"In the Cloud deployment model, the File Storage uses an Azure Blob Storage Account to store files. A storage account is provisioned automatically per environment."*

**Contexte historique** : nous avions choisi de ne pas activer cette feature au provisionnement initial du tenant. Avec l'arrivée du flux Talend, ce choix est à reconsidérer.

**Action** (priorité haute, court terme) :
1. **Ouvrir un ticket IFS** demandant l'activation de `Cloud File Storage` sur notre tenant, ou la confirmation qu'on peut l'activer côté admin :
   - **Media Item Setup** : Solution Manager › Object Properties › Object LU `MediaItem` › property `REPOSITORY` → valeur `FILE_STORAGE`
   - **Document Management Setup** : Solution Manager › Document Management › Repositories → ajouter un nouveau Repository, Type = `File Storage`, Document Class = `*` (ou cibler `DOC A GARDER`, `INVOICE` d'abord), Status = `Generating`
2. **Migrer les 10 Go existants** via le Web Assistant intégré (selon la doc Migration Tool : *"For 'smaller' installations ... there are two IFS Cloud Web assistants for moving document files and media items to IFS Cloud File Storage: Transfer Documents / Transfer Media. **That option is fully automatic and is preferable to using this tool.**"*). On est dans ce cas (DB déjà en Cloud), pas dans le cas "FS Mig Tool externe" (réservé aux upgrades Apps 8/9/10 → Cloud).
3. **Basculer l'ancien repository en `Usable`** (read-only) ou le supprimer une fois vide.
4. **Pour les nouveaux dépôts** : Talend et NELGRA continuent de pousser via l'API standard IFS DocMan — le service `Cloud File Storage` intercepte transparentement et stocke sur Azure Blob (REST API abstrait le storage).

**Risque** : Faible. La doc IFS décrit la procédure comme *"Setting up IFS Cloud File Storage is an easy task."* et le Web Assistant de migration est *"fully automatic"*. Pas de perte fonctionnelle — les documents restent accessibles via les mêmes URLs/projections IFS.

**Gain économique attendu** : Le stockage objet est typiquement **10× moins cher au Go** que le stockage BDD. Sur la trajectoire Talend, l'économie cumulée se chiffre rapidement en milliers d'euros par an.

**Pourquoi ça remplace une purge** : la purge classique ne peut PAS s'appliquer aux PJ factures (obligation 10 ans). L'activation de `Cloud File Storage` est donc le **seul levier qui adresse réellement le volume documentaire** chez nous — et c'est une feature IFS standard, pas une demande exotique.

---

## 6. Calendrier suggéré

```
Semaine 1  ────────────────────────────────────
  ▸ Demande de purge WRI$_ADV_OBJECTS         (gain 10,9 Go)
  ▸ Désactivation debug BPMN + purge logs      (gain 3,9 Go)
  ▸ Réduction rétention AWR                   (gain 3 Go)
  ▸ Purge LANGUAGE_FILE_IMPORT_TAB            (gain 1 Go)
  ▸ Purge recyclebin                          (gain variable)
  ▸ **Ticket IFS : activer Cloud File Storage + planifier migration EDM**
                                              ─────────────
                                  GAIN W1 :    ~19 Go (+ activation FSS lancée)

Semaine 2-3 ──────────────────────────────────
  ▸ Resize UNDOTBS1                           (gain 7 Go)
  ▸ Politique rétention IAM (90j)             (gain 4 Go)
  ▸ Purge EXT_FILE_TRANS_TAB                  (gain 1,5 Go)
  ▸ Validation/suppression MAINTENIX, JASPER  (gain 2 Go)
  ▸ **Migration EDM via Transfer Documents Web Assistant** (gain ~10 Go)
                                              ─────────────
                                 GAIN W2-3 :  ~24,5 Go

Mois 2-3 ──────────────────────────────────────
  ▸ Ticket FND_MODEL_* cleanup
  ▸ Suivi : croissance EDM désormais sur Azure Blob (hors stockage BDD)
                                              ─────────────
                                CIBLE 3 MOIS :  **~78 Go** (BDD Oracle) + Azure Blob pour EDM
```

---

## 7. Suivi à mettre en place

Après chaque purge, relancer les rapports de référence pour mesurer le gain :

```sql
-- Suivi par tablespace
SELECT tablespace_name,
       ROUND(SUM(bytes)/1024/1024/1024, 2) AS allocated_gb
FROM dba_data_files
GROUP BY tablespace_name
ORDER BY SUM(bytes) DESC;

-- Suivi par owner
SELECT owner,
       ROUND(SUM(bytes)/1024/1024/1024, 2) AS used_gb
FROM dba_segments
GROUP BY owner
ORDER BY SUM(bytes) DESC;

-- Suivi top segments
SELECT owner, segment_name, segment_type,
       ROUND(bytes/1024/1024, 0) AS size_mb
FROM dba_segments
ORDER BY bytes DESC;
```

Constituer un **tableau de bord mensuel** avec :
- Volume total alloué
- Volume utilisé par catégorie (CLIENT / IFS-APP / IFS-OPS / ORACLE)
- Évolution mois après mois
- Croissance projetée

---

## 8. Tableau récapitulatif des gains

| Phase | Gain cumulé | Volume cible |
|-------|-------------|--------------|
| État actuel | — | 122 Go |
| Après actions P1 + AWR | -22 Go | ~100 Go |
| Après actions P2 + P3 | -8 Go | ~92 Go |
| Après actions P4 (long terme) | -10 Go | ~82 Go |

**Gain total potentiel : ~40 Go** (122 → 82 Go) en supprimant uniquement des éléments techniques, sans aucun impact sur les données métier.
