---
title: "Business Rule not firing on insert"
aliases:
  - KB0999137
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0999137
kb_number: KB0999137
last_modified: 2025-10-14
---

## Business Rule not firing on insert

  

### Issue

The user had a two-fold issue with their Business Rule (BR) not firing:

-   The BR would not fire on insert when the record was inserted per the Platform UI
-   The BR would not fire on insert when the record was inserted per the user's integration

### Cause

The causes were as follows:

-   With the manual record insert via the Platform UI, the BR was not running due to its condition not being met. Hence, it skipped. This was isolated per the "Debug Business Rules (Details)" module
-   With the integration insert failing, this was due to case-sensitivity between was was sent to the system and what was required for the BR to run

### Resolution

In each scenario, the customer was counseled to adjust their BR to align with their process. For example, ensure that any technician inserting a record manually via the Platform UI needs to do this X way, and whenever an integration inserts a record per the code it is sending into the ServiceNow instance, that code needs to be consistently formatted in Y way to faithfully trigger the BR.

When these adjustments were made, the behavior resolved in both scenarios.
