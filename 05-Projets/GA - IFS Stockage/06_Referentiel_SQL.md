# 📚 Référentiel SQL — Analyse volumétrie base IFS Cloud

> **Usage** : Recueil des requêtes SQL utilisées pour analyser la volumétrie de la base de données IFS Cloud (25R2), réutilisables via l'outil **Rapport Rapide IFS** ou un client SQL classique.
>
> **Cible** : Administrateurs IFS internes et DBA pour suivre l'évolution de la volumétrie ou refaire l'analyse périodiquement.

---

## 🚦 Avertissement préalable — Contraintes du Rapport Rapide IFS

L'outil **Rapport Rapide** d'IFS Cloud est restrictif quant aux requêtes SQL acceptées. Les contraintes observées sont :

| Construction SQL | Statut |
|------------------|--------|
| `SELECT` simple avec `WHERE` / `ORDER BY` | ✅ Autorisé |
| `LIKE` avec wildcards | ✅ Autorisé |
| Fonctions scalaires (`ROUND`, `TO_CHAR`, `SUBSTR`...) | ✅ Autorisé |
| `DBMS_LOB.GETLENGTH(col)` | ✅ Autorisé |
| `ROWNUM` dans `WHERE` | ✅ Autorisé |
| **`GROUP BY` / `COUNT()` / `SUM()`** | ❌ **Bloqué** |
| **`JOIN` (toute forme : INNER, LEFT, syntaxe `(+)`)** | ❌ **Bloqué** |
| **Sous-requêtes** (`SELECT ... FROM (SELECT ...)`) | ❌ **Bloqué** |
| **`FETCH FIRST N ROWS ONLY`** | ❌ **Bloqué** |
| **Fonctions analytiques** (`RANK() OVER`, etc.) | ❌ **Bloqué** |
| Vues `CDB_*` | ❌ Pas d'accès |
| Vues `DBA_LOBS`, `DBA_TABLES`, `DBA_OBJECTS` | ❌ Pas de droits |
| Vues `DBA_SEGMENTS`, `DBA_DATA_FILES`, `DBA_FREE_SPACE` | ✅ Accessibles |
| Vues `ALL_LOBS`, `ALL_TABLES`, `ALL_TAB_COLUMNS` | ✅ Accessibles |

### Stratégie d'analyse face à ces contraintes
1. **Faire des requêtes "plates"** : SELECT simple sans JOIN ni agrégation.
2. **Exporter les résultats en xlsx** depuis le Rapport Rapide.
3. **Agréger / joindre / analyser côté Python ou Excel** une fois les données extraites.

---

## 1️⃣ Analyse globale de la volumétrie

### 1.1 Volume par segment (tous schémas) — vue détaillée

```sql
SELECT owner,
       segment_name,
       segment_type,
       tablespace_name,
       ROUND(bytes / 1024 / 1024, 0) AS size_mb
FROM dba_segments
ORDER BY bytes DESC
```

**À quoi ça sert** : Liste exhaustive de tous les objets stockés (tables, index, LOB, clusters) avec leur taille. C'est la **requête de référence** pour identifier les plus gros consommateurs d'espace.

**Volume typique** : ~10 000 lignes pour une base IFS Cloud — export léger.

**À combiner avec** : la requête 3.1 (mapping LOB→table) pour comprendre les segments `SYS_LOB...`.

---

### 1.2 Datafiles alloués par tablespace

```sql
SELECT tablespace_name,
       ROUND(SUM(bytes) / 1024 / 1024, 0) AS allocated_mb,
       ROUND(SUM(bytes) / 1024 / 1024 / 1024, 2) AS allocated_gb,
       COUNT(*) AS nb_files
FROM dba_data_files
GROUP BY tablespace_name
ORDER BY SUM(bytes) DESC
```

