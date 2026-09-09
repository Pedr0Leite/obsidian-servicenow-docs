---
title: "One time code via email is  not sending during the Multifactor Authentication process (MFA)"
aliases:
  - KB0818495
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818495
kb_number: KB0818495
last_modified: 2026-08-17
---

## One time code via email is not sending during the Multifactor Authentication process (MFA)

  

### Issue

During the Multifactor authentication process "one-time code via email" is not being sent to the user.

On a  Multifactor Authentication enabled instance, once in front of the login screen, user will input their credentials.

![](sys_attachment.do?sys_id=b5356c89db4cb4d04cfbeeb5ca96198d)

After this step the following screen follows: 

![](sys_attachment.do?sys_id=b1356c89db4cb4d04cfbeeb5ca961990)When clicking on "Click here to receive a one time code via email", no email is sent.

### Release

All

### Resolution

After having made sure that the user has a valid email address in the user record, please make sure that the notification  called "OneTimePasswordEmailNotification" is enabled.
