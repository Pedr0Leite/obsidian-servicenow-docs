---
title: "Determining if precision errors are causing issues with ODBC queries"
aliases:
  - KB0538953
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538953
kb_number: KB0538953
last_modified: 2024-05-19
---

## Determining if precision errors are causing issues with ODBC queries

  

### Issue

Determining if precision errors are causing issues with ODBC queries 

Symptoms

* * *

-   Queried information lost
-   Precision errors received
-   Error message received during processing

   
Cause

* * *

Performing queries on SQL Server 2008 and 2012 may cause precision errors for decimal or number field values using the 

**OPENQUERY** syntax with the ODBC driver. 

Resolution

* * *

In this case, use the **Cast** syntax to convert the precision. For example:

SELECT \* from OPENQUERY(SERVICENOW, ‘SELECT Cast(sys\_mod\_count as Decimal(38,0)), number, short\_description from incident’)
