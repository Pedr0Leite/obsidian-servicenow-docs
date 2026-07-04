---
title: "No Data from Microsoft 365 Direct Integration, the scheduled jobs got completed with out any errors."
aliases:
  - KB2906160
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2906160
kb_number: KB2906160
last_modified: 2026-03-20
---

## No Data from Microsoft 365 Direct Integration, the scheduled jobs got completed with out any errors.

  

### Issue

No Data from Microsoft 365 Direct Integration, the scheduled jobs got completed without any errors.

### Symptoms

\[-\]No HTTP outbound logs triggered

\[-\]No failure messages

\[-\]The SAM - Import M365 User Subscriptions, scheduled job gets completed immediately after the trigger without any errors.

\[-\]Rest Message field on the integration profile is empty.

### Release

Any Version

### Cause

When we add special characters in the display name of the integration profile, the BR "Create Office 365 OAuth app and REST msg" responsible for generating the 'Rest Message" is failing to process.

Example Display Name: Microsoft 365 - Test

"-" special character causing the issue. 

### Resolution

Please delete the existing integration profile and recreate the integration profile again without any special characters in the display name of the integration profile.
