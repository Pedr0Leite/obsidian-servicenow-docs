---
title: "How to continue running Workflow SLA timers during upgrades"
aliases:
  - KB0550770
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0550770
kb_number: KB0550770
last_modified: 2026-04-21
---

## How to continue running Workflow SLA timers during upgrades

  

### Issue

How to continue running Workflow SLA timers during upgrades

Workflow Timer activities and SLA Percentage Timers in SLA Workflows use the System Scheduler to wake the workflow up again after a timer. **During a system Upgrade or Patch, Workflow Timer activities and SLA Percentage Timers are prevented from running**. Any that should have triggered during the upgrade run after the upgrades finishes. This introduces a persistent delay in your workflows, meaning all subsequent activities such as SLA Notification emails will be run and sent late.

Generally, it is a never a good idea to run more than you have to during an upgrade. Code and data mismatches for short periods of time during the upgrade could, theoretically, cause unexpected behavior. Custom Workflows and the updates they trigger could also cause performance issues at any time, and that would be bad if it were to happen during an upgrade. However, we do not prevent workflows starting or continuing due to user transactions during an upgrade, so it would be equally safe to allow workflows to continue running after timers as well.

**IMPORTANT NOTES**:

-   For **SLA Percentage Timer** this should only be done if the SLA workflows (for task\_sla) are still Out-of-Box, if customizations have been verified to not generate possible problems during the upgrade, or if it is crucial that SLAs notifications are not paused during the upgrade.  
    Remember that SLA workflows should only ever have Timers and Create Event or Notification activities, and Branch and Join, and never have any functional code doing changes or updates. The out-of-box business rules for tasks and SLAs are not designed to have additional updates happen during the SLA Workflow running, and this will cause performance issues like recursion.
-   It is not recommended to force continuing workflows after normal '**Timer**' activities during an upgrade, because with a good workflow implementation this is never necessary. Where very short 'Timer' activities have been used as a fix or workaround for some other issue in code running as part of the same transaction or for the same record, then the correct solution to that would be to fix the other issue. Where that can't be easily fixed, instead of a Timer, best practice is to use Workflow Events and the Wait for WF Event workflow activity to continue the workflow after whatever it had to wait for has finished running and broadcast the event to allow the workflow to continue.

### Release

All

### Resolution

There are multiple ways to control if workflow can wake up from timer during upgrade.

**1.  Configure workflow individually**

Every Timer activity has configuration "Run during upgrade" that has 3 options:

1) If global property is true(glide.workflow.timer.upgrade\_safe)

Timer will resume if property glide.workflow.timer.upgrade\_safe set to 'true'. Default property value is 'false'

2) Always

Always resume even during upgrade irrespective of property value.

3) Never

Don't resume during upgrade  irrespective of property value.

![](/sys_attachment.do?sys_id=0c4bd11193020e18f2167de86cba1008)

**2\. Set global property**

Global property glide.workflow.timer.upgrade\_safe can be set to 'true'. Default value for this property is 'false'.

By default "Run during upgrade" configuration is set to option #1, 'If global property is true(glide.workflow.timer.upgrade\_safe)'. This way global property will affect all the workflows in the system.

If it is possible to identify which Timer activity is critical to run during upgrade, prefer approach #1 which is Configure workflow individually
