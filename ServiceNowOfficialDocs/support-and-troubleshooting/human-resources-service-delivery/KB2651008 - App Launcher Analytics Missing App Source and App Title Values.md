---
title: "App Launcher Analytics Missing \"App Source\" and \"App Title\" Values"
aliases:
  - KB2651008
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2651008
kb_number: KB2651008
last_modified: 2025-12-16
---

## App Launcher Analytics Missing "App Source" and "App Title" Values

  

### Issue

App Launcher analytics reports show empty values for the App Source and App Title fields, impacting reporting accuracy for user activity.

### Release

Any

### Cause

The out-of-box App Launcher widget script uses `app.appid` instead of `app`, resulting in missing field values in analytics.

### Resolution

·  Upgrade to Employee Center Pro plugin version 36.0.1 or later (July 2025 release), which includes the fix for this issue.

·  After upgrading, revert any customized App Launcher widgets to the latest OOB version to ensure the corrected script is applied.

·  Validate analytics reports after upgrade to confirm that App Source and App Title fields are populated correctly.
