# CRIM E-Facture — Base de travail

*Source : Redmine POP + GLPI. Généré le 20/08/2026.*

## Légende

| Colonne | Signification |
|---|---|
| **Statut** | Statut Redmine suivi de l'acteur en charge (spec → celui qui spécifie, dev → le développeur, validé → terminé) |
| **A/R RSI** | Nombre de retours de Justine Navarro après livraison |
| **Retard spec** | Jours de retard si la spec n'est **pas finalisée** et sa date est passée.<br>`N (valid.)` = spec livrée et finalisée, mais **en attente de validation métier** depuis N jours |
| **Retard dev** | Jours de retard si la date dev est passée et la CRIM n'est **pas encore Livré** |
| **Créé GLPI** | Date d'ouverture du ticket GLPI (vraie date de la demande) |
| **Spec / Dev initiale** | Première date planifiée |
| **Livr. spec / dev** | Date actuelle, avec `(±Nj)` d'écart vs la date initiale |

> **Jours ouvrés** — toutes les durées excluent les week-ends, les jours fériés français et le **13/07** (fermeture GA & Globasoft, appliquée aux seules CRIM développées par eux).


## Références CRIM ↔ Redmine ↔ ticket externe

| CRIM | Lot | Description | Redmine | Ticket externe |
|---|---|---|---|---|
| **#1** | L2 | Mise à disposition des factures au format UBL pour l | [20007](https://redmine.ga.fr/issues/20007) | [GLPI 25365](https://support.ga.fr/front/ticket.form.php?id=25365) |
| **#2** | L3 | Mise à disposition des factures éligibles à la démat | [20017](https://redmine.ga.fr/issues/20017) | [GLPI 26716](https://support.ga.fr/front/ticket.form.php?id=26716) |
| **#5** | L2 | Fiche « client » - Automatiser la définition d’une f | [20013](https://redmine.ga.fr/issues/20013) | — |
| **#6** | L2 | Fiche « Client », rendre obligatoire la saisie de «  | [20014](https://redmine.ga.fr/issues/20014) | — |
| **#7** | L2 | Fiche « Société », rendre obligatoire la saisie de « | [20015](https://redmine.ga.fr/issues/20015) | — |
| **#8** | L2 | Fiche « Client », rendre obligatoire la saisie du «  | [20008](https://redmine.ga.fr/issues/20008) | — |
| **#9** | L2 | Integrer l'editique Armony de la facture comme lisib | [20009](https://redmine.ga.fr/issues/20009) | [GLPI 26668](https://support.ga.fr/front/ticket.form.php?id=26668) |
| **#10** | L2 | Integrer l'editique Armony de la facture comme lisib | [20010](https://redmine.ga.fr/issues/20010) | [GLPI 26669](https://support.ga.fr/front/ticket.form.php?id=26669) |
| **#12** | L2 | Personnalisation pour saisir et automatiser sur les  | [20016](https://redmine.ga.fr/issues/20016) | — |
| **#14** | L1 | Ajuster la mise à disposition du référentiel fournis | [19994](https://redmine.ga.fr/issues/19994) | [GLPI 24386](https://support.ga.fr/front/ticket.form.php?id=24386) |
| **#16** | L1 | Mise a disposition des factures fournisseurs e-invoi | [19993](https://redmine.ga.fr/issues/19993) | [GLPI 25884](https://support.ga.fr/front/ticket.form.php?id=25884) |
| **#18** | L1 | Mise à disposition d’ESKER le cycle de vie de la fac | [20002](https://redmine.ga.fr/issues/20002) | — |
| **#20** | L1 | Fiche « fournisseur » - Automatiser la définition d’ | [20003](https://redmine.ga.fr/issues/20003) | — |
| **#21** | L1 | Fiche « fournisseur », rendre obligatoire la saisie  | [20004](https://redmine.ga.fr/issues/20004) | — |
| **#22** | L1 | Interdire le rejet technique de la facture fournisse | [19995](https://redmine.ga.fr/issues/19995) | — |
| **#23** | L1 | Automatiser l’envoi des factures électroniques à l'i | [20005](https://redmine.ga.fr/issues/20005) | — |
| **#24** | L1 | Gestion des lisibles factures fournisseurs dans le c | [19996](https://redmine.ga.fr/issues/19996) | [GLPI 26399](https://support.ga.fr/front/ticket.form.php?id=26399) |
| **#25** | L2 | Lobby pour valider les factures préliminaires des fa | [20011](https://redmine.ga.fr/issues/20011) | — |
| **#26** | L1 | Personnaliser le bon de commande (Edition Armony) po | [19997](https://redmine.ga.fr/issues/19997) | [Ootary TI26003547](https://armony.ootary.com/ticket_ticket/details/4291a4f7-9eb7-4ad3-82c8-dcf1174b4157) |
| **#27** | L2 | Récupérer les PJ additionnelles (hors lisible factur | [20012](https://redmine.ga.fr/issues/20012) | [GLPI 26675](https://support.ga.fr/front/ticket.form.php?id=26675) |
| **#28** | L1 | Mise à disposition des factures fournisseurs "e-invo | [19998](https://redmine.ga.fr/issues/19998) | [GLPI 25936](https://support.ga.fr/front/ticket.form.php?id=25936) |
| **#29** | L1 | Gestion des lisibles factures fournisseurs dans le c | [19999](https://redmine.ga.fr/issues/19999) | [GLPI 26560](https://support.ga.fr/front/ticket.form.php?id=26560) |
| **#30** | L1 | Changer l'encodage du fichier .csv ref fournisseur I | [20000](https://redmine.ga.fr/issues/20000) | — |
| **#31** | L1 | Changer l'encodage du fichier .csv ref fournisseur I | [20001](https://redmine.ga.fr/issues/20001) | — |
| **#32** | L1 | Automatiser le fait d’annuler après un refus de fact | [20006](https://redmine.ga.fr/issues/20006) | — |
| **#33** | L2 | Modification du template facture FACTORY pour GAE (e | [20024](https://redmine.ga.fr/issues/20024) | [GLPI 26882](https://support.ga.fr/front/ticket.form.php?id=26882) |

