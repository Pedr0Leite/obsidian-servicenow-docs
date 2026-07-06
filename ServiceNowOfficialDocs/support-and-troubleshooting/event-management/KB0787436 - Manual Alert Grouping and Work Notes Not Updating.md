---
title: "Manual Alert Grouping and Work Notes Not Updating"
aliases:
  - KB0787436
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787436
kb_number: KB0787436
last_modified: 2024-04-08
---

## Issue

When alerts are linked (parent/child) manually, work notes for both parent and child should contain a system reference in the Activity stream. This isn't working.

## Resolution

The work notes get generated only for **automated grouping of alerts** when you have the system property "**evt\_mgmt.alert\_groups\_reasoning.enable\_worknotes**" set to "all".
