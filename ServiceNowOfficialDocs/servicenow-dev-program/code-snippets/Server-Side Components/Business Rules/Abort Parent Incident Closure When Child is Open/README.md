---
title: "Abort Parent Incident Closure When Child is Open"
aliases:
  - Abort Parent Incident Closure When Child is Open
tags:
  - servicenow-dev-program
  - code-snippet
  - abort-parent-incident-closure-when-child-is-open
  - business-rules
---

This business rule is designed for ServiceNow to prevent a parent incident from being closed or resolved while it still has active child incidents.
If a user attempts to set the parent incident's state to "Resolved," "Closed," or "Cancelled," the rule will query for any related child incidents that are still open. 
If open children are found, the update will be aborted, and an error message will be displayed to the user.

Navigate to System Definition > Business Rules in the ServiceNow filter navigator.
Click New.
Fill out the form with the following details:
Name: Prevent Parent Closure with Open Children
Table: Incident [incident]
Advanced: true
When: before
Update: Check this box.
In the When to run tab, set the Condition field:
current.state.changesTo(7) || current.state.changesTo(6) || current.state.changesTo(8)  //The state values are: 6 (Resolved), 7 (Closed), 8 (Cancelled).
Note: The state values (6, 7, 8) may vary based on your instance configuration.
In the Advanced tab, paste the provided script into the Script field.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add woknotes for 75 percent SLA/README|Add woknotes for 75 percent SLA]]
