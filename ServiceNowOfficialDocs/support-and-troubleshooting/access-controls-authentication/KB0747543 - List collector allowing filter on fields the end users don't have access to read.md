---
title: "List collector allowing filter on fields the end users don't have access to read"
aliases:
  - KB0747543
tags:
  - servicenow
  - support-kb
  - acl
  - field-level-acl
  - list-collector
  - text-search
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0747543
kb_number: KB0747543
last_modified: 2024-04-07
---

## List collector allowing filter on fields the end users don't have access to read

  

### Issue

# Symptoms

List collector and table list allowing filter on fields the end users don't have access to read

# Release

All releases

# Cause

Expected behavior

# Resolution

This behavior is addressed in PRB1259457 - ACLs do not apply to the search in the list view and in the global text search. Though the PRB address this issue in List. Our development team has deemed this PRB as "working as expected" with the following reason. "Field-level ACLs are evaluated for the display of content, but do not have any impact on the actual text search. Fields with sensitive content can be excluded from being indexed." 

# Additional Information

In the screenshot below. ITIL user is not able to see the value in the SSN field but is able to search and return a value.

![](/sys_attachment.do?sys_id=de0d6062db82b450e515c22305961924)

## Related

- [[KB0727211 - FAQ Can an ACL work on the list view and be bypassed on the related list (or vice versa)]]
- [[KB0749174 - Customization considerations for Access Controls (ACLs)]]
- [[acl-function-fields]] - official docs on field-level ACL behavior
