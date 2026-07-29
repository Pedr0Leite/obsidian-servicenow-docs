---
title: "SAM - Salesforce Subscription Job Fails with \"Failed to Download Subscriptions\" Due to Missing Function in Older Store App Version"
aliases:
  - KB3024110
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3024110
kb_number: KB3024110
last_modified: 2026-05-16
---

## SAM - Salesforce Subscription Job Fails with "Failed to Download Subscriptions" Due to Missing Function in Older Store App Version

  

### Issue

The job SAM - Refresh Salesforce Subscription Subscriptions"fails with the error "Failed to download subscriptions." The OAuth refresh token is present and valid on the Direct Integration profile, so authentication does not appear to be the cause.

### Release

Nor release specific

### Cause

The failure is caused by a missing function in an outdated version of the Software Asset Management - SaaS License Management store app. The Salesforce download subscription subflow calls getCachedExclusionRulesByType from the SAMSaasCommonUtils script include.

This issue is mainly in version 16.0.7. If the store app has not been upgraded, this function does not exist, and the subflow fails immediately.

Relevant Log Pattern

```
*** WARNING ***
Cannot find function getCachedExclusionRulesByType in object [object Object].
   Process Automation.<sys_id> : Line(3) column(0)
      1: var profile = inputs.subflow_inputs_integration_profile;
      2: var saasCommonUtil = new sn_sam_saas_int.SAMSaasCommonUtils();
==>   3: var exclusionIndentifiers = saasCommonUtil.getCachedExclusionRulesByType('subscription_identifier', profile.profile_type, profile.sys_domain);

*** ERROR *** Script: Error: Failed to download subscriptions.
```

### Resolution

Please upgrade the Software Asset Management - SaaS License Management plugin from version 16.0.7 to the latest available version via below link.  
  
https://<instance\_name>.service-now.com/now/app-manager/home/app/id/cbba4378877023003800ed4d87cb0b6c  
  
Once the update is complete, please re-run the Salesforce subscription job and confirm the results.
