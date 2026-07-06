---
title: "Send notification if the incident remains unassigned"
aliases:
  - Send notification if the incident remains unassigned
tags:
  - servicenow-dev-program
  - code-snippet
  - send-notification-if-the-incident-remains-unassigned
  - ui-actions
---

This is a UI Action script that adds a button to the Incident form. When clicked, it will check if the incident has been unassigned for more than 5 days. 
If this condition is met, the button will trigger a notification to the manager of the incident's assignment group, informing them that the incident is still unassigned.

Below are the conditions when UI action will be created:
Table: Incident
Show Insert: False
Show Update: True
Form Button: Checked (to add the button on the form)
Condition: current.assigned_to.nil() && current.assignment_group

The code contains below vaidations:
- The script checks if the incident has been unassigned for more than 5 days by comparing the current date with the sys_created_on date using gs.daysAgo().
- It verifies that the incident has an assignment group. If it does not, it displays an error message.
- Queries the sys_user_group table to get the assignment group’s manager. If a manager is found, it sets up a notification to send an email directly to the manager.
- Provides feedback to the user if the notification was sent or if there were issues (like missing assignment group or manager).
- Redirects the user back to the current incident form after the UI Action runs.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Loggedin user as Incident assigned to/ReadMe|Add Loggedin user as Incident assigned to]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add Show Workflow Related link/README|Add Show Workflow Related link]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Add collapsible element in knowledge article/README|Add collapsible element in knowledge article]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Call Subflow/README|Call Subflow]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/CallingPopUpBoxInListView/README|CallingPopUpBoxInListView]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Cancel Flow Executions/README|Cancel Flow Executions]]
