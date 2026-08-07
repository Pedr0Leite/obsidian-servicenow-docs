---
title: "Determining if ODBC processing has failed due to low memory"
aliases:
  - KB0538950
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538950
kb_number: KB0538950
last_modified: 2024-05-19
---

## Determining if ODBC processing has failed due to low memory

  

### Issue

Determining if ODBC processing has failed due to low memory

Symptoms

* * *

-   ODBC driver runs out of memory during processing
-   Queried information lost
-   Cannot connect to the instance
-   Connection dropped

Cause

* * *

The driver may have run out of memory during ODBC process due to large result sets.   

  
Resolution

* * *

To remedy this, change the maximum Java heap size by accessing the ODBC Management Module. Go to **Windows Start button > ServiceNow ODBC > Management Console** and edit the -Xmx150m parameter of the ServiceJVMOptions property. For more information, see [ODBC Driver Configuration](https://docs.servicenow.com/csh?topicname=configuring-odbc.html&version=latest "ODBC Driver Configuration") in the ServiceNow product documentation.
