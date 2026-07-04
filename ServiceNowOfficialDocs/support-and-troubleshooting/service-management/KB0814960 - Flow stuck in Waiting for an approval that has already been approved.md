---
title: "Flow stuck in \"Waiting\" for an approval that has already been approved"
aliases:
  - KB0814960
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814960
kb_number: KB0814960
last_modified: 2024-09-20
---

## Flow stuck in "Waiting" for an approval that has already been approved

  

### Issue

The user has a record where the associated Flow is still stuck "Waiting" for an approval even though the approval has already come through as approved.

### Resolution

In this sort of example the very first thing to try, after verifying that the sysapproval\_approver record was approved, would be nudging the Flow.  
  
To do this, we will need to run a background script. Here's an example "nudge" (**please note:** the nudge API will only work in New York Patch 3 and beyond):

-   `sn_fd.FlowAPI.nudgeFlowsWaitingOn("_TABLE_NAME_", "_SYS_ID_", 20);   `

Where "\_TABLE\_NAME\_" is the table the affected record lives on, "\_SYS\_ID\_" is the sys\_id of the record (e.g. the sys\_id of the incident, change, etc), and the "20" is the amount of time the system should wait before nudging the Flow, in seconds.  
  
So, the above will create a sysevent record with name "flow.nudge\_waiting\_on" to be executed in about 20 seconds from its creation with a target based on the information specified in \_TABLE\_NAME\_ and \_SYS\_ID\_.

You should be able to run the above script in a background script and nudge the Flow this way.  
  
If the flow does not respond to the nudge although all evidence dictates that it should, there may be a larger issue with the associated sys\_rw\_action record not having a "flow.listener" for the approval record(s).
