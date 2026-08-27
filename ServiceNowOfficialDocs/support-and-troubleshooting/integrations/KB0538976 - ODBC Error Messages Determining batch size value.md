---
title: "ODBC Error Messages: Determining batch size value"
aliases:
  - KB0538976
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538976
kb_number: KB0538976
last_modified: 2024-05-19
---

## ODBC Error Messages: Determining batch size value

  

### Issue

ODBC Error Messages: Determining batch size value

Symptoms

* * *

-   query resulted in data sizes that exceed the Java maximum 
-   query timed out while processing  
      

Cause

* * *

If you receive an query error message that the data limit has been exceeded, the query you issued likely resulted in data that exceeded the default Java maximum heap size.

Resolution

* * *

If you receive the following error message when running an ODBC query, _\[DataDirect\]\[ODBC OpenAccess SDK driver\]\[OpenAccess SDK SQL Engine\]_ **_Error running query for execute: OutOfMemoryError: GC overhead limit exceeded. Your current batch size for fetching records is set at 2000. Please set it to 1000 and try again._**, the query you have issued resulted in batch data sizes that exceed the default Java maximum heap size. Try reducing the record fetching batch size so that a lesser number of records are fetched per-request, and more requests are made for the query instead. Adjust the value to the recommended size specified in the error message.

In the ODBC Administrator: go to the **System DSN** tab and configure the ServiceNow ODBC Driver that you plan on using.

In the **Custom Properties** field, add **BatchSize=1000**.

For more information on how to change this value, see [Configuring the ODBC Driver](https://docs.servicenow.com/csh?topicname=configuring-odbc.html&version=latest "Configuring the ODBC Driver") in the ServiceNow product documentation.
