---
title: "HAM - Asset Indoor Map Tab Not Visible in Hardware Asset Workspace"
aliases:
  - KB2972800
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2972800
kb_number: KB2972800
last_modified: 2026-04-22
---

## HAM - Asset Indoor Map Tab Not Visible in Hardware Asset Workspace

  

### Issue

The Indoor Map tab does not appear in the Hardware Asset Workspace under Asset Estate, even after following the official product documentation for setting up indoor map tracking.

### Release

Not release Specific

### Cause

The Indoor Map tab in the Hardware Asset Workspace is controlled by a dedicated property in the asset\_property table, not the standard sys\_properties table.

Administrators who follow the documentation may incorrectly set the property under sys\_properties, which has no effect on the visibility of the Indoor Map tab. The correct property must be set in the asset\_property table for the feature to activate.

### Resolution

Navigate to the asset\_property table (asset\_property.list).

Locate the property: com.sn\_hamp.indoormap.enabled

Set the value to true and save the record.

Navigate to the Hardware Asset Workspace and open Asset Estate. The Indoor Map tab should now be visible.
