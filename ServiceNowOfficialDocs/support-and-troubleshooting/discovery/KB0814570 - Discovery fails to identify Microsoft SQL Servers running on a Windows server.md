---
title: "Discovery fails to identify Microsoft SQL Servers running on a Windows server"
aliases:
  - KB0814570
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814570
kb_number: KB0814570
last_modified: 2025-07-03
---

## Issue

Learn the cause and solution to when discovery finds a Windows server but fails to discover the Microsoft SQL Server running on it, and discovery logs do not show any errors. 

## Resolution

To resolve this:

-   Enable the Microsoft SQL Server Process Classification.
-   Validate that the trigger probes section contains the following:
    -   MSSql DB On Windows Pattern for Pattern-based discovery.
    -   Windows - MSSQL probe for Probe-based discovery.   
-   Ensure the sqlservr.exe process is running on the target Windows server host and rerun discovery on the Windows server.

## Additional Information

[MSSQL server discovery](https://docs.servicenow.com/csh?topicname=mssql-data-collected-pattern.html&version=latest#mssql-data-collected-pattern "MSSQL server discovery")

[Microsoft SQL Server Classifier](https://instance_name.service-now.com/nav_to.do?uri=discovery_classy_proc.do?sys_id=7b91be46c0a80fd000fac9a374861146 "Microsoft SQL Server Classifier")

[Running processes](https://instance_name.service-now.com/cmdb_running_process_list.do?sysparm_query=computer%3D93f9fe1edb5a47009c2ff2adbf9619bd%5Eabsent%3Dfalse%5EnameLIKEsql "Running Processes")
