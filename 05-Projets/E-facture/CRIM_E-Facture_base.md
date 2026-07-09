# CRIM E-Facture - Base de travail (par lot, P0/P1)

> Source `GA C1113 ... 20260610.xlsx` - 26 CRIM non soldes/annules.  
> Process : **Spec -> Dev -> Test RSI -> Recette -> PROD**.  
> ⚠️ = P0 **valide** sans chiffrage et/ou sans date de livraison.

**Controle P0 valides incomplets : 10** -> #1, #2, #8, #22, #24, #25, #026, #27, #028, #29

## Lot 1 - Fournisseur - eInvoicing  (14)

### 🔴 P0 - GoLive (9)

| # | Statut | Avancement (Statut2) | Pipeline | Chiffrage | Redmine | GLPI | Objet |
|---|--------|----------------------|----------|-----------|---------|------|-------|
| **14** | Validé | MEP 4/07 | Spec OK > Dev OK > Test RSI OK > Recette OK > [PROD(4/07)] | spec 0.5j / real 1.5j | [#19994](https://redmine.ga.fr/issues/19994) | #24386 | Ajuster la mise à disposition du référentiel fournisseurs |
| **30** | Validé | MEP 4/07 | Spec OK > Dev OK > Test RSI OK > Recette OK > [PROD(4/07)] | real 0.5j | [#20000](https://redmine.ga.fr/issues/20000) | - | Changer l'encodage du fichier .csv ref fournisseur IFS > ESK |
| **31** | Validé | MEP 1/07 | Spec OK > Dev OK > Test RSI OK > Recette OK > [PROD(1/07)] | real 0.5j | [#20001](https://redmine.ga.fr/issues/20001) | - | Changer l'encodage du fichier .csv ref fournisseur INFOR > E |
| **16** | Validé | EN COURS DE DEVELOPPEMENT | Spec OK > [Dev] > Test RSI(20/07) > Recette > PROD | spec 1j / real 1.5j | [#19993](https://redmine.ga.fr/issues/19993) | #25884 | Mise à disposition des factures fournisseurs "e-invoicing" d |
| **24** ⚠️ | Validé | EN ATTENTE DE RETOUR DE BWS | Spec(07/07) OK > [Dev] > Test RSI(20/07) > Recette > PROD | - | [#19996](https://redmine.ga.fr/issues/19996) | En cours de co | Gestion des lisibles factures fournisseurs dans le cadre des |
| **028** ⚠️ | Validé | EN COURS DE DEVELOPPEMENT | Spec OK > [Dev] > Test RSI(20/07) > Recette > PROD | - | [#19998](https://redmine.ga.fr/issues/19998) | #25936 | Mise à disposition des factures fournisseurs "e-invoicing" d |
| **29** ⚠️ | Validé | EN ATTENTE DE RETOUR DE BWS | Spec(07/07) OK > [Dev] > Test RSI(20/07) > Recette > PROD | - | [#19999](https://redmine.ga.fr/issues/19999) | En cours de co | Gestion des lisibles factures fournisseurs dans le cadre des |
| **22** ⚠️ | Validé | A RENSEIGNER DANS DOSSIER DE PARAMETRAGE | [Spec] > Dev > Test RSI > Recette > PROD | spec 0.5j / real 0.5j | [#19995](https://redmine.ga.fr/issues/19995) | Dossier de par | Interdire le rejet technique de la facture fournisseur à par |
| **026** ⚠️ | Validé | A VALIDER (ELODIE / LAURENCE / JESSICA) | [Spec] > Dev > Test RSI > Recette > PROD | real 4j | [#19997](https://redmine.ga.fr/issues/19997) | - | Personnaliser le bon de commande (Edition Armony) pour  enle |

### 🟢 P1 - Post GoLive (5)

| # | Statut | Avancement (Statut2) | Pipeline | Chiffrage | Redmine | GLPI | Objet |
|---|--------|----------------------|----------|-----------|---------|------|-------|
| **18** | A chiffrer | - | [Spec] > Dev > Test RSI > Recette > PROD | - | [#20002](https://redmine.ga.fr/issues/20002) | - | Mise à disposition d’ESKER le cycle de vie de la facture fou |
| **20** | A chiffrer | - | [Spec] > Dev > Test RSI > Recette > PROD | - | [#20003](https://redmine.ga.fr/issues/20003) | - | Fiche « fournisseur » - Automatiser la définition d’une fich |
| **21** | A décider | - | [Spec] > Dev > Test RSI > Recette > PROD | - | [#20004](https://redmine.ga.fr/issues/20004) | - | Fiche « fournisseur », rendre obligatoire la saisie de « id  |
| **23** | A chiffrer | - | [Spec] > Dev > Test RSI > Recette > PROD | - | [#20005](https://redmine.ga.fr/issues/20005) | - | Automatiser l’envoi des factures électroniques à l'imputatio |
| **32** | A chiffrer | - | [Spec] > Dev > Test RSI > Recette > PROD | - | [#20006](https://redmine.ga.fr/issues/20006) | - | Automatiser le fait d’annuler après un refus de facture |

## Lot 2 - Client - eInvoicing  (10)

### 🔴 P0 - GoLive (6)

| # | Statut | Avancement (Statut2) | Pipeline | Chiffrage | Redmine | GLPI | Objet |
|---|--------|----------------------|----------|-----------|---------|------|-------|
| **1** ⚠️ | Validé | SPEC LIVREE A RELIRE / A VALIDER | [Spec] > Dev > Test RSI > Recette > PROD | spec 2.5j / real 22.5j | [#20007](https://redmine.ga.fr/issues/20007) | #25365 | Mise à disposition des factures au format UBL pour les clien |
| **8** ⚠️ | Validé | SPEC EN COURS DE REDACTION + DEV EN COURS | [Spec] > Dev > Test RSI > Recette > PROD | spec 0.5j / real 1j | [#20008](https://redmine.ga.fr/issues/20008) | - | Fiche « Client », rendre obligatoire la saisie du « SIRET »  |
| **9** | A chiffrer | - | [Spec] > Dev > Test RSI > Recette > PROD | - | [#20009](https://redmine.ga.fr/issues/20009) | - | Intégrer l’édition de la facture pdf au titre d’une pièce at |
| **10** | A chiffrer | - | [Spec] > Dev > Test RSI > Recette > PROD | - | [#20010](https://redmine.ga.fr/issues/20010) | - | Intégrer l’édition de la facture pdf au titre d’une pièce at |
| **25** ⚠️ | Validé | SPEC EN COURS DE REDACTION + DEV EN COURS | [Spec] > Dev > Test RSI > Recette > PROD | spec 0.75j / real 1j | [#20011](https://redmine.ga.fr/issues/20011) | - | Lobby pour valider les factures préliminaires des factures |
| **27** ⚠️ | Validé | A SPECIFIER | [Spec] > Dev > Test RSI > Recette > PROD | - | [#20012](https://redmine.ga.fr/issues/20012) | A spécifier | Récupérer les PJ additionnelles (hors lisible facture qui se |

### 🟢 P1 - Post GoLive (4)

| # | Statut | Avancement (Statut2) | Pipeline | Chiffrage | Redmine | GLPI | Objet |
|---|--------|----------------------|----------|-----------|---------|------|-------|
| **5** | A chiffrer | - | [Spec] > Dev > Test RSI > Recette > PROD | - | [#20013](https://redmine.ga.fr/issues/20013) | Accès refusé - | Fiche « client » - Automatiser la définition d’une fiche cli |
| **6** | A chiffrer | - | [Spec] > Dev > Test RSI > Recette > PROD | - | [#20014](https://redmine.ga.fr/issues/20014) | - | Fiche « Client », rendre obligatoire la saisie de « id adres |
| **7** | A chiffrer | - | [Spec] > Dev > Test RSI > Recette > PROD | - | [#20015](https://redmine.ga.fr/issues/20015) | - | Fiche « Société », rendre obligatoire la saisie de « id adre |
| **12** | Validé | SPEC LIVREE A RELIRE / A VALIDER | [Spec] > Dev > Test RSI > Recette > PROD | spec 1j / real 3j | [#20016](https://redmine.ga.fr/issues/20016) | - | Personnalisation pour saisir et automatiser sur les factures |

## Lot 3 - Client - eReporting  (2)

### 🔴 P0 - GoLive (2)

| # | Statut | Avancement (Statut2) | Pipeline | Chiffrage | Redmine | GLPI | Objet |
|---|--------|----------------------|----------|-----------|---------|------|-------|
| **2** ⚠️ | Validé | SPEC EN COURS DE REDACTION | [Spec] > Dev > Test RSI > Recette > PROD | real 22.5j | [#20017](https://redmine.ga.fr/issues/20017) | - | Mise à disposition des factures éligibles à la dématérialisa |
| **3** | A décider | - | [Spec] > Dev > Test RSI > Recette > PROD | spec 1.5j / real 22.5j | [#20018](https://redmine.ga.fr/issues/20018) | #25369 | Mise à disposition vers ESKER du e-reporting de transactions |