---
title: "Using the REST Table API to Get Data From an Instance a HTTP-200 is Returned, but Not all of the Data is Given in the JSON Response Body"
aliases:
  - KB0778443
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778443
kb_number: KB0778443
last_modified: 2024-04-08
---

## Using the REST Table API to Get Data From an Instance a HTTP-200 is Returned, but Not all of the Data is Given in the JSON Response Body

  

### Issue

Using the REST Table API to Get Data From an Instance a HTTP-200 is Returned, but Not all of the Data is Given in the JSON Response Body

### Release

Applies to any release.

### Cause

Analysis of the JSON response body at the client shows an error at the end:

...test","application":"appr","u\_state":"","escalated\_ticket":""}\],"error":{"detail":"No such column Check logs for error trace or enable glide.rest.debug property to verify REST request processing","message":"Transaction cancelled: maximum execution time exceeded"},"status":"failure"}

This indicates that one of the REST Transaction Quota Rules have been exceeded.  Meaning that the request ran too long and was terminated.

To get details on which Quota Rule was exceeded check the node logfile, in this example the "REST Table API request timeout" was exceeded:

2019-09-11 14:09:02 (858) glide.quota.manager Quota exceeded for REST Table API request timeout, requesting cancel  
2019-09-11 14:09:02 (858) glide.quota.manager WARNING \*\*\* WARNING \*\*\* Transaction: Cancelling transaction #320040 /api/now/table/sn\_customerservice\_case (maximum execution time exceeded): Thread API\_INT-thread-2 (null, 3EF11742DBBFB300483F5D104B9619B4), after 60682ms  
2019-09-11 14:09:02 (863) glide.quota.manager SYSTEM Cancelled 0 child transactions  
2019-09-11 14:09:02 (864) API\_INT-thread-2 3EF11742DBBFB300483F5D104B9619B4 txid=36f11742dbbf WARNING \*\*\* WARNING \*\*\* Long Transaction started at 09/11/19 14:08:02.176, Memory at start was 677, Memory is 669, SQL count is 1,167, BR count is now 158.  
2019-09-11 14:09:02 (864) API\_INT-thread-2 3EF11742DBBFB300483F5D104B9619B4 txid=36f11742dbbf WARNING \*\*\* WARNING \*\*\* Transaction cancelled: maximum execution time exceeded  
2019-09-11 14:09:02 (865) API\_INT-thread-2 3EF11742DBBFB300483F5D104B9619B4 txid=36f11742dbbf SEVERE \*\*\* ERROR \*\*\* Transaction cancelled: maximum execution time exceeded  
java.lang.RuntimeException: Transaction cancelled: maximum execution time exceeded  
at com.glide.rest.serializer.impl.JSONSerializer.handleSerializeException(JSONSerializer.java:163)  
at com.glide.rest.serializer.impl.JSONSerializer.serializeServiceResult(JSONSerializer.java:59)  
at com.glide.rest.handler.impl.ServiceResultHandlerImpl.serialize(ServiceResultHandlerImpl.java:130)  
at com.glide.rest.handler.impl.ServiceResultHandlerImpl.serializeIterable(ServiceResultHandlerImpl.java:116)  
at com.glide.rest.handler.impl.ServiceResultHandlerImpl.processServiceResultBody(ServiceResultHandlerImpl.java:94)

This means that the request ran longer than the defined "Maximum Duration (seconds)" in the Quota Rule.

Quota Rules can be found at:

System Definition -> Transaction Quota Rules

### Resolution

There are at least two separate solutions for this issue:

(1) Extending the "Maximum Duration (seconds)" in the Quota Rule.  To modify the Quota Rules go to System Definition -> Transaction Quota Rules.  This may not be the best option as it will cause the semaphore to be tied up for a longer time and may cause performance issues if there are a lot of requests coming into the instance.  The risk of API\_INT semaphore exhaustion becomes more probable.

(2) A better option is to limit the results sent back in a response so that the request will execute more quickly.  Use the REST API Custom Query Parameters.  You can change the query in the request by using sysparm\_query, limit the fields returned by using sysparm\_fields , sending multiple requests that only send back a limited number of rows using sysparm\_limit and sysparm\_offset. 

For information on the REST API Custom query parameters see the documentation here:

[https://docs.servicenow.com/csh?topicname=c\_RESTAPI.html&version=latest](https://docs.servicenow.com/csh?topicname=c_RESTAPI.html&version=latest)
