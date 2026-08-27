---
title: "Failing widget: 'SC Categories' (4c03cba0cb11020000f8d856634c9ce1)"
aliases:
  - KB0831475
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0831475
kb_number: KB0831475
last_modified: 2025-04-03
---

## Issue

When opening page..**"sc\_category"** on the portal, the following error is shown:

com.snc.process\_flow.exception.ProcessAutomationException: Plan does not exist with an id 

Script source code logged to console

Failing widget: 'SC Categories' (4c03cba0cb11020000f8d856634c9ce1)

## Resolution

Do any of the following:

1.  Catalog items with invalid flow sys\_id should be set to active false 
2.  Define a valid flow for the catalog item

Run cache.do
