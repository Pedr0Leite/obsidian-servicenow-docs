---
title: "Inconsistent SAM Reconciliation Across Environments for Not Licensable Software Models and LMR Consumption Visibility for Excluded Products"
aliases:
  - KB2757751
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2757751
kb_number: KB2757751
last_modified: 2026-02-04
---

## Issue

The customer observed inconsistent reconciliation behavior across environments for certain software models marked as Not Licensable. In one environment, LMRs/SMRs showed no consumption and compliance, while in the other environment, the same product showed license usage and non-compliance. The customer also requested guidance on tracking consumption details in LMR for software models excluded via Product License Exception Rules.

## Resolution

Resolution:   
\-------------  
\-- Confirmed the observed behavior aligns with expected SAM design (once the PRB is addressed)  
\-- Validated that Product License Exception Rules marked as Not Licensable correctly exclude installs/subscriptions from consumption, resulting in no rights consumed in LMR and compliant SMRs  
\-- Aligned editions/DMAPs across environments and updated License under management to false where applicable  
\-- Clarified that SAM does not support tracking license consumption for software models that are excluded as Not Licensable  
  
Workaround (optional, visibility only):  
\----------------  
\-- Re-enable LUM and use a zero-cost, unlimited entitlement, with the understanding that this re-introduces the product into licensing/reconciliation logic.  
  
The related PRB1979864 is expected to be addressed in the Brazil release. We request that you wait for the Brazil release for the permanent fix.
