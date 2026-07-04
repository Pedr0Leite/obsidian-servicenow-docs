---
title: "Why my server has MySQL Server on Sotware Installations tab despite MariaDB is installed on the server?"
aliases:
  - KB2015511
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2015511
kb_number: KB2015511
last_modified: 2025-03-27
---

## Issue

Customer installs MariaDB and runs it on servers.  
After running discovery, we see "MySQL Server" is shown on Software Installations tab but we installed only MariaDB.  
Why MySQL Server is shown on the tab?

## Resolution

It's working as expected. Current behavior is below.  
  
1\. When mysql or mariadb process is detected, Discovery pattern "My SQL server On Windows and Linux" is invoked to detect MySQL instance.

2\. In the pattern, post pattern script "Sync Installed Software" is run and it creates "MySQL Server" on Software Installations tab (cmdb\_sam\_sw\_install table.)
