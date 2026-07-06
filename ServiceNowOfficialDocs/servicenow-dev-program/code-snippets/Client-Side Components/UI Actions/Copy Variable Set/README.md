---
title: "Copy Variable Set"
aliases:
  - Copy Variable Set
tags:
  - servicenow-dev-program
  - code-snippet
  - copy-variable-set
  - ui-actions
---

This UI action will help create a copy of the Variable set, including the Catalog Client Script, Catalog UI actions and Variable.

Below Configurations need to be performed on the UI action form on creation

Table : Variable Set
Active: True
Show Update : True
Client : True
Action name : copyQuestionSet
On Click : clientConfirm()

### update
To complete a task on issue #745 
Replace JavaScript function confirm() with GlideModal() API.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Loggedin user as Incident assigned to/ReadMe|Add Loggedin user as Incident assigned to]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Show Workflow Related link/README|Add Show Workflow Related link]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add collapsible element in knowledge article/README|Add collapsible element in knowledge article]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Call Subflow/README|Call Subflow]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/CallingPopUpBoxInListView/README|CallingPopUpBoxInListView]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Cancel Flow Executions/README|Cancel Flow Executions]]
