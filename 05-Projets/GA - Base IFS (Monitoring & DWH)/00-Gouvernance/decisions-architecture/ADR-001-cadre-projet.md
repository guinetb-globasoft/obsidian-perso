---
adr: 001
titre: Cadre du projet — accès lecture seule sur production, double finalité monitoring + DWH
statut: acceptée
date: 2026-07-10
tags: [adr, gouvernance]
---

# ADR-001 — Cadre du projet

## Statut
Acceptée — 2026-07-10.

## Contexte

- Accès à la base **Oracle IFS de production** (`PISAPRD1_1`) via DBeaver, compte **lecture seule** `IFSDBREADONLY`.
- Double objectif : (1) **monitorer** la santé technique, (2) préparer un **datawarehouse** alimenté par IFS (cible Microsoft Fabric / OneLake).
- Benoît ne connaît pas la structure de la base ; apprentissage progressif piloté par requêtes.

## Décisions

1. **Lecture seule stricte sur production.** Aucun DML/DDL. Éviter les requêtes lourdes (full scans, tri sur LOB) susceptibles de peser sur la prod. Toute requête de volumétrie s'appuie sur les métadonnées (`DBA_SEGMENTS`, `DBMS_LOB.GETLENGTH`) plutôt que sur des `COUNT(*)` de grosses tables.
2. **Classement fonctionnel** des notes (comprendre / surveiller / alimenter) suivant la méthodologie interne, avec transverses obligatoires posés dès le départ.
3. **Monitoring d'abord côté Oracle natif** puisque les vues `DBA_*` d'espace/jobs et `v$session` sont accessibles (confirmé salve 2), **complété** par le framework IFS (Background Jobs, Application Messages) pour la lecture fonctionnelle.
4. **DWH : approche par les vues métier IFS** (couche `XXX` / `XXX_TAB`) plutôt que par reverse-engineering des tables physiques — à instruire une fois l'architecture LU comprise.
5. **RGPD à traiter avant tout usage DWH** : IFS contient des données personnelles ; une cartographie RGPD sera nécessaire (angle 8/10 conditionnel) avant d'exporter vers Fabric.

## Conséquences

- Le monitoring technique est réalisable sans élever les droits (bonne nouvelle).
- Angle mort assumé : `IFSIAMSYS` (auth/login) inaccessible → pas de supervision des connexions applicatives IFS par ce compte.
- Trou de perf `v$sysmetric` refusé → prévoir des contournements (`DBA_HIST_*`, autres `V$`).
- Un **runbook** d'exploitation devra être produit (conditionnel obligatoire — prod).

## Alternatives écartées

- *Demander un compte DBA* : non nécessaire pour l'instant, le périmètre lecture couvre le besoin ; à réévaluer si des vues perf clés manquent.
