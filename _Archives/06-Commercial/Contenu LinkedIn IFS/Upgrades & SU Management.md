---
tags: ["linkedin", "contenu", "ifs", "upgrade"]
created: 2026-06-01
---

# Pilier — Upgrades & SU Management

**Pourquoi ça marche** : tout le monde galère sur les montées de version / Service Updates. Sujet evergreen, fort en commentaires.

## Brouillon de post (EN)
> **Most IFS Cloud upgrade pain isn't the upgrade — it's the dependency order nobody mapped.**
>
> Recurring traps:
> • Deployment order wrong → upgrade fails ("resource mapping not found")
> • Customizations from Apps 10 not uplifted → custom event logic breaks
> • Management servers under-sized for the new release
> • SU dependencies skipped (23R1 → 23R2 → …)
>
> Before your next upgrade:
> 1️⃣ Build the **dependency / deployment-order map** first `[à préciser]`
> 2️⃣ Convert custom event logic to **workflows** before uplift
> 3️⃣ Check the **sizing guide** for the target release
> 4️⃣ Dry-run in a clone, not in TEST
>
> What's burned you most in an IFS upgrade? 👇

## Fils sources (community.ifs.com)
- Order of deployment while installation in 25r2 — https://community.ifs.com/framework-experience-infrastructure-cloud-integration-dev-tools-50/order-of-deployment-while-installation-in-25r2-67218
- 26r1 upgrade error: resource mapping not found — https://community.ifs.com/upgrades-updates-81/26r1-upgrade-error-upgrade-failed-resource-mapping-not-found-for-name-67598
- Applying updates in IFS Cloud 23r1 to 23r2 and further — https://community.ifs.com/upgrades-updates-81/applying-updates-in-ifs-cloud-23r1-to-23r2-and-further-66551
- Uplifting IFS Apps 9 to Cloud: converting custom event logic to workflow — https://community.ifs.com/upgrades-updates-81/uplifting-ifsapp-9-to-ifs-cloud-converting-custom-event-logic-to-workflow-65451
- Upgrade Cloud latest from V10 with customizations — https://community.ifs.com/upgrades-updates-81/upgrade-cloud-latest-from-v10-with-customizations-65813
- 25r2 sizing guide — https://community.ifs.com/upgrades-updates-81/25r2-sizing-guide-63633
