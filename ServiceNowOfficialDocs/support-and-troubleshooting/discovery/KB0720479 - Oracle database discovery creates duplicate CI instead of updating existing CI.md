---
title: "Oracle database discovery creates duplicate CI instead of updating existing CI"
aliases:
  - KB0720479
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0720479
kb_number: KB0720479
last_modified: 2025-07-23
---

## Oracle database discovery creates duplicate CI instead of updating existing CI

  

### Issue

Performing discovery of a Linux server hosting an Oracle database instance creates a duplicate configuration item (CI) in the Oracle database. The expectation is that discovery updates the existing CI. 

### Release

Any supported release

### Cause

The manually imported record in the CMDB is missing Oracle SID information and a listener relationship to the Oracle database instance.

### Resolution

The default Oracle database CI identification rule creates or updates the CI based on the Oracle SID attribute. 

If the existing CI is missing the SID information, it creates a new CI instead. 

To resolve this, update the Oracle SID and listener relationship to the existing database CI.
