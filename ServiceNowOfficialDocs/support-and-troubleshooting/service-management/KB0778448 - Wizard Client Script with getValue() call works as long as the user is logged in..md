---
title: "Wizard Client Script with \"getValue()\" call works as long as the user is logged in."
aliases:
  - KB0778448
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778448
kb_number: KB0778448
last_modified: 2024-04-08
---

## Wizard Client Script with "getValue()" call works as long as the user is logged in.

  

### Issue

"getValue()" call in Wizard client script does not work if users unauthenticated. That is when they try to access survey as public page,without logging in,  g\_form.getValue() is returned blank.

You might see some errors in the console as soon as you select any value on the form . For example as in the screenshot:

![](sys_attachment.do?sys_id=97a7a7b4db4c34d0471f9c41ba96192f)

### Release

All releases.

### Cause

Variables of the survey wizard are not public. Even if the survey wizard is public, and the variables are not public then issue occurs.

### Resolution

1.  Manually add public to write role and read role for the wizard variables.
2.  If you do not see the columns for read and write role, then personalize form and then make changes. Please refer to the screenshot attached:![](sys_attachment.do?sys_id=1fa7a7b4db4c34d0471f9c41ba961930)
