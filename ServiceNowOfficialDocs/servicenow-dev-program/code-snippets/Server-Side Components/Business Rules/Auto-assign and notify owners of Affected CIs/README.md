---
title: "Auto-assign and notify owners of Affected CIs"
aliases:
  - Auto-assign and notify owners of Affected CIs
tags:
  - servicenow-dev-program
  - code-snippet
  - auto-assign-and-notify-owners-of-affected-cis
  - business-rules
---

Create Change Tasks for each affected CI and notify its owner

1. Create a Business Rule - After Insert/Update Change Request Table
2. Query the task_ci table to get all CIs linked to this Change Request 
4. Fetch all the actual CI records present in the table
5. Proceed if CI has a owner, check if a Change Task for this CI and owner already exists
6. If not existing create a change task for CI owner
7. Triggers an event to notify the CI owner (email/push).

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
