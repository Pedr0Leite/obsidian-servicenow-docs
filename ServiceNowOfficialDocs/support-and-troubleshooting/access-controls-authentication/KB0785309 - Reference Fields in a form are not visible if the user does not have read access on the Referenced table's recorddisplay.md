---
title: "Reference Fields in a form are not visible if the user does not have read access on the Referenced table's record/display field"
aliases:
  - KB0785309
tags:
  - servicenow
  - support-kb
  - acl
  - reference-fields
  - dot-walking
  - display-field
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785309
kb_number: KB0785309
last_modified: 2024-04-08
---

## Reference Fields in a form are not visible if the user does not have read access on the Referenced table's record/display field

  

### Issue

Reference Fields in a form are not visible if the user does not have read access on the Referenced table's record/display field. For example: if a form contain the field "cpu\_manufacturer", the field will not be visible if the user does not have read access to the "core\_company" table

### Release

All release

### Cause

User does not have read access to the Referenced table's record/display field

### Resolution

User needs to have read access to the referenced table's record/display field.

## Related

- [[KB0755717 - Non-itil users cannot see a read-only field on the catalog task which is extended from the request table.]] — same dot-walk/reference read-access pattern
- [[KB0759218 - Certain fields are visible to non-admin users only when the fields not empty.]] — related reference-row-check ACL behavior
- [[r_ContScriptCondAppRefFld]] — official docs on applying ACL script conditions to reference fields
