---
title: "\"Send Email\" flow action in flow designer is not sending notification to Delegates"
aliases:
  - KB0960988
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0960988
kb_number: KB0960988
last_modified: 2025-09-03
---

## "Send Email" flow action in flow designer is not sending notification to Delegates

  

### Issue

When using flow designer and having OOB flow action "Send Email", certain users are receiving email notifications when the action is triggered. But these users have active delegates as well, but they are not receiving notifications.  
Steps to Reproduce  
Configure a flow having "Send Email" action  
Trigger the flow and notice the email is only triggered to this user and not for the  delegate

### Cause

This is an expected behavior with Send email action  
Send Email just sends an email to the recipients you specify.  

### Resolution

Delegation is a feature of the notification system. If you need delegation, you may need to define a system notification, and then use the 'Send Notification" action in the flow.  
Before triggering a notification as an action step in Flow Designer, ensure that the notification is set up for use in the platform.  

### Related Links

Refer : https://community.servicenow.com/community?id=community\_question&sys\_id=45a9ef01dba0d704852c7a9e0f961974  
https://community.servicenow.com/community?id=community\_question&sys\_id=ae2b0be6db020cd85129a851ca961950  
https://docs.servicenow.com/bundle/orlando-servicenow-platform/page/administer/flow-designer/reference/trigger-notification-action-designer.html
