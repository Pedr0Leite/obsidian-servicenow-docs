---
title: "If Conflicts are there restrict change resquest to move further"
aliases:
  - If Conflicts are there restrict change resquest to move further
tags:
  - servicenow-dev-program
  - code-snippet
  - if-conflicts-are-there-restrict-change-resquest-to-move-further
  - business-rules
---

This is a before Business rule with update(checked)
When we try to move the record from new to assess state it will check for the possible conficts which are available in the record. even if it finds a single match. It restricts the record to move further and it pops an error message to the user indicating that there are conficts to resolve before moving to the assess State

This code helps in restricting the records to move further especially for change requests if there are some conflicts in the records it also shows an error message to the user.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
