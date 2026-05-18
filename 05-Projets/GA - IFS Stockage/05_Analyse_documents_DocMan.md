# 📁 Analyse des documents DocMan — Inventaire et pistes de nettoyage interne

> **Nature de ce document** : Analyse interne descriptive du contenu de `EDM_FILE_STORAGE_TAB` (9,2 Go, 10 444 fichiers), enrichie par une analyse de la projection IFS Cloud `DocReferenceObjectAttachmentHandling.svc`.
>
> **À noter** : Ces documents sont **notre propre contenu** (uploads manuels, migrations, documents auto-générés par IFS à notre demande dans le cadre de notre activité). Ce document n'est **pas un argument contre IFS** dans la négociation — c'est un **plan d'action interne** pour mieux maîtriser notre volumétrie documentaire.
>
> **Mise à jour 2026-05-18** : sections 7 (nouvelle) et 8 (révisée) ajoutées. Les "limites métadonnées" évoquées en section 6 sont en pratique **levées** côté API IFS Cloud, qui expose dates, créateurs et rattachements aux objets métier — voir section 7.

---

## 1. Vue d'ensemble

| Métrique | Valeur |
|----------|--------|
| Nombre total de fichiers | **10 444** |
| Volume total | **9 416 Mo (9,2 Go)** |
| Taille moyenne par fichier | 923 Ko |
| Taille médiane | 323 Ko |
| Taille maximum | **114 Mo** |
| Taille minimum | 1 Ko |

**Méthode d'analyse** : Extraction directe via `DBMS_LOB.GETLENGTH(file_data)` sur `IFSAPP.EDM_FILE_STORAGE_TAB`.

---

## 2. Répartition par classe documentaire

| Classe | Nb fichiers | % nb | Volume | % vol | Taille moy. | Taille max |
|--------|-------------|------|--------|-------|-------------|------------|
| `DOC A GARDER` | 6 228 | 60 % | **7 622 Mo** | **81 %** | 1 253 Ko | 114 Mo |
| `INVOICE` | 2 377 | 23 % | 997 Mo | 11 % | 430 Ko | 7 Mo |
| `PJ_BL` | 414 | 4 % | 243 Mo | 2,6 % | 600 Ko | 4 Mo |
| `PJ_COMMANDE` | 564 | 5 % | 220 Mo | 2,3 % | 399 Ko | 13 Mo |
| `DISCO DOC` | 330 | 3 % | 163 Mo | 1,7 % | 504 Ko | 7 Mo |
| `CRM PANEL` | 382 | 4 % | 151 Mo | 1,6 % | 406 Ko | 7 Mo |
| `PJ_CDE-PRJ` | 17 | <1 % | 13 Mo | 0,1 % | 783 Ko | 4 Mo |
| `PJ_FACTURE` | 129 | 1 % | 6,5 Mo | 0,1 % | 52 Ko | 0,4 Mo |
| `IPC JSON`, `MM DOC` | 4 | <1 % | <2 Mo | <0,1 % | — | — |
| **TOTAL** | **10 444** | 100 % | **9 416 Mo** | 100 % | 923 Ko | 114 Mo |

### Observations
- **`DOC A GARDER` concentre 81 % du volume** sur 60 % des fichiers — c'est de loin la classe la plus volumineuse en moyenne (1,25 Mo par fichier vs 430 Ko pour INVOICE).
- Les **15 plus gros fichiers de toute la base** (allant de 23 Mo à 114 Mo) sont tous dans cette classe.
- Les classes "métier opérationnelles" (pièces jointes commandes / BL / factures / projets) ne pèsent au total que ~480 Mo, soit **5 % du volume documentaire**.

---

## 3. Décomposition par classe × type de document

| Classe | Type | Nb | Volume |
|--------|------|----|---------| 
| DOC A GARDER | ORIGINAL | 6 227 | 7 622 Mo |
| DOC A GARDER | VIEW | 1 | 0,2 Mo |
| INVOICE | ORIGINAL | 1 646 | 654 Mo |
| INVOICE | VIEW | 731 | 343 Mo |
| PJ_BL | ORIGINAL | 414 | 243 Mo |
| PJ_COMMANDE | ORIGINAL | 564 | 220 Mo |
| DISCO DOC | ORIGINAL | 330 | 163 Mo |
| CRM PANEL | ORIGINAL | 382 | 151 Mo |
| PJ_CDE-PRJ | ORIGINAL | 17 | 13 Mo |
| PJ_FACTURE | ORIGINAL | 129 | 6,5 Mo |
| IPC JSON | ORIGINAL + VIEW | 2 | 1,1 Mo |
| MM DOC | ORIGINAL | 1 | 0,2 Mo |

