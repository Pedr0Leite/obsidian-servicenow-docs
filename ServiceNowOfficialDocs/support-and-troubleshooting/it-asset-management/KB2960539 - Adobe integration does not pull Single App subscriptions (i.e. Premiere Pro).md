---
title: "Adobe integration does not pull Single App subscriptions (i.e. Premiere Pro)"
aliases:
  - KB2960539
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2960539
kb_number: KB2960539
last_modified: 2026-04-15
---

## Adobe integration does not pull Single App subscriptions (i.e. Premiere Pro)

  

### Issue

The Adobe Creative Cloud integration profile successfully imports most Adobe product subscriptions into the `samp_sw_subscription` table, but subscriptions for certain Single App products (such as Adobe Premiere Pro) are not imported, even when users have valid assignments in the Adobe Admin Console.

### Symptoms

-   Records in `samp_sw_subscription` are created for Adobe products like Photoshop, Illustrator, Dreamweaver, and InDesign, but not for Adobe Premiere Pro (or other affected Single App products)
-   Affected users have confirmed active Premiere Pro assignments in the Adobe Admin Console
-   The scheduled integration job completes without errors
-   The issue is isolated to specific Single App product subscriptions, not the overall integration
-   The `assigned_software_identifier` field is empty for the missing subscription records

### Facts

-   The Adobe integration relies on software identifier mappings in the ServiceNow content library to match Adobe API responses to discovery models (DMAPs)
-   Adobe Single App products return a `singleApp: true` flag in the API payload, along with a `groupName` such as `"Single App - Edition 4 - Premiere Pro"`
-   If the corresponding identifier (e.g., `ADOBESINGLEAPP_Premiere`) is absent from the content library, no `samp_sw_subscription` record is created for that product
-   Example API response for an unmatched product:

json

`{   "groupId": 882882474,   "groupName": "Single App - Edition 4 - Premiere Pro: default configuration",   "type": "PRODUCT_PROFILE",   "productName": "Premiere (ETLA,Single App - Edition 4,...)",   "singleApp": true }`

-   A fix allowing unidentified identifiers to be created automatically (even without content) was delivered in DEF0771551, included in the Australia (true-up) release

### Release

-   Workaround (content request): All supported versions
-   Permanent fix (DEF0771551 — unidentified identifier creation): Available in the Australia release (true-up) and later

### Cause

The missing subscription records are caused by the absence of the Single App product identifier in the ServiceNow content library. In this case, the identifier `ADOBESINGLEAPP_Premiere` was not mapped to the discovery model `DMAP0298670` (Adobe Systems Premiere Pro Edition 4). Without this mapping, the integration cannot match the Adobe API response to a software model, and no subscription record is written to `samp_sw_subscription`.

### Resolution

Option 1 — Content Request (all versions): Submit a content task to the Asset Management Content Services team requesting the addition of the missing Single App identifier to the content library. Provide the Adobe API response payload as reference. Once the content update is shipped and downloaded, re-run the integration scheduled job. The subscription records should be created on the next execution.  
  
For the Premiere Pro case specifically, the identifier `ADOBESINGLEAPP_Premiere` should be mapped to DMAP `DMAP0298670` (Adobe Systems Premiere Pro Edition 4). Note that `ADOBESINGLEAPP_Premiere Pro` already maps to `DMAP0005323` and should not be confused with the above.

  
Option 2 — Self-service via Australia release (DEF0771551): If the instance is on the Australia release (true-up) or later, administrators can manually create unidentified software identifiers directly in the instance without waiting for a content update. Once added, the next integration job run will resolve the subscription and auto-update the assigned software model.
