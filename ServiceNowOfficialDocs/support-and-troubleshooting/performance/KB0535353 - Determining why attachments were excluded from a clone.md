---
title: "Determining why attachments were excluded from a clone"
aliases:
  - KB0535353
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535353
kb_number: KB0535353
last_modified: 2025-01-22
---

## Determining why attachments were excluded from a clone

  

### Issue

Sometimes you will find that attachments are missing after a clone. Some of the symptoms are:

-   Some attachments are available in the target instance after the clone, but not all.
-   Attachments missing after a clone.

### Release

Any

### Cause

Attachments missing after performing a clone are typically the result of having the **Exclude large attachment data** option selected.

### Resolution

To determine if this is selected in your instance:

1.  Type "Clone" into the navigation filter.
2.  Click **Clone History**.
3.  Sort **Created Z to A** and locate the last clone requested.
4.  Open the record.
5.  De-select **Exclude large attachment data** if it was selected and re-run the clone.
