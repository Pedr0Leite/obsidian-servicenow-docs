---
title: "ODBC is not displaying the Import Set Row tables,  tables starting with ecc_, sysx_ and ts_"
aliases:
  - KB0713204
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713204
kb_number: KB0713204
last_modified: 2026-05-04
---

## ODBC is not displaying the Import Set Row tables, tables starting with ecc\_, sysx\_ and ts\_

  

### Issue

When retrieving data using ODBC, some tables will not be available for the queries.

You will recognize this problem because executing <instance>?SCHEMA on a browser, the missing tables do not show in the results.

### Release

All releases

### Cause

Some tables are not accessible via ODBC by design.

The following tables are not accessible:

-   tables where ACLs do not provide read access
-   tables that are on rotation extension
-   import set tables
-   tables that begin with "ecc\_", "sysx\_" and "ts\_"

### Resolution

You can allow access to protected tables by doing the following:

1.  Go to the Microsoft DSN entry for the SN ODBC driver.
2.  Change the value of the **Custom Properties** field:  
    -   From: url=<instance>
    -   To: url=<instance>;EnableDBSchema=false
3.  Reconnect to the DSN with your reporting tool, IE: Excel or ISQL, or SQL Linked Server.
4.  Validate you are able to report on the 'ldap\_import' table.
