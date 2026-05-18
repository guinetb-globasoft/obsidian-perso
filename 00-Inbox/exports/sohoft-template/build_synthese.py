"""Génère la version courte (synthèse) du markdown propale.

Sections extraites selon le brief :
- ch. 3.1 Contexte + 3.3 Vision cible + 3.4 Enjeux clés
- ch. 4.1 Périmètre + 4.3.1 Snowflake + 4.5 Cas d'usage MVP + 4.8 Livrables (titres + finalités)
- ch. 6.1.1 Vue d'ensemble du planning
- ch. 7 Engagements (complet)
- ch. 9 Hypothèses (synthèse 1 page = titres H2 + points clés)
- ch. 10 Proposition financière (complet)
- ch. 11 Conditions contractuelles (complet)

Note : ch. 1 (Synthèse) et ch. 2 (Qui est SoHoft) sont absents du markdown source
(référencés dans le sommaire uniquement).
"""
from pathlib import Path
import re

SRC = Path(r'C:/Users/Shadow/Documents/vault-prive/00-Inbox/Propale Sohoft - CA Immobilier - Engagement 1.md')
OUT = Path(r'C:/Users/Shadow/Documents/vault-prive/00-Inbox/exports/_propale_synthese.md')

lines = SRC.read_text(encoding='utf-8').splitlines()

def slice_lines(start_1based, end_1based_exclusive):
    """Retourne les lignes [start..end_exclusive-1] (1-based)."""
    return lines[start_1based - 1 : end_1based_exclusive - 1]

PB = '\n<div style="page-break-after: always;"></div>\n'

parts = []

# --- Front matter + page de garde Synthese ---
parts.append('''---
tags: ["commercial", "CA-Immobilier", "propale", "sohoft", "synthese"]
created: 2026-04-23
---

# Proposition technique et financière — Synthèse

**SoHoft x Crédit Agricole Immobilier**

**Socle Modern Data Stack sur Snowflake — Phase 1**

Date : 22/04/2026

*Document synthétique destiné aux sponsors (CDO, Direction Générale).*
*Le dossier technique détaillé est remis séparément.*
''')
parts.append(PB)

# --- Sommaire synthese ---
parts.append('''# Sommaire

1. Compréhension du besoin (contexte, vision cible, enjeux clés)
2. Proposition technique (périmètre, architecture Snowflake, cas d'usage MVP, livrables)
3. Planning macro
4. Engagements SoHoft
5. Hypothèses structurantes
6. Proposition financière
7. Conditions contractuelles
''')
parts.append(PB)

# --- 1. Comprehension du besoin : 3.1 + 3.3 + 3.4 ---
parts.append('# 1. Compréhension du besoin\n')
parts.append(PB)

# 3.1 Contexte (89-106)
parts.append('\n'.join(slice_lines(89, 107)))
parts.append(PB)

# 3.3 Vision cible (131-166)
parts.append('\n'.join(slice_lines(131, 167)))
parts.append(PB)

# 3.4 Enjeux clés (167-184)
parts.append('\n'.join(slice_lines(167, 185)))
parts.append(PB)

# --- 2. Proposition technique ---
parts.append('# 2. Proposition technique\n')
parts.append(PB)

# 4.1 Périmètre (207-250)
parts.append('\n'.join(slice_lines(207, 251)))
parts.append(PB)

# 4.3.1 Snowflake (293-315)
parts.append('\n'.join(slice_lines(293, 316)))
parts.append(PB)

# 4.5 Cas d'usage MVP (398-439)
parts.append('\n'.join(slice_lines(398, 440)))
parts.append(PB)

# 4.8 Livrables : on garde intro + les H3 avec juste la ligne "Finalité"
synth_48 = ['## 2.4 Livrables du Périmètre 1', '']
synth_48.append("À l'issue du Périmètre 1, SoHoft remet six livrables structurants. Chaque livrable a une finalité opérationnelle et un destinataire identifié. Le détail complet (contenu, destinataires, formats) figure dans le dossier technique.\n")
# 4.8.1 -> ligne 502, 4.8.2 -> 530, 4.8.3 -> 566, 4.8.4 -> 588, 4.8.5 -> 610, 4.8.6 -> 632
livrables = [
    (502, 504, 'DAT — Document d\'Architecture Technique'),
    (530, 532, 'Grille de chiffrage de migration'),
    (566, 568, 'Cartographie macro de l\'existant'),
    (588, 590, 'Cadre FinOps'),
    (610, 612, 'Roadmap de migration globale'),
    (632, 634, 'Supports de présentation'),
]
for title_ln, finalite_ln, label in livrables:
    finalite_text = lines[finalite_ln - 1]  # ligne 1-based "Finalité :"
    synth_48.append(f'### {label}')
    synth_48.append('')
    synth_48.append(finalite_text)
    synth_48.append('')