## Lot 1 — Fournisseur (eInvoicing)

### 🔴 P0

| # | Description | Statut | A/R RSI | Retard spec | Retard dev | Créé GLPI | Spec initiale | Livr. spec | Dev initiale | Livr. dev |
|---|---|---|---|---|---|---|---|---|---|---|
| 14 | Ajuster la mise à disposition du référentiel f | Validé — — | - | - | - | 17/04 | - | - | 04/07 | 04/07 |
| 16 | Mise a disposition des factures fournisseurs e | Validé — — | 5 | - | - | 19/06 | 07/07 | 07/07 | 20/07 | 26/06 (-14j) |
| 24 | Gestion des lisibles factures fournisseurs dan | Validé — — | 0 | - | - | 06/07 | 07/07 | 07/07 | 20/07 | 15/07 (-3j) |
| 26 | Personnaliser le bon de commande (Edition Armo | Validé — — | 1 | - | - | 09/07 | 08/07 | 08/07 | 16/07 | 24/07 (+6j) |
| 28 | Mise à disposition des factures fournisseurs " | Validé — — | - | - | - | 22/06 | 07/07 | 07/07 | 20/07 | 27/07 (+5j) |
| 29 | Gestion des lisibles factures fournisseurs dan | Validé — — | 3 | - | - | 09/07 | 07/07 | 07/07 | 20/07 | 27/07 (+5j) |
| 30 | Changer l'encodage du fichier .csv ref fournis | Validé — — | - | - | - | - | - | - | 04/07 | 04/07 |
| 31 | Changer l'encodage du fichier .csv ref fournis | Validé — — | - | - | - | - | - | - | 01/07 | 01/07 |
| 22 | Interdire le rejet technique de la facture fou | Livré — GA | 1 | - | - | - | 08/07 | 08/07 | 17/07 | 27/07 (+6j) |

### ⏱️ Durées du cycle *(jours ouvrés)*

De l'ouverture du ticket à la validation RSI. **D1 mesure la qualification interne** (avant que la demande n'arrive chez le prestataire) ; le **cycle presta** ne se compte qu'à partir de l'**arrivée presta** — escalade vers TMA Globasoft, ou création du ticket chez le prestataire lorsque le suivi se fait hors GLPI (Ootary).

