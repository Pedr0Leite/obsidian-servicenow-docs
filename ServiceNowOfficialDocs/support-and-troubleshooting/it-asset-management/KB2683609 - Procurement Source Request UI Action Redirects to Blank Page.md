---
title: "Procurement Source Request UI Action Redirects to Blank Page"
aliases:
  - KB2683609
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2683609
kb_number: KB2683609
last_modified: 2025-12-29
---

## Issue

When users click the Source Request UI Action on SCTASK records generated from the _Hardware Inventory Stock Order_ catalog item, the system redirects to a broken page.

Error from system logs:

`Cannot read property "ASSET_FUNCTION" from undefined`

## Resolution

We can try any of the following steps as a workaround

1\. Repair or Upgrade the Hardware Asset Management Plugin

-   Navigate to System Definition > Plugins.
-   Locate Hardware Asset Management.
-   Perform a Repair or upgrade the plugin to the latest available version.
-   This action restores corrupted out-of-the-box script includes, including `HAMConstants`.

2\. Restore the Out-of-the-Box HAMConstants Script Include (If Needed)

-   If the issue persists after plugin repair or upgrade, import from the OOTB instance

Verify that the HAMConstants script include has required constants, including `ASSET_FUNCTION`.
