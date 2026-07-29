---
title: "Deflection metrics for HR KB is not working as expected"
aliases:
  - KB1647740
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1647740
kb_number: KB1647740
last_modified: 2026-03-09
---

## Deflection metrics for HR KB is not working as expected

  

### Issue

Deflection metrics for HR KB (HR Cases deflection using KB articles) is not populating on the Self Service Analytics Deflection Metrics table (ssa\_deflection\_metric).

### Release

Plugin: HR Success Dashboard Indicators

### Cause

Required settings for the scheduled job 'HR KB Deflection Analytics for User' to run successfully is incomplete

### Resolution

Make sure that below Restricted Caller Access records (RCA) are set to 'Allowed':

Source: Script Include: ActivityUtilsSNC  
Target Scope: Human Resources: Core  
https://{Instance}.service-now.com/nav\_to.do?uri=sys\_restricted\_caller\_access.do?sys\_id=8fab6ad5c37dcad070770a359901314f  
  
Source: Script Include: SSADeflectionAnalyticsServiceSNC  
Target Scope: Human Resources: Core  
https://{Instance}.service-now.com/nav\_to.do?uri=sys\_restricted\_caller\_access.do?sys\_id=8112e109c371ced04f709d477a01315f  
  
Source: Script Include: DeflectionContextDAO  
Target Scope: Human Resources: Core  
https://{Instance}.service-now.com/nav\_to.do?uri=sys\_restricted\_caller\_access.do?sys\_id=9476455b47b686104fdcaf7b116d439

### Related Links

Other important points to consider:

Make sure HR KB is not viewed through an impersonated user. As the code checks for the last time the user logged in, the HR KB has to be viewed by a logged in user.

Make sure that after viewing the HR KB a record is populated in the 'kb\_use' table.

If necessary, for testing purposes, change the duration of the deflection calculation to a shorter period through searching for 'ssa\_deflection\_configuration\_list.do' in the navigator, and editing the 'HR Cases deflection using KB articles' record. Make sure the duration of the configuration and scheduled job time is aligned.
