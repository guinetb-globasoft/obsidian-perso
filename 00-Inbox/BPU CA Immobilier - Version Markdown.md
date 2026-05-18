---
tags: ["commercial", "CA-Immobilier", "BPU", "sohoft"]
created: 2026-04-24
---

---
tags: ["commercial", "CA-Immobilier", "BPU", "sohoft"]
created: 2026-04-24
related: "[[Propale Sohoft - CA Immobilier - Engagement 1]]"
---

# BPU — Mission CA Immobilier × SoHoft

**Version markdown pour itération facile** — miroir du fichier Excel `BPU_CA_Immobilier_SoHoft.xlsx`

**Forfait global : 68,5 j / 44 425 € HT** (base propale §10, intangible)

---

## Guide de lecture du bordereau

Ce BPU complète la proposition technique et financière SoHoft :

- **Démarrage** : 4 mai 2026 | **Fin** : 4 septembre 2026 | **Durée** : 18 semaines
- **Forfait global** : 68,5 j / 44 425 € HT (voir détail §10 de la proposition)
- Les prix sont **forfaitaires et fermes**, définitifs à la signature
- Le forfait est une prestation **indissociable** — les prix par ligne sont une ventilation analytique, pas une décomposition commerciale séparable

**Colonnes :**

- **Poste** : regroupement par nature d'activité (ne présage pas du séquencement)
- **Rappel des livrables** : livrables du poste tels qu'ils figurent dans la proposition (§4.8, §4.9, §10)
- **Feature / Lot de travail** : élément d'architecture ou brique fonctionnelle (parties P2 et P3)
- **Points de complexité** : indice relatif attribué par le prestataire
- **Charge J/H** : effort estimé en jours/homme
- **Indice de confiance (1-3)** : 1 = hypothèses à affiner, 2 = éléments standards, 3 = engageant sur éléments maîtrisés
- **Prix forfaitaire € HT** : TJM 700 € (Architecte / Expert / Pilotage) ou 550 € (Développeur Data Engineer)
- **Commentaire** : référence §propale + hypothèses de la ligne

---

## Section 1 — Cadrage & Conception (Périmètre 1)

**Sous-total : 34,5 j / 24 150 € HT**

### Ligne 1 — Animation des ateliers structurants

| Champ | Valeur |
|---|---|
| Poste | Animation des ateliers structurants |
| Feature / Lot | Kickoff + ateliers cadrage (architecture, gouvernance, FinOps, CISO, revue intermédiaire) |
| Points complexité | 5 |
| Charge | **8 j** |
| Confiance | 3 |
| Prix | **5 600 €** |

**Livrables :**

- Préparation et conduite du kickoff (S1)
- Animation des ateliers structurants : architecture cible (S2), gouvernance (S2), FinOps (S3), revue intermédiaire DAT (S4)
- Comptes-rendus des ateliers (formalisation 48h, diffusion aux parties prenantes)
- Décisions structurantes tracées et validées avant rédaction du DAT

**Commentaire :** Propale §10.2 Lot 1 — Kickoff et animation des ateliers cadrage (8j). Activité de conception et d'animation, distincte du pilotage projet (cf. ligne 2). TJM Architecte Data 700 €.

---

### Ligne 2 — Pilotage projet (coproj + COPIL)

| Champ | Valeur |
|---|---|
| Poste | Pilotage projet (coproj + COPIL) |
| Feature / Lot | — |
| Points complexité | 2 |
| Charge | **1,5 j** |
| Confiance | 3 |
| Prix | **1 050 €** |

**Livrables :**

- 8 coproj hebdomadaires (30 min de tenue + 15 min de préparation chacun) avec le référent technique
- 2 COPIL (1 h de tenue + 1 h de préparation chacun) — COPIL 1 en S4 (revue intermédiaire DAT), COPIL 2 en S8 (clôture P1)
- Comptes-rendus du coproj et des COPIL
- Suivi de l'avancement, alertes et arbitrages tracés
- Préparation des supports de présentation pour les COPIL

