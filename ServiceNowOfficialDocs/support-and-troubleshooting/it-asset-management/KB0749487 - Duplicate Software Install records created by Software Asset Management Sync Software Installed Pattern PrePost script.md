---
title: "Duplicate Software Install records created by Software Asset Management \"Sync Software Installed\" Pattern Pre/Post script"
aliases:
  - KB0749487
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749487
kb_number: KB0749487
last_modified: 2024-04-07
---

## Issue

Duplicate Software Install records created by Software Asset Management "Sync Software Installed" Pattern Pre/Post script

Example Issue: Duplicate "SQL Server Standard Edition (64-bit)" Software Install record is being created every time the node is discovered.

## Resolution

WorkAround: Navigate to Configuration -> Reconciliation Definitions  -> Search Applies to \[ MSFT SQL Instance \] (for above example) . Add 'version' and 'edition' attributes
