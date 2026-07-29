---
title: "Variable editor in agent workspace show announcements that are not made portal specific"
aliases:
  - KB0816062
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0816062
kb_number: KB0816062
last_modified: 2024-04-08
---

## Variable editor in agent workspace show announcements that are not made portal specific

  

### Issue

Variable editor in agent workspace show announcements that are not made portal specific.

Steps to Reproduce:

1\. Add variable editor to the incident form on workspace view  
2\. Create an announcement and do not make it portal specific  
3\. Create an incident using record producer so that it shows variables on variable editor  
4\. Open this new incident in agent workspace > click on variable editor

Notice that announcement shows on the top of the pop-up as shown in below screenshot:

![](/sys_attachment.do?sys_id=b4cfac4ddb88b4d0471f9c41ba961975)  
Expected: it should not show announcement on the variable editor in agent workspace

### Release

Madrid, New York

### Cause

Portal page is used to display the variable editor.

The URL looks like: [https://<instance\_name>.service-now.com/swp?id=variable\_editor&sys\_id=<sys\_id>&table=<table\_name>](https://kyribadev.service-now.com/swp?id=variable_editor&sys_id=5ec9ee37db43c8104efc2a9b8a9619ff&table=sn_customerservice_case)

### Resolution

Please make the announcement portal specific to make it not show up on swp portal while it displays variable editor.  
  
The table that holds the m2m mapping for an announcement to the portal is "m2m\_announcement\_portal". Hence, if you make an entry on that table to display only for a specific portal such that it excludes for swp portal, it will not show that announcement on the agent workspace variable editor pop-up.   
  

### Related Links

The variable editor in workspace is moved to native form in Orlando.  
The temporary portal page is no more in the product. Hence this behavior can not be reproduced post New York.
