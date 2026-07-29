---
title: " Flow takes around 4 minutes in evaluate all \"Wait for condition\" steps"
aliases:
  - KB0958113
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0958113
kb_number: KB0958113
last_modified: 2024-02-27
---

## Issue

Within a flow that works with a Project record, there are a number of "Wait for condition" actions. Some of these are triggered when a Project Task is closed, and are used to change the 'state' of the next Project Task to a 'Work in Progress' state.

With this issue, it was taking approx 4 minutes for the 'state' of the next Project task to be changed to the 'Work in Progress' state.

## Resolution

On this occasion, the trigger on relevant flow 'On Create' from 'On Update', which changed the order the events were created in. This resulted in the 'key' event being processed before the slower events.
