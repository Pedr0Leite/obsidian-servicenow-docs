---
title: "Customer renamed their instance and cannot login afterwards"
aliases:
  - KB0815424
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815424
kb_number: KB0815424
last_modified: 2026-06-30
---

## Customer renamed their instance and cannot login afterwards

  

### Issue

Customer reported that they have renamed their instance and no user can login after that. When trying to access their instance in browser they are getting redirected to an incorrect ServiceNow instance and end up with below screen. Let's consider below example scenario for better understanding:

Instance's old name was: **https://oldname.service-now.com** 

Renamed as: **https://newname.service-now.com**

Getting redirected to: **https://unknown.service-now.com**

![This site can't be reached](sys_attachment.do?sys_id=e9a87ea547f9c7583542f24c736d43bf "This site can't be reached")

### Release

All

### Cause

The issue has no relation with instance renaming process and is caused by incorrect SSO configurations which includes **https://unknown.service-now.com** in below properties on Identity Provider record:

![](sys_attachment.do?sys_id=a5a8bea547f9c7583542f24c736d4335)

### Resolution

Correct these SSO configurations with the name of your ServiceNow instance and SSO login works again.

### Related Links
