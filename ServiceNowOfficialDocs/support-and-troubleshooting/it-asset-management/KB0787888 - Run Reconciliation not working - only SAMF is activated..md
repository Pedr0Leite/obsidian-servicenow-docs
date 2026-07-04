---
title: "Run Reconciliation not working - only SAMF is activated."
aliases:
  - KB0787888
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787888
kb_number: KB0787888
last_modified: 2024-04-07
---

## Issue

**Issue:**  
Run Reconciliation is failing in an instance with ONLY Software Asset Management Foundation (SAMF) plugin is active.  
  
  
**Steps to Reproduce:**  
1\. A Software Model named 'Adobe Systems Creative Cloud'  
2\. Add the Suite Components 'Photoshop' and 'Acrobat DC Pro'.  
3\. Save  
4\. Run Reconciliation  
5\. Reconciliation Results - failed.

Reconciliation Results is not showing any information on the "Product Results", "License Metric Results", "Software Model Results".

  

Note: 

Software Model "Adobe Systems Creative Cloud" and the Suite Component (Software Models) have "Subscription software" checked (true).

  

**Error from the logs:**

"SAM:ReconciliationEngine: org.mozilla.javascript.EvaluatorException: GlideRecord.addQuery() - invalid table name: samp\_sw\_subscription (sys\_script\_include.7514cbca0b1232006586650d37673ac0.script; line 16): no thrown error"

## Resolution

Please contact ServiceNow Technical Support for assistance and apply the workaround on the 'Protected' Script Include "SAMPSuiteEngine".
