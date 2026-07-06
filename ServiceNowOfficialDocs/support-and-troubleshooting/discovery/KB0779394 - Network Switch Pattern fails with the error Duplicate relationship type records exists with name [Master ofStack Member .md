---
title: "Network Switch Pattern fails with the error \"Duplicate relationship type records exists with name [Master of::Stack Member of] in table [cmdb_rel_type] having sys_ids: \""
aliases:
  - KB0779394
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779394
kb_number: KB0779394
last_modified: 2024-04-07
---

## Issue

During an IP switch Discovery, the Network Switch pattern fails with the below error :

Duplicate relationship type records exists with name \[Master of::Stack Member of\] in table \[cmdb\_rel\_type\] having sys\_ids:<sys\_id1>,<sys\_id2>

## Resolution

Delete the duplicate record in the cmdb\_rel\_type table and make sure there is only one record with sys\_name as "Master of:: Stack Member of"
