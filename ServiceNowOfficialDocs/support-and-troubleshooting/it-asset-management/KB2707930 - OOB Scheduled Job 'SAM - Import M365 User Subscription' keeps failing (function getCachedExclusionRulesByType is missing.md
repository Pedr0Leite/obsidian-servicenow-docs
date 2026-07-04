---
title: "OOB Scheduled Job : 'SAM - Import M365 User Subscription' keeps failing (function getCachedExclusionRulesByType is missing)"
aliases:
  - KB2707930
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2707930
kb_number: KB2707930
last_modified: 2026-01-12
---

## OOB Scheduled Job : 'SAM - Import M365 User Subscription' keeps failing (function getCachedExclusionRulesByType is missing)

  

### Issue

  
The Scheduled Job 'SAM - Import M365 User Subscriptions' as part of the 'Software Asset Management - SaaS License Management' Plugin keeps failing. The failure is observed in the 'Scheduled Job Results' tab under 'License Operations' in the 'Software Asset Workspace'. The error logs indicate a TypeError: Cannot find function getCachedExclusionRulesByType in object \[object Object\].  
  
  

### Release

Zurich instance

Software Asset Management - SaaS License Management plugin

Versions 16.0.6, 16.0.7

### Cause

**Root Cause**  
The issue was caused by the absence of the function 'getCachedExclusionRulesByType' in the Software Asset Management (SaaS License Management) plugin version 16.0.7. This function was available in the next stable version 16.0.8, which resolved the TypeError encountered during job execution.  
  

### Resolution

1\. Upgrade the plugin 'Software Asset Management - SaaS License Management' from version 16.0.7 to 16.0.8.  
2\. Verify that the 'SAMSaasCommonUtils' script include now contains the function 'getCachedExclusionRulesByType'.  
3\. Ensure the job runs as expected after the upgrade.  
4\. Refer to the latest release notes for updates and bug fixes: https://www.servicenow.com/docs/bundle/store-release-notes/page/release-notes/store/it-asset-management/store-rn-itam-sam-saas-license-mgmt-integrations.html
