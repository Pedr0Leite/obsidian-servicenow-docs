---
title: "Flow Designer error: Error occured while inserting record: Error during insert of sys_user_group"
aliases:
  - KB0827213
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0827213
kb_number: KB0827213
last_modified: 2025-09-22
---

## Flow Designer error: Error occured while inserting record: Error during insert of sys\_user\_group

  

### Issue

There is a flow defined where the variable values entered in the record are processed further in the for loop and sent into the create record action where the record is created in the user group table

But the flow is failing and showing the below errors:

1\. Operation(Create New Group and Add Members.c239d9a9db34d4508672324d7c961912.f9e09916c31332002841b63b12d3aeaa) failed with error: com.snc.process\_flow.exception.OpException: Error occured while inserting record: Error during insert of sys\_user\_group (Testing Group Creation)  

2\. Operation(NTU Creating/Modifying Group.If$1.346bfc32dbfc58506ef8f00ebf961949.If$1.786bfc32dbfc58506ef8f00ebf96194c.Create New Group and Add Members$1.callSub) failed with error: com.snc.process\_flow.exception.OpException: called block 'NTU Creating/Modifying Group.If$1.346bfc32dbfc58506ef8f00ebf961949.If$1.786bfc32dbfc58506ef8f00ebf96194c.Create New Group and Add Members$1.callSub' failed. Check the context log for exception details.

3.error:2020-05-21 02:17:00 (359) worker.7 worker.7 txid=7c79a79fdbbc SEVERE \*\*\* ERROR \*\*\* Flow Designer: Operation(Create New Group and Add Members.ForEach$1.itemIterator) failed with error: java.lang.ClassCastException: java.lang.String cannot  
be cast to java.lang.Iterable  
at com.snc.process\_flow.engine.ForEachOperation.run(ForEachOperation.java:53)  
at com.snc.process\_flow.engine.Operation.execute(Operation.java:107)  
at com.snc.process\_flow.engine.ProcessEngine.executeOps(ProcessEngine.java:435)  
at com.snc.process\_flow.engine.ProcessEngine.run(ProcessEngine.java:382)

### Cause

From the below error there is list variable which is trying to be processed in the for loop of subloop where it is failing

error:2020-05-21 02:17:00 (359) worker.7 worker.7 txid=7c79a79fdbbc SEVERE \*\*\* ERROR \*\*\* Flow Designer: Operation(Create New Group and Add Members.ForEach$1.itemIterator) failed with error: java.lang.ClassCastException: java.lang.String cannot  
be cast to java.lang.Iterable  
at com.snc.process\_flow.engine.ForEachOperation.run(ForEachOperation.java:53)  
at com.snc.process\_flow.engine.Operation.execute(Operation.java:107)  
at com.snc.process\_flow.engine.ProcessEngine.executeOps(ProcessEngine.java:435)  
at com.snc.process\_flow.engine.ProcessEngine.run(ProcessEngine.java:382)

### Resolution

  
Problem was created for the above issue if process the list type variable in for loop

Problem:PRB1406475  

Workaround : Instead of sending the output of 'getcatalogvariable' step add an 'lookup records' step and send that to the output of the subflow which is processing the group
