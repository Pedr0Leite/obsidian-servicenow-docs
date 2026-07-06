---
title: "Check for active tickets before inactivating user"
aliases:
  - Check for active tickets before inactivating user
tags:
  - servicenow-dev-program
  - code-snippet
  - check-for-active-tickets-before-inactivating-user
  - business-rules
---

This BR is designed to identify all active tickets from the "tables" array in ServiceNow and if there are any active tickets are found then the user would not be inactivated.
This BR helps administrators easily to find all the active tickets that assigned to the user who is being deactivated so that they can notify the management about this inconsistancy.

Administrators can either notify the user or the assignment group managers so that the active tickets can be transferred to a different user so that this user can be deactivated.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
