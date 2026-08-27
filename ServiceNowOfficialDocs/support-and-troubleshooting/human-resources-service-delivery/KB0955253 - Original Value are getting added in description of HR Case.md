---
title: "\"Original Value\" are getting added in description of HR Case"
aliases:
  - KB0955253
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0955253
kb_number: KB0955253
last_modified: 2025-07-08
---

## "Original Value" are getting added in description of HR Case

  

### Issue

"Original Value" are getting added in the HR employee relation Case Description when created from Record Producer

![](/sys_attachment.do?sys_id=d1eca7fc930db190057c7de86cba1017)

### Cause

Original Value are getting populated from OOB record producers such as "Employee Profile Update" to show original values from User or HR Profile tables for matching variable names.

This is expected behaviour and is found in the script include: **hr\_CaseUtils**

**https://<<instance name>>.servicenow.com[/](https://support.servicenow.com/)sys\_script\_include.do?sys\_id=24c782869f202200d9011977677fcf89**

### Resolution

-   Avoid using similar variable names that is being used in a Record Producer.
-   The code from "\_getDescriptionFromAnswers" function in the hr\_CaseUtils script include can be removed or commented out if there is a need to hide display original values (from User or HR Profile table for the matching variable names) along with submitted values.  See code below:  
     
    
    if ((originalValue || originalDisplayValue) && !this.\_requiresUserOrProfileCreation.hasOwnProperty(hrServiceValue)) {
    
    var txt = gs.getMessage(' (original value: {0})', originalDisplayValue);
    
    filledValues += txt;
    
    }
