---
title: "Users can not edit On-Call shifts"
aliases:
  - KB0783335
tags:
  - servicenow
  - support-kb
  - acl
  - express-acl
  - on-call
  - on-call-scheduling
  - rota
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783335
kb_number: KB0783335
last_modified: 2024-04-20
---

## Issue

A user that had both _rota\_manager_ and _rota\_admin_ can not edit the shift members. On the modal popup to edit the members, no user is listed.

## Resolution

In some rare cases we do see conflicting issues with Express ACLs. These are denoted by the field '**Express security**' set to true. You can safely disable this ACL to resolve the behavior.

## Related

- [[KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow]] — general ACL evaluation background
- [[KB0861944 - On-Call users using default system schedules can cause SLA issues]] — another On-Call scheduling issue
- [[c_OnCallScheduling]] — official docs on On-Call Scheduling configuration and rota roles
