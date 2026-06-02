---
tags: ["comptabilité", "guinet-digital-group", "exercice-2025", "diagnostic"]
created: 2026-05-09
updated: 2026-05-21
---

# Diagnostic exercice 2025 GDG (état au 09/05/2026)

> **⚠️ Document snapshot au 09/05/2026** — Ce fichier conserve le diagnostic initial à valeur historique. Pour les chiffres actuels (21/05/2026), voir [[00-Etat-de-la-situation#📸 Snapshot Odoo 21/05/2026 — chiffres-clés à jour]].

> Premier exercice de 12 mois (01/01/2025 → 31/12/2025) après l'exercice court 2024 (01/02→31/12, 11 mois).

## Cadre

| Élément | Valeur |
|---|---|
| Période | 01/01/2025 → 31/12/2025 |
| À-nouveau | OD/2024/12/A-NOUVEAU (id 5530), 156 595 €, posted 31/12/2024 |
| Plan comptable | Aligné PCG/SC ([[Exercice 2024/06-Plan-Comptable-GDG-Mapping]]) |
| Cabinet présumé | Super Compteur (continuité) |
| Bilan SC 2025 | Pas encore disponible, exercice non clôturé |

## Volumétrie

| Catégorie | 2024 (11 mois) | 2025 (12 mois) | Évol. |
|---|---:|---:|:--|
| Factures clients (FAC) | 23 | **39** | +70% |
| Factures fournisseurs (FACTU) | ~70 | **170** | +143% |
| ODs FACTO BPCE Factor | 0 | **12** | nouveau |
| **CA HT estimé** | 123 600 € | **~201 178 €** | **+63%** |

## Factures clients 2025 (séquence FAC/2025/00001 → 00039, pas de trou)

Clients principaux :
- **Sohoft Toulouse** : client historique, environ 23 factures sur l'année
- **Map Technologies** : 1 facture (FAC/2025/00007, 5 280 €) — bug TVA, payé mais bloqué
- **AEROTEC & CONCEPT** : FAC/2025/00015 (16 476 €)
- **PINK SAS / ONE PINK / GA SAS (Sébastien Thalamy)** : nouveau client important sur S2
- **Mindeo - FZCO** : nouveau (1 facture draft FACTU/2025/11/0002)

## Factures fournisseurs 2025 (170)

Beaucoup de petits frais quotidiens : restaurants, taxis, fournitures, postes (NDF probable). Quelques fournisseurs récurrents :
- **Banque Populaire Occitane** : frais bancaires mensuels (FACTU/2025/MM/0001)
- **API RESTAURATION** : tickets repas réguliers
- **CARREFOUR HYPERMARCHES** : courses (rôle Benoit non clarifié — probable refacturation indemnité kilométrique ?)
- **MAXEL (OSMOZ), DICAPO, JIFU, BOWLING DU CHATEAU ROUSSILLON** : récurrents
- **Up France** : titres restau salarié

## ⚠️ Points critiques détectés

### A. 17 moves en draft (à arbitrer en priorité)

| Type | Nombre | Total | Détail |
|---|---:|---:|---|
| BILL Up France | 12 | ~1 656 € | Titres restau salarié, 21/01 → 05/10/2025 — pourquoi tous draft ? |
| BILL Mindeo - FZCO | 1 | 69 € | FACTU/2025/11/0002 |
| BILL anonymes (sans partner) | 3 | 47 € | 1 BILL 27 € (id 4861), 2 BILL 12,99 + 6,91 € (Gandi probable, ids 4845, 4843) |
| OD MISC "VAT Juin" | 1 | 62 € | id 5277, draft 30/06/2025 — anomalie séquence (idem que VAT Juin1 sur Phase 5) |
| OD MISC2 transfert 445740 | 1 | 0 € | MISC2/2025/11/0001 (id 4364), 23/11/2025 — "Transférer la pièce comptable sur 445740 TVA collectée sur opérations non réglées" |

### B. Lettrage clients 411 : 39 708 € non lettrés (6 lignes)

| Tiers | Montant | Statut |
|---|---:|---|
| AEROTEC & CONCEPT | 16 476 € | FAC/2026/00010 — récente |
| Sohoft Toulouse | 12 096 € | 2 lignes 2026 — récentes, normal |
| **Map Technologies** | 10 560 € | FAC/2025/00007 + BNK1/2025/00293 — **bug TVA, payé mais bloqué** |
| ONE PINK | 576 € | FAC/2026/00003 — récente |

### C. Lettrage fournisseurs 401 : **6 700 € sur 81 lignes non-lettrées** 🔴

Beaucoup de lignes anciennes (300-400j de retard). Pattern probable : **payé par CB personnelle de Benoit**, à reclasser en 455010 (compte courant) plutôt qu'en 401. Détail :
- Top 10 par montant : SARL SPORT BAR 711, CARREFOUR 562, LA POSTE 447, Up France 424, sans partenaire 362, MAXEL 349, PIMLICO 304, LES DEUX CAVISTES 264, QNPR 232, Au Pois Gourmand 227
- 9 lignes "sans partenaire" totalisant 362 €

### D. Bug TVA Map Tech (point reconnu, FAC/2025/00007 bloquée)
- tax_repartition_line 566 → 258 corrigée
- Mais erreur "tax_ids: '20% S', '20% S' appartient à une autre société" persiste
- Décision actuelle : laissé en l'état
- Impact : Map Tech reste `not_paid` dans Odoo malgré paiement réel

### E. Lettrage 4671 BPCE Factor : 50 lignes non-lettrées
- À traiter avec bordereaux Factor détaillés sous les yeux
- Lignes prioritaires : id=12178 (13 928,35€) FACTO/2026/01/0002, id=12295 (12 125,86€) FACTO/2026/02/0001

## Besoins pour clôture 2025

| Catégorie | Priorité | Détail |
|---|---|---|
| Drafts Up France (12 BILL) | 🔴 Haute | Décider : poster ou supprimer |
| Drafts anonymes (3 BILL + 1 OD MISC2) | 🟠 Moy | Renseigner partenaire / investiguer |
| OD VAT Juin draft (62 €) | 🟠 Moy | Origine ? |
| Lettrage 401 (81 lignes / 6 700 €) | 🟠 Moy | OD compensation 455010 (Benoit) ou rapprochement bancaire |
| Lettrage 4671 BPCE Factor | 🟠 Moy | Avec bordereaux détaillés |
| Bug TVA Map Tech | 🟢 Bas | OD compensation 411 si besoin |
| Vérif CA Odoo vs déclarations TVA mensuelles | 🔴 Haute | Confrontation 12 mois |
| Recensement fiches de paie 2025 | 🔴 Haute | Salaires, URSSAF, retraite |
| Amortissement Citroën C5 2025 | 🟠 Moy | 6 000 € (12 mois × 500) |
| Inventaire CCA 2025 | 🟠 Moy | Mutuelle, RCP, assurances pro |
| Affectation résultat 2024 | 🟠 Moy | 32 646 € : passer 120000 → 110000 après AG |

## Insights tirés de l'analyse 2024 (à appliquer en 2025)

1. **Centimes** : les bilans cabinet présentent les chiffres arrondis à l'euro. L'écart d'arrondi 0,53 € sur le résultat 2024 est sous le seuil de matérialité ; même méthode acceptée pour 2025.

2. **TVA "20% S"** : multiples taxes existent (id 38 GDG purchase, 60 GDG sale, 105/127 Le Petit Cerf, 172/194 Guinet Group - New). Toujours utiliser **id 60** pour les FAC GDG. Vérifier qu'aucune nouvelle facture 2025 n'a hérité d'une mauvaise tax_repartition.

3. **Pattern "Benoit avance"** : compte 455010 sert de tampon pour les frais payés perso. À ne pas confondre avec les vrais 401 (à régler par virement).

4. **Cabinet** : continuité Super Compteur. Date probable de bilan 2025 : T1 2026 (avril-mai).

## Liens
- Brief : [[../Brief-Comptable-Odoo]]
- Phase 5 GDG 2024 : [[../Exercice 2024/07-OD-A-Nouveau-31122024-GDG]]
- Bilan SC 2024 : [[../Exercice 2024/03-Comptes-annuels-GDG-2024]]
