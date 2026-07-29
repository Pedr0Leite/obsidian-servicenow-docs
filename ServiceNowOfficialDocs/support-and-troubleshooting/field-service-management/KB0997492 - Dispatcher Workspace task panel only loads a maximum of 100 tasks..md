---
title: "Dispatcher Workspace task panel only loads a maximum of 100 tasks."
aliases:
  - KB0997492
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0997492
kb_number: KB0997492
last_modified: 2024-08-28
---

## Dispatcher Workspace task panel only loads a maximum of 100 tasks.

  

### Issue

Dispatcher Workspace task panel only loads a maximum of 100 tasks.

### Cause

It is causing because of binding of the total property of the Pagination control element.

### Resolution

Download the attached update set "CSTASK245173 - DW Task Panel total record count fix" (Attached - [CSTASK245173 - DW Task Panel total record count fix.xml](https://support.servicenow.com/sys_attachment.do?sys_id=43c99b611b83f854c16b43f6fe4bcbb0)).

Apply this update set in the instance which needs the fix.

This functionality is added in the _San Diego_ release. So, you can revert the OOB before updating to the San _Diego_ release.
