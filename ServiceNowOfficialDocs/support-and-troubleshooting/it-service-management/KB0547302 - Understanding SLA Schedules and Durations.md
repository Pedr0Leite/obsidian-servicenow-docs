---
title: "Understanding SLA Schedules and Durations"
aliases:
  - KB0547302
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547302
kb_number: KB0547302
last_modified: 2025-01-11
---

## Understanding SLA Schedules and Durations

  

### Issue

This article helps to understand SLA time duration measurements and provides guidelines for SLA schedules definitions.

### Ignore Legacy Fields

The following fields are present on the Task table (but do not appear on the default Task form), which were used by the old [Legacy escalation engine](https://docs.servicenow.com/csh?topicname=c_GetStartedWithSLAs.html&version=latest "Legacy escalation engine"): 

-   **Escalation**
-   **Made SLA**
-   **SLA due**

These are legacy fields, and have not been used since the [2010 / 2011 engine](https://docs.servicenow.com/csh?topicname=c_GetStartedWithSLAs.html&version=latest "2010 / 2011 engine") were introduced.

Please ignore these legacy fields, they have no relevance to current SLA functionality.

### Remove the "Days" element from Duration fields

[As described here](/kb?id=kb_article_view&sysparm_article=KB0547270 "KB0547270: Understanding SLA times: actual elapsed time and business elapsed time"), the business duration fields (**Business elapsed time**, **Business elapsed percentage** and **Business time left**) for a task SLA are based on a [schedule](https://docs.servicenow.com/csh?topicname=c_UseSchedules.html&version=latest "schedule") if such a schedule is specified in the relevant [SLA Definition](https://docs.servicenow.com/ "SLA Definition"). Similarly, the **Planned end time** of the Task SLA is calculated based on the **Schedule** and **Duration** values entered on the SLA Definition.

This can cause some confusion over the different definitions of a "day" between business (form the Schedule) and actual elapsed times.  For example, if you select a Schedule of 09:00-17:00 Monday-Friday on the SLA Definition and wanted a **Planned end time** in 3 days time you would need to enter 1 day in the **Duration** field - _8 hour working days multiplied by 3 = 24 hours_

One way of reducing this confusion is to modify the **Duration** field on the SLA Definition, to remove the **Days** element.

To do this: 

1.  Open an SLA Definition record, which shows **Days** within the **Duration** field. For example:  
      
    ![](/sys_attachment.do?sys_id=d89b2f4bdb8101d4679499ead3961906)  
      
    
2.  Right-click on the **Duration** field and select **Configure Dictionary**.
3.  Ensure you are on the **Advanced** view in the Dictionary record.
4.  In the **Attributes** field, enter **max\_unit=hours**  
      
    ![](/sys_attachment.do?sys_id=909b2f4bdb8101d4679499ead396190c)  
      
    
5.  Save the record.
6.  This removes the **Days** element from the Duration field in an SLA record. For example:  
      
    ![](/sys_attachment.do?sys_id=509b2f4bdb8101d4679499ead396190a)

 **Note:** This same modification can be made to any duration type fields where it would make more sense to show the value in just hours, minutes and seconds

### Force Population of Business Elapsed Time

By default, if the SLA definition does not use a schedule, business duration fields are left blank.

If you want this to be always populated, you can force this by using a 24 X 7 schedule. 

1.  Navigate to **System Scheduler > Schedules > Schedules**.
2.  Create a new schedule.
3.  Add a schedule entry to the schedule, checking the **All day** check box, and selecting **Daily** in the Repeats field.  
      
    ![](/sys_attachment.do?sys_id=5c9b2f4bdb8101d4679499ead396190f)  
      
      
    **Note:** if a schedule has no entries, schedule calculation will still work but is highly inefficient.  
      
    
4.  Submit the schedule entry and save the schedule record.
5.  Return to the SLA Definition record, and set the **schedule** field to be the new 24 X 7 schedule

All future task SLA records will then have business duration fields populated.

### Related Links

-   [Troubleshooting service level agreements (SLAs)](/kb?id=kb_article_view&sysparm_article=KB0523638 "Troubleshooting service level agreements (SLAs)")
-   [KB0547270: Understanding SLA times: actual elapsed time and business elapsed time](/kb?id=kb_article_view&sysparm_article=KB0547270 "KB0547270: Understanding SLA times: actual elapsed time and business elapsed time")
