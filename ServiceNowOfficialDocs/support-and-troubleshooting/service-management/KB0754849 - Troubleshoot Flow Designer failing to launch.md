---
title: "Troubleshoot Flow Designer failing to launch"
aliases:
  - KB0754849
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0754849
kb_number: KB0754849
last_modified: 2026-03-04
---

## Troubleshoot Flow Designer failing to launch

  

### Issue

  

When trying to launch Flow Designer from left filter navigation, you may see the error "The page you are looking for could not be found". The following steps should help to resolve this issue.

### Release

Madrid and Xanadu releases

### Cause

 This error is caused by a versioning issue with the Flow Designer UI.

### Resolution

To resolve this: 

1.  Uninstall **Flow-Action Designer** from sys\_store\_app using maint user credentials.
    1.  URL: sys\_store\_app.do?sysparm\_query=scope%3Dsn\_flow\_designer)
2.  Search for the related **Uninstall** link.
3.  Restart all active nodes in your instance.
4.  Open the sys\_plugins list  and repair the com.glide.hub.designer plugin.
5.  If the issue persists after repairing the application, go to cache.do and clear both caches.
