---
title: "Deprecated \"Templates\" Option Appearing in HR Agent Workspace After Upgrade"
aliases:
  - KB2639785
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2639785
kb_number: KB2639785
last_modified: 2025-12-16
---

## Deprecated "Templates" Option Appearing in HR Agent Workspace After Upgrade

  

### Issue

After upgrading the instance, the "Templates" option appeared in the context menu of HR Cases in Agent Workspace, even though it is marked as deprecated.  
This caused confusion during UAT sign-off and impacted readiness for production upgrade.

### Release

Any Release

### Cause

The Agent Workspace for HR Case Management plugin (version 4.0.x) includes deprecated UX App Route and Screen components from older record pages, which still apply to the current Case SRP page.

### Resolution

-   Navigate to HR Agent Workspace settings → Record > Contextual Side Panel > Sidebar Tabs visibility.
-   Remove table names under the Templates section.
-   Save changes to hide the deprecated Templates option from the sidebar.  
    Future platform updates will unmark these components as deprecated.
