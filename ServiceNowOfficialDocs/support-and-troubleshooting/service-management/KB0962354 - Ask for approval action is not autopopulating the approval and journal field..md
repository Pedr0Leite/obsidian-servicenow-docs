---
title: "Ask for approval action is not autopopulating the approval and journal field."
aliases:
  - KB0962354
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0962354
kb_number: KB0962354
last_modified: 2024-04-23
---

## Ask for approval action is not autopopulating the approval and journal field.

  

### Issue

Flow Designer lets process owners use natural language to automate approvals, tasks, notifications, and record operations without coding.  
There is an ask for approval action where the approval and journal fields would be auto populated but the issue here is these fields are not being auto populated for few tables.  

Steps to reproduce:  
1.Open the flow designer.  
2.Create a new flow.  
3.Select the trigger as a knowledge table.  
4.Now configure the ask for approval action and select the record as trigger record in step3.  
5.Check the approval and journal fields are not autopopulated.

### Cause

We tried replicating the behaviour and found that the behaviour is the same in Out of Box as well.  
The issue is present only for the tables that are not containing the approval and journal fields.

### Resolution

We have checked and found that it is expected behavior.  
It is expected behaviour because the autocomplete only works if the table has the Approval and Journal fields.
