---
title: "Unable to add Aisle and Space in Enterprise Asset Workspace"
aliases:
  - KB2431743
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2431743
kb_number: KB2431743
last_modified: 2025-11-20
---

## Unable to add Aisle and Space in Enterprise Asset Workspace

  

### Issue

In the Enterprise Asset Workspace, we are attempting to create Aisle and space as outlined in the ServiceNow Docs  
https://www.servicenow.com/docs/bundle/zurich-it-asset-management/page/product/enterprise-asset-management/task/add-aisle-space-stockroom-eam-ws.html  
  
We are unable to add Aisle and Space as String unique Value from Enterprise Asset Workspace, when we are adding new Aisle or space its saved as blank without no data  
  
We are able to create Aisle and Spaces records directly from table - sn\_itam\_common\_aisle\_space but not from Enterprise Asset Workspace as mentioned in the above docs

### Release

All

### Resolution

The root cause of this issue is a customer-implemented business rule named "Set Location Name" on the cmn\_location table. This business rule automatically generates the location name by concatenating the city and street field values.   
  
The Problem: When creating an aisle through the workspace (or any location record directly in the cmn\_location table), the city and street fields are not populated, resulting in empty values. Consequently, the business rule generates a location name of just "\_" (underscore) due to the missing field data.  
  
Impact:  
  
Aisle creation from workspace produces invalid location names  
Direct location creation in cmn\_location table exhibits the same behavior  
All affected location records have names displaying as "\_"  
  
Resolution Required: Disable Custom "Set Location Name" business rule. If the this functionality is still needed updated the customer BR to handle scenarios where city and street fields are empty, or add custom logic to the aisle creation process to populate these required fields before the business rule executes.
