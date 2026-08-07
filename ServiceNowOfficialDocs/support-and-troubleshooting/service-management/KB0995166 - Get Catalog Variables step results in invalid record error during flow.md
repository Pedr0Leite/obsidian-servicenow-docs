---
title: "Get Catalog Variables step results in invalid record error during flow "
aliases:
  - KB0995166
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0995166
kb_number: KB0995166
last_modified: 2025-08-28
---

## Get Catalog Variables step results in invalid record error during flow

  

### Issue

When using Flow Designer, the Get Catalog Variables step fails with the error "is not a valid record" due to timing issues between record creation and flow execution.

![Image of error message showing "is not a valid record" during Get Catalog Variables from flow action](/sys_attachment.do?sys_id=d8a7360393afe6145736b25d6cba1009)

### Release

All versions

### Cause

1.  The Request Item (RITM) record is created (for example: "2021-08-28 18:23:22").
2.  The flow.fire event is created at the same time. You can verify this in the System Event table: https://<instance\_name>.service-now.com/sysevent\_list.do sysparm\_query=instanceSTARTSWITH<sys\_id\_of\_flow\_context>
3.  Root cause: The business rule, Start FlowDesigner Flow, is configured to run before Insert.
4.  The Flow engine cannot fetch the Glide Record because the record is not fully created when the flow attempts to access it.  
    **Note:** This issue occurs intermittently due to variables such as flow engine performance, scheduler timing, and Glide record CRUD operations.
5.   Error stack:

Operation(Name of Flow Flow.e80662b9db65e4143726a4f6d49619d2.b70ba3abc31013002841b63b12d3aeff) failed with error: com.snc.process\_flow.exception.OpException: is not a valid record.  
at com.snc.process\_flow.operation.GetCatalogVariablesOperation.run(GetCatalogVariablesOperation.java:98)  
at com.snc.process\_flow.engine.Operation.execute(Operation.java:198)  
at com.snc.process\_flow.engine.ProcessEngine.executeOps(ProcessEngine.java:501)  
at com.snc.process\_flow.engine.ProcessEngine.run(ProcessEngine.java:411)  
at com.snc.process\_flow.engine.ProcessAutomation.run(ProcessAutomation.java:66)  
at com.snc.process\_flow.engine.GlideProcessAutomation.runSync(GlideProcessAutomation.java:128)  
at com.snc.process\_flow.engine.GlideProcessAutomation.runWithDomain(GlideProcessAutomation.java:243)  
at com.snc.process\_flow.engine.GlideProcessAutomation.lambda$runAsUserSync$1(GlideProcessAutomation.java:216)  
at com.snc.process\_flow.engine.PFSessionClone.run(PFSessionClone.java:55)  
at com.snc.process\_flow.engine.GlidePFSession.runPlanAsUserSession(GlidePFSession.java:42)  
at com.snc.process\_flow.engine.GlideProcessAutomation.runAsUserSync(GlideProcessAutomation.java:214)  
at com.snc.process\_flow.engine.GlideProcessAutomation.messageFlow(GlideProcessAutomation.java:283)  
at com.snc.process\_flow.engine.ProcessHubEventHandler.doSendMessage(ProcessHubEventHandler.java:450)  
at com.snc.process\_flow.engine.ProcessHubEventHandler.process(ProcessHubEventHandler.java:108)  
at com.snc.process\_flow.engine.ProcessHubEventHandler.process(ProcessHubEventHandler.java:80)  
at com.snc.process\_flow.engine.FlowEventManager.processEvents(FlowEventManager.java:97)  
at com.glide.job.EventHandlerJob.execute(EventHandlerJob.java:32)  
at com.glide.schedule.JobExecutor.lambda$executeJob$0(JobExecutor.java:115)

### Resolution

To resolve the error, revert the following business rules to their default configuration.

-   **Start FlowDesigner Flow**  
    Access at: https://<instance\_name>.service-now.com/nav\_to.do?uri=sys\_script.do?sys\_id=837a49f63ba013008ed00d8044efc4e5
-   **Cascade Request Approval to Request Item**  
    Access at: https://<instance\_name>.service-now.com/nav\_to.do?uri=sys\_script.do?sys\_id=2d0885b4c61122840070856bf5994bca

**Note:** Avoid customizing these business rules as they can interfere with the proper timing of record creation and flow execution.

### Related Links

undefined
