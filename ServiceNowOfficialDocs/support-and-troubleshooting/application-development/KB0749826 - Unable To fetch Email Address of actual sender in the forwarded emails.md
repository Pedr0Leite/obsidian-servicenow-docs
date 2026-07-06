---
title: "Unable To fetch Email Address of actual sender in the forwarded emails"
aliases:
  - KB0749826
  - Unable To fetch Email Address of actual sender in the forwarded emails
tags:
  - servicenow
  - support-kb
  - inbound-email
  - email-headers
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749826
kb_number: KB0749826
last_modified: 2024-04-07
---

## Unable To fetch Email Address of actual sender in the forwarded emails

  

### Issue

Email address of the sender who has initiated the mail to instance is not visible in the "FROM" field of the activity log. As the emails can be forwarded to the instance , the body of the email should contain the email address in FROM field of the email. 

When an email is sent to the instance in order to update a record on a table, this email updates the record and the same is logged in the activity log of the incident.

The issue occurs when the email address of the sender is not populated beside the display name in FROM field inside the activity log of a record

Activity log in a record:

![](sys_attachment.do?sys_id=0690c278dbccb0d0471f9c41ba961919)

  

Incoming email log of above record:

![](sys_attachment.do?sys_id=0290c278dbccb0d0471f9c41ba961917)

### Cause

This behaviour is due to the mail server of the sender which is actually not populating the email address in the FROM field of the initial email.

The mail address is not populated in the email body under the FROM field on the instance and neither in the activity log of the respective record.

### Resolution

Reach your email admin and also check your outlook or email client properties to validate if the email address is actually updated in the "email" field on your email account profile.

## Related

- [[KB0817647 - Forwarded emails and SPAM SPF_SOFTFAIL or SPF_HARDFAIL]]
- [[KB0749517 - Inbound email embedded images are being added as attachments to the target record]]

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0520595 - Inbound Email overview and troubleshooting|Inbound Email overview and troubleshooting]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0529478 - Emails to incidents come in as winmail.dat attachments|Emails to incidents come in as winmail.dat attachments]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0691482 - Inbound emails with attached icons logos signatures images add duplicate repeated attachments in Activity Stream of targ|Inbound emails with attached icons / logos / signatures images add duplicate repeated attachments in Activity Stream of target record]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0693349 - Inbound emails received and processed display broken attached images in preview HTML body and in target record activity |Inbound emails received and processed display broken attached images in preview HTML body and in target record activity stream notes]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0749517 - Inbound email embedded images are being added as attachments to the target record|Inbound email embedded images are being added as attachments to the target record]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0749868 - Inbound emails are not creating HR cases|Inbound emails are not creating HR cases]]
