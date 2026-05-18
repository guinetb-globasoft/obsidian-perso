---
tags: ["comptabilité", "exercice-2024", "guinet-group", "diagnostic"]
created: 2026-05-08
---

---
tags: ["comptabilité", "guinet-group", "exercice-2024", "diagnostic", "alignement"]
created: 2026-05-08
société: Guinet Group
company_id: 1
---

# Diagnostic Odoo vs Bepmale — Guinet Group au 31/03/2024

> Confrontation des soldes Odoo et du bilan Bepmale à la date de clôture du 1er exercice (31/03/2024).
> 93 lignes posted dans Odoo Guinet Group ≤ 31/03/2024.

---

## 1. État des deux sources

### Bepmale (source de vérité — liasse fiscale déposée DGFiP)

| Catégorie | Montant |
|---|---|
| Total Actif | **11 342 €** (avant amortissements) |
| Total Passif | **11 342 €** |
| Total bilan net | 9 064 € (après amortissements 70 + perte 2 207 + capital 5 000…) |
| Résultat | **-2 207 €** (perte) |

### Odoo (état actuel)

| Catégorie | Montant |
|---|---|
| Total débits | **7 349 €** |
| Total crédits | 7 349 € |
| Équilibre | OK (D = C) |

→ **Le total Odoo est inférieur de ~4 000 € au total Bepmale.** Pas de comparaison directe possible : Odoo n'a saisi qu'**une partie** de la réalité comptable.

---

## 2. Soldes Odoo détaillés au 31/03/2024

| Compte | Débit | Crédit | Solde | Lignes | Note |
|---|---|---|---|---|---|
| 101401 Bank | 0 | 4 522,60 | 4 522,60 Cr | 3 | ⚠️ Compte par défaut Odoo, mal utilisé |
| 101402 Bank Suspense Account | 8 111,98 | 5 164,49 | 2 947,49 Dr | 14 | ⚠️ Compte d'attente — ne devrait pas figurer en bilan |
| 101405 FR7617807000179552197114463 | 0 | 554,05 | 554,05 Cr | 4 | Compte BP 4463 |
| 101406 GUINET GROUP XX8343 | 164,49 | 2 385,90 | 2 221,41 Cr | 22 | CB BP 8343 — solde Cr anormal |
| 211000 Account Payable | 0 | 50,80 | 50,80 Cr | 2 | ⚠️ Compte par défaut Odoo |
| 401100 Fournisseurs biens et services | 2 856,83 | 0 | 2 856,83 **Dr** | 28 | 🚨 **Solde DÉBITEUR anormal** (devrait être créditeur) |
| 445660 TVA déductible | 5,83 | 0 | 5,83 Dr | 3 | OK |
| 512110 BP Occitane | 5 000,00 | 3 506,26 | 1 493,74 Dr | 13 | OK structurellement |
| 600000 Expenses | 44,97 | 0 | 44,97 Dr | 4 | ⚠️ Compte par défaut Odoo |

---

## 3. Bilan Bepmale détaillé

### Actif (avant amort.)

| Compte SAGE | Libellé | Montant |
|---|---|---|
| 201100 | Frais de constitution | 708 Dr |
| 218300 | Matériel bureau & informatique | 1 716 Dr |
| 261100 | Actions (Globasoft) | 1 000 Dr |
| 418100 | Clients factures à établir | 3 000 Dr |
| 486000 | Charges constatées d'avance | 1 680 Dr |
| 512100 | Banque (BP Occitane) | 1 031 Dr |
| Sous-total | | **9 135 Dr** |

### Amortissements

| 280110 | Amort. frais constitution | 21 Cr |
| 281830 | Amort. matériel info | 49 Cr |

### Passif

