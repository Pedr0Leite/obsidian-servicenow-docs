---
title: "MID-Server installation not creating associated Windows Service"
aliases:
  - KB0815813
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815813
kb_number: KB0815813
last_modified: 2024-04-08
---

## MID-Server installation not creating associated Windows Service

  

### Issue

When a newly installed MID server is started using start.bat , sometimes the corresponding Windows service for the MID server is not created and visible under Windows services tab.

### Resolution

To resolve this issue:

1.  On the MID server box, navigate to /agent/bin folder
2.  Run InstallMID-NT.bat. 
3.  Go to Windows Services tab and click refresh. The MID server service should be created and visible.
