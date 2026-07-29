---
title: "No survey instances or notifications are created for the new added audience into an existing Emergency Outreach record"
aliases:
  - KB0858347
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0858347
kb_number: KB0858347
last_modified: 2024-04-08
---

## No survey instances or notifications are created for the new added audience into an existing Emergency Outreach record

  

### Issue

When updating the audience for an existing Emergency Outreach record and clicking on the 'Resend Notification' button, no survey instances or notifications are created for the new added audience.

### Cause

Working as designed.

### Resolution

The survey instances and notifications are created and sent to the selected audience once you hit the 'Send Notification' button.

After that the new button 'Resend Notification' will be displayed instead of the 'Send Notification' button.

From our documentation we have:

**Send Notification:**  
The notification and survey link are sent to the target audience. A survey instance is created for each recipient, with the status Ready to take.  
When you send the outreach survey notification, any open survey instances for the recipients are canceled.   
When you resend a notification for an outreach, the open survey instances are not canceled.

**Resend Notification:**  
As employees complete the survey, the status updates in their survey instance.  
If employees haven't responded yet, click Resend Notification. The notification is sent again only to employees who have not yet responded.

As we can see from above, the 'Resend Notification' will only send a new notification to the employees that haven't yet responded to the survey.

This behaviour can be reproduce into an OOB instance.

If you need to change the survey audience then you can create a new outreach for that new audience.

By doing that and selecting the 'Send Notification' button, it will create the survey instances and send a notification to the selected users.

### Related Links

[Send a readiness survey and view responses](https://docs.servicenow.com/csh?topicname=send-eo-outreach-survey.html&version=latest "Send a readiness survey and view responses")
