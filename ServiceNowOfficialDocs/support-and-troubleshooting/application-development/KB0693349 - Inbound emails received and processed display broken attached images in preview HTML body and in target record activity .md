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

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0691482 - Inbound emails with attached icons logos signatures images add duplicate repeated attachments in Activity Stream of targ|Inbound emails with attached icons / logos / signatures images add duplicate repeated attachments in Activity Stream of target record]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0749517 - Inbound email embedded images are being added as attachments to the target record|Inbound email embedded images are being added as attachments to the target record]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0689652 - Troubleshooting users unable to access responsive dashboards|Troubleshooting users unable to access responsive dashboards]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0759218 - Certain fields are visible to non-admin users only when the fields not empty.|Certain fields are visible to non-admin users only when the fields not empty.]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0782082 - When 'Admin Overrides' is unchecked and the requirement is to allow a specific roled users (but not admin) to access a f|When 'Admin Overrides' is unchecked and the requirement is to allow a specific roled users (but not admin) to access a field, need to make to use of ACL script.]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0816018 - Admin role does not pass an ACL when Admin Overrides is selected|Admin role does not pass an ACL when Admin Overrides is selected]]
