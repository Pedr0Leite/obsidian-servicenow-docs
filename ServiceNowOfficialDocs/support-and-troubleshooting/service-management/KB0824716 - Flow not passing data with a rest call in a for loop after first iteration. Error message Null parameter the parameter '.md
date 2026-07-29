---
title: "Flow not passing data with a rest call in a for loop after first iteration. Error message:: Null parameter: the parameter '<variable name here>' cannot be null"
aliases:
  - KB0824716
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0824716
kb_number: KB0824716
last_modified: 2024-04-08
---

## Flow not passing data with a rest call in a for loop after first iteration. Error message:: Null parameter: the parameter '' cannot be null

  

### Issue

A flow has a foreach (for loop) action that performs rest api actions.

The foreach action gets its information from a lookup records. It should take that data and send it to an action inside the loop. This action has a rest call.

It works on the first iteration, but does not work on subsequent iterations saying "Null parameter: the parameter '<variable name here>' cannot be null" in the runtime

  

### Resolution

In the flow in flow designer

Add a "Wait for Duration" inside the foreach before the action that makes the rest call. The duration can be 1 or even 0 seconds.
