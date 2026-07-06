---
title: "Additional Comments field missing for Watch List users"
aliases:
  - KB0721299
tags:
  - servicenow
  - support-kb
  - acl
  - watch-list
  - additional-comments
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0721299
kb_number: KB0721299
last_modified: 2024-04-07
---

## Issue

Additional Comments field missing for Watch List users

## Resolution

Add OR condition on table write ACL where "Watch list IS (dynamic) Me"

## Related

- [[KB0749174 - Customization considerations for Access Controls (ACLs)]]
- [[KB0746724 - Reference field is hidden from layout]]
- [[access-control-rules]] - official docs on ACL rule evaluation
