---
title: "SaaS Overview dashboard doesnot show my model under subscription software model"
aliases:
  - KB0829859
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0829859
kb_number: KB0829859
last_modified: 2024-04-08
---

## Issue

I see a software model record in software subscriptions module but I do not see that model in the select elements section in SaaS overview dashboard.

I have verified that I have selected Subscription software model in the left hand side section.

![](sys_attachment.do?sys_id=59e2fcc9db0478d0fec4fb24399619ec)

## Resolution

For subscription software model to reflect in search element section of the SaaS dashboard, the product has to satisfy three conditions:   
1\. Ignore\_install should be true   
2\. subscription software should be true   
3\. product type should be licensable. 

If even one of these conditions do not satisfy the software model will not reflect.
