---
title: "How to fix ServiceNow Flows not triggering when conditions are met"
aliases:
  - KB0997550
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0997550
kb_number: KB0997550
last_modified: 2025-11-17
---

## How to fix ServiceNow Flows not triggering when conditions are met

  

### Issue

The following steps help to resolve cases where flows are not triggering even when the conditions are met.

### Release

Some steps will not work after the Tokyo upgrade due to changes in the sys\_json\_chunk table structure.

### Cause

This typically happens when flows are moved by an update set that doesn't include all necessary trigger mappings required for the flows to run properly. To verify if this is the cause follow these steps to verify if the trigger mapping is set up correctly.

#### Find the flow trigger record

1.  From the sys\_hub\_flow table, obtain the sys\_ID of the non-triggering flow.
2.  Go to the sys\_flow\_trigger\_plan table and search using Plan ID = Flow Sys ID (From Step 1)   
    -   _https://<instance\_name>.service-now.com/sys\_flow\_trigger\_plan\_list.do?sysparm\_query=plan\_id=<flow\_sys\_id>_
3.  Open the resulting record.
4.  Right-click the header, select **Show XML**, and copy the sys ID from the **trigger** field.
5.  Go to the sys\_flow\_trigger table and search using sys ID = Flow Trigger sys ID (from Step 4) 
    -   https://<instance\_name>.service-now.com/sys\_flow\_trigger\_list.do?sysparm\_query=sys\_id=<sys\_flow\_trigger\_sys\_id>

The results should show the flow trigger record for the affected flow.

-   Missing \[sys\_flow\_plan\_context\_binding\] record: The flow has likely never been executed.
-   Missing \[sys\_flow\_trigger\] record: This is preventing the flow from executing. 

**Note**: These verification steps won't work after the Tokyo upgrade due to changes in the sys\_json\_chunk table structure.

#### Verify the trigger mapping

1.  Copy the sys ID of the trigger record identified in the previous steps (step 6).
2.  Go to the sys\_trigger\_runner\_mapping table and search using Trigger.sys ID = Trigger sys ID (from Step 1)
    -   https://<instance\_name>.service-now.com/sys\_trigger\_runner\_mapping\_list.do?sysparm\_query=trigger.sys\_id=<sys\_flow\_trigger\_sys\_id>
3.  Copy the sys\_trigger\_runner\_mapping sys ID from the record found in Step 2.
4.  Go to the sys\_json\_chunk table and search using Parent = Trigger Runner Mapping sys ID (from Step 3) 
    -   https://<instance\_name>.service-now.com/sys\_json\_chunk\_list.do?sysparm\_query=document\_id=<sys\_trigger\_runner\_mapping\_sys\_id>

If you found all records: The trigger mapping is correct; look for other issues affecting your flows.

If any records are missing: The trigger mapping is incorrect, causing your flows not to trigger.

### Resolution

To fix this issue:

1.  Make a small change to the affected flow (such as adding a comment).
2.  Publish and activate the flow.

This forces the flow to recompile, generating the triggers correctly.

Additionally, identify the update set containing the affected flow and advise against using it in the future.
