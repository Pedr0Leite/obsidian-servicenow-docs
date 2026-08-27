---
title: "HR Case Transfer - Error Message"
aliases:
  - KB0858327
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0858327
kb_number: KB0858327
last_modified: 2025-09-03
---

## Issue

Sometimes for a user when HR case is transferred, they get - duplicate key violation

java.sql.BatchUpdateException: (conn=79826) Duplicate entry 'xxx4f3a1bf9d450c49c628f7b4bcb57' for key 'PRIMARY'

## Resolution

StandardCaseTransfer" and "ReclassifyCaseTransfer" were customized , reverting to OOB fixed the issue
