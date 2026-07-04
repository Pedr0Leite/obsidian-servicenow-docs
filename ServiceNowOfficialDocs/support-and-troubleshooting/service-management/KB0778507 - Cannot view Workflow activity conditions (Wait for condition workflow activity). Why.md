---
title: "Cannot view Workflow activity conditions (\"Wait for condition\" workflow activity). Why?"
aliases:
  - KB0778507
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778507
kb_number: KB0778507
last_modified: 2026-04-17
---

## Cannot view Workflow activity conditions ("Wait for condition" workflow activity). Why?

  

### Issue

When attempting to edit a "Wait for condition" activity in the Workflow editor, the conditions are hidden for a user. When other users impersonate that same user, they can see the conditions. Why is this?

### Cause

The user had personalized the Diagrammer view (which displays when viewing the workflow editor) for the workflow activity "Wait for condition".

### Resolution

Some time ago, the user had personalized this form using the slider icon ("Personalize Form"). To find this slider (it looks like an abacus), navigate to the affected record outside of the workflow editor and, in the top right, look for three stacked lines with circles in the lines. Clicking into this reveals that the following three Form Fields have been unchecked:

-   -   -   script\_condition
        -   Condition
        -   wait\_for\_condition

To remedy the behavior, kindly check each of those three boxes and save the changes. The form will now display per the user's expectation.
