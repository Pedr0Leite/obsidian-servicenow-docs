---
title: "Changing 'From' email address in Notifications"
aliases:
  - KB0778346
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778346
kb_number: KB0778346
last_modified: 2025-07-16
---

## Issue

Email notifications are generally sent out of ServiceNow instances with the email user label and username configured in the instance Email Account. When the email message goes out to the recipients, they can see it as the example below:

![Department and Email ID](sys_attachment.do?sys_id=0f71eed593b26e90c2513f986cba1058 "Department and Email ID")

However, most instance administrators want to have this From address different for different notifications.

## Resolution

This can be achieved using the 'What it will contain' tab -> 'From' field  of the email notification:

<table id="t_CreateANotification__table_g21_dvb_kr"><tbody><tr><td headers="t_CreateANotification__table_g21_dvb_kr__entry__1 ">From</td><td headers="t_CreateANotification__table_g21_dvb_kr__entry__2 "><p>Enter the email address that you want the email notification to use in the From field. For example, helpdesk@yourcompany.com. The email must be in a valid format, otherwise a notification message appears near the field.</p><p>Changing this address requires an advanced email setup such as&nbsp;<a title="Enable using your own SMTP server so that you can leverage the existing filtering, retention, or compliance aspects of your own SMTP server while also using the ServiceNow POP3 server." href="https://docs.servicenow.com/csh?topicname=t_ConfAltEmailUsgOwnSMTP.html&amp;version=latest" target="_blank" rel="noopener noreferrer">enabling email forwarding</a>.</p></td></tr></tbody></table>

  
When just adding an email address (e.g.: xyz@example.com) to the 'From' field and configuring the notification, the recipients can see it as below:

![Department and Email ID](sys_attachment.do?sys_id=9f71eed593b26e90c2513f986cba105b "Department and Email ID")  
When the Label is also required to be changed, this can be done in two ways:

1) In the notification, you can use the below format in the from field  
TEST NAME <ab@mail.com>   
  
2) If you want to use mail script, use the format below.  
email.setFrom("TEST NAME <ab@mail.com>"); 

  
The recipients can then see the email as below :

![Just the Name and email ID](sys_attachment.do?sys_id=1f71eed593b26e90c2513f986cba1083 "Just the Name and email ID")

## Additional Information

[https://www.servicenow.com/docs/csh?topicname=t\_CreateANotification.html&version=latest](https://www.servicenow.com/docs/csh?topicname=t_CreateANotification.html&version=latest)
