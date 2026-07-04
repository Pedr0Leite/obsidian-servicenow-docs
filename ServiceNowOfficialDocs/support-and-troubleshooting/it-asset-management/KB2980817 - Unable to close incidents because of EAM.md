---
title: "Unable to close incidents because of EAM"
aliases:
  - KB2980817
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2980817
kb_number: KB2980817
last_modified: 2026-05-01
---

## Unable to close incidents because of EAM

  

### Issue

  
When trying to close an incident, we encounter the following error: 'To resolve this incident, choose an asset action for each asset'.

### Release

Enterprise Asset Management

### Cause

Confirm that the affected incidents have references in the 'incident\_asset' table. If so, this is happening due to the installation of the EAM (Enterprise Asset Management) plugin.

This plugin installs a BR called 'Check if incident can be resolved' (sys\_script.do?sys\_id=a67ae943ebe2301046605377d8522801). The BR checks if the incident being closed/resolved has a reference in the 'incident\_asset' table and requires an asset action for each entry.

### Resolution

This is intended behavior after plugin installation.

To workaround this:  
1\. Navigate to the incident\_asset table and check for the affected incidents under the 'incident' column.  
2\. You can either choose to remove those table entries or add the relevant incident asset.
