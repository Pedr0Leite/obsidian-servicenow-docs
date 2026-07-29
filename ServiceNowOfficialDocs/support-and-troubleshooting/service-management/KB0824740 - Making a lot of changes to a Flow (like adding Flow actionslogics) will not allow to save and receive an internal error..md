---
title: "Making a lot of changes to a Flow (like adding Flow actions/logics) will not allow to save and receive an internal error."
aliases:
  - KB0824740
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0824740
kb_number: KB0824740
last_modified: 2024-04-08
---

## Making a lot of changes to a Flow (like adding Flow actions/logics) will not allow to save and receive an internal error.

  

### Issue

The Flow Designer will only let us make small changes to a flow before saving. If we make lots of changes to a flow then try to save, we receive an error message saying there is an internal error and to check the logs for more information.

### Cause

When we try to make a large number of changes to the flow or sub-flow and save: We see an error message like below in the system logs:

\`\`\` Flow Designer: Rejected large REST payload with content-length = 17642503 bytes. Max allowed: 10485760 bytes. com.glide.rest.serializer.impl.RequestDeserializerImpl.validateContentLength(RequestDeserializerImpl.java:117) com.glide.rest.serializer.impl.RequestDeserializerImpl.getRequestDataIfWithinContentLengthLimit(RequestDeserializerImpl.java:94) com.glide.rest.serializer.impl.RequestDeserializerImpl.getRequestDataAsString(RequestDeserializerImpl.java:85) com.glide.rest.domain.ServiceRequestImpl.getRequestBodyAsString(ServiceRequestImpl.java:106) com.glide.flow\_design.rest.FlowService.updateFlow(FlowService.java:435) sun.reflect.GeneratedMethodAccessor2950.invoke(Unknown Source) sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43) java.lang.reflect.Method.invoke(Method.java:498) com.glide.rest.handler.impl.ServiceHandlerImpl.invokeService(ServiceHandlerImpl.java:44) com.glide.rest.processors.RESTAPIProcessor.process(RESTAPIProcessor.java:286) com.glide.processors.AProcessor.runProcessor(AProcessor.java:553) com.glide.processors.AProcessor.processTransaction(AProcessor.java:241) com.glide.processors.ProcessorRegistry.process0(ProcessorRegistry.java:177) com.glide.processors.ProcessorRegistry.process(ProcessorRegistry.java:166) com.glide.ui.GlideServletTransaction.process(GlideServletTransaction.java:31) com.glide.sys.Transaction.run(Transaction.java:2218) java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) java.lang.Thread.run(Thread.java:748) : no thrown error

\`\`\` And this comes from the \`RequestDeserializerImpl.java\` which looks for the system property "\`glide.rest.max\_content\_length\`" whose default value is '25'. When we try to save changes the flow designer process a REST API like \`api/now/processflow/flow/\` And fails to save if the payload has exceeded the limit.

### Resolution

When we have a large flow (high number of actions/flow logics), every change/update generates a flow plan and it is very huge.  
This can cause lot of problems in production, it can also bring instance down as it keeps building the plan in memory.  
So, the recommendation is to create another sub-flow including all the flow logic steps and call this newly created sub-flow (you can use wait for this sub-flow to finish).  
This will reduce your flow size dramatically and you will not have memory issue or other hidden issues as here.
