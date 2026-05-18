---
tags: ["commercial", "CA-Immobilier", "propale", "sohoft"]
created: 2026-04-22
---

# Brief Sohoft — CA Immobilier

**Date :** 22/04/2026
**Intermédiaire :** Sohoft
**Objet :** S'accorder sur la stratégie de propale avant envoi
**Démarrage mission cible :** 4 mai 2026 (ASAP)
**Contexte :** 3 sociétés consultées dont nous

---

## 1. Ce qu'il faut retenir du besoin

- **Client :** Crédit Agricole Immobilier (Property Management + Promotion)
- **Interlocuteurs clés :** Ziyad Ben Messaoud (CDO), Florian Chaigne (Expert Talend / Ref tech)
- **Objectif :** Migration Modern Data Stack — sortir de Talend + SSIS + SQL Server, consolider 4 DW en 1 Snowflake
- **Stack cible confirmé :** Python + DLT (ingestion) / dbt + Snowflake (transfo) / Airflow (orchestration) / PowerBI (restit)
- **Modèle d'engagement demandé :** forfait avec engagement de résultat
- **Phase 1 en 5 étapes (leur slide) :** DAT → Déploiement Snowflake → Quick Wins (2 cas d'usage) → FinOps → Roadmap
- **Jalons :** T3 2026 fin phase 1 / 31/12/2026 2/3 du patrimoine migré / T1 2027 cible finale
- **Référentiel CISO groupe lourd :** BIOK/Tri Secret, Azure Key Vault, hébergement AWS Francfort, SSO Cerbère/ILEX, Usercube, Graylog, alimentation unilatérale, data masking PowerBI, désensibilisation non-prod

---

## 2. Répartition des rôles et contrainte financière

### Qui fait quoi sur l'engagement 1

**⚠️ Point structurant : la charge Snowflake (déploiement technique, étape 2 de la slide client) n'est PAS portée par Globasoft, elle est portée par Sohoft.**

| Étape slide client | Lot | Porteur | Commentaire |
|---|---|---|---|
| 1 | Conception & validation du DAT | **Globasoft** | Cœur de notre expertise |
| 1 | Cartographie AS-IS (macro) | **Globasoft** | Analyse Talend/SSIS |
| 1 | Intégration CISO | **Globasoft** | Architecture sécurité |
| 1 | Arbitrage dbt Cloud vs in Snowflake | **Globasoft** | Recommandation dans le DAT |
| 1/3 | Choix cas d'usage MVP + grille chiffrage | **Globasoft** | Sélection, pas implémentation |
| 4 | Cadre FinOps (doc + templates) | **Globasoft** | Conception du dispositif |
| 5 | Roadmap migration | **Globasoft** | Livrable doc |
| **2** | **Déploiement Snowflake** | **Sohoft** | **Paramétrage plateforme, config selon DAT — à chiffrer par eux** |
| 3 | Développement MVP (dbt/DLT) | **À clarifier** | Qui développe les 2 cas d'usage ? |
| 4 | Déploiement FinOps technique (resource monitors, tags, dashboard) | **À clarifier** | Probablement Sohoft si Snowflake = eux |

### Contrainte financière — à clarifier

- **Budget client annoncé :** 30 k€ HT pour l'engagement 1
- **Question majeure à poser à Sohoft :** les 30 k€ couvrent-ils **mon périmètre seul** ou **Globasoft + déploiement Snowflake Sohoft** ?
  - **Si 30 k€ = Globasoft seul** → 25,5 k€ net pour Globasoft, mission à l'équilibre. Sohoft chiffre sa partie Snowflake séparément (et prend sa commission ailleurs).
  - **Si 30 k€ = enveloppe totale E1** → il faut retrancher le déploiement Snowflake avant de savoir ce qui reste pour Globasoft. Très probablement pas tenable au périmètre complet.
- **Commission Sohoft :** 15% — à clarifier : sur quel montant exactement ? Part Globasoft ou total E1 ?

### Détail charge Globasoft (hors Snowflake)

| Lot                                 | Temps J/H |
| ----------------------------------- | --------: |
| Kickoff + ateliers cadrage          |         8 |
| Cartographie AS-IS (macro)          |      3,75 |
| Formalisation DAT                   |         4 |
| Intégration CISO                    |         9 |
| Arbitrage dbt Cloud vs in Snowflake |         3 |
| Cas d'usage MVP + grille chiffrage  |         6 |
| Cadre FinOps (doc + templates)      |         3 |
| Roadmap migration globale           |       1,8 |
| Présentations DG + CISO             |         6 |
| Pilotage projet                     |         8 |
| **TOTAL Globasoft**                 |    **53** |

**Hors périmètre Globasoft :**
- Déploiement Snowflake (étape 2) → Sohoft
- Développement technique des 2 cas d'usage MVP (étape 3) → à clarifier
- Déploiement FinOps technique dans Snowflake → probablement Sohoft

### Conditions à documenter dans la propale Globasoft

**⚠️ Ces gains élevés ne tiennent que si on scope proprement les lots suivants :**

1. **Cartographie à 75% = cartographie MACRO** (volumes, domaines, fréquences, criticité, classification des 37 jobs et 1200 tables). La **cartographie détaillée** (règles de transformation, logique métier de chaque job) bascule en engagement 2 au moment de traiter chaque cas d'usage.

2. **FinOps à 70% = livrable DOC + TEMPLATES** (conventions de tagging, définition des resource monitors, structure du dashboard, document de gouvernance des coûts). Le **déploiement technique** dans Snowflake est porté par Sohoft ou basculé en E2.

3. **Le déploiement Snowflake (étape 2) n'est PAS dans le chiffrage Globasoft.** Le DAT définit les spécifications, Sohoft déploie. À expliciter dans la propale et dans le contrat : "Le présent engagement porte sur la conception et la documentation. Le déploiement technique Snowflake fait l'objet d'un chiffrage distinct par Sohoft."

4. **Les Quick Wins Métiers (étape 3) — qui développe ?** À trancher avec Sohoft. Si Globasoft prend le dev des 2 cas d'usage : +15 à 30 j/h en engagement 2. Si Sohoft : chiffrage séparé.

Sans ces précisions, risque majeur de malentendu sur le périmètre et sur qui fait quoi.

---

## 3. Stratégie proposée (côté Globasoft)

### Posture générale
**Mission d'investissement commercial maîtrisé** pour rentrer chez le client et capter la vraie valeur sur la **phase 2 de réalisation** (mai 2026 → T1 2027, plusieurs centaines de k€ potentiels).

### Positionnement du périmètre Globasoft
Globasoft se positionne comme **cabinet de conseil / architecte data** sur les étapes 1, 4 et 5 de la démarche client :
- Étape 1 : Conception & validation du DAT (+ cartographie macro + CISO + arbitrage dbt + choix MVP)
- Étape 4 : Cadre FinOps (doc + templates)
- Étape 5 : Roadmap de migration

Sohoft se positionne comme **intégrateur technique Snowflake** sur l'étape 2 (et éventuellement étape 3 et déploiement technique étape 4).

### Option retenue : périmètre Globasoft à 30 k€ ferme
- **Engagement 1 Globasoft à 30 k€ ferme, ~53 j/h avec Claude** (100 j/h sans)
- Livrables Globasoft : DAT + arbitrage dbt + 2 cas d'usage MVP sélectionnés + grille de chiffrage pré-acceptée pour suite + Cadre FinOps (doc+templates) + Roadmap de migration
- **Conditions scope explicites dans la propale** (voir section 2)
- **TJM effectif ≈ 482 €/j** → mission à l'équilibre côté Globasoft
- **Engagement 2 Globasoft (chiffré après E1) :** accompagnement migration, cartographie détaillée des cas d'usage, éventuellement dev des Quick Wins si c'est nous qui les prenons — fourchette à préciser selon arbitrages

### Pourquoi cette logique
1. Respecte la demande de forfait à engagement de résultat
2. Livre les étapes 1, 4, 5 complètes attendues par le client
3. Sécurise le chiffrage de la suite sur des bases validées (DAT + CISO)
4. Différencie face aux concurrents (posture architecte + levier IA)
5. Permet de rentrer avec la contrainte budgétaire tout en étant à l'équilibre comptable
6. Évite d'empiéter sur le périmètre technique de Sohoft (bonne relation long terme)

---

## 3bis. Détail des ateliers de cadrage (8 j/h dans scénario complet, 6 j/h dans Mix)

**Objectif :** passer de "compris à distance" à "décisions tranchées et documentées". Sans ces ateliers, le DAT se fait retoquer = re-travaux à notre charge en forfait engagement de résultat.

### Les ateliers à planifier

1. **Kickoff et cadrage du cadrage (0,5 j)** — Ziyad, Florian, sponsors. Périmètre, livrables, planning, comitologie, contacts clés (CISO, CAGIP, métiers).

2. **Approfondissement existant & pain points (1 j)** — Florian principalement. Détail des 37 flux (criticité, bugs, conso), des 1200 tables (domaines, volumétries, fréquences), dépendances entre 4 DW, incidents récents. Sert à prioriser la cartographie.

3. **Architecture cible & arbitrages techniques (1 j)** — Ziyad + Florian + Pascal. Approfondir la slide AS-IS → TO-BE :
   - dbt Cloud vs dbt in Snowflake (leur question ouverte)
   - DLT managé vs self-hosted
   - Airflow : hébergement, lien services groupe
   - Orchestration bout-en-bout
   - Modélisation data (Kimball / Data Vault / médaillon)

4. **Exigences CISO et sécurité (1 j) — CRITIQUE** — CISO ou représentant + RSI CA Immobilier. Passer en revue chaque point de leur slide :
   - BIOK + Tri Secret Secure Encryption
   - Azure Key Vault + Snowflake
   - SSO Cerbère / ILEX CAGIP
   - Alimentation unilatérale depuis zone sécurisée (impact DLT)
   - Data masking PowerBI (Snowflake dynamic masking, row access policies)
   - Désensibilisation non-prod (méthode : masking, synthétisation, copies partielles)
   - Usercube + Graylog : points d'intégration
   - **Tout ce qui n'est pas tranché ici = risque à notre charge**

5. **Choix des cas d'usage MVP (0,5 j)** — Ziyad + représentants métiers. Sélection des 2 cas selon critères : valeur métier, complexité technique, représentativité des patterns à industrialiser. Équilibre entre quick win visible et démonstration de la méthode.

6. **FinOps et modèle de consommation (0,5 j)** — Ziyad + finance IT si possible. Granularité refacturation, enveloppes Snowflake contractées groupe, gouvernance des coûts, reporting type.

7. **Gouvernance data & articulation DMO (0,5 j)** — Data Management Office. Qui fait quoi : catalogue, lineage, ownership, qualité. Éviter les doublons Snowflake/dbt ↔ DMO.

8. **Présentation intermédiaire du DAT (0,5 j)** — À mi-parcours, pas en fin. Valider les grands choix avant rédaction V1 complète.

### Ce qui est inclus dans les j/h "ateliers"

Pour chaque atelier : préparation (le plus gros), animation, compte-rendu + formalisation des décisions, diffusion, relance sur points ouverts.

### Règle à appliquer

**Aucun chapitre du DAT ne se rédige avant que l'atelier correspondant ait eu lieu et que les décisions aient été validées par CR signé.**

### Planning calendaire

Les 8 j/h (ou 6 en scénario Mix) s'étalent sur **4 à 5 semaines** car les interlocuteurs côté client sont rarement tous dispo en même temps. À intégrer dans le rétroplanning global de 8 semaines.

---

## 4. Sujets à cadrer avec Sohoft

### Priorité critique (à clarifier absolument avant d'envoyer la propale)

1. **Les 30 k€ couvrent quoi exactement ?**
   - Option A : budget Globasoft seul, le déploiement Snowflake de Sohoft est chiffré et facturé en plus par Sohoft au client
   - Option B : enveloppe totale E1 à se partager entre Globasoft et Sohoft
   - **Réponse = structure complètement différente. À éclaircir en priorité.**

2. **Qui porte le développement des 2 cas d'usage MVP (étape 3) ?**
   - Si Globasoft : +15 à 30 j/h à chiffrer en engagement 2 au TJM normal
   - Si Sohoft : à chiffrer par eux
   - Si mixte : quel découpage ?

3. **Périmètre de la commission Sohoft 15%**
   - Sur quoi exactement ? Part Globasoft ? Enveloppe totale ?
   - **Négocier un modèle dégressif** : 15% sur E1, 10% sur E2, 5% sur phase 2
   - Ou base fixe au lieu d'un %
   - **Chaque point gagné = 300 € sur E1 + beaucoup plus sur la suite**

### Priorité haute

4. **Clarifier le budget 30 k€** — ferme ou indicatif ?
   - Si c'est un seuil de décision autonome (sans N+1), une proposition à 35-40 k€ avec périmètre plus complet peut passer
   - À faire remonter via Sohoft avant envoi propale

5. **Process sous-traitant Groupe CA** — Globasoft devra probablement être inscrit au contrat cadre Groupe (mention "Square Habitat nouveau sous-traitant" sur leur slide CISO)
   - Anticiper pour ne pas retarder le démarrage du 4 mai

6. **Cohérence de la propale conjointe**
   - Est-ce qu'on envoie UNE propale conjointe (Globasoft + Sohoft) ou DEUX propales distinctes ?
   - Qui signe quoi côté client ?
   - Qui est l'interlocuteur unique en face du client ?

### Priorité moyenne

7. **Accès au CISO** — pouvoir valider nos hypothèses tôt évite les re-travaux
8. **Qui sont les 2 autres concurrents ?** — pour affiner le positionnement
9. **Disponibilité Ziyad et son équipe** — impact sur le planning 8 semaines

---

## 5. Éléments de différenciation à mettre en avant

- Lecture fine du référentiel CISO groupe (les concurrents survoleront)
- Méthode d'alignement avec les services groupe : Cerbère/ILEX, Usercube, Azure Key Vault, Graylog, CAGIP
- Pattern "alimentation unilatérale" maîtrisé
- Stratégie désensibilisation non-prod + masking PowerBI
- Promesse d'arbitrage dbt Cloud vs in Snowflake dans le DAT (leur question ouverte)
- Utilisation d'IA pour accélérer la production du DAT (gain ~25% sans rogner sur la qualité)

---

## 6. Décisions à prendre sur ce point

- [ ] Valider la logique "mission d'investissement" avec acceptation d'une marge nulle/faible sur E1
- [ ] Mandat pour négocier la commission (objectif : dégressif ou 10%)
- [ ] Mandat pour sonder le budget (ferme vs indicatif)
- [ ] Qui envoie la propale, sous quel entête, à qui exactement
- [ ] Calendrier d'envoi (idéal : avant fin de semaine pour laisser le temps d'un échange avant le 4 mai)
- [ ] Qui enclenche le process sous-traitant Groupe CA

---

## Annexes

- Notes réunion complète : article Odoo Knowledge #154 (instance globasoft)
- Modèle de chiffrage : `Propale_CA_Immobilier_Chiffrage.xlsx` (variables pilotables)
- Slides client reçues : architecture AS-IS/TO-BE, recommandations CISO, démarche 5 étapes
