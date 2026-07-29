---
title: " Last scan date in Software Installations table isn't getting updated for linux server software installs"
aliases:
  - KB1638653
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1638653
kb_number: KB1638653
last_modified: 2024-03-25
---

## Last scan date in Software Installations table isn't getting updated for linux server software installs

  

### Issue

Last scan date in Software Installations table isn't getting updated for linux server software installs.

### Cause

 "Linux - Installed Software" probe has cached results enabled

### Resolution

-   The last scanned field is not being updated because the software installs data received during latest discovery doesn't have any new information.
-   By default the Probe "Linux - Installed Software" has cached results enabled, which will not update the software installs last scanned unless we've any data change.

**Note:** You can disable the cache results but it might cause performance impact.
