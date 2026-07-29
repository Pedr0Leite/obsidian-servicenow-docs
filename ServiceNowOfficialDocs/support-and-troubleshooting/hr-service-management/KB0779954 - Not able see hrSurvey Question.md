---
title: "Not able see hrSurvey Question"
aliases:
  - KB0779954
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779954
kb_number: KB0779954
last_modified: 2024-04-08
---

## Not able see hrSurvey Question

  

### Issue

Created survey for hr cases but not able see the survey question that use send for end user on close complete hr cases.

### Resolution

This issue is occurring because "glide.security.admin.override.accessterm" System Property is not present in customer's instance.  
  
Please follow below steps to create new property:

1\. Proceed to the System Properties table (sys\_properties.list) via the filter navigator  
2\. Click the "New" button  
Name = glide.security.admin.override.accessterm  
Type = True/False  
Value = True
