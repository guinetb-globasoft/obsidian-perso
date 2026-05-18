---
projet: DWH Aerotec — Contrôle de gestion
sprint: MEP 2 — Suivi factures achats
referent_metier: Elza
recette_cible: 2026-05-02
statut: en-cours
date_creation: 2026-04-25
date_revue: 2026-04-25
tags: [dwh, mep-2, factures-achats, sprint, controle-gestion]
---

# Sprint MEP 2 — Suivi factures achats

## Contexte

Suite de la MEP 1 (Imputations, recette Lilia 20/04). Même méthode :
- **Conception** = Claude (Opus, ce dossier + vault DWH/)
- **Réalisation** = Claude Code (Sonnet, repo `aerotec-etl/`)
- **Recette métier** = Elza, jalon 02/05/2026

## Cible MEP 2

- **Silver cible** : `silver_mep2.factures_fournisseurs` (en-têtes ENFACFO enrichies)
- **Sources** : CLIPPER AEC + AEG (ENFACFO, FACFO, TTCENFACFO, FOURNISS, BC, Monnaies) + saisies manuelles Elza
- **Restitution** : Excel agrégé multi-sites avec colonnes pour saisie manuelle Elza
- **Pattern out → in** : Excel sortant pour saisie Elza → ré-ingestion bronze de l'Excel modifié

## Périmètre fichiers source à analyser

Dossier `C:\Users\Shadow\Documents\GitHub\DWH_Contrôle de gestion\DWH_Contrôle de gestion\Suivi factures achats\` :
- `Suivi factures fournisseurs AEC.xlsx` (9.5 Mo) — instance AEC, pattern documenté en cartographie v2 §4.4
- `Suivi factures fournisseurs global.xlsx` (4.1 Mo) — consolidation multi-instances ?
- `Suivi factures-145.xlsb` (2.8 Mo) — site 145 AEG, format binaire
- `WoW suivi factures achats.xlsx` (12 Ko) — Way of Working / procédure métier

## Notes du sprint

| Note | Objet |
|---|---|
| `01-Brief-Claude-Code-Analyse-Fichiers.md` | Brief pour faire analyser les 4 fichiers Excel par Claude Code |
| `02-Resultats-Analyse-Fichiers.md` | Résultats de l'analyse (à remplir après exécution Claude Code) |
| `03-Conception-Silver-FAC.md` | Notes de conception silver factures fournisseurs |
| `04-Conception-Restitution-Pattern-OutIn.md` | Pattern de restitution Excel out → bronze in (réutilisable autres MEP) |
| `05-Brief-Claude-Code-Realisation.md` | Brief de réalisation Claude Code (steps SQL + scripts) |
| `06-Journal-Iterations.md` | Journal du sprint (décisions, itérations, blocages) |

## Points clés de méthode

### Pattern out → in (nouveau, à formaliser sur cette MEP)

Différence majeure vs MEP 1 :
- En MEP 1, les saisies manuelles Lilia étaient déjà absorbées dans les Excel historiques (pré-existantes) — pas de cycle re-saisie.
- En MEP 2, **le contrôle de gestion ajoute de la valeur sur le flux ERP** (commentaires compta, Chrono Sage, dates de paiement, statuts). Ces données n'existent pas dans CLIPPER.

**Conséquence architecturale** :
1. Le DWH génère un Excel agrégé "à compléter" (out)
2. Elza saisit ses colonnes manuelles
3. Le DWH ré-ingère le fichier modifié en bronze
4. La silver fusionne ERP + saisies Elza

À formaliser comme pattern réutilisable pour les autres MEP (FNP MEP 3, projets MEP 4 — cf. §5.4 cartographie v2 sur Tableau21714 qui a aussi ce profil).

### Référence aux fiches DWH

Toutes les fiches structurelles vivent dans le repo Git :
`C:\Users\Shadow\Documents\GitHub\DWH_Contrôle de gestion\DWH\`

Ce dossier Obsidian = **journal de sprint et briefs Claude Code**, pas la doc structurelle.

## Historique

| Date | Événement |
|---|---|
| 2026-04-25 | Reprise sprint après MEP 1, création dossier de sprint, brief analyse fichiers |
