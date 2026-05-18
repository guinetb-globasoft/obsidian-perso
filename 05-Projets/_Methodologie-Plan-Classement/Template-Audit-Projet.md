---
tags: ["methodologie", "plan-classement", "template", "audit"]
created: 2026-05-17
---

---
type: audit-plan-classement
projet: 
auditeur: 
date-audit: 
version-plan-audite: 
statut: brouillon
---

# Audit du plan de classement — {{Nom du projet}}

> Template d'audit appuyé sur la méthodologie [[00-Index|Méthodologie d'évaluation des plans de classement]].
> Dupliquer ce fichier dans le dossier du projet audité avant remplissage.

## Contexte de l'audit

| Élément | Description |
|---|---|
| **Projet audité** | |
| **Périmètre** | (Tout le projet / une phase / un sous-domaine) |
| **Plan évalué** | (Lien vers le plan ou capture de la structure) |
| **Volumétrie** | (Nb de dossiers, nb de documents, espace disque) |
| **Outils** | (SharePoint, Drive, GED, système de fichiers...) |
| **Acteurs interrogés** | (Liste des personnes consultées) |
| **Date de l'audit** | |
| **Auditeur** | |

## Plan de classement actuel (synthèse)

> Coller ici l'arborescence actuelle ou un extrait représentatif.

```
01-XXX/
  01.01-YYY/
  01.02-ZZZ/
02-AAA/
...
```

---

## Évaluation par angle

### 1. Logique structurante → [[01-Logique-structurante]]

**Note : __ / 3**

**Constat**
- Sur quoi repose la structure ?
- Logique fonctionnelle / organigramme / types ?

**Points forts**
- 

**Points faibles**
- 

**Recommandations**
- 

---

### 2. Profondeur et hiérarchie → [[02-Profondeur-hierarchie]]

**Note : __ / 3**

**Constat**
- Nombre de niveaux observés : 
- Largeur moyenne par niveau : 
- Branches obèses / creuses : 

**Points forts**
- 

**Points faibles**
- 

**Recommandations**
- 

---

### 3. Exhaustivité et exclusivité (MECE) → [[03-Exhaustivite-exclusivite]]

**Note : __ / 3**

**Constat**
- Présence d'un dossier "Divers" ? 
- Guide de classement existant ? 
- Test de classement sur 10 docs : taux de placement non ambigu = __ %

**Points forts**
- 

**Points faibles**
- 

**Recommandations**
- 

---

### 4. Calendrier de conservation et sort final → [[04-Calendrier-conservation-DUA]]

**Note : __ / 3**

**Constat**
- Existence d'un calendrier de conservation ? 
- Couverture (% catégories ayant une DUA) : __ %
- Sorts finaux définis ? 
- Procédures de purge en place ? 

**Points forts**
- 

**Points faibles**
- 

**Recommandations**
- 

---

### 5. Stabilité et évolutivité → [[05-Stabilite-evolutivite]]

**Note : __ / 3**

**Constat**
- Règle de codification documentée ? 
- Marges de numérotation ? 
- Procédure d'évolution ? 
- Propriétaire du plan identifié ? 

**Points forts**
- 

**Points faibles**
- 

**Recommandations**
- 

---

### 6. Métadonnées → [[06-Metadonnees]]

**Note : __ / 3**

**Constat**
- Niveau de maturité (0 à 4) : 
- Métadonnées obligatoires définies ? 
- Vocabulaire contrôlé ? 
- Métadonnées requêtables ? 

**Points forts**
- 

**Points faibles**
- 

**Recommandations**
- 

---

### 7. Adéquation aux usages → [[07-Adequation-usages]]

**Note : __ / 3**

**Constat**
- Test de recherche : temps moyen = __ min
- Test de classement : temps moyen = __ sec
- Taux de docs au bon endroit (audit aléatoire) : __ %
- Volume "Inbox" / non classé : __ %
- Existence de chemins parallèles (Teams, mails, drives perso) ? 

**Points forts**
- 

**Points faibles**
- 

**Recommandations**
- 

---

### 8. Conformité réglementaire → [[08-Conformite-reglementaire]]

**Note : __ / 3**

