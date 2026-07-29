---
title: "Troubleshooting email notification failures in ServiceNow"
aliases:
  - KB0538135
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538135
kb_number: KB0538135
last_modified: 2026-05-26
---

## Troubleshooting email notification failures in ServiceNow

  

### Issue

Troubleshoot email notification failures in ServiceNow by verifying common configuration settings and eliminating potential causes.  This article provides a diagnostic checklist that identifies common causes and links to detailed articles for each verification step.

### Symptoms

Symptoms may include the following:

-   Notification is not sent or does not trigger
-   Notification event does not fire
-   Email message is not sent or is stuck in the Outbox
-   Users do not receive a notification
-   Users not getting an email
-   Caller or other specified recipient does not receive a notification
-   Users receive duplicate notifications
-   Users receive notifications they should not receive
-   Notifications do not reach all members of a group
-   Notification content is incorrect
-   Notification condition fails
-   Failed status due to invalid addresses
-   Approval notification is not sent

### Release

All supported releases  

### Resolution

Use the following checklist to identify the cause of email notification failures in your environment. Select the reference article for detailed verification steps and corrective actions.

| Take this action | Reference article |
| --- | --- |
| Verify that there are no high-level issues with outbound email | [Outbound email troubleshooting](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0521382) |
| Review common email notification errors and their solutions | [Troubleshooting email notifications](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535129) |
| Check notification record conditions | [How to verify notification record conditions have been met](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0528655) |
| Verify the formatting of the recipient email address | [Verifying the recipient email address is properly formatted](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0528671) |
| Verify that another condition does not have a higher weight | [Create an email notification](https://www.servicenow.com/docs/r/platform-administration/t_CreateANotification.html) |
| Validate the instance is enabled to send email | [Verifying your instance is enabled to send email](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0524529) |
| Confirm email is not set to go to the debug user | [Outbound mail configuration](https://www.servicenow.com/docs/r/platform-administration/r_OutboundMailConfiguration.html) |
| Verify email event was created in the Event Log | [Verifying that an email event is created in the Event Log](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0523579) |
| Verify that the events process job is running | [Verifying that the events process job is running](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0523578) |
| Verify the notification event was generated | [Verifying that the notification event was generated](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1640734) |
| Check that events and notifications are set up correctly | [Email FAQs and troubleshooting notification emails](https://www.servicenow.com/docs/r/platform-administration/troubleshooting-notification-emails.html) |
| Verify the events process scheduled job is running | [How to identify a delay in an event processing job](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0758422) |
| Confirm the user has not disabled notifications and a notification device is configured | [Verifying a user's notification preferences](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0528667) |
| Enable subscribable notifications  | [Subscription-based notifications are not working](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0831284) |
| Verify email notification is based on the correct table | [Email notifications](https://docs.servicenow.com/csh?topicname=c_EmailNotifications.html&version=latest) |
