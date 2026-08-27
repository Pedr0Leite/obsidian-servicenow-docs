---
title: "CAB Workbench \"{{heading}}\" displays where the Change Request form details should appear"
aliases:
  - KB0999620
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0999620
kb_number: KB0999620
last_modified: 2024-10-16
---

## CAB Workbench "{{heading}}" displays where the Change Request form details should appear

  

### Issue

The user had installed CAB Workbench and, on opening the workbench, when opening a pending or completed agenda item, the section of the workbench where the details of the Change Request (CHG) should appear only displayed "{{heading}}". The user wanted to know why this was, as they had not customized any piece of the CAB Workbench.

### Cause

This was due to some widget dependencies (sp\_dependencies) set to "Include on page load" = "true", and "Portals for page load" was "empty". What this meant was that the user's custom widget dependencies were always included on page load, and on all portals (including CAB Workbench). This unintentionally caused the CAB Workbench to break.

### Resolution

The user was counseled to set the "Portals for page load" to the desired list of portals where they wanted the widget dependencies to load (CAB Workbench excluded), and/or they could set the widget dependencies to "Include on page load" = "false", though the former is likely preferred over the latter as the user did not want to disregard the widget dependencies (or their child JS Includes) altogether.

Once this was done, the CAB Workbench rendered perfectly, just as it does in a fresh, Out of Box (OOB) instance with the plugin installed.
