---
title: "How to disable response options in change request calendar invitations"
aliases:
  - KB0596327
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0596327
kb_number: KB0596327
last_modified: 2025-10-28
---

## How to disable response options in change request calendar invitations

  

### Issue

Depending on business requirements, admins may want to disable response options in calendar invitations. The ServiceNow Change Request application can send pending changes to a Microsoft Outlook Calendar automatically via email. This article explains how to modify the template to remove response options. 

By default, the Notify Change Calendar email notification sends calendar invitations when a change is created. The template change.calendar.integration is used to compose the email contents.

### Release

All supported releases

### Resolution

To turn this feature off:

1.  Go to **System Notification** > **Emails** \> **Templates**.
2.  Open the change.calendar.integration email template.
3.  Change the value for RSVP to FALSE by modifying this line:  
      
    ATTENDEE;ROLE=REQ-PARTICIPANT;RSVP=TRUE:MAILTO:${to}  
    to:  
    ATTENDEE;ROLE=REQ-PARTICIPANT;RSVP=FALSE:MAILTO:${to}
4.  Select **Update**.

After making these changes, recipients no longer see the response option in their email invitations.

**Note:** These changes only disable the **Email organizer** option and do not remove all RSVP controls for recipients.