### Note sur les types ORIGINAL / VIEW
La présence de types `VIEW` pour `INVOICE` (731 vues sur 1 646 originaux) indique des **rendus d'aperçu** générés à côté du document original. Cette duplication ajoute ~343 Mo. À vérifier si ces vues sont indispensables ou si elles pourraient être générées à la volée.

---

## 4. Distribution des tailles de fichiers

| Tranche | Nb fichiers | % nb | Volume | % vol |
|---------|-------------|------|--------|-------|
| < 100 Ko | 1 252 | 12,0 % | 80 Mo | 0,9 % |
| 100 - 500 Ko | 5 097 | 48,8 % | 1 214 Mo | 12,9 % |
| 500 Ko - 1 Mo | 2 415 | 23,1 % | 1 585 Mo | 16,8 % |
| 1 - 5 Mo | 1 378 | 13,2 % | 3 317 Mo | **35,2 %** |
| 5 - 10 Mo | 213 | 2,0 % | 1 532 Mo | 16,3 % |
| 10 - 50 Mo | 86 | 0,8 % | 1 421 Mo | 15,1 % |
| **> 50 Mo** | **3** | <0,1 % | **267 Mo** | **2,8 %** |

### Observations
- **84 % des fichiers font moins de 1 Mo**, ce qui est cohérent avec un usage normal (PDF de factures, scans, photos compressées).
- **31 % du volume est concentré dans 3 % des fichiers** (ceux > 5 Mo).
- **3 fichiers dépassent les 50 Mo** et représentent à eux seuls 267 Mo — à identifier et auditer en priorité.

---

## 5. Top 15 des plus gros fichiers individuels

| Rang | Taille | Classe | Type | File No |
|------|--------|--------|------|---------|
| 1 | **114,5 Mo** | DOC A GARDER | ORIGINAL | 1 |
| 2 | 97,9 Mo | DOC A GARDER | ORIGINAL | 1 |
| 3 | 55,1 Mo | DOC A GARDER | ORIGINAL | 1 |
| 4 | 30,8 Mo | DOC A GARDER | ORIGINAL | 1 |
| 5 | 30,7 Mo | DOC A GARDER | ORIGINAL | 1 |
| 6 | 30,4 Mo | DOC A GARDER | ORIGINAL | 1 |
| 7 | 28,1 Mo | DOC A GARDER | ORIGINAL | 1 |
| 8 | 28,1 Mo | DOC A GARDER | ORIGINAL | 1 |
| 9 | 27,4 Mo | DOC A GARDER | ORIGINAL | 1 |
| 10 | 24,9 Mo | DOC A GARDER | ORIGINAL | 1 |
| 11 | 24,8 Mo | DOC A GARDER | ORIGINAL | 1 |
| 12 | 24,7 Mo | DOC A GARDER | ORIGINAL | 1 |
| 13 | 24,4 Mo | DOC A GARDER | ORIGINAL | 1 |
| 14 | 24,0 Mo | DOC A GARDER | ORIGINAL | 1 |
| 15 | 23,7 Mo | DOC A GARDER | ORIGINAL | 1 |
| | **~700 Mo cumulés** | | | |

Pour identifier précisément ces fichiers, requête à lancer :
```sql
SELECT doc_class, doc_no, doc_sheet, doc_rev,
       DBMS_LOB.GETLENGTH(file_data) AS bytes_size
FROM ifsapp.edm_file_storage_tab
ORDER BY DBMS_LOB.GETLENGTH(file_data) DESC
```
Ensuite, identifier le contenu via le `DOC_NO` dans l'UI IFS DocMan — ou via la jointure avec l'API IFS (cf. section 7) qui expose `Title`, `UserCreated`, `DtCre` et le rattachement métier de chaque document.

---

## 6. Limites de l'analyse SQL — résolues côté API IFS

La table `EDM_FILE_STORAGE_TAB` possède des colonnes pour la traçabilité mais elles sont **toutes vides** sur les 10 444 lignes :
- `CREATED_BY` : 100 % NULL
- `CREATED_DATE` : 100 % NULL
- `LOCAL_FILE_NAME` : 100 % NULL (impossible donc de connaître les extensions originales)
- `ENTITY_TYPE` : 100 % NULL (impossible de savoir à quel objet métier IFS chaque doc est rattaché depuis cette table)

