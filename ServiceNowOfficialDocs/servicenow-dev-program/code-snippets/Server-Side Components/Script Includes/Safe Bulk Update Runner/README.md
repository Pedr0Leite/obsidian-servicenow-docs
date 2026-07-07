---
title: "Safe Bulk Update Runner"
aliases:
  - Safe Bulk Update Runner
tags:
  - servicenow-dev-program
  - code-snippet
  - safe-bulk-update-runner
  - script-includes
---

# Safe Bulk Update Runner (auto-throttled)

## Use case
Run large backfills/hygiene tasks without timeouts or instance impact. Instead of one risky long transaction, process records in chunks and automatically schedule the next slice.

## Where to use it
- Script Include invoked from Background Script, on-demand Scheduled Job, or Flow Action wrapper.

## How it works
- Queries a time-boxed chunk (e.g., 40 seconds, 500 rows).
- Executes a caller-supplied per-record function.
- Saves a checkpoint (`sys_id`) in a system property.
- Uses `ScheduleOnce` to queue the next slice (no `gs.sleep`).

## Configuration
- Target table, encoded query, orderBy field (default `sys_id`)
- Chunk size, max execution seconds
- Property name for checkpoint

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
