---
title: "Reassign Tasks When Assigned User is Inactive"
aliases:
  - Reassign Tasks When Assigned User is Inactive
tags:
  - servicenow-dev-program
  - code-snippet
  - reassign-tasks-when-assigned-user-is-inactive
  - business-rules
---

## Purpose
Automatically reassigns tasks or incidents when the currently assigned user becomes inactive.
This ensures that no work item stays unattended due to user deactivation, termination, or role changes, maintaining operational continuity and SLA compliance.
## Tables Applicable:
Any task-based table, such as incident, problem, change_request, etc.
## Implementation Details
Table: sys_user
Trigger: Business Rule – After Update
Condition: current.active == false && previous.active == true
Purpose: Trigger logic only when a user becomes inactive.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
