---
title: "Instance User Password Reset Error"
aliases:
  - KB0781873
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781873
kb_number: KB0781873
last_modified: 2025-04-08
---

## Instance User Password Reset Error

  

### Issue

When an instance admin (System Administrator) tries the 'Reset Password' option under the related links in the user record, an error appears: 'No service-desk processes found for the user selected.' 

![Error message, No service desk processes found for the user selected](sys_attachment.do?sys_id=74d1588a47f71290b6d8aa25126d43f8)

### Resolution

Please follow the steps below:

1.  Log in to the instance as an admin.
2.  Navigate to Password Reset > Process.
3.  Activate the 'Service-Desk Password Reset for Local ServiceNow' Password Reset Process.
4.  Check the 'Apply To All Users' checkbox to true. This will allow you to reset the password for a specific user.

Please refer to the screenshot below for reference.

       ![Active and apply to all users is checked](sys_attachment.do?sys_id=70d1988a47f71290b6d8aa25126d43a9)
