---
title: "Issue with the Flow designer not getting/delay in triggering"
aliases:
  - KB0819167
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0819167
kb_number: KB0819167
last_modified: 2026-01-28
---

## Issue with the Flow designer not getting/delay in triggering

  

### Issue

The flow engine is not processing the Updates faster and which results in the delay of updates to the Major Incidents.. In the processing duration for the events in event queue for few incident records. It took so long for processing the updates from flow designer. It’s not expected behavior usually the updates would happen no longer than 60secs.

When it is happening:

It is happening occasionally where the event processor is busy and once the event queue is cleared , the updates are happening to the Incidents.

Requirement:

To run the Flow synchronously for the flow that you have configured on MIM incidents.

### Release

ALL

### Cause

Configuration of "When to run the flow"

### Resolution

The Flow engine can be run synchronously by changing the "When to run the flow" to "Run flow in foreground".  
  
Option Description in the product document :  
  
Run flow in background (default) Flow that runs asynchronously in the background. Use this option for flows that do not require immediate updates and to allow other system processes to run at the same time.  
  
Run flow in foreground Flow that runs synchronously in the current session. Use this option to provide immediate updates to an end user. For example, if a flow opens a task after the previous task closes, use this option to open the next task immediately after a user closes one.  
Note: Running a flow in foreground blocks the current session thread and prevents it from running anything else until the flow finishes. To avoid making your system unresponsive while running a flow, do not use this trigger option for flows that take a long time to complete.  
  
  

### Related Links

Refer the below Flow Designer Document regarding the triggering options.

[CLICK HERE](https://docs.servicenow.com/csh?topicname=flow-triggers.html&version=latest# "CLICK HERE")
