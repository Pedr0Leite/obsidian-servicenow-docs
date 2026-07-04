---
title: "Task SLAs aren't attaching"
aliases:
  - KB0998479
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0998479
kb_number: KB0998479
last_modified: 2024-09-25
---

## Task SLAs aren't attaching

  

### Issue

The user was facing an issue where their SLA Definition was not attaching as a task SLA.

Also, task SLAs were only attaching one at a time, per update (e.g. if three SLA Definitions were supposed to attach to the task record on insert, SLA Definition attached as a task SLA on update #0, update #1 a new SLA Definition would attach, etc).

### Cause

The user was missing core Script Include **TaskSLAFlow**.

### Resolution

As shared above, the user was missing a core Script Include, **TaskSLAFlow**. 

All of the remaining pieces of the user's SLA configuration (Script Includes, Business Rules, etc) were Out of Box (OOB).

After importing **TaskSLAFlow** from a lower environment into Production, the issue stopped, and all task SLAs attached on insert as expected and transitioned correctly when their Start/Pause/Stop conditions were met.
