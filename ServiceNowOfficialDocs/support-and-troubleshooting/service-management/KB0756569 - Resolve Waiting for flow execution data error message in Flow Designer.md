---
title: "Resolve \"Waiting for flow execution data\" error message in Flow Designer"
aliases:
  - KB0756569
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0756569
kb_number: KB0756569
last_modified: 2025-08-05
---

## Resolve "Waiting for flow execution data" error message in Flow Designer

  

### Issue

Flow designer does not start and displays the message "Waiting for flow execution data". 

### Release

Any release

### Cause

No Flow Engine Event Handler records in the sys\_trigger are in a READY state to process the flow.   
  

### Resolution

To resolve this:

1.  Verify whether the instance is overloaded with event processing.
    -   Go to **System Diagnostics** > **Diagnostic Page.** If pending events are marked in red, check with your performance team.
2.  Make sure that Flow Engine Event Handler records in the sys\_trigger table are in the READY state to process the flow.
    -   Check this in **System Definition** > **Tables** by filtering the sys\_trigger table for Flow Engine Event Handler records.  
        [sys\_trigger\_list.do?sysparm\_query=name%3DFlow%20Engine%20Event%20Handler](/sys_trigger_list.do?sysparm_query=name%3DFlow%20Engine%20Event%20Handler)
