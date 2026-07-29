---
title: "Transfer HR Case Fails for Bot-Created Cases Due to Correlation ID Conflict"
aliases:
  - KB2633860
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2633860
kb_number: KB2633860
last_modified: 2026-01-01
---

## Transfer HR Case Fails for Bot-Created Cases Due to Correlation ID Conflict

  

### Issue

The Transfer HR Case functionality does not work for cases created by system or bot processes.  
Attempts to transfer these cases to another HR Service result in errors such as “Failed to insert a new case”.  
The issue is reproducible in multiple environments.

### Release

Any Release

### Cause

-   A unique key violation occurs on the Correlation ID field during case transfer.
-   When transferring, the correlation\_id from the original case is copied to the new case, causing the insert to fail.

### Resolution

Verify the Error:

-   Check system logs for messages like “Failed to insert a new case” or unique key violation on correlation\_id.

Update System Property:

-   Navigate to System Properties → HR Core.
-   Locate the property:

-   sn\_hr\_core.transfer\_case.ignored\_fields

-   Add correlation\_id to the list of ignored fields.

Validate Transfer Functionality:

-   Attempt to transfer a bot-created HR case to another HR Service.
-   Confirm that the transfer completes successfully without errors.

Plan for Permanent Fix:

-   Monitor release notes for the scheduled fix associated with PRB1918489.
-   The permanent fix is targeted for the Australia release (expected March 2026).
-   Remove the workaround after upgrading to the release containing the official fix.
