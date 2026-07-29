---
title: "How to fix event notifications that fail to trigger"
aliases:
  - KB0791868
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791868
kb_number: KB0791868
last_modified: 2026-01-12
---

## How to fix event notifications that fail to trigger

  

### Issue

If you configured a notification to trigger on a specific event, the notification may not activate when the event occurs. This article helps you to resolve the event notification triggering issue.

### Release

All supported releases

### Cause

This issue is caused because the event name in the event registry doesn't match the name in the event logs. When these names don't match exactly, the notification system can't recognize the event and won't trigger the notification. Common issues include:

-   Extra spaces at the end of the event name (for example, "X " instead of "X")
-   Case sensitivity differences
-   Spelling inconsistencies

### Resolution

Verify that the event name in the event registry exactly matches the event name in the event logs.

**Note**: This article assumes that:

-   Preview notifications are working correctly.
-   The Notification Device \[cmn\_notif\_device\] table contains proper recipient records.
-   The Notification Messages \[cmn\_notif\_message\] table contains correct message data.

### Related Links
