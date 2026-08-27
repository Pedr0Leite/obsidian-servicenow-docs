---
title: "Why is there is a delay when a flow is triggered and when it is started?"
aliases:
  - KB0864512
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0864512
kb_number: KB0864512
last_modified: 2025-11-17
---

## Why is there is a delay when a flow is triggered and when it is started?

  

### Issue

A flow triggers on an event, but sometimes it takes up to 10 seconds before the flow eventually start. Why is this and how can this be improved?

### Cause

You can check the timing via the sysevent record. Look for flow.event and check the details. You'll see something like this:

<process\_on>2020-11-13 12:34:58</process\_on>  
<processed>2020-11-13 12:35:09</processed>  
<sys\_created\_on>2020-11-13 12:34:58</sys\_created\_on>

_sys\_created\_on_ and _processed\_on_ are the moment the event was created, _processed_ is the moment the flow is actually started. 

This latency depends on the event delegator which assigns events to nodes and then jobs on those nodes that pick them up. 

  

  

### Resolution

If the flow is configured to run synchronously, it will start automatically as it gets executed on the current user's thread. To do this go to the trigger and change it to run in foreground (by default it's running in the background).
