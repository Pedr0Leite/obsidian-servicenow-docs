---
title: "Incidents are being automatically updated by system"
aliases:
  - KB0750214
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750214
kb_number: KB0750214
last_modified: 2024-04-07
---

## Incidents are being automatically updated by system

  

### Issue

# Symptoms

Many incidents are being automatically being updated around 8:00 and a few minutes past that.   
The updated by shows that it is being updated by (user = system) but there are no records on the audit table showing that anything was updated at that time.   
Reviewed scheduled jobs but there are no jobs running at that time. 

# Cause

After checking the node logs, it was observed that the System updates to Incidents are made by SLA default scheduled jobs which run regularly to refresh the time calculations on each active task SLA associated to the Incidents. 

Also, it was observed that the Next Action field values of the SLA default scheduled jobs correlate with the system update on Incidents

# Resolution

This is the expected behaviour. The System updates to Incidents are made by SLA default scheduled jobs which run regularly to refresh the time calculations on each active task SLA associated to the Incidents.   
  
Detailed information about the SLA scheduled Jobs can be found here:   
\- Scheduled jobs for SLA   
[https://docs.servicenow.com/csh?topicname=c\_ScheduledJobsForSLA.html&version=latest](https://docs.servicenow.com/csh?topicname=c_ScheduledJobsForSLA.html&version=latest)   
  
These Scheduled jobs run more frequently when the task SLA associated to the Incident is closer to being breached.
