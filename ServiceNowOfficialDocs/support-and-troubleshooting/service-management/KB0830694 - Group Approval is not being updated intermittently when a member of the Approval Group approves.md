---
title: "Group Approval is not being updated intermittently when a member of the Approval Group approves "
aliases:
  - KB0830694
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0830694
kb_number: KB0830694
last_modified: 2025-04-30
---

## Group Approval is not being updated intermittently when a member of the Approval Group approves

  

### Issue

Group Approval is not being updated intermittently when a member of the Approval Group approves 

### Cause

Here, Ask for Approval action is followed by Update record. Found 2 errors thrown by the flow during the process of approval update event and around the time of the approval from user.

1.Error Flow Designer: Operation(BIL Franchise Creation.0bc66397db2d045097af3a1b7c961987.5df22d920b10030085c083eb37673a04.updateHandler$1) failed with error: com.snc.process\_flow.exception.OpException: called block 'BIL Franchise Creation.0bc66397db2d045097af3a1b7c961987.5df22d920b10030085c083eb37673a04.updateHandler$1' failed. Check the context log for exception details.

2.Error Flow Designer: Operation(updateHandler.Update Approvals) failed with error: java.lang.NullPointerException

First error indicates an exception during the execution of business rules when the Approval action was trying to update  
the approval field

Based on this, a possible race condition could happen during the processing of the approval update event by the flow and later the update of same record being approved.

### Resolution

If this issue is recurrent, consider the possibility to add a "Wait for a duration of time" flow logic between the "Ask for Approval" action and the "Update Record" action for this flow to reduce the possibility of a race condition.
