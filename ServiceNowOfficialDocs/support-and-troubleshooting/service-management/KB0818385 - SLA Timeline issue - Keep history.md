---
title: "SLA Timeline issue - Keep history"
aliases:
  - KB0818385
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818385
kb_number: KB0818385
last_modified: 2026-05-21
---

## SLA Timeline issue - Keep history

  

### Issue

You have reported an issue whereby you are noticed an issue in the SLA Timeline after instance upgrade.  
The SLAs which are "out of time" appear in red from the start, and they were green, then orange, then red, depending on the different thresholds crossed.  
You request to keep the history of SLA incident states/color according to the states by which it happened.

### Release

N/A

### Cause

The TaskSLA and SLACalculatorNG Script Includes were customized and using Custom Versions

### Resolution

Issue was resolved after merging with OOB.

They have modified these customized files to include the OOB code that has been missed out while still keeping their customizations.  
This has now resolved the issue.