> ⚠️ **Cette requête contient `GROUP BY` et `SUM`** — elle a fonctionné dans le test mais peut être bloquée selon votre configuration. Si bloquée, retirez les agrégations :
> ```sql
> SELECT tablespace_name,
>        ROUND(bytes / 1024 / 1024, 0) AS allocated_mb,
>        file_name
> FROM dba_data_files
> ORDER BY bytes DESC
> ```

**À quoi ça sert** : Mesure l'**espace alloué physiquement** par Oracle (≠ espace utilisé). Permet de comparer ce qu'IFS facture (basé sur l'allocation physique typiquement) à ce qui est réellement utilisé.

---

### 1.3 Espace libre par tablespace

```sql
SELECT tablespace_name,
       ROUND(SUM(bytes) / 1024 / 1024, 0) AS free_mb
FROM dba_free_space
GROUP BY tablespace_name
ORDER BY SUM(bytes) DESC
```

**À quoi ça sert** : Identifie l'espace **alloué mais vide** — utile pour repérer la sur-allocation (UNDO presque vide, tablespaces de modules non utilisés, etc.).

**Croisement utile** : `allocated_mb - free_mb = used_mb` (espace réellement occupé).

---

### 1.4 Volume par propriétaire (schéma)

```sql
SELECT owner,
       ROUND(SUM(bytes) / 1024 / 1024, 0) AS size_mb,
       COUNT(*) AS nb_segments
FROM dba_segments
GROUP BY owner
ORDER BY SUM(bytes) DESC
```

**À quoi ça sert** : Décompose la base par schéma applicatif (IFSAPP, IFSIAMSYS, SYS, AUDSYS...). Met en évidence le poids relatif de chaque module IFS et d'Oracle.

---

### 1.5 Volume par tablespace (espace réellement utilisé)

```sql
SELECT tablespace_name,
       ROUND(SUM(bytes) / 1024 / 1024, 0) AS used_mb
FROM dba_segments
GROUP BY tablespace_name
ORDER BY SUM(bytes) DESC
```

**À quoi ça sert** : Vue agrégée par tablespace de l'espace effectivement consommé par les segments.

---

## 2️⃣ Détail du schéma SYS (Oracle système)

### 2.1 Tous les segments du schéma SYS

```sql
SELECT segment_name,
       segment_type,
       ROUND(bytes / 1024 / 1024, 0) AS size_mb,
       tablespace_name
FROM dba_segments
WHERE owner = 'SYS'
ORDER BY bytes DESC
```

**À quoi ça sert** : Permet d'identifier les composants Oracle système qui occupent le plus de place. C'est là qu'on trouve :
- `WRI$_ADV_OBJECTS` (stockage SQL Tuning Advisor — souvent surdimensionné = bug)
- `SOURCE$`, `IDL_UB1$`, `C_TOID_VERSION#` (code PL/SQL IFS compilé)
- `WRH$_*` (statistiques AWR)
- Tables système Oracle (dictionnaire, scheduler, stats CBO)

**Indicateur clé** : si `WRI$_ADV_OBJECTS` dépasse 500 Mo, c'est anormal et purgeable.

---

## 3️⃣ Analyse des LOB (Large Objects) et tables

### 3.1 Mapping LOBSEGMENT → table/colonne

```sql
SELECT owner,
       segment_name,
       table_name,
       column_name
FROM all_lobs
WHERE owner IN ('IFSAPP', 'IFSIAMSYS')
ORDER BY segment_name
```

**À quoi ça sert** : Les LOBSEGMENT ont des noms générés (`SYS_LOB0000065924C00009$$`) qui ne disent rien. Cette requête fait le **lien entre le segment et la table/colonne** qu'il stocke.

**Convention Oracle** : `SYS_LOB<object_id>C<column_id>$$` — donc `SYS_LOB0000075310C00014$$` est la colonne 14 de l'objet 75310.

**Usage typique** : croiser avec la requête 1.1 dans Excel/Python (Power Query, pandas) pour enrichir les LOBSEGMENT avec leur vraie origine.

---

### 3.2 Statistiques des tables

```sql
SELECT owner,
       table_name,
       num_rows,
       blocks,
       ROUND(blocks * 8 / 1024, 0) AS size_mb_approx
FROM all_tables
WHERE owner IN ('IFSAPP', 'IFSIAMSYS')
ORDER BY blocks DESC
```

**À quoi ça sert** : Vue alternative axée sur le nombre de lignes et la taille en blocs. Utile pour repérer les tables avec beaucoup de lignes (≠ tables avec beaucoup de blobs).

> ⚠️ `num_rows` et `blocks` sont mis à jour par les statistiques Oracle, qui peuvent être obsolètes. Pour des chiffres exacts en temps réel, préférer `DBA_SEGMENTS`.

---

### 3.3 Structure d'une table (liste des colonnes)

```sql
SELECT column_name,
       data_type,
       data_length,
       nullable
FROM all_tab_columns
WHERE owner = 'IFSAPP'
  AND table_name = 'NOM_DE_LA_TABLE'
ORDER BY column_id
```

**À quoi ça sert** : Explorer la structure d'une table inconnue avant de l'interroger. Indispensable car les noms de colonnes IFS peuvent varier d'une version à l'autre.

**Usage typique** : avant d'écrire une requête sur `EDM_FILE_STORAGE_TAB`, on a d'abord listé ses colonnes ainsi.

---

## 4️⃣ Recherche de tables par motif

### 4.1 Tables liées aux fichiers / documents

```sql
SELECT table_name
FROM all_tables
WHERE owner = 'IFSAPP'
  AND (table_name LIKE 'EDM%'
       OR table_name LIKE 'DOC_%'
       OR table_name LIKE '%FILE%')
ORDER BY table_name
```

**À quoi ça sert** : Identifier les tables potentiellement liées au stockage de fichiers / DocMan.

**Astuce** : pour exclure les **tables virtuelles d'Aurena** (vues UI temporaires, suffixées `_VIRTUAL_VRT`) qui polluent les résultats, ajouter :
```sql
  AND table_name NOT LIKE '%VIRTUAL_VRT'
  AND table_name NOT LIKE '%HANDLING%'
```

---

### 4.2 Recherche large sur un préfixe / mot-clé

```sql
SELECT table_name
FROM all_tables
WHERE owner = 'IFSAPP'
  AND table_name LIKE '%MOT_CLE%'
ORDER BY table_name
```

**À quoi ça sert** : Exploration générale pour comprendre quels modules touchent un domaine fonctionnel (`%INVOICE%`, `%VOUCHER%`, `%CUSTOMER%`, etc.).

---

## 5️⃣ Analyse des documents (module DocMan)

### 5.1 Inventaire des documents (métadonnées sans BLOB)

```sql
SELECT doc_class,
       doc_no,
       doc_sheet,
       doc_rev,
       doc_type,
       file_no,
       entity_type,
       created_by,
       created_date,
       local_file_name
FROM ifsapp.edm_file_storage_tab
ORDER BY created_date DESC
```

**À quoi ça sert** : Lister tous les documents stockés avec leurs métadonnées, **sans extraire le contenu binaire** (qui ferait planter l'export).

> ⚠️ **Ne JAMAIS sélectionner `file_data`** dans une telle requête — c'est le BLOB de plusieurs Go et l'export deviendrait inexploitable.

**Limite observée** : sur le système analysé, les colonnes `created_by`, `created_date`, `entity_type`, `local_file_name` sont vides à 100 %. À investiguer côté config IFS.

---

### 5.2 Taille de chaque fichier (via DBMS_LOB)

```sql
SELECT doc_class,
       doc_type,
       file_no,
       DBMS_LOB.GETLENGTH(file_data) AS bytes_size
FROM ifsapp.edm_file_storage_tab
```

**À quoi ça sert** : Récupérer la **taille en octets** de chaque fichier individuellement, sans lire le contenu du BLOB.

**Performance** : `DBMS_LOB.GETLENGTH` lit uniquement les métadonnées du LOB locator, donc rapide même sur des Go.

**Usage typique** : croiser avec la requête 5.1 pour produire une analyse complète par classe documentaire (volume, taille moyenne, top fichiers).

---

### 5.3 Top des plus gros fichiers

```sql
SELECT doc_class,
       doc_no,
       doc_sheet,
       doc_rev,
       DBMS_LOB.GETLENGTH(file_data) AS bytes_size
FROM ifsapp.edm_file_storage_tab
ORDER BY DBMS_LOB.GETLENGTH(file_data) DESC
```

**À quoi ça sert** : Identifier directement les fichiers les plus volumineux (les premières lignes du résultat).

Une fois le `DOC_NO` repéré, on peut le rechercher dans l'UI IFS DocMan pour identifier son contenu et décider d'une action (conservation / suppression / externalisation).

---

## 6️⃣ Requêtes de purge (à exécuter par DBA / référent IFS)

> ⚠️ **Toutes ces requêtes nécessitent des privilèges étendus et doivent être validées par un DBA Oracle ou par le support IFS Cloud.** Ne pas exécuter en self-service.

### 6.1 Purger `WRI$_ADV_OBJECTS` (SQL Tuning Advisor)

```sql
-- 1. Lister les tâches advisor existantes
SELECT task_id, task_name, status, created
FROM dba_advisor_tasks
ORDER BY created;

-- 2. Supprimer les anciennes tâches
EXEC DBMS_ADVISOR.DELETE_TASK('SYS_AUTO_SQL_TUNING_TASK');

-- 3. Réorganiser la table après purge
ALTER TABLE SYS.WRI$_ADV_OBJECTS MOVE;
ALTER INDEX SYS.WRI$_ADV_OBJECTS_PK REBUILD;
ALTER INDEX SYS.WRI$_ADV_OBJECTS_IDX_01 REBUILD;
ALTER INDEX SYS.WRI$_ADV_OBJECTS_IDX_02 REBUILD;
```

**Gain attendu** : ~10 Go.
**Référence Oracle** : Notes 1281703.1 et 2030447.1.

---

### 6.2 Réduire la rétention AWR

```sql
-- Réduire la rétention à 14 jours (au lieu de 30+ par défaut sur certaines installations)
EXEC DBMS_WORKLOAD_REPOSITORY.MODIFY_SNAPSHOT_SETTINGS(retention => 14*24*60);

-- Identifier les snapshots à purger
SELECT MIN(snap_id), MAX(snap_id), MIN(begin_interval_time), MAX(end_interval_time)
FROM dba_hist_snapshot;

-- Purger une plage de snapshots
EXEC DBMS_WORKLOAD_REPOSITORY.DROP_SNAPSHOT_RANGE(low_snap_id => 1000, high_snap_id => 5000);
```

**Gain attendu** : ~3 Go (selon la rétention initiale).

---

### 6.3 Resize du tablespace UNDO

```sql
-- Vérifier d'abord les transactions actives et la rétention UNDO
SELECT name, value FROM v$parameter WHERE name LIKE '%undo%';

-- Identifier les datafiles UNDO
SELECT file_name, ROUND(bytes/1024/1024,0) AS mb
FROM dba_data_files
WHERE tablespace_name = 'UNDOTBS1';

-- Réduire (à valider en environnement de test d'abord)
ALTER DATABASE DATAFILE '<chemin>/undotbs01.dbf' RESIZE 2G;
```

**Gain attendu** : ~7 Go si l'UNDO est sur-dimensionné.

---

### 6.4 Vider la recyclebin Oracle

```sql
-- Voir le contenu
SELECT * FROM dba_recyclebin;

-- Purger
PURGE DBA_RECYCLEBIN;
```

**Gain attendu** : variable, souvent quelques centaines de Mo à plusieurs Go.

---

### 6.5 Purge des logs de debug BPMN (côté IFS)

```sql
-- À valider avec IFS Support — vérifier d'abord que le mode debug est désactivé
DELETE FROM IFSAPP.BPMN_DEBUG_ACTIVITY_LOG_TAB
WHERE created_date < SYSDATE - 30;
COMMIT;

-- Récupérer l'espace dans le LOB
ALTER TABLE IFSAPP.BPMN_DEBUG_ACTIVITY_LOG_TAB
  MOVE LOB(variables) STORE AS (TABLESPACE IFSAPP_LOB);
```

**Gain attendu** : ~4 Go (selon historique).

---

### 6.6 Purge avec rétention IAM

```sql
-- Événements IAM (authentification) — exemple sur 90 jours de rétention
DELETE FROM IFSIAMSYS.EVENT_ENTITY
WHERE event_time < SYSTIMESTAMP - INTERVAL '90' DAY;

DELETE FROM IFSAPP.IAM_LOGIN_EVENT_DETAIL_TAB
WHERE event_time < SYSTIMESTAMP - INTERVAL '90' DAY;

COMMIT;
```

**Gain attendu** : ~4 Go (à adapter selon votre politique de rétention et exigences RGPD).

---

### 6.7 Purge des imports de langues

```sql
DELETE FROM IFSAPP.LANGUAGE_FILE_IMPORT_TAB
WHERE import_date < SYSDATE - 90;
COMMIT;
```

**Gain attendu** : ~1 Go.

---

### 6.8 Purge des transferts externes

```sql
DELETE FROM IFSAPP.EXT_FILE_TRANS_TAB
WHERE created_date < SYSDATE - 180
  AND status IN ('COMPLETED', 'FAILED');
COMMIT;
```

**Gain attendu** : ~1,5 Go.

---

### 6.9 Suppression des tablespaces inutilisés

```sql
-- Vérifier qu'aucun objet n'est dedans
SELECT COUNT(*) FROM dba_segments WHERE tablespace_name = 'MAINTENIX';
SELECT COUNT(*) FROM dba_segments WHERE tablespace_name = 'JASPER';

-- Si vides et modules non utilisés
DROP TABLESPACE MAINTENIX INCLUDING CONTENTS AND DATAFILES;
DROP TABLESPACE JASPER INCLUDING CONTENTS AND DATAFILES;
```

**Gain attendu** : ~2 Go.

---

## 7️⃣ Suivi mensuel — Tableau de bord recommandé

Une fois l'analyse initiale faite, voici les requêtes à rejouer périodiquement (chaque mois) pour suivre l'évolution :

### 7.1 Indicateur principal — taille allouée totale

```sql
SELECT ROUND(SUM(bytes) / 1024 / 1024 / 1024, 2) AS total_allocated_gb
FROM dba_data_files
```
> Si bloqué par `SUM`, exporter le détail et agréger dans Excel.

### 7.2 Top 50 segments — évolution mois après mois

```sql
SELECT owner,
       segment_name,
       segment_type,
       ROUND(bytes / 1024 / 1024, 0) AS size_mb
FROM dba_segments
ORDER BY bytes DESC
```
Comparer le résultat aux exports précédents pour repérer les segments qui grossissent anormalement vite.

### 7.3 Volume documentaire — évolution

```sql
SELECT doc_class,
       file_no,
       DBMS_LOB.GETLENGTH(file_data) AS bytes_size
FROM ifsapp.edm_file_storage_tab
```
Agréger par classe en Python/Excel pour produire une courbe mensuelle par classe.

---

## 8️⃣ Bonus — Requêtes utiles non utilisées dans l'analyse

### 8.1 Indexes les plus volumineux

```sql
SELECT owner,
       segment_name AS index_name,
       tablespace_name,
       ROUND(bytes / 1024 / 1024, 0) AS size_mb
FROM dba_segments
WHERE segment_type = 'INDEX'
ORDER BY bytes DESC
```

**À quoi ça sert** : Repérer les index disproportionnés par rapport à leurs tables — peut indiquer des index obsolètes ou redondants.

### 8.2 Espace par utilisateur Oracle

```sql
SELECT owner,
       segment_type,
       ROUND(SUM(bytes) / 1024 / 1024, 0) AS size_mb
FROM dba_segments
GROUP BY owner, segment_type
ORDER BY owner, size_mb DESC
```

**À quoi ça sert** : Vue croisée propriétaire × type d'objet (table / index / lob) pour comprendre la composition de chaque schéma.

### 8.3 Tables sans statistiques

```sql
SELECT owner, table_name, last_analyzed, num_rows
FROM all_tables
WHERE owner = 'IFSAPP'
  AND (last_analyzed IS NULL OR last_analyzed < SYSDATE - 30)
ORDER BY last_analyzed
```

**À quoi ça sert** : Identifier les tables dont les statistiques Oracle sont obsolètes (impact performance).

### 8.4 Fragmentation des tablespaces

```sql
SELECT tablespace_name,
       ROUND(SUM(bytes) / 1024 / 1024, 0) AS free_mb,
       COUNT(*) AS nb_chunks,
       ROUND(MAX(bytes) / 1024 / 1024, 0) AS max_chunk_mb
FROM dba_free_space
GROUP BY tablespace_name
ORDER BY nb_chunks DESC
```

**À quoi ça sert** : Beaucoup de petits "chunks" libres = fragmentation. Indicateur de la nécessité d'un éventuel `ALTER TABLESPACE ... COALESCE`.

---

## 📋 Annexe — Vues système Oracle utiles (référence)

| Vue | Description | Statut Rapport Rapide |
|-----|-------------|------------------------|
| `DBA_SEGMENTS` | Tous les segments physiques | ✅ |
| `DBA_DATA_FILES` | Datafiles alloués | ✅ |
| `DBA_FREE_SPACE` | Espace libre par tablespace | ✅ |
| `DBA_TABLESPACES` | Liste et caractéristiques tablespaces | ✅ |
| `DBA_TAB_PARTITIONS` | Tables partitionnées | ✅ |
| `DBA_INDEXES` | Index | ✅ |
| `DBA_USERS` | Utilisateurs Oracle | ✅ |
| `DBA_ADVISOR_TASKS` | Tâches SQL Tuning Advisor | ✅ |
| `DBA_HIST_SNAPSHOT` | Snapshots AWR | ✅ |
| `DBA_RECYCLEBIN` | Recyclebin Oracle | ✅ |
| `DBA_LOBS` | Mapping LOB → table | ❌ Bloqué |
| `DBA_TABLES` | Tables | ❌ Bloqué |
| `DBA_OBJECTS` | Tous les objets | ❌ Bloqué |
| `ALL_LOBS` | Mapping LOB (limité aux objets accessibles) | ✅ |
| `ALL_TABLES` | Tables (limité aux objets accessibles) | ✅ |
| `ALL_TAB_COLUMNS` | Colonnes des tables accessibles | ✅ |
| `ALL_INDEXES` | Index des objets accessibles | ✅ |
| `CDB_*` | Vues Container Database | ❌ Pas d'accès |
| `V$DATABASE`, `V$INSTANCE` | Vues dynamiques | ❌ Généralement bloquées |

---

## 🔧 Annexe — Reproduction de l'analyse complète

Pour refaire l'analyse complète depuis zéro, exécuter dans cet ordre :

1. Requête 1.1 → export `segments.xlsx`
2. Requête 3.1 → export `lobs.xlsx`
3. Requête 1.2 → export `datafiles.xlsx`
4. Requête 1.3 → export `freespace.xlsx`
5. Requête 1.4 → export `owners.xlsx`
6. Requête 2.1 → export `sys_segments.xlsx`
7. Requête 5.2 → export `doc_sizes.xlsx`
8. Requête 5.1 → export `doc_metadata.xlsx`

Croiser ensuite ces exports dans Excel ou Python (pandas) pour produire :
- La répartition par tablespace
- La répartition par propriétaire fonctionnel (client / IFS / Oracle)
- Le détail du schéma SYS
- L'analyse documentaire
- L'identification des plus gros segments et fichiers
