---
projet: Recrutement BizDev
titre: Brief — plusieurs entretiens par candidat (3 maximum)
type: brief-developpement
statut: a-realiser
version: 1.0
date_creation: 2026-09-19
perimetre: cockpit-globasoft — module Entretiens
source_verite: code applicatif (cockpit/views.py, cockpit/models.py) au commit 37ac8cf
depot: GitHub/daf-globasoft
tags: ["recrutement", "bizdev", "cockpit", "entretiens", "brief", "developpement"]
---

# Brief — plusieurs entretiens par candidat (3 maximum)

> Demande fonctionnelle pour le module Entretiens du cockpit. Rédigée depuis le
> code, avec les points d'intervention exacts. Voir [[Module Entretiens du cockpit]]
> pour la documentation du module existant.

## 1. Le besoin

Un recrutement se joue rarement en un seul entretien. Le cas concret qui déclenche
la demande : **Lucas Duger**, reçu le 26 août par deux collègues, puis revu le
22 septembre par le dirigeant avant décision. Deux tours, deux dates, deux
interlocuteurs — c'est un déroulé normal, pas une exception.

Aujourd'hui, poser le second rendez-vous **efface le premier**. On perd la date du
premier tour, sa durée, son format et son commentaire. Or c'est précisément sur les
candidats qui vont au bout que l'historique a de la valeur.

**Objectif : autoriser jusqu'à 3 entretiens par candidat et par poste.**

## 2. Ce que fait le code aujourd'hui

La règle « un entretien par candidat » est **purement applicative**. Il n'existe
aucune contrainte d'unicité en base — vérifié sur la base de production : la table
`cockpit_entretien` ne porte que sa clé primaire, la FK vers `auth_user` et le
`CHECK (duree_min >= 0)`. **Aucune migration n'est donc nécessaire pour lever la
règle.**

Elle tient en deux endroits :

| Fichier | Emplacement | Rôle |
|---|---|---|
| `cockpit/views.py` | `EntretiensView.post`, `Entretien.objects.update_or_create(applicant_id=…, job_id=…)` | **C'est ici que l'écrasement se produit.** Le couple candidat + poste sert de clé : reposer un rendez-vous met à jour l'existant au lieu d'en créer un. |
| `cockpit/views.py` | `EntretiensView.get`, `planifies = {e.applicant_id: e for e in Entretien.objects.filter(job_id=job_id).order_by('debut')}` | Dictionnaire indexé par candidat : même si plusieurs entretiens existaient, **seul le plus tardif** serait visible dans la liste, les autres écrasés silencieusement. |

Le calendrier, lui, est déjà prêt : il itère sur un queryset (`entretiens`), pas sur
le dictionnaire. Plusieurs étiquettes pour un même candidat s'afficheraient sans
modification.

Les actions `modifier` et `supprimer` ciblent déjà un `pk` précis : elles
fonctionneront telles quelles avec plusieurs entretiens.

## 3. Comportement attendu

1. **Créer n'écrase plus.** Poser un rendez-vous pour un candidat qui en a déjà un
   ajoute une ligne.
2. **Plafond à 3** par candidat et par poste. Le 4e est **refusé avec un message
   explicite** — jamais un écrasement silencieux, jamais une erreur 500.
3. **Modifier et supprimer** continuent de viser un entretien précis par son `pk`.
4. Chaque entretien reste **autonome** : sa date, sa durée, son format et son
   commentaire lui appartiennent.

## 4. Décisions fonctionnelles à trancher

Ces points ne sont pas tranchés, ils appellent un arbitrage avant codage.

**Le rang de l'entretien.** Faut-il afficher « 1er entretien », « 2e entretien » ?
*Recommandation : calculer le rang à la volée par ordre de date, ne pas le stocker.*
Un numéro stocké devient faux dès qu'on déplace une date, et l'ordre chronologique
est la seule définition qui reste vraie.

**Ce que montre la liste des candidats.** Elle affiche aujourd'hui une date unique.
*Recommandation : le prochain rendez-vous à venir, avec le nombre total en second
plan (« 22/09 14h · 2 entretiens »).* C'est l'action qui compte au quotidien ;
l'historique complet a sa place sur la fiche, pas dans la liste.

**L'indicateur d'écart.** Le code signale aujourd'hui les contradictions entre
l'étape Odoo et la présence d'une date (`ecart` = `sans_date` ou `a_avancer`).
*Recommandation : conserver la sémantique sur « au moins un entretien ».*

**Le plafond est-il dur ou souple ?** Un 4e tour reste concevable.
*Recommandation : constante de classe (`MAX_ENTRETIENS = 3`) plutôt qu'un 3 en dur,
pour qu'un changement d'avis ne demande pas de relire la logique.*

## 5. Ce qui ne change pas

- **La contrainte de créneau** : un entretien doit tenir entièrement dans une plage
  ouverte, vérifié côté serveur. Elle s'applique à chacun des 3.
- **La granularité de 30 minutes** et la grille lundi → vendredi, 8h → 20h.
- **Odoo reste en lecture seule.** Planifier ne fait toujours rien bouger dans Odoo.
- **Aucune notification** n'est envoyée au candidat.
- **Aucune détection de chevauchement** — choix assumé, inchangé.

## 6. Critères d'acceptation

- [ ] Poser un 2e puis un 3e entretien pour un même candidat crée bien 3 lignes, le 1er intact.
- [ ] Le calendrier affiche les 3 étiquettes, y compris sur des semaines différentes.
- [ ] Une 4e tentative est refusée avec un message nommant le plafond, sans rien écraser.
- [ ] Déplacer le 2e entretien ne touche ni le 1er ni le 3e.
- [ ] Supprimer le 1er laisse les deux autres en place.
- [ ] Une requête POST forgée à la main ne contourne ni le plafond ni la contrainte de créneau.
- [ ] Un candidat sans aucun entretien reste signalé comme aujourd'hui.

## 7. Hors périmètre

Notifications au candidat, écriture dans Odoo, détection de chevauchement, et le
cloisonnement des accès CV/photo — ce dernier point est un défaut connu, à traiter
séparément avant l'ouverture d'un second poste.

## Voir aussi

- [[Module Entretiens du cockpit]] — documentation du module existant
- [[Note de présélection]] — vivier et critères de classement
