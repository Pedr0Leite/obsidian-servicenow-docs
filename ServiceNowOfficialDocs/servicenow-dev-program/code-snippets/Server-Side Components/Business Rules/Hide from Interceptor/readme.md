---
title: "Hide from Interceptor"
aliases:
  - Hide from Interceptor
tags:
  - servicenow-dev-program
  - code-snippet
  - hide-from-interceptor
  - business-rules
---

How often you come across cases where 'Private Task' or any other task available from the list needs to be disabled for handful of users (users who are ITIL users but from XYZ department) from the interceptor that shows up when 'New' button is clicked on the Task table.
This can be controlled by creating a 'Query' Business Rule on Answer (sys_wizard_answer) table. Script will be used in Business Rule to achieve the same.
Private Task is just an example as the point here is to help understand how to control something that shows up in the interceptors needs to be made available/disabled.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
