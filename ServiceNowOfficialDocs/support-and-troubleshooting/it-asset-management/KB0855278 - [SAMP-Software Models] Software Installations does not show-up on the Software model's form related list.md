---
title: "[SAMP-Software Models] Software Installations does not show-up on the Software model's form related list"
aliases:
  - KB0855278
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0855278
kb_number: KB0855278
last_modified: 2024-04-08
---

## \[SAMP-Software Models\] Software Installations does not show-up on the Software model's form related list

  

### Issue

On the software model form, under the related list the "Software Installations" tab no records showing up. Even though there are software installations exists for the same software model.

![](/sys_attachment.do?sys_id=752cf4c9db04f4d04cfbeeb5ca96192d)

### Cause

There are at-least two related tables with same label "Software Installations" one from "Software Model" and other with "Inferred Suite". Might be the incorrect referenced table added in related list. 

Software Installations > Software Model . (correct one)

Software Installations > Inferred Suite (incorrect one)

### Resolution

Configure the form layout and select the right table.  
On the Software model form >> Right click on header >> Related Lists >> Select the tables you would like to choose here "_Software Installations > Software Model_".

![](/sys_attachment.do?sys_id=712cf4c9db04f4d04cfbeeb5ca96192b)

  

![](/sys_attachment.do?sys_id=f92cf4c9db04f4d04cfbeeb5ca96192e)
