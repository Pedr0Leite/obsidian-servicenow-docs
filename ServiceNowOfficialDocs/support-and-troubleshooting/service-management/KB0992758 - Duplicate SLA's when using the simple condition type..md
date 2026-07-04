---
title: "Duplicate SLA's when using the \"simple\" condition type."
aliases:
  - KB0992758
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0992758
kb_number: KB0992758
last_modified: 2026-06-24
---

## Duplicate SLA's when using the "simple" condition type.

  

### Issue

You have reported an issue with the use of the "simple" condition type.

You have a requirement to allow response slas to attach even if stop condition is met at the same time.  
This works, but you have noticed it is now creating duplicate response SLA's rather than just one.

Question: Why do you have multiple response slas attached?

### Release

All

### Cause

  
Having more than one sla when using the "simple" condition type is not unknown and can occur based on it's design.  
  
Explanation:  
This is expected behavior with using the Simple Condition Type. It is possible to have multiple slas of the same definition attaching, but these will not be created at the same time, so they are not duplicates.  
  
When using the Simple condition type, Task SLA records will only attach when the Start conditions match. However if the Stop Conditions match when a Task SLA is being attached, the Task SLA is still processed but it completes immediately.  
Based on this explanation, this means that once the initial task sla has attached and completed, any subsequent update to the Task record will execute the 'after update' Run Slas BR's.  
Assuming the Start conditions on your Sla definition still match, it will again reprocess and attach a new Sla however as stop condition is matched at this time then it completes it immediately.  
This will continue to occur through the life of the Task.  
  
On the other hand with the Default SlaConditionBase, this will check the stop condition at the time it is processing the new sla and if it finds that stop condition has already been met it will NOT bother to attach the sla.

### Resolution

  
The reported behavior is a possible feature of using the "simple" condition type.  
  
When using the "simple" condition type, if you would only want the Sla to attach once after stop condition has been met you need to design your sla definition to meet this requirement.  
  
So for e.g. you can include an additional criteria in your start condition that basically checks stop condition has been met once.
