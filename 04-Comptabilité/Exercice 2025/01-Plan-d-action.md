---
tags: ["comptabilité", "guinet-digital-group", "exercice-2025", "plan-action"]
created: 2026-05-08
updated: 2026-05-21
société: Guinet Digital Group
company_id: 4
---

# Plan d'action — Clôture exercice 2025 Guinet Digital Group

> Document vivant — alimenté au fil de l'analyse de l'état de la situation.
> Démarré le 08/05/2026. Refresh 21/05/2026 : les chiffres de phase et de volumétrie ci-dessous reflètent le diagnostic initial (08/05) ; pour l'état actuel **voir [[00-Etat-de-la-situation#📸 Snapshot Odoo 21/05/2026 — chiffres-clés à jour]]**.

## 🔄 Avancement réel au 21/05/2026 (résumé)

- ✅ **Phase 0 Diagnostic** : terminé (CA, trésorerie, lettrage)
- ✅ **Rapprochements bancaires BNK1/BNK2** : 13/13 statements 2025 (10/05/2026)
- ✅ **Lettrage 471000 BNK1/BNK2** : ~99% (1 + 3 lignes résiduelles 2025)
- ✅ **Drafts Up France** : tous postés (sauf BNK2/2025/00255 résiduel + OD VAT Juin)
- 🟡 **Lettrage 401** : 115 lignes ouvertes — désormais surtout des NDF Guinet Benoit 2026 à apurer via OD vers 455010 (gros chantier 08/05 réglé, nouveau chantier NDF émergé)
- ✅ **Lettrage 411 Map Tech** : à faire (bug TVA encore présent — FAC/2025/00007 toujours `not_paid`)
- ✅ **Interco 451000** : flux 2025 majoritairement reclassés (Phase L.1 du 10/05/2026)
- 🔴 **Phase 2.2 ODs de paie 2025** : 12 ODs toujours à créer
- 🔴 **Phase 4.2 Bilan Bepmale GDG 2024** : non récupéré
- 🔴 **Amortissement Citroën C5 2025** : non saisi

> Le plan détaillé ci-dessous (rédigé le 08/05) reste pertinent comme méthode ; seuls les volumes ont changé.

---

---

## Objectif

Mettre à jour la comptabilité 2025 de Guinet Digital Group le plus vite possible :
- Tous justificatifs 2025 saisis
- Tous comptes de tiers lettrés (411, 401, 4671, 421, 431, 451)
- Trésorerie rapprochée au 31/12/2025
- TVA déclarée correctement
- Comptes finaux prêts pour bilan

---

## Phases (à confirmer au fur et à mesure)

### Phase 0 — Diagnostic (en cours)
- [x] Chargement briefs Obsidian
- [x] CA 2025 + créances/dettes ouvertes
- [ ] Trésorerie + lettrage 411 + lettrage 401
- [ ] Inventaire factures clients / fournisseurs / OD 2025
- [ ] Trous mensuels (mois sans pièce)
- [ ] Comptes interco / paie / URSSAF

### Phase 1 — Saisie complémentaire
- À définir après diagnostic

### Phase 2 — Lettrages
- À définir après diagnostic

### Phase 3 — Rapprochements bancaires
- À définir après diagnostic

### Phase 4 — Contrôles de cohérence & TVA
- À définir après diagnostic

### Phase 5 — Préparation clôture
- À définir après diagnostic




---

## Plan d'action détaillé (mis à jour au 08/05/2026)

> Suite au diagnostic complet — cf. `00-Etat-de-la-situation.md`.

### Vue d'ensemble — ce qu'il faut faire

Quatre chantiers majeurs (par ordre de priorité business) :
1. 🚩 **Compta de paie 2025** (12 ODs manquantes + URSSAF + cohérence salaires bruts/nets)
2. 🚩 **Rapprochements bancaires** 512001 et surtout 512002 (sources des relevés à retrouver)
3. 🚩 **Lettrage 401** (95 lignes – conséquence directe des rapprochements ci-dessus)
4. ⚠️ **Compte courant interco 451** (zéro mouvement 2025 — anormal)

