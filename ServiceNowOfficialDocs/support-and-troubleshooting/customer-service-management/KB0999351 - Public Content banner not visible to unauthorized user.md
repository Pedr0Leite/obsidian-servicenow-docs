---
title: "Public Content banner not visible to unauthorized user"
aliases:
  - KB0999351
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0999351
kb_number: KB0999351
last_modified: 2026-06-11
---

## Public Content banner not visible to unauthorized user

  

### Issue

Public Content banner not visible to unauthorized user

### Release

N/A

### Resolution

Welcome Banner content doesn't show up for unauthorized user as per out of the box design.  
  
The recommended fix is,  
1\. Create an audience record with the condition – user id is guest. Please find attached screenshot.  
2\. Add a schedule content for the newly created audience  
https://docs.servicenow.com/bundle/rome-employee-service-management/page/product/employee-center/task/ecpro-schedule-content.html  
  
Hope this helps!
