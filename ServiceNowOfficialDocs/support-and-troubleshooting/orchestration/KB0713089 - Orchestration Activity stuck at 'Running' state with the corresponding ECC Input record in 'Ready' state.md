---
title: "Orchestration Activity stuck at 'Running' state with the corresponding ECC Input record in 'Ready' state"
aliases:
  - KB0713089
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713089
kb_number: KB0713089
last_modified: 2026-05-22
---

## Orchestration Activity stuck at 'Running' state with the corresponding ECC Input record in 'Ready' state

  

### Issue

If a Workflow Activity is stuck at '**Running**' state and the corresponding ECC Input record is stuck in '**Ready**' state. This may lead to an issue with the instance's scheduler workers.

### Release

Ant

### Cause

After the insert of the corresponding ECC Input record, The out-of-box '**Automation - Sensors**' will be triggered and creates a schedule record in **sys\_trigger** table with name '**Async: Automation Sensors**' which one of the instance's scheduler workers should pick and process it and as a result the corresponding ECC Input Record's state will change to '**Processed**' instead of '**Ready**' which will complete the activity execution and move to the workflow to the next activity. 

There are several potential causes for this:

-   Other scheduled jobs at higher priority are queued and would need to finish executing first.
-   long running jobs are blocking the scheduler workers
-   You may check the count and status of the Background scheduler workers from Instance\_name.service-now.com/**stats.do** 

### Resolution

You can check the count and status of the Background scheduler workers from Instance\_name.service-now.com/stats.do page.

Inspect the sys\_trigger table to see if anything is currently 'running' state, and since when. 

Using the next run time, state, and priority fields, see if other jobs are effectively blocking the Async: Automation Sensors jobs from running. Identify what those jobs are and how many of them. It's possible a huge batch job is running, or a custom script is running out of control and causing a flood of unexpected jobs.
