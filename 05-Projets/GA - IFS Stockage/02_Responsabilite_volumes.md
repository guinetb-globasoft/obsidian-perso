# ⭐ Responsabilité des volumes — Qui génère quoi ?

> **Document central pour la négociation IFS.**
> Décomposition précise du contenu des 122 Go selon la **responsabilité** de génération et le **contrôle** que nous avons dessus.

---

## 1. Grille d'analyse

Chaque catégorie de données est classée selon **deux axes** :

### Axe 1 — Origine de la donnée

| Code | Origine | Définition |
|------|---------|------------|
| 👤 **CLIENT** | Activité utilisateur | Données créées par notre utilisation métier (transactions, documents uploadés, configurations métier) |
| 🏢 **IFS-APP** | Framework applicatif IFS | Métadonnées, modèles UI, code applicatif IFS — installées et maintenues par IFS |
| 🏢 **IFS-OPS** | Logs et audit IFS | Logs techniques, audit, debug, traces générés par le fonctionnement interne d'IFS |
| 🔧 **ORACLE** | Système Oracle | Dictionnaire Oracle, AWR, stats, structures techniques — sous responsabilité du DBA (IFS Cloud) |

### Axe 2 — Niveau de contrôle client

| Code | Contrôle | Définition |
|------|----------|------------|
| ✅ **DIRECT** | Le client peut agir directement (paramétrage, purge) |
| ⚠️ **INDIRECT** | Le client peut influencer via configuration ou demande |
| ❌ **AUCUN** | Le client n'a aucun moyen d'agir sans intervention IFS |

---

## 2. Décomposition complète des 122 Go

### 2.1 Vue par responsabilité

| Origine | Volume | % | Notre contrôle |
|---------|--------|---|----------------|
| 👤 **CLIENT** — Données métier client | **~13 Go** | **11 %** | ✅ Direct |
| 🏢 **IFS-APP** — Framework et code IFS | ~21 Go | 17 % | ❌ Aucun |
| 🏢 **IFS-OPS** — Logs et audit IFS | ~14 Go | 12 % | ⚠️ Indirect |
| 🔧 **ORACLE** — Système Oracle (sous gestion IFS) | ~28 Go | 23 % | ❌ Aucun |
| 🔧 **ORACLE** — Espace vide alloué | ~20 Go | 16 % | ❌ Aucun |
| 🔧 **ORACLE** — TEMP/UNDO/redo (estimation) | ~22 Go | 18 % | ❌ Aucun |
| Autres petits schémas Oracle | ~4 Go | 3 % | ❌ Aucun |
| **TOTAL** | **122 Go** | **100 %** | |

### 2.2 Vue agrégée

```
RESPONSABILITÉ CLIENT  →  ~13 Go  (11 %)
RESPONSABILITÉ IFS     →  ~109 Go (89 %)
```

---

## 3. Détail des données générées par le CLIENT (~13 Go)

| Volume | Objet | Description | Levier |
|--------|-------|-------------|--------|
| ~10,0 Go | `EDM_FILE_STORAGE_TAB` | Documents uploadés via DocMan (PDF, Excel, images attachés aux objets métier) | Politique d'archivage / externalisation |
| ~1,3 Go | Tables transactionnelles Finance/Commercial | Factures, vouchers, écritures (`GEN_LED_VOUCHER_ROW_TAB`, `INTERNAL_VOUCHER_ROW_TAB`, `INVOICE_TAB`, etc.) | Aucun (vraies données métier) |
| ~0,6 Go | `PDF_ARCHIVE_TAB` | Archives de rapports PDF générés | Rétention |
| ~0,5 Go | Autres petites tables de configuration métier | Listes de valeurs, paramétrages custom | Aucun (configuration nécessaire) |
| ~0,5 Go | Tables de référentiel métier (parts, clients...) | Données maîtres | Aucun |
| **~13 Go** | **TOTAL CLIENT** | | |

### ✅ Conclusion sur les données client
**Notre usage métier réel représente ~13 Go**, dont 77 % sont des documents uploadés (qui ne nécessitent pas un stockage en BDD relationnelle — externalisation possible vers un stockage objet).
**Hors documents, la base métier "transactionnelle" pure ne fait que ~3 Go.**

---

## 4. Détail des éléments générés par IFS-APP (~21 Go)

Ce sont les **structures internes du logiciel IFS** : sa propre représentation des modèles UI, son code applicatif, ses métadonnées. **Nous ne pouvons rien y faire** — c'est livré et maintenu par IFS.

