---
title: "We can set unacceptable State and Substate combination when updating alm_hardware with Easy Import"
aliases:
  - KB1434824
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1434824
kb_number: KB1434824
last_modified: 2026-06-01
---

## We can set unacceptable State and Substate combination when updating alm\_hardware with Easy Import

  

### Summary

When we update the status of the alm\_hardware table with Easy Import, State and Substate that cannot be set manually can be set.

## Steps to Reproduce

  
1\. Set the State and Substate in alm\_hardware.   
  
![](/sys_attachment.do?sys_id=88a7e8aa47443d90f93138ce536d43b8 "State_Substate.png")  
  
2\. Update alm\_hardware State with Easy Import  
  
![](/sys_attachment.do?sys_id=3b97e8aa47443d90f93138ce536d43b1 "Excel_import.png")  
  
3\. Only the State is updated, and State and Substate that cannot be set manually can be set.  
  
![](/sys_attachment.do?sys_id=84a7e8aa47443d90f93138ce536d43b6 "State_Change.png")  
  
If I try to create a new record on alm\_hardware table then I cannot select available for "Lost" as Substate.  
  
![](/sys_attachment.do?sys_id=80a7e8aa47443d90f93138ce536d43b4 "new.png")  
  

## Resolution

This behavior is working as expected.

The acceptable Substate values depends on the state, but easy import does not support this. On the form, there are many client scripts and UI policies that manipulate Substate.

When I go to the form for a record of the table where the issue occurs, one choice field's value affects what values are valid for another field. This is done with lots of client side scripting on the form. For some values of the first field, it will even set the second field to have no value and not be editable. On the simple import side, we put the records from any table into a spread sheet, allow the user to download the spread sheet, which they then change and resubmit as an import which applies the changes to the spread sheet to the table they were taken from. For choice fields, the spread sheet is restricted to any choice for that field (excel support a drop-down of choices for a cell, and that's what we use). We can't embed client side scripts run on a web browser into a spread sheet, so any such scripting is not included, and more importantly can't be included.

### Release

Any
