---
title: "Incident Business timings are showing as '0' when they should have values"
aliases:
  - KB0869390
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0869390
kb_number: KB0869390
last_modified: 2023-11-29
---

## Incident Business timings are showing as '0' when they should have values

  

### Issue

A user noted that with many of their incidents, business timings (Business duration and Business resolve time fields) were showing as '0' when they should have had some value. They wanted to know what was happening here.

### Cause

The business rule that populates Business duration was customized and was excluding the calculation needed to assign the desired values.

### Resolution

Investigating the issue, it was found that the user was concerned with two main fields:

-   business\_duration (Business duration)
-   business\_stc (Business resolve time)

Typically, these calculations are handled in the Out of Box (OOB) "mark closed" Business Rule.  
  
In the user's instance, however, there was a custom version of the Business Rule called "custom\_mark\_closed".  
  
It was noted that the OOB portion of the Business Rule which should calculate Business duration is commented out:

`if (dataChange || current.business_duration.nil())   current.business_duration = gs.calDateDiff(opened, closed, false);`  
  
And while a custom "sched" variable is declared which has the below logic,

`var sched = new GlideSchedule(sc);   current.business_duration= sched.duration(startDateTime,endDateTime).getDurationValue();   }`

It is actually never called or used anywhere, so there is no opportunity to fill in a business\_duration.  
  
It was recommended to the user that they revert the custom business rule to OOB or make the necessary changes internally to their custom version to populate business\_duration going forward. This would be a fix-forward resolution.

If the user wanted to fix the currently impacted tickets, they would need to write a custom script to iterate through the filtered list of incidents and run them through the logic to populate the correct times into the business duration field. It was recommended that the user do this via script in a scheduled job during off-business hours. Writing and testing such a script, if the user so desired to correct the impacted records, would be something that they and their internal development team would need to own.  
  
Support engineers are experts in OOB behavior and specialize in resolving OOB break-fix behaviors. Unfortunately, the debugging and implementation of customizations like this is not in the Support engineer's area of expertise and is out of scope for Support.
