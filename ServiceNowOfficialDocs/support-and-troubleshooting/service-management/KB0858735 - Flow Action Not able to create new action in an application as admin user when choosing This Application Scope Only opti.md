---
title: "Flow Action: Not able to create new action in an application as admin user when choosing \"This Application Scope Only\" option from Accessible from field"
aliases:
  - KB0858735
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0858735
kb_number: KB0858735
last_modified: 2024-04-08
---

## Flow Action: Not able to create new action in an application as admin user when choosing "This Application Scope Only" option from Accessible from field

  

### Issue

1.  Admin user has the role "action\_designer"
2.  Admin user is NOT able to create an action on any application when we choose "This Application Scope Only" option from Accessible from the field.
3.  Below Error Message is seen: Bad Request, Insufficient access level for create operation on Action

### Release

All Versions

### Cause

This is the expected behavior in out of the box as users cannot modify Accessible from setting in scopes they do not own.

Insufficient access level for create operation on Action: com.glide.flow\_design.action.data.ActionDesignAccessLevelException: Insufficient access level for create operation on Action: com.glide.flow\_design.action.data.ActionTypeGlideRecordRepo.insertActionType(ActionTypeGlideRecordRepo.java:379)  
com.glide.flow\_design.action.providers.ActionTypeRepoBackedProvider.saveNewActionType(ActionTypeRepoBackedProvider.java:229)  
com.glide.flow\_design.rest.ActionService.saveActionTypeDefinition(ActionService.java:325)  
sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)  
sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)  
sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)  
java.lang.reflect.Method.invoke(Method.java:498)  
com.glide.rest.handler.impl.ServiceHandlerImpl.invokeService(ServiceHandlerImpl.java:44)  
com.glide.rest.processors.RESTAPIProcessor.process(RESTAPIProcessor.java:287)  
com.glide.processors.AProcessor.runProcessor(AProcessor.java:576)  
com.glide.processors.AProcessor.processTransaction(AProcessor.java:264)  
com.glide.processors.ProcessorRegistry.process0(ProcessorRegistry.java:181)  
com.glide.processors.ProcessorRegistry.process(ProcessorRegistry.java:169)  
com.glide.ui.GlideServletTransaction.process(GlideServletTransaction.java:44)  
com.glide.sys.Transaction.run(Transaction.java:2228)  
java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)  
java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)  
java.lang.Thread.run(Thread.java:748)  
  
save Action Definition: com.glide.flow\_design.action.data.ActionDesignAccessLevelException: no thrown error  
  
  
![](sys_attachment.do?sys_id=d3e7f041db04b4d0b55f0b55ca961983)  
  
![](sys_attachment.do?sys_id=93e7f041db04b4d0b55f0b55ca9619e8)  

### Resolution

Users should be able to set the access level when creating actions in a scope they own on their instance.

The below method will work well

-   Create a new app using Studio
-   Create a new action in Flow Designer
-   Select the new application scope created in step 1
-   Set the Accessible from to This application only
-   Save the action

### Related Links

[https://docs.servicenow.com/csh?topicname=create-action.html&version=latest](https://docs.servicenow.com/csh?topicname=create-action.html&version=latest)

-   For Example, "Alert Management Content" is out of the box application which belongs to ServiceNow Scope.
-   So, the end-user wouldn't be able to set the "Accessible From" to "This application scope only" but they should be able to set it to "All Application Scopes"
