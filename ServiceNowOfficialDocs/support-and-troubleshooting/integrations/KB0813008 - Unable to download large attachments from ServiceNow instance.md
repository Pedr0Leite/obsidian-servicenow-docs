---
title: "Unable to download large attachments from ServiceNow instance"
aliases:
  - KB0813008
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813008
kb_number: KB0813008
last_modified: 2024-08-28
---

## Unable to download large attachments from ServiceNow instance

  

### Issue

User when trying to download the attachment , never got the download file name

### Cause

Proxy URL configured for the instance on the customer network to redirect <instancename>.service-now.com to <proxyname>.xxxx.xxxx

### Resolution

Use Servicenow instance URL to dowload the file. Work with the internal proxy admin why the download was being blocked.
