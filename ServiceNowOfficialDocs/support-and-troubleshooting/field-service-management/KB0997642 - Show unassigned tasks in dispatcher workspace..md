---
title: "Show unassigned tasks in dispatcher workspace."
aliases:
  - KB0997642
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0997642
kb_number: KB0997642
last_modified: 2024-08-28
---

## Issue

Requirement was to show those tasks in dispatcher workspace which are unassigned by the dispatcher in dispatcher workspace.  
To implement this requirement a custom field "unassigned" was created and added as a  checkbox in work order task form(wm\_task table) and a BR was created   This solution is working actually but not in the dispatcher workspace. This custom business rule is working on the form layout of the work order task but if they try to unassign the task from dispatcher workspace then this is not working.  
How to make this configuration work on dispatcher workspace?

## Resolution

For dispatcher workspace, you need to make change on this client script: **sys\_ux\_client\_script\_3389fdfb71131010f87784d70d5e4dd3.xml** (**Calendar Event Popover Overflow Handler**)

in this block:

**_}else if (event.payload.payload.action.id == 'dropdownItem\_unassign\_wot') {_**  
  
**_change updateRecord('wm\_task', event.payload.context.sysId, "assigned\_to=''", false);_**

to

**_`updateRecord('wm_task', event.payload.context.sysId, "work_notes='unassigned'^u_unassigned=true^assigned_to=''", false);`_**

Note : assuming the column name for unassigned in your wm\_task table is 'u\_unassigned' instead of 'unassigned'.

For future change in dispatcher workspace, please look into script in **'sys\_ux\_client\_script**' table. Dispatcher workspace do not share client script with the platform.

Our dev made the following changes in your instance:

**There's no limitation on using BR.** In this case, the miss was that we did not modify code in the correct script.
