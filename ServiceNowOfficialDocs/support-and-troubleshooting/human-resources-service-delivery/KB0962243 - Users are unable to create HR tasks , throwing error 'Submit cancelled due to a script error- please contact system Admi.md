---
title: "Users are unable to create HR tasks , throwing error '\"Submit cancelled due to a script error- please contact system Administrator\"
aliases:
  - KB0962243
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0962243
kb_number: KB0962243
last_modified: 2025-09-03
---

## Users are unable to create HR tasks , throwing error '"Submit cancelled due to a script error- please contact system Administrator"

  

### Issue

Issue : When user is trying to create HR tasks , it not submitting the form and throwing error ""Submit cancelled due to a script error- please contact system Administrator"  
  
  

### Cause

Cause: Prevent use of docusign task template

Link: https://XXXXXX.service-now.com/sys\_script\_client.do?sys\_id=d429315277063300a629aed7c810618c

### Resolution

Client script is causing the issue "Prevent use of docusign task template"

Client script was not submitting the form - 

"template" field was not added to form layout due to which below code line from client script was causing this Issue - "Prevent use of docusign task template" -  
  
Code - g\_form.getDisplayBox('template').value == 'Docusign Task Template'  
  
As this field is not visible on the form so it's returning an undefined value.  
  
The issue will be resolved by adding this field on form layout
