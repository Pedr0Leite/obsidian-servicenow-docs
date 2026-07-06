---
title: "How to fix missing group notifications"
aliases:
  - KB0785233
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785233
kb_number: KB0785233
last_modified: 2025-10-14
---

## How to fix missing group notifications

  

### Issue

You may not receive group notifications that are subscribable (where the subscribable option is set to true). This article explains how to resolve subscription issues. 

### Release

All supported releases

### Cause

When you receive a subscription notification for the first time, an entry is created in the cmn\_notif\_message table where all notification subscriptions are stored.

If you unsubscribe from a notification, the corresponding record in the cmn\_notif\_message table is updated and the Filter column value changes to Unsubscribe.

If the Filter column has a value of (none), check the Advanced Filter column. If this column has a value of true, open the notification record and review the filter conditions.

When checking the notification preview, you might see this error: "Excluded Recipient because user's notification preference 'Filter' filtered it. See (cmn\_notif\_message.notification\_filter)" 

### Resolution

1.  If you're not receiving notifications, subscribe to the notification.
2.  If you're an admin managing multiple users, update the records for these users in the cmn\_notif\_message table.
