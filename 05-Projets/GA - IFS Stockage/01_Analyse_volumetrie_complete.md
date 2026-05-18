# 📊 Analyse volumétrique complète — Base de données IFS 25R2

## 1. Périmètre et méthodologie

### 1.1 Source des données
Analyse réalisée à partir de requêtes SQL directes sur les vues système Oracle accessibles depuis l'outil **Rapport Rapide IFS** :
- `DBA_SEGMENTS` (segments par owner, type, tablespace)
- `DBA_DATA_FILES` (datafiles alloués)
- `DBA_FREE_SPACE` (espace libre par tablespace)
- `ALL_LOBS` (mapping LOBSEGMENT → table/colonne)
- `ALL_TABLES` (statistiques tables)

### 1.2 Limites
- `DBA_LOBS`, `DBA_TABLES`, `CDB_*` non accessibles depuis l'environnement IFS Cloud.
- Volumes TEMP, UNDO, redo logs, archive logs non détaillés (estimés par différence).
- Analyse statique à un instant T.

---

## 2. Vue d'ensemble — 122 Go

### 2.1 Réconciliation avec le chiffre IFS

| Niveau de mesure | Volume | Commentaire |
|------------------|--------|-------------|
| **Volume facturé IFS** | **122 Go** | Vue facturation |
| Datafiles alloués (`DBA_DATA_FILES`) | ~100 Go | Espace réservé sur disque |
| Segments réellement remplis (`DBA_SEGMENTS`) | ~82 Go | Données effectives |
| Données IFSAPP + IFSIAMSYS uniquement | ~50 Go | Données applicatives IFS |
| **Données métier client (transactions + documents)** | **~13 Go** | **Notre usage réel** |

### 2.2 Différence entre les niveaux

```
┌──────────────────────────────────────────────────┐
│ 122 Go - Vue IFS / disque                         │
│  ├─ ~22 Go TEMP/UNDO/redo (non visibles segments) │
│  └─ ~100 Go datafiles                              │
│      ├─ ~20 Go espace vide alloué                  │
│      └─ ~80 Go segments remplis                    │
│          ├─ ~50 Go schémas IFSAPP/IAMSYS           │
│          │   ├─ ~13 Go données métier              │
│          │   └─ ~37 Go framework, logs, audit IFS  │
│          ├─ ~27 Go schéma SYS (Oracle système)     │
│          └─ ~3 Go autres schémas                   │
└──────────────────────────────────────────────────┘
```

---

## 3. Décomposition par tablespace

| Tablespace | Alloué | Utilisé | Libre | Description |
|------------|--------|---------|-------|-------------|
| `IFSAPP_LOB` | 30,2 Go | 28,7 Go | 1,5 Go | Fichiers binaires IFS (DocMan, LOB) |
| `SYSAUX` | 15,5 Go | 14,8 Go | 0,8 Go | Oracle système (AWR, stats annexes) |
| `IFSAPP_DATA` | 13,0 Go | 12,4 Go | 0,7 Go | Tables IFS |
| `SYSTEM` | 12,7 Go | 12,7 Go | 0,0 Go | Dictionnaire Oracle, code PL/SQL |
| `IFSAPP_INDEX` | 9,1 Go | 8,6 Go | 0,5 Go | Index IFS |
| `UNDOTBS1` | 8,7 Go | 0,4 Go | 8,3 Go | Undo Oracle (95 % vide) |
| `AUDIT_DATA_TBSP` | 8,3 Go | 1,9 Go | 6,4 Go | Audit Oracle (77 % vide) |
| `MAINTENIX` | 1,0 Go | 0,0 Go | 1,0 Go | Vide (module MRO ?) |
| `JASPER` | 1,0 Go | 0,0 Go | 1,0 Go | Vide (JasperReports ?) |
| Autres petits | < 0,3 Go | — | — | Reporting, USERS, archive |
| **TOTAL DATAFILES** | **~100 Go** | **~80 Go** | **~20 Go** | |

### Observations notables
- **20 Go d'espace alloué vide** dans les datafiles, dont 8,3 Go d'UNDO presque vide et 6,4 Go d'audit non utilisés.
- Deux tablespaces complets (`MAINTENIX`, `JASPER`) de 1 Go chacun sont vides — modules non utilisés.

