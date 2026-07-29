---
title: "Change requests fields are not editable for the users with the change_manager role"
aliases:
  - KB0814752
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814752
kb_number: KB0814752
last_modified: 2026-07-02
---

## Issue

Some custom ACLs have been defined on the change\_request form, so that users with role either admin or change\_manager will be able to edit the fields on the change request, irrespective of its state. However, the form was found showing read-only for the users with change\_manager role.

## Resolution

In such scenarios, it is a good approach to search all the client scripts active on the affected table, looking for scripts containing the role name. Debugging security and JS will show if ACLs are not blocking access and the client-side code actions.
