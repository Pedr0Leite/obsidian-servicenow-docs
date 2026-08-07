---
title: "Table field value is not populate inside the sys_choice table after Import the data using the excel sheet."
aliases:
  - KB0758186
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0758186
kb_number: KB0758186
last_modified: 2024-04-07
---

## Table field value is not populate inside the sys\_choice table after Import the data using the excel sheet.

  

### Issue

Importing into sys\_choice table using easy import option, the data uploads but the 'Table' column label is empty.

**Steps to Reproduce:**   
  
1\. Open the Choice List Records  
2\. Click on List Control (hamburger menu) icon, and click on Import  
3\. Select Create Template and export it.  
4\. Fill the data inside the excel spreadsheet  
5\. Import the excel data sheet  
  
\>> Choice will add inside the sys\_choice table but table field will displayed empty.

### Cause

Issue has been reported on known PRB1315898.  
This is caused by system property 'glide.import\_template.field\_types\_to\_ignore'  
This defines a set of filed types to ignore in easy import. The Table column is in table\_name type which is a ignore field by default.

### Resolution

Removing table\_name from the list on Value field from system property 'glide.import\_template.field\_types\_to\_ignore'
