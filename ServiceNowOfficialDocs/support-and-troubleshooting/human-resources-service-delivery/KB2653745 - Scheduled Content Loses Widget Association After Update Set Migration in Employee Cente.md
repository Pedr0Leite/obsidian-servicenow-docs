---
title: " Scheduled Content Loses Widget Association After Update Set Migration in Employee Cente"
aliases:
  - KB2653745
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2653745
kb_number: KB2653745
last_modified: 2026-01-01
---

## Scheduled Content Loses Widget Association After Update Set Migration in Employee Cente

  

### Issue

When moving update sets with Employee Center Pro page/container changes from DEV to TEST or PROD, published content (e.g., News Feed widget articles) may become dissociated from widgets, even though the widget itself is not replaced or recreated.

### Release

Any

### Cause

If a widget instance is moved from one container to another and the original container is deleted in the same update set, a business rule may delete the widget instance prematurely, causing Schedule Content records to lose their widget association.

### Resolution

-   Split the process into two separate update sets:
    1.  First update set: Create the new container and move the widget.
    2.  Second update set: Delete the old container.
-   This approach ensures the widget instance remains intact and content associations are preserved during migration.
-   Validate changes in a non-production environment before applying to production.