| # | Créé ticket | Arrivée presta | Prise en compte | Livr. dev | Validé RSI | D1 créa→presta | D2 presta→prise | D3 prise→dev | D4 dev→RSI | Total |
|---|---|---|---|---|---|---|---|---|---|---|
| 14 | 17/04 | 15/06 | - | 04/07 | 07/07 | 37 | - | - | 2 | 16 |
| 16 | 19/06 | 22/06 | 23/06 | 26/06 | 20/07 | 1 | 1 | 3 | 14 | 18 |
| 24 | 06/07 | 06/07 | - | 15/07 | 20/07 | 0 | - | - | 3 | 8 |
| 26 | 09/07 | 09/07 | 09/07 | 24/07 | 11/08 | 0 | 0 | 10 | 12 | 22 |
| 28 | 22/06 | 22/06 | 29/06 | 27/07 | 28/07 | 0 | 5 | 18 | 1 | 24 |
| 29 | 09/07 | 10/07 | - | 27/07 | 11/08 | 1 | - | - | 11 | 20 |

- **#14** (GLPI 24386) — **D1** création ticket 17/04 → arrivée presta 15/06 = **37 j** *(qualification interne)* · **D4** livraison dev 04/07 → Validé RSI 07/07 = **2 j** · **Cycle presta (escalade→RSI) 16 j** — ⚠️ pas de message de prise en compte dans le fil GLPI
- **#16** (GLPI 25884) — **D1** création ticket 19/06 → arrivée presta 22/06 = **1 j** *(qualification interne)* · **D2** arrivée presta 22/06 → prise en compte 23/06 = **1 j** · **D3** prise en compte 23/06 → livraison dev 26/06 = **3 j** · **D4** livraison dev 26/06 → Validé RSI 20/07 = **14 j** · **Cycle presta (escalade→RSI) 18 j**
- **#24** (GLPI 26399) — **D1** création ticket 06/07 → arrivée presta 06/07 = **0 j** *(qualification interne)* · **D4** livraison dev 15/07 → Validé RSI 20/07 = **3 j** · **Cycle presta (escalade→RSI) 8 j** — ⚠️ pas de message de prise en compte dans le fil GLPI
- **#26** (Ootary TI26003547) — **D1** création ticket 09/07 → arrivée presta 09/07 = **0 j** *(qualification interne)* · **D2** arrivée presta 09/07 → prise en compte 09/07 = **0 j** · **D3** prise en compte 09/07 → livraison dev 24/07 = **10 j** · **D4** livraison dev 24/07 → Validé RSI 11/08 = **12 j** · **Cycle presta (escalade→RSI) 22 j**
- **#28** (GLPI 25936) — **D1** création ticket 22/06 → arrivée presta 22/06 = **0 j** *(qualification interne)* · **D2** arrivée presta 22/06 → prise en compte 29/06 = **5 j** · **D3** prise en compte 29/06 → livraison dev 27/07 = **18 j** · **D4** livraison dev 27/07 → Validé RSI 28/07 = **1 j** · **Cycle presta (escalade→RSI) 24 j**
- **#29** (GLPI 26560) — **D1** création ticket 09/07 → arrivée presta 10/07 = **1 j** *(qualification interne)* · **D4** livraison dev 27/07 → Validé RSI 11/08 = **11 j** · **Cycle presta (escalade→RSI) 20 j** — ⚠️ pas de message de prise en compte dans le fil GLPI

### 💰 Charges *(jours)*

