---
title: "Software model result is (empty) on the majority of licensable installations after upgrade to Zurich "
aliases:
  - KB2971044
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2971044
kb_number: KB2971044
last_modified: 2026-04-23
---

## Software model result is (empty) on the majority of licensable installations after upgrade to Zurich

  

### Issue

**Problem**  
After upgrading to the Zurich release, the majority of products with License Type 'Licensable', which are Normalized or manually Normalized, do not have the Software Model result in the cmdb\_sam\_sw\_install table. This issue was observed in the cmdb\_sam\_sw\_install table, where filtering for licensable software and checking the Software Model result showed a significant number of entries with (empty) as the result. The issue was noted to affect reporting and potentially cause other issues. Steps to reproduce included filtering the install table for licensable software and checking the Software Model result.  
  

### Release

Zurich

### Cause

**Root Cause**  
The root cause was the system property 'com.snc.samp.unlicensed\_smr\_creation' being set to false after the upgrade to Zurich. This property, introduced in the Zurich release, determines whether SMRs are set on unlicensed installs. Prior to Zurich, SMRs were stamped on unlicensed installs, but the property's default value of false caused SMRs to be empty for unlicensed installs in the upgraded environment.  
  

### Resolution

**Steps to Resolve**  
Enable the system property 'com.snc.samp.unlicensed\_smr\_creation', which controls whether software model result (SMR) is set on unlicensed installs. This property was introduced in the Zurich release and defaults to false. Enabling it ensures SMRs are set on both licensed and unlicensed licensable installs, addressing the behavior change observed after the upgrade.   
  
  
Note:  
\- Potential data integrity issue: If SMR is not set on licensed installs, those where license metric result (LMR) is set, that would indicate a problem.   
\- Expected behavior: It is valid for SMR to not be set when an install is ignored — this can be confirmed via the Ignored Installs progress indicator in the reconciliation

### Related Links

Documentation for this property can be found at -  https://www.servicenow.com/docs/r/zurich/it-asset-management/software-asset-management/duplicate-sw-models.html.
