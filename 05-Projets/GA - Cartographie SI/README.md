---
projet: Cartographie du SI Groupe GA
statut: en-cours
date_creation: 2026-08-18
demandeur: Gildvin HIÉLARD (DDSI)
tags: [cartographie, urbanisation, archimate, archi, togaf, si, ga, readme]
---

# Cartographie du SI Groupe GA

> **Porte d'entrée du projet.** Commande de Gildvin HIÉLARD du 18/08/2026.

## Demande

Compléter le support `Présentation du SI vMASTER.pptx` (dossier Downloads) avec **deux
cartographies applicatives** — les représentations existantes n'étant « ni à jour ni
abouties visuellement » :

| # | Strate | Contenu demandé |
|---|---|---|
| 1 | **Fonctionnelle** | Applications par domaine fonctionnel / type d'activité métier, **ERP IFS au centre**, applications satellites regroupées autour |
| 2 | **Applicative** | Applications **et interfaces** (flux inter-applicatifs), ERP au centre. Focus **Finance** si le tout n'est pas lisible |

Question ouverte posée par Gildvin : **« Possible avec Archi ? »** → voir
[[04-Outillage/01-Faisabilite-Archi]].

Hors périmètre : la strate infrastructure (à voir avec Etienne GARINET).

### Destinataire final

Maëlle COUVREUX (DAF) → remplaçants temporaires de Victor (Deloitte, Delville), sous NDA.
Cible : **onboarding Finance/AF**, pas un public d'architectes. Le rendu doit être lisible
par un non-informaticien.

## Sources de vérité

| Source | Rôle | Emplacement |
|---|---|---|
| `INVENTAIRE - Applicatifs Métier.xlsx` | **Référentiel maître** : 150 apps, 250 lignes de flux | Teams > GA Service Informatique > Applicatifs Métiers |
| `Présentation du SI vMASTER.pptx` | Support à compléter (15 slides) | Downloads + Teams |
| `Synoptique des APPS par domaine fonctionnel.pptx` | Carto fonctionnelle **précédente** (celle à refaire) | Downloads |
| `Plan d'urbanisation POP - Pres.pptx`, `Slide urba.pptx` | Matériau d'urba antérieur | Downloads |
| `C:\Users\guinet\OneDrive\Togaf` | Référentiel méthodo (TOGAF 9.2, ArchiMate 3.1, viewpoints, ArchiSurance) | OneDrive perso |

## Plan de classement

| Dossier | Fonction | Contenu |
|---|---|---|
| `00-Gouvernance/` | Méta-doc | Changelog, décisions d'architecture |
| `01-Referentiel/` | **Fiabiliser** la donnée source | Contrôle qualité de l'inventaire, écarts à corriger |
| `02-Taxonomie/` | **Structurer** le sens | Domaines fonctionnels et affectation des 150 apps |
| `03-Cartographies/` | **Représenter** | Spécification des deux vues produites |
| `04-Outillage/` | **Industrialiser** | Faisabilité Archi, chaîne de génération |
| `05-Briefs/` | **Déléguer** | Les briefs donnés aux autres agents, et ce qu'ils ont renvoyé |

## Par où commencer

1. [[01-Referentiel/01-Qualite-du-referentiel]] — ce que vaut la donnée d'entrée (**à lire avant tout**)
2. [[02-Taxonomie/01-Domaines-fonctionnels]] — les 12 domaines retenus et pourquoi
3. [[03-Cartographies/01-Les-deux-vues-produites]] / [[03-Cartographies/01-Les-deux-vues-produites]]
4. [[04-Outillage/01-Faisabilite-Archi]] — réponse à la question de Gildvin
5. [[05-Briefs/README]] — les briefs donnés aux autres agents et leurs retours
6. [[00-Gouvernance/01-Changelog]] — le fil des avancées
