---
tags: ["tipdujour", "ifs", "reporting"]
created: 2026-06-01
---

#tipdujour #ifs

## Post (EN)
**Pilier** : Reporting & Report Studio

💡 **IFS Cloud tip**

Setting up an IAL (Information Access Layer) view and unsure which **Data Retrieval** mode to pick? It's a freshness-vs-load trade-off, not a default to ignore:

• **Use Live Data** → nothing stored; queries the source at runtime. Always current, but heavier on the database.
• **Copy All Data** → stores a full copy, reloaded each run (manual or scheduled). Lighter live load, but only as fresh as the last refresh.

Rule of thumb: **Live** for small, freshness-critical queries; **Copy** for heavy analytical sets you can refresh on a schedule. Match the mode to how live the data truly needs to be — the wrong choice shows up later as either a slow database or stale dashboards.

**Hashtags** : #IFS #IFSCloud #ERP #Reporting
**Source (1er commentaire)** : https://community.ifs.com/framework-experience-infrastructure-cloud-integration-dev-tools-50/ial-data-retrieval-settings-67352
**À vérifier** : néant
