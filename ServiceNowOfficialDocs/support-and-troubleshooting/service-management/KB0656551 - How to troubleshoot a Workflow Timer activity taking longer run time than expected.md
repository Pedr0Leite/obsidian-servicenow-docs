---
title: "How to troubleshoot a Workflow Timer activity taking longer run time than expected"
aliases:
  - KB0656551
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0656551
kb_number: KB0656551
last_modified: 2025-10-10
---

## How to troubleshoot a Workflow Timer activity taking longer run time than expected

  

### Issue

A **Workflow Timer activity** does not finish running for the intended time. For example, when the timer activity was set to run for 10 seconds, the system taking instead several minutes before finishing the activity execution.

### Release

All

### Cause

Overloaded scheduler due to **ASYNC Business Rules**, causing several ASYNC scheduled jobs running on the sys\_trigger\_list.do. The async jobs and WFTimer jobs have the same priority level 100. The system does not allow the WFTimer jobs to be pushed ahead of ASYNC jobs, and vice-versa. This causes a delay in WFTimer jobs while waiting on the worker threads.

### Resolution

Open the **System Diagnostics** page and check the **scheduler queue length**. In these circumstances, if the value shows in **red**, the scheduler is overloaded. Check all active ASYNC Business Rules generating scheduled jobs that are flooding the scheduler. Disable Async Business Rules, review and evaluate why the scheduler cannot handle the intended load.

For the priority level issue of the timer activity, a business rule can be created on the sys trigger table that will check to see if a wf.timer record is inserted. Once it gets inserted, the business rule should change the priority value to 90.

All jobs on the sys\_trigger table run at a priority 100. Therefore, making the wf.timer priority to 90 will cause it to run before other scheduled jobs, which will fix the issue.
