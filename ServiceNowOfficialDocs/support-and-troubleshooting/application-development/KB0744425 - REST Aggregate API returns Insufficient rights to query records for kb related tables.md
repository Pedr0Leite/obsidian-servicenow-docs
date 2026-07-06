---
title: "REST Aggregate API returns \"Insufficient rights to query records\" for kb related tables"
aliases:
  - KB0744425
tags:
  - servicenow
  - support-kb
  - rest-api
  - aggregate-api
  - access-control-acl
  - knowledge-management
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0744425
kb_number: KB0744425
last_modified: 2024-04-07
---

## REST Aggregate API returns "Insufficient rights to query records" for kb related tables

  

### Issue

The Aggregate API (api/now/stats/{table\_name}) returns the below response even though the user has access to these records from the list view.

{
    "error": {
        "detail": "No permission to read table 'kb\_knowledge'",
        "message": "Insufficient rights to query records"
    },
    "status": "failure"
}

  

### Release

The PRB has been fixed in New York Patch 8 and higher, Orlando Patch 2 and higher, and all family versions from Paris and higher.

### Cause

This is a known error reported in PRB1332230.

### Resolution

To workaround this issue, you need create a table level read ACL for the affected table. For the kb\_knowledge as an example, follow the below steps. 

1.  Login as admin.
2.  Elevate roles to security\_admin.
3.  Go to sys\_security\_acl.list from the filter navigator. 
4.  Click on 'New' to create a new ACL.
5.  Set the values as below:  
    1.  Type: record
    2.  Operation: read
    3.  For the name, select kb\_knowledge from the tables dropdown menu and 'None' from the fields dropdown menu.
    4.  Under 'Required roles' list, add 'itil' role or the role that the affected users have.
6.  Save the record.

## Related

- [[c_AggregateAPI]] - REST Aggregate API reference
- [[KB0753132 - Users getting Unauthorized access error in Service Portal when REST API level ACLs are in place]] - related REST API ACL issue

