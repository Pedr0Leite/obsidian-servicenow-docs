---
title: "After Submitting a HR case on the Service Portal the HR Case information is not Visible for certain users. Record Not Found"
aliases:
  - KB0786132
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786132
kb_number: KB0786132
last_modified: 2024-04-08
---

## After Submitting a HR case on the Service Portal the HR Case information is not Visible for certain users. Record Not Found

  

### Issue

Submit an HR Case through HR catalog on the ESC portal. After the Case submission, the HR case information is not visible on the portal.  For admins and some users, it is working.

### Release

New York Patch 1 Hot Fix 1a

### Cause

Once the HR case is submitted or while accessing the record from the platform, there is a query Business Rule on customer instance which has a custom script causing the issue.  
https://\*\*\*\*\*\*\*\*.service-now.com/sys\_script.do?sys\_id=1468d300db7844d09cf2553c689619ce&sysparm\_view=&sysparm\_domain=null&sysparm\_domain\_scope=null&sysparm\_record\_row=1&sysparm\_record\_rows=2&sysparm\_record\_list=collection%3dsn\_hr\_core\_case\_total\_rewards%5eORcollectionINsn\_hr\_core\_case\_total\_rewards%2csn\_hr\_core\_case%2ctask%5eaction\_query%3dtrue%5eORDERBYname

### Resolution

After disabling the mentioned Query Business Rule, we could see the user is able to access the HR record.
