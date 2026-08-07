---
title: "Employee Center Performance Degradation Due to Slow 'track_events' API Calls"
aliases:
  - KB2639205
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2639205
kb_number: KB2639205
last_modified: 2026-01-01
---

## Employee Center Performance Degradation Due to Slow 'track\_events' API Calls

  

### Issue

After the Yokohama upgrade, the Employee Center portal experienced long loading times due to the Content Analytics plugin's `track_events` REST call, which could take from 100ms up to 6s per page load. Performance degradation was traced to slow database queries on the `sn_cda_tracked_fld_value` table, which lacked appropriate indexing and accumulated large volumes of records.

### Release

Any Release

### Cause

The `track_events` API calls were delayed because the `sn_cda_tracked_fld_value` table did not have an index on the `value` and `field` columns, causing inefficient queries in instances with large data volumes.

### Resolution

To improve performance:

-   Navigate to System Definition > Tables and open the `sn_cda_tracked_fld_value` table.
-   Add a composite index on the columns `value` and `field`.
-   After adding the index, verify that `track_events` API calls complete within acceptable time (typically under 100ms).
-   Monitor performance after implementation to confirm improvement.
-   Note: ServiceNow has logged PRB1885734 for a permanent fix in future releases.
