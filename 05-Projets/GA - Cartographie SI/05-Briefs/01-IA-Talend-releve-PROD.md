---
titre: Brief pour l'IA connectée à Talend — vérité terrain PROD
statut: à envoyer
date: 2026-08-18
tags: [talend, tmc, referentiel, verification, brief]
---

# Brief à passer à l'IA connectée à Talend

> **Pourquoi** : l'inventaire déclare que **12 flux sur 37** impliquant IFS passent par Talend.
> Gildvin affirme que **toutes** les interfaces IFS passent par Talend. L'un des deux est faux,
> et c'est l'inventaire qui fait foi dans la cartographie diffusée. Il faut trancher sur du réel.
>
> Le texte ci-dessous est à copier tel quel dans l'IA connectée à Talend.

---

## ⬇️ À COPIER À PARTIR D'ICI ⬇️

Tu as accès à notre plateforme Talend (Talend Management Console + les projets/jobs).
J'ai besoin de la **vérité terrain sur ce qui tourne réellement en PRODUCTION**, pour corriger
un référentiel d'interfaces qui est déclaratif et probablement faux.

### Règles impératives

1. **Ne devine pas.** Si une information n'est pas disponible, écris `INCONNU`. Une case vide ou
   une supposition me coûte plus cher qu'un `INCONNU` assumé.
2. **Distingue « déployé » de « qui tourne ».** Une tâche peut exister, être planifiée, et n'avoir
   jamais été exécutée. Ce sont trois états différents, je veux les trois.
3. **Précise systématiquement l'environnement.** Ne mélange pas PROD, QUAL et DEV.
   Si un même flux existe dans plusieurs environnements, une ligne par environnement.
4. **Fenêtre d'observation : les 90 derniers jours.** Si tu ne peux pas remonter aussi loin,
   dis-le et donne la fenêtre réellement couverte.
5. Ne modifie rien. Lecture seule.

### Ce que je veux — 1. L'inventaire réel des tâches

Pour **chaque tâche / plan d'exécution de l'environnement PRODUCTION**, sans filtrer, sans
échantillonner (dis-moi le nombre total trouvé avant de lister) :

| Champ | Précision attendue |
|---|---|
| `tache` | nom exact de la tâche dans TMC |
| `projet` | projet / workspace / espace de travail |
| `artefact` | nom du job ou du artefact déployé, + version |
| `environnement` | PROD / QUAL / DEV |
| `moteur` | Remote Engine ou Cloud Engine utilisé |
| `planifiee` | OUI / NON |
| `type_declenchement` | cron / événement / webhook / manuel |
| `cron` | l'expression exacte, telle qu'elle est configurée |
| `fuseau` | fuseau horaire de la planification |
| `derniere_exec` | date et heure de la dernière exécution |
| `statut_derniere_exec` | succès / échec / annulé / jamais exécuté |
| `nb_exec_90j` | nombre total d'exécutions sur 90 jours |
| `nb_ok_90j` | dont en succès |
| `nb_ko_90j` | dont en échec |
| `duree_moy` | durée moyenne d'exécution |

### Ce que je veux — 2. Ce que chaque tâche fait réellement

Toujours par tâche, en te basant sur les **connexions, ressources et paramètres réellement
configurés** (pas sur le nom de la tâche) :

| Champ | Précision attendue |
|---|---|
| `source` | l'application ou le système d'où viennent les données |
| `cible` | l'application ou le système où elles vont |
| `protocole` | SFTP / REST / SOAP / base de données / fichier partagé / mail |
| `ressource` | le détail concret : chemin SFTP, URL d'endpoint, nom de base, nom de fichier |
| `donnees` | l'objet métier transporté, en une ligne (« factures fournisseurs », « OD de paie »…) |
| `code_int` | le code `INT-xxx` correspondant si le nom ou la documentation le porte, sinon `INCONNU` |

### Ce que je veux — 3. Les écarts, qui sont le vrai sujet

Réponds explicitement à ces cinq questions, avec les preuves :

1. **Quelles tâches PROD ne correspondent à aucun code `INT-xxx` ?**
   Ce sont des interfaces qui tournent sans être référencées.
