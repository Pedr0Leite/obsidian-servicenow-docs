---
title: "hr_admin roled users are unable to Manage the HR Catalog"
aliases:
  - KB0786441
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786441
kb_number: KB0786441
last_modified: 2024-04-08
---

## hr\_admin roled users are unable to Manage the HR Catalog

  

### Issue

According to the attached document, users with hr\_admin role should be able to manage the HR Catalog in the non-scoped version of HR. However, it doesn't seem to be giving them the right access. Users are able to get to the Manage HR Catalog links, but they can't actually see any of the categories and most of the UI Actions are grayed out for them.

### Resolution

\[code\]**Solution:** \[/code\]  
  
hr\_admin roled users are not able to see the catalogs and this is due to a different roles.  
  
The category page is controlled by ACL's and to access that page users should have the role: catalog\_admin.  
This is controlled by this ACL:  
https://<instance\_name>.service-now.com/nav\_to.do?uri=sys\_security\_acl.do?sys\_id=f1adcaa2eb9230003623666cd206fe83  
  
As user does not have this role, the page is being grayed out.  
  
You can either give catalog\_admin role to the user or update the ACL to include hr\_admin role as per your requirement.
