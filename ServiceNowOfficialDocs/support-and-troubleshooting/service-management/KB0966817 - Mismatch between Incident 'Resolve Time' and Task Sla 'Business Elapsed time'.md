---
title: "Mismatch between Incident 'Resolve Time' and Task Sla 'Business Elapsed time'"
aliases:
  - KB0966817
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0966817
kb_number: KB0966817
last_modified: 2026-06-24
---

## Mismatch between Incident 'Resolve Time' and Task Sla 'Business Elapsed time'

  

### Issue

  
The "Resolve time" Field on the Incident Record is not matching the "Business elapsed time" on the Task SLA 

### Release

All

### Cause

Basically the 2 fields are using different field values in their calculations.  
Resolve Time : calendar\_stc on Incident Table  
Business Elapsed Time: business\_duration in Task\_sla table  
  
1\. The Resolve time is available on the Incident \[incident\].  
This field allows for easy reporting on how long it takes for Incident to be closed, and is stored as an integer number of seconds.  
Specific business rules calculate the Resolve time field when the record is resolved or marked closed, and measure the difference between the Opened and Closed dates.  
On the Incident table, the field is calculated on the incident resolution, or closure, whichever happens first, based on the business rule mark\_resolved or mark\_closed. Both are based on the Incident table to get a trigger.  
When the incident is resolved, the calculation is based on the mark\_resolved business rule.  
  
Resolve time - calendar\_stc uses "dateDiff" function for calculating different of the duration between opened and resolved.  
  
dateDiff(String, String, boolean):-  
Calculates the difference between two dates independent of the calendar.  
  
  
2\. The Business Elapsed Time is on the Task\_sla table.  
Its calculations are done by the script include SLACalculatorNg.  
However it uses the SLA definition Start, pause, and stop conditions to determine how the calculations are executed.  
The Task Sla which attaches will have a Start time based by default when it got created, otherwise it uses the value in the field 'set start to'.

### Resolution

  
There is no incorrect behavior. The reported issue is by design based on the SLA definitions configuration and the standard design of mark\_resolved business rule.  
  
If you would like to try and get the calculations to match for these 2 fields then you can potentially configure the SLA Definitions 'set start to' field to 'opened'.  
This will ensure the Start time on the sla is using the 'opened' field value to start it's calculation same as the Business Rule which is calculating the 'Resolve time' value.
