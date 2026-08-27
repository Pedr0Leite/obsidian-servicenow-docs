---
title: "Tasks are created for some RITMs, but not all of them."
aliases:
  - KB0781559
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781559
kb_number: KB0781559
last_modified: 2024-09-20
---

## Tasks are created for some RITMs, but not all of them.

  

### Issue

A single Request was submitted with two child RITMs. One RITM has tasks being successfully created via the workflow. The second RITM, running the same workflow, is not having tasks being created. The user wanted to know why.

### Resolution

The reason the user was seeing the above reported behavior is that they had a "Wait for condition" workflow activity at the start of their RITM workflow. This activity was waiting for the RITM to be approved.  
  
The "Wait for condition" activity is not needed because there is already an Out of Box (OOB) feature which waits for the RITM to be approved.  
  
When a Request (REQ) is approved, only then are workflows even triggered on the Requested Items (RITMs). This "trigger" is the passing of the parent REQ's approval down to the child RITM (or children RITMs) via OOB Business Rule "Cascade Request approval to Requested Item".  
  
It simply does not make sense to use the same condition in the RITM's workflow which is already being executed via the aforementioned Business Rule. Unless the REQ is approved, the RITM workflow will never trigger - therefore, there is no need to wait for approval in an RITM workflow which is already only running if it has approval to run. In other words, the workflow will only ever start if that approval is already there. The check for approvals again in the RITM workflow is unnecessary.  
  
Removing that workflow activity does resolve the behavior.
