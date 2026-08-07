---
title: "Workflow is not working as expected"
aliases:
  - KB0696073
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696073
kb_number: KB0696073
last_modified: 2024-09-20
---

## Workflow is not working as expected

  

### Issue

Workflow is not working as expected. The if condition in the workflow is always taking the "no" path even though the condition for the "yes" path is satisfied.

### Release

Kingston Release

### Cause

The issue is caused due to the business rule

### Resolution

The issue is caused due to a custom business rule.

In the script section there is a current.update().

So whenever there is a current.update() in a business rule, then it would cause a recursive call of the same business rule until the service now back-end engine recognizes it and prevents the further execution of the business rule.

This would cause a delay in the execution of another business rule. We set the "requested\_for" value as the variable value"u\_requested\_for" over here.

So due to this reason,  if activity in the "workflow" would run before the execution of the first BR (one with current.update()).

Therefore, when the if activity runs, the "requested\_for" would still be the user who places the request. This user has the "workflow approver" value and therefore the if activity would take the "no" path. (this is the expected behaviour of the if activity)

But the "approval activity" would fetch the approvers from the variable value "u\_requested\_for." (and not the Request.requested\_for)

So the variable value will point to the caller (in our case the caller would have the "workflow approver" as empty). Therefore no approver records would be generated and the approval activity would be skipped.

Thus to avoid the issue, please remove the current.update in the Business rule.
