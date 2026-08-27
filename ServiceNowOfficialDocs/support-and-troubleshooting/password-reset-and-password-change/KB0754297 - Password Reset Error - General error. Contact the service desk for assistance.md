---
title: "Password Reset Error - General error. Contact the service desk for assistance"
aliases:
  - KB0754297
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0754297
kb_number: KB0754297
last_modified: 2024-04-07
---

## Password Reset Error - General error. Contact the service desk for assistance

  

### Issue

# Symptoms

After a user attempts to reset their password they encounter the following error

**Password Reset Error - General error. Contact the service desk for assistance**

**![](sys_attachment.do?sys_id=a3be78a2db0ab450e515c22305961939)**

# Cause

The Password Reset Process that you are using might not have a Credential Store associated with it.

![](sys_attachment.do?sys_id=e3be78a2db0ab450e515c2230596193e)

# Resolution

Add an appropriate Credential Store to the Password Reset Process and save it.

![](sys_attachment.do?sys_id=e3be78a2db0ab450e515c22305961943)
