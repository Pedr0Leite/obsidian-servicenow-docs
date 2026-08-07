---
title: "HR Case List Columns Show Empty in HR Agent Workspace Until Hover – ACL Enforcement"
aliases:
  - KB2657273
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2657273
kb_number: KB2657273
last_modified: 2026-01-01
---

## HR Case List Columns Show Empty in HR Agent Workspace Until Hover – ACL Enforcement

  

### Issue

In HR Agent Workspace (Yokohama release), HR Case list columns display as empty until a user hovers over a row. Correct values appear on hover and are visible when opening the record.  
All data is present in record details, but not in the list view.  
The issue is specific to HR Agent Workspace; other UI views (e.g., UI16) do not exhibit this behavior.

### Release

Yokohama

### Cause

In Agent Workspace list view, Access Control Lists (ACLs) on the referenced HR Case table (`sn_hr_core_case`) are enforced. If a user lacks read access to the referenced HR Case, the field appears empty in the list view.  
In form view, ACLs are not enforced at the field level, so the HR Case number may be visible even if the user cannot access the full record.

### Resolution

-   Grant read access to the `sn_hr_core_case` table for relevant HR Agent roles.
-   Verify that HR Case list columns display correctly in Agent Workspace after updating ACLs.
