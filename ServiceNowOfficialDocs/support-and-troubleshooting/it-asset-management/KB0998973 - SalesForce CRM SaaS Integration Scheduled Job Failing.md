---
title: "SalesForce CRM SaaS Integration Scheduled Job Failing"
aliases:
  - KB0998973
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0998973
kb_number: KB0998973
last_modified: 2024-10-07
---

## SalesForce CRM SaaS Integration Scheduled Job Failing

  

### Issue

SalesForce CRM SaaS integration failed. The connection was established, but the scheduled jobs are failing and the subscription data is not being pulled into the instance. 

Sample Error:  
Flow Designer: Operation(Salesforce CRM Download Subscriptions.DS\_action\_wrapper-03600a34db98201077155a75dc9619ea.03600a34db98201077155a75dc9619ea.Datastream$1./initializer) failed with error: com.snc.process\_flow.exception.OpException: Failed to iterate on data stream: com.glide.transform.transformer.exceptions.InvalidStructureException: JsonStreamParser\[2\]: JSON must be an object or an array: '<'  
at com.snc.process\_flow.engine.DataStreamLoopOperation.run(DataStreamLoopOperation.java:51)  
at com.snc.process\_flow.engine.Operation.execute(Operation.java:202)  
at com.snc.process\_flow.engine.ProcessEngine.executeOps(ProcessEngine.java:536)  
at com.snc.process\_flow.engine.ProcessEngine.run(ProcessEngine.java:445)  
.....

### Cause

Connection URL is not correct. 

### Resolution

Connection URL is not correct. The connection URL is referring to the Salesforce "My Domain URL".

The format is something like

https://<My\_Domain\_Name>.lightning.force.com
