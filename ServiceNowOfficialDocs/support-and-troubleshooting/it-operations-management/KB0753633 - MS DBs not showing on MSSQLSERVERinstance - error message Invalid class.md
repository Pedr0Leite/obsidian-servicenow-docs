---
title: "MS DBs not showing on MSSQLSERVERinstance - error message: Invalid class"
aliases:
  - KB0753633
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0753633
kb_number: KB0753633
last_modified: 2026-06-16
---

## Issue

Issue: MSSQL Discovery is not able to bring back the Database information to be populated in "cmdb\_ci\_db\_mssql\_database" and returning an error message: "Invalid class" on WMI Query.

\====

In the "MSSql DB on Windows" Pattern, we can see the following error on "Get list of db from Wmi" step.

Get list of db from wmi  
2019-06-25 17:32:14: Executing WMI query on host 10.12.32.45 query: SELECT Name FROM Win32\_PerfFormattedData\_MSSQLSERVER\_SQLServerDatabases  
2019-06-25 17:32:18: WMI query on host 10.12.32.45 failed. query: SELECT Name FROM Win32\_PerfFormattedData\_MSSQLSERVER\_SQLServerDatabases error: Invalid class  
2019-06-25 17:32:18: Groovy code failure. com.snc.sw.exception.CommandFailureException: Failed to execute WMI query on host 10.12.32.45 query: SELECT Name FROM Win32\_PerfFormattedData\_MSSQLSERVER\_SQLServerDatabases error message: Invalid class . Failed to execute WMI query on host 10.12.32.45 query: SELECT Name FROM Win32\_PerfFormattedData\_MSSQLSERVER\_SQLServerDatabases error message: Invalid class

## Resolution

Troubleshooting steps

\==============

Run the following Query to the target host from the MID server.

**gwmi -query "SELECT Name FROM Win32\_PerfFormattedData\_MSSQLSERVER\_SQLServerDatabases" -computer xxx.xxx.xxx.xxx | Format-list -Property Name**

if it works, it should show similar to the following screenshot.

![](sys_attachment.do?sys_id=89b2399e97c4f990d4743dae2153af13)

if it fails, it will look similar to the following screenshot below, which is what we see in the Pattern Log as well. Customer will then need to work further with their own Internal IT/DBA team to resolve the issue.

![](sys_attachment.do?sys_id=45b2399e97c4f990d4743dae2153af10)

## Additional Information

[WMI query for two fields returns five fields](https://support.servicenow.com/kb_view.do?sysparm_article=KB1441398 "WMI query for two fields returns five fields")
