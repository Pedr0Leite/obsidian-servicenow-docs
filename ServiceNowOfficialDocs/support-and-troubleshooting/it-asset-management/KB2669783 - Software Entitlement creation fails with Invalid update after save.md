---
title: "Software Entitlement creation fails with \"Invalid update\" after save"
aliases:
  - KB2669783
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2669783
kb_number: KB2669783
last_modified: 2025-12-08
---

## Issue

Creating a Software Entitlement from the form fails on save with a banner Invalid update.

## Resolution

#Check for custom logic that sets asset tags

\- Review Business Rules and other server-side logic on `alm_license` (Software Entitlement) and `alm_asset` that write to `asset_tag` on insert/update.

\- In a sub-prod instance, temporarily deactivate any such customization and re-test entitlement creation to confirm the save succeeds without the unique key error.

#Correct the customization (if required)

\- Ensure the logic always generates a unique, non-blank `asset_tag`, runs at the appropriate timing (typically insert), and avoids re-setting tags on update.

#Clear existing conflicts

\- Find existing `alm_asset` rows with the conflicting tag value(s) and rename/retire as appropriate so future inserts are not blocked.

#Re-enable and re-test

\- Re-enable the corrected logic and verify a new Software Entitlement saves successfully and creates the related asset.
