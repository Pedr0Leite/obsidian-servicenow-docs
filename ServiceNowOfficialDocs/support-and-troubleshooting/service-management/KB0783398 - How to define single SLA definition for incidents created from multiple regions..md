---
title: "How to define single SLA definition for incidents created from multiple regions."
aliases:
  - KB0783398
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783398
kb_number: KB0783398
last_modified: 2024-04-08
---

## How to define single SLA definition for incidents created from multiple regions.

  

### Issue

How to apply a specific holiday schedule for SLA, based on caller's location (around the world).

### Cause

The holiday schedule needs to reference the working schedule via the Child Schedule related list.

### Resolution

  
There are two possible solutions:  
  
1\. Define multiple SLA definitions for different regions (specifying holiday schedules)   
  
2\. Define SLA definition to derive the schedule to use from the Task record, the schedule should be the holiday schedule to ensure the correct holidays are factored for the region.

Example:  
\- On the SLA definition, set the 'Schedule Source' as 'Incident field' and 'Schedule Source field' to 'Caller's schedule'.  
  
\- Create a new entry in the holiday schedule 'Holiday US'.

\- Holiday US schedule has child schedule as the work schedule (Example: '8-5 weekdays')  
\- Navigate to the user's profile to set the schedule field on the record.(Beth Anglin)  
\- We selected 'Holiday US' schedule on the schedule field on the user record.  
  
\- Now, create incident record with the caller as 'Beth Anglin' then the task SLA honors the caller's schedule.
