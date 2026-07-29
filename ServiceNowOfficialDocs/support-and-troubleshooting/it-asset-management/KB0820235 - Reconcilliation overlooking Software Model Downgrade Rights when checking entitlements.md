---
title: "Reconcilliation overlooking Software Model Downgrade Rights when checking entitlements"
aliases:
  - KB0820235
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0820235
kb_number: KB0820235
last_modified: 2024-04-08
---

## Issue

After defining downgrade rights in the parent software model with available entitlements the over-allocated rights for the child (downgrade) software model is not being counted against the (upgrade) parent software model entitlement in the reconciliation process. 

## Resolution

This is expected out-of-the-box behavior. If you wish to change this please create a new business rule copy the relevant parameters and modify the script by modifying/removing the condition test in the if clause then deactivate the OOB business rule.  Please note that this is a customization and is out of support scope.  As always you take responsibility for validating and testing changes in sub-production prior to promoting the same change in production.
