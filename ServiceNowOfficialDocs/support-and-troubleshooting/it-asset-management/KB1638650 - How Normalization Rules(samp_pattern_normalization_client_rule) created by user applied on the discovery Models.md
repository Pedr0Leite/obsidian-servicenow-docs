---
title: "How Normalization Rules(samp_pattern_normalization_client_rule) created by user applied on the discovery Models"
aliases:
  - KB1638650
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1638650
kb_number: KB1638650
last_modified: 2024-04-03
---

## How Normalization Rules(samp\_pattern\_normalization\_client\_rule) created by user applied on the discovery Models

  

### Summary

1.  ServiceNow has two kinds of Normalization Rules for normalizing discovery models,
    -   The Normalization rules (and pattern rules) shipped by our content team
    -   Normalization Rules setup by users (samp\_pattern\_normalization\_client\_rule). 
2.  For a discovery model to be normalized based on the Normalization Rules newly added by users, a Discovery model needs to be in a "missed/ match not found" or "partially normalized or "publisher normalized" state.
3.  If the Discovery Model is "Manually Normalized" the only way for the user to update the version on the discovery model is to manually update it. We are currently evaluating an enhancement to automate this process using the customer-added normalization rules however at the moment there is no certainty to when it might be available.
4.  The system would try to normalize the discovery using the OOB maps/ rules. After applying the OOB rule if discovered is not in "Normalized" status, then the pattern rules are executed on the discovery model.
5.  For custom pattern rules, we need to click on the "Apply rule" button on "Pattern Normalization Rule" which needs to be applied and the rule will be applied on the Discovery model's that has "missed/ match not found" or "partially normalized or "publisher normalized" state.
