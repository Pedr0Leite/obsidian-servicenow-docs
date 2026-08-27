---
title: "Condition script to trigger the scheduled job on Quarterly basis"
aliases:
  - Condition script to trigger the scheduled job on Quarterly basis
tags:
  - servicenow-dev-program
  - code-snippet
  - condition-script-to-trigger-the-scheduled-job-on-quarterly-basis
  - scheduled-jobs
---

The script in code-snippets/Scheduled Jobs/Condition script to trigger the scheduled job on Quarterly basis/Condition script to trigger the scheduled job on Quarterly basis.js
can be used in the condition script of scheduled job so that the scheudled job will trigger only quarterly.

The script will make the answer true only on March, June, September, December months. All other months the script will make answer false.

Use Case:
There will be requirement to send audit tasks and approvals on every Quarter Day 1 (March 1, June1, September1, December1).
In this case the scheeduled job can be scheduled for every month day 1. Then in the condition script, the script in "Condition script to trigger the scheduled job on Quarterly basis.js" can be used.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/API Token Expiry Warning/Readme|API Token Expiry Warning]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Approval Reminder/README|Approval Reminder]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto Disable account/Readme|Auto Disable account]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto close changes requests updated 30 days prior/README|Auto close changes requests updated 30 days prior]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto upgrade store applications/Readme|Auto upgrade store applications]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto-Assign Unassigned Incidents Older Than 30 Minutes/Readme|Auto-Assign Unassigned Incidents Older Than 30 Minutes]]
