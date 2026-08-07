---
title: "LDAP Import Mapping to Sys_ID"
aliases:
  - KB0790011
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790011
kb_number: KB0790011
last_modified: 2024-04-08
---

## LDAP Import Mapping to Sys\_ID

  

### Issue

LDAP Import randomly assigning users information to the wrong people in the sys\_users table.

### Cause

ServiceNow generates the sys\_ids. When imports maps to that field it update the system SysID created by system. The data change the value of that record. 

### Resolution

Check the transform map to see which data source field is being mapped to sys\_ID

1.  Open import set table to list view  
    1.  filter the list where target record, and a unique field that shows the difference between the import data and target record.

           2. Open user records on the sys\_user

                     a.check sys\_id of the user versus the imported data sys\_id

To fix this issue open the "sys\_transform\_entry" and delete that custom field that is being mapped to the sys\_ID.
