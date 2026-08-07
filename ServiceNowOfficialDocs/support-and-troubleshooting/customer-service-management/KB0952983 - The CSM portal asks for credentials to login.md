---
title: "The CSM portal asks for credentials to login"
aliases:
  - KB0952983
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0952983
kb_number: KB0952983
last_modified: 2024-01-10
---

## The CSM portal asks for credentials to login

  

### Issue

If you open the CSM portal, it will ask you to enter the login details even if you are logged In.  

### Release

Paris

### Cause

Below Templates has been customized:

'spDropdownTreeTemplate':  
/nav\_to.do?uri=sp\_ng\_template.do?sys\_id=492127b05b301200e39fc7ad31f91a50  
  
'menuTemplate':  
/nav\_to.do?uri=sp\_ng\_template.do?sys\_id=1c01e3b05b301200e39fc7ad31f91af7

### Resolution

Revert the templates to OOB to fix the issue.
