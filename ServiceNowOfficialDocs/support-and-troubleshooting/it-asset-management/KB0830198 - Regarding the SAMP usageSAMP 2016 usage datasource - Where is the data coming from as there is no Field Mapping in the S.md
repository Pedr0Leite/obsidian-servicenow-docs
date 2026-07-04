---
title: "Regarding the  SAMP usage/SAMP 2016 usage datasource - Where is the data coming from as there is no Field Mapping in the  SAMP usage import Transform"
aliases:
  - KB0830198
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0830198
kb_number: KB0830198
last_modified: 2025-01-03
---

## Regarding the SAMP usage/SAMP 2016 usage datasource - Where is the data coming from as there is no Field Mapping in the SAMP usage import Transform

  

### Summary

The SAMP Usage job is designed much differently than a standard import, the test load from the Data Source record would not produce the same results.

The integration will not change the state or list a target record when viewed from the Import Set.

Additionally, each time it runs, the sql\_statement in the Data Source record will be reset to the below query:  
SELECT 1 from v\_MonthlyUsageSummary where 1=0

This is only a placeholder however. The actual query used against the SCCM servers and the incorporation of usage data is actioned through the SAMPUsageUtil Script Include, but only when executed by the system scheduler.  
The actual query that would be used is as below:  
SELECT TimeKey, TSUsageCount, UsageCount, UsageTime, LastUsage, ResourceID, MU.FullName as UserName, PFI.FileName FROM v\_MonthlyUsageSummary MUS LEFT JOIN v\_ProductFileInfo PFI on MUS.FileID = PFI.FileID LEFT JOIN v\_MeteredUser MU on MUS.MeteredUserID = MU.MeteredUserID WHERE FileName IN (...

  

### Related Links

The query is constructed through the below Script Include:  
SAMPUsageUtil  
[https://<instance-name>.service-now.com/sys\_script\_include.do?sys\_id=7ab34982cb632200f2de77a4634c9c2a](https://nestetest.service-now.com/sys_script_include.do?sys_id=7ab34982cb632200f2de77a4634c9c2a)

The SAMPUsageUtil is triggered by a pre-script included within SAMP Usage Import scheduled data import:  
[https://<instance-name>.service-now.com/sys\_transform\_map.do?sys\_id=621535c7cb122200f2de77a4634c9cba](https://nestetest.service-now.com/sys_transform_map.do?sys_id=621535c7cb122200f2de77a4634c9cba)
