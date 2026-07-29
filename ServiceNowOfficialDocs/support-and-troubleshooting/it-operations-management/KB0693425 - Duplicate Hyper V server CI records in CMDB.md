---
title: "Duplicate Hyper V server CI records in CMDB"
aliases:
  - KB0693425
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693425
kb_number: KB0693425
last_modified: 2025-04-07
---

## Duplicate Hyper V server CI records in CMDB

  

### Issue

  
  

# Description

The "DiscoveryHyperVSensor" script include creates or updates the hyper v server CI's. The cmdb\_ci\_hyper\_v\_server record is associated with a windows CI through the "windows\_host" field. The script include queries the cmdb\_ci\_hyper\_v\_server table to find the currently discovered windows CI associated with any record. If it finds the record, it updates it or if it does not, then it creates a new record.

# Procedure

When there is a duplicate hyper v server CI created, check if the existing original CI has a valid windows CI in "windows\_host" field.

# Applicable Versions

* * *

Any version
