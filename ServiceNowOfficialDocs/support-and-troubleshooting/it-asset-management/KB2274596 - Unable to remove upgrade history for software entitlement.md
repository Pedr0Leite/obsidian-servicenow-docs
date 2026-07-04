---
title: "Unable to remove upgrade history for software entitlement"
aliases:
  - KB2274596
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2274596
kb_number: KB2274596
last_modified: 2025-07-04
---

## Issue

For the related list under a software entitlement, we can see that it is not editable/removable entries. The option to delete the Upgrade History is present but greyed out.  
  
  

## Resolution

  
Entitlements that have related entitlements, upgrade history, entitlement history, or upgraded entitlements are not editable

https://docs.servicenow.com/bundle/tokyo-it-asset-management/page/product/software-asset-management2/task/track-software-rights.html   
  
Entitlements are typically not designed to be edited throughout the entitlement lifecycle.   
As new purchases are made, they should be logged as new entitlement records and not updates to existing records. As entitlements are created, their settings and relationships to other records (metric attributes, downgrades, next version, allocations, etc.) can be impacted if attributes are changed within the reconciliation. Therefore, many of the attributes are not editable  
  
Hence, we made the field greyed out. 

If there is a need to correct or update an entitlement:

1.  Delete the existing entitlement record (if appropriate).
2.  Import or manually create a new entitlement with the correct information.
