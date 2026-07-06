---
title: "The email notification for an Outlook meeting invite is not showing the description field"
aliases:
  - KB0728505
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0728505
kb_number: KB0728505
last_modified: 2025-06-05
---

## The email notification for an Outlook meeting invite is not showing the description field

  

### Issue

This issue occurs when: 

-   You are sending an invite type notification.
-   The invite is correct and contains DESCRIPTION: ${description} in the meeting template body.
-   The notification received by the email client has NO description (it is blank).

### Release

All

### Cause

For email meeting invites, you need to define the fields used on the email template in the email notification body.

### Resolution

Make sure to add the required fields used on the email template, DESCRIPTION: ${description}, in the email notification body.
