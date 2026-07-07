---
title: "Close parent RITM when SC Task is Closed"
aliases:
  - Close parent RITM when SC Task is Closed
tags:
  - servicenow-dev-program
  - code-snippet
  - close-parent-ritm-when-sc-task-is-closed
  - business-rules
---

This BR is created basically to close the parent requested item when ever the sc task is closed 
1. When: After
2. Update: true
3. Add filter condition as 
    1. State is one of closed complete or closed incomplete
    2. Catalog Item needs to be selected
4. Advanced check box needs to be checked
5. Refer to closeParentRITMwhenSCTaskisClosed.js

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
