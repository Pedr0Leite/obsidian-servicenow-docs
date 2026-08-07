---
title: "Flow Designer is in Waiting state even though no action pending in Waiting."
aliases:
  - KB0999355
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0999355
kb_number: KB0999355
last_modified: 2024-10-11
---

## Flow Designer is in Waiting state even though no action pending in Waiting.

  

### Issue

Flow Designer is in Waiting state even though no action is pending in Waiting.

### Cause

The flow execution is stuck in state WAITING because, after the last executed action, the next action needs inputs from previous actions that were skipped.

The next action is dependent on the outputs of the previous actions. However, those previous actions did not run due to surrounding If logic.

If the dependent actions do not execute the flow will continue to remain in the Waiting state only.

### Resolution

Create the flow in a way that the dependent actions always get executed.
