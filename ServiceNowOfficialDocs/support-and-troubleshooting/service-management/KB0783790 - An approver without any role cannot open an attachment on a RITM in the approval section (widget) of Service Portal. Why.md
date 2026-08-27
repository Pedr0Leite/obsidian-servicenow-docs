---
title: "An approver without any role cannot open an attachment on a RITM in the approval section (widget) of Service Portal. Why?"
aliases:
  - KB0783790
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783790
kb_number: KB0783790
last_modified: 2024-04-08
---

## An approver without any role cannot open an attachment on a RITM in the approval section (widget) of Service Portal. Why?

  

### Issue

The user is concerned that an approver without any roles, "Tony Stark", cannot open an attachment on RITM0010000 in the Service Portal approval module (/sp?id=approval&table=sysapproval\_approver&sys\_id=633e03b9db00c01091a5ea42ca96192e). They wanted to know why this is.

### Resolution

The reason the user "Tony Stark" is not able to view the sys\_attachment is that he is failing ACLs.

Here is an explanation of what is happening for Tony: attachments have a parent field. In this case, RITM0010000 is the parent record.  
  
Tony does not have access to the parent (RITM0010000), therefore he cannot access the attachment. This is a Platform behavior/rule.  
  
If the user wants Tony to have access, they need to configure their ACLs to allow public access (that is, to allow users like Tony with no roles to access).
