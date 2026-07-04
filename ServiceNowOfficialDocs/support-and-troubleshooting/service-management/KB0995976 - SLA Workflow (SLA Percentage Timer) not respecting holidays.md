---
title: "SLA Workflow (SLA Percentage Timer) not respecting holidays"
aliases:
  - KB0995976
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0995976
kb_number: KB0995976
last_modified: 2024-08-13
---

## SLA Workflow (SLA Percentage Timer) not respecting holidays

  

### Issue

The user had a task SLA with a schedule. In the schedule, a correctly configured floating holiday was present.

On the task SLA, there was a workflow running and, during the floating holiday, the SLA Percentage Timer progressed unexpectedly.

### Cause

System property "com.glideapp.workflow.duration.script\_uses\_schedule" (as the SLA Definition was using a "User specified duration" \[there is a different property for Relative duration SLA Definitions\]) was set to "false", so the schedule's holidays on the task SLA were not being honored.

### Resolution

As a result of the above system property having a value of "false", the schedule's holidays were not being honored. 

Once the property was set to a value of "true", the issue no longer occurred.
