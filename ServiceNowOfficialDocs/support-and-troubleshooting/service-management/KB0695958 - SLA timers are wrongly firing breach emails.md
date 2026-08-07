---
title: "SLA timers are wrongly firing breach emails"
aliases:
  - KB0695958
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695958
kb_number: KB0695958
last_modified: 2024-04-07
---

## SLA timers are wrongly firing breach emails

  

### Issue

# Symptoms

* * *

Receiving unexpected SLA breach emails

# Release

* * *

Jakarta Patch 8a

# Cause

* * *

What the user is seeing is expected behavior based on their configuration (please see continued explanation below...)

# Resolution

* * *

Per the above, the behavior seen is expected as the workflow associated to the task\_sla record does not recognize schedules on SLA definitions. Rather, the "SLA Percentage Timer" activity counts up to 100 percent based on when the task\_sla attaches to the parent record.  
  
When an SLA is attached, the workflow associated to the definition begins running immediately.  
  
The task\_sla of concern, "Change SLA - 8 Hours" attached to the parent record on 2018-07-31 at 09:59:22.  
  
The duration set on the relevant SLA Definition is 8 hours.  
  
Therefore, based on this information, an e-mail notification should fire per the SLA breaching on 2018-07-31 at about 17:59:22 (roughly 8 hours later).  
  
Indeed, the notification did fire: "CHG0642119 has exceeded closure SLA" at 2018-07-31, 17:59:31.  
  
This is expected.  
  
To avoid this behavior in the future, modify the workflow.  
  
After the "Begin" activity, it is recommended to use a "Wait For" activity with a Script inside which tells the system to calculate based on the Planned End Time (the user's desired "start" time). Only when that "start" time is reached, begin the 100% countdown.  
  
In this way, the above behavior will be avoided.
