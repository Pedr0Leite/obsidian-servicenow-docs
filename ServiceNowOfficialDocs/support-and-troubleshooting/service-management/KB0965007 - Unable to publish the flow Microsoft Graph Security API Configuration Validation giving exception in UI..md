---
title: "Unable to publish the flow \"Microsoft Graph Security API Configuration Validation\" giving exception in UI."
aliases:
  - KB0965007
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0965007
kb_number: KB0965007
last_modified: 2024-05-22
---

## Unable to publish the flow "Microsoft Graph Security API Configuration Validation" giving exception in UI.

  

### Issue

Unable to publish the OOB flow "Microsoft Graph Security API Configuration Validation" giving below exception in UI. 

  

![](sys_attachment.do?sys_id=1faa87871b3cf4107a5933f2cd4bcb26)

### Cause

If we look in highlighted section in first image flow designer is showing no data available for step1 , which is not correct as you can see that action has output variables.`          ![](sys_attachment.do?sys_id=1faa87871b3cf4107a5933f2cd4bcb28)         ![](sys_attachment.do?sys_id=9faa87871b3cf4107a5933f2cd4bcb2a)    `

Below exceptions can be seen from app node logs.

`2021-06-09 04:43:05 (623) Default-thread-10 BD3AAD0B1BEC7814751BA9342A4BCB32 txid=426d25cf1bec *** Start #974249 /xmlhttp.do, user: user   2021-06-09 04:43:05 (635) Default-thread-10 BD3AAD0B1BEC7814751BA9342A4BCB32 txid=426d25cf1bec sn_sec_graphsecapi: DVN source id 63772dd5531000107253ddeeff7b1285   2021-06-09 04:43:07 (515) Default-thread-10 BD3AAD0B1BEC7814751BA9342A4BCB32 txid=426d25cf1bec SEVERE *** ERROR *** Flow Designer: Tenant Id is mandatory and must be filled in   2021-06-09 04:43:07 (539) Default-thread-10 BD3AAD0B1BEC7814751BA9342A4BCB32 txid=426d25cf1bec SEVERE *** ERROR *** sn_sec_graphsecapi (GraphSecurityAPILogger): Microsoft Graph Security API (undefined) : Error Occured in Configuration Tile Validation   File Name : undefined   Error Message : The current operation ended in state: ERROR`  
  
  
Tenant Id is mandatory and must be filled in:  
com.glide.flow\_trigger.engine.FlowPlanRetriever.retrieve(FlowPlanRetriever.java:140)  
com.glide.flow\_trigger.engine.FlowPlanRetriever.retrieve(FlowPlanRetriever.java:89)  
com.snc.process\_flow.engine.serialization.PlanProxy.plan(PlanProxy.java:48)  
com.snc.process\_flow.engine.PFContext.init(PFContext.java:433)  
com.snc.process\_flow.engine.GlideProcessAutomation.\_init(GlideProcessAutomation.java:492)  
com.snc.process\_flow.engine.GlideProcessAutomation.runWithDomain(GlideProcessAutomation.java:241)  
com.snc.process\_flow.engine.GlideProcessAutomation.lambda$runAsUserSync$1(GlideProcessAutomation.java:216)  
com.snc.process\_flow.engine.PFSessionClone.run(PFSessionClone.java:55)  
com.snc.process\_flow.engine.GlidePFSession.runPlanAsUserSession(GlidePFSession.java:42)  
com.snc.process\_flow.engine.GlideProcessAutomation.runAsUserSync(GlideProcessAutomation.java:214)

### Resolution

Re-adding the "Tenant Id" input by taking the Action #1 output should fix this issue.

Also publish the flow from same application scope where the flow has been configured, else below exception will be thrown.

  

2021-06-10 05:43:12 (645) Default-thread-8 DA528BD31B2C7C9087CF5245624BCB6A txid=4cc48f931b6c SEVERE \*\*\* ERROR \*\*\* sn\_sec\_graphsecapi (GraphSecurityAPILogger): Microsoft Graph Security API (undefined) : Error Occured in Configuration Tile Validation  
File Name : undefined  
Error Message : The current operation ended in state: ERROR
