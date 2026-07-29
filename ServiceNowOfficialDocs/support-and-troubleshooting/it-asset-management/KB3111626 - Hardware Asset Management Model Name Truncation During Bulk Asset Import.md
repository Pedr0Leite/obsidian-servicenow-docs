---
title: "Hardware Asset Management: Model Name Truncation During Bulk Asset Import"
aliases:
  - KB3111626
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3111626
kb_number: KB3111626
last_modified: 2026-06-23
---

## Hardware Asset Management: Model Name Truncation During Bulk Asset Import

  

### Issue

When importing assets in bulk via Hardware Asset Workspace, model name values exceeding 40 characters are silently truncated during import. The truncated values are stored in the staging table and may cause asset identification and reconciliation failures downstream.

### Symptoms

-   Model names display correctly in your source data (spreadsheet, integration), but appear truncated to 40 characters in the staging table after import
-   Asset records fail to reconcile or match existing product models due to incomplete model name data
-   No error message is displayed during import; truncation occurs silently

### Facts

-   Affects: Hardware Asset Management (HAM) Pro — bulk asset import via Hardware Asset Workspace
-   Affected fields: `model_name`, `model_number`, `serial_number`, `manufacturer`, `reserved_for`
-   Staging table: `sn_itam_cmn_import_asset_row`
-   Target tables: `cmdb_hardware_product_model`, `alm_asset`, `core_company`, `sys_user` (support 80–255 character fields)
-   Condition: OOTB behavior — no custom configuration required to reproduce

### Release

All supported releases of Hardware Asset Management Pro 

### Cause

The staging table `sn_itam_cmn_import_asset_row` has no explicit `max_length` attributes defined in its XML dictionary for string fields (`model_name`, `model_number`, `serial_number`, `manufacturer`, `reserved_for`). When `max_length` is not specified, ServiceNow defaults string fields to 40 characters. Target tables support up to 255 characters, creating a data model mismatch that results in silent truncation.

### Resolution

Hi Kathy,  
  
Apologies for the delay as I've been out of office, and thank you for your patience. We've identified the root cause: the staging table sn\_itam\_cmn\_import\_asset\_row has a 40-character limit on model names, while the target table supports 255 characters. This causes truncation during import.  
  
I've escalated this to our CS-ATOM engineering team to determine if the field length needs to be aligned. They'll evaluate whether this requires a product fix.  
  
I'll follow up once we hear back.  
  
Best regards,  
Richard Luo  
ServiceNow Technical Support

### Related Links

This is a confirmed product defect (PRB2039498) currently in development