---

## 4. Décomposition par propriétaire (schéma)

| Owner | Volume | Part | Nature |
|-------|--------|------|--------|
| **IFSAPP** | 44,8 Go | 55 % | Application IFS principale |
| **SYS** | 27,4 Go | 34 % | Oracle système (PL/SQL compilé, AWR, dictionnaire) |
| **IFSIAMSYS** | 4,6 Go | 6 % | Audit et authentification IFS (IAM) |
| **AUDSYS** | 1,9 Go | 2 % | Audit Oracle natif |
| **IFSCAMSYS** | 0,5 Go | <1 % | IFS Connect / Auth |
| **XDB** | 54 Mo | <1 % | XML Oracle |
| **WMSYS** | 7 Mo | <1 % | Workspace Manager |
| **CTXSYS** | 4 Mo | <1 % | Oracle Text |
| Autres | < 5 Mo | <1 % | GSMADMIN_INTERNAL, OJVMSYS, etc. |

---

## 5. Top 20 des objets logiques (table + LOB + index agrégés)

| Rang | Volume | Objet | Catégorie |
|------|--------|-------|-----------|
| 1 | 11,0 Go | **`WRI$_ADV_OBJECTS`** (SYS) | 🔧 Bug Oracle - SQL Tuning Advisor |
| 2 | 10,1 Go | `EDM_FILE_STORAGE_TAB` | 📁 Documents métier (DocMan) |
| 3 | 5,5 Go | `FND_MODEL_DESIGN_TAB` | 🏢 Framework UI IFS |
| 4 | 4,9 Go | `SOURCE$` + `IDL_*` (SYS) | 🏢 Code PL/SQL IFS compilé |
| 5 | 3,9 Go | `BPMN_DEBUG_ACTIVITY_LOG_TAB` | 🏢 Logs debug workflows IFS |
| 6 | 3,8 Go | `EVENT_ENTITY` (IFSIAMSYS) | 🏢 Événements IAM |
| 7 | 3,1 Go | `FND_MODEL_API_DOC_TAB` | 🏢 Documentation API IFS |
| 8 | 3,0 Go | `FND_MODEL_DESIGN_DATA_TAB` | 🏢 Données modèles UI IFS |
| 9 | 2,0 Go | `C_TOID_VERSION#` (SYS) | 🏢 Versions des types Oracle |
| 10 | 1,7 Go | `EXT_FILE_TRANS_TAB` | 🏢 Logs transferts fichiers IFS |
| 11 | 1,5 Go | `IAM_LOGIN_EVENT_DETAIL_*` | 🏢 Audit connexions IFS |
| 12 | 1,3 Go | `SYS_LOB...22938...` | 🏢 LOB système Oracle |
| 13 | 1,0 Go | `LANGUAGE_FILE_IMPORT_TAB` | 🏢 Imports de traductions IFS |
| 14 | 0,8 Go | `CLIENT_PROFILE_HANDLING_XML...` | 🏢 Profils client IFS |
| 15 | 0,6 Go | `PDF_ARCHIVE_TAB` | 📁 Archives PDF |
| 16 | 0,5 Go | `CONSTRAINT_4` (IFSIAMSYS) | 🏢 Index IAM |
| 17 | 0,4 Go | `LANGUAGE_SYS_TAB` | 🏢 Système de traductions IFS |
| 18 | 0,4 Go | `IDX_EVENT_TIME` (IFSIAMSYS) | 🏢 Index audit IAM |
| 19 | 0,4 Go | `LANGUAGE_CONTEXT_TAB` | 🏢 Contexte de traductions IFS |
| 20 | 0,2 Go | `XLR_META_DATA_ARCHIVE_TAB` | 🏢 Lobby/Reporting IFS |

