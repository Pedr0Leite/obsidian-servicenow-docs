---
title: "TypeError: Cannot read property '$$hashKey' of undefined"
aliases:
  - KB0781583
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781583
kb_number: KB0781583
last_modified: 2024-04-07
---

## TypeError: Cannot read property '$$hashKey' of undefined

  

### Issue

When using the service portal widget 'Data Table from URL Definition' the results are not displayed and in the browser console the following error is presented:

TypeError: Cannot read property '$$hashKey' of undefined

### Cause

The widget 'Data Table from URL Definition' has a dependency to another widget 'Data Table'

<sp-widget widget="data.dataTableWidget"></sp-widget>

The error is presented as the roles defined for the widgets did not align.

### Resolution

Ensure the roles match for both widgets

'Data Table' /sp\_widget.do?sys\_id=5001b062d7101200b0b044580e6103eb

and

'Data Table from URL Definition' /sp\_widget.do?sys\_id=8ae61f55cb21020000f8d856634c9c93
