---
title: "How to enable and use rollback functionality for Fix Scripts"
aliases:
  - KB0761248
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0761248
kb_number: KB0761248
last_modified: 2026-05-03
---

## How to enable and use rollback functionality for Fix Scripts

  

### Summary

A fix script is server-side JavaScript code that you run after an application is installed or upgraded.

Include fix scripts to make changes that are necessary for the data integrity or product stability of an application.

Administrators and users with the script\_fix\_admin role can create and run fix scripts.

As of London Release there has been a new option to record a fix script for rollback. To use this option you just need to add the field to the form and you should be able to record your fix scripts using the rollback functionality so that if any issues occur after the fix script you can rollback easily.

### Release

London and above

### Instructions

When you open up the fix script form by default the record for rollback option is not there. 

System Definition > Fix Scripts

To add this

1) Right click the top menu and select Configure > Form Layout

![](sys_attachment.do?sys_id=88e3e116db2e20104fee66f748961906)

2) Find the Record for rollback field in the Available slush bucket and move it to the selected slushbucket by clicking the > button 

3) Move the field to wherever you want to have the field on your form.

4) Now you will have the field on the form and if you check this box then run the fix script a rollback context will be created for you to rollback the fix script.

Example:

1) I create a test script:

![](sys_attachment.do?sys_id=cce3e116db2e20104fee66f748961907)

2) I then ran this with rollback ticked

3) After the script was completed I checked the sys\_rollback\_context table and found the fix script job had run:

![](sys_attachment.do?sys_id=04e3e116db2e20104fee66f748961909)

4) You can see we have a rollback button so if you encounter an issue after the fix script you will be able to click the rollback button and rollback the changes made because of this script.

### Related Links

Documentation about rollback:

[https://docs.servicenow.com/csh?topicname=rollback-delete-recovery.html&version=latest](https://docs.servicenow.com/csh?topicname=rollback-delete-recovery.html&version=latest)
