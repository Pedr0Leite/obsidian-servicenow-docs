---
title: "When import sets from two different data sources are using same staging table, only  latest one is used during transform"
aliases:
  - KB0749267
  - When import sets from two different data sources are using same staging table, only latest one is used during transform
tags:
  - servicenow
  - support-kb
  - import-sets
  - transform-maps
  - staging-table
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749267
kb_number: KB0749267
last_modified: 2024-04-07
---

## When import sets from two different data sources are using same staging table, only latest one is used during transform

  

### Issue

# Symptoms

When we try to import data into a staging table using xls import using 2 different data sources it will create 2 different import sets(Importset1 and Importset2). After we transforming the data using the 2 different transform map at the same time from 2 different browsers, both these transform maps processing only the latest import set(importset2). Importset1 status is showing always loaded.

# Release

All Releases

# Cause

Even though we used 2 different transform maps to transform the 2 import sets, Transform maps always use the latest import set to process because both the import sets are stored in the same import set table.

# Resolution

1.  Use 2 different import set tables to import data and process the data using the transform map
2.  If we import data into single import set table, if we want to transform both the import sets while transforming the data select import      set you want to transform

# Additional Information

Please refer Transform map documentation :

[https://docs.servicenow.com/csh?topicname=c\_CreatingNewTransformMaps.html&version=latest](https://docs.servicenow.com/csh?topicname=c_CreatingNewTransformMaps.html&version=latest)

## Related

- [[KB0747613 - When importing data, some staging table records are duplicating or an Import set row is duplicating]]
