---
title: "Access to api 'setAbortAction' from scope 'X' has been refused due to api's cross-scope policy"
aliases:
  - KB0750017
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750017
kb_number: KB0750017
last_modified: 2026-06-22
---

## Access to api 'setAbortAction' from scope 'X' has been refused due to api's cross-scope policy

  

### Issue

When a user tries to submit the assessment, "Access to api 'setAbortAction' from scope 'sn\_vdr\_risk\_asmt' has been refused due to the api's cross scope access policy.

![](/sys_attachment.do?sys_id=4fe84cc397698f58f69577121153afb5)

#### Steps to reproduce

1.  Create a table 'x\_vdr\_risk\_asmt' in Global and in the 'Application Access' tab. Enable all properties (can read, can create, can update, can delete). Set Accessible from to 'All application scopes'
2.  Create a new application, i.e., in the 'Scope': abortion
3.  Switch the application picker to be in the application created in step 2
4.  Create a field called 'desc' under table that was created in step 1 'repor'
5.  Create a sample Business Rule as follows for field 'desc':  
    
    if(current.x\_snc\_abortion\_desc == "desc")  
    {  
    current.setAbortAction(true);  
    }
    
6.  Navigate to 'repor.list'
7.  Create a new record with desc field = 'desc'
8.  Submit the record

### Release

### Cause

### Resolution

Enable the business rule to debug while trying to reproduce the issue.

Identify the business rules that have the 'setAbortaction(true)' that have been defined in the different application scope but running on the current scope on a custom table.

### Related Links
