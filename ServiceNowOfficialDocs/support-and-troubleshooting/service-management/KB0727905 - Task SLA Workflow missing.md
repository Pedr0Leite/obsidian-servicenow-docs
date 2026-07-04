---
title: "Task SLA Workflow missing"
aliases:
  - KB0727905
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727905
kb_number: KB0727905
last_modified: 2026-01-09
---

## Task SLA Workflow missing

  

### Issue

task\_sla do not look like they have a workflow context or workflow attached

### Release

All

### Cause

com.snc.sla.workflow.run\_for\_breached is set to False by default

### Resolution

Enable this property if you would like the workflow to run for a Task SLA that is already breached when it is attached to the Task.

-   Type: true | false, set it to "True"
