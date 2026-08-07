---
title: "[SAMP-Reclamation] Removal Candidate requests (RCC) status stuck in \"Awaiting Revocation\" even after completion"
aliases:
  - KB1582136
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1582136
kb_number: KB1582136
last_modified: 2023-12-05
---

## \[SAMP-Reclamation\] Removal Candidate requests (RCC) status stuck in "Awaiting Revocation" even after completion

  

### Issue

Some of the Removal Candidate requests (RCC) are stuck in "Awaiting Revocation" even after completion of flow.

### Release

All instances with Software Asset Management Professional is installed.

### Cause

Once the [removal candidate is created](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1178718), then the related workflow _Reclamation workflow_ is triggered. Within the workflow, we have the activity "Run orchestration workflow" _(with stage "Awaiting Revocation")_ which is intended to decide type of software removal _(Software Installation, Software Subscription, Hybrid Software, etc)_. If the software is Hybrid type _(both physical install and subscription)_ then it will go in the path "Hybrid Subscription Software".

In this workflow path "Hybrid Subscription Software", there is no activity with stage "Closed Complete" to set the status of task to "Closed Complete.

So when the workflow runs the activity "Run orchestration workflow" its sets the task status as "Awaiting Revocation" based on activity stage. And once the this activity passes in "Hybrid Subscription Software" direction its directly connected to End activity and task status never set.

![](/sys_attachment.do?sys_id=9357b87b9732b514dfd73dae2153afaf)

### Resolution

We can customize the workflow with another activity between "Run orchestration workflow" and "End" activity to set the appropriate status to the task. _(Ex. Set Values activity with stage as "Closed Complete")_

### Related Links

-   [How software removal candidates are created for a reclamation rule](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1178718)
