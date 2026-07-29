---
title: "IBM license rights show incorrect consumption values after clone or connection removal"
aliases:
  - KB3006962
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3006962
kb_number: KB3006962
last_modified: 2026-05-07
---

## IBM license rights show incorrect consumption values after clone or connection removal

  

### Issue

IBM license rights display incorrect consumption values on the IBM entitlements page.

### Release

Not release specific

### Cause

This issue may occur if the ILMT Product Usage table (`ilmt_v2_product_usage`) contains invalid or corrupted entries.  
For example, usage records may exist even though the associated ILMT connection is missing or has been removed — a situation that can occur after instance clone.

The default business rule "Remove Product Usage For the Connection" is designed to clean up records in the `ilmt_v2_product_usage`, `ilmt_v2_product_usage_server`, and `ilmt_v2_discovered_computer` tables when a connection is set to inactive or deleted.  
If this cleanup did not run or was interrupted, orphaned records may remain and cause incorrect rights calculations.

### Resolution

Remove the invalid records from the affected tables to correct the rights consumption calculation.

1.  Navigate to the mentioned tables using the application navigator \[`ilmt_v2_product_usage,``ilmt_v2_product_usage_server,``ilmt_v2_discovered_computer`\].
2.  Identify records that reference an ILMT connection that no longer exists or is set to inactive.
3.  Delete the orphaned records from those tables which should correct the rights consumption calculation.
