---
title: "Cases are being created with no assignment group"
aliases:
  - KB0790090
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790090
kb_number: KB0790090
last_modified: 2024-04-08
---

## Cases are being created with no assignment group

  

### Issue

Some HR cases are created and not routed to the correct group via assignment rules.

### Release

All Releases.

### Cause

The assignment rules are primarily based on the user's country; however, the country field was empty when the case was created.

### Resolution

Create an assignment rules to handle the occurrences of these issues to auto route HR cases where the user does not have their country field populated.
