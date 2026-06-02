---
tags: ["tipdujour", "ifs", "data-migration"]
created: 2026-06-01
---

#tipdujour #ifs

## Post (EN)

**Pilier** : Data Migration (data quality)

💡 **IFS Cloud tip**

A migration trap that bites once and then refuses to be fixed: importing sales-rule combination values via DMM.

• The combination value ID is assigned on the **first** import and then sticks
• Re-running with corrections won't reassign it
• You must migrate a **fresh, not-yet-loaded** set, in the **correct order**, the first time

The lesson generalizes well beyond this screen: in data migration, **load order and idempotency aren't details** — they decide whether a re-run heals the data or scars it. Precisely the kind of risk worth catching with automated guardrails.

**Hashtags** : #IFS #IFSCloud #ERP #DataMigration
**Source (1er commentaire)** : https://community.ifs.com/data-migration-333/how-to-import-combination-values-for-sales-rule-combination-using-dmm-65065
**À vérifier** : néant

#IFS #IFSCloud #ERP #DataMigration

---
**Source** : best answer de Tien Huynh — https://community.ifs.com/data-migration-333/how-to-import-combination-values-for-sales-rule-combination-using-dmm-65065
