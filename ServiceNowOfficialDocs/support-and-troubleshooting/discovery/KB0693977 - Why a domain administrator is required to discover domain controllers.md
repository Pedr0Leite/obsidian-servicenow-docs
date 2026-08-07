---
title: "Why a domain administrator is required to discover domain controllers"
aliases:
  - KB0693977
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693977
kb_number: KB0693977
last_modified: 2025-06-30
---

## Why a domain administrator is required to discover domain controllers

  

### Issue

To discover Windows domain controllers, a domain administrator is required because ServiceNow Discovery runs on Windows Management Instrumentation (WMI). A Windows domain controller does not use an administrators group like other servers or workstations in the network normally have. 

### Release

All

### Resolution

Discovery runs remote WMI queries from the MID server while discovering Windows-based machines.

For domain controllers, the user who runs the remote WMI queries needs to be included in either:

-   the domain administrators group
-   the local administrators group

By default, these do not exist on a domain controller. This is a Microsoft Active Directory Domain Controller design limitation. 

### Related Links

[Credentials required for host discovery](https://docs.servicenow.com/csh?topicname=r_Credentials4HostDiscovery.html&version=latest)
