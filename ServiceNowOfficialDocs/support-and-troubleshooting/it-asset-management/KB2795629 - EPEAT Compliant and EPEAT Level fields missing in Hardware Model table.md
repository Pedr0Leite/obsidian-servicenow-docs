---
title: "EPEAT Compliant and EPEAT Level fields missing in Hardware Model table"
aliases:
  - KB2795629
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2795629
kb_number: KB2795629
last_modified: 2026-03-03
---

## EPEAT Compliant and EPEAT Level fields missing in Hardware Model table

  

### Issue

The 'EPEAT Compliant' and 'EPEAT Level' fields are missing from the Hardware Model table. However, according to the documentation linked below, these fields should be present post Yokohama upgrade.

[https://www.servicenow.com/docs/r/yokohama/it-asset-management/hardware-asset-management/hardware-model-fields.html](https://www.servicenow.com/docs/r/yokohama/it-asset-management/hardware-asset-management/hardware-model-fields.htmlT)

### Release

Yokohama and later

### Cause

These two fields are part of the Hardware Asset Management Plugin, which is not installed on the affected instance.

### Resolution

Install the Hardware Asset Management (HAM) plugin on your instance. After installation, the fields 'EPEAT Compliant' and 'EPEAT Level' will be available in the Hardware Model tables.
