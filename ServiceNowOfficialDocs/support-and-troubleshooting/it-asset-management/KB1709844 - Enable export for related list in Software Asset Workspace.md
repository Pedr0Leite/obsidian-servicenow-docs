---
title: "Enable export for related list in Software Asset Workspace"
aliases:
  - KB1709844
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1709844
kb_number: KB1709844
last_modified: 2025-05-06
---

## Enable export for related list in Software Asset Workspace

  

Support for exporting related list in SAM workspace was added in Xanadu release.  
To enable this functionality in pre Xanadu instances, please make following changes:  
  
1\. Navigate to Now Experience Framework -> Declarative Actions -> Related List Actions  
Search record with sys\_id '7f77b68c2dc32010fa9b7606d8ac8c94'.  
Open record -> Advanced View - > Conditions (section), remove existing 'Client Conditions'.  
  
2\. Navigate to table sys\_ux\_m2m\_action\_assignment\_action\_config.  
Create new record with below details.  
Action Configuration: 'Software Asset Workspace Declarative Actions'  
Declarative Action Assignment: Record with sys\_id '7f77b68c2dc32010fa9b7606d8ac8c94'  
  
Role Required: admin
