---
title: "Engineering License Dashboard (OpenLM Integration) – Data not visible in SAM Workspace"
aliases:
  - KB2593278
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2593278
kb_number: KB2593278
last_modified: 2026-05-21
---

## Issue

ServiceNow receives OpenLM data, but no meaningful information appears in the Engineering License Overview dashboard.  
Raw tables (like `ua_app_usage` and `samp_eng_app_license`) contain records, but most widgets in the workspace are blank.

## Resolution

Engage OpenLM support to fix the data feed.  
Request them to ensure at least one valid engineering license record is sent into `samp_eng_app_license` with:

`active = true`

`norm_product` populated

`norm_publisher` populated

`quantity` populated

`license_type` populated

Once valid license data exists, ServiceNow scheduled jobs will populate:

`samp_eng_app_usage_summary`

`samp_eng_app_utilization_user_ratio`

`samp_eng_app_product_usage`

`samp_eng_app_usage_by_country`

and the dashboard widgets will display correctly.

* * *

### Recommendations / Next Steps

Validate with OpenLM why all license rows are imported as inactive.

Ensure transform mappings populate normalized publisher/product fields.

Re-run ServiceNow scheduled jobs once the corrected data is loaded.

Reference documentation for expected data model and table dependencies:  
[Engineering License Overview (Concurrent Licenses)](https://www.servicenow.com/docs/bundle/xanadu-it-asset-management/page/product/software-asset-management2/concept/concurrent-licenses.html)

* * *

### Support Scope

The OpenLM → ServiceNow import and transform are maintained by OpenLM.

ServiceNow’s role is to validate that jobs and dashboards behave as designed once correct data is present.
