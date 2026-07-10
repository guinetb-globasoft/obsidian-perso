---
projet: Base IFS — Monitoring & Datawarehouse
note: Glossaire IFS / Oracle
date_maj: 2026-07-10
tags: [gouvernance, glossaire]
---

# Glossaire — IFS & Oracle

> Vocabulaire commun tech/métier. Alimenté au fil de l'apprentissage. Chaque terme est wikilinké depuis les fiches qui l'emploient.

| Terme | Définition |
|---|---|
| **IFS** | Progiciel ERP (IFS Applications / IFS Cloud). Ici hébergé sur Oracle Database. |
| **IFSAPP** | Schéma Oracle propriétaire de **tout** le modèle applicatif IFS (tables, vues, packages). |
| **IFSIAMSYS** | Schéma Identity & Access Management d'IFS (auth, événements de login). Inaccessible au compte `IFSDBREADONLY`. |
| **LU (Logical Unit)** | Unité logique métier IFS = une entité. Se matérialise par un triplet : table `_TAB` + vue + package `_API`. *(à confirmer/détailler)* |
| **`XXX_TAB`** | Table physique de base d'une LU (ex : `CUSTOMER_ORDER_TAB`). Contient les données réelles. |
| **`XXX` (vue)** | Vue métier au-dessus de la table `_TAB`, avec règles de sécurité/dérivations. Point d'entrée recommandé pour lire. |
| **`XXX_API`** | Package PL/SQL exposant la logique métier de la LU (création, validation, transitions d'état). |
| **Background Job** | Travail de fond IFS (batch asynchrone). Table candidate : `TRANSACTION_SYS_LOCAL_TAB`. *(à confirmer)* |
| **Application Message** | Message d'intégration/connectivité IFS (flux entrants/sortants). Table candidate : `APPLICATION_MESSAGE_TAB`. *(à confirmer)* |
| **Oracle Text (CTXSYS)** | Moteur de recherche plein-texte Oracle, utilisé par IFS. |
| **Tablespace** | Conteneur logique de stockage Oracle regroupant des datafiles. |
| **Segment** | Objet physique stocké (table, index, LOB…) — granularité de `DBA_SEGMENTS`. |
| **DUA** | Durée d'Utilité Administrative (records management) — combien de temps on conserve. |
| **OneLake / Fabric** | Plateforme data Microsoft, cible du futur datawarehouse. |

> _Termes en `(à confirmer)` = hypothèses à valider par requête._
