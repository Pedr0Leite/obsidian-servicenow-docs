---
title: "Employee Documents Not Displaying in HR Agent Workspace Sidebar"
aliases:
  - KB2657370
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2657370
kb_number: KB2657370
last_modified: 2025-12-14
---

## Employee Documents Not Displaying in HR Agent Workspace Sidebar

  

### Issue

Employee document section in HR Agent Workspace sidebar shows inconsistent behavior—sometimes all documents appear, sometimes none—even when documents are linked to the case. Issue occurs across production and sub-production instances without customizations.

### Release

Any

### Cause

Known defect PRB1868773: Filter configuration fails when Variable Sets are present on the HR Case form in HR Agent Workspace.

### Resolution

Workaround: Remove the variable editor from the HR Case form to restore document visibility.

Permanent fix: Upgrade to Zurich release, where the defect is resolved.
