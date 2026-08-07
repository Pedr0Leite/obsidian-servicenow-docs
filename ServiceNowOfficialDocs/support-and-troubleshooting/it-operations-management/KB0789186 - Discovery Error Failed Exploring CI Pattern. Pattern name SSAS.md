---
title: "Discovery Error Failed Exploring CI Pattern. Pattern name: SSAS"
aliases:
  - KB0789186
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789186
kb_number: KB0789186
last_modified: 2024-04-07
---

## Discovery Error Failed Exploring CI Pattern. Pattern name: SSAS

  

### Issue

SSAS pattern run fails to process further steps when it does not get the version information from the Windows Registry Editor (**regedit**) entry for the SSAS Instance.

### Release

Any

### Cause

Windows Registry Editor (**regedit**) for the SSAS application should ideally contain the instance information. If it does not, then the version information is not fetched. If the version information is not fetched, the Step 7 on the SSAS pattern fails to meet the condition.

This value is derived from the executablePath variable for the SSAS process.

Expected Result:  
HKEY\_LOCAL\_MACHINE SOFTWARE\\Microsoft\\Microsoft SQL Server\\SSAS\_INSTANCE\\MSSQLServer\\CurrentVersion\\\*

### Resolution

The Step 7 on the SSAS pattern is looking for the version information to proceed further, if not, it fails at that step.  
  
There are 2 possibilities here,  
  
1\. You can go ahead and add another condition on the meet field for Step 7 to also include the \[$version\] \[is EMPTY\] so that the Step 8 and 9 proceeds for a successful pattern execution. (Refer Screenshot below of the SSAS pattern debug mode)

  
2\. You can check with your SSAS team to incorporate the \[$Instance\] value into the RegEdit in order to fetch the "version" information of the SSAS server.  
  
\* The Ideal scenario would be the second option here.  
  

![](sys_attachment.do?sys_id=23ea5bf0db0078d066e0a345ca96193c)
