---
title: "Password Reset SMS verification code sent with a [question mark]\"?\" when you are using  iPhones"
aliases:
  - KB0691022
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0691022
kb_number: KB0691022
last_modified: 2024-04-07
---

## Password Reset SMS verification code sent with a \[question mark\]"?" when you are using iPhones

  

### Issue

# Symptoms

* * *

When we are using Password Reset Process, we have an option to enroll devices for Two Factor authentication.  
  
During this process, we are seeing that "NEWLINE" in the message body is interpreting as "?" in the SMS in iPhones  
  
[https://docs.servicenow.com/csh?topicname=t\_EnrollUsingSMS.html&version=latest](https://docs.servicenow.com/csh?topicname=t_EnrollUsingSMS.html&version=latest)

![](sys_attachment.do?sys_id=a31ff026db0ab450e515c2230596199c)

# Release

* * *

When working Password Reser Plugin

# Cause

* * *

In the email body we are seeing a NEW LINE and it's causing the issue for us here.

# Resolution

* * *

Goto the email Notification.

/nav\_to.do?uri=sysevent\_email\_action.do?sys\_id=7cd0c421bf200100710071a7bf0739bd%26sysparm\_view=advanced

Please remove the space between 

  
Use this verification code to verify your identity:   
<<SPACE>>  
${event.parm2}   
  
and set it as "Use this verification code to verify your identity: ${event.parm2}" in Message and SMS.
