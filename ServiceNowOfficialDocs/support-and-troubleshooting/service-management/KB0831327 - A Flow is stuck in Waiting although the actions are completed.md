---
title: "A Flow is stuck in Waiting although the actions are completed"
aliases:
  - KB0831327
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0831327
kb_number: KB0831327
last_modified: 2024-04-08
---

## A Flow is stuck in Waiting although the actions are completed

  

### Issue

A Flow is stuck in state Waiting but the flow execution doesn't show a step waiting, only complete and not run

### Cause

You need to review the design of the Flow and check if you use any if-statements. A common reason is that a value is the output of a step which isn't always executed because the if-condition isn't met. So if at a later stage you use an action which depends on an input of an earlier action which didn't run, the Flow gets stuck in a Waiting stage.

  

### Resolution

  
  
Need to redesign Flow and ensure there's a valid value for action 'wait for stage'.
