---
title: "Creating an event to trigger flow is not working"
aliases:
  - KB0960053
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0960053
kb_number: KB0960053
last_modified: 2025-10-20
---

## Creating an event to trigger flow is not working

  

### Issue

Flows do not get triggered when an event is created from background scripts using the `gs.eventQueue()` API.

### Steps to Reproduce**:**

1.Create a Flow on the sysevent table with a condition where the event name equals "Test" — this Flow should trigger when the event occurs.

2.From a background script, generate the event using the gs.eventQueue() API.  
The Flow does not trigger.

3.However, if the event is created using GlideRecord, the Flow does trigger.

Working one :

  
var gr = new GlideRecord("sysevent");  
gr.initialize();  
gr.name = "Test";  
gr.parm1 ="Random";  
gr.parm2 ="testing";  
gr.insert();

Non working one: 

  
gs.eventQueue("Test", null , "Random", "testing");

### Release

Applicable to all releases

### Cause

### Root Cause

The `gs.eventQueue()` method internally uses `setWorkflow(false)` when creating events.  
Starting with the Paris release, this behavior changed — when `setWorkflow(false)` is applied, the Flow Engine does not run.

### Resolution

To restore the previous behavior and allow Flows to trigger for events created using the gs.eventQueue() API:

1.Create a new system property:  
Name: trigger\_engine.ignore.set\_workflow  
Type: Boolean  
Value: true

This enables the Flow Engine to trigger even when setWorkflow(false) is set internally.
