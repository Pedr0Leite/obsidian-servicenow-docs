---
title: "SAMP Usage 2016 sql query is a false query"
aliases:
  - KB0786542
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786542
kb_number: KB0786542
last_modified: 2024-04-08
---

## SAMP Usage 2016 sql query is a false query

  

### Issue

The SAMP Usage 2016 data source has the following query :SELECT 1 from v\_MonthlyUsageSummary where 1=0 

This is a false query and will never run. How do we import usage data?

### Resolution

The SCCM related SAMP Usage 2016 data source has an SQL query which is 

SELECT 1 from v\_MonthlyUsageSummary where 1=0 

This is a dummy query and is not the actual query that gets executed. Two criterions that are required for the this SCCM related SAMP Usage 2016  to bring in data are the following:

1.  Create reclamation rules for products. Based on these rules, the sql query will be built dynamically through the script include SAMPUsageUtil.  
    2\. You will have to run the whole "SCCM System 2016 Import" parent job for data to be brought in and not just this datasource.
