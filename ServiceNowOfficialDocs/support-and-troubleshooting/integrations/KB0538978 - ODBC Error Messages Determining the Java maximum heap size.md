---
title: "ODBC Error Messages: Determining the Java maximum heap size"
aliases:
  - KB0538978
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538978
kb_number: KB0538978
last_modified: 2024-05-19
---

## ODBC Error Messages: Determining the Java maximum heap size

  

### Issue

ODBC Error Messages: Determining the Java maximum heap size

Symptoms

* * *

-   query resulted in data sizes that exceed the Java maximum 
-   query timed out while processing  
      

Cause

* * *

If you receive an out of memory error message indicating that the Java heap size maximum should be increased, the query you issued likely resulted in an intial response that exceeded the Java maximum heap size.

Resolution

* * *

If you receive the following error message when running an ODBC query, _**\[DataDirect\]\[ODBC OpenAccess SDK driver\]\[OpenAccess SDK SQL Engine\]OutOfMemoryError:** **Java heap space. Your current maximum heap size is set at 150MB. Please set it at 300MB and try again.**_, the query you have issued resulted in an initial response that exceeded the default Java maximum heap size. Try increasing the default Java maximum heap size. 

To increase the size to the value recommended by the error message:

1.  Go to the Management Console and navigate to **Services > Service Settings > IP Parameters**. 
2.  Set the value of **ServiceJVMOptions** to **\-Xms64m -Xmx300m**. 

For more information on how to change this value, see [Configuring the ODBC Driver](https://docs.servicenow.com/csh?topicname=configuring-odbc.html&version=latest "Configuring the ODBC Driver") in the ServiceNow product documentation.
