---
title: "Transfer Order Line remains in Draft and does not create tasks when TransferOrderLineTemplateTaskAPI is customized not on latest OOB version"
aliases:
  - KB2750231
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2750231
kb_number: KB2750231
last_modified: 2026-01-31
---

## Issue

● Transfer Order Line does not create Transfer Order Line Tasks and remains in Draft state

## Resolution

● Review the Script Include TransferOrderLineTemplateTaskAPI and verify it matches the OOB version  
● If it is customized or outdated, revert TransferOrderLineTemplateTaskAPI back to the OOB baseline  
● Re-test by creating a new Transfer Order and Transfer Order Line and validate  
↳ alm\_transfer\_order\_line\_task records are created  
↳ Transfer Order Line progresses through the expected stages
