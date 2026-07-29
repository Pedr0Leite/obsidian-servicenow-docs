---
title: "HR workflows not running"
aliases:
  - KB0690767
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0690767
kb_number: KB0690767
last_modified: 2024-04-07
---

## HR workflows not running

  

### Issue

When an HR record is created the workflows will not attach and run.

### Release

All versions

### Cause

Due to a custom change made on the state flow record.

### Resolution

State flow record - /nav\_to.do?uri=sf\_hr\_case.do?sys\_id=15d129b3df23210068c37a0d3df26313

This state flow record is being called by an base system business rule - /nav\_to.do?uri=sys\_script.do?sys\_id=19d129b3df23210068c37a0d3df26313

and there is a _starting state_ and _ending state_ missing. 

Reverting the state flow to the base system one will help resolve the issue.
