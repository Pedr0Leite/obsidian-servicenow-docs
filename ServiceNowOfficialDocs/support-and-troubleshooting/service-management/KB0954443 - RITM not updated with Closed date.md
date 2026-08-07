---
title: "RITM not updated with Closed date"
aliases:
  - KB0954443
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0954443
kb_number: KB0954443
last_modified: 2025-07-23
---

## RITM not updated with Closed date

  

### Issue

RITM in the closed state not updated with Closed date

### Cause

In the Audit history, the Active field is not getting updated with Active=False, when the request is marked as Closed.  
Due to this, on closing the requested item, the date and time of change closure is not getting updated under the field "Closed at" and it remains blank.  
  
While checking the XML of the record could see that false  
  
The BR "Set Closure Fields" is not getting triggered because of the condition not satisfied: Condition: current.active.changesTo(false)  
  
The BR "Set Closure Fields" runs after the BR "mark closed" which updates the closure fields after the state of the task is made Inactive.

### Resolution

Below OOB Business rules are not activated. Please activate these business rules which will set the Active to false once the RITM stage is set to Completed.

-   Set Active Flag After Workflows
-   Set Closure Fields After Workflows
