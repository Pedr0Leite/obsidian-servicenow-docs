---
title: "Clicking on a record in a list gives a record not found error."
aliases:
  - KB0546729
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0546729
kb_number: KB0546729
last_modified: 2023-10-11
---

## Clicking on a record in a list gives a record not found error.

  

### Issue

When clicking on a record in a list you receive a record not found message instead of being taken to the expected record.

### Cause

The most likely cause for this issue is that there is a dictionary record in the table (or a parent table) that is a reference field but has not table defined in the **Reference** field.

### Resolution

You should be able to correct this issue by reviewing the dictionary for your table and the associated parent tables for any fields that are reference types and have no value. This would mean taking the following steps:

1.  Go to **System Definition > Dictionary**.
2.  Set your filters as follows:
    -   \[Type\] \[is\] \[Reference\]  
        and
    -   \[Reference\] \[is\] \[empty\]

You can also enter the URL directly as follows: `/sys_dictionary_list.do?sysparm_query=internal_type%3DReference%5EreferenceISEMPTY`  
  

If any records are displayed then you should update the **Reference** field with the correct table that the reference should be pointing to.  
  
![](/sys_attachment.do?sys_id=3d4b44024775b1d0f64de825126d4354)

If records were found then correcting them should resolve your issue.
