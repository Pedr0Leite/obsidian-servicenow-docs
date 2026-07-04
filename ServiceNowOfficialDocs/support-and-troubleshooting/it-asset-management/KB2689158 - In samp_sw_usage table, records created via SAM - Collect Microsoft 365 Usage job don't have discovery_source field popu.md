---
title: "In samp_sw_usage table, records created via \"SAM - Collect Microsoft 365 Usage\" job don't have discovery_source field populated"
aliases:
  - KB2689158
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2689158
kb_number: KB2689158
last_modified: 2026-03-27
---

## In samp\_sw\_usage table, records created via "SAM - Collect Microsoft 365 Usage" job don't have discovery\_source field populated

  

### Issue

Few records under \[samp\_sw\_usage\] table doesn't populate \[discovery\_source\] field.

### Release

Yokohama

### Cause

For this Microsoft integration, we bring the data using the API call, the discovery source is not considered, hence it shows empty.  
  
The Script Include "SAMPSoftwareUsageDataSourceIntegration" will populate Discovery source for records filtered by IRE (Example SG-Jamf, SG-SCCM)  
https://<INSTANCE\_NAME>.service-now.com/sys\_script\_include.do?sys\_id=fcdc2ceae71300107aea07d8d2f6a935  
  
This is expected behavior.

### Resolution

Customer to log an enhancement request if they need discovery source to be populated by the Microsoft Integration via API.
