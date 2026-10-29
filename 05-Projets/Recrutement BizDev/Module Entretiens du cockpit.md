---
projet: Recrutement BizDev
titre: Module Entretiens — cockpit Globasoft
type: documentation-fonctionnelle
statut: a-valider
version: 1.0
date_creation: 2026-09-13
perimetre: cockpit-globasoft — application Django interne (Render)
source_verite: code applicatif (cockpit/views.py, cockpit/models.py) au commit 197409e
confidentialite: interne — décrit un dispositif traitant des données de candidats
tags: ["recrutement", "bizdev", "cockpit", "entretiens", "documentation", "odoo"]
---

# Module Entretiens — cockpit Globasoft

> **Deuxième phase du parcours de recrutement du cockpit.** Elle prend le relais de la
> présélection : une fois les candidats retenus, ce module sert à poser les rendez-vous.
> Documentation rédigée depuis le code, pas depuis l'intention.

## 1. Objectif

Transformer une liste de candidats retenus en rendez-vous datés, **sans quitter le cockpit
et sans écrire dans Odoo**.

Le problème résolu est concret : à l'issue de la présélection, six candidats se retrouvent à
l'étape « Entretien à planifier » dans Odoo, et rien n'indique quand les voir. Odoo sait
*qui* est à cette étape mais ne porte aucune disponibilité ; le calendrier personnel sait
*quand* on est libre mais ignore les candidats. Le module fait tenir les deux dans un même
écran.

Une contrainte a guidé toute la conception : **le cockpit ne modifie jamais Odoo**. Odoo
reste la source de vérité des candidatures ; tout ce que produit le module vit dans la base
du cockpit.

## 2. Carte d'identité

| | |
|---|---|
| **Adresse** | `/rh/entretiens/` — menu **RH ▸ 📅 Entretiens** |
| **Accès** | groupes `Dirigeants` ou `Recrutement` (ou superuser) |
| **Condition d'ouverture** | le poste doit avoir atteint l'étape « Entretien à planifier » |
| **Lecture Odoo** | `hr.applicant`, `hr.recruitment.stage` — en lecture seule, cache 10 min |
| **Écriture** | base du cockpit uniquement : `Entretien`, `CreneauDisponible` |
| **Poste par défaut** | `hr.job` 3 — Business Developer BtoB (alternance) |

## 3. Les deux notions du module

Tout le module repose sur deux objets qu'il ne faut pas confondre.

### Créneau disponible

Une plage horaire pendant laquelle des entretiens **peuvent** être posés — par exemple
*mercredi 26 août, 14 h → 18 h*.

C'est une **contrainte, pas une indication**. Hors de ces plages, la grille du calendrier
n'est pas cliquable, et le serveur refuse l'enregistrement même si la requête est forgée à
la main. Un entretien qui déborderait de la fin du créneau est rejeté : sur une plage
14 h–18 h, un rendez-vous d'une heure passe à 17 h 00 mais pas à 17 h 30.

| Champ | Rôle |
|---|---|
| `job_id` | poste concerné — un créneau n'est pas global |
| `date`, `heure_debut`, `heure_fin` | la plage |
| `commentaire` | libellé libre |

Unicité garantie sur le triplet poste + date + heure de début.

### Entretien

Un rendez-vous réellement posé avec un candidat.

| Champ | Rôle |
|---|---|
| `applicant_id`, `job_id` | rattachement à la candidature Odoo |
| `nom` | dénormalisé, pour rester lisible si la candidature disparaît d'Odoo |
| `debut`, `duree_min` | **1 heure par défaut**, modifiable de 15 à 240 min |
| `mode` | visio · sur site · téléphone |
| `commentaire` | lien visio, salle, intervenants |
| `cree_par` | qui a posé le rendez-vous |

> **Un entretien est un fait, pas une opinion.** C'est pourquoi il est partagé par toute
> l'équipe, contrairement aux likes et favoris de la présélection (`AvisCandidat`) qui sont
> personnels à chaque recruteur.

## 4. Ce que contient la page

De haut en bas :

**Le fil du parcours** — Présélection ✓ › Entretiens. Une phase franchie reste consultable,
une phase jamais atteinte s'affiche verrouillée.

**Le calendrier**, façon agenda hebdomadaire : lundi → vendredi, 8 h → 20 h, par tranches de
30 minutes. Les plages ouvertes apparaissent en bande verte, les étiquettes candidats se
placent dessus, colorées selon le format (bleu visio, violet sur site, vert téléphone). Les
étiquettes sont **positionnées côté serveur** : le calendrier reste juste même sans
JavaScript.

Par défaut, seules les **semaines utiles** sont affichées — celles qui portent une
disponibilité à venir ou un entretien déjà posé. Ce second critère évite qu'un rendez-vous
devienne invisible si l'on retire le créneau correspondant. Un bouton « Voir toutes les
semaines » rebascule sur une fenêtre glissante de trois semaines : c'est le seul moyen
d'atteindre une semaine sans créneau pour en ouvrir un.

**Les créneaux ouverts**, en puces vertes cliquables qui amènent le calendrier sur la semaine
concernée, avec un formulaire pour en ouvrir ou en retirer.

