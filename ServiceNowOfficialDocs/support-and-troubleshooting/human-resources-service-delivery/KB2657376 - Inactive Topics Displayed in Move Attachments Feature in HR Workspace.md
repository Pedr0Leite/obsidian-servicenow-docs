---
title: "Inactive Topics Displayed in Move Attachments Feature in HR Workspace"
aliases:
  - KB2657376
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2657376
kb_number: KB2657376
last_modified: 2026-01-02
---

## Inactive Topics Displayed in Move Attachments Feature in HR Workspace

  

### Issue

The Move Attachments feature in HR Workspace displays inactive Topic Details, which is not desired. Customer requested that only active topics with at least one active document type be shown.

### Release

Any

### Cause

Logic in `hr_UIBMoveAttachmentsUtilsSNC` script include and macroponent’s encodedQuery returned all topics, including inactive ones.

### Resolution

Update `getTopicDetails()` function in `hr_UIBMoveAttachmentsUtilsSNC` to return only active topics.

Add filter in macroponent’s data query to ensure only active topics display after UI changes.

Track fix under PRB1921177; permanent solution included in HR Agent Workspace v4.3 (Dec 2025).

Move changes to Test and Production using an Update Set.
