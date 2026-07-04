---
title: "Repairing SLAs is taking a long time - why?"
aliases:
  - KB0748239
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748239
kb_number: KB0748239
last_modified: 2024-04-07
---

## Repairing SLAs is taking a long time - why?

  

### Issue

# Symptoms

-   When using the Repair SLAs functionality on only 10-15 records, the process at times takes 30+ seconds and thus seems to impact performance.

# Release

-   Kingston Patch 12

# Cause

Even with repairing only 10-15 task\_sla records, the process can take time.  
  
The reasoning behind this possible delay is that Repair SLAs spins through the entire history of the task and runs the SLA engine for each historic change to rebuild the related task\_sla records. The speed of this process depends on the complexity of the history of the task, the load on the system at the time of repair, etc. Repairing is quite a heavy activity.  
  
If there are any additional concerns after reading through this article, please feel free to open up a case and an Engineer will happily assist.
