---
title: "Why some Software Models are not shown in the Reconciliation Result list?"
aliases:
  - KB1698985
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1698985
kb_number: KB1698985
last_modified: 2026-05-27
---

## Why some Software Models are not shown in the Reconciliation Result list?

  

### Summary

**Why some Software Models are not shown in the Reconciliation Result list?**

\[[Reconciliation - Software Models.png](https://support.servicenow.com/sys_attachment.do?sys_id=439bda724789c39c11eaf24c736d436e&sysparm_this_url=u_kb_template_kcs_how_to_for_cs.do%3Fsys_id%3Dfbe10be04748ded0f64de825126d4352%26sysparm_record_target%3Dkb_knowledge%26sysparm_record_row%3D1%26sysparm_record_rows%3D1%26sysparm_record_list%3DnumberSTARTSWITHKB1698985%255EORDERBYDESCsys_updated_on)\]

**The Reconciliation Results will have the Software Model listed:**  
a. If the Software Model have valid Entitlements; OR  
b. If the Software Installs cannot be covered by any Entitlements they have.

**Note:**

Downgrade Rights (or the Downgrade Software Models) will not be shown as it will be under the Software Model for which the Entitlement is assigned.

In the example shown in the screenshot \[[SW Model - Microsoft Visio 2019 Standard.png](https://support.servicenow.com/sys_attachment.do?sys_id=db9bda724789c39c11eaf24c736d4374&sysparm_this_url=u_kb_template_kcs_how_to_for_cs.do%3F%26sysparm_stack%3Dno%26sys_id%3D-1%26sys_is_list%3Dtrue%26sys_target%3Dkb_knowledge%26sysparm_referring_url%3Dkb_knowledge_list.do%26sysparm_query%3Dkb_knowledge_base%253D124c2ca22bb9f1002f42729fe8da152e%255EEQ)\]

  
The current result for the Microsoft Visio (2019 Standard), shows that the Software Model: Microsoft Visio 2019 Standard has 9 Downgrade Rights (Software Models) which have no Entitlements and used the 1 Entitlement associated with "Software Model: Microsoft Visio 2019 Standard".

In the results, the reconciliation shows the results under "Microsoft > Visio > 2019 Standard".

  
  
In the case of Windows Server, on why there are software models shown in the list while they are also in the Downgrade Rights of the higher version, in the investigation, it was found that:

1.  Only the Software Model "Microsoft Windows Server 2012 R2 Standard" has an Entitlement among 9 Software Models listed; and
2.  The Software Model/s that has a higher version where the Downgrade Rights are defined has no Entitlements 

 E.g. Software Models "Microsoft Windows Server 2019 Standard" or "Microsoft Windows Server 2019 Datacenter"

\[[SW Model Results - Windows Server.png](https://support.servicenow.com/sys_attachment.do?sys_id=579bda724789c39c11eaf24c736d43ab)\]

  
The reconciliation will treat the installs to the closest Software Model and that is the reason why the specific Software Models were listed in the Software Model Result.  
  

### Release

All
