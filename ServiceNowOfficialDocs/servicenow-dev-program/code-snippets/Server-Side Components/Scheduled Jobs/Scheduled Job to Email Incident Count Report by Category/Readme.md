---
title: "Scheduled Job to Email Incident Count Report by Category"
aliases:
  - Scheduled Job to Email Incident Count Report by Category
tags:
  - servicenow-dev-program
  - code-snippet
  - scheduled-job-to-email-incident-count-report-by-category
  - scheduled-jobs
---

Scheduled Job: Sends an email with monthly report based on incident category count

Uses a custom event (custom.monthly.incident.report) with two parameters:
parm1 → The formatted incident count report body
parm2 → The month name

Working:
Runs automatically on the 1st of each month.
Fetches all incidents created in the previous month.
Groups them by category and counts totals.
Sends a summarized email report to the admin.

Event Registration
Name: custom.monthly.incident.report
Queue: default

Notification Configuration
Name: Monthly Incident Report by Category
When to send: Event is fired
Event name: custom.monthly.incident.report
Recipients: admin@example.com (or “Admin” group)

Subject
Monthly Incident Count Report - ${event.parm2}

Body

Hello Admin,

Here is the count of incidents created during ${event.parm2}, categorized by type:
${event.parm1}

Regards,
ServiceNow Automated Reports

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/API Token Expiry Warning/Readme|API Token Expiry Warning]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Approval Reminder/README|Approval Reminder]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto Disable account/Readme|Auto Disable account]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto close changes requests updated 30 days prior/README|Auto close changes requests updated 30 days prior]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto upgrade store applications/Readme|Auto upgrade store applications]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto-Assign Unassigned Incidents Older Than 30 Minutes/Readme|Auto-Assign Unassigned Incidents Older Than 30 Minutes]]
