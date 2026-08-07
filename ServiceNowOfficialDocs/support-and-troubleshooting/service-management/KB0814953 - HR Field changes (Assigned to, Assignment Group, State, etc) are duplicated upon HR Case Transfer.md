---
title: "HR Field changes (Assigned to, Assignment Group, State, etc) are duplicated upon HR Case Transfer"
aliases:
  - KB0814953
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814953
kb_number: KB0814953
last_modified: 2025-09-03
---

## HR Field changes (Assigned to, Assignment Group, State, etc) are duplicated upon HR Case Transfer

  

### Issue

When the user is transferring a HR case via the Out of Box (OOB) Transfer functionality, much of the activity stream is getting "duplicated" (the entries are duplicated in the sys\_audit also).

### Resolution

The behavior is not a result of customization. Rather, it is because system property "glide.sys.audit\_inserts" is set to "true".  
  
When this property is set to "true", audit records are generated for inserts. Out of Box (OOB), the system property "glide.sys.audit\_inserts" is set to "false" which is why the issue is not reproducible there. This is [documented](https://docs.servicenow.com/csh?topicname=c_TrackingInserts.html&version=latest "documented").

As a result, the system is generating the audit for the insert as well which is causing the duplicate entries to show on the activity formatter.  
  
To stop the duplicate entries, the user needs to simply set the system property back to the default value of "false".
