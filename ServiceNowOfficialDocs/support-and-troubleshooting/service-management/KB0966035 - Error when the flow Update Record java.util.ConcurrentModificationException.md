---
title: "Error when the flow Update Record: java.util.ConcurrentModificationException "
aliases:
  - KB0966035
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0966035
kb_number: KB0966035
last_modified: 2025-10-27
---

## Error when the flow Update Record: java.util.ConcurrentModificationException

  

### Issue

When running the flow, sometimes will get error failed with error: java.util.ConcurrentModificationException when the flow Update Record

This problem happens randomly. Every time it happens, the error message is similar and also happens during update record.

This is the error message we get when viewing the flow error:

  
Operation(Catalog Item - Access to PowerBI.e4403d3c1b532410c8576359bc4bcbd4.5ad05916c31332002841b63b12d3ae63) failed with error: java.util.ConcurrentModificationException  
at java.util.ArrayList$Itr.checkForComodification(ArrayList.java:911)  
at java.util.ArrayList$Itr.next(ArrayList.java:861)  
at com.glide.glideobject.Journal.insertOrUpdateEntries(Journal.java:473)  
at com.glide.glideobject.Journ...  
Error  
Flow Designer: Operation(Catalog Item - Access to PowerBI.e4403d3c1b532410c8576359bc4bcbd4.5ad05916c31332002841b63b12d3ae63) failed with error: java.util.ConcurrentModificationException  
at java.util.ArrayList$Itr.checkForComodification(ArrayList.java:911)  
at java.util.ArrayList$Itr.next(ArrayList.java:861)  
at com.glide.glideobject.Journal.insertOrUpdateEntries(Journal.java:473)  
at com.glide.gl...  
  

Steps to reproduce:

1.  Create a flow trigger on service catalog.
2.  Create step to update record on sc\_request table which triggered item associated to.
    -   Set requested for field to triggered request item request\_for field.
3.  Attach this flow to a service catalog item.
4.  Create a new Service catalog item 3) defined.
    -   Sometimes the error will present as ConcurrentModificationException like mentioned above.

### Release

### Cause

This is due to when a RITM is created, a request would be created under sc\_request, then a workflow will be triggered.

When flow runs Update record on sc\_request table, the related record is still in creating process.

So those two processes are trying to update the same records, then cause concurrentmodification error as mentioned.

When this happens, two workflow content will be triggered for same request.

One is created by the user who raised the request item, which is expected.

Another one is created by system, which was triggered by the flow update step, which is incorrect.

### Resolution

Add timer before the Update record step to avoid conflict with sc\_request/workflow creation.

Request\_for field has been populated when sc\_request is created, so reapplying the field again is not needed.
