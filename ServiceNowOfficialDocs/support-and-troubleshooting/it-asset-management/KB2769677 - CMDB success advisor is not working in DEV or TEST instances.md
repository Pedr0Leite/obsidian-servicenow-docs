---
title: "CMDB success advisor is not working in DEV or TEST instances "
aliases:
  - KB2769677
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2769677
kb_number: KB2769677
last_modified: 2026-04-27
---

## CMDB success advisor is not working in DEV or TEST instances

  

### Issue

**Problem**  
When accessing the module via the 'CMDB workspace' and clicking the 'Resume setup' button under the CMDB success advisor tile, the 'Select model categories' screen displays no available model categories to select from.  
  

### Release

N/A

### Cause

**Root Cause**  
The root cause of the issue is a model category configured to point to itself as its parent category, which is invalid. This caused the '\_getRootParentCategory(modelCatGR)' function in the script include "ModelCategoryManager" to fail, resulting in no model categories being displayed in CMDB success advisor tile.  
  
[https://<INSTANCE-NAME>.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=2b8cf529ff202210b590ffffffffffa2](https://\<INSTANCE-NAME\>.service-now.com/nav_to.do?uri=sys_script_include.do?sys_id=2b8cf529ff202210b590ffffffffffa2)

### Resolution

**Steps to Resolve**  
1\. Identify the model category where the parent category is pointing to itself (e.g., 'Computer is parent of itself').  
2\. Remove the invalid configuration in the model category record.  
3\. Verify the resolution by re-accessing the CMDB success advisor and ensuring model categories are now available for selection.
