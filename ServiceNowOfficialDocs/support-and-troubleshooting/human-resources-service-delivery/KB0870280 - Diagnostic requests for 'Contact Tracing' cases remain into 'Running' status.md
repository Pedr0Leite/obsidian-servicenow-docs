---
title: "Diagnostic requests for 'Contact Tracing' cases remain into 'Running' status"
aliases:
  - KB0870280
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0870280
kb_number: KB0870280
last_modified: 2023-12-13
---

## Diagnostic requests for 'Contact Tracing' cases remain into 'Running' status

  

### Issue

In a 'Contact Tracing' case, when executing the 'Run Diagnostics' UI action from a 'Diagnostic Request' record, the 'Report generation status' remains as 'Running' and does not move to 'Completed'.

  

Steps to reproduce the behaviour:  

1.  Log in or impersonate a user with 'sn\_imt\_tracing.case\_manager' role.
2.  Go to 'Contact Tracing > All Cases' (sn\_imt\_tracing\_case table).
3.  Open a 'Contact Tracing' case record.
4.  Go to 'Diagnostic Request' Tab.
5.  Open a 'Diagnostic Request' record and click 'Run Diagnostic' Ui action.
6.  The 'Report generation status' field is showing as 'Running' and does not move to 'Completed'.

  

### Cause

The scheduled jobs that trigger the diagnostic execution are set to inactive as part of an instance clone process.

### Resolution

Check the below Scheduled Job records in the instance:  
  
Reprocess workplace diagnostic requests  
https://<instance-name>.service-now.com/nav\_to.do?uri=sysauto.do?sys\_id=a26b16b929011010fa9bfc3eba3dc181  
  
Execute employee diagnostic events  
https://<instance-name>.service-now.com/nav\_to.do?uri=sysauto.do?sys\_id=47afa00cc3931010a3a6ddaa7d40dd87  
  
Activate both Scheduled Jobs in the instance and check the diagnostics.
