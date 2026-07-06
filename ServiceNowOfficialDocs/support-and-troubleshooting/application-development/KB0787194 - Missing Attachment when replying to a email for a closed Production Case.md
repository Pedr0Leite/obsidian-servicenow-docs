---
title: "Missing Attachment when replying to a email for a closed Production Case"
aliases:
  - KB0787194
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787194
kb_number: KB0787194
last_modified: 2024-04-08
---

## Issue

An employee tried to re-open a case, however due to custom scripts in the inbound action, a new case was created and the attachment from the email was not attached to the new case. 

## Resolution

As a solution for your custom inbound action you can force attachment copies by inserting the code to copy the attachment in your script using  
GlideSysAttachment.copy('sourcetable','sys\_id','destinationtable','sys\_id')  
(example shown in below link:  
https://docs.servicenow.com/csh?topicname=r\_UsefulAttachmentScripts.html&version=latest)  
  
As an example the following code will copy the attachment from the email source to the HR ticket:  
  
gr.update();  
GlideSysAttachment.copy('sys\_email',sys\_email.sys\_id,'hr',current.sys\_id);  
....  
and  
....  
var newSysID= gr.insert();  
GlideSysAttachment.copy('sys\_email',sys\_email.sys\_id,'hr',newSysID);
