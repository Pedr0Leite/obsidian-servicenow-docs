---
title: "Auto upgrade store applications"
aliases:
  - Auto upgrade store applications
tags:
  - servicenow-dev-program
  - code-snippet
  - auto-upgrade-store-applications
  - scheduled-jobs
---

This script will automatically upgrade the Store applications of your choice, based on a system property.

A few key points about this approach:
• The script upgrades only the applications listed in the system property (auto_upgrade_store_apps) and applications that are included as child.
• It can be scheduled to run automatically or triggered manually.
• You can add an email notification, a banner, or another form of alert to notify admins about which applications were updated.

This is a simple way to save time and keep Store applications up to date without manual intervention.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/API Token Expiry Warning/Readme|API Token Expiry Warning]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Approval Reminder/README|Approval Reminder]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto Disable account/Readme|Auto Disable account]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto close changes requests updated 30 days prior/README|Auto close changes requests updated 30 days prior]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto-Assign Unassigned Incidents Older Than 30 Minutes/Readme|Auto-Assign Unassigned Incidents Older Than 30 Minutes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Bucket Group Reporting/readme|Bucket Group Reporting]]
