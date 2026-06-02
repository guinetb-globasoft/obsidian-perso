---
tags: ["tipdujour", "ifs", "data-migration"]
created: 2026-06-01
---

#tipdujour #ifs

## Post (EN)

**Pilier** : Data Migration

💡 **IFS Cloud tip**

Scheduling an IFS Cloud migration that loads an external file? It won't all run as one scheduled job.

• "**Migrate source data**" schedules normally
• "**Create table from file**" must first **fetch the file** (e.g. pull it from FTP) before it can run

Split the chain: automate the retrieval step, then the migration step. Treating a two-stage data load as a single scheduled job is exactly why teams hit the dreaded "it ran successfully but imported nothing." Sequence beats hope.

**Hashtags** : #IFS #IFSCloud #ERP #DataMigration
**Source (1er commentaire)** : https://community.ifs.com/data-migration-333/ifs-cloud-migration-job-by-schedule-65442
**À vérifier** : néant

#IFS #IFSCloud #ERP #DataMigration

---
**Source** : réponse de Fikret — https://community.ifs.com/data-migration-333/ifs-cloud-migration-job-by-schedule-65442
