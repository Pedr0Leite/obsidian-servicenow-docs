---
title: "Determining causes for skipped approvals (group or user)"
aliases:
  - KB0549963
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0549963
kb_number: KB0549963
last_modified: 2025-07-03
---

## Determining causes for skipped approvals (group or user)

  

### Issue

While a Flow is running (active execution) or a workflow is running in an active context, an approval step/activity can inadvertently skip to the next step/activity.

### Cause

-   The desired approval user or group is missing or invalid (for example, sys\_id).
-   The desired group record from which to pull approvers has no group members.
-   The desired approval user or group record became inactive after the approval record was created.
-   The target for user or group information is a dot-walked field, such as current.opened\_by.department.manager, and it has a missing or invalid approval user or group.
-   The business rule on the table that is associated with the workflow is invalid.

### Resolution

1.  Verify after approval that the workflow progressed to the next activity. If a workflow failed to progress, check the business rules. For more information, see [Debugging Business Rules](https://docs.servicenow.com/csh?topicname=r_DebuggingBusinessRules.html&version=latest).
2.  Point to each processed approval activity to find activities where the State is **Finished** and the Result is **Skipped**.
3.  Navigate to **Workflow > Workflow Editor** and open the workflow.
4.  Double-click the skipped activity, and then click **Users** or **Groups**.
5.  Assign an active user or group for the approval activity. For more information, see [Workflow Error Handling](https://docs.servicenow.com/csh?topicname=c_WorkflowErrorHandling.html&version=latest).
6.  For Flows, ensure that within the execution, referenced users/groups are both active and, if a group record, that there are group members in the group (if the desired outcome is to pull the members of 'X' group and populate them as approvers).
