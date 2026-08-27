---
title: "How to add the ability to add attachments to the defect form when opened through the Report Defect link from the test case record"
aliases:
  - KB0692109
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0692109
kb_number: KB0692109
last_modified: 2024-04-07
---

## How to add the ability to add attachments to the defect form when opened through the Report Defect link from the test case record

  

### Issue

  
  

# Description

* * *

By default OOB there's no way to add attachments to a new defect (rm\_defect) form if it's opened from the test case (tm\_test\_case\_instance) via the "Report Defect" link since the header bar (where the attachment icon is located) is not visible.

![](sys_attachment.do?sys_id=e11b682adb42b450e515c22305961997)

This article details that steps that can be taken to workaround this behavior to allow users to still be able to add attachments to the new defect form.

# Procedure

* * *

1) Create a new UI Action:

  
Name: Add Attachment  
Table: Defect \[rm\_defect\]  
Action name: add\_attachment  
Show insert: checked  
Show update: checked  
Client: checked  
Form link: checked  
Onclick: myFunction()  
Script:  
function myFunction()  
{  
saveAttachment(g\_form.getTableName(), g\_form.getUniqueValue());  
}  
  
Once this UI Action is created there would now be a related link on the rm\_defect form that users can click to add attachment to the record.

2) Add the "Attachments" related list to the form as an embedded list (this can be done by going to rm\_defect form > Configure > Form Layout > Add "Attachments" related list to the form).

Please note that the rm\_defect form that is opened through the test case form is using the 'Scrum' view so one would need to add the "Attachments" element to that view.  
This extra step is needed so users would know/see what attachment(s) they have added (attachments would normally show on the header of the form but since that's not available this would be the workaround for it).

![](sys_attachment.do?sys_id=651b682adb42b450e515c2230596199c)

# Applicable Versions

* * *

All versions that use Test Management application

# Additional Information

* * *

[Creating UI Actions](https://docs.servicenow.com/csh?topicname=t_EditingAUIAction.html&version=latest#t_EditingAUIAction "Creating UI Actions")

[Test Management documentation](https://docs.servicenow.com/csh?topicname=c_TestManagement.html&version=latest "Test Management documentation")
