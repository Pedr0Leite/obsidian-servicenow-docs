---
title: "User not recognized for incoming emails"
aliases:
  - KB0790953
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790953
kb_number: KB0790953
last_modified: 2024-04-08
---

## User not recognized for incoming emails

  

### Issue

Incoming emails for some users not recognizing users even though their email id exist in the system. Below is the error message in the email log :

Error: watermark's target table 'asmt\_assessment\_instance' does not match any Inbound Action table, setting to 'Ignored' state

### Release

All

### Cause

If 2 different users has same email id in the instance this type of issues will come

### Resolution

 If multiple users have the same email address, the email reader will pick a user randomly. In some cases, it may pick the same user (probably because of cache or because that user always comes up first in DB query, etc).  
Email addresses are supposed to be unique for users in the instance.  
  
Please refer below note from the documentation : [Email](https://docs.servicenow.com/csh?topicname=inbound-action-processing.html&version=latest "Email")  
  
" Note: Each user record must have a unique email address so that the instance can reliably match the email to the correct user. "
