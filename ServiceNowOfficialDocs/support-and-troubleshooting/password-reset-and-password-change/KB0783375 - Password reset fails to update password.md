---
title: " Password reset fails to update password"
aliases:
  - KB0783375
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783375
kb_number: KB0783375
last_modified: 2026-06-19
---

## Password reset fails to update password

  

### Issue

The password reset fails to update password  
  
**Steps to reproduce:**

1\. Go to [https://<instacnename>.service-now.com](https://\<instacnename\>.service-now.com)   
2\. click forgot password  
3\. enter user name: test1  
4\. enter email:test1@example.com  
  
go to email log and click the password reset link,

Enter the new password and it fails.

Check back password reset->Activity Log to observe the fail

Checked the flow designer (see attachment), it had "Error updating password".

![](sys_attachment.do?sys_id=470fe770dbc07890dc2beeb5ca961939)

### Release

Newyork

### Cause

While clicking on the password reset link from the email, the user was logged in.

If the user is logged in and then clicks the password reset email URL our code check fails and hence it does not let you reset and triggers an error.

### Resolution

While clicking on the password reset link from the email, the user should not be logged in to the instance.

Need to log out of the instance , then click on the password reset link to update the password.
