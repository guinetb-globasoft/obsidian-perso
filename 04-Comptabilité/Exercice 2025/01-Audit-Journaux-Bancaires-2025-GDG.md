---
tags: ["comptabilité", "guinet-digital-group", "exercice-2025", "audit-bancaire"]
created: 2026-05-09
updated: 2026-05-21
---

# Audit complétude des journaux bancaires GDG 2025

> Vérifier la couverture de chaque journal avant de continuer la clôture 2025.

> 🎯 **Tableau de bord clôture 2025** : voir [[00-Etat-de-la-situation#📸 Snapshot Odoo 21/05/2026 — chiffres-clés à jour]]
>
> **État BNK au 21/05/2026** : statements BNK1 + BNK2 = 100% complets (13/13 chacun, inchangé depuis 10/05). Lettrage BNK1 471000 sur 2025 = **~99% (1 ligne 6 € résiduelle)**. Lettrage BNK2 471000 sur 2025 = **~99% (3 lignes 14,74 € résiduelles)**. Le gros chantier de lettrage BNK est donc essentiellement clos.

## Configuration

| Journal | ID | Compte | Description | Mode alimentation |
|---|---:|---|---|---|
| **BNK1** Bank | 27 | 512001 | Compte principal | Connexion bancaire automatique |
| **BNK2** GLOBASOFT XX7328 | 30 | 512002 | CB différé liée au BNK1 | Imports manuels |
| **BNK3** Compte TVA | 31 | 512003 | Compte annexe utilisé uniquement pour TVA | Saisie manuelle |

## BNK1 — Compte principal (auto)

### Statements de relevé (account.bank.statement)
| Statement | ID Odoo | Date | balance_start | balance_end | balance_end_real | Status |
|---|---:|---|---:|---:|---:|---|
| 20250106 | 58 | 03/01 | 1 712,62 | 610,08 | 610,08 | ✅ |
| 20250204 | 57 | 04/02 | 610,08 | 449,58 | 449,58 | ✅ |
| 20250304 | 56 | 04/03 | 449,58 | 2 074,22 | 2 074,22 | ✅ |
| 20250402 | 55 | 01/04 | 2 074,22 | 9,72 | 9,72 | ✅ |
| 20250505 | 54 | 03/05 | 9,72 | 2 622,48 | 2 622,48 | ✅ |
| 20250605 | 53 | 04/06 | 2 622,48 | -9 708,77 | -9 708,77 | ✅ |
| 20250702 | 52 | 02/07 | -9 708,77 | -15 257,00 | -15 257,00 | ✅ |
| 20250804 | 50 | 02/08 | -15 257,00 | -14 320,94 | -14 320,94 | ✅ |
| 20250905 | 49 | 05/09 | -14 320,94 | -8 824,04 | -8 824,04 | ✅ |
| 20251002 | 48 | 30/09 | -8 824,04 | -3 603,09 | -3 603,09 | ✅ |
| 20251104 | 47 | 31/10 | -3 603,09 | -10 980,25 | -10 980,25 | ✅ |
| 20251205 | 89 | 04/12 | -10 980,25 | 1 228,01 | 1 228,01 | ✅ |
| 20260105 | 97 | 31/12 | 1 228,01 | 730,12 | 730,12 | ✅ créé 10/05/2026 |

> ✅ **Tous les 13 statements BNK1 2025 sont complets et équilibrés** (12 corrigés le 09/05/2026 — 13e créé le 10/05/2026).

### Récapitulatif lignes : 494 BNK1 sur 2025 — 13 statements complets

## BNK2 — CB différé (manuel)

> Vérifié dans Odoo le 10/05/2026. La situation a évolué depuis le premier audit du 08/05.

### Statements jan→juil 2025 — ✅ complets (IDs 82-88)

> `balance_start = 0` sur tous : cohérent avec un compte CB différé (solde remis à zéro chaque mois lors du débit sur BNK1).

| ID | Statement | Date | balance_start | balance_end | balance_end_real | Statut |
|---|---|---|---:|---:|---:|---|
| 82 | 20250106 | 2024-12-30 | 0,00 | -3 717,48 | -3 717,48 | ✅ |
| 83 | 20250204 | 2025-01-27 | 0,00 | -2 556,14 | -2 556,14 | ✅ |
| 84 | 20250304 | 2025-02-25 | 0,00 | -2 062,44 | -2 062,44 | ✅ |
| 85 | 20250402 | 2025-03-27 | 0,00 | -1 848,64 | -1 848,64 | ✅ |
| 86 | 20250505 | 2025-04-29 | 0,00 | -2 701,68 | -2 701,68 | ✅ |
| 87 | 20250605 | 2025-05-27 | 0,00 | -2 031,47 | -2 031,47 | ✅ |
| 88 | 20250702 | 2025-06-29 | 0,00 | -5 596,87 | -5 596,87 | ✅ |

### Statements août→déc 2025 — ✅ corrigés le 10/05/2026 (IDs 68, 65, 63, 61, 76, 96)

> **Cause racine** : `balance_start` incorrectement reporté (-4 920,19 €) au lieu de 0 (CB différé — solde remis à zéro chaque mois). Les lignes elles-mêmes étaient correctes (sommes = totaux PDF). Solution : `balance_start=0` + `balance_end_real` = total PDF signé.

| ID | Statement | Date | balance_start | balance_end_real | Statut |
|---|---|---|---:|---:|---|
| 68 | 20250804 | 04/08 | 0,00 | -4 630,84 | ✅ corrigé |
| 65 | 20250905 | 28/08 | 0,00 | -3 403,38 | ✅ corrigé |
| 63 | 20251002 | 02/10 | 0,00 | -3 003,49 | ✅ corrigé |
| 61 | 20251104 | 30/10 | 0,00 | -3 986,49 | ✅ corrigé |
| 76 | 20251205 | 26/11 | 0,00 | -2 443,97 | ✅ corrigé |
| 96 | Décembre | 30/12 | 0,00 | -2 221,30 | ✅ créé (46 lignes IDs 4745-4790) |

### Trous — tous comblés ✅
- ~~🚨 **6 mois manquants** : aucun statement BNK2 pour janvier → juin 2025~~ ✅ créés
- ~~🚨 **Aucun statement décembre 2025**~~ ✅ créé (id 96, 10/05/2026)
- ~~⚠️ **5 statements (août→nov) ont balance_end ≠ balance_end_real**~~ ✅ corrigé
- ~~🗑️ **7 vieux statements 2024** (IDs 8, 10, 13, 15, 18, 19, 66)~~ ✅ purgés (10/05/2026)

### Récapitulatif lignes : 231 BNK2 sur 2025
- **13 statements** couvrant jan→déc 2025, tous `is_complete=oui`, `balance_end=balance_end_real` ✅

## BNK3 — Compte TVA (manuel)

### Statements
**Aucun statement** créé pour 2025.

### Lignes : 9 transactions seulement
- **Janvier 2025** : 6 transactions (virements TVA, 02/01 à 13/01)
- **Août 2025** : 3 transactions (frais saisie + virement)
- **Reste de l'année** : aucune transaction

### Conclusion
BNK3 est **quasi-inactif** depuis fin août 2025. Activité résiduelle uniquement sur les déclarations TVA de janvier.

## Récapitulatif : trous à combler

| Journal | Trous |
|---|---|
| **BNK1** | ✅ **Complet** — 13 statements, tous équilibrés (12 corrigés 09/05/2026 — 13e créé 10/05/2026) |
| **BNK2** | ✅ **Complet** — 13 statements, tous équilibrés (corrigé 10/05/2026) |
| **BNK3** | À vérifier si activité réelle correcte (compte fermé ?) ou si imports manquants |

## Plan d'action proposé

1. ~~**Importer les relevés bancaires manquants** (BNK1 nov+déc 2025)~~ ✅
2. ~~**Corriger les balances incohérentes** sur statement 20250106 BNK1~~ ✅
3. ~~**BNK2** : importer relevés jan→juin 2025~~ ✅ · ~~Corriger balances août→nov, créer statement déc, purger 7 vieux statements 2024~~ ✅
4. **Investiguer BNK3** : compte vraiment fermé fin août 2025 ? Si oui, l'archiver
5. **Une fois bancaire à jour**, retourner aux drafts BILL Up France (point 1 du plan initial)

## Liens

- Diagnostic 2025 : [[00-Diagnostic-GDG-2025]]
- Brief : [[../Brief-Comptable-Odoo]]




---

## 🚨 BUG CRITIQUE découvert le 09/05/2026 : inversion mapping bancaire dans l'à-nouveau

### Faits vérifiés via PDFs BPCE

| Compte BPCE | IBAN | Solde 31/12/2024 | Type |
|---|---|---:|---|
| **55621004634** | FR76 1780 7000 1755 6210 0463 426 | **-35,92 €** (débiteur) | Compte courant principal opérationnel (CB, prélèvements, virements) |
| **95621009495** | FR76 1780 7000 1795 6210 0949 584 | **+6 309,12 €** (créditeur) | Compte annexe utilisé pour TVA |

### Mapping selon la liasse SC vs réalité Odoo

| SC dit | Montant | Vrai compte BPCE | Doit être sur | Mais l'à-nouveau Odoo a posté |
|---|---:|---|---|---|
| **512100 Banque** | 6 309 € (Db) | **95621009495** | BNK3 / 512003 | ❌ 512001 (BNK1) |
| **512000 Banque N°4634** | 36 € (Cr) | **55621004634** | BNK1 / 512001 | ❌ 512002 (BNK2) |

### Conséquences

- Le journal **BNK1 a 6 309 € en trop** depuis le 01/01/2025 (alors que le compte démarrait l'année à -35,92 €)
- Le journal **BNK2 a -36 €** alors qu'un compte CB différé n'a normalement pas de solde reportable (c'est un compte de transit interne)
- Le journal **BNK3 manque ses 6 309 €** d'à-nouveau

### Confirmation par les statements Odoo

- Le statement BNK1 `20250106` a **balance_start = 1 712,62 €** → c'est exactement le SOLDE CRÉDITEUR AU 05/12/2024 du compte **55621004634** dans le PDF BPCE
- Donc la **connexion bancaire BNK1 = 55621004634** ✅ (le journal Odoo est OK, c'est l'à-nouveau qui est faux)

### Action correctrice à appliquer

OD de correction au 31/12/2024 ou modification directe de l'à-nouveau (id 5530) :

| Compte | Sens | Montant |
|---|---|---:|
| 512001 BNK1 | **Cr** | 6 345,04 € (annule les 6 309 + ajoute les -36) |
| 512002 BNK2 | **Db** | 36 € (annule le -36 fictif) |
| 512003 BNK3 | **Db** | 6 309,12 € (apporte le vrai solde 95621009495) |

⚠️ Avant exécution : valider que les 78 lignes BNK1 de nov+déc 2025 ne sont pas affectées par cette correction (elles ne devraient pas l'être, car la correction est au 31/12/2024).

## Inventaire des PDFs disponibles localement (`C:/Users/Shadow/Downloads/Releves_BPCE_2025/`)

### Compte 55621004634 (→ BNK1)
- ✅ **12 extraits 2025** : 20250106, 20250204, 20250304, 20250402, 20250505, 20250605, 20250702, 20250804, 20250905, 20251002, 20251104, 20251205
- ✅ **12 relevés CB** (→ BNK2) : mêmes dates
- 12 factures pro mensuelles (frais bancaires)

### Compte 95621009495 (→ BNK3)
- 6 extraits seulement : 20250106, 20250204, 20250304, 20250402, 20250505, 20250905
- **6 mois sans extrait** : juin, juillet, août, oct, nov, déc 2025 (probablement aucun mouvement bancaire)

### Documents complémentaires
- 3 lettres de notification de rejet (20250804, 20250918, 20250929)
- 1 Impayé prêt (20250808)
- 2 souscriptions assurance prévoyance
- Plusieurs documents juridiques (Conditions Générales, IPID, etc.)




---

## ✅ Bug d'inversion corrigé (09/05/2026 — soir)

L'à-nouveau OD/2024/12/A-NOUVEAU (id 5530) a été corrigé directement :
- Ligne BNK1 : Db 6 309 → **Cr 36** (le vrai solde du 55621004634)
- Ligne BNK2 : Cr 36 → **supprimée** (CB différé n'a pas de solde de bilan)
- Ligne BNK3 : ajoutée **Db 6 309** (le vrai solde du 95621009495)

Total OD inchangé (156 595 €), équilibre OK, 25 lignes, posted.

Détail dans : [[../Exercice 2024/07-OD-A-Nouveau-31122024-GDG]]

**Conséquence** : maintenant le brief Claude Code [[02-Brief-ClaudeCode-Imports-BPCE]] peut router proprement les imports :
- `Extrait de compte 55621004634` → BNK1 (id 27, 512001)
- `Extrait de compte 95621009495` → BNK3 (id 31, 512003)
- `Relevé CB 55621004634` → BNK2 (id 30, 512002)

Reste à traiter :
- ~~78 lignes BNK1 nov+déc 2025 sans statement → créer les statements~~ ✅
- ~~Statement 20250106 BNK1 avec balance_end ≠ balance_end_real~~ ✅
- ~~Toutes les balances BNK2 incohérentes~~ ✅
- ~~Trous BNK2 jan→juin et déc 2025~~ ✅
- ~~31 lignes orphelines décembre BNK1 → créer statement 97~~ ✅ 10/05/2026

Actions en suspens :
- [x] 34 lignes orphelines novembre BNK1 — **confirmés doublons PDF vs bank feed, toutes supprimées 10/05/2026** ✅
  - 2 groupes délettrés (`full_reconcile` 678 + 495) avant suppression
  - ⚠️ 10 lignes statement 89 à re-lettrer : IDs 4718-4725 (8 COMMISSION CB) + 4712 (RYTHMEO) + 4705 (FRAIS SAISIE ADMIN)
- [ ] Fix ligne 11615 (BNK1/2025/00487 — CARTE FACTURETTES CB déc) → compte 471000 → 580001
- [x] Fix statement 76 BNK2 : déjà à -2 443,97 en Odoo ✅ — typo dans les notes corrigé

---

## ✅ BNK1 statements entièrement corrigés (09/05/2026 — nuit)

### Cause racine identifiée

L'import PDF des relevés BPCE avait créé des **lignes en double** pour chaque mois : une fois via la connexion bancaire automatique (bank feed, `statement_id=null`), une fois via l'import PDF (lignes dans le statement). Résultat : chaque statement avait ses lignes doublées, ce qui faussait `balance_end` vs `balance_end_real`.

De plus, certaines transactions étaient **présentes dans le PDF mais absentes du statement Odoo** (non capturées par l'import PDF), leur ligne bank feed étant orpheline.

### Actions réalisées

**Suppression de 79 lignes en double** (doublons PDF import non réconciliés) :
- Statement 47 (oct) : 40 lignes supprimées (BNK1/2025/00535→00574) — écart -18 241 € résolu
- Statement 49 (sep) : 16 lignes supprimées (BNK1/2025/00500→00515) — écart -2 139 € résolu
- Statement 48 (oct) : 19 lignes supprimées (BNK1/2025/00516→00534) — écart -853 € résolu
- Statement 57 (fév) : 3 lignes supprimées (BNK1/2025/00497→00499) — écart +13 636 € résolu
- Statement 58 (jan) : 1 ligne supprimée (BNK1/2025/00496) — écart +500 € résolu

**Assignation de 12 lignes orphelines** aux bons statements :
- Statement 89 (nov-déc) : 6 lignes BPCE Factor/virements (IDs 2987, 2990, 2997, 3005, 3989, 3994) ajoutées lors de la session précédente
- Statement 89 (nov-déc) : 6 lignes manquantes identifiées via PDF 20251205 (IDs 2988, 2989, 3974, 3990, 3992, 3993 — retraits CB + CARTE FACTURETTES + EUROVIR déc) ajoutées ce soir

### Résultat final

| Statement | Avant | Après |
|---|---|---|
| 20250106 (jan) | ⚠️ +500 € | ✅ 610,08 = 610,08 |
| 20250204 (fév) | ⚠️ +13 636 € | ✅ 449,58 = 449,58 |
| 20250905 (sep) | ⚠️ -2 139 € | ✅ -8 824,04 = -8 824,04 |
| 20251002 (oct) | ⚠️ -853 € | ✅ -3 603,09 = -3 603,09 |
| 20251104 (nov) | ⚠️ -18 241 € | ✅ -10 980,25 = -10 980,25 |
| 20251205 (déc) | ⚠️ +6 060 € | ✅ 1 228,01 = 1 228,01 |

Tous les 12 statements BNK1 2025 ont `is_complete = oui`.

---

## ✅ Lettrage BNK1 fournisseurs réalisé le 10/05/2026

### Méthode (Odoo 19 SaaS — reconcile_bank_line inopérant)

1. Trouver `account.move.line` compte 471000 (suspense) via `statement_line_id`
2. Batch `update_record` : `account_id` 1235 → 1134 (401100 Fournisseurs)
3. `reconcile_lines` : [ligne 401100 facture] + [ligne(s) 401100 bank]

### Digidom — 17 lignes BNK1 lettrées (compte 613500)

Toutes les lignes BNK1 Digidom 2025–2026 (28,80 €/mois ou 63,60 €/mois) lettrées avec leurs 17 factures fournisseurs FACTU.

### Super Compteur — 23 lignes BNK1 lettrées (compte 622600)

| Lot | Lignes BNK1 | Facture | Résultat |
|---|---|---|---|
| F250101613 | 12 × 172,80 € (jan–déc 2025) | FACTU/2025/01/0004 | ✅ Complet |
| F250101660 | 1 × 110,40 € (03/02/2025) | FACTU/2025/01/0005 | ✅ Complet |
| F250701796 | 1 × 82,80 € (04/07/2025) | FACTU/2025/07/0020 | ✅ Complet |
| F251001884 | 1 × 649,20 € (31/10/2025) | FACTU/2025/10/0024 | ✅ Complet |
| F260102001 | 5 × 188,40 € (jan–mai 2026) | FACTU/2026/01/0003 | 🔄 Partiel (7 prélèvements à venir) |
| F260102076 | 1 × 369,60 € (27/02/2026) | FACTU/2026/01/0004 | ✅ Complet |
| F260402149 | 1 × 210,00 € (30/04/2026) | FACTU/2026/04/0002 | ✅ Complet |
| F240701367 | 1 × 276,60 € (10/12/2024) | FACTU/2024/07/0001 | ⚠️ Partiel (5 acomptes 2024 non importés) |

**Lignes sans match BNK1 :**
- F240701384 (166,80 €) + F241001497 (328,80 €) + F250401718 (82,80 €) → relevés 2024 probablement non importés
- ID 4177 (-127,43 € 30/12/2025 "SC regul") → régularisation à identifier

---

## ✅ Lettrage BNK2 fournisseurs SaaS réalisé le 10/05/2026

### Méthode (même que BNK1)

1. Recherche des lignes BNK2 compte 471000 (suspense) par partenaire / montant
2. Batch `update_record` : `partner_id` + `account_id` 1235 → 1134 (401100)
3. Création facture fournisseur FACTU + `post`
4. `reconcile_lines` : [ligne 401100 BNK2] + [ligne 401100 facture]
5. `attach_file_to_record` : PDF Gandi/GitHub/Miro joint à la facture

### GitHub — 15 factures BNK2 lettrées (compte 615600)

- Partner id=91 (GitHub Inc., USA — hors UE → autoliquidation TVA, tax 20% S non applicable)
- Toutes les lignes BNK2 GitHub 2025 lettrées : FACTU/2025/01/0006 → /12/0011
- Montants : 16,99–17,13 €/mois (USD → EUR flottant)

### Miro — 12 factures BNK2 lettrées (compte 615600)

- Jan–Oct : RealtimeBoard Inc. (USA, USD) partner id=415 → autoliquidation
- Nov–Déc : RealtimeBoard BV (NL, EUR 20,00 €) → TVA UE 20%
- Toutes les lignes BNK2 Miro 2025 lettrées : FACTU/2025/01/0007 → /12/0013

### Gandi — 15 débits CB lettrés (compte 615600, TVA 20%)

Partner id=46 (Gandi SAS, FR81423093459 — fournisseur français, TVA normale 20%, tax id=38).

**H2 2025 (11 factures, traitées 10/05/2026) :**

| Facture Odoo | Ref Gandi | Date | TTC | BNK2 ID |
|---|---|---|---:|---:|
| FACTU/2025/07/0024 | … | juil | var. | — |
| … | | | | |
| FACTU/2025/12/0012 | … | déc | var. | — |

**H1 2025 (4 factures, traitées 10/05/2026) :**

| Facture Odoo | Ref Gandi | Date | TTC | BNK2 ID | Note |
|---|---|---|---:|---:|---|
| FACTU/2025/02/0007 | 2025021200223 | 12/02 | 7,20 € | 12785 | transfert globasoft.fr |
| FACTU/2025/05/0018 | 2025051100284 | 11/05 | 115,15 € | 12955 | ⚠️ 100% le-petit-cerf.* → interco GG (pt 20) |
| FACTU/2025/06/0024 | 2025061000508 | 10/06 | 71,22 € | 13025 | globasoft.fr + erp-control.* |
| FACTU/2025/06/0025 | 2025061900183 | 19/06 | 29,99 € | 13059 | glodoo.com/net/fr |

> Les 4 lignes BNK2 H1 n'avaient pas de `partner_id` — retrouvées par montant/date. Toutes à `account 471000` → corrigées en `401100`, lettrées, PDFs attachés.

### En suspens (Gandi)

- **~14 factures prépayées** (solde prépayé Gandi, pas de débit BNK2) — PDFs disponibles, décision à prendre sur création Odoo
- **460,51 € interco** (FACTU/2025/07/0025, 09/07) — 9 domaines GUINET GROUP → OD GDG→GG 451000 à créer
- **115,15 € interco** (FACTU/2025/05/0018, 11/05) — 100% le-petit-cerf.* → OD GDG→GG 451000 à créer

### Google Workspace — 10 factures BNK2 lettrées (compte 615600, TVA 20% S)

Partner id=17 (Google Cloud France SARL, FR78881721583 — fournisseur français, TVA normale 20%, tax id=38).

> Facturation adressée à "Globasoft" (ancien nom GDG) jan→sep 2025 (SIREN 983391079) puis "GDG" oct (SIREN 990641235) — bascule liée au renommage social août 2025. Toutes imputées GDG (option A : carte BNK2 = GDG).

| Facture Odoo | Ref Google | Période | TTC | BNK2 ID | Lettrage |
|---|---|---|---:|---:|---|
| FACTU/2025/01/0010 | GCFRD0008089984 | Jan | 49,68 € | 12767 | ✅ |
| FACTU/2025/02/0009 | GCFRD0008341539 | Fév | 84,72 € | 12817 | ✅ |
| FACTU/2025/03/0008 | GCFRD0008672075 | Mar | 124,20 € | 12871 | ✅ |
| FACTU/2025/04/0019 | GCFRD0008861770 | Avr | 124,20 € | 12933 | ✅ |
| FACTU/2025/05/0020 | GCFRD0009172920 | Mai | 124,20 € | 12993 | ✅ |
| FACTU/2025/06/0027 | GCFRD0009473608 | Juin | 142,42 € | 10109 | ✅ |
| FACTU/2025/07/0028 | GCFRD0009703932 | Juil | 163,96 € | 9849 | ✅ |
| FACTU/2025/08/0021 | GCFRD0010042250 | Août | 192,52 € | 9693 | ✅ |
| FACTU/2025/09/0035 | GCFRD0010312438 | Sep | 215,68 € | 9483 | ✅ |
| FACTU/2025/10/0031 | GCFRD0010749769 | Oct | 193,10 € | (Nov 1 à venir) | ⏳ BNK2 nov à importer |

**Total : 1 414,68 € · 9/10 lettrées · 1 PDF par facture attaché (ids 19900–19909)**

### En suspens (Google)

- **BNK2 ID 12719 (jan 1, 49,68 €)** = facture déc 2024 (non fournie)
- **BNK2 ID 9493 (oct 2, 12,10 €)** = charge Google non identifiée (probable GCP)
- **Google Storage/Play 4 lignes** (ids 9555, 9559, 10655, 10659 — 3,49 € + 7,19 € ×2) → traitement séparé

---

## 🎯 Bilan global lettrage BNK2 au 10/05/2026

| Paquet | Nb factures | Lignes lettrées | TTC total |
|---|---:|---:|---:|
| GitHub (US) | 15 | 15 | ~256 € |
| Miro (US/NL) | 12 | 12 | ~250 € |
| Gandi (FR) | 15 | 15 | ~340 € |
| Vercel (US) | 12 | 11 | 406 € |
| **Google (FR)** | **10** | **9** | **1 415 €** |
| **TOTAL paquets traités** | **64** | **62** | **~2 667 €** |

**Restant BNK2** : ~310 lignes / ~21 K€ — voir plan d'action [[00-Etat-de-la-situation#🚀 Plan d'action — séquence optimale pour clôturer]].

---

### Google Workspace — 10 factures BNK2 lettrées (compte 615600)

Partner id=17 (Google Cloud France SARL, FR78881721583 — fournisseur français, TVA 20%, tax id=38).

> Facturation adressée à "Globasoft" (ancien nom GDG) de Jan à Sep 2025 (SIREN 983391079). GDG renommé août 2025 → même entité juridique. Oct 2025 déjà au bon SIREN GDG (990641235). Charges débitées sur BNK2 → toutes imputées à GDG (option A).

| Facture Odoo | Ref Google | Période | TTC | BNK2 ID | Lettrage |
|---|---|---|---:|---:|---|
| FACTU/2025/01/0010 | GCFRD0008089984 | Jan 2025 | 49,68 € | 12767 | ✅ |
| FACTU/2025/02/0009 | GCFRD0008341539 | Fév 2025 | 84,72 € | 12817 | ✅ |
| FACTU/2025/03/0008 | GCFRD0008672075 | Mar 2025 | 124,20 € | 12871 | ✅ |
| FACTU/2025/04/0019 | GCFRD0008861770 | Avr 2025 | 124,20 € | 12933 | ✅ |
| FACTU/2025/05/0020 | GCFRD0009172920 | Mai 2025 | 124,20 € | 12993 | ✅ |
| FACTU/2025/06/0027 | GCFRD0009473608 | Juin 2025 | 142,42 € | 10109 | ✅ |
| FACTU/2025/07/0028 | GCFRD0009703932 | Juil 2025 | 163,96 € | 9849 | ✅ |
| FACTU/2025/08/0021 | GCFRD0010042250 | Août 2025 | 192,52 € | 9693 | ✅ |
| FACTU/2025/09/0035 | GCFRD0010312438 | Sep 2025 | 215,68 € | 9483 | ✅ |
| FACTU/2025/10/0031 | GCFRD0010749769 | Oct 2025 | 193,10 € | ⏳ Nov 1 | ⏳ BNK2 à importer |

**Total traité : 1 283,78 € · En suspens :**
- BNK2 ID 12719 (Jan 1, 49,68€) = facture déc 2024 (non fournie dans le dossier)
- BNK2 ID 9493 (Oct 2, 12,10€) = charge Google non identifiée (GCP ?)
- BNK2 IDs 9555+9559+10655+10659 (3,49€+7,19€ × oct+nov) = Google Storage/Play — à traiter séparément
