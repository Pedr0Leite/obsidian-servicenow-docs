---
title: "discovery_source field is switching between \"unknown\" and empty values"
aliases:
  - KB0695325
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695325
kb_number: KB0695325
last_modified: 2024-04-07
---

## discovery\_source field is switching between "unknown" and empty values

  

### Issue

# Symptoms

* * *

Discovery source is switching between "unknown" and empty values

# Release

* * *

Any release

# Cause

The "discovery\_source" is a mandatory parameter for Identification Reconciliation Engine. CMDB Health audit job for duplicate processor will be triggered when CMDB Health Dashboard scheduled jobs are kicked off. This will pick up CI records which have empty value for the discovery source field for evaluation, as they might have go through Identification Reconciliation Engine. Once the evaluation is done, it marks the CI discovery source as "unknown".

This "unknown" status will reset to empty whenever there is an update to CI record to ensure that it is picked for duplicate evaluation. This done by a business rule "Reset Unknown Discovery Source State" which is triggered when there is an update to the CI

This can happen in a loop when the CMDB health job is run everyday, and there is a update to the CI

# Resolution

* * *

In order to break the loop, make sure that the "discovery\_source" is not empty for the CI's, it needs to be of any value, so that it would not be set and reset from "unknown"
