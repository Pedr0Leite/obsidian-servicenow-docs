---
title: "Top10jobsbyprocessingtime"
aliases:
  - Top10jobsbyprocessingtime
tags:
  - servicenow-dev-program
  - code-snippet
  - top10jobsbyprocessingtime
  - scheduled-jobs
---

This is script will be useful to montior your system performance by identifying the top contributors from schedule jobs by processing time to take necessary action. 

In this script time intervalis updated as last 15 min but in ideal scenario this should be scheduled everyday to get the count report and montior the schedule job that is take more time to get completed. 

OUTPUT:
*** Script: 
Top 10 url values from syslog_transaction



********** Execution Details for the column JOB: Check Glide Service Status **********

Executed total number of times : JOB: Check Glide Service Status 1

Top 10 response times : 45300


********** Execution Details for the column JOB: Regenerate CRL and Flush CRL Cache **********

Executed total number of times : JOB: Regenerate CRL and Flush CRL Cache 1

Top 10 response times : 1462


********** Execution Details for the column JOB: SC - Calculate Compliance **********

Executed total number of times : JOB: SC - Calculate Compliance 1

Top 10 response times : 5401


********** Execution Details for the column JOB: [ITSM Analytics] Daily Data Collection **********

Executed total number of times : JOB: [ITSM Analytics] Daily Data Collection 1

Top 10 response times : 16341

[0:00:00.048] Total Time

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/API Token Expiry Warning/Readme|API Token Expiry Warning]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Approval Reminder/README|Approval Reminder]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto Disable account/Readme|Auto Disable account]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto close changes requests updated 30 days prior/README|Auto close changes requests updated 30 days prior]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto upgrade store applications/Readme|Auto upgrade store applications]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto-Assign Unassigned Incidents Older Than 30 Minutes/Readme|Auto-Assign Unassigned Incidents Older Than 30 Minutes]]
