---
title: "Security Operations LogRhythm Integration: Delay in creating an incident on the instance"
aliases:
  - KB0788857
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788857
kb_number: KB0788857
last_modified: 2024-04-08
---

## Security Operations LogRhythm Integration: Delay in creating an incident on the instance

  

### Issue

Security Operations LogRhythm Integration: Delay in creating an incident on the instance when 'Process LogRhythm integrations', Schedule Job is set to run every 5 minutes.

### Cause

The Schedule Job runs only when the current time and the last successful processed time of the profile is greater than the polling interval, the polling interval is 5 minutes

### Resolution

Update the scheduled job interval to be run more frequently.  
Go to 'System Definition' --> 'Scheduled Jobs' --> 'Process LogRhythm integrations'.  
Change the 'Repeat Interval' to run for every 1 minute instead of out of the box 5min.

NOTE: You cannot update the LogRhythm Alarm Profile to less than 5 minutes.
