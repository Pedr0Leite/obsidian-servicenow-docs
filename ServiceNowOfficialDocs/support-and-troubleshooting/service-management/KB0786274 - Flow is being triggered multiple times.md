---
title: "Flow is being triggered multiple times"
aliases:
  - KB0786274
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786274
kb_number: KB0786274
last_modified: 2024-04-07
---

## Flow is being triggered multiple times

  

### Issue

This KB is for Flows that are triggered on CRUD operations on any supported table 

-   The flow is being triggered more than once
-   Multiple flows are running on the same source record

### Cause

-   This issue can be caused by the existence of duplicate Record Triggers for the same Flow
-   or the issue can be caused by the flow's condition being met twice on the same GlideRecord update

### Resolution

-   Review the Record triggers \[sys\_flow\_record\_trigger\] for the flow and check for any duplicate triggers. Deactivate the duplicate trigger

  

-   If the issue is NOT with the duplicate trigger records, then it could be due to the flow's condition being met twice
-   for example, if there is a condition: stage "is" fulfillment; and during the GlideRecord update it's being set twice, then the Flow will trigger twice
-   to resolve this in the example above, change the condition to: stage "changes to" fulfillment
-   Also, multiple flows triggering twice, as been determined to be a PRB; PRB1445168 - Flow has been triggered twice at the same time when two record updates happens concurrently even if the flow is configured to trigger once on update

  

-   if none of the above applies then it could be due to multiple \[sys\_trigger\_runner\_mapping\] records, where the "identifier" column is the flow's sys\_id, there should only be one of these records

### Related Links

**How do you link \[sys\_flow\_trigger\_plan\] record back up to the flow?**

-   Open \[sys\_flow\_trigger\_plan\] table, the "Plan Id" field contains the flow's sys\_id, and the "trigger" field contains the \[sys\_flow\_trigger\_plan\] record, alternatively if the flow is based on data/time trigger then it would be a \[sys\_flow\_timer\_trigger\] record
