---
title: "[SAM] Installs created by Schedule job \"SAM - Software Asset Connections\" doesn't have last scan date populated."
aliases:
  - KB2677922
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2677922
kb_number: KB2677922
last_modified: 2026-05-19
---

## Issue

  
Issue 1 - SAM - Software Asset Connections is not setting Last Scanned on cmdb\_sam\_sw\_install. We should use cmdb\_ci\_appl.last\_discovered.

Issue 2 - Sync Installed Software Pattern Pre/Post Script does not honor discovery source of the application record  
1\. Create an application in cmdb\_ci\_db\_mssql\_instance (it extends application table), set the discovery source as ACC  
2\. Run the "Synch Installed Software" Pattern Pre/Post Script  
3\. Check the install table

Expect:  
The created install should have discovery source as ACC, pattern = true  
Actual:  
The created install should have discovery source as ServiceNow, pattern = true

## Resolution

  
This was a known issue & has been fixed in Yokohama Patch 12, Zurich Patch 6 & Australia releases. Please plan for an upgrade accordingly as there are no workaround available as of now.
