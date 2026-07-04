---
title: "ODBC Error Messages: Determining if you need to increase file size limit"
aliases:
  - KB0538985
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538985
kb_number: KB0538985
last_modified: 2025-09-29
---

## ODBC Error Messages: Determining if you need to increase file size limit

  

### Issue

ODBC Error Messages: Determining if you need to increase the file size limit

### Symptoms

-   disk cache file size limit reached
-   query resulted in data sizes that exceed the maximum

### Cause

If you receive an error message indicating that the 

Disk Cache file size limit has been reached, this is likely caused by performing operations on a large number of columns.

### Resolution

If you receive the following error message when running a query, **\[ODBC OpenAccess SDK driver\]\[OpenAccess SDK SQL Engine\]Disk Cache file size limit has reached.**, the disk cache file size limit has been reached. If it is necessary for you to complete the query or operations without reducing the file size, increase the file size limit of the property.

Using the Management Console application, navigate to **Services > ServiceNow\_ODBC > Service Settings > SQL Engine Parameters** and increase the ServiceSQLDiskCacheMaxSize property.
