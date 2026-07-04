---
title: "Unable to add choice type field on Work order templates"
aliases:
  - KB0960738
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0960738
kb_number: KB0960738
last_modified: 2024-10-09
---

## Issue

Unable to add choice type field on Work order templates

Steps to reproduce:

1.  Field Service  Management plugin installed
2.  Open table definition on wm\_task, create new column : Service Type (u\_service\_type)  with Choice type, list few choice in the list.. 
3.  Navigate to Work Order Template and Create New
4.  On Task 1 section, Task type is "Work Order Task", click Edit , to add Service Type.

Expected behaviour : dropdown list is showing up 

Actual behaviour: there is blank on the Service Type , choices can not be selected..

## Resolution

The workaround is provided as below:

-   Modify the column Service Type from Choice type to String.
-   Remain other choice list and setup as it is..

After above changes, the work order template shows the dropdown list as desired.
