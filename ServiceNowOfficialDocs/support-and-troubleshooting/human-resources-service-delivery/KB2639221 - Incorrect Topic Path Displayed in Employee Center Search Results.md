---
title: "Incorrect Topic Path Displayed in Employee Center Search Results"
aliases:
  - KB2639221
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2639221
kb_number: KB2639221
last_modified: 2026-01-01
---

## Incorrect Topic Path Displayed in Employee Center Search Results

  

### Issue

When searching for requests in Employee Center, the results display an incorrect topic path for catalog items. The topic path order shown in search results does not match the expected hierarchy, affecting items such as “NA - New Plant Request.” The customer requested correction of the topic path display in the Employee Center portal.

### Release

Any Release

### Cause

The issue was due to incorrect mapping in the EVAM view template, where `textHeaderLabelTwo` was mapped to `topics` instead of `taxonomy_topic.topic_path`.

### Resolution

-   Navigate to the EVAM view template configuration.
-   Update the mapping for `textHeaderLabelTwo` to reference taxonomy\_topic.topic\_path instead of `topics`.
-   Validate the changes by performing a search in Employee Center and confirming the correct topic path hierarchy is displayed.
-   Optionally, apply the same update in production or wait for the official patch addressing PRB1820709.
