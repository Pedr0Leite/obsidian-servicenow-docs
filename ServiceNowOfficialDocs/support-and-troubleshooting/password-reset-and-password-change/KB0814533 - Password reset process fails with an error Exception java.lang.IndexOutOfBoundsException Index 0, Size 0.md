---
title: "Password reset process fails with an error \"Exception: java.lang.IndexOutOfBoundsException: Index: 0, Size: 0\"
aliases:
  - KB0814533
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814533
kb_number: KB0814533
last_modified: 2024-04-08
---

## Password reset process fails with an error "Exception: java.lang.IndexOutOfBoundsException: Index: 0, Size: 0"

  

### Issue

Newly Configured Password Reset Process fails with an error "Exception: java.lang.IndexOutOfBoundsException: Index: 0, Size: 0"

After you configure your new Password reset process try to reset the password for an user

Steps to reproduce :

1.  Open the password reset link  https://<instance-name>.service-now.com/$pwd\_reset.do?sysparm\_url="process Name"
2.  Enter the user name and click on the next 
3.  The user identified successfully and moves to verification phase
4.  Enter the Email address and click on the next 
5.  The password reset fails with a error  

              ![](sys_attachment.do?sys_id=a4e3e049dbc8f0d016d2a345ca9619ed)  ![](sys_attachment.do?sys_id=e4e32449dbc8f0d016d2a345ca961915)

  

          Open the password reset Request from the instance to view the error.

           1. Log into instance : https://<instance-name>.service-now.com

           2. Go to Application navigator and type "Reset requests"

           3. Open the reset request generated to view the error

           ![](sys_attachment.do?sys_id=2ce3e049dbc8f0d016d2a345ca9619ee)

### Release

ALL

### Cause

The Password reset workflow was failing at the work flow - Pwd Get Lock State - Master with an error as below

\[Pwd Get Lock State - Master Work Flow :Step 1: Process input parameters Activity\] --> There are 0 credential stores defined for process "sysid of process". There should only be one.

![](sys_attachment.do?sys_id=9ce3e049dbc8f0d016d2a345ca9619e7)

### Resolution

Map the credential store for the Newly defined process

1\. Log into the instance : https://<instance-name>.service-now.com

2\. Goto https://<instance-name>.service-now.com/pwd\_map\_proc\_to\_cred\_store\_list.do

3\. Map the credential store for the newly defined process 

![](sys_attachment.do?sys_id=68e32449dbc8f0d016d2a345ca961919)
