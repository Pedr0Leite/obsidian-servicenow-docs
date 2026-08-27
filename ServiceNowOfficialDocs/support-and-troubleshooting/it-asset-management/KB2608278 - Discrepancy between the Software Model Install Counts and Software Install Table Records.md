---
title: "Discrepancy between the Software Model Install Counts and Software Install Table Records"
aliases:
  - KB2608278
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2608278
kb_number: KB2608278
last_modified: 2025-11-06
---

## Issue

Customers may observe mismatches between `software_install_count` on `cmdb_software_product_model` and ad-hoc counts taken directly from `cmdb_sam_sw_install`.

## Resolution

OOTB, we have a weekly scheduled job "SAM - Get install count for software model" which updates the number in the field  cmdb\_software\_product\_model.sam\_install\_count.   
  

If the customers want the number to reflect immediately, they can run this job on demand.
