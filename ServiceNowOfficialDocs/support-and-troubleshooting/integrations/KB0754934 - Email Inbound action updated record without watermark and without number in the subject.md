---
title: "Email Inbound action updated record without watermark and without number in the subject"
aliases:
  - KB0754934
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0754934
kb_number: KB0754934
last_modified: 2024-04-07
---

## Email Inbound action updated record without watermark and without number in the subject

  

### Issue

How is it possible that a reply to the original Email that was first sent to an instance can end up updating the target case although that original Email does not contain anywhere a record number, nor even a watermark ?

-   Email A sent out to an instance 
-   Email A received and Inbound Action processes Email and creates a new record
-   Email sender, opens up original Email in Outlook and sends a reply to that same Email.

### Release

All

### Cause

Expected behaviour that Email should open a duplicate record

### Resolution

When a received email does not have watermark and record number, ServiceNow checks the email in-reply-to header.

If the header contains a <messageID> value that matches a previously received email message that resulted in a record creation, then the email is classified as a Reply to that record and the record is updated
