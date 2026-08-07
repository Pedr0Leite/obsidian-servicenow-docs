---
title: "How unlicensed_install field is set in SAMP"
aliases:
  - KB0951763
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0951763
kb_number: KB0951763
last_modified: 2025-01-03
---

## How unlicensed\_install field is set in SAMP

  

### Summary

This article explains how unlicensed\_install field is populated.

### Release

All releases with Software Asset Management Professional **SAMP** installed.

### Instructions

-   There is a Business Rule on **Software** **Discovery** **Model** table called _**U**__**pdate install with product information**_. This Business rule populates _norm\_publisher_ and _norm\_product_ fields value on **Software** **Installations** table.
-   If this product is non-licensable, it will leave these 2 fields empty and therefore, reconciliation will skip them and leave _unlicensed\_install_ field set as false. If however, these 2 fields are populated then, these software installation records will go through reconciliation and will set _unlicensed\_install_ as true.

### Related Links

There is a scheduled job called **_SAM - Apply latest content change_s.** This job traverses all Content tables starting from **Publisher** samp\_sw\_publisher and **Product** samp\_sw\_product tables to apply any changes we have to all the Out of the box Publishers and Products. If this job is failing, it could lead to having incorrect _unlicensed\_install_ field.

You can check the progress and previous executions of this Job from Software Asset > Administration > Job Results
