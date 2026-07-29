---
title: "ODBC Error Messages: Verifying that the URL of your instance is correct"
aliases:
  - KB0538955
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538955
kb_number: KB0538955
last_modified: 2024-05-19
---

## ODBC Error Messages: Verifying that the URL of your instance is correct

  

### Issue

ODBC Error Messages: Verifying that the URL of your instance is correct

Symptoms

* * *

-   driver unable to connect
-   receive connection timed out error message

Cause

* * *

If you receive a connection timed out error message, it may be that the driver was unable to connect to the URL configured to your instance, or the URL may be incorrect.

Resolution

* * *

If you receive the following error message, **_\[DataDirect\]\[ODBC OpenAccess SDK driver\]\[OpenAccess SDK SQL Engine\]java.net.ConnectException:_ _Connection timed out: connect_**, check to see if you have configured global defaults or DSN, and ensure that the URL is correct.

For more information on configuring global defaults and creating a new DSN using the ODBC driver, see [ODBC Driver](https://docs.servicenow.com/csh?topicname=c_ODBCDriver.html&version=latest "ODBC Driver") in the ServiceNow product documentation.