**Constat**
- Cartographie réglementaire formalisée ? 
- Données personnelles tracées (RGPD) ? 
- DPO impliqué ? 
- Niveaux de confidentialité définis ? 
- Procédure de réponse aux demandes (CNIL, audit) ? 

**Points forts**
- 

**Points faibles**
- 

**Recommandations**
- 

---

### 9. Livrabilité et clôture projet → [[09-Livrabilite-cloture-projet]]

**Note : __ / 3**

**Constat**
- Distinction structurelle livrable / interne ? (sous-dossier `_livrable/`, branche dédiée…)
- Attribut frontmatter `livrable_client` ou équivalent ?
- Existence d'un **index livrable global** maintenu à jour ?
- Test de livraison : temps pour préparer la livraison aujourd'hui = __
- Script ou procédure automatisée de livraison ?
- Livrables par phase clairement identifiés ?
- Historique des livraisons réalisées ?

**Points forts**
- 

**Points faibles**
- 

**Recommandations**
- 

---

### 10. Complétude structurelle → [[10-Completude-structurelle]]

**Note : __ / 3**

**Checklist obligatoires** (les 7 doivent être présents)
- [ ] Dossier de gouvernance documentaire
- [ ] Décisions d'architecture (ADR)
- [ ] Changelog projet
- [ ] Glossaire métier
- [ ] Dossier d'archives / annexes
- [ ] README / Vue d'ensemble
- [ ] Cartographie d'architecture

**Checklist conditionnels** (cocher uniquement si la condition s'applique)
- [ ] Calendrier de conservation *(si soumis à obligations réglementaires)*
- [ ] Cartographie RGPD *(si données personnelles)*
- [ ] Index des livrables *(si livraisons structurantes)*
- [ ] Runbook / Guide d'exploitation *(si projet en production)*

**Constat**
- Nombre d'obligatoires manquants : __ / 7
- Nombre de conditionnels applicables manquants : __ / __
- Scoring : 3 si tous présents (obligatoires + conditionnels applicables) · 2 si obligatoires OK mais conditionnels manquent · 1 si 1-2 obligatoires manquent · 0 si 3+ obligatoires manquent

**Points forts**
- 

**Points faibles**
- 

**Recommandations**
- 

---

## Synthèse globale

### Scoring final

| Angle | Score | Constat | Action corrective |
|-------|-------|---------|-------------------|
| 1. Logique structurante | __ / 3 | | |
| 2. Profondeur | __ / 3 | | |
| 3. Exhaustivité/exclusivité | __ / 3 | | |
| 4. DUA / sort final | __ / 3 | | |
| 5. Stabilité/évolutivité | __ / 3 | | |
| 6. Métadonnées | __ / 3 | | |
| 7. Adéquation usages | __ / 3 | | |
| 8. Conformité | __ / 3 | | |
| 9. Livrabilité / clôture | __ / 3 | | |
| 10. Complétude structurelle | __ / 3 | | |
| **TOTAL** | **__ / 30** | | |

### Interprétation du score

- **25-30** : Plan exemplaire — maintenir et améliorer en continu
- **19-24** : Plan solide avec axes d'amélioration identifiés
- **13-18** : Plan fonctionnel mais fragile — plan d'action prioritaire à construire
- **6-12** : Plan dégradé — refonte partielle nécessaire
- **0-5** : Plan défaillant — refonte complète à envisager

### Top 3 des forces

1. 
2. 
3. 

### Top 3 des risques

1. 
2. 
3. 

## Plan d'action

| # | Action | Angle | Priorité | Responsable | Échéance | Statut |
|---|---|---|---|---|---|---|
| 1 | | | (Haute/Moyenne/Basse) | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |

## Prochaine revue

- **Date prévue** : 
- **Périmètre** : (Re-audit complet / suivi du plan d'action / audit ciblé)
- **Critères de succès** : 

---

## Annexes

### Documents consultés
- 

### Personnes interrogées
- 

### Échantillon de documents testés
- 

---

*Audit réalisé selon la méthodologie [[00-Index]] · Référence normes : [[11-Normes-references]] · Vocabulaire : [[12-Glossaire]]*
