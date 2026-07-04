---
title: "Determining whether missing ACLs are causing access issues with ODBC queries"
aliases:
  - KB0542655
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0542655
kb_number: KB0542655
last_modified: 2024-05-19
---

## Determining whether missing ACLs are causing access issues with ODBC queries

  

### Issue

Determining whether missing ACLs are causing access issues with ODBC queries

Symptoms

* * *

-   Query returns error message
-   Queried returns table column names but not values
-   Query does not allow read access

   
Cause

* * *

There are no ACLs defined for a table to allow access to the user. If ACLs are not defined, the default is to deny access to the user without the admin role.

Resolution

* * *

You may receive this error message when running an ODBC query:  
  
**_\[DataDirect\]\[ODBC OpenAccess SDK driver\]\[OpenAccess SDK SQL Engine\]Could not find any column information for table:<table\_name>.\[10131\]  
_**

To allow read access, add an ACL for a particular role, and add that role to the user record. The odbc role is provided by default starting with Helsinki. Make sure to verify and add all necessary ACLs.
