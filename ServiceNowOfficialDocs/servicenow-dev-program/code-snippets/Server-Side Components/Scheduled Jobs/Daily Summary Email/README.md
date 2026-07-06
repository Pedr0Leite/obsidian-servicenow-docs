---
title: "Daily Summary Email"
aliases:
  - Daily Summary Email
tags:
  - servicenow-dev-program
  - code-snippet
  - daily-summary-email
  - scheduled-jobs
---

Use Case: Daily Summary Notification Email
This scheduled job sends a daily email to a specific IT group with a quick summary of important IT service metrics, including:
Number of open incidents
Pending approvals
SLAs breached today
High priority incidents (P1/P2)
Incidents unassigned for more than 24 hours

Who receives it?
Active members of a designated ServiceNow group (like Incident Management or IT Operations).

Why?
To give IT teams and managers daily visibility into workload, critical issues, and bottlenecks so they can act quickly and keep service running smoothly.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/API Token Expiry Warning/Readme|API Token Expiry Warning]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Approval Reminder/README|Approval Reminder]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto Disable account/Readme|Auto Disable account]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto close changes requests updated 30 days prior/README|Auto close changes requests updated 30 days prior]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto upgrade store applications/Readme|Auto upgrade store applications]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto-Assign Unassigned Incidents Older Than 30 Minutes/Readme|Auto-Assign Unassigned Incidents Older Than 30 Minutes]]
