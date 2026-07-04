---
title: "Knowledge Articles Missing After Language Switch in Employee Center"
aliases:
  - KB2630112
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2630112
kb_number: KB2630112
last_modified: 2026-01-01
---

## Knowledge Articles Missing After Language Switch in Employee Center

  

### Issue

-   Knowledge Base (KB) articles do not appear in the Topic Content section of the Employee Center portal.
-   Articles are attached to topics and show up in search suggestions, but are missing from topic pages.
-   Issue affects multiple topics and child topics, impacting user access to support resources.

### Release

Any Release

### Cause

-   The `kb_knowledge.language` field was missing in the Knowledge table.
-   This occurred due to an incomplete installation of the plugin:  
    `com.glideapp.knowledge.i18n2` (Knowledge Internationalization V2).
-   Without this field, Employee Center cannot properly filter and display articles by language.

### Resolution

1.  Verify the Issue:
    -   Check if KB articles are attached to topics but not visible in the portal.
    -   Confirm they appear in search results but not in topic content.
2.  Check Plugin Installation:
    -   Navigate to System Definition > Plugins.
    -   Search for com.glideapp.knowledge.i18n2.
    -   If the plugin shows as Installed, click Repair to ensure all components are correctly applied.
3.  Validate Language Field:
    -   Go to System Definition > Tables.
    -   Open Knowledge \[kb\_knowledge\] table.
    -   Confirm the Language field exists. If missing, repairing the plugin should restore it.
4.  Reindex Knowledge Table:
    -   Navigate to AI Search > Indexes.
    -   Select the Knowledge index and click Reindex to refresh search and topic content visibility.
5.  Test in Employee Center:
    -   Open a topic page and verify that KB articles now display correctly in the Topic Content section.
6.  Apply Fix to Other Instances:
    -   If the issue exists in Test or Production, repeat the above steps.
