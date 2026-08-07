---
title: "Scheduled Job running 'SAM - Update Software Total Usage Metric' is not moving software usage from staging table to Software Usage (samp_sw_usage) table "
aliases:
  - KB2672963
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2672963
kb_number: KB2672963
last_modified: 2026-03-27
---

## Scheduled Job running 'SAM - Update Software Total Usage Metric' is not moving software usage from staging table to Software Usage (samp\_sw\_usage) table

  

### Issue

  
The Scheduled Job 'SAM - Update Software Total Usage Metric' is not moving software usage from the staging table to the Software Usage (samp\_sw\_usage) table. The staging data remains in the staging table even when the job is manually executed. 

The job details are available at https://instancename.service-now.com/sysauto\_script.do?sys\_id=5417a9e9cea448018cb35d671ca172c1. 

The staging data can be viewed at https://instancename.service-now.com/now/nav/ui/classic/params/target/sn\_acc\_vis\_content\_sam\_software\_usage\_staging\_list.do%3Fsysparm\_clear\_stack%3Dtrue.  
  

### Release

Xanadu

### Cause

  
The root cause was a date format mismatch in the composite key logic between the script include 'SAMPSoftwareUsageDataSourceIntegration' and the Business Rule 'Build primary key on insert'. The month field in the Business Rule was stored as a single-digit value, while the script include used a double-digit format, causing a discrepancy in the primary key and preventing successful data insertion.  
  

### Resolution

  
Apply the fix in the Business Rule 'Build primary key on insert' to address the date format mismatch between the script include and the Business Rule. 

BR- [https://instancename.service-now.com/sys\_script.do?sys\_id=b77a2414cb232200f2de77a4634c9c58](https://\<Instance\>.service-now.com/sys_script.do?sys_id=b77a2414cb232200f2de77a4634c9c58&sysparm_record_target=sys_script&sysparm_record_row=3&sysparm_record_rows=4&sysparm_record_list=nameCONTAINSbuild+primary%5EORDERBYname)

Add below code under the line 10 or var month = current.month\_used || ' ' ;

**if (month.toString().length<2) {**

**month = "0" + month;**

**}**

The month field was adjusted to ensure consistency between single-digit and double-digit formats. 

Ref: PRB1906425
