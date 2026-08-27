---
title: "Removal candidates are not getting created as expected based on low usage table for M365"
aliases:
  - KB2576619
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2576619
kb_number: KB2576619
last_modified: 2025-10-24
---

## Removal candidates are not getting created as expected based on low usage table for M365

  

### Issue

The OOB Scheduled job "SAM - Create New Reclamation Candidates for Office 365 Integration" will create removal candidates for M365 products based on low usage.

Customers on Xanadu release may observe that they are missing removal candidates for software that fits the reclamation rule's criteria. This is because reclamation rules creating removal tasks for low usage justification is not supported on this release. You can see this via the below documentation "Reclamation rules for Microsoft 365 integration":  
[https://www.servicenow.com/docs/bundle/yokohama-it-asset-management/page/product/software-asset-management2/reference/m365-reclamation-rules.html](https://www.servicenow.com/docs/bundle/yokohama-it-asset-management/page/product/software-asset-management2/reference/m365-reclamation-rules.html)  
  
From the above documentation, you can see this was recently introduced in Yokohama release (Xanadu documentation notes do not exist for low usage removal candidate generation).

### Release

Xanadu and prior releases

### Resolution

Automatic removal candidate generation is only possible on upgrade to Yokohama or subsequent releases.

For the Microsoft 365 integration, the below products are supported for this feature:  
\[-\] Power BI  
\[-\] Exchange Online  
\[-\] SharePoint Online  
\[-\] OneDrive for Business  
\[-\] Teams  
\[-\] Project Online  
\[-\] Visio Online  
\[-\] Microsoft 365 Copilot
