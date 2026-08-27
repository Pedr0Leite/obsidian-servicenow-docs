---
title: "Error \"No service-desk processes found for the user selected\" when trying to reset password using Password Reset > Service Desk"
aliases:
  - KB0695237
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695237
kb_number: KB0695237
last_modified: 2024-04-07
---

## Error "No service-desk processes found for the user selected" when trying to reset password using Password Reset > Service Desk

  

### Issue

 For Service Desk password reset, after selecting the user, an error message "No service-desk processes found for the user selected." is displayed on the top

### Release

All

### Cause

Taking OOB 'Default Self Service' process to explain the behavior.

  
1\. The process is marked as public access in Password Reset -> Processes.

2\. When the process is marked as public, you need to directly access the 'Public URL' on the process to reset the password.

### Resolution

1\. If you want to access the process via Service Desk, you need to uncheck the 'public access' box on the process and you should be able to access from service desk.
