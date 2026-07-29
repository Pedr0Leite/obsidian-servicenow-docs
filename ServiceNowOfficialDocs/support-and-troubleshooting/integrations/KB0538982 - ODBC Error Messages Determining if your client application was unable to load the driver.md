---
title: "ODBC Error Messages: Determining if your client application was unable to load the driver"
aliases:
  - KB0538982
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538982
kb_number: KB0538982
last_modified: 2024-05-01
---

## ODBC Error Messages: Determining if your client application was unable to load the driver

  

### Issue

ODBC Error Messages: Determining if your client application was unable to load the driver

Symptoms

* * *

-   driver not loading
-   driver times out waiting for a response

   
Cause

* * *

If you receive an error message during loading or initializing an ODBC driver connection, it is likely that the client application was unable to load the driver.

Resolution

* * *

If you receive the following error message when attempting to load or intialize the driver connection, _**\[DataDirect\]\[ODBC OpenAccess SDK driver\]\[OpenAccess SDK Client\]Failed to initialize the Service component.**_, it may indicate that the client application (for example, Crystal Reports) was unable to load the driver. One of the reasons may be that the default Java maximum heap size is too large for the reporting application.

1.  In the Management Console, navigate to **Services** \> **Service Settings** \> **IP Parameters**.
2.  Reduce the value of **ServiceJVMOptions** to **\-Xms32m -Xmx64m**.
3.  If the error persists, reduce the memory more.
