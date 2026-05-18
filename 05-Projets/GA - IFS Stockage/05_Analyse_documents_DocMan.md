# 📁 Analyse des documents DocMan — Inventaire et pistes de nettoyage interne

> **Nature de ce document** : Analyse interne descriptive du contenu de `EDM_FILE_STORAGE_TAB` (9,2 Go, 10 444 fichiers).
>
> **À noter** : Ces documents sont **notre propre contenu** (uploads manuels, migrations, documents auto-générés par IFS à notre demande dans le cadre de notre activité). Ce document n'est **pas un argument contre IFS** dans la négociation — c'est un **plan d'action interne** pour mieux maîtriser notre volumétrie documentaire.

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
Ensuite, identifier le contenu via le `DOC_NO` dans l'UI IFS DocMan.

---

## 6. Limites de l'analyse — Métadonnées manquantes

La table `EDM_FILE_STORAGE_TAB` possède des colonnes pour la traçabilité mais elles sont **toutes vides** sur les 10 444 lignes :
- `CREATED_BY` : 100 % NULL
- `CREATED_DATE` : 100 % NULL
- `LOCAL_FILE_NAME` : 100 % NULL (impossible donc de connaître les extensions originales)
- `ENTITY_TYPE` : 100 % NULL (impossible de savoir à quel objet métier IFS chaque doc est rattaché depuis cette table)

### Conséquences
1. **On ne peut pas dater les dépôts** ni mesurer la croissance mensuelle.
2. **On ne peut pas identifier les déposeurs** (humains vs comptes techniques).
3. **On ne peut pas connaître les extensions de fichiers** (PDF/Excel/images/etc.) sans ouvrir le BLOB.
4. **Le rattachement document ↔ objet métier** doit se faire via une autre table de référence (à identifier — probablement dans le module métier ayant créé l'attachement, pas dans DocMan directement).

### À investiguer
- Pourquoi les métadonnées ne sont-elles pas renseignées ? Configuration IFS ? Mode d'alimentation (intégration vs UI) ?
- Existe-t-il une table de liaison côté Customer Order / Purchase Order / Invoice pour retrouver les rattachements ?

---

## 7. Hypothèses sur les classes documentaires

Les classes étant **custom** (créées chez nous), seul un référent métier interne peut confirmer leur usage exact. Hypothèses indicatives :

| Classe | Hypothèse d'usage |
|--------|--------------------|
| `DOC A GARDER` | Classe générique "documents à conserver" — possible dépôt de masse ou catégorie fourre-tout |
| `INVOICE` | Factures sortantes (générées par le module Customer Order/Invoice) |
| `PJ_COMMANDE` | Pièces jointes aux commandes (achats ou ventes) |
| `PJ_BL` | Pièces jointes aux Bons de Livraison |
| `PJ_FACTURE` | Pièces jointes aux factures fournisseurs |
| `PJ_CDE-PRJ` | Pièces jointes aux commandes projet |
| `CRM PANEL` | Documents liés au module CRM |
| `DISCO DOC` | À clarifier — "discontinued docs" ? "documents disco/audio" ? |
| `IPC JSON` | Probable lien avec le module IPC (illustrated parts catalog) |
| `MM DOC` | Probable lien avec le module Materials Management |

**Action recommandée** : faire confirmer ces définitions par le référent fonctionnel IFS interne.

---

## 8. Plan d'action interne

### 🎯 Court terme (gains rapides, peu de risque)

1. **Auditer les 3 fichiers > 50 Mo** (267 Mo cumulés)
   - Identifier leur contenu via `DOC_NO`
   - Vérifier s'ils sont indispensables au métier ou s'il s'agit de scans / archives anciens
   - Si non critiques : suppression ou export vers stockage externe

2. **Auditer la classe `DOC A GARDER`** (7,6 Go, 60 % du volume documentaire)
   - Comprendre l'origine de cette classe et la politique qui la peuple
   - Identifier un échantillon (top 100 plus gros) et caractériser leur contenu
   - Définir une **politique de rétention** : doivent-ils rester en BDD ? Pour combien de temps ?

3. **Vérifier les `INVOICE / VIEW`** (343 Mo)
   - Comprendre si les vues PDF des factures doivent être stockées en plus des originaux
   - Possibilité de purge si elles peuvent être régénérées à la demande

### 🎯 Moyen terme (politique documentaire)

4. **Définir une politique de cycle de vie documentaire**
   - Quels documents doivent rester accessibles en ligne (BDD IFS) ?
   - Quels documents peuvent être archivés (stockage externe, moins coûteux) ?
   - Quels documents peuvent être supprimés après X années ?

5. **Investiguer pourquoi les métadonnées sont vides**
   - Vérifier la configuration IFS sur la table `EDM_FILE_STORAGE_TAB`
   - S'assurer que les futurs dépôts portent `created_by`, `created_date`, `entity_type`, `local_file_name`
   - C'est important pour la traçabilité et pour les futures analyses de ce type

6. **Externalisation des archives lourdes**
   - Étudier avec IFS la possibilité de stocker les documents (notamment `DOC A GARDER`) sur un stockage objet externe (S3, Azure Blob) plutôt qu'en BDD
   - Le stockage objet est typiquement 10× moins cher au Go que le stockage BDD
   - IFS Cloud peut supporter ce type d'architecture — à demander explicitement

### 🎯 Long terme

7. **Tableau de bord documentaire mensuel**
   - Une fois les métadonnées correctement renseignées, suivre la croissance par classe
   - Détecter les anomalies (pics, classes inattendues qui grossissent)
   - Anticiper les seuils contractuels

---

## 9. Gain potentiel estimé

| Action | Gain estimé | Effort |
|--------|-------------|--------|
| Purge des 3 fichiers > 50 Mo si non critiques | ~270 Mo | Faible |
| Audit + purge sélective de `DOC A GARDER` | **1 à 5 Go** | Moyen |
| Suppression des `INVOICE / VIEW` si régénérables | ~340 Mo | Faible |
| Externalisation `DOC A GARDER` vers stockage objet | **~7,6 Go** déplacés | Élevé |
| **TOTAL potentiel sur DocMan** | **1 à 8 Go** | Variable |

> ⚠️ Ces gains nécessitent **une analyse fonctionnelle** préalable. Aucune purge ne doit être faite sans validation par les référents métier (compta, achats, ventes, projets...).

---

## 10. Synthèse

- **9,2 Go de documents dans IFS, dont 81 % concentrés dans une seule classe (`DOC A GARDER`)**.
- L'usage documentaire opérationnel "vivant" (pièces jointes au métier actif) ne représente que **~480 Mo, soit 5 %** du volume documentaire.
- **Les métadonnées de traçabilité sont absentes** — c'est un point d'attention pour l'avenir.
- **Plan d'action interne** : auditer les classes pour identifier ce qui peut être supprimé ou externalisé, mettre en place une politique de cycle de vie.
- **Ces documents sont notre responsabilité** — toute action de purge ou d'externalisation se décide en interne, en concertation avec les équipes métier.
