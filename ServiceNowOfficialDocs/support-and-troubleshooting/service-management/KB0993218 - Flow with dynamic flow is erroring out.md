---
title: "Flow with dynamic flow is erroring out"
aliases:
  - KB0993218
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0993218
kb_number: KB0993218
last_modified: 2024-08-28
---

## Flow with dynamic flow is erroring out

  

### Issue

Flow is erroring out with the following error:  
  

Flow Designer: Operation(Asset Mgmt Registration Workflow.DYNAMIC\_FLOW\_BLOCK$1.startSub) failed with error: com.snc.process\_flow.exception.OpException: Error While fetching dynamic flow/sub-flow process plan for Asset Mgmt Registration Transform SubFlow - firstname.lastname  
at com.snc.process\_flow.engine.subflow.StartFlowOperation.run(StartFlowOperation.java:220)  
at com.snc.process\_flow.engine.Operation.execute(Operation.java:165)  
at com.snc.process\_flow.engine.ProcessEngine.executeOps(ProcessEngine.java:498)  
at com.snc.process\_flow.engine.ProcessEngine.run(ProcessEngine.java:414)  
at com.snc.process\_flow.engine.ProcessAutomation.run(ProcessAutomation.java:66)  
at com.snc.process\_flow.engine.GlideProcessAutomation.runSync(GlideProcessAutomation.java:158)  
at com.snc.process\_flow.engine.GlideProcessAutomation.runWithDomain(GlideProcessAutomation.java:261)  
at com.snc.process\_flow.engine.GlideProcessAutomation.lambda$runAsUserSync$1(GlideProcessAutomation.java:239)  
at com.snc.process\_flow.engine.PFSessionClone.run(PFSessionClone.java:58)

### Release

Paris

### Cause

Dynamic Flow Template is using a name of a subflow containing a period

### Resolution

remove the period
