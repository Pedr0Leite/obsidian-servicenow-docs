---
title: "SAM - Refresh Activity *  Job for SuccessFactors integration failing with \"Invalid alias override. Alias are not found in flow successfactors_update_user_activity\""
aliases:
  - KB2681919
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2681919
kb_number: KB2681919
last_modified: 2026-05-18
---

## SAM - Refresh Activity \* Job for SuccessFactors integration failing with "Invalid alias override. Alias are not found in flow successfactors\_update\_user\_activity"

  

### Issue

"SAM - Refresh Activity \*  Job for SuccessFactors integration is fails with below error:  
  
Invalid alias override. Alias are not found in flow successfactors\_update\_user\_activity. Detail:  
  
  

### Symptoms

  
  

### Facts

Custom Alias for OOB connection is not supported OOB for Refresh \*activity flow since there are no Rest API steps in Subflow.

### Release

All

### Cause

Custom Alias for OOB connection is not supported OOB for Refresh \*activity flow.

While the documentation says you can create alias overrides for connection URLs, not all SAM integration subflows support child alias resolution.  
  
The Refresh Activity job runs a Subflow: SubFlow: SuccessFactors Update User Activity  
This Subflow does not use REST steps directly where aliases are required.  
  
Root Cause: The subflow does not use any Connection Alias  
• If the subflow has no action step that uses the alias, ServiceNow does not register its alias IDs and hence override fails, as the SAMSaasCustomIntegration script include tries resolving aliases by reading from the integration profile.  
  

### Resolution

Child alias is not supported for this flow OOB.  
  
Other alternative is you can add multiple connections with different URL's in the OOB alias, by keeping only one connection active at a time.