> 📁 = Données générées par notre usage
> 🏢 = Généré par IFS / Oracle, hors de notre contrôle direct
> 🔧 = Défaut technique (bug ou défaut d'administration)

---

## 6. Décomposition fonctionnelle des données IFSAPP + IFSIAMSYS

| Catégorie | Volume | % de IFSAPP+IAMSYS | Notre contrôle ? |
|-----------|--------|--------------------|--------------------|
| Framework UI / Métadonnées Aurena | 11,7 Go | 24 % | ❌ Non |
| Documents métier (DocMan/EDM) | 10,1 Go | 20 % | ✅ Oui (uploads utilisateurs) |
| Sécurité / Audit / IAM | 6,9 Go | 14 % | ⚠️ Partiel (rétention) |
| Index et structures techniques | 6,4 Go | 13 % | ❌ Non |
| Traductions / Multi-langues | 5,0 Go | 10 % | ❌ Non |
| Workflows BPMN (logs debug) | 3,9 Go | 8 % | ⚠️ Mode debug activable |
| Imports / Archives fichiers | 3,4 Go | 7 % | ⚠️ Partiel |
| **Données métier transactionnelles** | **1,3 Go** | **2,5 %** | ✅ Oui |
| Profils client | 1,1 Go | 2 % | ❌ Non |
| Lobby / Reporting | 0,07 Go | <1 % | ✅ Oui |

### ⚠️ Constat majeur
**Sur les ~50 Go de schémas applicatifs IFS, seuls ~13 Go (26 %) sont des données générées par notre activité métier** :
- ~10 Go de documents uploadés (EDM)
- ~1,3 Go de transactions (factures, écritures comptables, etc.)
- ~1,5 Go d'usage divers (configurations, lobby, archives PDF utiles)

**Les 37 Go restants relèvent du fonctionnement interne d'IFS**.

---

## 7. Détail du schéma SYS (27,3 Go) — Oracle système

| Sous-catégorie | Volume | % de SYS | Description |
|----------------|--------|----------|-------------|
| **AWR / SQL Tuning Advisor** (`WRI$_*`, `WRH$_*`) | 13,1 Go | 47 % | Stats perf historiques + bug `WRI$_ADV_OBJECTS` |
| **Dictionnaire PL/SQL compilé** (`SOURCE$`, `IDL_*`, `C_*`) | 8,5 Go | 31 % | Code IFS stocké comme procédures Oracle |
| Index système | 2,7 Go | 10 % | Index sur tables système |
| LOB système | 2,4 Go | 9 % | LOB internes Oracle |
| Statistiques optimiseur | 0,4 Go | 2 % | Stats CBO |
| Scheduler Oracle | 0,3 Go | 1 % | Logs jobs Oracle |
| Audit Oracle (`AUD$`) | <1 Mo | 0 % | Vide (probablement migré vers AUDSYS) |
| Autres | 0,4 Go | 1 % | Divers |

### Top 5 segments SYS

| Volume | Segment | Nature |
|--------|---------|--------|
| 4 897 Mo | `WRI$_ADV_OBJECTS` | 🔧 **Bug Oracle** - SQL Tuning Advisor non purgé |
| 3 076 Mo | `SOURCE$` | Code source PL/SQL (packages IFS) |
| 2 417 Mo | `WRI$_ADV_OBJECTS_IDX_01` | 🔧 Index du bug ci-dessus |
| 2 048 Mo | `C_TOID_VERSION#` | Versions des types Oracle |
| 2 016 Mo | `WRI$_ADV_OBJECTS_IDX_02` | 🔧 Index du bug ci-dessus |

**Les segments `WRI$_ADV_OBJECTS` et ses 3 index totalisent à eux seuls 10,9 Go** — soit ~9 % de la base totale, sur une table qui devrait être maintenue à quelques Mo en condition normale.

---

## 8. Annexe — Évolution potentielle

### Croissance attendue par catégorie (sans action)
- Documents (EDM) : croissance linéaire avec l'activité utilisateur
- Logs IAM (`EVENT_ENTITY`, `IAM_LOGIN_EVENT_*`) : croissance forte si pas de rétention
- BPMN debug : continuera de croître tant que le mode debug est actif
- `WRI$_ADV_OBJECTS` : croissance illimitée (bug non corrigé)
- Framework `FND_MODEL_*` : croissance par paliers à chaque mise à jour IFS
- Données métier : croissance maîtrisée, faible

### Risque de dérive
Sans action sur les éléments hors contrôle, la base peut atteindre **150 Go d'ici 6 à 12 mois** avec une part "données utiles" qui restera à ~13-15 Go (~10 % du total).
