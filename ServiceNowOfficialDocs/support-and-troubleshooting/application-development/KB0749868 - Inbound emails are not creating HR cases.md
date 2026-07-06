---
title: "Inbound emails are not creating HR cases"
aliases:
  - KB0749868
  - Inbound emails are not creating HR cases
tags:
  - servicenow
  - support-kb
  - inbound-email
  - hr-service-delivery
  - hr-cases
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749868
kb_number: KB0749868
last_modified: 2024-04-07
---

## Inbound emails are not creating HR cases

  

### Issue

# Symptoms

Inbound emails to the instances are not creating HR Cases. 

# Release

Valid for all releases

# Cause

The out of the box inbound email actions for creating HR cases are - 'Create HR Case' and 'Create HR Case (Forwarded)'.

These inbound email actions are not matching, leading the HR cases not getting created. The primary condition for these inbound email actions is 

email.recipients.indexOf(gs.getProperty("sn\_hr\_core.hr\_email")) > -1

This is dependent on the system property - 'sn\_hr\_core.hr\_email', which is not set correctly in the instance.

# Resolution

'sn\_hr\_core.hr\_email' property needs to be set.

The value for system property 'sn\_hr\_core.hr\_email' is case sensitive. The user will need to make sure the incoming email address is the same as what is configured this system property.

When email comes to the instance through this email address, the primary condition mentioned above will match and inbound email actions will work to create HR case as expected.

## Related

- [[KB0749517 - Inbound email embedded images are being added as attachments to the target record]]
- [[KB0749826 - Unable To fetch Email Address of actual sender in the forwarded emails]]

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0520595 - Inbound Email overview and troubleshooting|Inbound Email overview and troubleshooting]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0529478 - Emails to incidents come in as winmail.dat attachments|Emails to incidents come in as winmail.dat attachments]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0691482 - Inbound emails with attached icons logos signatures images add duplicate repeated attachments in Activity Stream of targ|Inbound emails with attached icons / logos / signatures images add duplicate repeated attachments in Activity Stream of target record]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0693349 - Inbound emails received and processed display broken attached images in preview HTML body and in target record activity |Inbound emails received and processed display broken attached images in preview HTML body and in target record activity stream notes]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0749517 - Inbound email embedded images are being added as attachments to the target record|Inbound email embedded images are being added as attachments to the target record]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0749826 - Unable To fetch Email Address of actual sender in the forwarded emails|Unable To fetch Email Address of actual sender in the forwarded emails]]
