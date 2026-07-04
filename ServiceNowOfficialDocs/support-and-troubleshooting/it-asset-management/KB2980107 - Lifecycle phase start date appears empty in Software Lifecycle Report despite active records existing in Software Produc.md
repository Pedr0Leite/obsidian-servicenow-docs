---
title: "Lifecycle phase start date appears empty in Software Lifecycle Report despite active records existing in Software Product Lifecycles table"
aliases:
  - KB2980107
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2980107
kb_number: KB2980107
last_modified: 2026-04-29
---

## Lifecycle phase start date appears empty in Software Lifecycle Report despite active records existing in Software Product Lifecycles table

  

### Issue

One or more lifecycle phase start dates (End of Support, End of Extended Support, or End of Life) appear empty in the Software Lifecycle Report (sam\_sw\_product\_lifecycle\_report) even though active lifecycle records with dates exist in the Software Product Lifecycles table (sam\_sw\_product\_lifecycle) for the same product.

### Release

ALL

### Cause

The report generation logic (SampLifecycleReportGenerator : `(clearBadPhaseDates: function(reportsObject) { ))` enforces that lifecycle phase dates must follow chronological order:  
GA <=EOS <= EOES <= EOL   
  
If any phase has a start date earlier than the preceding phase, the system removes that date from the report to prevent inconsistent data. This results in an empty start date on the report even though a corresponding record exists in the source table. 

### Resolution

Verify the lifecycle dates in sam\_sw\_product\_lifecycle for the affected product. If any phase date precedes the prior phase in the expected order (GA => EOS => EOES => EOL),  
  
If the affected phase start dates are sourced= internal then they are custom record customer need to verify the date and correct them  
  
If they content pushed dates then submit a content correction request to ensure dates follow chronological order.
