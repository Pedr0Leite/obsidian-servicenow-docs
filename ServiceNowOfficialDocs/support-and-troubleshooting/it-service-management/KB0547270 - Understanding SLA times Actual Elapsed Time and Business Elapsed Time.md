---
title: "Understanding SLA times: Actual Elapsed Time and Business Elapsed Time"
aliases:
  - KB0547270
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547270
kb_number: KB0547270
last_modified: 2026-06-03
---

## Understanding SLA times: Actual Elapsed Time and Business Elapsed Time

  

### Issue

Task SLA records are associated to task records, such as incidents, based on their relevant [SLA Definition](https://docs.servicenow.com/csh?topicname=t_CreateAnSLADefinition.html&version=latest "SLA Definition").

Task SLAs contain timing information, including Actual elapsed time and Business elapsed time.  
  

![](/sys_attachment.do?sys_id=a89d68e2db82b450e515c223059619a8)

_**Tip**: To view the latest elapsed times, use the **Run SLA Calculation** button on the task SLA form._

Actual Elapsed Time and Business Elapsed Time

* * *

-   **Actual elapsed time** is the total time the SLA has taken until this time, minus any pause duration.
-   **Business elapsed time** is the total time the SLA has taken until this time, minus any pause duration, within the [business schedule](https://docs.servicenow.com/csh?topicname=c_UseSchedules.html&version=latest "business schedule") used by that SLA's [SLA Definition](https://docs.servicenow.com/csh?topicname=c_SLADefinitions.html&version=latest "SLA Definition").

**Note**: If the SLA definition does not use a schedule, Business elapsed time is left blank. 

Example

* * *

A schedule defined from 9am to 5pm is 8 hours long. If a task SLA starts at 12am, and the current time is 12pm, then the actual elapsed time is 12 hours, but the business elapsed time is 5 hours, and the business elapsed time will only restart at 9am on the following day.

![](/sys_attachment.do?sys_id=ac9d68e2db82b450e515c223059619bc)

  
In addition, if a schedule defines an 8-hour working day, a 24-hour business elapsed time equates to a 3-day elapsed time.

![](/sys_attachment.do?sys_id=349d68e2db82b450e515c223059619eb) 

Video Tutorial

* * *

  

### Related Links

[SLA elapsed time measures](https://docs.servicenow.com/csh?topicname=r_ElapsedTimeCounting.html&version=latest "SLA elapsed time measures")

[Troubleshooting service level agreements (SLAs)](https://support.servicenow.com/kb_view.do?sysparm_article=KB0523638 "Troubleshooting service level agreements (SLAs)")

[Understanding SLA Conditions](https://support.servicenow.com/kb_view.do?sysparm_article=KB0547356 "Understanding SLA Conditions")
