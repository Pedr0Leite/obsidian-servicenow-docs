---
title: "Inbound emails with attached icons / logos / signatures images add duplicate repeated attachments in Activity Stream of target record"
aliases:
  - KB0691482
tags:
  - servicenow
  - support-kb
  - inbound-email
  - sys_attachment
  - system-properties
  - email-images
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0691482
kb_number: KB0691482
last_modified: 2025-10-28
---

## Inbound emails with attached icons / logos / signatures images add duplicate repeated attachments in Activity Stream of target record

  

### Issue

Attachment icons/images of Signatures continue to display even after setting system property '**glide.email.inbound.image\_sys\_attachment.filter.action**'.

### Cause

When processing inbound emails which has images such as attachment icons/logos/email signature, the platform creates duplicate records in the sys\_attachment table for the target table record even if system property **glide.email.inbound.image\_sys\_attachment.filter.action** value is set as **AttachNone**.

### Symptoms

1.  Duplicate image attachments in the **Manage Attachments** section at the top of table record in form view which keeps on increasing with forthcoming reply emails.
2.  The same duplicate images keep on appearing on the **Activity Notes** in addition to **Email updates**.

### Resolution

Using system property **glide.email.inbound.image\_sys\_attachment.filter.action** alone does not work. To filter images from emails and reduce duplicate image attachments to target records, configure both of the following mentioned system properties:

1.  glide.email.inbound.image\_sys\_attachment.filter.minimum\_bytes
2.  glide.email.inbound.image\_sys\_attachment.filter.action

### Related Links

[Email image filtering properties](https://docs.servicenow.com/csh?topicname=email-image-filters.html&version=latest "Email image filtering properties")

## Related

- [[KB0693349 - Inbound emails received and processed display broken attached images in preview HTML body and in target record activity ]] — related inbound email inline-image processing issue
- [[KB0529478 - Emails to incidents come in as winmail.dat attachments]] — another inbound email attachment artifact caused by sender-side formatting
- [[KB0520595 - Inbound Email overview and troubleshooting]] — general inbound email troubleshooting overview
