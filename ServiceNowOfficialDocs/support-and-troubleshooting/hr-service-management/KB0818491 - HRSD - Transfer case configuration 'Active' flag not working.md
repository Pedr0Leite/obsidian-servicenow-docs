---
title: "HRSD - Transfer case configuration 'Active' flag not working"
aliases:
  - KB0818491
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818491
kb_number: KB0818491
last_modified: 2025-09-03
---

## HRSD - Transfer case configuration 'Active' flag not working

  

### Issue

How to remove option 'Transfer to a new case number' option in 'Transfer case' the popup window ?

### Resolution

1.  Navigate as HR Admin to /sn\_hr\_core\_transfer\_case\_config\_list.do?sysparm\_query=&sysparm\_view=
2.  You will see 2 records there.
3.  Pick up the one which says "standard" and set Active = False for it.
4.  `Open record "Reclassify" and set it to default` .
5.  save and test

          ![](/sys_attachment.do?sys_id=83c46809db4cb4d04cfbeeb5ca961958)
