---
title: "Show Today Emails Logs"
aliases:
  - Show Today Emails Logs
tags:
  - servicenow-dev-program
  - code-snippet
  - show-today-emails-logs
  - ui-actions
---

# Show Today Emails Logs

The UI Action simplifies the debugging of ServiceNow notifications by redirecting you from the notification definition to the email log list view with the predefined filter.

Setting:
- Name: Show Today Emails Logs
- Table: sysevent_email_action
- Show insert: false
- Show update: true
- Client: true
- Form link: true
- Onclick: openEmailLogList()
- Condition: new GlideRecord('sys_email_log').canRead()

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Loggedin user as Incident assigned to/ReadMe|Add Loggedin user as Incident assigned to]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Show Workflow Related link/README|Add Show Workflow Related link]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add collapsible element in knowledge article/README|Add collapsible element in knowledge article]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Call Subflow/README|Call Subflow]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/CallingPopUpBoxInListView/README|CallingPopUpBoxInListView]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Cancel Flow Executions/README|Cancel Flow Executions]]
