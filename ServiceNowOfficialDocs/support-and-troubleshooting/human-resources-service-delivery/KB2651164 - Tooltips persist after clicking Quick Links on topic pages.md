---
title: "Tooltips persist after clicking Quick Links on topic pages"
aliases:
  - KB2651164
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2651164
kb_number: KB2651164
last_modified: 2026-01-01
---

## Tooltips persist after clicking Quick Links on topic pages

  

### Issue

On the Employee Center portal, tooltips associated with Quick Links do not disappear after clicking the link, causing them to linger unnecessarily on the screen.  
This issue occurs under the Topic/Sub-Topic Page, specifically with the Quick Links on Topic Page widget.  
The behavior is reproducible in both Employee Center and Service Portal environments, impacting user experience.

### Release

Any

### Cause

The issue is caused by a product defect tracked under PRB1907440. Initial investigation linked it to PRB1732384, but upgrading the Employee Center plugin did not resolve the problem.

### Resolution

-   A permanent fix is included in Employee Center Bundle v38.0.2, scheduled for release at the end of July 2025.
-   Upgrade the Employee Center application to v38.0.2 or later to resolve the issue.
-   Track PRB1907440 for updates on the fix.
