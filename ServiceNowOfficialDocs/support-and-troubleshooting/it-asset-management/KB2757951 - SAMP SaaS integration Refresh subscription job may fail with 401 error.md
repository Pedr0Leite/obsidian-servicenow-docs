---
title: "SAMP SaaS integration: Refresh subscription job may fail with 401 error"
aliases:
  - KB2757951
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2757951
kb_number: KB2757951
last_modified: 2026-02-06
---

## Issue

The following scheduled jobs on the instance are failing with a 401 (Unauthenticated) error:

-   SAM – Refresh Google Workspace Integration for SAM Subscriptions
-   SAM – Refresh Zoom Integration for SAM Subscriptions

## Resolution

Configure the scheduled jobs to run with a user account that has the 'Admin' role, ensuring access to the required OAuth credentials.

Verify the job execution after applying the 'Run as' user configuration to confirm successful authentication and resolution of the 401 error.

Note: The ACL was added to enhance the instance security; we do not recommend disabling it.