| Compte SAGE | Libellé | Montant |
|---|---|---|
| 101000 | Capital | 5 000 Cr |
| 401000 | Fournisseurs divers | 1 778 Cr |
| 408100 | Fournisseurs FNP | 412 Cr |
| 421000 | Personnel | 1 298 Cr |
| 428200 | Dettes prov. CP | 177 Cr |
| 431000 | Sécurité sociale | 306 Cr |
| 437200 | ARRCO | 71 Cr |
| 438200 | Charges sociales sur CP | 3 Cr |
| 438600 | Autres charges à payer | 21 Cr |
| 455100 | C/C Guinet Benoit | 1 473 Cr |
| 487000 | Produits constatés d'avance | 733 Cr |
| Sous-total | | **11 272 Cr** |

### Résultat
| Résultat de l'exercice (perte) | -2 207 |

---

## 4. 🚨 Écarts critiques

### A) Comptes du bilan Bepmale ABSENTS d'Odoo

**Tout l'actif immobilisé est absent** :
- ❌ 201100 Frais de constitution (708 €)
- ❌ 218300 Matériel bureau & informatique (1 716 €)
- ❌ 261100 Actions Globasoft / GDG (1 000 €) ⚠️
- ❌ 280110 Amort. frais (21 €)
- ❌ 281830 Amort. matériel (49 €)

**La quasi-totalité des comptes de tiers du passif** :
- ❌ 418100 Clients factures à établir (3 000 €)
- ❌ 486000 CCA (1 680 €)
- ❌ 487000 PCA (733 €)
- ❌ 401000 / 408100 fournisseurs (1 778 + 412 €) → **les fournisseurs sont saisis sur 401100, pas 401000/408100**
- ❌ 421000 Personnel (1 298 €)
- ❌ 428200 Dettes provis. CP (177 €)
- ❌ 431000 Sécurité sociale (306 €)
- ❌ 437200 ARRCO (71 €)
- ❌ 438200 Charges sociales sur CP (3 €)
- ❌ 438600 Autres charges à payer (21 €)
- ❌ 455100 C/C Guinet Benoit (1 473 €) ⚠️
- ❌ 101000 Capital (5 000 €)
- ❌ Résultat (-2 207 €)

### B) Comptes Odoo ABSENTS du bilan Bepmale

⚠️ Ces soldes Odoo ne sont **nulle part** dans la liasse fiscale :

| Compte Odoo | Solde | Diagnostic |
|---|---|---|
| 101401 Bank | 4 523 Cr | Compte par défaut Odoo, **utilisé alors qu'il ne devrait pas** |
| 101402 Bank Suspense Account | 2 947 Dr | Compte d'attente — devrait être 0 |
| 101405 FR7617807000179552197114463 | 554 Cr | BP 4463 — non identifié dans le bilan Bepmale |
| 101406 GUINET GROUP XX8343 | 2 221 Cr | CB BP 8343 — non identifié dans le bilan Bepmale |
| 211000 Account Payable | 51 Cr | Compte par défaut Odoo |
| 401100 Fournisseurs | 2 857 **Dr** | Sens inversé ! |
| 600000 Expenses | 45 Dr | Compte par défaut Odoo |

### C) Banque : un seul compte chez Bepmale, plusieurs dans Odoo

Bepmale agrège tout sur **512100 = 1 031 €**. Odoo a 4 comptes différents (101401, 101405, 101406, 512110) totalisant net :
- 101401 : -4 523 Cr
- 101405 : -554 Cr
- 101406 : -2 221 Cr
- 512110 : +1 494 Dr

**Solde net Odoo banque** = 1 494 - 4 523 - 554 - 2 221 = **-5 805 € créditeur** (= banque en découvert massif !).
**Solde Bepmale banque** = +1 031 € débiteur.

→ **Écart de 6 836 €** sur la trésorerie !

### D) Solde fournisseurs anormal dans Odoo

