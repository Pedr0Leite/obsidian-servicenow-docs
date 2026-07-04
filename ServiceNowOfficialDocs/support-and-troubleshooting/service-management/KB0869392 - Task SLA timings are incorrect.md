---
title: "Task SLA timings are incorrect"
aliases:
  - KB0869392
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0869392
kb_number: KB0869392
last_modified: 2024-04-18
---

## Task SLA timings are incorrect

  

### Issue

The user was reporting that timings on their task SLA record(s) were incorrect, and they wanted to know why.

### Resolution

It was found that the user had customized a core SLA-related Script Include, **TaskSLA**. 

The user was counseled to revert this Script Include, and then to utilize the [Repair SLAs](https://docs.servicenow.com/bundle/paris-it-service-management/page/product/service-level-management/concept/c_RepairSLAs.html "Repair SLAs") functionality.

This kind of behavior with unexpected timings can occur when _any_ core SLA-related Script Includes are customized. Most typically, it is seen when **TaskSLA**, **TaskSLAController**, or **SLAConditionBase** are customized. 

It is critically important to note that Support Engineers are experts in OOB behavior and specialize in resolving OOB break-fix behaviors. Behaviors occurring as a direct result of customizations like this (and which do not occur when OOB methods are used) are not in the engineer's area of expertise and are out of scope for Support.