**Commentaire :** Propale §10.2 Lot 1 — Pilotage projet (1,5j). Chiffrage selon règle mécanique : coproj 0,75 h × 8 sem = 6 h + COPIL 2 h × 2 = 4 h, soit 10 h arrondies à 1,5 j. **Hors pilotage** : animation des ateliers (ligne 1), rédaction des livrables, présentations DG/CISO (ligne 8). TJM Architecte Data 700 €.

---

### Ligne 3 — Spécifications générales (cadrage architecture)

| Champ | Valeur |
|---|---|
| Poste | Spécifications générales (cadrage architecture) |
| Feature / Lot | Cartographie AS-IS macro + ateliers cible |
| Points complexité | 5 |
| Charge | **5 j** |
| Confiance | 2 |
| Prix | **3 500 €** |

**Livrables :**

- Cartographie macro AS-IS : 37 flux Talend/SSIS + 1200 tables
- Inventaire des flux avec caractéristiques (source, cible, fréquence, volumétrie, criticité)
- Classification par domaine fonctionnel et par complexité
- Identification des dépendances majeures entre flux
- Estimation du coût MCO actuel par flux

**Commentaire :** Propale §10.2 Lot 2 — Cartographie AS-IS macro (5j). Niveau macro assumé ; la cartographie détaillée (RG ligne à ligne) est hors scope P1 — cf. §8.3 conditions limites.

---

### Ligne 4 — Spécifications détaillées (cas d'usage MVP)

