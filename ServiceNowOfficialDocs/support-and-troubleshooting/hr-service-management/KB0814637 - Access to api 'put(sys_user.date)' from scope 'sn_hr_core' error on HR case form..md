---
title: "\"Access to api 'put(sys_user.date)' from scope 'sn_hr_core'\" error on HR case form."
aliases:
  - KB0814637
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814637
kb_number: KB0814637
last_modified: 2024-04-08
---

## "Access to api 'put(sys\_user.date)' from scope 'sn\_hr\_core'" error on HR case form.

  

### Issue

While creating HR case from Record producer, below error message pop up . Access to api 'put(sys\_user.date)' from scope 'sn\_hr\_core' has been refused due to the api's cross-scope access policy. 

### Cause

Custom script in date variable.

### Resolution

The behavior seen is due to custom script in default value of date variable

Current script  
javascript: var gdt = new GlideDateTime();  
current.date= gdt.getDisplayValue();  
  
When replicating this issue, we find in the node logs:  
Cannot set property "date" of null to "01-14-2020 09:36:13"  
Caused by error in at line 3  
1:  
2: var gdt = new GlideDateTime();  
\==> 3: current.date= gdt.getDisplayValue();  
  
In this case, current is referencing the user, not the variable. The following script resolves the issue:  
javascript: var gdt = new GlideDateTime();  
gdt.getDisplayValue();
