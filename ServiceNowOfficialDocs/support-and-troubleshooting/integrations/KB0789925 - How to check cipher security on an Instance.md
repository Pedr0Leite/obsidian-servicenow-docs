---
title: "How to  check cipher security on an Instance"
aliases:
  - KB0789925
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789925
kb_number: KB0789925
last_modified: 2026-01-13
---

## How to check cipher security on an Instance

  

### Issue

-   Certificate issue on Web Service integration
-   You would like to know the cipher suite used on a service now instance.
-   You have an issues with an old web service interface and wanted to check what's wrong (handshake failure, ERR\_BAD\_SSL\_CLIENT\_AUTH\_CERT).

### Resolution

The current Cipher used on any instance can be found using the following site  
https://www.ssllabs.com/ssltest/analyze.html?d=<instance name>.service-now.com  
  
E.G. for the <instance> instance :  
https://www.ssllabs.com/ssltest/analyze.html?d=<instance name>.service-now.com

Review the configuration section and see the cipher suites.  
  
![](sys_attachment.do?sys_id=78e21f38db142810d5c4d9d96896197f)
