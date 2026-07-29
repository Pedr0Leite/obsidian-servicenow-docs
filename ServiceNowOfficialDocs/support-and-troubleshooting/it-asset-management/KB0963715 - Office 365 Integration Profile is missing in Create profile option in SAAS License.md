---
title: "Office 365 Integration Profile is missing in Create profile option in SAAS License"
aliases:
  - KB0963715
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0963715
kb_number: KB0963715
last_modified: 2026-06-19
---

## Office 365 Integration Profile is missing in Create profile option in SAAS License

  

### Issue

While trying to Create a Microsoft Office 365 integration profile to download subscription information for compliance, we cannot able to Select Office 365 Integration Profile by navigating to

SaaS License > Administration > Direct Integration Profiles and then click New.  
https://docs.servicenow.com/bundle/paris-it-asset-management/page/product/software-asset-management2/task/set-up-microsoft-office-365.html  
  
  

![](sys_attachment.do?sys_id=c4b8851c478ff91411eaf24c736d4321)

### Release

All

### Cause

The reason for it not being visible is that active value is false in sys\_wizard\_answer for "Office 365 Integration Profile".

[https://instanename.service-now.com/nav\_to.do?uri=sys\_wizard\_answer.do?sys\_id=43f65d6173630300759a259dfaf6a7b1%26sysparm\_view=wizardsimple](https://instanename.service-now.com/nav_to.do?uri=sys_wizard_answer.do?sys_id=43f65d6173630300759a259dfaf6a7b1%26sysparm_view=wizardsimple)

![](sys_attachment.do?sys_id=88b8851c478ff91411eaf24c736d4324)

### Resolution

1) Navigate to sys\_wizard\_answer record for "Office 365 Integration Profile" by accessing the below link.  
[https://instancename.service-now.com/nav\_to.do?uri=sys\_wizard\_answer.do?sys\_id=43f65d6173630300759a259dfaf6a7b1%26sysparm\_view=wizardsimple](https://instancename.service-now.com/nav_to.do?uri=sys_wizard_answer.do?sys_id=43f65d6173630300759a259dfaf6a7b1%26sysparm_view=wizardsimple)

  
2) Please enable the ACTIVE tab and save

  
3) Now you can see the "Office 365 Integration Profile" under SaaS License > Administration > Direct Integration Profiles >> New

### Related Links

The active value should have been ideally set to true via a fix script when the plugin (com.snc.samp.microsoft) was activated.
