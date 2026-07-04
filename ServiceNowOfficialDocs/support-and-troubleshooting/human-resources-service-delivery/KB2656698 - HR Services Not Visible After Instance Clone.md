---
title: "HR Services Not Visible After Instance Clone"
aliases:
  - KB2656698
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2656698
kb_number: KB2656698
last_modified: 2025-12-17
---

## HR Services Not Visible After Instance Clone

  

### Issue

After cloning the DEV instance, HR Service Delivery features stopped working. No HR Services were displayed for the related COE in HR Agent Workspace when creating a case, and end users encountered errors when creating HR cases from the portal.

### Release

Any

### Cause

The system property `sn_hr_core.impersonateCheck` was set to true, which enforces impersonation checks. When enabled, the read ACL on sn\_hr\_core\_case and related tables denies access if the user is impersonated, preventing HR services and COEs from appearing.

### Resolution

-   Navigate to System Properties and locate `sn_hr_core.impersonateCheck`.
-   Set the property value to false.
-   Validate that HR Services and COEs are visible in the Create New Case page.
-   Note: HR services with HR Criteria require the Subject Person to be selected before skipping verification; this is expected behavior.