Plus quatre chantiers secondaires :
- Valider les 15 drafts fournisseurs (Up France principalement)
- Régulariser le compte TVA 512003 (+9 574 € de solde anormal)
- Vérifier les 13 résidus journal MISC1 (Affacturage déprécié)
- Recouvrement Map Technologies 5 280 € (ou provisionnement)

---

## Phase 1 — Préparation & sourcing des données externes (J0 → J+2)

**Objectif** : rassembler tout ce qu'il faut pour pouvoir saisir.

### 1.1 Paie 2025 — récupérer les bulletins
- [ ] Récupérer les 12 bulletins de paie 2025 (M. RHODES Guillaume) — Drive `social_2025`
- [ ] Vérifier qu'on a bien les états récapitulatifs URSSAF mensuels (DSN, montants à régler)
- [ ] Identifier les comptes 641xxx (salaires bruts) et 645xxx (charges patronales) à utiliser dans le plan comptable
- [ ] Si les comptes n'existent pas dans le plan comptable de Guinet Digital Group → les créer (`create_account`)

### 1.2 Banque — récupérer les relevés
- [ ] Relevés mensuels 512001 (compte principal) janv → déc 2025 — Drive `2025_releves_bancaires`
- [ ] Relevés mensuels 512002 GLOBASOFT XX7328 janv → déc 2025
- [ ] Vérifier ce qui existe vs ce qui manque sur Drive

### 1.3 Interco 451 — retrouver les flux 2025
- [ ] Lister depuis 512001 et 512002 toutes les lignes 2025 dont le libellé contient "GUINET GROUP" ou "VIR INST" interco
- [ ] Croiser avec les relevés banque côté Guinet Group (instance, company_id=1)

---

## Phase 2 — Saisies & corrections (J+2 → J+10)

### 2.1 Validation des drafts fournisseurs
**Effort : ~1 h · risque faible**
- [ ] Examiner les 15 pièces draft (cf. tableau 7.1 état de la situation)
- [ ] Pour chaque Up France : valider tiers, compte de charge (6257 ?), TVA, échéance → poster
- [ ] Renseigner partner_id sur les 2 drafts "—"
- [ ] Décider sur Mindeo et Gandi décembre

### 2.2 Saisie des ODs de paie 2025
**Effort : ~4-6 h · risque moyen (besoin des bulletins)**
- [ ] Pour chaque mois de 2025 (12 ODs) — journal SLR (id 29) :
  - Dr 641xxx Salaires bruts (montant brut)
  - Dr 645xxx Charges patronales URSSAF
  - Cr 421000 Salaires nets à payer (montant net)
  - Cr 431000 URSSAF (cotisations salariales + patronales)
  - Cr 437xxx autres organismes (mutuelle, retraite, etc.) si applicable
- [ ] Lettrer chaque ligne 421 par le virement banque correspondant (déjà en débit 421)
- [ ] Lettrer 431 par les paiements URSSAF (à saisir dans la phase 2.3)

### 2.3 Saisie des paiements URSSAF 2025
**Effort : ~2-4 h**
- [ ] Identifier les prélèvements URSSAF dans les relevés 512001 mensuels
- [ ] Saisir chaque paiement : Dr 431000 / Cr 512001
- [ ] Vérifier que le solde 431 revient à zéro à fin 2025 (au mois près si décalage de paiement)

### 2.4 Régularisation interco 451000
**Effort : ~2-4 h**
- [ ] Identifier et saisir tous les flux interco Guinet Digital ↔ Guinet Group de 2025
- [ ] Vérifier la cohérence avec le 451 chez Guinet Group (company_id=1)
- [ ] Convention courante : flux interco constatés via 451 (et non via 467x)