Chiffrage initial (1er chiffrage dev, heures Redmine ÷ 8) face au temps passé déclaré par le prestataire. L'écart n'est significatif que sur les CRIM **terminées** : ailleurs, un consommé inférieur signifie simplement qu'il reste du travail.

| # | Statut | Chiffrage init. | Consommé | Écart |
|---|---|---|---|---|
| 14 | Validé | 1,5 j | 3,75 j | +2,25 j (+150 %) |
| 16 | Validé | 1,5 j | 6 j | +4,5 j (+300 %) |
| 22 | Livré | 0,5 j | 0,02 j | -0,48 j (-96 %) |
| 24 | Validé | 6 j | 7,75 j | +1,75 j (+29 %) |
| 26 | Validé | 4 j | - | - |
| 28 | Validé | 1 j | 7 j | +6 j (+600 %) |
| 29 | Validé | 3 j | 1,375 j | -1,625 j (-54 %) |
| 30 | Validé | 0,5 j | - | - |
| 31 | Validé | 0,5 j | - | - |
| **Total lot** | | **18,5 j** | **25,89 j** | |

- **#14** — chiffré **1,5 j**, consommé **3,75 j** → **+2,25 j (+150 %)** *(dépassement)*.
- **#16** — chiffré **1,5 j**, consommé **6 j** → **+4,5 j (+300 %)** *(dépassement)*.
- **#22** — chiffré **0,5 j**, consommé **0,02 j** → **-0,48 j (-96 %)** *(sous le budget)*.
- **#24** — chiffré **6 j**, consommé **7,75 j** → **+1,75 j (+29 %)** *(dépassement)*.
- **#26** — chiffré **4 j**, *aucun temps passé saisi à ce jour*.
- **#28** — chiffré **1 j**, consommé **7 j** → **+6 j (+600 %)** *(dépassement)*.
- **#29** — chiffré **3 j**, consommé **1,375 j** → **-1,625 j (-54 %)** *(sous le budget)*.
- **#30** — chiffré **0,5 j**, *aucun temps passé saisi à ce jour*.
- **#31** — chiffré **0,5 j**, *aucun temps passé saisi à ce jour*.

**Répartition de la charge par phase** *(jours, 8 h = 1 j)* — à quelle étape du cycle le temps a été consommé :

| # | Total | Avant arrivée presta | Attente prise en compte | Développement | A/R RSI | Après validation RSI |
|---|---|---|---|---|---|---|
| 14 | **3,75 j** | — | — | 3,75 j | — | — |
| 16 | **6 j** | — | — | 2,88 j | 3,12 j | — |
| 24 | **7,75 j** | — | — | 6 j | 1,75 j | — |
| 28 | **2,25 j** | — | — | 2,25 j | — | — |
| 29 | **1,38 j** | 1,38 j | — | — | — | — |
| **Total lot** | **21,12 j** | **1,38 j** (7 %) | **—** | **14,88 j** (70 %) | **4,88 j** (23 %) | **—** |

### 🟢 P1

| # | Description | Statut | A/R RSI | Retard spec | Retard dev | Créé GLPI | Spec initiale | Livr. spec | Dev initiale | Livr. dev |
|---|---|---|---|---|---|---|---|---|---|---|
| 18 | Mise à disposition d’ESKER le cycle de vie de  | En spécification — Justine Navarro | - | - | - | - | - | - | - | - |
| 20 | Fiche « fournisseur » - Automatiser la définit | En spécification — Justine Navarro | - | - | - | - | - | - | - | - |
| 21 | Fiche « fournisseur », rendre obligatoire la s | En spécification — Justine Navarro | - | - | - | - | - | - | - | - |
| 23 | Automatiser l’envoi des factures électroniques | En spécification — Justine Navarro | - | - | - | - | - | - | - | - |
| 32 | Automatiser le fait d’annuler après un refus d | En spécification — Justine Navarro | - | - | - | - | - | - | - | - |

## Lot 2 — Client invoicing

### 🔴 P0

