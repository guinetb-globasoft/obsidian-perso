---
titre: Les deux cartographies produites
statut: livré (v1, à valider)
date: 2026-08-18
tags: [cartographie, livrable, artefact, pptx]
---

# Les deux vues produites — v1 du 18/08/2026

## Format retenu : artefact web, pas slide

**Arbitrage assumé.** La demande parlait de slides à intégrer dans le vMASTER. Deux vues
ont bien été générées au format PowerPoint (voir plus bas), mais le livrable principal est
un **artefact web interactif**. Raison :

- une slide fige **10 noms d'applications sur 150** ; la page les porte toutes les 150,
  filtrables, avec description / propriétaire / hébergement / statut ;
- une slide fige **24 flux sur 132** ; la page porte les 132, filtrables par statut,
  par Talend, par recherche libre ;
- le destinataire (consultants Deloitte / Delville en onboarding) a besoin de
  **chercher**, pas de regarder ;
- une slide se périme le jour où l'Excel bouge ; la page se **régénère** en relançant
  la chaîne.

### Deux pages, deux publics

| Page | Public | Contenu |
|---|---|---|
| **Version DSI / consultants** | Gildvin, Deloitte, Delville | Tout : les 2 vues, les chiffres, la qualité du référentiel, la réponse Archi |
| **Version collaborateurs** | Utilisateurs GA | Le plan des applications, la recherche, les échanges expliqués en langage courant |

🔗 **DSI / consultants** — https://claude.ai/code/artifact/07d37aed-c02b-4fad-a4b5-610586e0268a
🔗 **Collaborateurs** — https://claude.ai/code/artifact/350c32bf-c1ad-4221-a198-03b6fd692fb0
🔗 **Facture fournisseur de bout en bout** — https://claude.ai/code/artifact/f7ba288a-901c-49e4-9edc-db8142b57c8a

*(privées par défaut — à partager explicitement depuis le menu de chaque page)*

## La version collaborateurs

Dérivée des mêmes données, allégée pour un lecteur non-DSI :

- **conservé** : le plan des domaines fonctionnels, les 150 applications (recherche + filtre par
  métier), les échanges inter-applicatifs ;
- **retiré** : les chiffres du SI, le contrôle qualité du référentiel, la partie Archi — ce sont
  des sujets de DSI, pas d'utilisateur ;
- **traduit** : plus de codes `INT-xxx`, plus de mention Talend, plus de jargon de statut.
  Chaque échange est une phrase (« ESKER numérise les factures fournisseurs et les renvoie dans
  IFS avec leur bon à payer »), avec un simple marqueur *en place* / *en cours de mise en place* ;
- **nettoyé** : les noms de service sont normalisés à l'affichage (`INGENIERIE > ACHATS`
  → *Ingénierie › Achats*, `????` → *—*) sans toucher à la source ;
- **ajouté** : un renvoi vers le Service Support pour signaler une erreur ou un oubli — la page
  devient un canal de fiabilisation de l'inventaire.

Le point d'entrée est la **recherche** : la vraie question d'un collaborateur est
« quelle appli pour ça ? ». La recherche porte sur le nom, la description, le service et le
domaine, donc « facture », « chantier » ou « paie » ramènent les bonnes applications.

## Contenu de l'artefact

| Planche | Contenu |
|---|---|
| **01 — Vue fonctionnelle** | Le plan : bandeau *Pilotage* en haut, *Socle numérique* en bas, 10 domaines métier autour de l'ERP IFS au centre. Chaque domaine est cliquable → liste complète de ses applications. Recherche libre sur les 150 apps. |
| **02 — Les flux autour d'IFS** | Schéma hub & spoke : IFS au centre, 6 familles de flux Finance autour, sens + statut + marquage Talend. Puis le tableau des **132 flux vivants** du SI, filtrable. |
| **03 — Le SI en chiffres** | Applications par domaine, cycle de vie des 250 lignes de flux, applications les plus connectées. |
| **04 — Ce que vaut la donnée d'entrée** | Les 6 constats du contrôle qualité — voir [[01-Referentiel/01-Qualite-du-referentiel]]. |
| **05 — Et avec Archi ?** | Réponse argumentée + chemin en 4 étapes — voir [[04-Outillage/01-Faisabilite-Archi]]. |

### Parti pris graphique

Charte GA (magenta `#E6007E`, neutres froids type béton) dans une mise en page de
**jeu de planches de plans** : cartouche d'en-tête, filets fins, repères de planche et
données en chasse fixe. Cohérent avec le métier du groupe, et lisible en thème clair
comme sombre.

## La vue processus : la facture fournisseur de bout en bout

