---
title: "Publication Email getting send-ignored using Targeted Communication"
aliases:
  - KB0861745
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0861745
kb_number: KB0861745
last_modified: 2026-06-24
---

## Publication Email getting send-ignored using Targeted Communication

  

### Issue

You have created a publication, and whenever you publish the publication, the email is not sent.

The Email log gives an error "SMTPSender: no recipients, email send ignored"

### Release

N/A

### Cause

A custom email template "Publication Push" was being used. In the custom email template which you are using for the Publication, you are missing an all-important OOB email script "${mail\_script:add\_users\_to\_bcc\_list}".

Basically when you publish a communication as per the flow, the process should create an event "sn\_publications.createEmail", this is happening normally as we can see the email is created.  
  
The recipient list should be built via the script action \[add\_users\_to\_bcc\_list\] https://INSTANCENAME.service-now.com/nav\_to.do?uri=sys\_script\_email.do?sys\_id=81b6d890c341220071d07bfaa2d3aee2 and all the recipients in the list should be added to the notification, however this is not happening leaving causing the platform to ignore the email.  
  
  
If you look at the OOB email template i.e. "Publication Default", we have added the OOB email script "${mail\_script:add\_users\_to\_bcc\_list}" to make sure of adding all the recipient's from the recipients related list(m2m table) in the publication record to the blind\_copy field in an email.  
  
Since this script is missing in the customized email template "Publication Push" thus it is not adding anyone to the blind\_copy field in the email and ignoring the email to be sent.

  
See below screenshot showing the expected code as designed in OOB notification.

![](sys_attachment.do?sys_id=076831eb47e1c3103542f24c736d4374)

### Resolution

To resolve this issue please update your custom Notification and add the missing line of relevant code "${mail\_script:add\_users\_to\_bcc\_list}"
