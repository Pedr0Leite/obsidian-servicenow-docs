---
title: "Lookup Select Box variable is read-only in Submit Catalog Item Request flow action"
aliases:
  - KB0962980
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0962980
kb_number: KB0962980
last_modified: 2025-08-01
---

## Lookup Select Box variable is read-only in Submit Catalog Item Request flow action

  

### Issue

When using the Submit Catalog Item Request flow action, a catalog item with a Lookup Select Box variable appears unavailable (read-only) and cannot be modified.

**Steps to reproduce**

1.  Create a catalog item with a Lookup Select Box variable.
2.  Create a flow with the **Submit Catalog Item Request** action.
3.  In the flow, select the catalog item you created in step 1.

  
Unexpected behavior: The Lookup Select Box variable is read-only and cannot be configured.   
Expected behavior: The Lookup Select Box variable should be configurable. 

### Release

### Resolution

The Lookup Select Box variable type is not supported in the Submit Catalog Item Request flow action. To request this functionality, submit an enhancement request through the Idea Portal in the ServiceNow Community.
