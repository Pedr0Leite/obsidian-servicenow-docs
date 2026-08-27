---
title: "Event Management dashboard showing business services that are out of sync with alerts"
aliases:
  - KB0720820
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0720820
kb_number: KB0720820
last_modified: 2024-04-07
---

## Event Management dashboard showing business services that are out of sync with alerts

  

### Issue

# Symptoms

* * *

You are noticing the business services on Event Management Dashboard are showing wrong impact and are out of sync with the alerts.

# Release

* * *

All releases

# Cause

* * *

If you tried cleaning up the records in em\_alert and em\_alert\_history tables, then with the new alerts coming in, certain business services might be showing wrong impact calculation.

This is because there are multiple other places where we do the impact calculation from. Deleting em\_alert and em\_alert\_history would not reset the impact calculations on business services.

# Resolution

* * *

In the EM dashboard, for the services where the impact is not showing correctly and out of sync, moving them to non-operational and then setting back to operational, will trigger fresh impact calculation jobs. This will set back the services to sync.
