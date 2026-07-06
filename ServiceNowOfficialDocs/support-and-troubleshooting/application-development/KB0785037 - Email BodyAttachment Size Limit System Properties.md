---
title: "Email Body/Attachment Size Limit System Properties"
aliases:
  - KB0785037
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785037
kb_number: KB0785037
last_modified: 2026-05-06
---

## Email Body/Attachment Size Limit System Properties

  

### Summary

The system properties **glide.email.inbound.max\_body\_chars** and **glide.email.outbound.max\_body\_chars** are used to limit excessive sys\_email HTML and plain text message data when processed in the instance. The default value is ~524k characters (524288) and does not consider the email headers or any attachments.

These properties are not based on multi-byte character encoding as the previous ones pre-London, to prevent confusion understanding how big a message really is. If the message of an incoming email exceeds the size defined in **glide.email.inbound.max\_body\_chars**, then truncation will occur in the message data itself.

Calendar, image, octet stream and RFC822 compliant message attachments are separately limited in size by **glide.email.inbound.max\_total\_attachment\_size\_bytes**. If any one attachment exceeds the limit defined there then that attachment will be discarded completely and a reason will be logged. If the limit is reached prior to reading remaining attachments, the remaining attachments are not stored.

[KB0521772](https://hi.service-now.com/kb_view.do?sysparm_article=KB0521772 "KB0521772") notes that the ServiceNow email servers have an encoded size limit of an inbound email is 75MB and 25MB for outbound email. It also notes that encoding can increase the size of the original attachment by 1.3 - 1.4x. Therefore a limit of 50MB in total for an inbound email and 18MB in total for outbound email are reasonable expectations. This total includes the entire email - HTML, plain text, attachments, headers and any encoding overhead.

If an inbound email exceeds the mail server's limit, the in-instance properties described here do not apply because the email is never read into the instance. In this case it is rejected at the mail server level.

If the system property specific to email attachments **glide.email.inbound.max\_total\_attachment\_size\_bytes** is exceeded, email logs will trace the error message:  
Maximum combined attachment size exceeded. (max:18874368 bytes). One or more attachment records ignored.  
  
For outbound email, the size of the encoded headers, message HTML and plaintext, and any encoding cannot exceed 25 MB. The default value for **glide.email.outbound.max\_total\_attachment\_size\_bytes** is 18MB which should leave sufficient capacity for a reasonably large message body, headers, and any encoding needed to produce the email. 

There should always be a differentiation between the properties **glide.email.outbound.max\_total\_attachment\_size\_bytes** and **glide.email.inbound.max\_total\_attachment\_size\_bytes** as they apply exclusively to attachments processed via emails. In contrast, **com.glide.attachment.max\_size** is relevant for all other attachments processed within the system, excluding those via emails.

Although they serve different purposes, **com.glide.attachment.max\_size** sets the maximum file size allowed for any attachment in the system and overrides any larger values set by **glide.email.inbound.max\_total\_attachment\_size\_bytes** and **glide.email.outbound.max\_total\_attachment\_size\_bytes**.

### Related Links

-   [Message body size limit properties](https://docs.servicenow.com/csh?topicname=r_EmailBodySizeLimitProperties.html&version=latest "Message body size limit properties")
-   [Email server size limit prevents emails from being sent or received](https://support.servicenow.com/kb_view.do?sysparm_article=KB0521772 "Email server size limit prevents emails from being sent or received")
-   [Attachment Properties](https://docs.servicenow.com/csh?topicname=r_AttachmentLimitProperties.html&version=latest)
