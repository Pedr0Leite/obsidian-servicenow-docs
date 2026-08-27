---
title: "Employee Relations installed but can't find \"Report misconduct\" Catalog Item/Record Producer"
aliases:
  - KB1002176
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1002176
kb_number: KB1002176
last_modified: 2025-09-03
---

## Employee Relations installed but can't find "Report misconduct" Catalog Item/Record Producer

  

### Issue

Employee Relations installed but can't find "Report misconduct" Catalog Item/Record Producer

### Resolution

The Plugin File for the Record Producer "Report misconduct" has a dependency on having the "Employee Service Center" (com.sn\_hr\_service\_portal) Plugin installed as well. Once that is installed, you will be able to use "Report misconduct".  
  
NEXT STEPS:  
  
1\. Install the "Employee Service Center" (com.sn\_hr\_service\_portal) Plugin  
2\. Repair the "Human Resources Scoped App: Employee Relations" (com.sn\_hr\_employee\_relations) Plugin if needed afterwards
