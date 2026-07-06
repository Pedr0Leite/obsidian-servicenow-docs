---
title: "My company applications page does not load In Development tab records"
aliases:
  - KB0784489
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0784489
kb_number: KB0784489
last_modified: 2026-03-10
---

## Issue

My Company Applications page does not load and displays spinning icon for the Developed apps tab

## Resolution

  
The page does not load due to the empty scope on this sys\_app record 'Fiscal Calendar'.

Check if the sys\_app record has associated application files which have been modified by user intentionally.

1\. If not delete this record and the app list should load correctly.  
  
/nav\_to.do?uri=sys\_app.do?sys\_id=e24e9692d7702100738dc0da9e6103dd  
  

2\. If there are application files edited by user, for valid reasons, then updating the scope field of the sys\_app record should resolve the issue. XML update should work in this case.
