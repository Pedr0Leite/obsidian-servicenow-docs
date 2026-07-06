---
title: "Microsoft Office365 SMTP configured  in ServiceNow, but SMTP connection fails with  STARTTLS on port 587"
aliases:
  - KB0787245
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787245
kb_number: KB0787245
last_modified: 2024-04-26
---

## Issue

When testing connection for a new SMTP Email account using Microsoft Office365 with STARTLS on port 587 , the following Error is shown in the UI

## Email sender connection invalid.: Cannot connect to SMTP server: smtp.office365.com, as: email@domain.com, message: 535 5.7.3 Authentication unsuccessful

## Resolution

Here are the following Microsoft recommendations when this error is shown

POP and IMAP email settings for Outlook  
[https://support.office.com/en-gb/article/pop-and-imap-account-settings-cb41d2b8-98cb-4ab2-ad60-218349f37e2e?redirectSourcePath=%252fen-us%252farticle%252fPOP-and-IMAP-settings-for-Outlook-Office-365-for-business-7fc677eb-2491-4cbc-8153-8e7113525f6c&ui=en-US&rs=en-GB&ad=GB](https://support.office.com/en-gb/article/pop-and-imap-account-settings-cb41d2b8-98cb-4ab2-ad60-218349f37e2e?redirectSourcePath=%252fen-us%252farticle%252fPOP-and-IMAP-settings-for-Outlook-Office-365-for-business-7fc677eb-2491-4cbc-8153-8e7113525f6c&ui=en-US&rs=en-GB&ad=GB)  
  
and  
  
POP and IMAP account settings  
[https://support.office.com/en-gb/article/pop-and-imap-account-settings-cb41d2b8-98cb-4ab2-ad60-218349f37e2e?redirectSourcePath=%252fen-us%252farticle%252fPOP-and-IMAP-settings-for-Outlook-Office-365-for-business-7fc677eb-2491-4cbc-8153-8e7113525f6c&ui=en-US&rs=en-GB&ad=GB](https://support.office.com/en-gb/article/pop-and-imap-account-settings-cb41d2b8-98cb-4ab2-ad60-218349f37e2e?redirectSourcePath=%252fen-us%252farticle%252fPOP-and-IMAP-settings-for-Outlook-Office-365-for-business-7fc677eb-2491-4cbc-8153-8e7113525f6c&ui=en-US&rs=en-GB&ad=GB)

DNS record

Create DNS records at any DNS hosting provider for Office 365  
[https://docs.microsoft.com/en-us/office365/admin/get-help-with-domains/create-dns-records-at-any-dns-hosting-provider?view=o365-worldwide](https://docs.microsoft.com/en-us/office365/admin/get-help-with-domains/create-dns-records-at-any-dns-hosting-provider?view=o365-worldwide)

See doc link on Additional email properties

[https://docs.servicenow.com/csh?topicname=r\_AdditionalProperties.html&version=latest](https://docs.servicenow.com/csh?topicname=r_AdditionalProperties.html&version=latest)

It is possible to get more verbosity in the logs by adding system properties 'glide.smtp.debug', this should be set to true.

![](sys_attachment.do?sys_id=10f2219adbae60102e6a2183ca961929)
