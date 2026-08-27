---
title: "ODBC OpenAccess SDK Driver SQL Error - [OpenAccess SDK SQL Engine]Base table:incident not found"
aliases:
  - KB0535771
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535771
kb_number: KB0535771
last_modified: 2024-04-30
---

## ODBC OpenAccess SDK Driver SQL Error - \[OpenAccess SDK SQL Engine\]Base table:incident not found

  

### Issue

# Overview

* * *

The error below has been observed occurring when a user tries to run a SQL query in ISql using the OBDC driver:  
  
ODBC Call = SQLPrepareW()  
SQL State = 42S02  
Native error = 10129(2791)  
Error Message = \[DataDirect\]\[ODBC OpenAccess SDK driver\]\[OpenAccess SDK SQL Engine\]Base table:incident not found.  
Elapsed time 2683 ms.  
Elapsed time: Prepare 0 ms. Execute 0 ms. Fetch results 2683 ms.

# Solution

* * *

This is due to a database view that has referenced itself, throwing the SchemaProcessor into a recursive loop, so causing a stack overflow.  
  
Go to **System Definitions > Database Views** to remove or rename the self-referencing view.
