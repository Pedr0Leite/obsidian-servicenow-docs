---
title: "Incident Is updated by System"
aliases:
  - KB0749452
  - Incident Is updated by System
tags:
  - servicenow
  - support-kb
  - incident-management
  - inactivity-monitor
  - sla
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749452
kb_number: KB0749452
last_modified: 2025-11-19
---

## Incident Is updated by System

  

### Issue

Some cases will create incidents that are updating the system but not showing in the transaction logs, not showing in the work notes or additional comments. The only thing we can see is an updated system and updated date.

2019-05-17 01:32:54 (961) worker.5 worker.5 txid=f823ced4db61 \*\*\* Start Background transaction - system, user: system  
2019-05-17 01:32:54 (964) worker.5 worker.5 txid=f823ced4db61 Starting: Flow Engine Event Handler.cf2c76f2db652300598718df4b9619f6, Trigger Type: Repeat, Priority: 100, Upgrade Safe: true, Repeat: 2 Seconds  
2019-05-17 01:32:54 (964) worker.5 worker.5 txid=f823ced4db61 Name: Flow Engine Event Handler  
2019-05-17 01:32:54 (977) worker.5 worker.5 txid=f823ced4db61 Completed: Flow Engine Event Handler in 0:00:00.010, next occurrence is 2019-05-17 03:32:55  
2019-05-17 01:32:55 (012) worker.0 worker.0 txid=f823ced4db61 \*\*\* Start Background transaction - system, user: system  
2019-05-17 01:32:55 (027) worker.4 worker.4 txid=f823ced4db61 \*\*\* Start Background transaction - system, user: system  
2019-05-17 01:32:55 (029) worker.0 worker.0 txid=f823ced4db61 Starting: report view events process.0fb2c110871321004ebe19fa84e3ecf8, Trigger Type: Interval, Priority: 100, Upgrade Safe: false, Repeat: 5 Seconds  
2019-05-17 01:32:55 (029) worker.0 worker.0 txid=f823ced4db61 Name: report view events process  
2019-05-17 01:32:55 (034) worker.4 worker.4 txid=f823ced4db61 Starting: activity.monitor timer INC0858620.64b7ed58db25f30057d6164948961969, Trigger Type: Once, Priority: 100, Upgrade Safe: false, Repeat:  
2019-05-17 01:32:55 (034) worker.4 worker.4 txid=f823ced4db61 Name: activity.monitor timer INC0858620  
2019-05-17 01:32:55 (040) worker.0 worker.0 txid=f823ced4db61 Completed: report view events process in 0:00:00.009, next occurrence is 2019-05-17 03:33:00  
2019-05-17 01:32:55 (051) worker.6 worker.6 txid=f823ced4db61 \*\*\* Start Background transaction - system, user: system  
2019-05-17 01:32:55 (051) worker.4 worker.4 txid=f823ced4db61 Completed: activity.monitor timer INC0858620 in 0:00:00.014, next occurrence is null

### Cause

-   Check the: Navigate to **System Policy > SLA > Inactivity Monitors > [Priority One Inactivity](https://empvmettukingston.service-now.com/sysrule_escalate_am.do?sys_id=34a17cb4c61122b7006b897258cbd702&sysparm_view=)**
-   Check this Priority One Inactivity setting. this is the one updating the incident in the background based on scheduled time.

### Related Links

Check the documentation: [Set an inactivity monitor](https://www.servicenow.com/docs/bundle/xanadu-platform-administration/page/administer/time/task/t_SetAnInactivityMonitor.html)

## Related

- [[KB0524319 - Inactivity Monitor not triggering events as expected for incident matching conditions]]
