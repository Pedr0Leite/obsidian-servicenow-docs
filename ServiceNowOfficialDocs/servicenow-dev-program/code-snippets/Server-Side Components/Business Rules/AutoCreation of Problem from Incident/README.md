---
title: "AutoCreation of Problem from Incident"
aliases:
  - AutoCreation of Problem from Incident
tags:
  - servicenow-dev-program
  - code-snippet
  - autocreation-of-problem-from-incident
  - business-rules
---

This is After- Business rule Created on Incident Table.
In which I have enabled Both insert and Update check Box to true.
Intially, we will create a field called major Incident(true/false field).
If the user checks that and updates an Incident record Immediately a Problem record will be generated with the current values of the Incident
A pop up message will be displayed as well.
If we want we can even put the condition's that only an incident manager can enable this checkBox
Without Installing the Major Incident Managment plugin, we can use this. But this will provide limted features for free.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
