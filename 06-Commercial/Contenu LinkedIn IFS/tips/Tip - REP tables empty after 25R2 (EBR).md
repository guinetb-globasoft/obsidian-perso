---
tags: ["tipdujour", "ifs", "reporting"]
created: 2026-06-01
---

#tipdujour #ifs

## Post (EN)

**Pilier** : Reporting & Report Studio

💡 **IFS Cloud tip**

If you built reports or integrations that read straight from the `%_REP` result tables, a recent IFS Cloud change can break them **silently**.

To enable EBR (edition-based redefinition, for zero-downtime patching), IFS stopped writing report result sets to those RPT/REP tables. Your queries don't error — they just return nothing.

• Audit anything that reads from `%_REP` tables
• Re-point it to the projection / source data

A silent empty result is the worst kind of regression: no alert, just wrong numbers. Hunt these down *before* the upgrade, not after a user notices.

**Hashtags** : #IFS #IFSCloud #ERP #Reporting
**Source (1er commentaire)** : https://community.ifs.com/upgrades-updates-81/where-are-rep-reports-stored-in-25r2-66121
**À vérifier** : version/SU exacte du changement (25R2 SU2 ?) [à vérifier]

#IFS #IFSCloud #ERP #Reporting

---
**Source** : réponse d'Amila Samarasinghe — https://community.ifs.com/upgrades-updates-81/where-are-rep-reports-stored-in-25r2-66121
