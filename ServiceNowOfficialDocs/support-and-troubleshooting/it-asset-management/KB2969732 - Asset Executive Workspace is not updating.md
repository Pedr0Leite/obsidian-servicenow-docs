---
title: "Asset Executive Workspace is not updating "
aliases:
  - KB2969732
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2969732
kb_number: KB2969732
last_modified: 2026-04-20
---

## Asset Executive Workspace is not updating

  

### Issue

The Asset Executive Workspace is showing zeros across all dashboards after running "Asset Management - Populate KPI Aggregate table" scheduled job.  
  

### Symptoms

Scheduled Job - "Asset Management - Populate KPI Aggregate table" failed with below error

Error :

Invalid choice 'hardware' for field 'product' (table 'asset\_kpi\_aggregate'). Allowed values:  
\[  
"software"  
\]

### Release

All

### Cause

The hardware choice value for the 'Product' field on the 'asset\_kpi\_aggregate' table was set to inactive (inactive = true), causing the job to fail with an invalid choice error.  
  

### Resolution

1\. Navigate to the sys\_choice record for the 'Product' field on the 'asset\_kpi\_aggregate' table using the link: https://xxxx.service-now.com/nav\_to.do?uri=sys\_choice.do?sys\_id=ef31b60861470110c88663d42c67cb2a  
2\. Set the 'inactive' field for the 'hardware' choice value to false.  
3\. Re-run the 'Asset Management - Populate KPI Aggregate table' job.
