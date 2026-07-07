---
title: "Convert Request to Incident"
aliases:
  - Convert Request to Incident
tags:
  - servicenow-dev-program
  - code-snippet
  - convert-request-to-incident
  - ui-actions
---

This is a UI Action that creates an Incident using the field values of the current Request and closes the Request as "Closed Skipped".
It also compliles all the worknotes and comments into a single worknote on the Incident.

This action has an OnClick function as well as a server-side function that runs using:

if (typeof current != 'undefined')

The OnClick function opens a confirmation window to protect against misclicks.

Setting up the UI Action:

![alt text](https://github.com/ezratkim/code-snippets/blob/main/UI%20Actions/Convert%20Request%20to%20Incident/UIActionScreenshot.png)

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Loggedin user as Incident assigned to/ReadMe|Add Loggedin user as Incident assigned to]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Show Workflow Related link/README|Add Show Workflow Related link]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add collapsible element in knowledge article/README|Add collapsible element in knowledge article]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Call Subflow/README|Call Subflow]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/CallingPopUpBoxInListView/README|CallingPopUpBoxInListView]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Cancel Flow Executions/README|Cancel Flow Executions]]
