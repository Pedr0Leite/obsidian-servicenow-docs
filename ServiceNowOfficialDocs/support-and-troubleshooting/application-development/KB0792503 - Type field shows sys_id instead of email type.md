---
title: "Type field shows sys_id instead of email type"
aliases:
  - KB0792503
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792503
kb_number: KB0792503
last_modified: 2025-10-29
---

## Type field shows sys\_id instead of email type

  

### Issue

When viewing system-generated emails in System Logs > Emails, you may see a sys\_id in the type field instead of the expected display value of the type of email, like send-ready. 

### Release

All supported releases

### Cause

This is the normal operation with processing queues that are handled by multiple scheduled jobs. The type field temporarily stores the sys\_id of scheduled sender jobs during email processing. You typically only see these sys\_ids when checking jobs very quickly or when sending many emails at once. 

### Resolution

To verify this information:

1.  Go to **System Scheduler** > **Scheduled Jobs**.
2.  Search for the sys\_id you found in the type field.
3.  Confirm that the sys\_id belongs to a scheduled job record such as SMTP Sender, SMTP Sender2, or SMS Sender.
