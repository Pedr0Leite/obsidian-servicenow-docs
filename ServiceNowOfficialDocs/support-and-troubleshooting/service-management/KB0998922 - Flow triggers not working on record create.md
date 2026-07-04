---
title: "Flow triggers not working on record create"
aliases:
  - KB0998922
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0998922
kb_number: KB0998922
last_modified: 2024-10-03
---

## Flow triggers not working on record create

  

### Issue

When a record is created that has a flow with a created or updated trigger, even though the trigger conditions are met, the flow does not start.  
  
It does start on when the record is updated.  
  
There are no flow.fire events created on create but there are on update.

### Cause

Any business rules with "SetWorkflow(false)" - will prevent other business rules and engines from executing, including flow designer.

Hence when you are inserting a record into the table even though flow conditions are matched, flow didn't get executed.

### Resolution

kindly please remove the line current.setWorkflow(false); from the business rules to resolve the issue
