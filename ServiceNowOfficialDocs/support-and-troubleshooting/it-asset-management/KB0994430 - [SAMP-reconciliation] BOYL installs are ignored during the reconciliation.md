---
title: "[SAMP-reconciliation] BOYL installs are ignored during the reconciliation"
aliases:
  - KB0994430
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0994430
kb_number: KB0994430
last_modified: 2024-08-28
---

## \[SAMP-reconciliation\] BOYL installs are ignored during the reconciliation

  

### Issue

BYOL (Bring Your Own Licenses) installations are not visible in License Workbench.

### Release

Jakarta ++

### Cause

1\. The related installs could be ignored by setting up [Exclude device installations](https://docs.servicenow.com/bundle/quebec-it-asset-management/page/product/software-asset-management2/reference/sam-properties.html "Exclude device installations") during reconciliation.

2\. Could be due to some of installs which are supposed to be filtered. 

(Ex: If we have any installations with 'Security update' in the primary key which doesn't create Discovery models)

### Resolution

1\. Make sure the related installations are not excluded from reconciliation.

2\. Check if any of affected installations does have filtered keys in Primary key of that installations.

### Related Links

1\. [Enter the name of the true/false field added to cmdb\_ci\_hardware table to exclude software installed on selected devices from Software Asset Management](https://docs.servicenow.com/bundle/quebec-it-asset-management/page/product/software-asset-management2/reference/sam-properties.html "Enter the name of the true/false field added to cmdb_ci_hardware table to exclude software installed on selected devices from Software Asset Management")
