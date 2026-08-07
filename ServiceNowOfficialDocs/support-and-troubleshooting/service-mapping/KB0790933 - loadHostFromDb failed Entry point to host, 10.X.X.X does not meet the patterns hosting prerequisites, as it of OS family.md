---
title: "loadHostFromDb failed: Entry point to host, 10.X.X.X does not meet the patterns hosting prerequisites, as it of OS family cmdb_ci_win_server and the pattern accepts OS family cmdb_ci_lb_netscaler."
aliases:
  - KB0790933
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790933
kb_number: KB0790933
last_modified: 2024-04-08
---

## Issue

loadHostFromDb failed: Entry point to host, 10.X.X.X does not meet the patterns hosting prerequisites, as it of OS family cmdb\_ci\_win\_server and the pattern accepts OS family cmdb\_ci\_lb\_netscaler.

Steps to reproduce:

-   Open Service Map which has the Cluster with top-level as Netscaler.
-   Within the cluster, there is an IIS server and Virtual Directory pair.
-   Begin debug session on the IIS server's Identification section.
-   The debug will not start and will instead throw the error referenced above in the system log.

## Resolution

Navigate to IIS pattern and set Operating system to **ALL**.
