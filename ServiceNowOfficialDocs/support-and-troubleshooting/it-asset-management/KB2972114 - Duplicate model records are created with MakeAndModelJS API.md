---
title: "Duplicate model records are created with MakeAndModelJS API"
aliases:
  - KB2972114
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2972114
kb_number: KB2972114
last_modified: 2026-04-21
---

## Duplicate model records are created with MakeAndModelJS API

  

### Issue

MakeAndModelJS API can create duplicate product models if the input parameters provided does not match the existing data in cmdb\_model table for all the fields such as Manufacturer, Model Name and Model ID.

### Release

Not release specific

### Resolution

Working of MakeAndModelJS API:  
1\. MakeAndModelJS.fromNames(manufacturerName, modelName, modelTable);  
2\. MakeAndModelJS.fromNamesAndNumber(manufacturerName, modelName, modelNumber, modelTable)  
  
Execution flow for the first method — MakeAndModelJS.fromNames(manufacturerName, modelName, modelTable);  
  
\=> For the manufacturer name provided, get normalized name from cds\_client\_mapping table and find the core\_company record's sys\_id with that normalized name.  
\=> Find record in cmdb\_model table with matching manufacturer's sys\_id and matching modelName as name of the cmdb\_model record.  
\=> If found, return the sys\_id of the cmdb\_model record, if not found, create a new cmdb\_model record with the manufacturer's sys\_id and the modelName and return its sys\_id.  
\----------------------------  
  
\=> If manufacturer name is empty, find record in cmdb\_model table with matching model name and empty manufacturer.  
\=> If found, return the sys\_id of the cmdb\_model record, if not found, create a new cmdb\_model with the modelName and empty Manufacturer and return its sys\_id.  
\==================  
  
Execution flow for the second method — MakeAndModelJS.fromNamesAndNumber(manufacturerName, modelName, modelNumber, String modelTable);  
  
\=> For the manufacturer name provided, get normalized name from cds\_client\_mapping table and find the core\_company record's sys\_id with that normalized name.  
\=> Find record in cmdb\_model table with matching manufacturer's sys\_id and matching modelNumber as the model\_number of the cmdb\_model record.  
\=> If found, return the sys\_id of the cmdb\_model record, if not found, create a new cmdb\_model record with the manufacturer's sys\_id, modelName, modelNumber and return its sys\_id.  
\----------------------------  
  
  
\=> If manufacturer name is empty, find record in cmdb\_model table with matching modelName, modelNumber and empty manufacturer.  
\=> If found, return the sys\_id of the cmdb\_model record, if not found, create a new cmdb\_model with the modelName, modelNumber and empty Manufacturer and return its sys\_id.  
\==================
