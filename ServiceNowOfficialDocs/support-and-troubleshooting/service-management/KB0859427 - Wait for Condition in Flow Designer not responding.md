---
title: "Wait for Condition in Flow Designer not responding"
aliases:
  - KB0859427
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0859427
kb_number: KB0859427
last_modified: 2025-05-15
---

## Wait for Condition in Flow Designer not responding

  

### Issue

A flow on a requested item gets stuck on a wait for condition on a field on the record. There are subsequent steps in the flow that affect requested items on the same request. These include adding an 'ask for approval' and an update record on those other items. Some of the items have their own flow and some of the items have their own workflow.

Incorrect value on the field in the runtime value of the flow execution may also be noticed. For example, the state on the RITM is a value of '2' but the runtime value shows '3'.

### Cause

A record is not getting created on the \[sys\_rw\_action\] table, so the flow does not 'wake up' when the state is changed.

### Resolution

In this case, moving the actions in the flow that related to other RITMs to a separate subflow can resolve the issue.

### Related Links

[KB0955312 Flow is in "waiting" state even though approval or wait for condition has been satisfied](https://support.servicenow.com/kb_view.do?sysparm_article=KB0955312 "Flow is in \"waiting\" state even though approval or wait for condition has been satisfied")
