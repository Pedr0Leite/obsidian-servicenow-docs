---
title: "RITM is not transitioning Stages correctly."
aliases:
  - KB0781007
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781007
kb_number: KB0781007
last_modified: 2024-09-20
---

## RITM is not transitioning Stages correctly.

  

### Issue

On the user's Catalog Item "Quarterly polishing of Mjölner", the Stage is not transitioning to "Completed" even though the RITM is in a State of "Closed Complete". The user wanted to know this is happening.

### Resolution

After an in-depth investigation, it was found that the reason the workflow on Catalog Item "Quarterly polishing of Mjölner" was not progressing properly (and thus, setting correct Stage values -- the activity which set the Stage to "Complete" is later in the workflow) was because of "Run Script" workflow activity had an erroneous condition on it.

The "Run Script" workflow activity had a "Success" condition where the "Condition" field was set to "activity.result === 'success'". This is not correct.  
  
Changing the condition to "activity.result == 'success'" resolves the issue, and the Workflow progresses properly on the RITM, allowing the next activity to fire which has the Stage value of "Complete" set on it.  
  
Furthermore, all Out of Box (OOB) workflow conditions are with two '=' signs, never three. Please use only two (e.g. '==').
