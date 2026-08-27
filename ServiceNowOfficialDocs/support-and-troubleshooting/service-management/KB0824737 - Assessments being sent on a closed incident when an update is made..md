---
title: "Assessments being sent on a closed incident when an update is made."
aliases:
  - KB0824737
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0824737
kb_number: KB0824737
last_modified: 2024-04-08
---

## Assessments being sent on a closed incident when an update is made.

  

### Issue

Customer experienced a scenario where an assessment was sent on a closed incident that already had an assessment sent.

### Cause

Whenever there is an update on an incident record, even though the update was not a change of state, the 'after' update business rules will run, for example the **Auto assessment** business rule will be executed and if the condition on the trigger matches then it can trigger the survey again. This is expected platform behaviour.

### Resolution

The suggested approach to ensure the trigger conditions only match once, is to use for example,

**State > changes to > Closed** instead of **State > is > Closed**
