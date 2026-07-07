---
title: "Set Incident Priority Critical"
aliases:
  - Set Incident Priority Critical
tags:
  - servicenow-dev-program
  - code-snippet
  - set-incident-priority-critical
  - ui-actions
---

Set Incident Priority Critical

This UI Action sets current incident record as priority as Critical.

When clicked
Below Conformation message will be displayed to the user as below
"Are you sure you want to set priority as Critical?"

If user selects cancel nothing will happen.

If user selects confirm then
a) It sets the Priority of the current Record as 1-Critical by setting Urgency and Impact as 1-High.
b) It also sets 'assigned_to' field as 'logedin user'.
c) It also upends the description as "Priority is set to Critical by 'logedin User'".

** Please note that it changes field values only on the form that is client side. 
Unless you submit or update the record, field values will not be updated in the database table records.

You can use this as reference to set other field values as well.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Loggedin user as Incident assigned to/ReadMe|Add Loggedin user as Incident assigned to]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Show Workflow Related link/README|Add Show Workflow Related link]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add collapsible element in knowledge article/README|Add collapsible element in knowledge article]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Call Subflow/README|Call Subflow]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/CallingPopUpBoxInListView/README|CallingPopUpBoxInListView]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Cancel Flow Executions/README|Cancel Flow Executions]]
