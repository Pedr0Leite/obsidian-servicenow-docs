---
title: "Certain cmdb_sam_sw_install records have property: Active install (active): false and Deduplication processed (deduplicated): false"
aliases:
  - KB1123484
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1123484
kb_number: KB1123484
last_modified: 2025-07-08
---

## Certain cmdb\_sam\_sw\_install records have property: Active install (active): false and Deduplication processed (deduplicated): false

  

### Issue

Certain cmdb\_sam\_sw\_install records have property: Active install (active): false and Deduplication processed (deduplicated): false

### Release

All

### Cause

Likely the Discovery Model on the Software Installations is not normalized / doesn't have normalized product

### Resolution

  
1\. Normalize the discovery models for the affected installs. Make sure normalized product is present on discovery models  
2\. Run "SAM - Deduplicate Install Table" scheduled job

### Related Links

[Software Normalization Deep Dive](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0859819)
