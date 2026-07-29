---
title: "One time password when ldap server is down"
aliases:
  - KB0778193
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778193
kb_number: KB0778193
last_modified: 2025-11-04
---

## One time password when ldap server is down

  

### Issue

When ldap server is not connecting successfully, you can still be able to login to the instance by requesting one time password. 

### Release

ALL

### Cause

Test connection on the ldap server record is unsuccessful causing all users to fail authentication via LDAP.

### Resolution

1.  Go to https://INSTANCE.service-now.com/login.do and enter your ldap credentials. 
2.  Because ldap server is unable to connect successfully, you will get the message at top of the login page saying 'Your account is configured to use LDAP authentication, and we cannot currently connect to the LDAP server. Please contact your ServiceDesk to resolve this issue. To obtain a password for one-time login, click here. An email message containing the password will be sent to you.'
3.  On clicking 'click here' to obtain a password for one-time login, you will receive an email with one time password to login to the instance. 
4.  One time password will only be sent if `'glide.ldap.onetime.password.enabled' system property is set to 'true'`
5.  'glide.authenticate.onetime.password.validity' is the system property that controls the validity of this one time password, the default validity is 10 minutes
6.  Go to https://INSTANCE.service-now.com/login.do and enter your user\_id and one time password sent to your email.
7.  You will be able to login to the instance.
