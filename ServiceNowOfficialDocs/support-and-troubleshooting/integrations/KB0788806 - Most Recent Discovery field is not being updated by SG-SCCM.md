---
title: "Most Recent Discovery field is not being updated by SG-SCCM"
aliases:
  - KB0788806
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788806
kb_number: KB0788806
last_modified: 2026-06-12
---

## Most Recent Discovery field is not being updated by SG-SCCM

  

### Issue

Customer has an active SCCM integration that runs periodically. The logs indicate there are successful updates and inserts but when you go look at the "Most Recent Discovery" field in the CI record it hasn't been updated.

### Release

All supported release

### Cause

Since the records are created by the SCCM integration\\transform sets and not by Discovery, the field "Most recent discovery" is not mapped by default.

### Resolution

The Service Graph Connector for SCCM does not map this field out of the box. It maps to source\_recency\_timestamp in the target record, representing the last time this object was seen by that external source. So in this case, it would be the lastHWscan for SCCM import.

You can map the field "Most recent discovery" or any other field of your choice by going to the robust transform definition in IntegrationHub ETL. This would be a customization of the Service Graph Connector for SCCM and is outside the scope of support to implement. 

-   [Documentation around using IntegrationHub ETL](https://www.servicenow.com/docs/r/servicenow-platform/integration-hub-etl/integrationhub-etl.html)
