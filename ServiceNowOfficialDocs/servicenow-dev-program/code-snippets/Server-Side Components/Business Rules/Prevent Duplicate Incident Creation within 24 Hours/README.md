---
title: "Prevent Duplicate Incident Creation within 24 Hours"
aliases:
  - Prevent Duplicate Incident Creation within 24 Hours
tags:
  - servicenow-dev-program
  - code-snippet
  - prevent-duplicate-incident-creation-within-24-hours
  - business-rules
---

Prevent Duplicate Incident Creation within 24 Hours 

1. Write a Business Rule - Before Insert
2. Select the Incident Table
3. Only run/execute for all the active incidents
4. By Gliding the Incident Table will get the caller_id, short_description for checking the current caller and text provided for the short description
5. Querying the Incident Table as created within 24 Hours and excluding the closed incidents
6. Stop insert and show an error message
7. Prevent Incident record creation

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
