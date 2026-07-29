---
title: "Resolved Incidents are resolved daily and not auto closed"
aliases:
  - KB0717836
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0717836
kb_number: KB0717836
last_modified: 2024-04-07
---

## Resolved Incidents are resolved daily and not auto closed

  

### Issue

Incidents are updated daily by the system and are not closing after the expected 5 days. 

### Release

Kingston Patch 8

### Cause

There is an inactivity monitoring running every 8 hours and each time it runs, a scheduled job is fired and updates the incident from the system. As there is a recent update to the incident, the incident auto-close business rule will not run. 

### Resolution

Add a condition on the inactivity monitor to not run when the incident is resolved.
