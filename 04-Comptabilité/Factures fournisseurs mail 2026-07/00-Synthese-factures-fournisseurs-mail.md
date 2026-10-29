# Factures fournisseurs récupérées par mail — 20/07/2026

> Dépouillement de la boîte **guinet.benoit@globasoft.fr** (`globasoft-perso`) : 132 factures fournisseurs 2026 identifiées, rapprochées des lignes bancaires réelles puis comptabilisées.
> Lié à [[00-Synthese-notes-de-frais-2026-07]].

## Résultat

| | Nb | Montant |
|---|---|---|
| Factures identifiées (2026) | 132 | — |
| Déjà en compta (Globasoft, lignes déjà lettrées) | 63 | — |
| **Créées + lettrées** | **57** | **2 757,04 €** |
| Doublon évité (déjà en base, seulement lettrée) | 1 | 12,00 € |
| Sans rapprochement bancaire (non saisies) | 11 | 986,62 € |

**Constat majeur** : Globasoft ESN était déjà à jour, mais **les abonnements de Guinet Digital Group n'avaient jamais été comptabilisés** — cohérent avec le fait que la CB 7328 de GDG n'avait jamais été ventilée.

## Guinet Digital Group — 51 factures (1 820,78 €), IDs 7836→7886

Fournisseurs : GitHub (6), Anthropic (7), Screencastify (6), Vercel (6), Miro (6), Excalidraw (2), Gandi (14), UpCoop (2), Chez Molly (2).
Toutes postées, PDF attaché, **lettrées avec leur ligne CB** (`payment_state = paid`, vérifié en base).

- **Compte de charge : 615600 Maintenance** (id 1340) pour les abonnements SaaS — aligné sur l'historique 2025 de la société (une première saisie en 622600 a été réalignée, 47 lignes, sans casser le lettrage).
- Exceptions conservées : **UpCoop → 647100** (titres-restaurant, tiers Up France), **Chez Molly → 625700** (réception).
- **Autoliquidation** : `20% EX` (id 36) pour les fournisseurs hors UE (US), `20% EU S` (id 35) pour Miro (NL) et Excalidraw (CZ).

⚠️ **Correction devise importante** : 14 factures (GitHub, Vercel, Excalidraw) sont libellées en **USD** alors que le débit bancaire est en EUR et plus faible (ex. GitHub « 20,00 USD » = **17,07 €** réels). Les montants EUR réellement débités ont été retenus — sinon chaque lettrage laissait ~3 € de résidu. Écart total : 1 879,70 annoncés → **1 820,78 comptabilisés**.

## Globasoft ESN — 6 factures (936,29 €) + 1 doublon évité

| Facture | Fournisseur | TTC | Compte | TVA |
|---|---|---|---|---|
| FACTU/2026/07/0003 | Odoo S.A. | 404,60 | 6135000 | autoliq. UE |
| FACTU/2026/06/0015 | Google Cloud France | 238,22 | 6135000 | TVA 20 % |
| FACTU/2026/07/0005 | Render Services | 236,23 | 615600 | autoliq. hors UE |
| FACTU/2026/07/0007 | Stello / AXA IARD | 23,98 | 616400 | sans taxe (TCA) |
| FACTU/2026/07/0006 | Excalidraw | 18,46 | 6135000 | autoliq. UE |
| FACTU/2026/07/0004 | Sinch Mailgun | 14,00 | 615600 | autoliq. hors UE |

**Doublon évité** : SEDOMICILIER 12,00 € — la facture `FACTU/2026/06/0013` existait déjà (postée, non lettrée). Elle a seulement été **rapprochée**, pas recréée.

Note : sur Globasoft, l'historique impute Odoo/Google/Excalidraw en **6135000 Location logiciels**, pas en 615600 — convention différente de GDG, respectée fournisseur par fournisseur.

## ⚠️ Deux points à valider

### 1. Autoliquidation sur la CA3 (Globasoft)
Les factures d'autoliquidation **antérieures (janv→juin) ont été saisies SANS aucune taxe**. J'ai appliqué les vraies taxes de reverse charge sur les nouvelles (impact net nul vérifié en brouillon, donc lettrage sans résidu). C'est **plus juste fiscalement** mais cela crée une rupture avec 6 mois d'historique et fait **apparaître de l'autoliquidation sur la CA3 de juillet**.
→ **À valider**, et à régulariser rétroactivement sur janv-juin si tu confirmes.

### 2. Deux doublons VP CONSEIL à annuler
| Facture Odoo | Réf | Montant | État |
|---|---|---|---|
| FACTU/2026/06/0001 (id 615) | F-26060481 | 60,00 | postée, **not_paid**, jamais prélevée |
| FACTU/2026/06/0002 (id 616) | F-26060483 | 275,36 | postée, **not_paid**, jamais prélevée |

Juin a en réalité été réglé via **Pennylane** (F-2026-06490 + F-2026-06506, toutes deux lettrées). Ces deux pièces sont des doublons de la bascule Fulll → Pennylane. → **À annuler / avoir** après confirmation du cabinet.

## Les 11 factures sans rapprochement (non saisies)

- **2 doublons avérés** : VP CONSEIL ci-dessus.
- **2 prélèvements à venir** : VP CONSEIL F-2026-07532 (33,60) et F-2026-07542 (385,76), SEPA annoncé au **22/07** — à saisir au prochain rapprochement.
- **1 déjà saisie** : VP CONSEIL F-26010254 (24,00) → `FACTU/2026/01/0007` existe.
- **6 récurrents GDG en attente du relevé CB de juillet** (le relevé s'arrête au 29/06) : Anthropic 90,00 · GitHub 20,00 · Miro 20,00 · Screencastify 20,00 · Gandi 18,00 · **Le Tire Bouchon 39,90** (restaurant → à imputer en **625700**, pas 615600).

## Archivage Drive

Les **127 PDF** (70 Globasoft + 57 GDG) ont été copiés dans `H:\Mon Drive\Comptabilité Groupe\<entité>\2026\Factures Fournisseurs`, conformément au [[00_Plan-de-classement]]. Les 5 sans société identifiée n'ont pas été classés.

## Divers
- Tiers **Stello / AXA France IARD** créé (id 430) — créé par erreur avec pays Gabon, corrigé en France.
