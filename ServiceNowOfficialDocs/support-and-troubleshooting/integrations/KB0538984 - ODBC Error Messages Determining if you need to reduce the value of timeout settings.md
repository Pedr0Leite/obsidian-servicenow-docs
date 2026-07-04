---
title: "ODBC Error Messages: Determining if you need to reduce the value of timeout settings"
aliases:
  - KB0538984
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538984
kb_number: KB0538984
last_modified: 2024-05-19
---

## ODBC Error Messages: Determining if you need to reduce the value of timeout settings

  

### Issue

ODBC Error Messages: Determining if you need to reduce the value of timeout settings

Symptoms

* * *

-   driver not loading
-   driver times out waiting for a response

   
Cause

* * *

If you receive an error message during a query indicating that the ODBC driver timed out waiting for a response, this is likely caused by overly aggressive proxy server or firewall socket inactivity timeout settings.

Resolution

* * *

If you receive the following error message when running a query, _**ERROR \[HY000\] \[DataDirect\]\[ODBC Open Access SDK driver\]\[OpenAccess SDK SQL Engine\]**_ _**Error running query for execute: The ODBC driver timed out waiting for a response. This is often caused by overly aggressive proxy server or firewall socket inactivity timeout settings.**_ _**You may need to set instance property glide.soap.request\_ processing\_timeout to a smaller value.**_ _**Error Message: Socket timeout**_ _**\[1010\]**_, this indicates that the driver timed out during a long-running query and you can set the instance property to a smaller value to prevent this from happening again. 

Create an integer property on the instance called glide.soap.request\_processing\_timeout and set the value to 28 seconds. (This is based on the 30 second socket inactivity timeout value.)  
  
This new setting causes the SOAPProcessor to perform a temporary HTTP redirect after 28 seconds to keep the connection alive while the long-running query is executing on the instance.
