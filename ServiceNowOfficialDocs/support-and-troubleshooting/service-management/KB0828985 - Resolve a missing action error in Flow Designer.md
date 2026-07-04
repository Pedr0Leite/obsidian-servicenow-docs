---
title: "Resolve a missing action error in Flow Designer"
aliases:
  - KB0828985
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0828985
kb_number: KB0828985
last_modified: 2025-08-11
---

## Resolve a missing action error in Flow Designer

  

### Issue

When trying to open an action in Flow Designer, you may see the error message "This action cannot be found." 

### Release

Any supported release

### Cause

This error occurs due to underlying database problems. A common cause is the use of restricted words in step parameters. To identify the problem:

1.  Go to the Step Extension Inputs table \[sys\_hub\_step\_ext\_input\].
2.  Sort by the Created or Updated columns.
3.  Use the **Model** field to find the specific action.

### Resolution

Look for values of 'Column Name', a common problem is using sys\_id, which is restricted and causes database issues. You can call it sysid but not sys\_id. If that's the case you need to remove the record.

1.  Look for values in the **Column Name** field.
2.  Check if any use the restricted word **sys\_id**, which causes database issues.
3.  Remove any records found that use **sys\_id**.

**Note**: You can use sysid (without the underscore) as an alternative to sys\_id.
