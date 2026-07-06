---
title: "How to resolve email notifications marked as send-ignored"
aliases:
  - KB0790932
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790932
kb_number: KB0790932
last_modified: 2025-10-24
---

## How to resolve email notifications marked as send-ignored

  

### Issue

Email notifications may unexpectedly appear with the send-ignored status without a clear indication why. When this happens, neither the email logs attached to the sys\_email record nor the record details explain the reason for this status. The sys\_email record headers often appear incomplete. 

* * *

![Example of email header](/sys_attachment.do?sys_id=cc69b0219374f2547c79b36d6cba100e)

* * *

![Example of second email header with create date and message details](/sys_attachment.do?sys_id=0869b0219374f2547c79b36d6cba10e7)

### Release

All supported releases

### Cause

This issue occurs when duplicate notification emails with identical content are triggered simultaneously from a single event.

To verify if this is causing your issue:

1.  Isolate a sys\_email record marked as send-ignored.
2.  Search for other sys\_email records created at the exact same second.
3.  Check if you find another record sent to the same recipients as your problem email, but with one email sent and the other ignored.

![Example of identical email records with exact timestamps - one sent and one marked send-ignored](/sys_attachment.do?sys_id=7759b0219374f2547c79b36d6cba100c)

  

To prevent redundancy, ServiceNow automatically filters out duplicate emails. When two notifications with the identical content trigger from the same event and target the same recipients, the system marks one as send-ignored to prevent sending identical messages. 

### Resolution

Use one of the following methods to resolve this issue:

1.  **Change the order** of the notifications so both notifications fire at slightly different times. This prevents the redundancy check.
2.  **Change the weight** of the notification records so only the notification with the higher weight fires. This avoids the redundancy check.
3.  **Modify the email body** of the notifications, even slightly, to prevent the redundancy check.

These solutions prevent emails from being marked as send-ignored.
