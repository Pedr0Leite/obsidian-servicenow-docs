---
title: "Update CI status on Change Request closure"
aliases:
  - Update CI status on Change Request closure
tags:
  - servicenow-dev-program
  - code-snippet
  - update-ci-status-on-change-request-closure
  - business-rules
---

Update CI status on Change Request Closure 

1. Create a Business Rule - After Update
2. Select the Change Request Table.
3. Add a condition as when Change state = "Closed"
4. Run only when Change is moving to Closed
5. Query all CI relationships for this Change Request
6. Update CI status based on the condition
7. The relationship table that links a change (task) to CIs (ci_item).

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
