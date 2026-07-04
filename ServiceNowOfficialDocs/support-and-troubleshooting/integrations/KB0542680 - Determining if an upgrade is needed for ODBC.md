---
title: "Determining if an upgrade is needed for ODBC"
aliases:
  - KB0542680
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0542680
kb_number: KB0542680
last_modified: 2025-06-23
---

## Determining if an upgrade is needed for ODBC

  

### Issue

### Symptoms

-   No data is returned
-   Error message is received

### Cause

This may be caused if you are using the ODBC 1.0.7.1 version, which has a known error.

### Resolution

If you receive the error message below, you need to upgrade to 1.0.7.3 ODBC to view results:  
  
**\[DataDirect\]\[ODBC OpenAccess SDK driver\]\[OpenAccess SDK SQL Engine\]Could not find any column information for table:<table\_name>.\[10131\]**
