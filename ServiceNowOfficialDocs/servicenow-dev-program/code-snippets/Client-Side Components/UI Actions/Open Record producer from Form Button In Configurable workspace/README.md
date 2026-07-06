---
title: "Open Record producer from Form Button In Configurable workspace"
aliases:
  - Open Record producer from Form Button In Configurable workspace
tags:
  - servicenow-dev-program
  - code-snippet
  - open-record-producer-from-form-button-in-configurable-workspace
  - ui-actions
---

When we want to open a catalog item with details from current record and map it to the opened catalog form then we can use this code.

This UI Action and catalog client script Redirects you to the record producer or catalog item( based on the sys id provided) and auto-populates the fields from the parent record to the catalog item/record producer variables.

1. UI Action
   Client - true
   action name - open_item
   show update - true ( As per your requirement)
   onClick - openItem();
   Workspace Form button - true
   Format for Configurable Workspace - true 

2. Catalog Client script.
   Type - Onload
   Applies on catalog item view - true
   Name - ParseURL

Note : Above UI Action works in Configurable workspace and opens the catalog item/record producer in workspace itself.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Loggedin user as Incident assigned to/ReadMe|Add Loggedin user as Incident assigned to]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Show Workflow Related link/README|Add Show Workflow Related link]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add collapsible element in knowledge article/README|Add collapsible element in knowledge article]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Call Subflow/README|Call Subflow]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/CallingPopUpBoxInListView/README|CallingPopUpBoxInListView]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Cancel Flow Executions/README|Cancel Flow Executions]]
