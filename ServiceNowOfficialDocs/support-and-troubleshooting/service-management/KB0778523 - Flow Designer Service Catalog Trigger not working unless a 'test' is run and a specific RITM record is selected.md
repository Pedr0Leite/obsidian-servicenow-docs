---
title: "Flow Designer Service Catalog Trigger not working unless a  'test' is run and a specific RITM record is selected"
aliases:
  - KB0778523
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778523
kb_number: KB0778523
last_modified: 2025-05-15
---

## Flow Designer Service Catalog Trigger not working unless a 'test' is run and a specific RITM record is selected

  

### Issue

The user is trying to convert their system from using workflows to using flow designer, but they are facing issues getting their flows to work for Service Catalog.

### Cause

There is no method in the user's system to approve parent Request records. Without an approval being processed on the parent Request record, no approval gets passed down to the child RITM to kick off the Flow the user designed (per Business Rule "Cascade Request Approval to Request Item" on sc\_request).

### Resolution

Typically, the above-mentioned process is handled through the Out of Box (OOB) "Service Catalog Request" workflow which processes an automatic approval if the price of the ordered item is less than $1000.00.  
  
The user can create their own Flow on the sc\_request table, with their own parameters, to handle such an automatic process. This will ensure that the user's sc\_req\_item (RITM) Flows will kick off each time without issue.

For the user's convenience, attached to this Knowledge article is the OOB "Service Catalog Request" workflow so that they (or any user) can examine it and build their flow to model it, then customize it according to their needs.
