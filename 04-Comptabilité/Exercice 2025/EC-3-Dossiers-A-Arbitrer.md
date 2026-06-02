---
tags: ["comptabilité", "guinet-digital-group", "exercice-2025", "expert-comptable", "à-arbitrer"]
created: 2026-05-21
destinataire: Super Compteur
société: Guinet Digital Group
company_id_odoo: 4
---

# Dossiers à arbitrer — Clôture 2025 GDG

> 8 sujets nécessitant une décision ou une saisie de votre part avant clôture. Pour chacun : contexte, données chiffrées, proposition de traitement, alternative envisagée. Numérotation reprend [[EC-1-Synthese-2025#5. Sujets à arbitrer — vue résumée]].

---

## A. 🔴 ODs de paie 2025 — 12 mois manquants

### Contexte
- 1 salarié sur l'exercice : **M. Guillaume RHODES** (CDI), bulletins mensuels disponibles auprès de Super Compteur (cabinet de paie historique).
- Les **virements de salaire net** sont bien comptabilisés côté banque : 9 lignes 421000 / 15 430 € (BNK1 et BNK2).
- Les **prélèvements URSSAF** (12 mois, ~4 048 €) et **Klesia retraite** (11 mois, ~904 €) sont comptabilisés en 645100 / 645300 au paiement direct, **sans contrepartie 431000/437200**.
- Conséquence : compte 421000 affiche un solde débiteur de ~20 952 € (les virements nets sans la dette miroir), et 431000 / 437xxx sont quasi vides.

### Pièces justificatives
- 12 bulletins de paie 2025 (à fournir si pas déjà en votre possession via Super Compteur)
- 12 DSN mensuelles
- Détail des prélèvements bancaires 2025 BNK1 : Drive `2025_releves_bancaires`

### Proposition de traitement
12 ODs mensuelles dans le journal SLR (Odoo id 29) :

```
Dr 641100 Salaires bruts (montant brut bulletin)
Dr 645100 URSSAF patronale
Dr 645300 Retraite Klesia
Dr 645800 Mutuelle / prévoyance (Malakoff Humanis)
Dr 647100 / 648100 Tickets restau (quote-part employeur, Up France)
   Cr 421000 Salaire net à payer
   Cr 431000 URSSAF (cotisations sal+pat)
   Cr 437000 Mutuelle
   Cr 437200 Klesia retraite
```

Puis lettrage des comptes 431/437xxx avec les paiements BNK1 existants → tout doit retomber à zéro.

### Décision attendue
- **Option 1 (recommandée)** : nous saisissons les 12 ODs depuis les bulletins, vous validez les écritures.
- **Option 2** : vous saisissez directement (vous avez les bulletins) — schéma plus rapide.

---

## B. 🟡 Bug TVA Map Technologies — FAC/2025/00007 bloquée

### Contexte
- FAC/2025/00007 émise le 04/03/2025, Map Technologies, **5 280 € TTC** (4 400 € HT + 880 € TVA).
- Statut Odoo : `posted` mais `payment_state = not_paid` depuis 430+ jours.
- **Le paiement est en réalité reçu** : virement de 5 280 € le 09/04/2025 (BNK1/2025/00293, ligne Odoo id 8403), libellé "VIR MAP TECHNOLOGIES".
- Mais la ligne BNK1 n'a ni `partner_id` ni `full_reconcile_id` avec la FAC.

### Cause du blocage
- La ligne TVA de la FAC (Odoo id 6825) utilise `tax_repartition_line_id = 566` qui appartient à la société **"Le Petit Cerf"** (company_id=7) au lieu de GDG (company_id=4, équivalent = 258).
- Odoo refuse le lettrage avec : *"FAC/2025/00007 appartient à GDG, tandis que 'Taxes' appartient à une autre société."*
- 54 autres lignes TVA FAC 2025 utilisent correctement les repartition 206 ou 258 (GDG). C'est un **incident isolé** (probable mauvaise société active au moment de la saisie).

### Proposition de traitement
1. Modifier la ligne 6825 : `tax_repartition_line_id` 566 → 258 (équivalent GDG de la même taxe 20% S invoice)
2. Renseigner `partner_id = Map Technologies` sur la ligne BNK1 id 8403
3. Lancer le lettrage → `full_reconcile_id` automatique, FAC passe à `paid`

### Décision attendue
- **Option 1 (recommandée)** : on corrige techniquement comme ci-dessus, aucune incidence comptable
- **Option 2** : provision créance douteuse de 5 280 € (Dr 681000 / Cr 491000) si vous préférez tracer le risque dans le bilan
- **Option 3** : provision partielle (50 % = 2 640 €)

---

## C. 🔴 Amortissement Citroën C5 2025 — dotation manquante

### Contexte
- Véhicule acquis en 2024 (immobilisation 218200, financement 164100 Emprunt Citroën C5).
- En 2024 (11 mois), dotation passée par Super Compteur dans la liasse (à confirmer le montant exact).
- En 2025, **aucune écriture 681120 Dotation amortissement** n'a été saisie.

### Proposition
- Hypothèse : amortissement linéaire 5 ans, valeur brute amortissable ~30 000 € → 6 000 €/an.
- À passer en **une seule OD au 31/12/2025** (ou 12 OD mensuelles si vous préférez) :

```
Dr 681120 Dot. amort. matériel transport   6 000 €
   Cr 281820 Amort. matériel transport     6 000 €
```

### Décision attendue
- Confirmation du montant annuel (votre liasse 2024 fait foi)
- Confirmation 1 OD annuelle vs 12 mensuelles
- Vérifier le calcul TVS 2025 (635140) — pas encore saisi

---

## D. 🟡 Affectation résultat 2024 — OD AG non passée

### Contexte
- Bilan 2024 SC : **résultat net = 32 646 €** posté sur compte **120000 Résultat de l'exercice**.
- Selon procès-verbal AG 2024 (à fournir si AG tenue), affecter à 110000 Report à nouveau ou autre.
- À ce jour : 120000 = +32 646 €, 110000 = vide.

### Proposition
OD au 31/12/2025 (ou date AG si différente) :

```
Dr 120000 Résultat de l'exercice 2024  32 646 €
   Cr 110000 Report à nouveau          32 646 €
```

### Décision attendue
- Quand l'AG a-t-elle été tenue ?
- Affectation 100 % en report à nouveau, ou réserve légale + distribution dividendes ?

---

## E. 🟡 CCA inventaire 2025 — charges constatées d'avance

### Contexte
- Compte **486000 Prepayments** dispose déjà d'un à-nouveau 2 720 € (corrigé Phase 5 2024 par SC).
- Ligne ajoutée en 2025 : dépôt de garantie Bureau Toulouse 660 € (Etincelle Coworking) — **à reclasser** car un dépôt de garantie va sur compte 275, pas 486.
- Charges à reventiler en CCA fin 2025 (probablement) : RCP BPCE IARD prépayée, mutuelle prépayée, assurance Vie prépayée.

### Proposition
1. Reclasser le dépôt de garantie Etincelle 660 € : Dr 275000 / Cr 486000
2. Inventaire fin 2025 des prépaiements (à confirmer avec les contrats) :
   - RCP IARD : montant prorata 2026
   - Mutuelle Malakoff : montant prorata 2026
   - Vie Homme Clé BPCE : montant prorata 2026

OD au 31/12/2025 :

```
Dr 486000 CCA   X €
   Cr 616100 / 616160 / 645800 (selon nature)   X €
```

### Décision attendue
- Validation du chiffrage CCA (nous fournissons les montants si vous validez la méthode)
- Reclassement Etincelle ou laissez tel quel

---

## F. 🟡 Solde 512003 Compte TVA — +9 574 € anormal

### Contexte
- Compte annexe BPCE 95621009495 utilisé essentiellement pour les acomptes TVA payés au DGFIP.
- Activité résiduelle : 6 transactions janvier (virements TVA 020/021/022/023), 3 transactions août, **0 mouvement sept→déc 2025**.
- Solde Odoo +9 574 € au 31/12/2025 (acompte sans contrepartie ?), avec un solde réel banque +6 309 € au 31/12/2024 (à-nouveau).

### Hypothèses
- Soit acomptes TVA payés sans OD de TVA en miroir
- Soit déclaration CA3 du dernier trimestre non saisie en compta

### Proposition
1. Audit des 9 transactions 2025 sur 512003 vs déclarations CA3 trimestrielles 2025
2. OD de régularisation au 31/12/2025 si besoin (probable Dr 445510 ou 445660 / Cr 512003)
3. Vérifier si le compte BPCE 95621009495 est toujours actif (aucun mouvement depuis 08/2025)

### Décision attendue
- Pouvez-vous récupérer les CA3 2025 ?
- Compte 512003 à fermer (clôture banque) ou conserver ?

---

## G. 🟢 NDF Guinet Benoit 2026 — apurement 401 → 455010

### Contexte
- En mai 2026, 50+ NDF Guinet Benoit ont été saisies comme **BILLs fournisseurs** (séries FACTU/2026/01/0008 → FACTU/2026/04/0017) pour traçabilité TVA.
- Total ~4 100 € — toutes datées 13/05/2026 ou 14/05/2026 (date saisie, pas date des tickets).
- Apparaissent dans les dettes fournisseurs 401100 (8 026 € au 21/05/2026 dont ~4 100 € de NDF Benoit).
- **Ces dettes ne sont pas réelles** : il s'agit d'avances perso Benoit, à apurer par compensation avec 455010.

### Proposition
OD groupée à passer **côté 2026** (impact hors clôture 2025) :

```
Dr 401100 Guinet Benoit   ~4 100 €
   Cr 455010 C/C Benoit Guinet   ~4 100 €
```

Effet : les BILLs passent en `paid`, le compte 455010 enregistre la dette de la société envers Benoit (refinancée par futur virement BNK1 → Benoit).

### Décision attendue
- Procédé acceptable ? Ou préférez-vous un autre schéma (passage direct en charge sans BILL fournisseur) pour les NDF futures ?

> Cette pratique (NDF saisie comme BILL fournisseur du salarié-dirigeant) permet d'avoir la TVA déductible bien tracée, le détail par ligne de dépense et le PDF attaché à chaque BILL. À discuter si méthode plus légère préférée.

---

## H. 🟡 Lettrage 4671 BPCE Factor — finalisation

### Contexte
- Compte courant Factor 4671 : **48 lignes non lettrées**, solde net **-7 622 € créditeur** (decisions > cessions à fin 2025 — soit un avoir à recouvrer).
- 7 paires déjà lettrées au 10/05/2026 (juillet/septembre/décembre 2025).
- Reste : paires complexes août/octobre/novembre 2025 où décaissements partiels, libérations fonds garantie et commissions de financement s'entremêlent.

### Proposition
- Détail complet dans [[EC-5-BPCE-Factor]] (dossier joint)
- Sur la base des 32 PDFs (bordereaux + relevés CC + décomptes commissions) nous lettrerons les paires restantes.
- Reste à identifier un écart résiduel ~511 € sur le compte 4676 Fonds garantie (notre calc 4 194 € vs relevé Factor 3 682,80 €) — sera traité au cours du lettrage final.

### Décision attendue
- Aucune décision urgente — le lettrage 4671 ne change pas le résultat 2025 (jeu d'écritures entre comptes de bilan)
- Valider la méthode de calcul des commissions et libérations FG (cf. [[EC-5-BPCE-Factor]] §3)

---

## I. Autres points mineurs (information uniquement)

| Sujet | Statut |
|---|---|
| 2 drafts résiduels (OD 5277 VAT Juin 62 € + BNK2/2025/00255 Up France 208 €) | À investiguer — sans impact matérialité |
| BNK1 ligne 4177 (-127,43 € 30/12/2025 "SC regul") | À identifier — votre régularisation interne ? |
| BNK1 ligne 11615 (CARTE FACTURETTES CB déc) | À basculer 471000 → 580001 (compte de virement interne) |
| BNK3 9 transactions seulement sur 2025 | Compte fermé ou imports manquants ? |
| MISC2/2025/11/0001 OD "Transférer pièce 445740" | À neutraliser ou justifier |
| 6 factures CEC Bepmale pour Guinet Group | À créer côté **Guinet Group** (pas GDG) |
| Super Compteur F042517610 (864 €) | PDF manquant — facture pas encore créée dans Odoo |

---

## Récap décisions attendues

| # | Sujet | Action attendue de votre part |
|---|---|---|
| A | ODs paie | Validation méthode + fourniture bulletins si pas eu |
| B | Map Tech | Choix correction technique vs provision |
| C | Amort C5 | Confirmation montant annuel |
| D | Affectation 2024 | Date AG + détail affectation |
| E | CCA 2025 | Validation méthode chiffrage |
| F | 512003 TVA | Récupérer CA3 + décision fermeture compte |
| G | NDF Benoit | Validation schéma BILL+OD ou simplification |
| H | Factor 4671 | Validation méthode lettrage |

Sur un rendez-vous d'1h, on peut traiter A, B, C, D, G en discussion directe. E, F, H peuvent se faire par échange écrit après l'audit.

## Liens

- Synthèse : [[EC-1-Synthese-2025]]
- Mapping comptes : [[EC-2-Mapping-Comptes-2025]]
- Dossier Factor : [[EC-5-BPCE-Factor]]
- Référentiel partenaires : [[Referentiel-Partenaires-Comptes-GDG]]
- État de la situation interne (1787 lignes, journal de session) : [[00-Etat-de-la-situation]]
