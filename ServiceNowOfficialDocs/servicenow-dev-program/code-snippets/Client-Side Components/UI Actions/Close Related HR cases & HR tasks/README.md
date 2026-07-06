---
title: "Close Related HR cases & HR tasks"
aliases:
  - Close Related HR cases & HR tasks
tags:
  - servicenow-dev-program
  - code-snippet
  - close-related-hr-cases--hr-tasks
  - ui-actions
---

Scenario:-

Table: HR Case

Create a form button named "Check related item and Close Complete" feature and list down the related child HR cases and HR tasks
in the pop-up message.
Upon confirmation, it will close the current case and other listed items.

This will help in reducing the manual effort of closing items manually.

Scripts:
Client UI script to handle the confirmation popup and state of current case.

GlideAJAX enabled script include to fetch the data and close the related items.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Loggedin user as Incident assigned to/ReadMe|Add Loggedin user as Incident assigned to]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Show Workflow Related link/README|Add Show Workflow Related link]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add collapsible element in knowledge article/README|Add collapsible element in knowledge article]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Call Subflow/README|Call Subflow]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/CallingPopUpBoxInListView/README|CallingPopUpBoxInListView]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Cancel Flow Executions/README|Cancel Flow Executions]]
