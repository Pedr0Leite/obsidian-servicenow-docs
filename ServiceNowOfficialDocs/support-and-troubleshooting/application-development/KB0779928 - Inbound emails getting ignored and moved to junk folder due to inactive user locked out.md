---
title: "Inbound emails getting ignored and moved to junk folder due to inactive user locked out"
aliases:
  - KB0779928
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779928
kb_number: KB0779928
last_modified: 2026-02-12
---

## Inbound emails getting ignored and moved to junk folder due to inactive user locked out

  

### Issue

Incoming emails to the instance may get skipped and not be processed, with their state in received-ignored.

The email logs traces errors like:  
Skipping <Inbound\_Action\_Name>, User Guest User with email guest@example.com is locked out  
Skipping <Inbound\_Action\_Name>, User Guest User with email guest@example.com is inactive

### Facts

-   Email processing follows a user-based authentication model:
    -   Emails from senders existing in the user table are processed under that user's context
    -   Emails from external senders (not in user table) are processed by the guest user
-   The guest user account must be active to process external emails
-   When the guest user is inactive or locked out, the system skips processing and marks emails as "received-ignored"
-   Proper permissions are required for the guest user to perform actions like creating incidents or processing attachments

### Release

All releases

### Cause

When a user sends an email to the instance from an email address which is not present in the sys\_user table, the system impersonates the Guest user account and updates / creates a target record.

In order for emails to get processed by unknown addresses, the Guest account with email address guest@example.com should always be present and active in the sys\_user table.

Even if the administrator creates a new account with user\_name as Guest and email address as guest@example.com, this would not work. The default Guest user account must be active in the system if you want to allow unknown inbound email addresses.

### Resolution

Enable the default Guest user record and make sure Active = True and is not locked out. You can then reprocess the emails which were ignored, if necessary.

### Related Links

[Emails being received-ignored with an unknown error string](https://support.servicenow.com/kb_view.do?sysparm_article=KB0870995 "Emails being received-ignored with an unknown error string")

[Reviewing emails getting ignored by inbound actions](https://support.servicenow.com/kb_view.do?sysparm_article=KB0535493 "Reviewing emails getting ignored by inbound actions")
