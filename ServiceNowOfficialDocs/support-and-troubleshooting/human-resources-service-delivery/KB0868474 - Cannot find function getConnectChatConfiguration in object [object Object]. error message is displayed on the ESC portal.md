---
title: "\"Cannot find function getConnectChatConfiguration in object [object Object].\" error message is displayed on the ESC portal"
aliases:
  - KB0868474
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0868474
kb_number: KB0868474
last_modified: 2026-03-17
---

## Issue

When navigating to My Tasks on the ESC portal, the "Cannot find function getConnectChatConfiguration in object \[object Object\]." error message is displayed.

## Resolution

Revert the Script Include 'hr\_PortalUtil' to OOB or if custom script include is still needed,  append the getConnectChatConfiguration function from the OOB into the custom script include.  
https://instance\_name.service-now.com/sys\_script\_include.do?sys\_id=3c764fda534032003585c3c606dc34e9
