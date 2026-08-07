---
title: "Workflow timer is not taking the updated date/time value. Why?"
aliases:
  - KB0783796
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783796
kb_number: KB0783796
last_modified: 2024-09-20
---

## Workflow timer is not taking the updated date/time value. Why?

  

### Issue

A user has a RITM, where on the RITM there is a workflow. Within that workflow, the user has a Timer activity based on a date/time field. After updating the date/time field, the workflow timer seems to be using the previous (original) date/time, and not the updated time.

### Resolution

Here is the premise: when a user creates a RITM, they are setting a date/time field set to a certain value. The associated workflow on the RITM is using the value stored in the date/time field for a Timer activity within the workflow.  
  
The issue the user is seeing is that when they update the value in the date/time field ( _when the Timer activity which is based on that time value is already executing_ ), that is not being reflected in the workflow.  
  
This behavior is expected when the condition in that red text is met. When the RITM is created and that date/time field is given a value, the user has up until the workflow activity which is based on that timestamp executes to change it.

If the user attempts to change the timestamp value after the activity has already begun executing, this will not work. The workflow will take the original value and operate off of that.
