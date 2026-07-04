---
title: "Determining whether user is missing query role to view ODBC data "
aliases:
  - KB0542667
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0542667
kb_number: KB0542667
last_modified: 2025-04-07
---

## Determining whether user is missing query role to view ODBC data

  

### Issue

Determining whether user is missing query role to view ODBC data 

Symptoms

* * *

-   Cannot view ODBC data 
-   Data can be viewed in UI but not in ODBC

   
Cause

* * *

The user does not have the soap\_query role to view data in ODBC.

Resolution

* * *

ODBC uses SOAP web services. If you have _**glide.soap.strict\_security**_ set to **true,** you need to add the soap\_query role to the user. You can also use the odbc role starting with Helsinki.