Troisième page, demandée le 18/08. Là où les deux premières répondent à « de quoi le SI
est-il fait » et « qui parle à qui », celle-ci répond à **« par où passe une facture »** —
c'est une lecture par le processus, pas par l'application.

Périmètre arbitré avec Benoît : **cycle fournisseur (P2P)**, entités **GA et Equilab**.

Sept étapes : engager la dépense · réceptionner · recevoir la facture · valider ·
comptabiliser · payer · rapprocher et informer. À chaque étape, les applications des deux
circuits (IFS pour GA, Infor Syteline pour Equilab) et **les interfaces réelles avec leur
cadence** lue dans les planifications Talend.

Ce que la vue fait ressortir, et que les deux autres ne montraient pas :

- **Le référentiel fournisseurs est toujours poussé de l'ERP vers ESKER**, jamais l'inverse.
  C'est une règle d'architecture implicite qui n'était écrite nulle part.
- **Les deux circuits convergent en deux points seulement** : ESKER pour la capture,
  IFS pour la comptabilisation. Tout le reste est parallèle.
- **La boucle de retour INT-259** (statut du paiement vers ESKER) est ce qui permet au
  comptable et au fournisseur de savoir si une facture est payée sans ouvrir l'ERP.
  Elle est active, et c'est l'un des trois flux actifs **sans tâche Talend identifiée**
  — sauf si l'hypothèse INT-234 se confirme.
- **L'ancienne chaîne tourne encore** : six interfaces `ZyScan → PROGIDOC → Compta` sont au
  statut « actif, à disparaître ». Deux circuits de facture fournisseur coexistent selon
  les entités — c'est signalé en encadré sur la page.

À faire si besoin : le pendant **cycle client (O2C)**, de la facturation IFS à l'e-invoicing
et à l'encaissement.

## Le livrable PowerPoint (secondaire)

Deux slides ont malgré tout été générées, pour le cas où le support vMASTER doit rester
le véhicule officiel :

`~\Downloads\Présentation du SI vMASTER - cartos.pptx` — **copie** du vMASTER, l'original
n'est pas touché (conformément à la règle de la slide 14 du support).

- **position 8** — *Cartographie fonctionnelle du SI* (après la slide « Les principales
  applications et leurs interlocuteurs »)
- **position 14** — *Cartographie applicative — les flux Finance* (après la slide
  « Trésorerie, Paie & Notes de frais »)

Charte respectée : magenta `E6007E`, Calibri, cartes `F7F7F7` / bordures `E4E4E4`,
mêmes conventions que les slides 7, 9 et 12.

## Chiffres publiés (recalculés, pas repris)

| Indicateur | Valeur | Remarque |
|---|---:|---|
| Applications | **150** | cohérent avec l'onglet STATS |
| Domaines fonctionnels | **12** | + le cœur ERP |
| Lignes de flux | 250 | ≠ interfaces : une interface = plusieurs lignes |
| Flux **vivants** | **132** | actifs + à venir + en construction + à prévoir + à disparaître |
| Flux **actifs** | **61** | = le chiffre « ≈60 » de la slide 6 |
| Flux impliquant IFS | **37** | IFS est le hub n°1 du SI |
| Flux orchestrés par Talend | 12 | colonne « Géré avec Talend » renseignée |

> ⚠️ **Point à trancher avec Gildvin** : la slide 6 du vMASTER annonce « ≈60 flux ».
> C'est la photo d'aujourd'hui (61 actifs). La trajectoire, elle, en compte **132**.
> Communiquer 61 sous-estime ce que le projet ERP est en train de construire.

## Régénération

Chaîne dans `scratchpad/` (à rapatrier dans un dépôt si le format est retenu) :

```
extract.py      INVENTAIRE.xlsx      -> referentiel.json
domaines.py     taxonomie + affectation des 150 apps (échoue si une app n'est pas classée)
payload.py      referentiel + domaines -> payload.json
build_artefact.py  artefact_tpl.html + payload.json -> cartographie-si-ga.html   (version DSI)
                   simple_tpl.html  + payload.json -> applications-groupe-ga.html (version collaborateurs)
gen_cartos.py   referentiel + domaines -> les 2 slides PPTX
qa.py           contrôle qualité du référentiel
archi_scan.py / archi_diff.py / archi_match.py   écart avec le modèle Archi
```

## Reste à faire

- [ ] Valider la taxonomie des 12 domaines avec Gildvin
- [ ] Trancher le chiffre communiqué : 61 (photo) ou 132 (trajectoire)
- [ ] Décider du véhicule : artefact web, slides, ou les deux
- [ ] Croiser les flux déclarés avec le **repo Talend** `ga-talend` (interfaces réellement
      implémentées) et les docs de flux de `DSI - TMA Globasoft - Général` → écart
      déclaratif / réel, non fait à ce stade
