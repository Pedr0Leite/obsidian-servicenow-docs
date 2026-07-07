---
title: "Inbound email embedded images are being added as attachments to the target record"
aliases:
  - KB0749517
  - Inbound email embedded images are being added as attachments to the target record
tags:
  - servicenow
  - support-kb
  - inbound-email
  - attachments
  - email-images
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749517
kb_number: KB0749517
last_modified: 2025-10-28
---

## Inbound email embedded images are being added as attachments to the target record

  

### Issue

When inbound emails are received by an instance, all the embedded images, signatures, or files get attached to the target task record, i.e. the Incident table, along with the actual attachments based on the inbound email action.

This is an out-of-box behavior and can be an issue for users not wanting signatures or images as final attachments into the task table records. It is advisable to implement a custom business rule to prevent storing unwanted attachments, or prevent updating the target record.

### Release

### Cause

There is nothing standard in an incoming MIME email to distinguish whether an image attachment is an unwanted signature or similar file to discard.   
When images arrive in an email, they may or may not have a file name, depending on the sending email application, and they will have attributes like content type and byte size.   
Thus, there are no characteristics to filter on that to be 100% correct for all users all the time, such that it could be implemented as an out-of-box feature.   
  
The only data available to do any sort of filtering is that which is stored in the sys\_attachment table, such as size, filename, content type.   
The byte size feature was added as a shortcut for a commonly seen business rule for customers to add to use filtering, and may not be effective for all users.

### Resolution

This procedure can help administrators to customize the instance accordingly:

  
1) The image filtering properties can be set up in the \[sys\_properties\] table as per requirements:

![Image filtering properties](sys_attachment.do?sys_id=9796467693bc76d48960fb2d6cba1032 "Image filtering properties")  
  
[https://docs.servicenow.com/csh?topicname=email-image-filters.html&version=latest](https://docs.servicenow.com/csh?topicname=email-image-filters.html&version=latest) 

  
  
2) System Property glide.email.inbound.convert\_html\_inline\_attachment\_references

  
[https://docs.servicenow.com/csh?topicname=r\_AdditionalProperties.html&version=latest](https://docs.servicenow.com/csh?topicname=r_AdditionalProperties.html&version=latest%29)

3) It is possible to create a Business Rule on the \[sys\_attachment\] table to remove small embedded image attachments.

[https://community.servicenow.com/community?id=community\_question&sys\_id=e444cb29dbd8dbc01dcaf3231f9619d5](https://community.servicenow.com/community?id=community_question&sys_id=e444cb29dbd8dbc01dcaf3231f9619d5)

## Related

- [[KB0693349 - Inbound emails received and processed display broken attached images in preview HTML body and in target record activity]]
- [[KB0691482 - Inbound emails with attached icons logos signatures images add duplicate repeated attachments in Activity Stream of target]]
- [[KB0529478 - Emails to incidents come in as winmail.dat attachments]]

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0529478 - Emails to incidents come in as winmail.dat attachments|Emails to incidents come in as winmail.dat attachments]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0691482 - Inbound emails with attached icons logos signatures images add duplicate repeated attachments in Activity Stream of targ|Inbound emails with attached icons / logos / signatures images add duplicate repeated attachments in Activity Stream of target record]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0693349 - Inbound emails received and processed display broken attached images in preview HTML body and in target record activity |Inbound emails received and processed display broken attached images in preview HTML body and in target record activity stream notes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Attachment to Base64/README|Attachment to Base64]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Attachment to base64 in scope/README|Attachment to base64 in scope]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Base 64 to Attachment/README|Base 64 to Attachment]]
