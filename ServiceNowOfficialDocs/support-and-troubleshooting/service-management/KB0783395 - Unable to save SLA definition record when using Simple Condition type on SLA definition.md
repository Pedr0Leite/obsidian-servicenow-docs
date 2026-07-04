---
title: "Unable to save  SLA definition record when using Simple Condition type on SLA definition"
aliases:
  - KB0783395
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783395
kb_number: KB0783395
last_modified: 2024-04-08
---

## Unable to save SLA definition record when using Simple Condition type on SLA definition

  

### Issue

  
  
It is not possible to use Simple Condition type on SLA definition  
  
You have tried to create a SLA definition with "Simple", this causes errors that makes impossible to use the Simple Condition type.  
  
You would like to use the Simple Condition type because you would like always to have an SLA attached, even if Stop condition is met at the same time as the Start condition.

  
Steps to reproduce:  
1\. Create new SLA definition  
2\. Set "Condition type" = Simple  
3\. Error at "When to cancel" and "When to resume"

### Cause

  
  
In customers instance, we could see that in the given sla definition they had the settings below  
  
In the Start Condition  
when to cancel: Never  
  
In Pause Condition  
when to resume: resume conditions are met  
  
With above settings the issue is reproduced.

However as per design When to resume / When to cancel conditions cannot be used when the condition type is set to Simple.

### Resolution

  
  
The definitions have to be defined so that only start and pause conditions are evaluated.  
  
Modifying it as below, will allow the Simple Condition rule to be saved on an Sla definition.  
  
In the Start Condition  
when to cancel: Start Conditions are not met  
  
In Pause Condition  
when to resume: Pause Conditions are met  
  
With the settings above on the provided sla definition, the sla definition was  updated and saved.
