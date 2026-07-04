---
title: "After upgrading to Zurich, some of the SAM jobs are failing with an error \"ReferenceError: \"SamLicenseBroker\" is not defined\""
aliases:
  - KB2672822
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2672822
kb_number: KB2672822
last_modified: 2025-12-31
---

## After upgrading to Zurich, some of the SAM jobs are failing with an error "ReferenceError: "SamLicenseBroker" is not defined"

  

### Issue

**Problem**  
The below 3 scheduled jobs are failing after upgrading to Zurich Patch 3.  
1\. SAM - Generate Software Lifecycle Report  
2\. SAM - Set client pull schedules  
3\. SAM - Software License Reconciliation  
  
  

### Symptoms

Reconciliation progress summary for result has below error 

ReferenceError: "SamLicenseBroker" is not defined.

### Release

Zurich

### Cause

Missing "SamLicenseBroker" script include file on the instance, causing errors during reconciliation.  
  

### Resolution

Repair the Software Asset Management plugin (App id: sn\_itam\_samp) to restore missing script includes, as this may have occurred during the upgrade where plugin files were not properly downloaded.
