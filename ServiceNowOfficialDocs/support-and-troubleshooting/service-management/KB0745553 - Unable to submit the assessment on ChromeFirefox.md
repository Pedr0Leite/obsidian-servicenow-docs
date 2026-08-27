---
title: "Unable to submit the assessment on Chrome/Firefox"
aliases:
  - KB0745553
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745553
kb_number: KB0745553
last_modified: 2024-04-07
---

## Unable to submit the assessment on Chrome/Firefox

  

### Issue

Unable to submit the assessment on Chrome/Firefox. Seeing the below alert when trying to submit the survey:

![](sys_attachment.do?sys_id=4e5a3dfcdb4cb0d0471f9c41ba961982)

### Release

All releases.

### Cause

The system property 'glide.ui.dirty\_form\_support' is set to 'true'.

### Resolution

Set the system property 'glide.ui.dirty\_form\_support' to 'false', clear the instance cache and re-login.

### Related Links

More information on this property can be found on our product documentation:

[Cancel changes to a form](https://docs.servicenow.com/csh?topicname=t_EditingInForms.html&version=latest#t_CancelAChange "Cancel changes to a form")
