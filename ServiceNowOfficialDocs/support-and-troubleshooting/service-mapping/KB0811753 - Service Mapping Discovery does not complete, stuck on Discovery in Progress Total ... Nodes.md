---
title: "Service Mapping Discovery does not complete, stuck on \"Discovery in Progress: Total ... Nodes\""
aliases:
  - KB0811753
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0811753
kb_number: KB0811753
last_modified: 2024-04-08
---

## Service Mapping Discovery does not complete, stuck on "Discovery in Progress: Total ... Nodes"

  

### Issue

When running Discovery on Application Service Map, the Discovery does not complete, and a message like below is showing on the map:

![](/sys_attachment.do?sys_id=2c7e7b78db40f0d016d2a345ca96199c)

### Cause

sysauto\_script "Update Business Service Status" might have been turned off

### Resolution

Check sa\_endpoint\_status table, and make sure the state of all entries are marked as complete.

Then check sysauto\_script "Update Business Service Status", make sure it's active.
