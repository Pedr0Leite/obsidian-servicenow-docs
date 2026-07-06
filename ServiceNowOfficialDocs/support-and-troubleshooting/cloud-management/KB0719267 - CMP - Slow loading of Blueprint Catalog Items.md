---
title: "CMP - Slow loading of Blueprint Catalog Items"
aliases:
  - KB0719267
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0719267
kb_number: KB0719267
last_modified: 2024-04-07
---

## CMP - Slow loading of Blueprint Catalog Items

  

### Issue

When attempting to load a Blueprint catalog item, you note that it takes several minutes for the form to properly load, even though there are no errors and Dev Console logs seem to indicate that variables are slowly being populated.

#   

### Release

All

### Resolution

If there are no errors, the most likely cause is that one of the variables is loading an excessive amount of records. Example:

By default, ApplicationPool for Application variable pulls "All" records from cmdb\_ci\_appl. If this table has a high quantity of records, the catalog item loading performance will be impacted as the system is trying to render all those records options into the drop down menu for the variable.

Be sure to check the variables and Resource Pool filters to validate whether the drop down menus are attempting to render and populate a reasonable number of options. Even just 100+ records will have a noticeable impact on loading performance. 

#
