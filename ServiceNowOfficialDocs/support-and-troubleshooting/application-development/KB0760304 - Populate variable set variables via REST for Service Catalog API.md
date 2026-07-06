---
title: "Populate variable set variables via REST for Service Catalog API"
aliases:
  - KB0760304
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0760304
kb_number: KB0760304
last_modified: 2025-01-03
---

## Populate variable set variables via REST for Service Catalog API

  

### Summary

This article explains how to Populate variable set variables via REST call for Service Catalog API

### Instructions

1\. Create a catalog item, which contains :  
One single line text variable (slt),  
One Single-Row Variable Set, which contains one Single line text (Slt2) and  
One Multi-Row Variable Set (mrvs), which contains one Single line text (Slt3)

The format of JSON request object would be like :  
{  
"sys\_id" : "039c516237b1300054b6a3549dbe5dfc",  
"sysparm\_quantity" : "1",  
"variables" : {  
"slt" : "slt\_value",  
"slt2" : "slt2\_value"  
"mrvs" : "\[{\\"slt3\\" : \\"slt3\_value\\"}\]"  
}  
}

For Single-Row Variable Set, we don't need to mention the internal\_name of Variable set. However, for'mvrs' we need to mention its name and the value should be an array of JSON objects.

If the variable as a reference set as below, then you set the value as below when you use REST, where ee329ce2dbb033002878dc965e96196c is the sys\_id of the reference field value.

"slvset1Qref" : "ee329ce2dbb033002878dc965e96196c" ( For Reference Field you should use sys\_id) .
