---
title: "How to prevent creation of duplicate assets from Purchase order"
aliases:
  - KB2538388
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2538388
kb_number: KB2538388
last_modified: 2025-09-30
---

## How to prevent creation of duplicate assets from Purchase order

  

### Summary

When receiving a Purchase Order, how to prevent the creation of duplicate assets if an asset with the same serial number already exists, then the action should be aborted.

### Release

All

### Instructions

Out of the box, ServiceNow provides the property `glide.asset.create_ci_with_ire`, which enables CIs to be created from assets using the CMDB Identification and Reconciliation Engine (IRE).

This property applies to CI classes that have an identification rule on serial number and no dependent relationships with other CI classes.

When the property is set to true, during the PO receive process, the system checks for an existing CI with the same serial number as soon as the details are submitted. If a match is found, the submit action is aborted, preventing duplicate asset creation.
