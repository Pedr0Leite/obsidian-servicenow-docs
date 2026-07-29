---
title: "Case Creation Page give generic {{errorMessage}} message on load."
aliases:
  - KB0998867
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0998867
kb_number: KB0998867
last_modified: 2024-10-02
---

## Case Creation Page give generic {{errorMessage}} message on load.

  

### Issue

Case Creation Page give generic {{errorMessage}} message on load.

### Cause

Custom invalid table that extended HR Case

### Resolution

1\.    Navigate to "sys\_properties.LIST"  
2\.    In the "Name" column search for "sn\_hr\_core.inactive\_tables" and go to the record  
3\.    Add the custom table name to the end preceded by a comma if needed. Keep it like this until the custom table is fixed  
4\.    Save the form
