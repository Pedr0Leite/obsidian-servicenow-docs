---
title: "Import - Field map does not correctly set the target field which is configured with a Choice List"
aliases:
  - KB0818197
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818197
kb_number: KB0818197
last_modified: 2024-04-08
---

## Import - Field map does not correctly set the target field which is configured with a Choice List

  

### Issue

When running imports against a target record field which is configured with a Choice List, it does not update the field with the correct value.

### Release

All ServiceNow platform releases.

### Resolution

-   If you're utilizing a source script on your Field map, implement the script to return the Label of the option in Choice List.
-   If it's possible, adjust the data source to have Label in the source data, so that you can use Field map with a direct Source to Target mapping.
