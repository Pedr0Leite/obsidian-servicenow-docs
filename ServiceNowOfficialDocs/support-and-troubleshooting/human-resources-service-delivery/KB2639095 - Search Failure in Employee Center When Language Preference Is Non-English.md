---
title: "Search Failure in Employee Center When Language Preference Is Non-English"
aliases:
  - KB2639095
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2639095
kb_number: KB2639095
last_modified: 2026-01-01
---

## Search Failure in Employee Center When Language Preference Is Non-English

  

### Issue

When users change their language preference to any language other than English in the Employee Center portal, performing a topic search on the `emp_taxonomy_topic_it` page causes the system to hang and no results are returned. The issue does not occur when the language is set to English.

### Release

Xanadu

### Cause

A product defect in AI Search indexing for non-English user preferences caused the search functionality to fail when translated fields were indexed.

### Resolution

-   Verified issue by impersonating users and testing across multiple SNC instances.
-   Attempt workarounds:
    -   Updated plugins
    -   Add entries to `sys_translated_text`
    -   Reindex catalog and knowledge tables
    -   Adjust user language preferences
-   Identified root cause as product defect PRB1823459.
-   Applied Xanadu Patch 8 Hot Fix 3 to affected instances.
-   Performed catalog reindex after applying the fix.
-   Set AIS indexed source attribute `index_translated_fields` to false for catalog items.
