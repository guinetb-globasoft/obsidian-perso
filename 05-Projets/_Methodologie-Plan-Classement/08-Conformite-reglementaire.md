---
tags: ["methodologie", "plan-classement", "conformite", "rgpd", "reglementaire"]
created: 2026-05-17
---

# 8. Conformité réglementaire

> Sommes-nous en règle au regard des obligations légales et sectorielles ?

## Principe

Au-delà de la pertinence et de l'usage, un plan de classement doit permettre à l'organisation de **respecter ses obligations légales** en matière de conservation, de protection et de production de documents.

C'est l'angle qui peut transformer un "défaut d'organisation" en **risque juridique** majeur.

## Obligations transverses à couvrir

### RGPD (Règlement Général sur la Protection des Données)
- **Minimisation** : ne pas conserver de données personnelles inutilement
- **Limitation de la conservation** : durées définies et appliquées
- **Droit d'accès / rectification / effacement** : pouvoir retrouver et agir sur les données d'une personne
- **Registre des traitements** : tenir à jour la cartographie
- **Sécurité** : confidentialité des données sensibles

### Code de commerce (entreprises)
- **Pièces comptables** : 10 ans
- **Documents fiscaux** : 6 ans minimum
- **Contrats commerciaux** : durée + 5 ans

### Code civil
- **Contrats** : prescription quinquennale (art. 2224) → 5 ans minimum
- **Responsabilité civile** : 10 ans (construction, etc.)

### Code du travail
- **Bulletins de paie** : conservation pendant toute la durée de présence + selon obligations légales en vigueur
- **Contrats de travail** : durée + 5 ans
- **Documents prévention** : variable selon type

### Sectoriel (selon contexte)
- **Santé** : conservation longue (jusqu'à 20 ans après la majorité du patient)
- **Banque/Finance** : ACPR, AMF, LCB-FT (5-10 ans)
- **Aéronautique / Industrie** : traçabilité production (souvent 30 ans+)
- **Secteur public** : Code du patrimoine, archives publiques
- **Défense / Sensible** : IGI 1300, classification confidentielle

## Obligations spécifiques aux projets IT

### Code source et licences
- Suivi des **licences open source** (compliance)
- Conservation des **livrables contractuels**
- Traçabilité **versions ↔ environnements**

### Données personnelles dans les SI
- Cartographie dans le **registre RGPD**
- Données de **test** : anonymisation / pseudonymisation
- **Logs** : durées limitées (souvent 6-12 mois)

### Cybersécurité (NIS2, LPM, etc.)
- Traçabilité des **incidents de sécurité**
- Conservation des **logs d'accès** privilégiés
- Plans de **continuité / reprise** (PCA / PRA)

### Marchés publics (si applicable)
- Conservation **dossiers de consultation** : 5-10 ans
- **Documents financiers** liés aux marchés : 10 ans
- Traçabilité des **décisions** et procédures

## Questions à poser

- [ ] La cartographie réglementaire applicable au projet a-t-elle été **identifiée** ?
- [ ] Le plan permet-il de **localiser rapidement** les documents soumis à obligation ?
- [ ] Les **durées de conservation** légales sont-elles définies catégorie par catégorie ?
- [ ] Le **registre RGPD** est-il à jour pour les traitements du projet ?
- [ ] Les **données personnelles** sont-elles identifiables / extractibles (droit d'accès) ?
- [ ] Existe-t-il une procédure de **réponse aux demandes** (CNIL, audit, contentieux) ?
- [ ] Les **mentions de confidentialité** sont-elles portées sur les documents sensibles ?
- [ ] Le plan distingue-t-il les **niveaux de classification** (public / interne / confidentiel) ?
- [ ] Les **délais de purge** sont-ils techniquement appliqués (pas juste théoriques) ?

## Signaux d'alerte 🚩

- Aucune cartographie réglementaire formalisée
- Données personnelles dispersées sans traçabilité
- Logs conservés "depuis le début" (5 ans, 10 ans...)
- Aucun document marqué confidentiel alors qu'il y en a manifestement
- Impossible de répondre à "où sont toutes les données concernant M. X ?"
- Pas de DPO impliqué dans la conception du plan
- Documents sensibles accessibles à tout le monde
- Pas de chiffrement / accès restreint sur les zones sensibles

## Articulation Plan ↔ Conformité

Le plan doit permettre 3 actions clés :

### 1. Localisation
"Où sont tous les documents soumis à l'obligation X ?"
→ Le plan doit permettre de répondre **immédiatement**.

### 2. Production
"Sortez-moi tous les contrats signés en 2023 avec leurs avenants."
→ La structure + les métadonnées doivent rendre l'extraction simple.

### 3. Suppression / Anonymisation
"Effacez toutes les données de M. X conformément à son droit à l'oubli."
→ Le plan doit permettre la **traçabilité** et l'**action ciblée**.

## Cas concrets à challenger

**Sur un projet ERP avec données clients**
- Si la CNIL demande un audit demain, peut-on extraire en 24h le registre des traitements à jour ?
- Si un client demande l'effacement de ses données, sait-on où elles sont toutes ?

**Sur un projet DWH avec données RH**
- Les données pseudonymisées en environnement de dev sont-elles traçables ?
- Les habilitations sont-elles documentées et auditables ?

**Sur un marché public**
- Le dossier de consultation est-il complet, daté, signé, conservé pour 10 ans ?
- En cas de recours, peut-on produire toute la procédure ?

## Acteurs à impliquer

- **DPO** (Délégué à la Protection des Données) : RGPD
- **RSSI** : sécurité, classification
- **Juriste / DAJ** : obligations contractuelles et réglementaires
- **Archiviste** : politique de conservation
- **Métier** : règles sectorielles spécifiques

## Lien avec les autres angles

- Conformité ↔ [[04-Calendrier-conservation-DUA|DUA / sort final]] : indissociables
- Conformité ↔ [[06-Metadonnees|métadonnées]] : confidentialité, classification, traçabilité
- Conformité ↔ [[03-Exhaustivite-exclusivite|exhaustivité]] : tout doc sensible doit être tracé

## Référence

- RGPD (Règlement UE 2016/679)
- Loi Informatique et Libertés modifiée
- Code du patrimoine (archives)
- Code de commerce, Code civil, Code du travail
- ISO 27001 (sécurité de l'information)
- NIS2 (cybersécurité)
- Référentiels sectoriels (ACPR, ANSSI, HAS, etc.)