| # | Description | Statut | A/R RSI | Retard spec | Retard dev | Créé GLPI | Spec initiale | Livr. spec | Dev initiale | Livr. dev |
|---|---|---|---|---|---|---|---|---|---|---|
| 9 | Integrer l'editique Armony de la facture comme | A recetter — Métier (recette) | - | - | - | 16/07 | 08/07 | 08/07 | 17/07 | 30/07 (+9j) |
| 27 | Récupérer les PJ additionnelles (hors lisible  | A recetter — Métier (recette) | - | - | - | 17/07 | - | - | 20/07 | 23/07 (+3j) |
| 25 | Lobby pour valider les factures préliminaires  | Validé RSI — RSI (Justine Navarro) | 1 | - | - | - | 10/07 | 09/07 (-1j) | 16/07 | 10/07 (-3j) |
| 1 | Mise à disposition des factures au format UBL  | Livré — Globasoft | - | - | - | 01/06 | 22/06 | 22/06 | 15/07 | 03/08 (+13j) |
| 8 | Fiche « Client », rendre obligatoire la saisie | Livré — Concret | 1 | - | - | - | 10/07 | 28/07 (+11j) | 10/07 | 31/07 (+14j) |
| 10 | Integrer l'editique Armony de la facture comme | En cours — Globasoft | - | - | 17 | 16/07 | 08/07 | 08/07 | 30/07 | 03/08 (+2j) |
| 33 | Modification du template facture FACTORY pour  | Prêt — ISIA | - | - | - | 27/07 | - | - | - | - |

### ⏱️ Durées du cycle *(jours ouvrés)*

De l'ouverture du ticket à la validation RSI. **D1 mesure la qualification interne** (avant que la demande n'arrive chez le prestataire) ; le **cycle presta** ne se compte qu'à partir de l'**arrivée presta** — escalade vers TMA Globasoft, ou création du ticket chez le prestataire lorsque le suivi se fait hors GLPI (Ootary).

| # | Créé ticket | Arrivée presta | Prise en compte | Livr. dev | Validé RSI | D1 créa→presta | D2 presta→prise | D3 prise→dev | D4 dev→RSI | Total |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 01/06 | 01/06 | 22/06 | 03/08 | - | 0 | 15 | 28 | - | - |
| 9 | 16/07 | 17/07 | - | 30/07 | 20/08 | 1 | - | - | 15 | 24 |
| 10 | 16/07 | 17/07 | - | - | - | 1 | - | - | - | - |
| 27 | 17/07 | 17/07 | 17/07 | 23/07 | 20/08 | 0 | 0 | 4 | 20 | 24 |
| 33 | 27/07 | - | - | - | - | - | - | - | - | - |

- **#1** (GLPI 25365) — **D1** création ticket 01/06 → arrivée presta 01/06 = **0 j** *(qualification interne)* · **D2** arrivée presta 01/06 → prise en compte 22/06 = **15 j** · **D3** prise en compte 22/06 → livraison dev 03/08 = **28 j**
- **#9** (GLPI 26668) — **D1** création ticket 16/07 → arrivée presta 17/07 = **1 j** *(qualification interne)* · **D4** livraison dev 30/07 → Validé RSI 20/08 = **15 j** · **Cycle presta (escalade→RSI) 24 j** — ⚠️ pas de message de prise en compte dans le fil GLPI
- **#10** (GLPI 26669) — **D1** création ticket 16/07 → arrivée presta 17/07 = **1 j** *(qualification interne)* — ⚠️ pas de message de prise en compte dans le fil GLPI
- **#27** (GLPI 26675) — **D1** création ticket 17/07 → arrivée presta 17/07 = **0 j** *(qualification interne)* · **D2** arrivée presta 17/07 → prise en compte 17/07 = **0 j** · **D3** prise en compte 17/07 → livraison dev 23/07 = **4 j** · **D4** livraison dev 23/07 → Validé RSI 20/08 = **20 j** · **Cycle presta (escalade→RSI) 24 j**
- **#33** (GLPI 26882) — cycle non encore mesurable — ⚠️ pas de message de prise en compte dans le fil GLPI

