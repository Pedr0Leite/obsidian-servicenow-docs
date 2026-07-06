---
title: "SLA Definition field value is not displaying on task sla list or related lists for some users"
aliases:
  - KB0749738
tags:
  - servicenow
  - support-kb
  - acl
  - access-control
  - contract-sla
  - sla
  - task-sla
  - read-acl
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749738
kb_number: KB0749738
last_modified: 2024-04-07
---

## SLA Definition field value is not displaying on task sla list or related lists for some users

  

### Issue

# Symptoms

For some users, when they view Task SLA lists or related lists, the SLA definition column displays a blank value. An example of this issue is shown in the image below.

![blank sla definition](sys_attachment.do?sys_id=29eb28eadb42b450e515c2230596198c "blank sla definition")

# Release

Kingston and later

# Cause

The user is failing an ACL check on the contract\_sla table and cannot read the value.

# Resolution

This can be resolved by adding a new read ACL on the contract\_sla table. Please note that you must have activated security admin privileges to create new ACLs.

  
1) Navigate to System Security > Access Control (ACL)   
2) Click the blue New button in the list header to create a new entry   
3) Change the Operation value to: read   
4) In the first Name dropdown, select: SLA Definition \[contract\_sla\], leave the second dropdown empty   
5) Scroll down to the Requires role section and double click the Insert a new row... text   
6) Add the role you wish to grant access for  
7) Save the record

## Related

- [[KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow]] — explains the table/field ACL evaluation order behind this issue
- [[KB0753582 - The non-admin users are not able to access to a table]] — same table-level read ACL root cause pattern
- [[KB0759218 - Certain fields are visible to non-admin users only when the fields not empty.]] — another field-visibility ACL edge case
- [[access-control-rules]] — official docs on ACL rule configuration
