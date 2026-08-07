---
title: "Resolve error of nonexistent or unreadable record in table in Flow Designer"
aliases:
  - KB0952921
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0952921
kb_number: KB0952921
last_modified: 2025-10-14
---

## Resolve error of nonexistent or unreadable record in table in Flow Designer

  

### Issue

When running a flow as an input of an action or step, you may see the following error: "Record in sc\_task table does not exist or is unreadable"

### Release

Any supported release

### Cause

The error usually happens on an input of an action or step. A common scenario involves creating a record in one step and using it in a subsequent step.

For example, if you create an sc\_task record in step 1 and use it in a wait-for-condition in step 2, the error can appear in step 2. This happens when:

1.  The record is invalid or doesn't exist.
2.  The output type from the first step (for example, Reference) doesn't match the expected input type of the second step (for example, String).

The Flow Designer UI may not detect this mismatch during configuration. For example:

  
var sc\_task = new GlideRecord('sc\_task');  
...  
var task1 = sc\_task.insert().toString();  
...  
outputs.var1 = task1;

If var1 is a Reference, the UI accepts this configuration without error. However, when the flow runs, step 2 expects a Reference but receives a String, triggering the error. 

### Resolution

To resolve this error, verify that you pass a valid record with the correct data type. For example, the correct code should be:  
  
var sc\_task = new GlideRecord('sc\_task');  
...  
sc\_task.insert();  
...  
outputs.sc\_task\_sys\_id = sc\_task;  
  
This solution passes the GlideRecord object directly, which is compatible with the Reference type, rather than converting it to a String.
