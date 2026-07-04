---
title: "Email server size limit prevents emails from being sent or received"
aliases:
  - KB0521772
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0521772
kb_number: KB0521772
last_modified: 2025-09-18
---

## Email server size limit prevents emails from being sent or received

  

### Issue

ServiceNow email servers have a maximum size limit on emails passing out (SMTP) or in (POP3) to the server. This maximum limit cannot be adjusted per instance.

 **Note:** ServiceNow instances have a few properties that limit inbound and outbound email body size as well as additional attachment processing limits. This article discusses the ServiceNow **mail server** infrastructure limits. Properties set on your instance are unrelated to the server size limits discussed in this article, and are not covered here.

Necessary email transmission encoding can significantly increase the total email size compared to the original email data.

You may experience this limit as follows:

-   When sending an email to the instance, it is bounced back for being too large, sometimes even though the email size as seen in your mail client or operating system appears to be under the mail server's documented limit.
-   The following error appears when trying to send emails from the instance: **552 5.3.4 Error: message file too big**.

### Release

All supported versions

### Cause

The ServiceNow servers limit the total encoded email size to 75 MB for inbound (POP3) and 25 MB for outbound (SMTP) emails. Emails beyond this size are rejected.

All emails sent to or from an instance follow the MIME specification (Multipurpose Internet Mail Extensions). Some data in an email (such as an attachment or an inline image attachment) cannot be transmitted in its original format. The MIME specification requires this data to be Base64-encoded, which will increase the original byte size of the attachment data by up to approximately **137%** of the original size.

You must therefore limit the size of all attachments and email body to approximately **50 MB or less** (as seen from your file system or mail client) to ensure that when encoded it will not be rejected. Sys\_email records being sent from ServiceNow must limit the size of all attachments and email body to approximately **18 MB or less**.

When your instance sends emails, this encoding information is based on the way ServiceNow sends outbound emails. When the instance receives emails, the encoding is done by your mail client, and also can be affected by your mail server. Consult your email administrator with questions.

 **Note:** The size limit is for the entire email content: the total size of all attachments, email headers, HTML body, text body, attachments, and some negligible MIME overhead. This limit makes it difficult for the email sender to predict the exact total size of an email _as_ it will be transmitted_._ It is usually large attachments that cause an email to exceed the limit. You can approximate the upper end of the transmission size by finding the size of your attachments in your file system (or by getting the size from sys\_attachment.size\_bytes field for outbound email) and multiplying by 1.37.

### Resolution

When encountering this limit, there is no workaround if using the ServiceNow email servers. You must either send smaller emails (fewer attachments, smaller email body, etc), or employ your own email infrastructure that supports larger emails.

If using your own separate email infrastructure instead of ServiceNow's, the same limit issue can exist. However, the size limit values for inbound and outbound may be different, as well as the error code reported. Consult your system's email administrator if you encounter this error.

### Related Links

-   [Message body size limit properties](https://docs.servicenow.com/csh?topicname=r_EmailBodySizeLimitProperties.html&version=latest "Message body size limit properties")
-   [Email body/attachment size limit system properties](https://support.servicenow.com/kb_view.do?sysparm_article=KB0785037 "Email body/attachment size limit system properties")
