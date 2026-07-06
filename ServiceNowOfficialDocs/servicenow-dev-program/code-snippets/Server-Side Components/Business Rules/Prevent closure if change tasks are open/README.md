---
title: "Prevent closure if change tasks are open"
aliases:
  - Prevent closure if change tasks are open
tags:
  - servicenow-dev-program
  - code-snippet
  - prevent-closure-if-change-tasks-are-open
  - business-rules
---

Prevent Closure if the change tasks are open

1. Create a Before Business Rule.
2. Applicable to Change Request Table.
3. Use Before - Update Business Rule.
4. Add filter conditions if required.
5. Apply the Business Rule script.
6. If the change request have the active change tasks are still open then we can't proceed with the submission.
7. If required we can add few more query conditions.
8. 

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
