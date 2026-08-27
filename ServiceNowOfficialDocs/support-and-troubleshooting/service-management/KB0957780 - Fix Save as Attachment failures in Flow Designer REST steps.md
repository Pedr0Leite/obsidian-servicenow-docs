---
title: "Fix Save as Attachment failures in Flow Designer REST steps"
aliases:
  - KB0957780
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0957780
kb_number: KB0957780
last_modified: 2025-08-27
---

## Fix Save as Attachment failures in Flow Designer REST steps

  

### Issue

When creating a Flow Designer action that retrieves files from Jira and uploads them as attachments to ServiceNow records, the Save as Attachment feature may fail with a NullPointerException error.    
  
The following error appears in the logs:

Operation(Upload Attachment.f9f7796edb476050002c3307f496195e) failed with error: java.lang.NullPointerException  
at com.snc.process\_flow.integration.MidAttachmentWrapper.saveResponseAsAttachment(MidAttachmentWrapper.java:118)  
at com.snc.process\_flow.operation.AbstractHttpOperation.processResponseAttachment(AbstractHttpOperation.java:389)  
at com.snc.process\_flow.operation.HttpOperation.processResponse(HttpOperation.java:287)  
at com.snc.process\_flow.operation.AbstractHttpOperation.requestAndProcessResponse(AbstractHttpOperation.java:131)  
at com.snc.process\_flow.operation.AbstractHttpOperation.invoke(AbstractHttpOperation.java:111)  
at com.snc.process\_flow.operation.RetryableIntegrationOperation.run(RetryableIntegrationOperation.java:46)  
at com.snc.process\_flow.engine.Operation.execute(Operation.java:165)  
at com.snc.process\_flow.engine.ProcessEngine.executeOps(ProcessEngine.java:497)  
at com.snc.process\_flow.engine.ProcessEngine.run(ProcessEngine.java:413)  
at com.snc.process\_flow.engine.ProcessAutomation.run(ProcessAutomation.java:66)  
at com.snc.process\_flow.engine.MidProcessAutomation.messageFlow(MidProcessAutomation.java:55)  
at com.service\_now.mid.probe.IPaaSActionProbe.probe(IPaaSActionProbe.java:101)  
at com.service\_now.mid.probe.AProbe.process(AProbe.java:104)  
at com.service\_now.mid.queue\_worker.AWorker.runWorker(AWorker.java:122)  
at com.service\_now.mid.queue\_worker.AWorkerThread.run(AWorkerThread.java:20)  
at com.service\_now.mid.threadpool.ResourceUserQueue$RunnableProxy.run(ResourceUserQueue.java:647)  
at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)  
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)  
at java.lang.Thread.run(Thread.java:748)

### Release

All releases

### Resolution

To resolve the Save as Attachment failure in Flow Designer:

1.  Verify that your MID Server is running and properly validated.
2.  Check that the MID Server has permissions to read the table you use in the flow (for example, the incident table).
3.  To test MID Server permissions:
    -   Impersonate the MID Server user
    -   Access the record in the user interface
4.  If the MID Server user cannot access the record, grant the appropriate permissions and test the flow action again.

**Note**:  For the incident table, you can disable the incident query business rule if it is not serving any purpose.
