---
title: "How are approvals marked as cancelled via a Workflow"
aliases:
  - KB0862953
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0862953
kb_number: KB0862953
last_modified: 2024-09-20
---

## How are approvals marked as cancelled via a Workflow

  

### Issue

The user wanted to know how their approvals were being marked as "Cancelled" - where that logic was stored.

### Resolution

The user was using an "Approval - Group" workflow activity to generate their approvals. It was found that the logic to transition the State of the approvals to "Cancelled" was stored in the Workflow Activity Definition for "Approval - Group". The function is as follows:

```
 onCancel: function() {      this.approvalUtils.setPendingGroupApprovalsByIds(activity.scratchpad.approval_ids, 'cancelled');      this.approvalUtils.setPendingUserApprovalsByGroup(activity.scratchpad.approval_ids, 'cancelled');      activity.state = 'cancelled';      activity.result = 'cancelled';   },
```

This logic is on line 105 of the "Script" section of the Workflow Activity Definition ( ref: /nav\_to.do?uri=wf\_activity\_definition.do?sys\_id=354e911f0a0a029a00e6a0e6ad74206f ).
