---
title: "Attachments are showing as Null when first attached to a record"
aliases:
  - KB0760215
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0760215
kb_number: KB0760215
last_modified: 2024-04-19
---

## Attachments are showing as Null when first attached to a record

  

### Issue

When a file is attached to any form, irrespective of the file name, it is showing the attachment name as null within the manage attachment popup as well as on the form(initially).

![](sys_attachment.do?sys_id=d0af539fdb23b708f7fca851ca9619c8)

After reloading the form, attached filename shows up correctly.

### Cause

The issue may occur if there is a "gr" variable being used (that is not wrapped in a function) within an ACL on the sys\_attachment table or on the affected table (e.g. incident, change etc.).

This conflicts with the attachment code which uses a gr variable as well. 

### Resolution

Change the variable name from 'gr' to any nonreserved(not used by the system at the backend) word.  
  

Note: As a best practice, do not use "gr" are your glide record variable. Make a custom variable name that you know will not be in the system or wrap your script in a function and then that gr variable will not impact others.
