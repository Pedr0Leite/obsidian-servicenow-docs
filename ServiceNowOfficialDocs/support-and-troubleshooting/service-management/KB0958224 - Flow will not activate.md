---
title: "Flow will not activate"
aliases:
  - KB0958224
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0958224
kb_number: KB0958224
last_modified: 2024-02-28
---

## Flow will not activate

  

### Issue

-   When trying to Activate flow or save it provides an internal server error.
-   Also, sometimes it will say Activation success but it still will not activate.  
    

### Release

Paris Patch 5

### Cause

Check if the flow contains Send Email Action with data pills. If then, 

-   This is a bug on the platform. PRB1420275 is raised for this issue - [https://support.servicenow.com/problem.do?sysparm\_query=number=PRB1420275](https://support.servicenow.com/problem.do?sysparm_query=number=PRB1420275)
-   The issue is with the Send Email action present on the flow.
-   If the email HTML body contains a table with data pills while publishing/activating the flow, an internal server error will be seen.
-   The fix for this PRB is to delete the "Send Email" actions within the Flow and recreate them manually. \[Please take a screenshot before deleting for reference purpose, if required\]
-   Unfortunately, there will not be a more robust solution until beyond the Quebec Patch 1 release.
-   For testing purposes, You can make a copy of the flow, delete the Send Email action, and try to activate the flow. The flow should get activated

### Resolution

-   Delete the "Send Email" actions within the Flow and recreate them manually. \[Please take a screenshot before deleting for reference purpose, if required\]

### Related Links

Note: The PRB fix prevents this defect from happening, but if the flow/action is currently affected by this defect, it will stay defective until the workaround is performed.
