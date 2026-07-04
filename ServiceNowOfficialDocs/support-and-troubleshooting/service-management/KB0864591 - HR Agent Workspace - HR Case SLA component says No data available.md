---
title: "HR Agent Workspace - HR Case SLA component says \"No data available\""
aliases:
  - KB0864591
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0864591
kb_number: KB0864591
last_modified: 2024-04-08
---

## HR Agent Workspace - HR Case SLA component says "No data available"

  

### Issue

The user reported that the HR Case SLA component in the HR Agent Workspace was showing "No data available" for a HR Case that had a task SLA on it. The user wanted to know why the task SLA did not show information there.

### Cause

The query that the seismic component "HR Case SLA" is using does not check for task SLAs which have a Stage of "Paused". This is why "No data available" is pulled and displayed - because the task SLA on the HR Case is Paused.

### Resolution

Based on a conversation had with ServiceNow's HR Developers, it was found that there is an internal query done on the task\_sla table for the task via it's sys\_id, checking for a Stage value of "In Progress" only (this is why task SLAs where Stage = Paused do not return results), and are ordered by remaining Business time left. 

So, in order to not see the "No data available", there should be a task SLA on the HR Case being queried where the Stage value is "In Progress". Then, the information for that task SLA will display.
