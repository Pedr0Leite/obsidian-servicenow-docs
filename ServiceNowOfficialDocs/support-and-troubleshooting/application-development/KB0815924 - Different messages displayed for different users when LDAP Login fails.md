---
title: "Different messages displayed for different users when LDAP Login fails"
aliases:
  - KB0815924
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815924
kb_number: KB0815924
last_modified: 2024-04-10
---

## Different messages displayed for different users when LDAP Login fails

  

### Issue

When LDAP down, different messages are displayed for different users.

User 1 might get:

Your account is configured to use LDAP authentication, and we cannot currently connect to the LDAP server. Please contact your ServiceDesk to resolve this issue.  
  

User 2 might get:

Your account is configured to use LDAP authentication, and we cannot currently connect to the LDAP server. Please contact your ServiceDesk to resolve this issue. To obtain a password for one-time login, click here. An email message containing the password will be sent to you.  
  

### Release

Applicable to all releases

### Cause

This is expected OOB behavior. If a user has the notification disabled OR does not have any email value in the email field for the sys\_user record, then the message will be displayed as for user 1 above, since the system cannot send emails.

### Resolution

If it is desired that users get message like user 2, then it is required that the users have notifications enabled on the sys\_user table and have valid email address in their sys\_user record.
