---
title: "Reject approvals created before an year"
aliases:
  - Reject approvals created before an year
tags:
  - servicenow-dev-program
  - code-snippet
  - reject-approvals-created-before-an-year
  - scheduled-jobs
---

**Script Purpose:**
This script helps you manage approval records in ServiceNow. It searches for approval requests in the sysapproval_approver table that were created more than 12 months ago and are currently marked as "requested." The script then updates these records to change their status to "rejected."

**How to Use This Script**
Where to Run It: You can execute this script in a server-side context, such as a Scheduled Jobs, Script Include, or Background Script. Make sure you have the necessary permissions to access and update records in the sysapproval_approver table.

**Be Cautious:** The script will automatically find the relevant approval records and update all matching records, so double-check the criteria before executing it.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/API Token Expiry Warning/Readme|API Token Expiry Warning]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Approval Reminder/README|Approval Reminder]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto Disable account/Readme|Auto Disable account]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto close changes requests updated 30 days prior/README|Auto close changes requests updated 30 days prior]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto upgrade store applications/Readme|Auto upgrade store applications]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto-Assign Unassigned Incidents Older Than 30 Minutes/Readme|Auto-Assign Unassigned Incidents Older Than 30 Minutes]]
