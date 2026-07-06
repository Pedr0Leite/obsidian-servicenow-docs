---
title: "Users do not see ticket information after ordering a catalog item"
aliases:
  - KB0746144
tags:
  - servicenow
  - support-kb
  - acl
  - business-rule
  - service-catalog
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746144
kb_number: KB0746144
last_modified: 2024-04-07
---

## Users do not see ticket information after ordering a catalog item

  

### Issue

# Symptoms

Users do not see ticket information on the ticket page after ordering a catalog item

# Release

All Supported Releases

# Cause

The user does not have access to the record created. The access can be restricted by a Business Rule or ACL

# Resolution

Find ACL or Business Rule restricting access to the record, Disable or change criteria to provide proper access.

## Related

- [[KB0748114 - Users see a No Matches Found on catalog item variable]]
- [[KB0749174 - Customization considerations for Access Controls (ACLs)]]
- [[c_BusinessRules]] - official docs on business rules
