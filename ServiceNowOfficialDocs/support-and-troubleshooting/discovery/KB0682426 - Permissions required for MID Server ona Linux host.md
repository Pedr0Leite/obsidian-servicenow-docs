---
title: "Permissions required for MID Server ona  Linux host"
aliases:
  - KB0682426
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0682426
kb_number: KB0682426
last_modified: 2025-06-27
---

## Permissions required for MID Server ona Linux host

  

### Issue

Although MID servers on Linux host cannot discover Windows machines, some customers may still want to configure MID servers on Linux.

Common questions include:

-   Do you need a root account to run a MID server? 
-   What permissions are required for a MID server on a Linux host? 

### Resolution

To run the MID server, a Java application, a non-root user account with ownership and Read, Write, and Execute permissions on the MID server installation directory is required. This account should also have ownership and permissions on the /tmp directory, which is necessary for auto-upgrades. 

You should use a dedicated user account for the MID server to avoid permission issues that can occur if other accounts, such as Root, accidentally run the server. It can also cause some files in the MID server directory to change ownership. If permission issues arise, the ownership of the MID server directory can be forcibly changed back to the specified user account.
