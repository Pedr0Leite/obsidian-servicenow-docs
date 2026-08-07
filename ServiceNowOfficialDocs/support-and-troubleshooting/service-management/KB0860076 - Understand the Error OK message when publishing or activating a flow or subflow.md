---
title: "Understand the \"Error OK\" message when publishing or activating a flow or subflow"
aliases:
  - KB0860076
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0860076
kb_number: KB0860076
last_modified: 2025-08-11
---

## Understand the "Error OK" message when publishing or activating a flow or subflow

  

### Issue

When publishing or activating a flow or subflow in Flow Designer, you may encounter an "Error OK" message. 

### Release

All versions

### Cause

This is expected behavior. Flows with recursive calls—actions that call the same flow that it is a part of—cannot publish, as documented in the [Flow Designer architecture overview](https://www.servicenow.com/docs/bundle/zurich-build-workflows/page/administer/flow-designer/concept/flow-designer-arch-overview.html#d30029e772).

When the system detects a recursive call, the system times out and displays an "Error OK" message because it has exceeded the maximum run time. 

Following is a stack trace showing the transaction cancellation as a result of this error. 

Transaction cancelled: maximum execution time exceeded: com.glide.rest.util.RESTRuntimeException: Transaction cancelled: maximum execution time exceeded: com.glide.rest.serializer.impl.JSONSerializer.handleSerializeException(JSONSerializer.java:166)  
com.glide.rest.serializer.impl.JSONSerializer.serializeServiceResult(JSONSerializer.java:60)  
com.glide.rest.handler.impl.ServiceResultHandlerImpl.serialize(ServiceResultHandlerImpl.java:130)  
com.glide.rest.handler.impl.ServiceResultHandlerImpl.processServiceResultBody(ServiceResultHandlerImpl.java:96)  
com.glide.rest.handler.impl.ServiceResultHandlerImpl.processServiceResult(ServiceResultHandlerImpl.java:40)  
com.glide.rest.processors.RESTAPIProcessor.process(RESTAPIProcessor.java:290)  
com.glide.processors.AProcessor.runProcessor(AProcessor.java:553)  
com.glide.processors.AProcessor.processTransaction(AProcessor.java:241)  
com.glide.processors.ProcessorRegistry.process0(ProcessorRegistry.java:177)  
com.glide.processors.ProcessorRegistry.process(ProcessorRegistry.java:166)  
com.glide.ui.GlideServletTransaction.process(GlideServletTransaction.java:31)  
com.glide.sys.Transaction.run(Transaction.java:2218)  
java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)  
java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)  
java.lang.Thread.run(Thread.java:748)

### Resolution

To resolve this issue, redesign your flow to eliminate recursive calls.

Recursive calls are not allowed because they can cause instance outages and consume excessive system resources.
