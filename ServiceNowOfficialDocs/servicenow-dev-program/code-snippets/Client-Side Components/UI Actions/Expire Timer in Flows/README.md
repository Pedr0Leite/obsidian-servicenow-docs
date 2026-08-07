---
title: "Expire Timer in Flows"
aliases:
  - Expire Timer in Flows
tags:
  - servicenow-dev-program
  - code-snippet
  - expire-timer-in-flows
  - ui-actions
---

This UI Action adds an admin-only button to Flow Context records in ServiceNow. It is designed to expire active timers within a flow, allowing developers and testers to bypass waiting stages during sub-production testing. This helps accelerate flow validation and debugging during development cycles, especially useful during events like Hacktoberfest.

Flows in ServiceNow often include Wait for Condition or Wait for Duration steps that can delay testing. This UI Action provides a quick way to expire those timers, enabling the flow to proceed immediately without waiting for the configured duration or condition. Features

Adds a button labeled "Expire Timers" to Flow Context records. Visible only to users with the admin role. Executes a script to expire all active timers associated with the selected Flow Context. Ideal for sub-production environments (e.g., development, test, or staging). Speeds up flow development and validation.

<img width="1584" height="165" alt="image" src="https://github.com/user-attachments/assets/64d02ab2-de5b-48b6-82ac-d00771f43898" />

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Loggedin user as Incident assigned to/ReadMe|Add Loggedin user as Incident assigned to]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Show Workflow Related link/README|Add Show Workflow Related link]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add collapsible element in knowledge article/README|Add collapsible element in knowledge article]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Call Subflow/README|Call Subflow]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/CallingPopUpBoxInListView/README|CallingPopUpBoxInListView]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Cancel Flow Executions/README|Cancel Flow Executions]]
