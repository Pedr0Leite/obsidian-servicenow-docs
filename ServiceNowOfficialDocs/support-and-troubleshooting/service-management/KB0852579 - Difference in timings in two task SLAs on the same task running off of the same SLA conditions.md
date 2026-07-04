---
title: "Difference in timings in two task SLAs on the same task running off of the same SLA conditions"
aliases:
  - KB0852579
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0852579
kb_number: KB0852579
last_modified: 2024-04-08
---

## Difference in timings in two task SLAs on the same task running off of the same SLA conditions

  

### Issue

The user was seeing timing discrepancies when comparing two task SLAs, based on two separate and distinct SLA Definitions which had the same conditions within each SLA Definition respectively. They wanted to know why the timings weren't identical.

### Resolution

The issue, in this case, is that while the SLA Start, Pause, Stop, and Reset conditions were the same, the Schedule was not.   
  
On one Schedule for one SLA Definition, the "Time zone" was set to "Floating", and on another, the "Time zone" was set to "US/Central".

This very small difference is what caused the issue.   
  
If a user selects the value of "Floating" for their Time Zone schedule field, the time zone is relative to whatever process is accessing the item at the time.  
  
For example, if a resource manager in Amsterdam sets a floating schedule for 8:00 AM. to 5:00 PM, a user in San Jose sees the schedule as 8:00 AM to 5:00 PM.  
  
When a schedule is defined in a specific time zone however, like US/Central, users in different time zones see the schedule with their own time zone applied. This is the difference and the cause of the behavior.
