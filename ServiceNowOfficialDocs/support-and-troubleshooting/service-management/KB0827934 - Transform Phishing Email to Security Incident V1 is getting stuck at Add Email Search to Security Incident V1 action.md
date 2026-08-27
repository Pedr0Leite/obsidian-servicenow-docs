---
title: "Transform Phishing Email to Security Incident V1 is getting stuck at \"Add Email Search to Security Incident V1\" action"
aliases:
  - KB0827934
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0827934
kb_number: KB0827934
last_modified: 2025-01-22
---

## Transform Phishing Email to Security Incident V1 is getting stuck at "Add Email Search to Security Incident V1" action

  

### Issue

When any Phisihing email is been received to Instance it create the Security Incident and when adding the email to security Incident it uses "Add Email Search to Security Incident V1" action which will stuck and the flow never get's executed

### Release

NewYork, Orlando

### Cause

If the system property "glide.email.forward\_subject\_prefix" is empty and doesn't contain any fw or FW prefix we see this issue

### Resolution

\* flow "Transform Phishing Email to Security Incident V1" is using the action "Add Email Search to Security Incident V1"  
\* In this action we are calling the script include "EmailSearchCapabilityUtil"  
\* and from the same action we are calling the function "createEmailSearchFromList"  
\* that function is checking for system property "glide.email.forward\_subject\_prefix"" in line 108  
\* If that system property is empty the flow got stuck and throwing the error  
\* we can see error as below  
  
\[code\]

<pre>  
com.glide.flow.exceptions.FlowNotFoundException: Flow not found: com.glide.rest.util.RESTRuntimeException: com.glide.flow.exceptions.FlowNotFoundException: Flow not found: com.glide.rest.handler.impl.ServiceHandlerImpl.handleInvocationTargetException(ServiceHandlerImpl.java:76)  
com.glide.rest.handler.impl.ServiceHandlerImpl.invokeService(ServiceHandlerImpl.java:49)  
com.glide.rest.processors.RESTAPIProcessor.process(RESTAPIProcessor.java:286)  
com.glide.processors.AProcessor.runProcessor(AProcessor.java:553)  
com.glide.processors.AProcessor.processTransaction(AProcessor.java:241)  
com.glide.processors.ProcessorRegistry.process0(ProcessorRegistry.java:177)  
com.glide.processors.ProcessorRegistry.process(ProcessorRegistry.java:166)  
com.glide.ui.GlideServletTransaction.process(GlideServletTransaction.java:31)  
com.glide.sys.Transaction.run(Transaction.java:2218)  
java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)  
java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)  
java.lang.Thread.run(Thread.java:748)  

</pre>  
\[/code\]  
  
\* Solution will be updating the "glide.email.forward\_subject\_prefix"" system property with valid prefix "fw:,fwd"  
  

### Related Links

Flow:

[https://<Instance Name>.service-now.com/$flow-designer.do?sysparm\_nostack=true#/flow-designer/e546bd1bb3033300ed7fc9c316a8dc11](https://carrixtest.service-now.com/$flow-designer.do?sysparm_nostack=true#/flow-designer/e546bd1bb3033300ed7fc9c316a8dc11)

  

Action:

[https://<Instance Name>.service-now.com/$flow-designer.do?sysparm\_nostack=true#/action-designer/187161c3b3d33300ed7fc9c316a8dc13/step/6f014cda-5cfb-4bfe-91d1-90aec306054e](https://carrixtest.service-now.com/$flow-designer.do?sysparm_nostack=true#/action-designer/187161c3b3d33300ed7fc9c316a8dc13/step/6f014cda-5cfb-4bfe-91d1-90aec306054e)