| Volume | Objet | Description |
|--------|-------|-------------|
| 5,5 Go | `FND_MODEL_DESIGN_TAB` | Modèles UI Aurena (projections, pages) — métadonnées IFS |
| 3,1 Go | `FND_MODEL_API_DOC_TAB` | Documentation API auto-générée par IFS |
| 3,0 Go | `FND_MODEL_DESIGN_DATA_TAB` | Données associées aux modèles UI |
| ~5,0 Go | Tables `LANGUAGE_*` | Système de traductions multi-langues IFS |
| ~1,1 Go | Tables `CLIENT_PROFILE_*` | Profils client IFS |
| ~3,3 Go | Index et structures techniques associées | Index sur tables framework |
| **~21 Go** | **TOTAL IFS-APP** | |

### ❌ Contrôle client : aucun
Ces tables sont créées, peuplées et maintenues par IFS. Elles grossissent à chaque mise à jour produit. Le seul levier est de demander à IFS une procédure de nettoyage officielle.

---

## 5. Détail des éléments générés par IFS-OPS (~14 Go)

Ce sont les **logs, audits, traces et historiques** générés par le fonctionnement interne d'IFS. Nous avons un contrôle indirect : nous pouvons demander à modifier les politiques de rétention.

| Volume | Objet | Description | Levier client |
|--------|-------|-------------|---------------|
| 3,9 Go | `BPMN_DEBUG_ACTIVITY_LOG_TAB` | Logs de debug des workflows BPMN | ⚠️ Désactiver le mode debug (paramètre IFS) |
| 3,8 Go | `EVENT_ENTITY` (IFSIAMSYS) | Événements IAM (auth) | ⚠️ Politique de rétention |
| 1,7 Go | `EXT_FILE_TRANS_TAB` | Historique transferts fichiers | ⚠️ Politique de rétention |
| 1,5 Go | `IAM_LOGIN_EVENT_DETAIL_*` | Détail audit connexions | ⚠️ Politique de rétention |
| 1,0 Go | `LANGUAGE_FILE_IMPORT_TAB` | Fichiers d'import de traduction | ⚠️ Purge post-import |
| 0,8 Go | `CLIENT_PROFILE_HANDLING_XML_VIRTUAL_VRT` | XML de profils client | ❌ Aucun |
| 0,5 Go | Indexes IAM et constraints | Index sur tables audit | ❌ Aucun |
| 0,4 Go | `XLR_META_DATA_ARCHIVE_TAB` | Archives lobby/reporting | ⚠️ Purge |
| 0,4 Go | `FNDCN_MESSAGE_BODY_TAB` | Messages IFS Connect | ⚠️ Purge |
| **~14 Go** | **TOTAL IFS-OPS** | | |

### ⚠️ Contrôle client : indirect
Nous pouvons demander à IFS d'appliquer des politiques de rétention, mais nous n'avons pas un accès direct aux paramètres. Le mode debug BPMN par exemple peut être désactivé en passant un ticket.

---

## 6. Détail des éléments générés par ORACLE (sous gestion IFS) (~70 Go au total)

C'est l'infrastructure technique Oracle, **administrée par IFS dans le cadre du Cloud IFS**. Nous n'avons aucun contrôle, mais c'est IFS qui devrait optimiser.

### 6.1 Schéma SYS (~27 Go)

| Volume | Objet | Description | Problème ? |
|--------|-------|-------------|------------|
| **10,9 Go** | `WRI$_ADV_OBJECTS` + 3 index | 🔧 **Stockage SQL Tuning Advisor non purgé — bug Oracle connu** | ⚠️ **OUI — défaut d'administration** |
| 8,5 Go | `SOURCE$`, `IDL_UB1$`, `IDL_UB2$`, `C_TOID_VERSION#`, `I_SOURCE1` | Code PL/SQL IFS compilé (packages, procédures) | Non — mais c'est leur code, pas le nôtre |
| ~3,5 Go | `WRH$_*` (AWR) | Statistiques de performance historiques Oracle | ⚠️ Rétention potentiellement excessive |
| ~2,4 Go | LOB système Oracle | LOBs internes Oracle | Non |
| ~1,7 Go | Index, scheduler, stats CBO | Divers Oracle | Non |
| **~27 Go** | **TOTAL SYS** | | |

> 🔧 **POINT CRITIQUE** : La table `WRI$_ADV_OBJECTS` ne devrait JAMAIS atteindre 4,9 Go. C'est un **défaut d'administration documenté** (Oracle Note 1281703.1). En conditions normales, elle fait quelques Mo.

### 6.2 Espace vide alloué (~20 Go)

