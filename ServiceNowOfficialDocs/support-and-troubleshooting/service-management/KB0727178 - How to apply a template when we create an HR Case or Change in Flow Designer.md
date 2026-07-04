---
title: "How to apply a template when we create an HR Case or Change in Flow Designer"
aliases:
  - KB0727178
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727178
kb_number: KB0727178
last_modified: 2024-04-07
---

## How to apply a template when we create an HR Case or Change in Flow Designer

  

### Issue

How to apply a template when we create an HR Case or Change in Flow Designer

### Release

Kingston, London, and Future releases

### Resolution

For HR Case

1.  We can use Actions in the Flow Designer to apply templates in the Flow Designer.
2.  For HR Application, Use Actions -> Select Field as HR Service -> Select an HR Service
3.  Based on the Selection of HR Service, the template for the HR Case will be automatically applied, if the template is defined for the HR Service in the platform

For Change and other task extended records, please use the script action.

API - applyTemplate() should be used in the code to apply the templates to records.

### Related Links

[https://developer.servicenow.com/app.do#!/api\_doc?v=jakarta&id=r\_GlideRecord-applyTemplate\_String](https://developer.servicenow.com/app.do#!/api_doc?v=jakarta&id=r_GlideRecord-applyTemplate_String)
