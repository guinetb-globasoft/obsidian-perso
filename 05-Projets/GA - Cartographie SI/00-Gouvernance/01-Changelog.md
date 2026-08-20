---
titre: Changelog
tags: [changelog]
---

# Changelog

## 2026-08-18 — Ouverture du projet et v1 des cartographies

**Demande** de Gildvin HIÉLARD : compléter `Présentation du SI vMASTER.pptx` avec deux
cartographies (strate fonctionnelle, strate applicative), ERP IFS au centre. Question
ouverte : « Possible avec Archi ? ». Destinataire final : Maëlle COUVREUX (DAF) →
consultants Deloitte / Delville en onboarding.

**Fait :**

- Extraction structurée de `INVENTAIRE - Applicatifs Métier.xlsx` : 150 applications,
  250 lignes de flux → `referentiel.json`
- **Contrôle qualité du référentiel** → [[01-Referentiel/01-Qualite-du-referentiel]].
  Constats : 14 extrémités de flux introuvables, 86 apps sans statut, Talend et Power BI
  non inventoriés, 26 IDs Archi manquants, 26/132 flux seulement avec protocole.
- **Taxonomie de 12 domaines fonctionnels** + affectation des 150 apps, 100 % de
  couverture → [[02-Taxonomie/01-Domaines-fonctionnels]]
- **Analyse du modèle Archi existant** (`Documents\Archi`, dépôt coArchi « GA ») :
  581 éléments, 156 composants applicatifs, 178 flux, 26 vues, scripts jArchi d'import.
  Découverte clé : **lien Excel↔Archi rompu côté applications (0 ID commun), intact
  côté flux (140/150)** → [[04-Outillage/01-Faisabilite-Archi]]
- **Livrable** : artefact web interactif publié (les 150 apps + les 132 flux, filtrables)
  + 2 slides PPTX dans une copie du vMASTER → [[03-Cartographies/01-Les-deux-vues-produites]]

**Arbitrage** : bascule slide → artefact web, à la demande de Benoît. Une slide ne peut
porter que 10 apps sur 150 et 24 flux sur 132.

**Non fait / à faire :**

- Croisement avec le repo Talend `ga-talend` et les docs de flux de
  `GA Smart Building\DSI - TMA Globasoft - Général` → confronter le **déclaratif**
  (inventaire) au **réel** (jobs Talend déployés). C'est la prochaine marche de fiabilité.
- Validation de la taxonomie par Gildvin.
- Arbitrage du chiffre communiqué : 61 flux actifs vs 132 vivants.
