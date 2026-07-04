---
title: "COE Field Does Not Update on HR Case Creation Page After Agent Workspace Upgrade to v3.1.3"
aliases:
  - KB2636346
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2636346
kb_number: KB2636346
last_modified: 2026-01-01
---

## COE Field Does Not Update on HR Case Creation Page After Agent Workspace Upgrade to v3.1.3

  

### Issue

After upgrading HR Agent Workspace to version 3.1.3, the HR case creation page is broken. Specifically, the COE field does not update when the HR Service is changed. The issue persists even when reverting to out-of-box (OOB) configuration and affects multiple users.

### Release

Any Release

### Cause

The issue is caused by a defect in HR Agent Workspace v3.1.3 and v3.1.5, impacting the dynamic update of the COE field on the case creation page. This is not related to customer-specific customizations.

### Resolution

To resolve the issue:

-   Upgrade HR Agent Workspace

-   -   The fix for this issue is included in SR - HR - HR Agent Workspace v4.1.
    -   Upgrade to v4.1 or later to restore COE field functionality.

-   PRB Reference

-   -   Problem Record: PRB1843265
    -   Status: Fixed in HR Agent Workspace v4.1.

-   Workaround

-   -   There is currently no workaround available for earlier versions.

-   Validation

-   -   After upgrading, verify that the COE field updates correctly when changing the HR Service on the case creation page.
