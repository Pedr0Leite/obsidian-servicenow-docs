---
title: "Unable to run custom business rules on Impact status table [em_impact_status]"
aliases:
  - KB0759333
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0759333
kb_number: KB0759333
last_modified: 2026-05-22
---

## Unable to run custom business rules on Impact status table \[em\_impact\_status\]

  

### Issue

Unable to run Custom business rules on Impact status table \[em\_impact\_status\]

### Release

All releases

### Cause

As we might insert records to impact status table in high rate (its impacted on the rate alerts created/updated) , we use the platform statement batcher to insert records in bulks. This does not run the platform Business Rule and other workflow that might runs when inserting records one by one using GlideRecord.   
  
Running Business Rule on this table can kill the performance! We batch insert to help with the performance. We do not expect any Business Rules on this table due to the high churn rate. 

### Resolution

This is expected behavior. We cannot run business rules on the table \[em\_impact\_status\] due to performance issues.
