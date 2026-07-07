---
title: "Safe Bulk Update with Logging"
aliases:
  - Safe Bulk Update with Logging
tags:
  - servicenow-dev-program
  - code-snippet
  - safe-bulk-update-with-logging
  - background-scripts
---

# Safe Bulk Record Update with Logging

## Overview
Efficiently update multiple records in batch with error handling, progress tracking, and logging to prevent timeouts and data loss.

## What It Does
- Updates records in configurable batch sizes
- Logs progress for monitoring
- Handles individual record errors without stopping batch
- Prevents script timeout with batch processing
- Tracks success/failure counts
- Logs detailed error information

## Use Cases
- Bulk data migrations
- Mass field updates after deployment
- Scheduled bulk corrections
- Data cleanup operations
- Batch status updates across records

## Files
- `bulk_update_with_progress.js` - Background Script for safe bulk updates

## How to Use

### Option 1: Run as Background Script
1. Go to **System Diagnostics > Script Background**
2. Copy code from `bulk_update_with_progress.js`
3. Modify the table name and query filter
4. Execute and monitor logs

### Option 2: Create as Scheduled Job
1. Go to **System Scheduler > Scheduled Jobs**
2. Create new job with the script code
3. Schedule for off-peak hours
4. Logs will be available in System Logs

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
