---
title: "Dictionary Override Changed to Read-Only on fields like Retired Date, Disposal Date, and Disposal Vendor on Medical Asset(sn_ent_medical_asset) table "
aliases:
  - KB2981887
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2981887
kb_number: KB2981887
last_modified: 2026-04-27
---

## Dictionary Override Changed to Read-Only on fields like Retired Date, Disposal Date, and Disposal Vendor on Medical Asset(sn\_ent\_medical\_asset) table

  

### Issue

Certain fields on the Medical Asset table (Retired Date, Disposal Date, and Disposal Vendor) became read-only due to dictionary overrides, preventing users from editing them. The fields were previously editable before the Zurich upgrade.  
  

### Release

Zurich or later

### Cause

The fields were transitioned to read-only status during the Zurich Release implementation. This change enforces proper workflow execution by programmatically updating the fields during the asset retirement and disposal process.  
  

### Resolution

These fields were transitioned to read-only status during the Zurich Release implementation.  
  
These attributes are programmatically updated at the terminal lifecycle state (Retired). Upon asset retirement and subsequent disposal, the asset record is removed from the active license pool, marking the completion of its operational lifecycle. Manual modification of these fields has been deprecated to enforce proper workflow execution.  
  
The retired\_date field is automatically populated via state transition logic when the asset status changes to Retired. The disposal\_date and disposal\_vendor fields are system-managed and populated upon successful completion of the disposal workflow process.