| Champ | Valeur |
|---|---|
| Poste | Spécifications détaillées (cas d'usage MVP) |
| Feature / Lot | Spécifications détaillées Natio + NPM Altaix |
| Points complexité | 4 |
| Charge | **3 j** |
| Confiance | 2 |
| Prix | **2 100 €** |

**Livrables :**

- Spécifications Natio (source DR / Vente de Neuf) : 9 sources, 4 cibles, RG SQL + Java, 2 faits + 2 dimensions, historisation mensuelle
- Spécifications NPM Altaix (Patrimoine) : 15 sources, 7 cibles, 6 entités (CABINET, SECTEUR, SERVICE, LOT, BATIMENT, IMMEUBLE)
- Périmètre fonctionnel, modèle de données, volumétrie
- Critères d'acceptation et tests de recette attendus

**Commentaire :** Propale §10.2 Lot 2 — Spécifications détaillées cas d'usage MVP (3j). Constitue le "contrat de réalisation" du Périmètre 3 (§4.5 propale). Validation par référents métier avant J8.

---

### Ligne 5 — Intégration des recommandations CISO *(fusionnée dans la ligne 9 — DAT)*

| Champ | Valeur |
|---|---|
| Poste | (fusionné dans la formalisation DAT — ligne 9) |
| Feature / Lot | Intégration des recommandations CISO Groupe CA |
| Points complexité | 0 |
| Charge | **0 j** |
| Confiance | 3 |
| Prix | **0 €** |

**Commentaire :** L'intégration CISO est désormais incluse dans l'effort de formalisation du DAT (ligne 9, 10 j). Pas de charge séparée.

---

### Ligne 6 — Cadre FinOps

| Champ | Valeur |
|---|---|
| Poste | (spécifications — suite) |
| Feature / Lot | Cadre FinOps (document + templates) — Composant 4 |
| Points complexité | 3 |
| Charge | **3 j** |
| Confiance | 3 |
| Prix | **2 100 €** |

**Commentaire :** Propale §10.2 Lot 3 — Cadre FinOps (3j). Livrable = document + templates. Déploiement technique réalisé dans le P2 (§4.6.1, §8.3).

---

### Ligne 7 — Roadmap de migration globale

| Champ | Valeur |
|---|---|
| Poste | (spécifications — suite) |
| Feature / Lot | Roadmap de migration globale — Composant 5 (37 flux / 1200 tables) |
| Points complexité | 2 |
| Charge | **2 j** |
| Confiance | 2 |
| Prix | **1 400 €** |

**Commentaire :** Propale §10.2 Lot 3 — Roadmap de migration globale (2j). Priorisation + vagues trimestrielles. Cible T1 2027 pour migration complète.

---

### Ligne 8 — Supports de présentation DG et CISO

| Champ | Valeur |
|---|---|
| Poste | (spécifications — suite) |
| Feature / Lot | Supports de présentation Direction Générale et CISO |
| Points complexité | 2 |
| Charge | **2 j** |
| Confiance | 3 |
| Prix | **1 400 €** |

**Commentaire :** Propale §10.2 Lot 3 — Présentations DG et CISO (2j). Supports éditables remis au sponsor.

---

### Ligne 9 — Réalisation du dossier de conception technique (DAT)

| Champ | Valeur |
|---|---|
| Poste | Réalisation du dossier de conception technique (DAT) |
| Feature / Lot | — |
| Points complexité | 10 |
| Charge | **10 j** |
| Confiance | 2 |
| Prix | **7 000 €** |

**Livrables :**

- Document d'Architecture Technique (DAT) complet
- Chapitre Snowflake dédié : zones, warehouses, RBAC, sécurité Business Critical, cycle de vie, observabilité
- **Intégration des recommandations CISO** (BIOK, Tri-Secret, Azure Key Vault, SSO Cerbère/ILEX, Data Masking, désensibilisation) — incluse dans la formalisation
- Architecture d'ingestion DLT + pattern d'alimentation unilatérale
- Architecture de transformation dbt Core (staging / intermediate / marts)
- Architecture d'orchestration Airflow
- Standards, conventions de nommage, schémas d'architecture
- Grille de chiffrage de migration (livrable 4.8.2)

**Commentaire :** Propale §10.2 Lot 2 — Formalisation DAT incluant intégration CISO (10j). L'effort CISO (questions S3, intégration réponses S5, itérations S7) est intégré dans la rédaction du DAT, pas chiffré séparément.

---

### ➡️ SOUS-TOTAL SECTION 1 : 34,5 j / 24 150 €

*Vérification : 8 + 1,5 + 5 + 3 + 0 (CISO fusionné) + 3 + 2 + 2 + 10 = 34,5 j ✓ | 5 600 + 1 050 + 3 500 + 2 100 + 0 + 2 100 + 1 400 + 1 400 + 7 000 = 24 150 € ✓*

---

## Section 2 — Développement, tests unitaires et d'intégration (Périmètres 2 + 3)

**Sous-total : 35 j / 21 200 € HT** *(ajusté après extraction de la recette en Section 3)*

### Sous-section 2.A — Périmètre 2 : Déploiement Snowflake

#### Ligne 10 — Setup compte Snowflake

| Champ | Valeur |
|---|---|
| Poste | Développement, tests unitaires et d'intégration (hors garantie) |
| Feature / Lot | Périmètre 2 — Setup compte Snowflake, databases, schemas, zones (raw/staging/core/marts) |
| Points complexité | 1 |
| Charge | **1 j** |
| Confiance | 3 |
| Prix | **575 €** |

**Livrables de la section :**

- Scripts et configurations de déploiement Snowflake (infrastructure-as-code)
- Pipelines DLT (Python) pour les 2 cas d'usage MVP
- Modèles dbt Core (staging, intermediate, core) avec tests natifs
- Macro dbt générique + template YAML (patron d'industrialisation)
- DAGs Airflow d'orchestration
- Tests unitaires et d'intégration compris
- Documentation technique et fonctionnelle des cas d'usage

**Commentaire :** Propale §10.3 P2 — Setup compte, databases, schemas, zones (1j). TJM Expert Snowflake 575 €.

---

#### Ligne 11 — Warehouses Snowflake

| Champ | Valeur |
|---|---|
| Feature / Lot | Périmètre 2 — Warehouses par usage + paramétrage (auto-suspend, scaling policy) |
| Points complexité | 1 |
| Charge | **1 j** |
| Confiance | 3 |
| Prix | **575 €** |

**Commentaire :** Propale §10.3 P2 — Configuration warehouses (1j). TJM Expert Snowflake 575 €.

---

#### Ligne 12 — RBAC Snowflake

| Champ | Valeur |
|---|---|
| Feature / Lot | Périmètre 2 — Déploiement RBAC (functional + access roles) selon DAT |
| Points complexité | 2 |
| Charge | **1,5 j** |
| Confiance | 3 |
| Prix | **862 €** |

**Commentaire :** Propale §10.3 P2 — Sécurité / déploiement RBAC (1,5j). TJM Expert Snowflake 575 €.

---

#### Ligne 13 — Environnements Dev/Recette/Prod

| Champ | Valeur |
|---|---|
| Feature / Lot | Périmètre 2 — Environnements Dev / Recette / Production + documentation |
| Points complexité | 1 |
| Charge | **1 j** |
| Confiance | 3 |
| Prix | **575 €** |

**Commentaire :** Propale §10.3 P2 — Environnements dev/rec/prod (1j). TJM Expert Snowflake 575 €.

---

#### Ligne 14 — Intégrations services Groupe

| Champ | Valeur |
|---|---|
| Feature / Lot | Périmètre 2 — Private Link (2j) + SSO Cerbère/ILEX (2j) + BIOK/Key Vault (3j) + Usercube (2j) + Graylog (1j) |
| Points complexité | 8 |
| Charge | **10 j** |
| Confiance | 2 |
| Prix | **5 750 €** |

**Commentaire :** Propale §10.3 P2 — Intégrations services Groupe (10j). Effort d'intégration côté Snowflake en coordination avec CAGIP et RSI CA Immobilier. Hypothèse : équipes Groupe disponibles et réactives sous 3 jours ouvrés. TJM Expert Snowflake 575 €.

---

#### Ligne 15 — Transverse P2

| Champ | Valeur |
|---|---|
| Feature / Lot | Périmètre 2 — Transverse (pilotage & coordination) |
| Points complexité | 1 |
| Charge | **0,5 j** |
| Confiance | 3 |
| Prix | **288 €** |

**Commentaire :** Propale §10.3 P2 — Pilotage et coordination (0,5j). TJM Expert Snowflake 575 €.

**Sous-total P2 : 15 j / 8 625 €**

---

### Sous-section 2.B — Périmètre 3 Natio (Talend / SQL Server, complexité moyenne)

#### Ligne 16 — Analyse RG Natio

| Champ | Valeur |
|---|---|
| Feature / Lot | Périmètre 3 / Natio — Analyse et documentation des règles de gestion (SQL + Java) |
| Points complexité | 5 |
| Charge | **3 j** |
| Confiance | 2 |
| Prix | **2 100 €** |

**Commentaire :** Propale §10.4 — Natio, analyse RG (3j). Conception Talend actuelle intègre RG SQL et Java. TJM Architecte Data 700 €. Risque spécifique : hypothèse 9.5 (RG Java de complexité standard).

---

#### Ligne 17 — Pipelines DLT + dbt staging Natio

| Champ | Valeur |
|---|---|
| Feature / Lot | Périmètre 3 / Natio — Setup pipelines DLT + modèles dbt staging (9 sources) |
| Points complexité | 5 |
| Charge | **5 j** |
| Confiance | 2 |
| Prix | **2 750 €** |

**Commentaire :** Propale §10.4 — Natio, DLT + dbt staging (5j). TJM Développeur Data Engineer 550 €.

---

#### Ligne 18 — dbt core Natio

| Champ | Valeur |
|---|---|
| Feature / Lot | Périmètre 3 / Natio — Modèles dbt core (2 faits + 2 dimensions, historisation mensuelle) |
| Points complexité | 3 |
| Charge | **2 j** |
| Confiance | 2 |
| Prix | **1 100 €** |

**Commentaire :** Propale §10.4 — Natio, modèles dbt core (2j). 2 tables de faits (Déclaration + Valeurs) + 2 dimensions.

---

#### Ligne 19 — Tests dbt et documentation Natio *(offert)*

| Champ | Valeur |
|---|---|
| Feature / Lot | Périmètre 3 / Natio — Tests dbt et documentation |
| Points complexité | 0 |
| Charge | **0 j** |
| Confiance | 3 |
| Prix | **0 €** |

**Commentaire :** Tests unitaires et documentation Natio **offerts** dans le cadre de cette proposition. Intégrés dans l'effort de développement des lignes 16 et 17.

**Sous-total Natio : 10 j / 5 950 €**

---

### Sous-section 2.C — Périmètre 3 NPM Altaix (SSIS / Oracle, complexité simple)

#### Ligne 20 — Macro dbt générique NPM Altaix

| Champ | Valeur |
|---|---|
| Feature / Lot | Périmètre 3 / NPM Altaix — Conception macro dbt générique + template YAML |
| Points complexité | 4 |
| Charge | **3 j** |
| Confiance | 3 |
| Prix | **2 100 €** |

**Commentaire :** Propale §10.4 — NPM Altaix, conception pattern générique (3j). TJM Architecte Data 700 €. Patron d'industrialisation réutilisable en Phase 2 (cf. Annexe C propale).

---

#### Ligne 21 — Instanciation 7 cibles Patrimoine

| Champ | Valeur |
|---|---|
| Feature / Lot | Périmètre 3 / NPM Altaix — Instanciation des 7 cibles du Patrimoine via template |
| Points complexité | 2 |
| Charge | **2 j** |
| Confiance | 3 |
| Prix | **1 100 €** |

**Commentaire :** Propale §10.4 — NPM Altaix, instanciation 7 cibles (2j). CABINET, SECTEUR, SERVICE, LOT, BATIMENT, IMMEUBLE + 1 table transverse.

---

#### Ligne 22 — Pipeline DLT, tests et documentation NPM Altaix *(offert)*

| Champ | Valeur |
|---|---|
| Feature / Lot | Périmètre 3 / NPM Altaix — Setup pipeline DLT, tests et documentation |
| Points complexité | 0 |
| Charge | **0 j** |
| Confiance | 3 |
| Prix | **0 €** |

**Commentaire :** DLT, tests et documentation NPM Altaix **offerts** dans le cadre de cette proposition. Intégrés dans l'effort de développement des lignes 19 et 20.

**Sous-total NPM Altaix : 5 j / 3 200 €**

---

### Sous-section 2.D — Transverse P3

#### Ligne 23 — Pilotage P3 (coproj + COPIL)

| Champ | Valeur |
|---|---|
| Feature / Lot | Périmètre 3 — Pilotage projet (coproj + COPIL) |
| Points complexité | 2 |
| Charge | **1 j** |
| Confiance | 3 |
| Prix | **700 €** |

**Commentaire :** Propale §10.4 — Pilotage P3 (1j). Chiffrage selon règle mécanique alignée sur P1 : coproj 0,75 h × 5 semaines pleines (S10, S11, S16, S17, S18) = 3,75 h + COPIL 2 h × 2 (COPIL 3 en S11, COPIL 4 en S18) = 4 h, soit 7,75 h arrondies à 1 j. **Hors pilotage** : ateliers métier de spécification (intégrés aux postes Natio et NPM Altaix), animation de la recette (intégrée aux postes de tests/recette/doc). La coupure estivale S12-S15 est sans sollicitation client, donc sans pilotage projet. TJM Architecte Data 700 €.

---

#### Ligne 24 — Intégration Airflow

| Champ | Valeur |
|---|---|
| Feature / Lot | Périmètre 3 — Intégration Airflow (orchestration des 2 cas d'usage) |
| Points complexité | 2 |
| Charge | **2 j** |
| Confiance | 2 |
| Prix | **1 100 €** |

**Commentaire :** Propale §10.4 — Airflow (2j). DAGs d'orchestration des pipelines DLT + runs dbt + contrôles qualité.

---

#### Ligne 25 — Coordination Snowflake

| Champ | Valeur |
|---|---|
| Feature / Lot | Périmètre 3 — Coordination avec l'environnement Snowflake |
| Points complexité | 1 |
| Charge | **1 j** |
| Confiance | 3 |
| Prix | **700 €** |

**Commentaire :** Propale §10.4 — Coordination Snowflake (1j). Interface avec l'admin Snowflake CAI pour mise en production assistée.

**Sous-total Transverse P3 : 4 j / 2 500 €**

---

### ➡️ SOUS-TOTAL SECTION 2 : 34 j / 20 275 €

*Vérification : P2 (15) + Natio (10) + NPM Altaix (5) + Transverse P3 (4) = 34 j ✓ | 8 625 + 5 950 + 3 200 + 2 500 = 20 275 € ✓*

---

## Section 3 — Recette de bout en bout

**Sous-total : 0 j / 0 € HT** *(recette offerte dans le cadre de cette proposition)*

### Ligne 26 — Recette métier des deux cas d'usage MVP

| Champ | Valeur |
|---|---|
| Poste | Recette de bout en bout de la solution complète |
| Feature / Lot | Recette métier Natio (Vente de Neuf) + NPM Altaix (Patrimoine) |
| Points complexité | 0 |
| Charge | **0 j** |
| Confiance | 3 |
| Prix | **0 €** |

**Commentaire :** Recette métier **offerte** dans le cadre de cette proposition. L'accompagnement recette est intégré dans l'effort de développement des cas d'usage (Périmètre 3).

---

### Ligne 27 — Préparation et assistance au déploiement en production

| Champ | Valeur |
|---|---|
| Poste | Préparation et assistance au déploiement en production |
| Feature / Lot | — |
| Points complexité | 0 |
| Charge | **0 j** |
| Confiance | 3 |
| Prix | **0 €** |

**Livrables :**

- Procédures d'installation et de configuration des composants Snowflake / dbt / Airflow
- Procédures d'exploitation (run, reprise sur incident, monitoring)
- Guide de transfert de compétence à l'équipe Data CA Immobilier
- Mise en production assistée des deux cas d'usage MVP

**Commentaire :** La préparation et la mise en production assistée sont INCLUSES dans les postes P2 (documentation + PV conformité) et P3 (transfert de compétence au J10, S18). Pas de coût additionnel.

---

### ➡️ SOUS-TOTAL SECTION 3 : 0 j / 0 €

---

## Section 4 — Garantie + Réversibilité

**Sous-total : 0 j / 0 € HT**

### Ligne 28 — Garantie

| Champ | Valeur |
|---|---|
| Poste | Garantie |
| Feature / Lot | — |
| Points complexité | 0 |
| Charge | **0 j** |
| Confiance | 1 |
| Prix | **0 €** |

**Livrables :**

- Bugs et anomalies résolu(e)s et livrables techniques redéployés
- Durée de garantie à convenir (typiquement 3 mois après mise en production)
- Canal de remontée des anomalies et SLA de réponse à définir
- Tenue d'un journal des incidents et des corrections

**Commentaire :** OPTION — Non incluse dans le forfait de base. La garantie est proposée séparément selon durée et SLA souhaités (typiquement 3 mois après MEP). Chiffrage sur demande.

---

### Ligne 29 — Réversibilité

| Champ | Valeur |
|---|---|
| Poste | Réversibilité |
| Feature / Lot | — |
| Points complexité | 0 |
| Charge | **0 j** |
| Confiance | 2 |
| Prix | **0 €** |

**Livrables :**

- Inventaire complet des documentations, sources, scripts et données reversés à CA Immobilier
- Code source sur le référentiel Git client (déjà le cas en mode natif dbt)
- Documentation de run, d'exploitation et de reprise sur incident
- Session de transfert de compétence à l'équipe interne

**Commentaire :** INCLUS DE FACTO dans le mode de travail : code dbt sur Git CAI, documentation publiée dans Confluence CAI, transfert de compétence au J10. Pas de frais de réversibilité additionnels au forfait.

---

### ➡️ SOUS-TOTAL SECTION 4 : 0 j / 0 €

---

## 🎯 TOTAL GÉNÉRAL

| Section | Charge | Prix HT |
|---|---:|---:|
| Section 1 — Cadrage & Conception (P1) | 34,5 j | 24 150 € |
| Section 2 — Développement (P2 + P3) | 34 j | 20 275 € |
| Section 3 — Recette de bout en bout | 0 j | 0 € |
| Section 4 — Garantie + Réversibilité | 0 j | 0 € |
| **FORFAIT GLOBAL** | **68,5 j** | **44 425 €** |

✓ Total conforme à la proposition §10.1

---

## Sommaire synthétique

| # | Ligne | Charge | Prix HT |
|---|---|---:|---:|
| | **SECTION 1 — Cadrage & Conception** | **34,5 j** | **24 150 €** |
| 1 | Animation des ateliers structurants | 8 j | 5 600 € |
| 2 | Pilotage projet (coproj + COPIL) | 1,5 j | 1 050 € |
| 3 | Spécifications générales (cadrage architecture) | 5 j | 3 500 € |
| 4 | Spécifications détaillées (cas d'usage MVP) | 3 j | 2 100 € |
| 5 | Intégration recommandations CISO (fusionnée dans DAT) | 0 j | 0 € |
| 6 | Cadre FinOps | 3 j | 2 100 € |
| 7 | Roadmap de migration globale | 2 j | 1 400 € |
| 8 | Supports de présentation DG et CISO | 2 j | 1 400 € |
| 9 | Réalisation du DAT (incluant CISO) | 10 j | 7 000 € |
| | **SECTION 2 — Développement (P2 + P3)** | **34 j** | **20 275 €** |
| 10-15 | Périmètre 2 — Déploiement Snowflake complet (6 lignes) | 15 j | 8 625 € |
| 16-19 | Périmètre 3 — Natio (4 lignes, dont tests/doc offerts) | 10 j | 5 950 € |
| 20-22 | Périmètre 3 — NPM Altaix (3 lignes, dont DLT/tests/doc offerts) | 5 j | 3 200 € |
| 23-25 | Périmètre 3 — Transverse (3 lignes) | 4 j | 2 500 € |
| | **SECTION 3 — Recette** | **0 j** | **0 €** |
| 25 | Recette métier (offerte) | 0 j | 0 € |
| 26 | Préparation et déploiement (inclus ailleurs) | 0 j | 0 € |
| | **SECTION 4 — Garantie + Réversibilité** | **0 j** | **0 €** |
| 27 | Garantie (option) | 0 j | 0 € |
| 28 | Réversibilité (incluse de facto) | 0 j | 0 € |
| | **TOTAL GÉNÉRAL** | **68,5 j** | **44 425 €** |

---

## Notes méthodologiques

**TJM appliqués :**

- 700 € HT : Architecte Data (lead), Expert Data Engineering, Pilotage
- 575 € HT : Expert Snowflake (déploiement plateforme, intégrations Groupe)
- 550 € HT : Développeur Data Engineer

**Indice de confiance :**

- 1 = charge comportant des hypothèses à affiner
- 2 = charge basée sur des éléments standards
- 3 = charge engageante sur éléments maîtrisés

**Principe commercial :** le forfait de 44 425 € HT est indissociable. La ventilation ci-dessus est analytique — elle permet au client de comprendre la structure du coût sans pouvoir détacher une ligne de manière isolée. Toute modification de périmètre fait l'objet d'un avenant conformément à §10.6 de la propale.

**Tests, recette et documentation offerts :** les lignes 18, 21 et 25 (tests dbt, documentation, recette métier) sont à 0 j / 0 € — leur effort est intégré dans les lignes de développement correspondantes. Cet investissement traduit notre engagement à livrer des cas d'usage complets et recettés, sans surcoût pour le client.

**Règle de chiffrage du pilotage projet (lignes 2 et 22) :**

- **Coproj hebdomadaire** : 30 min de tenue + 15 min de préparation = 0,75 h par coproj
- **COPIL** : 1 h de tenue + 1 h de préparation = 2 h par COPIL
- Cette règle s'applique mécaniquement et exclusivement au pilotage. Les ateliers de conception, la rédaction des livrables, les présentations DG/CISO et l'animation de la recette sont chiffrés séparément dans leurs postes respectifs.
