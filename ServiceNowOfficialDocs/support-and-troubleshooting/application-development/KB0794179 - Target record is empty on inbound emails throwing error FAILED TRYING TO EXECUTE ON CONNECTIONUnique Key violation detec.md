---
title: "Target record is empty on inbound emails throwing error FAILED TRYING TO EXECUTE ON CONNECTION/Unique Key violation detected by database"
aliases:
  - KB0794179
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0794179
kb_number: KB0794179
last_modified: 2024-04-07
---

## Issue

Target record is empty on inbound emails throwing error FAILED TRYING TO EXECUTE ON CONNECTION/Unique Key violation detected by database

## Resolution

Remove current.update from on-before business rule on sys\_email table (as it's firing on "before" so, it's not needed) should fix the issue.