### Conséquences (côté SQL uniquement)
1. **On ne peut pas dater les dépôts** depuis cette table ni mesurer la croissance mensuelle.
2. **On ne peut pas identifier les déposeurs** (humains vs comptes techniques).
3. **On ne peut pas connaître les extensions de fichiers** (PDF/Excel/images/etc.) sans ouvrir le BLOB.
4. **Le rattachement document ↔ objet métier** doit se faire via une autre source.

> ✅ **Mise à jour 2026-05-18** : ces quatre limites sont **levées dès qu'on interroge l'API IFS Cloud** au lieu (ou en complément) de la table SQL. Les métadonnées de date, créateur, titre, statut, et le **rattachement métier (LuName + KeyRef)** sont accessibles via `DocReferenceObjectAttachmentHandling.svc/DocIssueSet` et `DocReferenceObjectSet`. Voir **section 7** pour les chiffres concrets.

---

## 7. Analyse complémentaire via l'API IFS Cloud — métadonnées et rattachements (2026-05-18)

L'analyse SQL des sections 1-5 est exhaustive sur le volume mais aveugle sur la traçabilité (cf. section 6). L'API IFS `DocReferenceObjectAttachmentHandling.svc` côté projection apporte les métadonnées manquantes et les **rattachements aux objets métier** — ce qui change fondamentalement la lecture des chiffres.

### 7.1 Réconciliation SQL ↔ API

| Source | Nombre | Définition |
|--------|--------|------------|
| Table `EDM_FILE_STORAGE_TAB` (SQL) | **10 444 fichiers** | Fichiers physiques (BLOB) — un document peut produire plusieurs fichiers (ORIGINAL + VIEW) |
| API `DocIssueSet` (REST) | **9 723 documents** | Documents logiques (DocIssue = identifiant unique `DocClass / DocNo / DocRev / DocSheet`) |
| **Écart** | **~721 fichiers** | Correspond aux **types VIEW** (essentiellement INVOICE/VIEW = 731 fichiers, cf. section 3) |

→ Les deux comptes sont cohérents. La table SQL compte les fichiers BLOB, l'API compte les documents logiques.

### 7.2 Métadonnées disponibles via l'API (61 colonnes par document)

Là où la table SQL a `created_by/created_date/local_file_name/entity_type` = 100 % NULL, l'API expose pour chaque document :

- Identifiant : `DocClass`, `DocNo`, `DocRev`, `DocSheet`, `Title`
- Traçabilité : `DtCre`, `UserCreated`, `DtChg`, `UserSign`
- Workflow : `Objstate`, `IsLatestRev`, `RestrictedAccess`
- Métier : `DocRespSign`, `DocRespDept`, `NoOfSheets`, `FileType`, `OriginalCreator`, `OriginalCreationDate`
- ... + autres champs descriptifs (`Description1..6`, `Reference`, etc.)

