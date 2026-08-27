---
title: "Demand Field not populated on Project when created from Demand"
aliases:
  - KB0715645
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0715645
kb_number: KB0715645
last_modified: 2024-04-07
---

## Demand Field not populated on Project when created from Demand

  

### Issue

# Symptoms

* * *

When creating a project from a demand, the demand field is not populated on the new project record. This prevents the project from showing on the Demand's project related list.

# Release

* * *

Kingston Patch 6

# Cause

* * *

The DemandToProjectCreationHelper script include had been customized.

# Resolution

* * *

Revert the DemandToProjectCreationHelper to the out of box version.