### 💰 Charges *(jours)*

Chiffrage initial (1er chiffrage dev, heures Redmine ÷ 8) face au temps passé déclaré par le prestataire. L'écart n'est significatif que sur les CRIM **terminées** : ailleurs, un consommé inférieur signifie simplement qu'il reste du travail.

| # | Statut | Chiffrage init. | Consommé | Écart |
|---|---|---|---|---|
| 1 | Livré | 22,5 j | 15 j | -7,5 j (-33 %) |
| 8 | Livré | 1 j | 1,313 j | +0,313 j (+31 %) |
| 9 | A recetter | 3 j | 1,75 j | -1,25 j (-42 %) |
| 10 | En cours | 3 j | 0 j | -3 j (-100 %) |
| 12 | En spécification | 3 j | - | - |
| 25 | Validé RSI | 1 j | - | - |
| 27 | A recetter | 3 j | 3,5 j | +0,5 j (+17 %) |
| 33 | Prêt | 4 j | - | - |
| **Total lot** | | **40,5 j** | **21,56 j** | |

- **#1** — chiffré **22,5 j**, consommé **15 j** → **-7,5 j (-33 %)** *(sous le budget)*.
- **#8** — chiffré **1 j**, consommé **1,313 j** → **+0,313 j (+31 %)** *(dépassement)*.
- **#9** — chiffré **3 j**, consommé **1,75 j** → **-1,25 j (-42 %)** *(sous le budget)*.
- **#10** — chiffré **3 j**, consommé **0 j** → **-3 j (-100 %)** *(sous le budget)*.
- **#12** — chiffré **3 j**, *aucun temps passé saisi à ce jour*.
- **#25** — chiffré **1 j**, *aucun temps passé saisi à ce jour*.
- **#27** — chiffré **3 j**, consommé **3,5 j** → **+0,5 j (+17 %)** *(dépassement)*.
- **#33** — chiffré **4 j**, *aucun temps passé saisi à ce jour*.

**Répartition de la charge par phase** *(jours, 8 h = 1 j)* — à quelle étape du cycle le temps a été consommé :

| # | Total | Avant arrivée presta | Attente prise en compte | Développement | A/R RSI | Après validation RSI |
|---|---|---|---|---|---|---|
| 1 | **14,12 j** | — | — | 14,12 j | — | — |
| 27 | **1,75 j** | 0,88 j | — | 0,88 j | — | — |
| **Total lot** | **15,88 j** | **0,88 j** (6 %) | **—** | **15 j** (94 %) | **—** | **—** |

### 🟢 P1

| # | Description | Statut | A/R RSI | Retard spec | Retard dev | Créé GLPI | Spec initiale | Livr. spec | Dev initiale | Livr. dev |
|---|---|---|---|---|---|---|---|---|---|---|
| 5 | Fiche « client » - Automatiser la définition d | En spécification — Justine Navarro | - | - | - | - | - | - | - | - |
| 6 | Fiche « Client », rendre obligatoire la saisie | En spécification — Justine Navarro | - | - | - | - | - | - | - | - |
| 7 | Fiche « Société », rendre obligatoire la saisi | En spécification — Justine Navarro | - | - | - | - | - | - | - | - |
| 12 | Personnalisation pour saisir et automatiser su | En spécification — Anaëlle Van | - | - | - | - | - | - | - | - |

## Lot 3 — Client reporting

### 🔴 P0

| # | Description | Statut | A/R RSI | Retard spec | Retard dev | Créé GLPI | Spec initiale | Livr. spec | Dev initiale | Livr. dev |
|---|---|---|---|---|---|---|---|---|---|---|
| 2 | Mise à disposition des factures éligibles à la | En spécification — Justine Navarro | - | 20 | - | 20/07 | 08/07 | 31/07 (+15j) | 28/08 | 28/08 |

### ⏱️ Durées du cycle *(jours ouvrés)*

