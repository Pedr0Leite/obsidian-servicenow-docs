---
title: "Frequently Used Apps Not Displaying on HR Agent Workspace Landing Page"
aliases:
  - KB2627068
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2627068
kb_number: KB2627068
last_modified: 2026-01-03
---

## Frequently Used Apps Not Displaying on HR Agent Workspace Landing Page

  

### Issue

-   Frequently used apps do not appear on the HR Agent Workspace landing page.
-   Link content and scheduled content were created, and content IDs matched in UI Builder and content group, but links did not display.
-   Issue often occurs after cloning or customizing the workspace.

### Release

Any Release

### Cause

-   The Link Set Group component was missing from the Frequently Used Apps column in the HR Agent Workspace layout.
-   This component is part of the Out-of-Box (OOB) configuration and may be accidentally deleted during cloning or customization.

### Resolution

1.  Open UI Builder and navigate to the HR Agent Workspace landing page.
2.  Verify if the Link Set Group component exists in the Frequently Used Apps column.
3.  If missing, re-add the Link Set Group component:
    -   Bind it to the getMyFrequentlyUsedAppsContent data resource.
    -   Configure the Link set items field correctly.
4.  For newer UI Builder versions, use:
    
    ```
    @data.getmyfrequentlyusedappscontent.output.result
    ```
    
5.  Clear UI Builder cache and refresh the workspace.
6.  If migrating between instances, consider using update sets or manual configuration.

Outcome:  
Frequently used apps display correctly on the HR Agent Workspace landing page.
