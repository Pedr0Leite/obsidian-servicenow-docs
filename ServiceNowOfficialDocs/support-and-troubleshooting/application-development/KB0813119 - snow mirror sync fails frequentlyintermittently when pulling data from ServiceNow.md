---
title: "snow mirror sync fails frequently/intermittently when pulling data from ServiceNow"
aliases:
  - KB0813119
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813119
kb_number: KB0813119
last_modified: 2026-06-29
---

## snow mirror sync fails frequently/intermittently when pulling data from ServiceNow

  

### Issue

Snow mirror application is not able complete the sync process with ServiceNow and the sync fails frequently/intermittently when pulling data from ServiceNow. You end up with below errors on SnowMirror side:

INFO: 2020-01-24 07:00:02 \[ker-1\] - Getting count of records to insert, update and delete  
INFO: 2020-01-24 07:00:02 \[ker-1\] - Getting sys\_audit table total records count  
WARN: 2020-01-24 07:01:03 \[ker-1\] - The server responded with message 'Web service communication error occurred.; nested exception is 500 Internal Server Error'. HTTP status code: 500. Duration: 60.67 seconds. Retry will be executed.

### Release

All release

### Cause

Corresponding to the time stamp when you receive above error in SnowMirror, System Logs display below error:

_SEVERE \*\*\* ERROR \*\*\* com.glide.sys.TransactionCancelledException: Transaction cancelled: maximum execution time exceeded_  
_com.glide.rest.util.RESTRuntimeException: com.glide.sys.TransactionCancelledException: Transaction cancelled: maximum execution time exceeded_

You can also see this in **System Logs** > **System Log** > **Transaction Cancellations**

### Resolution

When Snow Mirror trying to sync with ServiceNow platform and pull the relevant data, it begins with making a REST Aggregate web service call to the respective table, evaluating the data count first. In this case, it is trying to sync sys\_audit table.

Since, it is a REST Web Service call therefore, this **Transaction Timeout** is caused by Transaction Quota Rule **REST Aggregate API request timeout** which has a default value of 60 seconds.

To fix this issue, create a copy of Transaction Quota Rule **REST Aggregate API request timeout** with below additions:  
  
a) Maximum Duration: 120 seconds  
b) Order: 50  
c) Add an AND condition wherein Created by is snowmirrow\_agent  
  
**NOTE:** Creating a copy of this Transaction Quota Rule, avoid modifying OOB Transaction Quota Rule **REST Aggregate API request timeout** and limits the scope of this fix to SnowMirror Integration only.

### Related Links
