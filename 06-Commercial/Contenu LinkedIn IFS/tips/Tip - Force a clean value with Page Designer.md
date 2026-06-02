---
tags: ["tipdujour", "ifs", "page-designer"]
created: 2026-06-01
---

#tipdujour #ifs

## Post (EN)

**Pilier** : Custom Fields & Workflow (data quality)

💡 **IFS Cloud tip**

Want a field to always carry the right value — and make a wrong one impossible? Stop policing it with LOV filters and design the mistake out instead.

• Make the field **non-editable** in Page Designer
• Let its **default value** populate it (current user, site, company…)
• If no valid default exists, the record simply can't be saved — the problem surfaces immediately, not three steps downstream

This flips data quality from "trust every user every time" to "the screen can't produce a bad record." That's the kind of guardrail worth building in by design rather than catching in a report later.

**Hashtags** : #IFS #IFSCloud #ERP #DataQuality
**Source (1er commentaire)** : https://community.ifs.com/framework-experience-infrastructure-cloud-integration-dev-tools-50/adding-lov-filter-ifs-page-designer-67430
**À vérifier** : néant

#IFS #IFSCloud #ERP

---
**Tip tiré de** : best answer de @AbdulHi — *« Easiest way is to make the Requisitioner field non-editable using Page Designer. The default value will be the current user id if defined as a Requisitioner, otherwise null and the system will not allow to save the record »*
**Source** : https://community.ifs.com/framework-experience-infrastructure-cloud-integration-dev-tools-50/adding-lov-filter-ifs-page-designer-67430
