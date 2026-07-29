---
title: "Updates are not being applied on an update set despite everything showing as committed successfully."
aliases:
  - KB0690757
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0690757
kb_number: KB0690757
last_modified: 2024-04-07
---

## Updates are not being applied on an update set despite everything showing as committed successfully.

  

### Issue

Updates are not being applied on an update set despite everything showing as committed successfully.

#   

### Release

Istanbul+

### Cause

Duplicate sys\_id updates are contained on the update set, causing issues upon commit.

### Resolution

1.  Query for update sets with the same sys\_id.
2.  Remove the duplicate update sets.
3.  Once the duplicates are removed, recommit the main update set.

#
