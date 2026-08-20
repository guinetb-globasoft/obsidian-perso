---
titre: Briefs — index
tags: [briefs, index]
---

# Briefs donnés à d'autres agents

Chaque note de ce dossier contient **un brief prêt à copier**, délimité par les repères
⬇️ / ⬆️. Le texte hors repères est le contexte pour nous, pas pour l'agent.

| # | Brief | Destinataire | Statut | Résultat |
|---|---|---|---|---|
| 01 | [[05-Briefs/01-IA-Talend-releve-PROD]] | IA connectée à Talend | ✅ exécuté le 18/08 | 31 tâches PROD relevées → `01-Referentiel/Talend-PROD-inventaire.csv` |
| 02 | [[05-Briefs/02-Claude-Excel-FLUX-phases-1-et-2]] | Claude Excel | ✅ exécuté le 18/08 | Phase 1 : 29 valeurs sur 26 lignes. Phase 2 : colonnes `Tâche Talend` (K) et `Dernière vérif. Statut` (P) |
| 03 | [[05-Briefs/03-Claude-Excel-correctifs]] | Claude Excel | ⏳ à exécuter | 43 cellules : protocole métier + date des commentaires |

## Ce qui fait qu'un brief passe bien

Retours d'expérience des trois premiers — à reprendre pour les suivants.

**Donner la valeur actuelle attendue, pas seulement la valeur cible.** C'est le garde-fou le
plus utile : l'agent ne peut pas écraser le travail de quelqu'un passé entre-temps, et une
divergence remonte au lieu de disparaître.

**Faire repérer les colonnes par leur libellé d'en-tête**, en donnant les lettres comme valeurs
à confirmer. Le classeur a des en-têtes sur plusieurs niveaux et une colonne dont le libellé est
resté à `Achats` — se fier aux positions aurait mal tourné. Ça a payé en phase 2 : les deux
insertions ont décalé toutes les lettres suivantes.

**Exiger `INCONNU` plutôt qu'une supposition.** Sur le brief Talend, c'est ce qui a fait
remonter les limites réelles de l'API (comptages tronqués à 600) au lieu de chiffres flatteurs
et faux.

**Demander explicitement ce qui n'a PAS été fait.** La liste des lignes non modifiées et
pourquoi est l'information la plus précieuse du compte rendu.

**Ne pas transmettre un extrait en le présentant comme le tout.** Sur le brief 01, je n'avais
envoyé que les 37 flux IFS ; l'agent en a conclu que 9 codes étaient « absents du référentiel »
alors qu'ils y figuraient tous. L'erreur était la mienne : il faut dire ce que l'extrait couvre
et ce qu'il ne couvre pas.

**Recouper le retour avant de l'appliquer.** Deux conclusions du brief 01 étaient à corriger,
et le compte rendu du brief 02 a relevé une erreur d'arithmétique dans mon propre en-tête
(26 lignes distinctes et non 28). Ça marche dans les deux sens.
