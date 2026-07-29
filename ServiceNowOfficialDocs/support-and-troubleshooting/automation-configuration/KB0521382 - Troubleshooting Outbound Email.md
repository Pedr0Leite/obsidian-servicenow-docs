---
title: "Troubleshooting Outbound Email"
aliases:
  - KB0521382
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0521382
kb_number: KB0521382
last_modified: 2026-02-23
---

## Troubleshooting Outbound Email

  

### Issue

ServiceNow instances can automatically notify selected users via email of specific activities in the system, such as updates to incidents or change requests. By default, all **outbound email notifications** are sent from the **default email address** of the instance. For organizations that need to send emails from specific email addresses, such as from multiple service desks, or want to send notifications in different languages, the platform supports the configuration of multiple outbound addresses and separate email addresses for responses. For more information, see [Email and SMS Notifications](https://docs.servicenow.com/csh?topicname=c_EmailNotifications.html&version=latest "Email and SMS Notifications") in the ServiceNow product documentation.  
  

### Notes and precautions

-   When reprocessing an outbound email for testing purposes, **double-check the recipients (to, cc, bcc)** to validate they will go to the intended targets.
-   Only customers may send emails to **personal email addresses** for testing purposes if they wish, not SN personnel.
-   **Customer consent** is needed if troubleshooting requires exporting a test record from a customer instance into a test instance.
-   Update **Email properties --> "Send all email to this test email address (non-production testing)" to a temp address** rather than disabling email sending. This will ensure emails do not remain in send-ready state preventing them from being sent out in the future if Email sending is enabled on the instance.  
      
    

When an instance does not send emails, it is important to identify the root cause. This section describes the outbound email process and provides troubleshooting solutions for common issues.

![](/sys_attachment.do?sys_id=01db3b949782261468d477121153af26)

<table class="noteTable" style="border: 1px solid #e0e0e0; width: 100%; border-spacing: 5px; background-color: #f5f5f5;"><tbody><tr><td style="text-align: center; padding: 5px;" width="25"><img title="Note" src="/Note_25x.pngx" alt="Note icon" align="bottom"></td><td style="text-align: left; padding: 5px;"><strong>Note</strong>: The troubleshooting steps on this page pertain to <em>sub-production instances only</em>. If you experience email notification issues on a production instance, submit an incident.</td></tr></tbody></table>

1.  Email notifications must be configured properly. To verify that the email notification system properties are configured properly, see [Email and SMS notifications](https://docs.servicenow.com/csh?topicname=c_EmailNotifications.html&version=latest "Email and SMS notifications"). If your instance sends messages from an SMTP server your company maintains (rather than a ServiceNow SMTP server), verify your instance connects to the proper SMTP server. For instructions, refer to [Verifying the instance has the proper custom SMTP server settings](/kb_view.do?sysparm_article=KB0524531 "Verifying the instance has the proper custom SMTP server settings")
2.  An action, such as **adding a comment** to an incident or **closing a problem**, triggers the addition of an event to the event log. If there is no email record listed in the Outbox or Sent mailbox, see [Verifying if email event is created in the Outbox](/kb_view.do?sysparm_article=KB0523579 "Verifying if email event is created in the Outbox").
3.  The **events process** job processes the events.  
    -   If email is held in the Outbox for a long period of time, see [Verifying the SMTP Sender schedule job is running](/kb_view.do?sysparm_article=KB0523599 "Verifying the SMTP Sender schedule job is running") or, for SMS notifications, [Verifying the SMS Sender scheduled job is running](/kb_view.do?sysparm_article=KB0541878 "Verifying the SMS Sender scheduled job is running").
4.  If a particular action no longer produces a notification, review the notification record's conditions to determine if they are valid. For additional information, see [Verifying the notification's record conditions have been met](/kb_view.do?sysparm_article=KB0528655 "Verifying the notification's record conditions have been met").
5.  The **SMTP Sender** and **SMS Sender** jobs transmit all processed requests to the mail server. The mail server sends the email message to the user. For information on troubleshooting outbound emails, refer to [Outbound Email Troubleshooting](/kb_view.do?sysparm_article=KB0521382 "Outbound Email Troubleshooting").
6.  The email client receives the message. If the email is not received, see [Obtaining the Message ID to troubleshoot the mail server](/kb_view.do?sysparm_article=KB0523600 "Obtaining the Message ID to troubleshoot the mail server").

###   
Common outbound email issues

The following are common outbound email issues, their symptoms, and solutions.

| **Common Outbound Email Issue** | **Symptom** | **Solution** |
| --- | --- | --- |
| Inactive user is locked out (Berlin or later releases). | A specific user stops receiving notifications. | [Verify the user is not locked out because they are inactive.](/kb_view.do?sysparm_article=KB0528661 "Verify the user is not locked out because they are inactive.") |
| User is locked out (Berlin or later releases). | A specific user stops receiving notifications. | [Verify the user is not locked out.](/kb_view.do?sysparm_article=KB0528699 "Verify the user is not locked out.") |
| User disabled notifications. | A specific user stops receiving notifications. | [Verify the user's notification preferences.](/kb_view.do?sysparm_article=KB0528667 "Verify the user's notification preferences.") |
| User preferences do not list active email device. | A specific user does not receive notifications or the instance fails to send a notification. | [Verify the user has an active email device in their notification preferences.](/kb_view.do?sysparm_article=KB0528667 "Verify the user has an active email device in their notification preferences.") |
| Intended recipient does not have an email address. | A specific user does not receive notifications or the instance fails to send a notification. | [Verify the intended recipient has an email address.](/kb_view.do?sysparm_article=KB0528669 "Verify the intended recipient has an email address.") |
| Intended recipient has improperly-formatted email address. | A specific user does not receive notifications or the instance fails to send a notification. | [Verify the email address is formatted properly.](/kb_view.do?sysparm_article=KB0528671 "Verify the email address is formatted properly.") |
| Option to notify event creator disabled. | A user receives some but not all notifications. | [Verify notification set to notify the event creator.](/kb_view.do?sysparm_article=KB0528673 "Verify notification set to notify the event creator.") |
| Intended recipient has an active delegate. | The instance sends a notification to an unexpected user. | [Verify the user who received the email is not a delegate of another user.](/kb_view.do?sysparm_article=KB0528677 "Verify the user who received the email is not a delegate of another user.") |
| Notification variable values change after the events process job creates notifications. | The events process job creates multiple notifications that all have the same notification variable values. | [Verify that the notification matches your business needs.](/kb_view.do?sysparm_article=KB0528679 "Verify that the notification matches your business needs.") |
| Attachments exceed maximum number or file size. (Not applicable to SMS notifications.) | Outgoing mail does not contain expected attachments. Can send some attachments, but not all. | [Verify the attachments do not exceed configured maximums.](/kb_view.do?sysparm_article=KB0528681 "Verify the attachment does not exceed 25MB.") |
| The instance is not enabled to send email. | The instance does not send any notifications at all. | [Verify the instance is enabled to send email.](/kb_view.do?sysparm_article=KB0524529 "Verify the instance is enabled to send email.") |
| Instance does not have proper settings for custom SMTP server. | When using a custom SMTP server, no messages appear in the **Outbox** or **Sent** mailboxes. | [Verify the instance has the proper custom SMTP server settings.](/kb_view.do?sysparm_article=KB0524531 "Verify the instance has the proper custom SMTP server settings.") |
| The notification's required conditions are not met (Berlin or later releases). | The instance does not send notifications for a particular type of record or action. | [Verify the notification record's conditions met.](/kb_view.do?sysparm_article=KB0528655 "Verify the notification record's conditions met.") |
| The SMTP sender scheduled job is in an error state. | The instance stops sending email notifications but there are messages in the Outbox. | 
[Verify the SMTP Sender scheduled job is running.](/kb_view.do?sysparm_article=KB0523599 "Verify the SMTP Sender scheduled job is running.")

 |
| The SMS sender scheduled job is in an error state. | The instance stops sending SMS notifications but there are messages in the Outbox. | 

[Verify the SMS Sender scheduled job is running.](/kb_view.do?sysparm_article=KB0541878 "Verify the SMS Sender scheduled job is running.")

 |
| The notification's required event is not being triggered (Aspen or earlier releases).  | The instance does not send notifications for a particular type of record or action. | [Verify the triggering action generated the notification event.](/kb_view.do?sysparm_article=KB0528653 "Verify the triggering action generated the notification event.") |
| There is a routing problem on the outbound mail server. | The instance sends the mail, but the recipient never receives it. | [Verify the outbound mail server received the email.](/kb_view.do?sysparm_article=KB0528658 "Verify the outbound mail server received the email.") |
| There are stuck events or email sending delays | Notifications are not being sent out or text indexing isn't happening after a clone. | [Event queue not processing due to incorrect state of schedulers](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778217 "Event queue not processing due to incorrect state of schedulers") |
| Excluded recipients because user has no usable devices for a subscribed user | A specific user is excluded from notification even after user is subscribed to it | [Verify the Users "send to" device in sys\_notif\_subscription](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786114) |
| 

Email is sent to different users when recipients are added using event.parm1 or event.parm2 or email target record

 | 

The email record target and Event record instance are not the same.

 | 

[Verify the associated Email scripts are not updating the event record.](https://support.servicenow.com/kb?id=kb_article_view&sys_kb_id=10989ce81bb46910cd3b33bc1d4bcb8c "https://support.servicenow.com/kb?id=kb_article_view&sys_kb_id=10989ce81bb46910cd3b33bc1d4bcb8c")

 |

### Video tutorial

If you are having issues using the outbound email functionality in ServiceNow, the following video tutorial can guide you, step-by-step, to a solution and provide common troubleshooting methods. This tutorial covers common issues, their causes, and the required steps to resolve them. They range from basic to more advanced topics, and are best watched in the order that they are listed.

You can view an overview to outbound email troubleshooting or click any one of the following links to jump to a different section of the series. These steps can usually be applied to other email issues, since they often have common root causes.

### Troubleshooting Template

\-----------------------------------------------------------------------------------------------------------

INFORMATION TO ASK FOR OUTBOUND EMAIL ISSUE:

\-----------------------------------------------------------------------------------------------------------

1\. Please confirm which instances are impacted. Is this live and does this affect both production and subproduction?

2\. When did the issue begin (please specify the time zone)?

3\. Have you verified the  Email Diagnostics page to ensure  that all parameters are green under Email Sending?

4\. Have you confirmed that "SMTPSender" job is running smoothly?

5\. What is the scope and what outbound notifications are affected? If possible, provide a link or query that lists the impacted notifications.

6\. Have we confirmed that ServiceNow emails are not being filtered or marked as spam in users' mailboxes??

7\. Have you tested sending emails from email client manually from the ServiceNow to verify the issue? If so, what were the results?

8\. Have you reviewed the email headers of the impacted emails for clues about delays, bounces, or rejections in sys\_email table?

9\. What specific error messages or logs are being generated in sys\_email and sys\_email\_logs tables, if any? Can you share the exact details or screenshots?

10\. Have there been any recent changes to the email configuration, such as SMTP settings email templates, or notification rules?

11\. Are all recipients affected, or is the issue limited to specific email addresses or domains?

12\. If you are using your own SMTP Email Account, can you confirm if the email delivery service (e.g.SMTP server) is operational and not experiencing outages?

13\. Are there any specific patterns or trends, such as only certain types of notifications or specific times when the issue occurs?

### Release

.

### Resolution

.
