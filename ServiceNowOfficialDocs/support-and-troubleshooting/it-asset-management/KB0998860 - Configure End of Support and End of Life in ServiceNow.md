---
title: "Configure End of Support and End of Life in ServiceNow"
aliases:
  - KB0998860
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0998860
kb_number: KB0998860
last_modified: 2024-10-28
---

## Issue

We hava gather end of support and end of life asset information and we want to map it in ServiceNow.  
Which table do we need to refer where I can find field to update EOL/EOS dates for Hardware.

## Resolution

1.  The life cycle information can be updated on cmdb\_model records.
2.  If you open any record in cmdb\_model ==> On the form layout
3.  Under relatedlists ==> There is "Hardware Model Lifecycles".
4.  Create records over here that reflect the model life cycle dates.

![](sys_attachment.do?sys_id=2acd7912db880154f77799ead3961961)
