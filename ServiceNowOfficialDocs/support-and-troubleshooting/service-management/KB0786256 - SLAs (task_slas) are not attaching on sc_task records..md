---
title: "SLAs (task_slas) are not attaching on sc_task records."
aliases:
  - KB0786256
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786256
kb_number: KB0786256
last_modified: 2024-04-07
---

## SLAs (task\_slas) are not attaching on sc\_task records.

  

### Issue

The user has many sc\_task records where they are expecting some SLAs (task\_slas) to attach. Unfortunately, the task\_sla is not attaching, and the user wanted to know why this is happening.

### Resolution

An investigation was conducted on reported record SCTASK0100000 to understand why SLA Definition "P3 - Clean Avengers Facility - 96 hrs" did not attach as a task\_sla. The reason this SLA Definition did not attach as a task\_sla to SCTASK0100000 is that it did not meet the Start conditions before the Stop conditions were also met (further explanation below).  
  
To have SLA Definition "P3 - Clean Avengers Facility - 96 hrs" attach to SCTASK0100000, the below must be true:

-   Assignment group is "Facilities"
-   Priority is "3 - Moderate"
-   State is not "Closed"

To stop the SLA Definition (transition the "Stage" of the task\_sla to "Completed"), the below must be true:

-   State is "Closed"

In this case, SCTASK0100000's audit history shows that Assignment group of "Facilities" is true, State not being "Closed" is true, but at the time Priority is set to "3 - Moderate", the Stop condition is also simultaneously true (State is "Closed"). It is covered in the documentation that a task\_sla will _never_ attach if both the Start and Stop condition are true simultaneously:

-   [SLA conditions](https://docs.servicenow.com/csh?topicname=c_SLAConditions.html&version=latest "SLA conditions")

Therefore, this SLA Definition not attaching as a task\_sla is expected, as Priority was only set after the Stop condition of the SLA was already met.  
  
This is an issue with the user's process, versus with the SLA Engine or SLA functionality. Out of Box (OOB), this does not occur.