**Rattachements aux objets métier** dans une seconde collection `DocReferenceObjectSet` (62 940 liens), avec pour chaque lien :
- `LuName` (type d'objet métier — ex: `ManSuppInvoice`, `PurchaseOrder`)
- `KeyRef` (clé fonctionnelle — ex: `ORDER_NO=C100489^`)
- `DateConnected`, `Category`

→ **6,5 rattachements par document en moyenne** sur PROD. Un même PDF de facture est typiquement attaché à toute la chaîne comptable (facture, écriture CG, item du grand-livre, etc.).

### 7.3 Distribution temporelle des créations (PROD) — nombre **et** volume

Mesures obtenues en croisant `DocIssueSet` (API IFS : DtCre + UserCreated) avec `EDM_FILE_STORAGE_TAB` (SQL : taille BLOB) via jointure côté Python sur `(DocClass, DocNo, DocRev, DocSheet)`.

| Mois | Documents créés | Fichiers physiques | **Mo créés** |
|------|-----------------|--------------------|-------------:|
| 2025-05 | 24 | 26 | 11,8 |
| 2025-06 | 29 | 27 | 54,6 |
| 2025-07 | 24 | 24 | 15,7 |
| 2025-08 | 17 | 17 | 10,6 |
| 2025-09 | 25 | 25 | 11,2 |
| 2025-10 | 155 | 155 | 51,1 |
| 2025-11 | 124 | 124 | 40,8 |
| 2025-12 | 121 | 121 | 49,2 |
| 2026-01 | 193 | 192 | 95,6 |
| 2026-02 | 173 | 173 | 77,5 |
| **2026-03** | **2 808** | **2 808** | **2 572** |
| **2026-04** | **3 764** | **3 762** | **4 246** |
| 2026-05 (au 18) | 1 451 | 1 451 | 1 511 |

### Totaux
- **6 derniers mois** : 8 634 docs → **8 593 Mo (~8,4 Go)**
- **12 derniers mois** : 8 908 docs → **8 748 Mo (~8,5 Go)**
- Volume total mesuré côté CSV (10 462 fichiers, snapshot 18/05/2026) : **9 471 Mo** (cohérent avec les 9,2 Go de la section 1, +55 Mo de nouveaux fichiers depuis l'extraction initiale).

→ **89 % des documents et 92 % du volume** des 12 derniers mois sont concentrés sur **mars-mai 2026**, l'accélération étant imputable au démarrage du compte Talend (voir 7.4).

### 7.4 Identification du contributeur principal : compte `TT` (Talend)

> **Contexte métier** : le compte `TT` correspond au connecteur **Talend** qui dépose dans IFS les **pièces jointes des factures fournisseurs**. Ce processus n'existait pas avant **mars 2026** — historiquement, ces PJ factures n'étaient pas archivées dans IFS. Le démarrage du flux Talend marque la mise en place d'une nouvelle politique d'archivage documentaire des justificatifs comptables.

Sur 72 créateurs distincts, **`TT` = 5 774 documents (60 % du total PROD)** et **7 368 Mo (~7,4 Go) = 78 % du volume documentaire total**. C'est mécaniquement le contributeur dominant depuis sa mise en service.

**Profil détaillé du compte TT :**

| Métrique | Valeur |
|----------|--------|
| Documents créés | 5 774 (60 % du nombre PROD) |
| **Volume créé** | **7 368 Mo (78 % du volume PROD)** |
| Taille moyenne par doc | **1,28 Mo** (cohérent avec la moyenne 1,25 Mo de `DOC A GARDER`) |
| Liens vers objets métier | 53 810 |
| Moyenne rattachements / doc | 9,3 (vs 6,5 sur l'ensemble) |
| Docs orphelins (sans rattachement) | 69 (1,2 %) |
| Activité démarrée | **2026-03** (rien avant — démarrage du process PJ factures) |
| Rythme actuel | ~80 docs / jour ouvré (~115 Mo / jour ouvré) |

**Volume mensuel généré par Talend depuis sa mise en service :**

| Mois | Docs Talend | **Mo Talend** |
|------|-------------|--------------:|
| 2026-03 | 1 778 | 2 173 |
| 2026-04 | 2 839 | 3 789 |
| 2026-05 (au 18) | 1 157 | 1 406 |
| **Total** | **5 774** | **7 368 Mo (~7,4 Go)** |

→ **En 2,5 mois, le flux Talend a déversé presque autant de volume que les 5 années d'activité IFS précédentes cumulées** (~2 000 Mo accumulés avant mars 2026 vs 7 368 Mo depuis). Ce n'est pas une anomalie — c'est l'effet **attendu** de la mise en archivage des PJ factures.

**Classes utilisées par Talend :**

| Classe | Documents Talend |
|--------|-------------------|
| **DOC A GARDER** | 5 772 (**100 %**) |

→ Talend pousse **exclusivement** dans la classe `DOC A GARDER`. Aucune classe `INVOICE`, `PJ_FACTURE` ou `PJ_COMMANDE` n'est utilisée par Talend, alors qu'elles existent et seraient sémantiquement plus adaptées. À investiguer : choix historique du connecteur ?

**Objets métier rattachés par les docs Talend :**

| LuName | Liens Talend | % | Rôle |
|--------|--------------|---|------|
| `GenLedVoucherRow` | 23 294 | 43,3 % | Lignes d'écriture comptable (~4 par facture) |
| `ManSuppInvoice` | 5 709 | 10,6 % | Facture fournisseur (entité principale) |
| `IncomingInvoice` | 5 691 | 10,6 % | Facture entrante |
| `PostingProposalHead` | 5 691 | 10,6 % | Proposition de comptabilisation |
| `InvoiceLedgerItem` | 4 465 | 8,3 % | Item facture du grand-livre |
| `LedgerItem` | 4 465 | 8,3 % | Item général du grand-livre |
| `GenLedVoucher` | 4 464 | 8,3 % | Pièce comptable |
| `VoucherRow` / `Voucher` | 25 | <0,1 % | Régularisations marginales |

→ **Lecture du flux Talend** : chaque PDF de facture est rattaché à toute la chaîne comptable :
`PDF` → `ManSuppInvoice` + `IncomingInvoice` + `PostingProposalHead` + (si validée comptablement) `GenLedVoucher` + ~4 × `GenLedVoucherRow` + `LedgerItem` + `InvoiceLedgerItem` = **~9 rattachements par facture**.

### 7.5 Anomalies et points à investiguer

| # | Constat | Interprétation |
|---|---------|----------------|
| 1 | 18 `ManSuppInvoice` Talend sans `IncomingInvoice` ni `PostingProposalHead` (5 709 vs 5 691) | Soit factures pas encore propagées, soit propagation cassée. À investiguer. |
| 2 | 1 244 factures Talend sans `LedgerItem` (5 709 `ManSuppInvoice` vs 4 465 `LedgerItem`) | Stock en attente de validation comptable. Normal mais à surveiller (~22 % en attente). |
| 3 | 69 documents Talend orphelins (sans aucun rattachement) | "Documents perdus" du flux Talend. À explorer si volume préoccupant. |
| 4 | 100 % des documents en statut `Preliminary` (tous envs) | Aucun document n'est passé en "Released" — soit ce n'est pas dans le workflow, soit le statut n'est pas géré. |
| 5 | 0 document avec `RestrictedAccess=1` | Aucun document confidentiel marqué — à confirmer si c'est l'intention. |

### 7.6 Comparaison TRN vs PROD

L'analyse a été conduite sur les deux envs. Les distributions mensuelles **avant mai 2026 sont rigoureusement identiques** — TRN est une copie PROD figée fin avril / début mai 2026. Depuis, PROD a continué à recevoir des documents Talend (1 437 docs en mai), TRN non (11 docs). Utile pour situer la fraîcheur des envs de test.

| Env | Total docs | Liens | Mai 2026 (au 18) |
|-----|------------|-------|------------------|
| PROD | 9 723 | 62 940 | 1 448 |
| TRN  | 8 286 | 49 280 | 11 |
| **Delta** | **+1 437** | **+13 660** | – |

### 7.7bis Solution standard IFS pour externaliser DocMan : `Cloud File Storage` (à activer)

> **Ajout 2026-05-18 (suite à lecture de la doc IFS Cloud)** : la feature `Cloud File Storage` existe nativement dans IFS Cloud SaaS et permet de stocker les documents sur **Azure Blob Storage** au lieu de la BDD Oracle. Nous avions choisi de ne pas l'activer au provisionnement initial du tenant — ce choix est à reconsidérer.

**Sources de documentation IFS** (Technical Documentation For IFS Cloud, Release 24R2) :
- *Solution Manager User Guide* › *Additional IFS Cloud Configuration* › **Cloud File Storage**
- *Solution Manager User Guide* › *Additional IFS Cloud Configuration* › **Cloud File Storage Migration Tool**

#### Architecture IFS pour Cloud SaaS

Citation directe :

> *"IFS Cloud File Storage is a platform service which can be used to store and retrieve documents from different storage locations. The service abstracts complexities in the underlying storage mode from the caller of the service. The caller interacts with the service using simple REST operations."*

> *"In the Cloud deployment model, the File Storage uses an Azure Blob Storage Account to store files. A storage account is provisioned automatically per environment. Access to the storage account is only allowed from the middle-tier related to the environment."*

→ Côté applicatif, **aucun changement** : les appels REST IFS DocMan sont identiques. Le service `Cloud File Storage` intercepte et redirige le stockage vers Azure Blob. Talend continue de pousser via l'API IFS habituelle.

#### Setup (selon doc IFS)

Deux étapes admin dans l'UI IFS, qualifiées par IFS d'*"easy task"* :

1. **Media Item Setup** :
   - Object Properties › LU `MediaItem` › property `REPOSITORY` → `FILE_STORAGE`

2. **Document Management Setup** :
   - Repositories › Nouveau repository
   - Type = `File Storage`
   - Document Class = `*` (toutes) ou cibler `DOC A GARDER`, `INVOICE` d'abord
   - Status = `Generating`
   - L'ancien repository passe en `Usable` (read-only) puis peut être supprimé une fois vide

#### Migration des 10 Go existants

Deux outils selon le contexte :

| Outil | Quand l'utiliser | Notre cas ? |
|---|---|---|
| **Web Assistants intégrés** (`Transfer Documents` / `Transfer Media`) | "smaller installations" où la base est déjà dans le cloud managé IFS | ✅ **OUI** — c'est nous |
| FS Mig Tool externe (Java) | Gros migrations Apps 8/9/10 → IFS Cloud où la base source n'a pas pu être déplacée telle quelle | ❌ Non |

Citation directe :

> *"For 'smaller' installations, where the full source database can be moved into the managed cloud environment as is, there are two IFS Cloud Web assistants for moving document files and media items to IFS Cloud File Storage: Transfer Documents / Transfer Media. **That option is fully automatic and is preferable to using this tool.**"*

→ Pour notre tenant Cloud déjà managé par IFS, la migration des 10 Go d'EDM existants se fait via le **Web Assistant `Transfer Documents`**, en mode "fully automatic".

#### Pourquoi c'est la bonne réponse pour nous

| Aspect | Sans `Cloud File Storage` (état actuel) | Avec `Cloud File Storage` activé |
|---|---|---|
| Stockage Talend | BDD Oracle (cher au Go) | Azure Blob (~10× moins cher au Go) |
| Trajectoire 12 mois | +36 Go en BDD | +36 Go en Azure Blob (BDD stable) |
| Trajectoire 10 ans (légale) | +360 Go en BDD | +360 Go en Azure Blob (BDD stable) |
| Accès applicatif | Inchangé (API REST DocMan) | Inchangé (API REST DocMan) |
| Effort de migration | — | Web Assistant "fully automatic" |
| Effort de mise en place | — | 2 propriétés à changer dans l'admin IFS |

→ C'est à la fois **la solution technique standard d'IFS** et **la réponse à notre problème de volume**.

### 7.7 Endpoints API utilisés (référence technique)

Base URL : `{env}/main/ifsapplications/projection/v1/DocReferenceObjectAttachmentHandling.svc/`

| Endpoint | Contenu | Volumétrie PROD |
|----------|---------|-----------------|
| `DocIssueSet` | Inventaire des documents (DocIssue) | 9 723 lignes |
| `DocReferenceObjectSet` | Liens document ↔ objet métier (LuName + KeyRef) | 62 940 lignes |
| `DocClassSet` | Référentiel des classes | 11 classes |
| `DocFormatSet` | Référentiel des formats | 1 format |
| `DocIssueRecordSet` | Détails par révision | 9 723 lignes |

**Particularité** : sur ces endpoints, IFS Cloud ne renvoie pas de `@odata.nextLink`. Le paramètre `$top` agit comme plafond absolu. **Sans `$top`, l'API renvoie le set complet en un seul appel** (~5 secondes pour 60 000 lignes via `$select` ciblé).

**Reproductibilité** : deux commandes management Django ad-hoc (non commitées dans `ifs-env`, prêtes à rejouer) permettent de relancer ces analyses sur n'importe quel env :
- `python manage.py explore_documents <env>` — discovery des endpoints disponibles
- `python manage.py analyze_documents <env> [--focus-user USER]` — analyse agrégée et focus utilisateur

---

## 8. Hypothèses sur les classes documentaires — confirmations / corrections

Les classes étant **custom** (créées chez nous), une confirmation par référent métier reste utile. La section 7 a permis de **valider ou corriger** plusieurs hypothèses :

| Classe | Hypothèse initiale | Statut après analyse API |
|--------|---------------------|--------------------------|
| `DOC A GARDER` | Classe générique "documents à conserver" — possible dépôt de masse ou fourre-tout | ⚠️ **Corrigé** : c'est en réalité **la classe utilisée par Talend pour archiver les PJ des factures fournisseurs** (92,5 % du total `DOC A GARDER` = 5 774 sur 6 238 docs PROD). Pas du tout un fourre-tout, mais une classe à **usage mono-fonctionnel** mise en service en mars 2026 pour répondre au besoin **d'archiver dans IFS les justificatifs factures fournisseurs** — ce qui n'était pas fait auparavant. |
| `INVOICE` | Factures sortantes (Customer Order/Invoice) | À confirmer par référent métier (l'API ne contredit pas, 1 495 liens vers `ManCustInvoice`). |
| `PJ_COMMANDE` | Pièces jointes aux commandes | Confirmé : liens vers `PurchaseOrder` côté API. |
| `PJ_BL` | Pièces jointes aux BL | Probable : liens vers `ReceiptInfo` (réception marchandises). |
| `PJ_FACTURE` | Pièces jointes aux factures fournisseurs | ⚠️ **Constat** : seulement 129 fichiers — alors que les factures sont *en réalité* déposées dans `DOC A GARDER` par Talend. **Cette classe semble peu utilisée par le flux principal** ; à clarifier qui s'en sert et pourquoi il n'y a pas de standardisation. |
| `PJ_CDE-PRJ` | Commandes projet | Plausible. |
| `CRM PANEL` | Module CRM | Confirmé : ~295 liens vers `BusinessOpportunity`. |
| `DISCO DOC` | ? | À clarifier — l'API ne donne pas d'indice métier. |
| `IPC JSON`, `MM DOC` | Modules IPC / Materials Management | Marginal (1 doc chacun). |

**Question soulevée** : pourquoi Talend dépose-t-il les factures dans `DOC A GARDER` au lieu d'`INVOICE` ou `PJ_FACTURE` ? C'est probablement un choix historique du connecteur Talend (à vérifier avec qui le maintient). **Standardiser** ferait gagner en lisibilité, en cohérence avec les autres flux et faciliterait les futures politiques de rétention par classe.

---

## 9. Plan d'action interne

### 🎯 Court terme (gains rapides, peu de risque)

1. **Auditer les 3 fichiers > 50 Mo** (267 Mo cumulés)
   - Identifier leur contenu via `DOC_NO`
   - Vérifier s'ils sont indispensables au métier ou s'il s'agit de scans / archives anciens
   - Si non critiques : suppression ou export vers stockage externe

2. **Vérifier le statut de `Cloud File Storage` sur notre tenant et finaliser l'activation si besoin, puis migrer les 9,5 Go d'EDM existants vers Azure Blob**
   - **Solution standard IFS, déjà documentée et probablement provisionnée sur notre tenant Cloud** : voir §7.7bis pour les références doc IFS (`Cloud File Storage` + `Cloud File Storage Migration Tool`). La doc IFS précise que *"A storage account is provisioned automatically per environment"* — le storage Azure Blob est donc vraisemblablement déjà alloué côté tenant.
   - **Process** :
     - **Étape 0 (validation)** — Vérifier dans l'admin IFS si un repository de type `File Storage` est configuré et si la property `REPOSITORY` du LU `MediaItem` vaut `FILE_STORAGE`. Si oui : la feature est active mais peut-être non sélectionnée comme default. Si non : passer aux étapes suivantes.
     - Object Properties › LU `MediaItem` › property `REPOSITORY` = `FILE_STORAGE`
     - Document Management › Repositories : nouveau repository Type=`File Storage`, Status=`Generating`
     - Lancement du Web Assistant `Transfer Documents` (qualifié de *"fully automatic"* par IFS)
   - **Pourquoi maintenant** : avec la trajectoire Talend (+36 Go/an, +360 Go à 10 ans pour respecter l'obligation légale), continuer en BDD Oracle devient économiquement absurde (le stockage objet est ~10× moins cher au Go).
   - **Contexte historique** : nous avions choisi de ne pas activer cette feature au provisionnement initial du tenant. Avec l'arrivée du flux Talend, ce choix est à reconsidérer en priorité.

3. **Vérifier les `INVOICE / VIEW`** (343 Mo)
   - Comprendre si les vues PDF des factures doivent être stockées en plus des originaux
   - Possibilité de purge si elles peuvent être régénérées à la demande

4. **Investiguer les 69 docs Talend orphelins** (cf. 7.5)
   - Sortir la liste (`DocNo`, `Title`, `DtCre`) via `python manage.py analyze_documents PROD --focus-user TT` (à enrichir pour lister explicitement les orphelins)
   - Identifier pourquoi ils n'ont aucun rattachement métier (échec d'import partiel ? doc poussé sans clé de rattachement ?)

5. **Investiguer les 18 `ManSuppInvoice` sans `IncomingInvoice`** (cf. 7.5 ligne 1)
   - Soit cas légitime (factures non propagées au flux comptable), soit défaut du connecteur Talend

### 🎯 Moyen terme (politique documentaire et qualité)

6. **Standardiser le choix de classes documentaires**
   - Définir une convention claire : quelle classe pour quel usage métier
   - Faire évoluer Talend pour utiliser `INVOICE` ou `PJ_FACTURE` plutôt que `DOC A GARDER` (lisibilité, futures politiques de rétention par classe, alignement avec les autres flux)
   - **Attention migration** : si on renomme la classe d'un lot existant, prévoir l'impact sur les éventuelles intégrations qui filtrent par classe

7. **Externalisation des archives lourdes**
   - Étudier avec IFS la possibilité de stocker les documents (notamment `DOC A GARDER`) sur un stockage objet externe (S3, Azure Blob) plutôt qu'en BDD
   - Le stockage objet est typiquement 10× moins cher au Go que le stockage BDD
   - IFS Cloud peut supporter ce type d'architecture — à demander explicitement

8. **Définir une politique de cycle de vie documentaire**
   - Quels documents doivent rester accessibles en ligne (BDD IFS) ?
   - Quels documents peuvent être archivés (stockage externe, moins coûteux) ?
   - Quels documents peuvent être supprimés après X années ?

### 🎯 Long terme

9. **Tableau de bord documentaire mensuel**
   - L'API IFS expose toutes les métadonnées nécessaires (date, créateur, classe, rattachement) — un indicateur Django / Celery dans **ERP-Control** serait facile à mettre en place (5 secondes par run, 2 endpoints)
   - Suivre la croissance par classe et par créateur
   - Détecter les anomalies (pics, classes inattendues qui grossissent, augmentation des orphelins Talend)
   - Anticiper les seuils contractuels
   - Promouvoir `analyze_documents` en indicateur officiel d'ERP-Control plutôt qu'en commande ad-hoc

---

## 10. Gain potentiel estimé

> **Lecture clé** : depuis qu'on sait que `DOC A GARDER` = PJ factures fournisseurs à conserver 10 ans légalement, le levier dominant n'est plus la **purge** mais l'**externalisation**. Les actions de purge ponctuelle restent possibles mais représentent <5 % du volume — à côté de l'enjeu d'externaliser les ~8 Go déjà en BDD + les ~36 Go/an que Talend va ajouter en croisière.

### 10.1 Gains de purge immédiate (BDD)

| Action | Gain estimé | Effort |
|--------|-------------|--------|
| Purge des 3 fichiers > 50 Mo si non critiques | ~270 Mo | Faible |
| Suppression des `INVOICE / VIEW` si régénérables | ~340 Mo | Faible |
| Investigation des 69 docs Talend orphelins (cf. 7.5) | Qualité (pas de gain volume direct) | Faible |
| **Sous-total purge** | **~610 Mo (~6 % du volume actuel)** | — |

→ Marginal sur le volume, mais à faire pour l'hygiène et la traçabilité.

### 10.2 Gain structurel (externalisation)

| Action | Volume concerné | Effort |
|--------|------------------|--------|
| Externaliser `DOC A GARDER` (PJ factures Talend) vers stockage objet S3 / Azure Blob | **7,4 Go actuels + ~36 Go/an de croissance** | Élevé |
| Mettre `INVOICE` en externe si pertinent | ~1 Go | Moyen |
| **Effet cumulatif sur 5 ans** | **~180 Go évités sur le stockage BDD** | — |

→ **C'est le seul levier qui adresse la trajectoire** (les PJ factures sont conservées 10 ans par obligation légale, donc rien à purger). L'externalisation transforme un coût BDD (cher au Go) en coût stockage objet (~10× moins cher au Go) sans perte de donnée ni de fonctionnalité.

### 10.3 Ce qu'on NE peut PAS faire

- ~~Purger les PJ factures Talend pour gagner du volume~~ : obligation comptable 10 ans, hors discussion.
- ~~Empêcher la croissance Talend~~ : c'est un processus métier mis en place volontairement pour combler un manque de traçabilité.

> ⚠️ Toute action de purge (10.1) nécessite **une analyse fonctionnelle** préalable et doit être validée par les référents métier (compta en priorité vu la nature factures fournisseurs, puis achats, ventes, projets...).

---

## 11. Synthèse

- **9,2 Go de documents dans IFS, dont 81 % concentrés dans une seule classe (`DOC A GARDER`)**.
- ~~Classe a priori fourre-tout~~ → **`DOC A GARDER` est l'archive des PJ factures fournisseurs alimentée par le connecteur Talend depuis mars 2026**, en réponse à un besoin de traçabilité qui n'était pas couvert auparavant (5 774 docs / 7,4 Go).
- ~~Volume "à nettoyer"~~ → **Volume légitime à piloter** : les PJ factures fournisseurs doivent être conservées 10 ans (obligation légale comptable). La question n'est donc pas de purger mais d'**anticiper la trajectoire** (~3 Go/mois Talend en croisière = ~36 Go/an).
- L'usage documentaire opérationnel "vivant" hors PJ Talend (pièces jointes au métier actif) ne représente que **~480 Mo, soit 5 %** du volume documentaire — confirmation que **le seul flux qui dimensionne le stockage IFS chez nous est l'archivage PJ factures**.
- ~~Les métadonnées de traçabilité sont absentes~~ → **Les métadonnées sont disponibles via l'API IFS Cloud** (`DocReferenceObjectAttachmentHandling.svc/DocIssueSet`), même si la table SQL `EDM_FILE_STORAGE_TAB` ne les conserve pas. Voir section 7.
- **Plan d'action interne** : **activer le service `Cloud File Storage` IFS** (priorité 1 court terme — feature standard, documentée, Web Assistant de migration "fully automatic" — voir §7.7bis), pilotage de la trajectoire Talend (priorité 2), standardisation des classes documentaires (priorité 3 lisibilité).
- **Ces documents sont notre responsabilité** — toute évolution se décide en interne, en concertation avec les équipes métier (**compta en premier** vu la nature factures fournisseurs et l'obligation légale).
