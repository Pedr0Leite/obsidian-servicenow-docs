---
title: "ScheduleJob by ExectionTime_perDay"
aliases:
  - ScheduleJob by ExectionTime_perDay
tags:
  - servicenow-dev-program
  - code-snippet
  - schedulejob-by-exectiontime-perday
  - glideaggregate
---

*********LONG RUNNING SCHEDULE JOBS PER DAY BY NUMBER OF TIMES EACH EXECUTED AND PROCESSING TIME********

Script to get Top 10 scheduled jobs by processing time and number of times executed per day

 - Query the table SYS_LOG_TRANSACTION to identify the TOP 10 Schedule Job by Number of times it executed in one day and How much processing time it took to complete the execution

>>>>> Go to https://<your instance URL>/syslog_transaction_list.do?sysparm_query=urlLIKE<your scheduled job name> and check the "Transaction processing time"

 - This will help to identify top contibutors that cconsume instance resource and can potentially cause slowness due to long running schedule jobs

 - You can execute this as Background scipt or Fix script to get the output.
 - This can be executed as scheduled script to gte the top contributor details daily to take proactive actions

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count All Open Incidents Per Priority/readme|Count All Open Incidents Per Priority]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count Inactive Users with Active incidents/README|Count Inactive Users with Active incidents]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count incidents based on category/README|Count incidents based on category]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count open Incidents per Priority and State using GlideAggregate/README|Count open Incidents per Priority and State using GlideAggregate]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Create Problem based on incident volume/README|Create Problem based on incident volume]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Find Oldest Open Incidents per Group/README|Find Oldest Open Incidents per Group]]