2. **Quelles tâches sont planifiées mais n'ont jamais tourné sur 90 jours ?**
   Ce sont des interfaces mortes qui polluent le référentiel.
3. **Quelles tâches échouent systématiquement ou majoritairement** (taux d'échec > 20 %) ?
   Donne le message d'erreur de la dernière exécution en échec.
4. **Y a-t-il des interfaces impliquant IFS qui ne passent PAS par Talend ?**
   (SFTP direct, intégration native IFS, connecteur applicatif, saisie manuelle…)
   C'est la question la plus importante du brief : je cherche à confirmer ou à démentir
   l'affirmation « toutes les interfaces IFS passent par Talend ».
5. **Une même tâche sert-elle plusieurs flux fonctionnels** (ou l'inverse : un flux
   fonctionnel est-il découpé en plusieurs tâches) ? La correspondance code ↔ tâche
   n'est probablement pas 1 pour 1, et j'ai besoin de connaître la vraie cardinalité.

### Ce que je veux — 4. La confrontation ligne à ligne

Voici les **37 flux vivants impliquant IFS** tels que notre inventaire les déclare aujourd'hui.
Pour chacun, dis-moi : **existe en PROD ? / passe par Talend ? / tourne réellement ?**
et signale toute divergence avec la colonne « Statut déclaré ».

| Code | Source | Cible | Statut déclaré | Talend déclaré | Objet |
|---|---|---|---|---|---|
| INT-002-IFS-Etafi/yourcegid | IFS | Etafi/yourcegid | A prévoir | - | ? |
| INT-003-IFS-ViaReport | IFS | ViaReport | A prévoir | - | ? |
| INT-140-ProjetCommercial-IFS | ProjetCommercial | IFS | Actif | - | Informations chantiers |
| INT-185-IFS-ESKER | IFS | ESKER | Actif | OUI | Fournisseur / Vendor |
| INT-187-188-ESKER-IFS | ESKER | IFS | Actif | OUI | BAP |
| INT-189-ESKER-IFS | ESKER | IFS | Actif | OUI | Liste des factures en attente de paiement |
| INT-191-Excel-IFS | Excel | IFS | A venir | - | Import de fichier Excel |
| INT-193-Expensya-IFS | Expensya | IFS | A venir | OUI | ecritures ndf |
| INT-194-Factory-IFS | Factory | IFS | A venir | - | ecriture vente + lien pdf (zylab) |
| INT-195-Hercule-IFS | Hercule | IFS | A venir | - | Ecritures stock |
| INT-196-ICS Compta-IFS | ICS Compta | IFS | A venir | - | Balance appel de fond |
| INT-199-IFS-Sage Signature | IFS | Sage Signature | A venir | - | virement |
| INT-202-IFS-Infor Syteline (CSI) | IFS | Infor Syteline (CSI) | A venir | - | référentiels à mettre àjour |
| INT-207-Inside Studio-IFS | Inside Studio | IFS | A venir | - | Import de fichier Excel |
| INT-209-Nibelis-IFS | Nibelis | IFS | A venir | OUI | Ecriture od de paie |
| INT-211-DevisNomenclatures-IFS | DevisNomenclatures | IFS | A venir | - |  |
| INT-212-PaieGRH-IFS | PaieGRH | IFS | A venir | OUI | Od de paie analytique |
| INT-213-PaieGRH-IFS | PaieGRH | IFS | A venir | OUI | Od de paie analytique |
| INT-217-Exfiles-IFS | Exfiles | IFS | Actif | OUI | Import des écritures bancaire |
| INT-222-Infor Syteline (CSI)-IFS | Infor Syteline (CSI) | IFS | A venir | OUI | Ecritures comptables des factures et avoir fournisseur (Jour |
| INT-223-Infor Syteline (CSI)-IFS | Infor Syteline (CSI) | IFS | A venir | OUI | Ecritures comptables des Factures Non Parvenues et des Extou |
| INT-224-Infor Syteline (CSI)-IFS | Infor Syteline (CSI) | IFS | A venir | - | PDF & XML Factures fournisseurs (exploitation du lien Esker  |
| INT-225-Infor Syteline (CSI)-IFS | Infor Syteline (CSI) | IFS | A venir | - | Ecritures comptables des factures de vente (Journal de vente |
| INT-226-Infor Syteline (CSI)-IFS | Infor Syteline (CSI) | IFS | A venir | - | Acompte frs |
| INT-227-Infor Syteline (CSI)-IFS | Infor Syteline (CSI) | IFS | A venir | - | Ecritures comptables Produits Constatés d’Avance (PCA) |
| INT-228-Infor Syteline (CSI)-IFS | Infor Syteline (CSI) | IFS | A venir | - | PDF & XML Factures clients (ou exploitation du lien Esker ?) |
| INT-229-Infor Syteline (CSI)-IFS | Infor Syteline (CSI) | IFS | A venir | - | Prix de revient des articles |
| INT-230-IFS-Infor Syteline (CSI) | IFS | Infor Syteline (CSI) | A venir | - | Estimations finalisées & révisions |
| INT-231-IFS-Infor Syteline (CSI) | IFS | Infor Syteline (CSI) | A venir | - | Validation du devis par le client |
| INT-232-IFS-ESKER | IFS | ESKER | A venir | OUI | Accusé réception facture |
| INT-233-IFS-ESKER | IFS | ESKER | Actif | OUI | Infos bancaires fournisseurs / Bank detail |
| INT-254-ESKER-IFS | ESKER | IFS | A venir | - | Factures Fournisseurs (yc écritures comptables + liens vers  |
| INT-259-IFS-ESKER | IFS | ESKER | Actif | - | Statut du paiement |
| INT-260-Sage XRT Trésorerie-IFS | Sage XRT Trésorerie | IFS | A venir | - | Relevés bancaires |
| INT-268-IFS-Sage XRT Trésorerie | IFS | Sage XRT Trésorerie | A venir | - | export prevision chèsque de ifs vers sagex treso |
| INT-275-IFS-QDV | IFS | QDV | Actif | - | Articles |
| INT-276-IFS-QDV | IFS | QDV | Actif | - | Prix des articles |

### Format de réponse

Deux blocs, dans cet ordre :

1. **Une synthèse en 10 lignes maximum** : combien de tâches en PROD, combien réconciliées avec
   un code INT, combien d'orphelines, combien de mortes, et la réponse franche à la question 4.
2. **Un CSV** (séparateur `;`, en-tête inclus, encodage UTF-8) reprenant toutes les colonnes des
   sections 1 et 2, une ligne par tâche. Ce fichier sera réinjecté dans notre référentiel, donc
   pas de commentaire à l'intérieur du CSV, pas de cellule fusionnée, pas de mise en forme.

Si tu ne peux pas répondre à une section faute d'accès, dis-le en une phrase au début plutôt
que de produire une réponse partielle sans le signaler.

## ⬆️ À COPIER JUSQU'ICI ⬆️

---

## Ce que j'en ferai au retour

| Réponse obtenue | Action sur le référentiel |
|---|---|
| Colonne « Géré avec Talend » réelle | Correction des 25 flux IFS aujourd'hui non marqués Talend |
| `protocole` + `ressource` + `cron` | Remplissage des colonnes techniques (aujourd'hui 26/132, 19/132) |
| Tâches orphelines sans code INT | Création des flux manquants dans l'onglet FLUX |
| Tâches mortes | Passage en « Décommissionné » — nettoie les 70 lignes sans statut |
| Cardinalité tâche ↔ flux | Arbitrage du compteur : « 61 flux » compte des lignes, pas des interfaces |
| Réponse à la question 4 | Détermine si le schéma de la carto doit faire apparaître Talend comme pivot |

**Conséquence probable sur les deux artefacts** : si l'affirmation se confirme, Talend cesse
d'être un badge discret sur quelques flux pour devenir un **nœud central du schéma**, entre IFS
et ses satellites. Ce serait une correction importante de la vue applicative — et un argument
de plus pour inventorier Talend comme application à part entière
(voir [[01-Referentiel/01-Qualite-du-referentiel]], constat n°3).

## Annexe — le tableau à coller

Généré depuis l'inventaire : `scratchpad/flux_ifs.md` (37 lignes).
