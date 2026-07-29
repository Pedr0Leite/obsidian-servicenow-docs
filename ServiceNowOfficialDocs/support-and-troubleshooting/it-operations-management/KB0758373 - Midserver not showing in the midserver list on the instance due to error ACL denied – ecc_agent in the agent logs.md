---
title: "Midserver not showing in the midserver  list on the instance due to error  ACL denied – ecc_agent in the agent logs"
aliases:
  - KB0758373
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0758373
kb_number: KB0758373
last_modified: 2024-04-07
---

## Issue

Installing a new midserver does not create a record in ecc\_agent table on the instance.Although the midserver service is up and running.

## Resolution

Removing all the extra roles other than role mid\_server, solved the issue.
