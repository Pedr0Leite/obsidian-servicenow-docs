---
title: "REST Import Set API - Creates an Import Set and Target Record, but Get an HTTP-500 Response Code and Response Body Contains Error:  \"null value in entry: transform_map=null\""
aliases:
  - KB0791757
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791757
kb_number: KB0791757
last_modified: 2024-04-08
---

## Issue

Using the REST Import Set API POST:  

Versioned URL: /api/now/v1/import/<staging table\_name>

or

Default URL: /api/now/import/<staging table\_name>

There is a record created in the staging/import set table and the target table so it appears that the import does work, but the calling client gets an HTTP-500 error and this content:

An error was encountered while processing request. Exception: {"error":{"detail":"null value in entry: transform\_map=null Check logs for error trace or enable glide.rest.debug property to verify REST request processing","message":"java.lang.NullPointerException: null value in entry: transform\_map=null"},"status":"failure"}  
Exception Message: The remote server returned an error: (500) Internal Server Error. (type WebException)  
Evaluation of expression 'eq(jsonpath('$.result\[0\].status')\[0\], 'inserted')' failed.

The following error stack is seen in the instance node logs:

2019-12-30 07:50:21 (655) API\_INT-thread-4 A52860E5DB4AC450B5B580C74B9619BF txid=e92860e5db4a SEVERE \*\*\* ERROR \*\*\* java.lang.NullPointerException: null value in entry: transform\_map=null  
com.glide.rest.util.RESTRuntimeException: java.lang.NullPointerException: null value in entry: transform\_map=null  
at com.glide.rest.handler.impl.ServiceHandlerImpl.handleInvocationTargetException(ServiceHandlerImpl.java:76)  
at com.glide.rest.handler.impl.ServiceHandlerImpl.invokeService(ServiceHandlerImpl.java:49)  
at com.glide.rest.processors.RESTAPIProcessor.process(RESTAPIProcessor.java:290)  
at com.glide.processors.AProcessor.runProcessor(AProcessor.java:553)  
at com.glide.processors.AProcessor.processTransaction(AProcessor.java:240)  
at com.glide.processors.ProcessorRegistry.process0(ProcessorRegistry.java:177)  
at com.glide.processors.ProcessorRegistry.process(ProcessorRegistry.java:166)  
at com.glide.ui.GlideServletTransaction.process(GlideServletTransaction.java:31)  
at com.glide.sys.Transaction.run(Transaction.java:2203)  
at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)  
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)  
at java.lang.Thread.run(Thread.java:748)  
Caused by: java.lang.NullPointerException: null value in entry: transform\_map=null  
at com.google.common.collect.CollectPreconditions.checkEntryNotNull(CollectPreconditions.java:34)  
at com.google.common.collect.ImmutableMapEntry.<init>(ImmutableMapEntry.java:49)  
at com.google.common.collect.ImmutableMap.entryOf(ImmutableMap.java:122)  
at com.google.common.collect.ImmutableMap$Builder.put(ImmutableMap.java:198)  
at com.glide.rest.service.impset.ImportSetResponse$Builder.buildItemResponse(ImportSetResponse.java:135)  
at com.glide.rest.service.impset.ImportSetResponse$Builder.build(ImportSetResponse.java:115)  
at com.glide.rest.service.impset.ImportSetAPIService.create(ImportSetAPIService.java:109)  
at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)  
at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)  
at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)  
at java.lang.reflect.Method.invoke(Method.java:498)  
at com.glide.rest.handler.impl.ServiceHandlerImpl.invokeService(ServiceHandlerImpl.java:44)  
... 10 more

2019-12-30 07:50:21 (657) API\_INT-thread-4 A52860E5DB4AC450B5B580C74B9619BF txid=e92860e5db4a WARNING \*\*\* WARNING \*\*\* #398701 \[REST API\] RESTAPIProcessor : Handling exception java.lang.NullPointerException: null value in entry: transform\_map=null  
2019-12-30 07:50:21 (657) API\_INT-thread-4 A52860E5DB4AC450B5B580C74B9619BF txid=e92860e5db4a WARNING \*\*\* WARNING \*\*\* #398701 \[REST API\] RESTAPIProcessor : Unknown exception RESTRuntimeException:java.lang.NullPointerException: null value in entry: transform\_map=nullDetail: null value in entry: transform\_map=null  
2019-12-30 07:50:21 (658) API\_INT-thread-4 A52860E5DB4AC450B5B580C74B9619BF txid=e92860e5db4a DEBUG: #398701 \[REST API\] RESTAPIProcessor : End of Request Processing  
2019-12-30 07:50:21 (658) API\_INT-thread-4 A52860E5DB4AC450B5B580C74B9619BF txid=e92860e5db4a DEBUG: #398701 \[REST API\] RESTAPIProcessor : REST Request Processing time total\_time\_to\_now\_micro\_secs=1460931  
2019-12-30 07:50:21 (658) API\_INT-thread-4 A52860E5DB4AC450B5B580C74B9619BF txid=e92860e5db4a \*\*\* End #398701 /api/now/import/u\_table, user: myUser, total time: 0:00:01.459, processing time: 0:00:01.458, total wait: 0:00:00.001, semaphore wait: 0:00:00.001, SQL time: 0:00:00.492 (count: 378), business rule: 0:00:01.183 (count: 10), ACL time: 0:00:00.015, Cache build time: 0:00:00.036, source: 10.10.10.10 , type:rest, method:POST, api\_name:now/import, resource:now/import/u\_table, version:Default, user\_id:b531e692db898c10b5b580c74b9619a0, response\_status:500

## Resolution

(1) In the sys\_user table check the user that is making the REST calls.  The user should have the Role import\_admin and/or import\_transformer or the admin Role.

(2) If the required Roles exist and the issue persists go to the ACLs and check all of the Operation = read ACLs on table sys\_transform\_map:

-   If the instance has gone through an Express to Enterprise conversion and there are ACLs active that have "Express Security" checked, these can be deactivated as they only apply to the Express version of the platform.
-   Check other ACLs to see if they may be blocking access for the user making the REST calls, based on that user's roles or customized ACL scripting
-   Add or modify ACLs to give the user read access to the sys\_transform\_map table or give the user the needed Role(s) to provide access for customized ACLs
-   The only ACL that is out of the box and considered required is the one shown in the screen shot, so if the user has the import\_admin and/or import\_transformer or admin Role this will allow the necessary access:

![](sys_attachment.do?sys_id=c2bbb3bcdb00f0d016d2a345ca961982)
