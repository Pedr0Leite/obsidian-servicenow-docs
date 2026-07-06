---
title: "Unable to get last analytics trigger time for processing. Exiting."
aliases:
  - KB0760549
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0760549
kb_number: KB0760549
last_modified: 2024-07-31
---

## Issue

Running the below code 

var serviceProcessor = new SNC.ServiceAnalyticsProcessor();  
serviceProcessor.query();

from "Scripts - Background" throws the error:

`"Unable to get last analytics trigger time for processing. Exiting..."`

![](sys_attachment.do?sys_id=74bea1f51b5af890ccc253da234bcb4a)

## Resolution

Update the below Hash value with the valid present date as shown in the screenshot:

https://instance\_name.service-now.com/sa\_hash\_list.do?sysparm\_query=nameLIKEanalytics

![](sys_attachment.do?sys_id=34bea1f51b5af890ccc253da234bcb22)
