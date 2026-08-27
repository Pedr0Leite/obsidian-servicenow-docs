---
title: "Flow designer - problems accessing system tables (sys_email, sys_journal_entry, sys_audit and sys_history_set) from a scoped app."
aliases:
  - KB0787435
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787435
kb_number: KB0787435
last_modified: 2024-04-08
---

## Flow designer - problems accessing system tables (sys\_email, sys\_journal\_entry, sys\_audit and sys\_history\_set) from a scoped app.

  

### Issue

How to access sys\_email table from scoped app in a flow designer

### Cause

This was a conscious decision made by our dev team for security reasons to prevent the misuse of system tables from scoped applications.

Accessing system tables in Flow Designer can cause unintended system wide consequences, especially since flows can be executed with elevated privileges (Run As System).

### Resolution

If you would still like to execute actions against system tables, you must create custom actions and try to modify from script
