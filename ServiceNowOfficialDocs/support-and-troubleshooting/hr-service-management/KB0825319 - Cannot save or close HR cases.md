---
title: "Cannot save or close HR cases"
aliases:
  - KB0825319
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0825319
kb_number: KB0825319
last_modified: 2025-09-03
---

## Cannot save or close HR cases

  

### Issue

Cannot save or close HR cases. Below error message:

onSubmit script error: TypeError: Cannot read property 'display' of undefined: function() { saveAllSelected(\[ gel(id) \], \[ gel(ref) \], ',', '\\\\', '--None--'); }

### Release

Any

### Cause

This can be caused by duplicate variables on the form

Usually caused by a custom widget or business rule and scripts

### Resolution

1) Check the variables on the form if duplicated.

2) Remove the variable editor on the form 

How to Configure Form: [https://docs.servicenow.com/csh?topicname=configure-form-layout.html&version=latest](https://docs.servicenow.com/csh?topicname=configure-form-layout.html&version=latest)

OR

1) Remove duplicate variables by going to the \[question\_answer\] table - [https://<instance\_name>.service-now.com/question\_answer\_list.do](https://\<instance_name\>.service-now.com/question_answer_list.do)

\* This table is where the submitted Record producer variables are stored

2) Filter table\_sys\_id=<record\_sys\_id>

3) Check if there are duplicate variables and remove the duplicates in this table

If you are encountering the issue on REQ/RITM/SCTASK, the variable submitted are stored in the tables \[sc\_item\_option\_mtom\] and \[sc\_item\_option\], so you can check these tables and remove the duplicates here instead
