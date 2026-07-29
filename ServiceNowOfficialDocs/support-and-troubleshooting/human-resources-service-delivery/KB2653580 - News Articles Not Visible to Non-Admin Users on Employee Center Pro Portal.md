---
title: "News Articles Not Visible to Non-Admin Users on Employee Center Pro Portal"
aliases:
  - KB2653580
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2653580
kb_number: KB2653580
last_modified: 2026-01-01
---

## News Articles Not Visible to Non-Admin Users on Employee Center Pro Portal

  

### Issue

News articles were only visible to admin users on the Employee Center Pro Portal. Non-admin users could not access them.  
The issue was not reproducible in an out-of-box instance, indicating it was environment-specific.  
This blocked the planned production rollout and impacted business/testing activities.

### Release

Any

### Cause

The `sn_cd_content_visibility` table was in the wrong application scope (“Agent Workspace for HR Case Management” instead of “Content Publishing”), likely due to plugin installation order.

### Resolution

·  Verify the issue

-   Confirm that non-admin users cannot view news articles on the portal.
-   Validate that the issue does not occur in an out-of-box instance.

·  Apply temporary workaround

-   Modify the script include to use GlideRecord instead of GlideRecordSecure to restore visibility.

·  Identify root cause

-   Check the application scope of the sn\_cd\_content\_visibility table.
-   Determine if the scope is incorrect due to plugin installation order.

·  Correct the scope

-   Update the table scope to the correct application (“Content Publishing”) in all environments (DEV, TEST, PROD).

·  Validate and confirm resolution

-   After applying the scope correction in production, verify that news articles are visible to non-admin users.
