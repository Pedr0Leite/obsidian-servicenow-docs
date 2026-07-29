---
title: "SAM - Clarification on OOB Adobe Creative Cloud Reclamation Rule logic for Low Usage candidates "
aliases:
  - KB2662174
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2662174
kb_number: KB2662174
last_modified: 2025-12-10
---

## SAM - Clarification on OOB Adobe Creative Cloud Reclamation Rule logic for Low Usage candidates

  

### Issue

-   The OOB Adobe reclamation rule appears to flag some subscriptions as Low Usage based on the Last Activity field, even though the Last Activity values are blank as expected due to the Adobe connector not bringing in this information.
-   The case involves validating how the rule determines Low Usage candidates when usage metering data is not available.
-    The reclamation candidates are of type subscription Software, auto-created via the Adobe Cloud Integration profile, and are around 3 months old.
-   The scheduled job 'SAM - Optimize Adobe Subscriptions' creates these reclamation candidates.

### Release

NA

### Cause

  
1\. The Last Activity field is blank because Adobe integration does not capture desktop usage in the samp\_sw\_usage table, and third-party integrations like SCCM are required for this data.

2\. The reclamation rule uses custom logic to compare subscription creation dates with the reclamation rule threshold, even when 'Include no activity' is unchecked, leading to flagging subscriptions as Low Usage based on date-based inactivity logic.  
  

### Resolution

  
1\. Understand that Adobe Hybrid Subscription optimization works by comparing the subscription creation date and the reclamation rule threshold to determine inactivity, as Adobe does not provide API-based usage data.

2\. Note that the 'Include no activity' flag on the Reclamation rule controls RC creation irrespective of Usage.

3\. Refer to the documentation for Publisher optimizations for Adobe for details on use cases and logic: https://www.servicenow.com/docs/bundle/zurich-it-asset-management/page/product/software-asset-management2/reference/pub-opt-adobe.html