De l'ouverture du ticket à la validation RSI. **D1 mesure la qualification interne** (avant que la demande n'arrive chez le prestataire) ; le **cycle presta** ne se compte qu'à partir de l'**arrivée presta** — escalade vers TMA Globasoft, ou création du ticket chez le prestataire lorsque le suivi se fait hors GLPI (Ootary).

| # | Créé ticket | Arrivée presta | Prise en compte | Livr. dev | Validé RSI | D1 créa→presta | D2 presta→prise | D3 prise→dev | D4 dev→RSI | Total |
|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 20/07 | 20/07 | 20/07 | - | - | 0 | 0 | - | - | - |

- **#2** (GLPI 26716) — **D1** création ticket 20/07 → arrivée presta 20/07 = **0 j** *(qualification interne)* · **D2** arrivée presta 20/07 → prise en compte 20/07 = **0 j**

### 💰 Charges *(jours)*

Chiffrage initial (1er chiffrage dev, heures Redmine ÷ 8) face au temps passé déclaré par le prestataire. L'écart n'est significatif que sur les CRIM **terminées** : ailleurs, un consommé inférieur signifie simplement qu'il reste du travail.

| # | Statut | Chiffrage init. | Consommé | Écart |
|---|---|---|---|---|
| 2 | En spécification | 22,5 j | 0 j | -22,5 j (-100 %) |
| **Total lot** | | **22,5 j** | **0 j** | |

- **#2** — chiffré **22,5 j**, consommé **0 j** → **-22,5 j (-100 %)** *(sous le budget)*.

## 📊 Synthèse consolidée — budget vs consommé

### Par lot

| Lot | CRIM chiffrées | Chiffrage init. | Consommé | Écart |
|---|---|---|---|---|
| Lot 1 — Fournisseur (eInvoicing) | 9 | 18,5 j | 25,89 j | +7,39 j (+40 %) |
| Lot 2 — Client invoicing | 8 | 40,5 j | 21,56 j | -18,94 j (-47 %) |
| Lot 3 — Client reporting | 1 | 22,5 j | 0 j | -22,5 j (-100 %) |
| **Total** | | **81,5 j** | **47,46 j** | **-34,04 j (-42 %)** |

> ⚠️ Cet écart global n'est **pas** une performance : la majorité des CRIM ne sont pas terminées, donc leur consommé est mécaniquement inférieur au budget. Seul le tableau des CRIM terminées ci-dessous est interprétable.

### CRIM terminées *(livrées ou au-delà)* — le seul écart interprétable

| # | Lot | Statut | Chiffrage init. | Consommé | Écart |
|---|---|---|---|---|---|
| 1 | L2 | Livré | 22,5 j | 15 j | -7,5 j (-33 %) |
| 8 | L2 | Livré | 1 j | 1,313 j | +0,31 j (+31 %) |
| 9 | L2 | A recetter | 3 j | 1,75 j | -1,25 j (-42 %) |
| 14 | L1 | Validé | 1,5 j | 3,75 j | +2,25 j (+150 %) |
| 16 | L1 | Validé | 1,5 j | 6 j | +4,5 j (+300 %) |
| 22 | L1 | Livré | 0,5 j | 0,02 j | -0,48 j (-96 %) |
| 24 | L1 | Validé | 6 j | 7,75 j | +1,75 j (+29 %) |
| 27 | L2 | A recetter | 3 j | 3,5 j | +0,5 j (+17 %) |
| 28 | L1 | Validé | 1 j | 7 j | +6 j (+600 %) |
| 29 | L1 | Validé | 3 j | 1,375 j | -1,62 j (-54 %) |
| **Total terminé** | | | **43 j** | **47,46 j** | **+4,46 j (+10 %)** |

### Répartition de la charge par phase, tous lots *(jours)*

| Phase | Charge | Part |
|---|---|---|
| Avant arrivée presta | 2,25 j | 6 % |
| Développement | 29,88 j | 81 % |
| A/R RSI | 4,88 j | 13 % |
| **Total** | **37 j** | **100 %** |