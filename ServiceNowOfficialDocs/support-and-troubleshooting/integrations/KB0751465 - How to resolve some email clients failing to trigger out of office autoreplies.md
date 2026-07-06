---
title: "How to resolve some email clients failing to trigger out of office autoreplies"
aliases:
  - KB0751465
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0751465
kb_number: KB0751465
last_modified: 2026-03-10
---

## How to resolve some email clients failing to trigger out of office autoreplies

  

### Issue

An email sent from an instance to a mailbox that has an out-of-office autoreply set up fails to trigger the out-of-office reply message. Consequently, no autoreply email is received. The email client, such as Outlook or Gmail, is not creating the out of office reply message.

### Release

### Cause

This can be caused by the following terms in outbound email headers:

-   **Precedence:bulk** - Some spam filters flag bulk email as spam
-   **Auto-submitted:auto-generated** \- Some email clients treat these as automated emails and do not bother triggering an auto reply email

### Resolution

Remove the terms from the email header sent by the instance. When received, this enables email clients, such as Gmail, to create and send the out of office autoreply.    

To do this:

1.  Go to the System Properties (Sys\_properties) table.
2.  Update the property **glide.smtp.precedence\_bulk** and set the value as **false**
3.  Update the sys\_property **glide.email.outbound.header.auto\_submitted** and ensure it is blank.

**Note**:  If these system properties are not already present, you may create them

**Warning**: Ensure these actions are tested in sub-production instances before implemented in production environments
