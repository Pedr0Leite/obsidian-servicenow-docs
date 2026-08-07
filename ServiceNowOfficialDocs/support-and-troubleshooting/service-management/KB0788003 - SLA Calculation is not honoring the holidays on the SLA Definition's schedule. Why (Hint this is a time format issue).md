---
title: "SLA Calculation is not honoring the holidays on the SLA Definition's schedule. Why? (Hint: this is a time format issue)"
aliases:
  - KB0788003
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788003
kb_number: KB0788003
last_modified: 2024-04-07
---

## SLA Calculation is not honoring the holidays on the SLA Definition's schedule. Why? (Hint: this is a time format issue)

  

### Issue

The user was facing a behavior where their holiday schedule was not being excluded from SLA breach time calculation. They wanted to know why this was.

### Resolution

_This behavior was originally documented in PRB1374850. However, this PRB is no longer available to see the details therein. Hence, this KB was created to document the issue._

* * *

It was found that when the "glide.sys.time\_format" system property is set to a value of "HH:mm z", some Out of Box (OOB) Business Rule and client-side scripting fail.

As such, what the user saved as 00:00 - 23:59, an "All day" range for a schedule, does not get saved as such. It gets saved as 00:00 - 00:00, or empty. This is further confirmed by clicking the "Show schedule" related link on the main cmn\_schedule record. When clicking "Show schedule", it is seen that no schedule entries show on the calendar there. This is why calculations are skewed.  
  
The workaround is to manually set the end time to 23:59 UTC. To do this, while on the main cmn\_schedule record, look down near the related lists and, in the schedule entry related list, double click where the "2019-06-10 (or whatever date) 00:00 UTC" display value is seen. This will bring up a value of "20190610T000000".  
  
It was recommended that the user change the value to be "20190610T235959" and that they press enter thereafter. This corrects the end time of the schedule and translates to a timestamp of "2019-06-10 23:59 UTC".  
  
Now, note that the "All day" flag turns from "False" to "True", and when the user navigates back to the main schedule "24 x 7 excluding weekends and holidays" and clicks the "Show schedule" Related link, entries are now seen in the calendar.
