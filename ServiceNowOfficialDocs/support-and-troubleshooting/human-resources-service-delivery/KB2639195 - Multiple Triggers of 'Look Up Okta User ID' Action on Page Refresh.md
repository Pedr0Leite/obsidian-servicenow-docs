---
title: "Multiple Triggers of 'Look Up Okta User ID' Action on Page Refresh"
aliases:
  - KB2639195
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2639195
kb_number: KB2639195
last_modified: 2026-01-01
---

## Multiple Triggers of 'Look Up Okta User ID' Action on Page Refresh

  

### Issue

The OOTB action "Look up Okta User ID" is triggered multiple times per page refresh, resulting in 20+ API calls per session instead of the expected single call. This excessive triggering consumes Integration Hub transactions and may impact licensing and performance.

### Release

Any Release

### Cause

Repeated calls occur due to the way the App Launcher widget and related script includes (`AppLauncherUtilSNC`, `OktaWebApplicationsUtilSNC`) handle session cache logic when the user is not mapped with a valid Okta user ID.

### Resolution

To resolve this issue:

-   Verify that the user is mapped with a valid Okta user ID in the system.
-   Navigate to Okta user mapping configuration and confirm the mapping for affected users.
-   If mapping is missing, update the user record to include the correct Okta user ID.
-   After mapping is corrected, refresh the portal and confirm that the "Look up Okta User ID" action triggers only once per session.