| Tablespace | Vide | Pourquoi c'est un problème |
|------------|------|----------------------------|
| `UNDOTBS1` | 8,3 Go | Tablespace UNDO sur-dimensionné (95 % vide) |
| `AUDIT_DATA_TBSP` | 6,4 Go | Tablespace d'audit sur-dimensionné |
| `MAINTENIX` | 1,0 Go | Module non utilisé mais alloué |
| `JASPER` | 1,0 Go | Module non utilisé mais alloué |
| Petits espaces libres divers | ~3 Go | Marges normales |
| **~20 Go** | **Sur-allocation IFS** | |

### 6.3 TEMP / UNDO / redo / archive logs (~22 Go estimés)

Ces éléments ne sont pas visibles dans `DBA_SEGMENTS` mais font partie de la base Oracle et sont visibles dans la facturation IFS :
- Tablespace TEMP (tris, hash joins)
- Redo logs en ligne (généralement 3 × ~500 Mo à 1 Go)
- Archive logs (selon rétention)
- Datafile control files
- Diagnostic dest

Le dimensionnement de ces éléments est **entièrement sous le contrôle d'IFS**.

### 6.4 Audit Oracle (AUDSYS) — 1,9 Go

Audit Oracle natif. IFS choisit le niveau d'audit appliqué. **Politique de rétention sous responsabilité IFS.**

### 6.5 Autres schémas Oracle (~4 Go)

XDB, WMSYS, CTXSYS, etc. — composants Oracle activés par IFS, peu d'impact.

---

## 7. Synthèse — Que payons-nous réellement ?

### 7.1 Décomposition finale

| Catégorie | Volume | Part | Devrait-on payer ? |
|-----------|--------|------|--------------------|
| 👤 Nos données métier réelles | 13 Go | 11 % | ✅ **OUI** (c'est notre usage) |
| 🏢 Framework IFS (modèles UI, code, traductions) | 21 Go | 17 % | ❓ **À discuter** (c'est leur produit) |
| 🏢 Logs et audit IFS | 14 Go | 12 % | ❓ **À discuter** (paramètres IFS) |
| 🔧 Code PL/SQL IFS dans SYS | 9 Go | 7 % | ❌ **NON** (c'est leur code, pas nos données) |
| 🔧 Bug Oracle `WRI$_ADV_OBJECTS` | 11 Go | 9 % | ❌ **NON** (défaut d'administration) |
| 🔧 AWR / dictionnaire Oracle | 7 Go | 6 % | ❌ **NON** (système, à dimensionner par IFS) |
| 🔧 Espace alloué vide | 20 Go | 16 % | ❌ **NON** (sur-allocation IFS) |
| 🔧 TEMP/UNDO/redo | 22 Go | 18 % | ❌ **NON** (technique Oracle) |
| 🔧 Audit Oracle + autres | 5 Go | 4 % | ❓ **À discuter** |
| **TOTAL** | **122 Go** | **100 %** | |

### 7.2 Conclusion factuelle

> **Si on devait facturer strictement sur la base des données que nous générons et que nous contrôlons, le périmètre serait de ~13 Go, soit 11 % du volume actuel.**
>
> **Si on intègre les éléments IFS pour lesquels nous avons un contrôle indirect (logs, audits avec rétention paramétrable), on monte à ~27 Go, soit 22 %.**
>
> **Les 75 Go restants relèvent du fonctionnement interne d'IFS et de la gestion Oracle assurée par IFS Cloud. Ce ne sont ni nos données, ni des éléments sur lesquels nous avons un quelconque contrôle.**

---

## 8. Tableau de référence pour la négociation

| Question IFS pourrait poser | Notre réponse factuelle |
|------------------------------|--------------------------|
| "Vous occupez 122 Go" | "Nos données utiles font 13 Go. Les 109 Go restants sont votre framework, vos logs, votre système Oracle et votre sur-allocation." |
| "Le framework fait partie du produit" | "D'accord — il devrait alors être inclus dans la licence de base, pas facturé au stockage." |
| "Les logs sont nécessaires" | "Avec quelle politique de rétention ? Le mode debug BPMN est-il activé en production de manière justifiée ? L'audit IAM est-il à 90 jours, 1 an, illimité ?" |
| "C'est l'usage Oracle normal" | "Alors purgez `WRI$_ADV_OBJECTS` (10,9 Go récupérables), revoyez la rétention AWR, et resizez UNDOTBS1 (8,3 Go vides). Ce sont vos responsabilités d'administration." |
| "Vous pouvez supprimer des documents" | "Nos documents ne représentent que 10 Go — soit 8 % du volume total. Même en les supprimant tous, on serait à 112 Go." |
