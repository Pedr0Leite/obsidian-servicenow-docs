---
title: "Resolving ODBC disk cache error due to maximum field length"
aliases:
  - KB0597334
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0597334
kb_number: KB0597334
last_modified: 2024-05-01
---

## Resolving ODBC disk cache error due to maximum field length

  

### Issue

Resolving ODBC disk cache error due to maximum field length

Problem

* * *

The ODBC Driver returns a disk cache error when the amount of data for a field is greater than the maximum field length.  

Symptoms

* * *

The following error message appears:  
  
OLE DB provider "MSDASQL" for linked server "SERVICENOW" returned message "\[SN\]\[ODBC ServiceNow driver\]\[OpenAccess SDK SQL Engine\]Disk cache error. Field length:89280 exceeds maximum limit of 65535.\[10232\]".

Cause

* * *

The max\_length dictionary attribute for a field in the query is smaller than the amount of data in that field.  

  
Resolution

* * *

Increase the [value of the max\_length dictionary attribute](https://docs.servicenow.com/csh?topicname=t_ModifyingStringFieldLength.html&version=latest "value of the max_length dictionary attribute") for the field to 16384 or greater.
