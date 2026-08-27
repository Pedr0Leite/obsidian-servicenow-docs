---
title: "Considerations about Pause in Service Level Agreements"
aliases:
  - KB0550783
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0550783
kb_number: KB0550783
last_modified: 2024-04-07
---

## Considerations about Pause in Service Level Agreements

  

### Issue

# Overview

* * *

Considerations about Pause in Service Level Agreements

# Subject

* * *

The Paused stage for a task\_sla is only an indicator that the record is paused. The 2010 and 2011 SLA Engines consider a task\_sla to be paused only if the pause\_time field is not null. If the pause time was not recorded in the record, it is not really paused and will continue to be processed even if the stage says Paused.

While a task\_sla is paused, the planned\_end\_time does not have any meaning because the engine has stopped calculating it. Because the length of the pause is undefined, the planned\_end\_time can't be known. The SLA Engine leaves the value set to its last expected value, and will recalculate the Planned end time when it comes off pause and resumes.

As documented in "Example: Using Relative Durations with SLAS" in the product documentation page Define a Relative Duration, pause processing is not compatible with relative durations. This is the reason the Pause Condition is removed from the form when you specify a relative duration in a SLA Definition.