Le compte **401100 a un solde DÉBITEUR de 2 857 €** alors qu'il devrait être créditeur (= dette envers fournisseurs). Ça veut dire que les **paiements** ont été imputés sur 401100 mais les **factures** n'ont jamais été saisies (ou alors saisies sur un autre compte).

C'est cohérent avec ce qu'on a vu sur GDG : import bancaire qui imute les paiements directement sur 401100 sans contrepartie de FACTU côté tiers.

---

## 5. Diagnostic global

**La compta Odoo de Guinet Group au 31/03/2024 n'est PAS la compta Bepmale.**

Ce qui s'est passé probablement :
1. Bepmale a fait la compta avec son outil SAGE en partant des relevés bancaires + factures + bulletins de paie + déclarations fiscales.
2. Odoo a été utilisé en parallèle pour saisir **uniquement** une partie des opérations bancaires (et encore, mal) — pas les factures, pas les paies, pas les amortissements, pas les CCA/PCA, pas le capital, pas l'interco.
3. Aucun à-nouveau de bilan Bepmale n'a jamais été repris dans Odoo.

**Conséquence pratique** : Odoo Guinet Group au 31/03/2024 est dans un état **inutilisable comme base** pour la suite — il faut le **reconstruire** en intégrant l'à-nouveau Bepmale.

---

## 6. Stratégie d'alignement (à valider)

### Option A — Reconstitution complète (lourd mais propre)

1. **Nettoyer Odoo** : supprimer ou neutraliser les écritures actuelles (qui ne reconstituent pas le bilan Bepmale).
2. **Saisir un journal d'à-nouveau** au 01/04/2024 reprenant **exactement** le bilan Bepmale au 31/03/2024 (avant affectation du résultat).
3. Repartir de cette base saine pour les exercices suivants.

→ Risque : perte d'historique des écritures bancaires détaillées 2024 dans Odoo. Mais comme cet historique n'a jamais été cohérent, ce n'est pas une vraie perte.

### Option B — Mode parallèle (Bepmale = source officielle, Odoo = outil opérationnel)

Accepter que Odoo et Bepmale divergent pour 2024, et **ne synchroniser qu'à partir de 2025** :
1. Saisir un journal d'à-nouveau au **01/01/2025** correspondant au bilan Bepmale au 31/12/2024 (à récupérer si exercice civil) ou au 31/03/2025 (si exercice fiscal 04→03).
2. Laisser Odoo 2024 tel quel ou l'archiver.

→ Plus rapide. Mais nécessite de récupérer le bilan Bepmale **2025** (ou le 2024 en année civile complète) pour l'à-nouveau.

### Option C — Hybride (recommandé)

1. **Créer dans Odoo le plan comptable manquant** (455100, 201100, 218300, 261100, 280110, 281830, 408100, 418100, 421000, 428200, 431000, 437200, 438200, 438600, 486000, 487000, 101000 si absent).
2. **Saisir une OD d'à-nouveau au 31/03/2024** (date pivot Bepmale) avec les soldes exacts du bilan Bepmale.
3. **Neutraliser ou délettrer** les écritures Odoo qui font doublon ou erreur sur cette période, plutôt que les supprimer.
4. Repartir propre pour la suite.

→ Conserve l'historique bancaire détaillé tout en alignant le bilan.

---

## 7. Questions bloquantes avant tout alignement

1. **Quelle date de pivot ?** 31/03/2024 (clôture Bepmale) ou 31/12/2024 (si exercice civil) ?
2. **Quelle est la durée du 2ème exercice Bepmale ?** A-t-on un 2ème bilan 04/2024 → 03/2025, ou 04/2024 → 12/2024 ?
3. **Veut-on aligner sur le bilan AVANT ou APRÈS affectation du résultat ?** (le PDF montre "avant affectation")
4. **Les comptes manquants ont-ils des libellés/configurations spécifiques** souhaités ? (ex : 455100 doit-il être nominatif "C/C Guinet Benoit" ou générique "Comptes courants associés" ?)
