---
title: "samp_country records in Software Asset Management"
aliases:
  - KB2773293
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2773293
kb_number: KB2773293
last_modified: 2026-05-18
---

## samp\_country records in Software Asset Management

  

 

## Overview

The `samp_country` table stores country records used for grouping during Software Asset Management (SAM) Reconciliation. These records are created automatically when you select Country as a grouping option during the reconciliation process.

## How samp\_country records are created

When SAM Reconciliation runs with country grouping enabled, the system uses the `sn_itam_samp.GroupingUtil` script include to perform the following steps:

1.  Collect unique country values from the `country` field on the Location \[cmn\_location\] table.
2.  Search for matching records in the `samp_country` table by comparing the `name` field.
3.  Return or create records based on the search results:
    -   If a matching `samp_country` record exists, the system returns the first matching record.
    -   If no matching record exists, the system creates a new `samp_country` record with the `name` field set to the country value from the Location \[cmn\_location\] table.

## Important considerations

### Duplicate country records

Because the process relies on exact matching of unique values from the `country` field in the Location \[cmn\_location\] table, data inconsistencies can create multiple `samp_country` records representing the same country.

**Example:** If your Location records contain different variations such as `UK` and `United Kingdom`, the system treats these as distinct values and creates a separate `samp_country` record for each variation.

To prevent this, regularly review the `country` field in the Location \[cmn\_location\] table for duplicate or inconsistent values before running reconciliation.

## Related Links

-   [Reconciliation of licenses across global entities](https://www.servicenow.com/docs/r/it-asset-management/software-asset-management/reconcile-licenses-global-entities.html)
