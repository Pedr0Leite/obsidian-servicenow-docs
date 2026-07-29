---
title: "Flow action is updating /adding to update set"
aliases:
  - KB0964403
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0964403
kb_number: KB0964403
last_modified: 2025-02-04
---

## Flow action is updating /adding to update set

  

### Issue

Flow action when modified, saved & published does not update the current Update Set. No erntries in the sys\_update\_xml. Only the complex record object.

In the system logs we see: 

Invalid query detected, please check logs for details \[Unknown field element in table sys\_flow\_step\_definition\]

In the node logs we see:

txid=2d6ea3d21b02 Operation against file 'sys\_hub\_action\_type\_definition' was aborted by Business Rule 'Ensure unique name in scope^4174dc021b65601049e3bc16464bcb9d'. Business Rule Stack:Ensure unique name in scope

txid=2d6ea3d21b02 Invalid query detected, stack trace below \[Unknown field element in table sys\_flow\_step\_definition\]  
com.glide.db.QueryEventLogger.logInvalidQuery(QueryEventLogger.java:56)  
com.glide.db.QueryEventLogger.logInvalidQuery(QueryEventLogger.java:47)  
com.glide.script.GlideRecord.isInvalidTableField(GlideRecord.java:2403)  
com.glide.script.GlideRecord.addQuery(GlideRecord.java:2375)  
com.glide.pojo.ElementDescriptorPlainObjectBuilder.getParamRecord(ElementDescriptorPlainObjectBuilder.java:227)

### Cause

Business Rule "Ensure unique name in scope" (/sys\_script.do?sys\_id=92555054670003005423ebc172415a44) gets triggered.  
There are actions with the same internal name.

### Resolution

Copying the action should allow republishing as it will create a new internal name.
