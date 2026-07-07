---
title: "Clone incident on Agent Workspace"
aliases:
  - Clone incident on Agent Workspace
tags:
  - servicenow-dev-program
  - code-snippet
  - clone-incident-on-agent-workspace
  - ui-actions
---

Agent can use this UI Action on incident form to clone/copy any existing incident.

This UI Action will create a copy of incident once agent confirm the action.

Caller field will not be copeied to newly created incident, only basic information of ticket like Company, Short Description, Category, Sub-Category 

Create an UI Action with below field values:

Name - Clone Incident

Action Name - clone_incident

Table - Incident

Client - checked (true)

Onclick - cloneIncident();

Workspace Form Button - checked (true)

Script - use clone_incident.js

Workspace Client script - use workspace_client_script.js

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Loggedin user as Incident assigned to/ReadMe|Add Loggedin user as Incident assigned to]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Show Workflow Related link/README|Add Show Workflow Related link]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add collapsible element in knowledge article/README|Add collapsible element in knowledge article]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Call Subflow/README|Call Subflow]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/CallingPopUpBoxInListView/README|CallingPopUpBoxInListView]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Cancel Flow Executions/README|Cancel Flow Executions]]
