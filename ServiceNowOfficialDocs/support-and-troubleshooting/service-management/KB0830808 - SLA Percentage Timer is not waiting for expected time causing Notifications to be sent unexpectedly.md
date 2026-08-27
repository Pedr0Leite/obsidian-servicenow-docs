---
title: "SLA Percentage Timer is not waiting for expected time causing Notifications to be sent unexpectedly"
aliases:
  - KB0830808
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0830808
kb_number: KB0830808
last_modified: 2026-06-24
---

## SLA Percentage Timer is not waiting for expected time causing Notifications to be sent unexpectedly

  

### Issue

SLA percentage timer is not waiting until the business elapsed percentage is reached and triggering notifications .

### Release

All

### Cause

The schedule record could not be retrieved when processing the Timer activity.

We had identified that at the time the workflow is being resumed the issue is that the User triggering the workflow has no access to the schedule.

In this case as the schedule record could not be retrieved when processing the Timer activity it executes erroneously.  
  
We could see this confirmed in the logs as below:

below shows the point at which we resumed the SLA for INC0050196:

04:38:43.073 Warning Default-thread-6 C762C9FB1BB454107EAAA718BD4BCBC2 txid=6b7315ff1b38 WARNING \*\*\* WARNING \*\*\* Get for non-existent record: cmn\_schedule:703ae601dbb74090f33f69b2ca961976, initializing  
04:38:43.075 Warning Default-thread-6 C762C9FB1BB454107EAAA718BD4BCBC2 txid=6b7315ff1b38 WARNING \*\*\* WARNING \*\*\* Adding 13 Days 3 Hours to 2020-05-22 11:32:02 using schedule null ran too long without hitting schedule times - using simple date addition  
04:38:43.076 Warning Default-thread-6 C762C9FB1BB454107EAAA718BD4BCBC2 txid=6b7315ff1b38 WARNING \*\*\* WARNING \*\*\* Adding 13 Days 3 Hours to 2020-05-22 11:32:02 using schedule null ran too long without hitting schedule times - using simple date addition  
04:38:43.122 Debug Default-thread-6 C762C9FB1BB454107EAAA718BD4BCBC2 txid=6b7315ff1b38 DEBUG: completed Wait 75 percent of SLA duration(d3572c95dbb0d090aa7e94b8db961925): event=update  
04:38:43.216 Warning Default-thread-6 C762C9FB1BB454107EAAA718BD4BCBC2 txid=6b7315ff1b38 WARNING \*\*\* WARNING \*\*\* Get for non-existent record: cmn\_schedule:703ae601dbb74090f33f69b2ca961976, initializing  
04:38:43.218 Warning Default-thread-6 C762C9FB1BB454107EAAA718BD4BCBC2 txid=6b7315ff1b38 WARNING \*\*\* WARNING \*\*\* Adding 13 Days 3 Hours to 2020-05-22 11:32:02 using schedule null ran too long without hitting schedule times - using simple date addition  
04:38:43.218 Debug Default-thread-6 C762C9FB1BB454107EAAA718BD4BCBC2 txid=6b7315ff1b38 DEBUG: completed Wait 75 percent of SLA duration(d3572c95dbb0d090aa7e94b8db961925): event=resume  
04:38:43.375 Warning Default-thread-6 C762C9FB1BB454107EAAA718BD4BCBC2 txid=6b7315ff1b38 WARNING \*\*\* WARNING \*\*\* Adding 1 Day 23 Hours 15 Minutes to 2020-05-22 11:38:43 using schedule null ran too long without hitting schedule times - using simple date addition  
04:38:43.375 Info Default-thread-6 C762C9FB1BB454107EAAA718BD4BCBC2 txid=6b7315ff1b38 \*\*\* Script: Scheduling: Workflowbdf1997f1b3854107eaaa718bd4bcba5 for: 2020-05-24 10:53:43

### Resolution

Change the domain of the Schedule to be Global to ensure it is visible to the Timer.
