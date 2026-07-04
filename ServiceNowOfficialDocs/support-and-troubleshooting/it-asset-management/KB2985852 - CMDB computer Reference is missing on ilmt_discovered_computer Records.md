---
title: "CMDB computer Reference is missing on ilmt_discovered_computer Records"
aliases:
  - KB2985852
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2985852
kb_number: KB2985852
last_modified: 2026-05-21
---

## Issue

CMDB computer Reference is missing on ilmt\_discovered\_computer Records

## Resolution

Ensure that the particular Configuration Item (CI) is having the Serial Number Type labeled as "system" within the cmdb\_serial\_number table, since the out-of-the-box (OOB) script include named **SamILMTTransformHandler** specifically uses the system type Serial Number to generate the corresponding reference CMDB computer record in the ilmt\_discovered\_computer table.