### 2.5 Rapprochements bancaires & lettrage 401
**Effort : ~6-12 h selon volume**
- [ ] Importer les relevés bancaires mensuels 512001 + 512002 (manquants)
- [ ] Pour chaque ligne du relevé qui correspond à une facture posée (FACTU/2025/...) → rapprocher (= lettrer 401)
- [ ] Cas particulier 512002 : vérifier qu'on a bien les mouvements **entrants** (alimentations) en plus des sorties
- [ ] Activer/configurer le lettrage automatique 4671 si possible (cf. point ouvert affacturage)
- [ ] Objectif : passer le solde 401 non lettré de 8 686 € à < 500 €

### 2.6 Régularisation 512003 Compte TVA
**Effort : ~1-2 h**
- [ ] Identifier l'origine du +9 574 € (probable acompte sans contrepartie ou OD de TVA manquante)
- [ ] Passer l'OD de régularisation (journal OD id=24)
- [ ] Vérifier la cohérence avec les déclarations CA3 trimestrielles

### 2.7 Résidus MISC1 (Affacturage déprécié)
**Effort : ~30 min**
- [ ] Vérifier que les 13 lignes restantes dans MISC1 sont toutes des extournes neutralisées
- [ ] Si oui, RAS. Sinon, basculer vers FACTO (id 61) ou neutraliser.

---

## Phase 3 — Contrôles & cohérence (J+10 → J+12)

### 3.1 Cohérence CA déclaré vs comptable
- [ ] Réconcilier le CA `get_chiffre_affaires` (201 178 €) avec la somme des FAC clients (241 414 €) — différence ~40 k€
- [ ] Vérifier la ventilation 706/707 et l'application des taux de TVA

### 3.2 Vérification soldes finaux 2025
- [ ] Trésorerie : solde Odoo vs relevé bancaire au 31/12/2025
- [ ] 411 : 5 lignes ouvertes attendues, 34 428 €
- [ ] 401 : < 10 lignes ouvertes attendues, < 500 €
- [ ] 421 : ~ 0 €
- [ ] 431 : ~ 0 € (ou un mois de cotisation décalé)
- [ ] 4671 BPCE Factor : à valider via brief affacturage
- [ ] 512003 Compte TVA : ~ 0 € après régularisation

### 3.3 Préparation déclarations & bilan
- [ ] Vérifier toutes les CA3 trimestrielles 2025
- [ ] Préparer les écritures de clôture (provision client Map Tech, OD d'inventaire, etc.)
- [ ] Bilan préparé pour expert-comptable

---

## Phase 4 — Dossiers spécifiques (en parallèle)

### 4.1 Map Technologies — FAC/2025/00007 (5 280 €)
- [ ] Décider : relance contentieuse OU provisionnement créance douteuse
- [ ] Si provision : Dr 681000 Dotations aux dépréciations / Cr 491000 Dépréciations comptes clients

### 4.2 Régularisation factures 2024 antédiluviennes
- [ ] 8 factures 2024 toujours non lettrées (Digidom, Le Tire Bouchon, Etincelle, Google Cloud, Up France, Tire Bouchon, GitHub, Guinet Benoit) — à neutraliser ou lettrer si paiement retrouvé

---

## Estimation globale

| Phase | Effort | Calendrier suggéré |
|---|---|---|
| 1. Sourcing | 2-4 h | Jour 1 |
| 2. Saisies | 17-30 h | Jours 2-10 (étalé) |
| 3. Contrôles | 4-6 h | Jours 11-12 |
| 4. Dossiers spé | 2-3 h | En parallèle |
| **Total** | **25-43 h** | **~2 semaines** |

---

## Prochaine étape concrète

Je propose de commencer par **Phase 1.1 — récupérer les bulletins de paie 2025** pour pouvoir attaquer les ODs de paie qui sont l'item le plus structurant.

Alternativement, on peut commencer par **Phase 2.1 — valider les 15 drafts fournisseurs** qui est un quick-win sans dépendance externe (1h max).

→ À toi de me dire par où on attaque concrètement.
