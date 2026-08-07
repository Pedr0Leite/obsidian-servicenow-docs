---
title: "Change Risk Assesment mandatory before state change"
aliases:
  - Change Risk Assesment mandatory before state change
tags:
  - servicenow-dev-program
  - code-snippet
  - change-risk-assesment-mandatory-before-state-change
  - business-rules
---

This is a code snippet which can be used in a Business rule to prevent the state of Change Request Move from New state when there is no risk Assesment attached to the Change Request.
Table : change_request When: Before Update: True Conditions : state || CHANGESFROM || New AND state || is not || Cancelled AND type || is one of || Normal,Emergency
Note: This script is helpful for all the tables and their related tables which has assesmenets enabled, The BR should be created on related table and filters can be added accordingly

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