parts.append('\n'.join(synth_48))
parts.append(PB)

# --- 3. Planning macro ---
parts.append('# 3. Planning macro\n')
parts.append(PB)
# 6.1.1 Vue d'ensemble (835-842)
planning = slice_lines(835, 843)
# retransformer le titre H3 en H2 pour la hiérarchie synthese
planning_text = '\n'.join(planning).replace('### 6.1.1 Vue d\'ensemble', '## Vue d\'ensemble (3 périmètres, 18 semaines)')
parts.append(planning_text)
parts.append(PB)

# --- 4. Engagements ---
parts.append('# 4. Engagements SoHoft\n')
parts.append(PB)
# 7 Engagements (968-1027) — on saute le titre de chapitre initial pour éviter doublon
engagements = slice_lines(969, 1028)  # skip line "# 7. Engagements SoHoft" (968)
parts.append('\n'.join(engagements))
parts.append(PB)

# --- 5. Hypothèses (synthese 1 page) ---
parts.append('''# 5. Hypothèses structurantes

Les engagements fermes de SoHoft reposent sur un ensemble d'hypothèses explicites. Toute hypothèse significativement invalidée en cours de mission donne lieu à un avenant documenté avant impact sur les livrables ou le planning.

## Système d'information existant

➜ Volumétrie conforme : 37 flux Talend + SSIS, 1200 tables, SQL Server (90%) + Oracle.
➜ Documentation des flux legacy disponible au moins pour les 2 cas d'usage MVP.
➜ Stabilité du paysage applicatif pendant la durée de la mission.

## Référentiel CISO et services Groupe

➜ Recommandations CISO stables pendant la mission.
➜ Services Groupe opérationnels : Snowflake (contrat cadre actif), Private Link AWS, SSO Cerbère/ILEX, Azure Key Vault, Usercube, Graylog.
➜ Inscription SoHoft au contrat cadre Groupe effective dans les 2 semaines suivant la signature.

## Déploiement Snowflake (Périmètre 2)

➜ Compte Snowflake mis à disposition avant démarrage du P2.
➜ Intégrations Groupe transverses (Private Link, SSO, Key Vault…) portées par CAGIP/RSI.
➜ Modèle RBAC arrêté dans le DAT, sans ré-arbitrage en phase de déploiement.

## Cas d'usage MVP (Périmètre 3)

➜ Périmètres Natio et NPM Altaix stables (scope arrêté dans le DAT).
➜ Règles de gestion Java Natio de complexité standard, transposables en SQL dbt / Python DLT.
➜ Données sources de qualité exploitable (pas de reprise massive ni de déduplication complexe).

## Disponibilité des parties prenantes

➜ Disponibilités formalisées en section 5.4 effectivement tenues.
➜ Réponse des interlocuteurs transverses (CAGIP, RSI) sous 3 jours ouvrés.

## Contractuel

➜ Signature au plus tard le 30 avril 2026 pour un démarrage au 4 mai 2026.
➜ Process d'achat Groupe non-bloquant sur le démarrage.

## Invalidation d'une hypothèse

Notification immédiate en COPIL ➜ analyse d'impact ➜ avenant ➜ pas d'arrêt de la mission en dehors des lots directement impactés.
''')
parts.append(PB)

# --- 6. Proposition financière (complet) ---
parts.append('# 6. Proposition financière\n')
parts.append(PB)
# 10 (1197-1374) — skip le titre chapitre initial "# 10. Proposition financière"
finance = slice_lines(1198, 1375)
parts.append('\n'.join(finance))
parts.append(PB)

# --- 7. Conditions contractuelles ---
parts.append('# 7. Conditions contractuelles\n')
parts.append(PB)
# 11 (1375-1432)
contract = slice_lines(1376, 1433)
parts.append('\n'.join(contract))

# --- Assembly ---
final = '\n'.join(parts)

# Rétrograder les # / ## / ### des sections extraites pour cohérence
# Les sections extraites gardent leur niveau original ("## 3.1", "### 4.1.1") ce qui est OK
# car on remet un # de niveau 1 au-dessus dans l'architecture de la synthèse.
# Mais on peut renormaliser en dégradant chaque niveau d'une marche pour aplatir.
# Pour simplifier : on ne renormalise pas, on garde la hiérarchie d'origine.

OUT.write_text(final, encoding='utf-8')
print(f'OK: {OUT}')
print(f'Taille: {OUT.stat().st_size:,} bytes')
print(f'Lignes: {final.count(chr(10)) + 1}')
# Compter les H1
h1 = len(re.findall(r'^# [^#]', final, re.MULTILINE))
h2 = len(re.findall(r'^## [^#]', final, re.MULTILINE))
h3 = len(re.findall(r'^### [^#]', final, re.MULTILINE))
print(f'H1: {h1}, H2: {h2}, H3: {h3}')
