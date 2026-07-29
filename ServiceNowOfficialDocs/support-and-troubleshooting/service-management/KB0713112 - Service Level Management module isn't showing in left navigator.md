---
title: "Service Level Management module isn't showing in left navigator"
aliases:
  - KB0713112
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713112
kb_number: KB0713112
last_modified: 2024-04-07
---

## Service Level Management module isn't showing in left navigator

  

### Issue

Even with the Service level management plugin (com.snc.sla) enabled, searching for "Service Level Management" in the left navigator does not display the Service Level Management module. 

### Release

Kingston +

### Cause

The Service Level Management module is inactive (meaning that it will not display).

### Resolution

To display the Service Level Management module:

1.  Navigate to the Application Menus table and search for the 'Service Level Management' record
2.  Open the record
3.  Select/check the 'Active' box
4.  Save/Update

(ref: /nav\_to.do?uri=sys\_app\_application.do?sys\_id=d8b260d20a0003a400d36c825eca3372 )

Note: Should you see any modules not displaying, you may also check their active status as well
