---
title: "Response templates not visible on HR agent workspace"
aliases:
  - KB0957282
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0957282
kb_number: KB0957282
last_modified: 2025-09-03
---

## Issue

For non-HR Admin users who are having the sn\_hr\_core.case\_writer and sn\_templated\_snip.template\_snippet\_reader role are unable to see Response templates in HR agent workspace

## Resolution

The OOB ACL on cxs\_context\_config table is de-activated. Reverting it to OOB resolved the issue:  
https://<instance>.service-now.com/nav\_to.do?uri=sys\_security\_acl.do?sys\_id=14340894eb5121003623666cd206fecf
