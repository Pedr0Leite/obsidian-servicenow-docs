---
title: "Incident resolution percentile by assignment group"
aliases:
  - Incident resolution percentile by assignment group
tags:
  - servicenow-dev-program
  - code-snippet
  - incident-resolution-percentile-by-assignment-group
  - glideaggregate
---

# Incident resolution percentile by assignment group

## What this solves
Leaders often ask for P50 or P90 of incident resolution time by assignment group. Out-of-box reports provide averages, but percentiles are more meaningful for skewed distributions. This utility computes configurable percentiles from incident resolution durations.

## Where to use
- Script Include callable from Background Scripts, Scheduled Jobs, or Flow Actions
- Example Background Script is included

## How it works
- Uses `GlideAggregate` to get candidate groups with resolved incidents in a time window
- For each group, queries resolved incidents ordered by resolution duration (ascending)
- Picks percentile ranks (for example 0.5, 0.9) using nearest-rank method
- Returns a simple object per group with count, average minutes, and requested percentiles

## Configure
- `WINDOW_DAYS`: number of days to look back (default 30)
- `GROUP_FIELD`: field to group by (default `assignment_group`)
- Percentiles array (for example `[0.5, 0.9]`)

## References
- GlideAggregate API  
  https://www.servicenow.com/docs/bundle/zurich-api-reference/page/app-store/dev_portal/API_reference/GlideAggregate/concept/c_GlideAggregateAPI.html
- GlideRecord API  
  https://www.servicenow.com/docs/bundle/zurich-api-reference/page/app-store/dev_portal/API_reference/GlideRecord/concept/c_GlideRecordAPI.html
- GlideDateTime API  
  https://www.servicenow.com/docs/bundle/zurich-api-reference/page/app-store/dev_portal/API_reference/GlideDateTime/concept/c_GlideDateTimeAPI.html

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count All Open Incidents Per Priority/readme|Count All Open Incidents Per Priority]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count Inactive Users with Active incidents/README|Count Inactive Users with Active incidents]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count incidents based on category/README|Count incidents based on category]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Count open Incidents per Priority and State using GlideAggregate/README|Count open Incidents per Priority and State using GlideAggregate]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Create Problem based on incident volume/README|Create Problem based on incident volume]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideAggregate/Find Oldest Open Incidents per Group/README|Find Oldest Open Incidents per Group]]
