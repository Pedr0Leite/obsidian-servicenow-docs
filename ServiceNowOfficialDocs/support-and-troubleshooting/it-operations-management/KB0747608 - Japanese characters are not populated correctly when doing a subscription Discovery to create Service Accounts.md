---
title: "Japanese characters are not populated correctly when doing a subscription Discovery to create Service Accounts"
aliases:
  - KB0747608
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0747608
kb_number: KB0747608
last_modified: 2024-04-07
---

## Japanese characters are not populated correctly when doing a subscription Discovery to create Service Accounts

  

### Issue

Workaround:

This issue is currently tracked in PRB1325766 and will be fixed in New York release.

-   This issue only happen in Windows MID Server.
-   It works fine with Linux MID Servers.
-   Adding below line in the "wrapper-override.conf" file seems to work for windows host.
-   But any use cases that depend on windows cp-1252 encoding may cause the issue.
-     
    
-     
    
-   wrapper.java.additional.201=-Dfile.encoding=UTF-8
