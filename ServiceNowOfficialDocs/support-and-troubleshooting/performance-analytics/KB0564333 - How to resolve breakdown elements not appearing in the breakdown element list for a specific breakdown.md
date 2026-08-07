---
title: "How to resolve breakdown elements not appearing in the breakdown element list for a specific breakdown"
aliases:
  - KB0564333
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0564333
kb_number: KB0564333
last_modified: 2026-04-16
---

## How to resolve breakdown elements not appearing in the breakdown element list for a specific breakdown

  

### Issue

Resolve breakdown elements not appearing in the breakdown element list for a specific breakdown in Performance Analytics.

When viewing scores for an indicator that uses a specific breakdown, no breakdown elements appear in the breakdown element list, even though the breakdown is configured and active.

### Release

All supported releases

### Cause

The number of breakdown elements for the affected breakdown exceeds the maximum value set by the `com.snc.pa.breakdown_element_cutoff` system property. When the element count exceeds this limit, no breakdown elements are displayed in the list.

### Resolution

> Warning: Increasing the number of visible breakdown elements may impact performance. Contact ServiceNow Technical Support before changing this property value.

To resolve this issue, update the `com.snc.pa.breakdown_element_cutoff` system property:

-   Set the property value to a number greater than the total number of breakdown elements you want to display.
-   Alternatively, clear the property value to allow any number of breakdown elements to display without a limit.