**La liste des candidats** à l'étape « Entretien à planifier » : photo, école, accès direct à
la fiche et au CV, et le rendez-vous affiché en vert une fois posé.

## 5. Le verrou de phase

Le module n'est accessible que si le recrutement a réellement atteint l'étape
« Entretien à planifier ». Sinon la page répond **403** avec un message indiquant l'étape
attendue et l'étape courante.

Le point subtil est la façon dont l'étape atteinte est calculée : elle se déduit de
**l'historique réel** des candidatures (`duration_tracking` d'Odoo conserve chaque étape
traversée, même quittée depuis), et non de leur position actuelle. Un candidat passé en
entretien puis refusé compte quand même comme une étape franchie — sans cela, la page se
refermerait derrière le recruteur au premier refus.

L'étape « Refusé » est exclue du calcul : elle porte la séquence la plus haute du pipeline
Odoo, mais ce n'est pas un avancement du recrutement.

## 6. Qui écrit quoi

| Donnée | Origine | Le cockpit peut-il l'écrire ? |
|---|---|---|
| Candidatures, étapes, CV, photos | Odoo | **Non** — lecture seule |
| Étape atteinte par le poste | Odoo (calculée) | Non |
| Créneaux de disponibilité | Cockpit | Oui |
| Entretiens planifiés | Cockpit | Oui |
| Likes / favoris / notes | Cockpit (par recruteur) | Oui |

> ⚠️ **Conséquence à connaître.** Planifier un entretien ne fait rien bouger dans Odoo : le
> candidat y reste à l'étape « Entretien à planifier ». Le déplacement d'étape reste un geste
> manuel dans Odoo.

## 7. Règles appliquées

| Règle | Détail |
|---|---|
| Durée par défaut | 1 heure, définie au seul endroit qui fait foi (le modèle) |
| Créneau obligatoire | un entretien doit tenir **entièrement** dans une plage ouverte |
| Vérification | faite côté serveur, pas seulement dans l'interface |
| Un entretien par candidat | et par poste — reposer un rendez-vous remplace le précédent |
| Granularité | 30 minutes |
| Semaines affichées | celles avec disponibilité à venir ou entretien posé |
| Cache Odoo | 10 minutes, bouton ↻ pour forcer la relecture |

## 8. Mode d'emploi

1. **Ouvrir un créneau** — formulaire sous le calendrier : date, heure de début, heure de fin.
2. **Poser un entretien** — cliquer une case verte du calendrier, ou le bouton *Planifier*
   d'un candidat de la liste. Choisir le candidat, la durée et le format.
3. **Déplacer ou annuler** — cliquer l'étiquette dans le calendrier.

## 9. Sous le capot

| Élément | Emplacement |
|---|---|
| Vue | `cockpit/views.py` → `EntretiensView` |
| Contrôle d'accès | `cockpit/views.py` → `RecrutementMixin` |
| Modèles | `cockpit/models.py` → `Entretien`, `CreneauDisponible` |
| Logique de parcours | `cockpit/odoo_engine.py` → `ETAPES_PARCOURS`, `etat_parcours`, `phase_ouverte` |
| Gabarits | `entretiens.html`, `_parcours.html`, `phase_verrouillee.html` |
| Migrations | `0012` Entretien · `0013` CreneauDisponible · `0014` créneaux initiaux · `0015` durée 1 h |

## 10. Limites connues

Ces points sont des choix ou des manques assumés, à connaître avant d'étendre le module.

| Limite | Portée |
|---|---|
| **Aucune détection de chevauchement** | deux entretiens peuvent se superposer dans une même plage — volontaire, un double rendez-vous peut être voulu |
| **Un seul entretien par candidat** | pas de second tour sans lever la contrainte |
| **Aucune notification** | le candidat n'est pas prévenu, aucun e-mail ni invitation calendrier n'est envoyé |
| **Odoo non mis à jour** | l'étape du candidat ne bouge pas après planification |
| **Cache non partagé** | le cache 10 min est propre à chaque processus ; avec plusieurs workers, une relecture peut survenir plus souvent qu'attendu |
| **CV et photos non cloisonnés** 🚩 | les adresses `/rh/recrutement/cv/<id>/` et `/photo/<id>/` ne vérifient pas que la candidature relève d'un poste autorisé — sans effet aujourd'hui (un seul poste ouvert), à corriger avant d'en ouvrir un second |
| **Pas d'accès en consultation seule** | tout titulaire du groupe `Recrutement` peut planifier, annuler et ouvrir des créneaux |

## 11. État au 13 septembre 2026

Le module est déployé et fonctionnel, mais **inutilisé depuis sa mise en place** :

- 6 candidats à l'étape « Entretien à planifier » depuis le 12 août ;
- 2 créneaux ouverts (26 août, 2 septembre), **tous deux passés sans entretien posé** ;
- 11 candidatures jamais triées en présélection.

> La donnée ci-dessus provient de la base locale pour les créneaux et entretiens ; la base de
> production (PostgreSQL sur Render) est distincte et peut différer.

## Voir aussi

- [[Note de présélection]] — critères de classement et vivier des 42 candidatures
- [[_Methodologie-Plan-Classement/00-Index|Méthodologie des plans de classement]] — grille d'évaluation appliquée à cette note
