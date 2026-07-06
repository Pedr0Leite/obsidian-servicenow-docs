---
title: "Inbound emails received and processed display broken attached images in preview HTML body and in target record activity stream notes"
aliases:
  - KB0693349
tags:
  - servicenow
  - support-kb
  - inbound-email
  - system-properties
  - email-images
  - activity-stream
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693349
kb_number: KB0693349
last_modified: 2026-05-06
---

## Inbound emails received and processed display broken attached images in preview HTML body and in target record activity stream notes

  

### Issue

When an email is sent to a ServiceNow instance with embedded/inline images in the email body, the email is received and processed successfully, but the images appear broken when checking the received email in activity notes of target record.  
  

Symptoms

* * *

When you open the target task record (incident/problem/change etc.) that is created/updated by the received email, the email content displays broken images / broken links in the activity notes.  
  

![Broken Image](sys_attachment.do?sys_id=3ec365969360c314101833527cba1090 "Broken Image")

### Release

All releases

### Resolution

The system property **glide.email.inbound.convert\_html\_inline\_attachment\_references** is set to false or probably misconfigured. This is a Boolean property (true/false). The term "misconfigured" means the property type is opted as String with value false. Setting this system property to true with the correct type will fix the issue for new inbound emails and apply no changes on previous emails.

## Related

- [[KB0691482 - Inbound emails with attached icons logos signatures images add duplicate repeated attachments in Activity Stream of targ]] — related inbound email attachment/image property tuning
- [[KB0520595 - Inbound Email overview and troubleshooting]] — general inbound email troubleshooting overview
