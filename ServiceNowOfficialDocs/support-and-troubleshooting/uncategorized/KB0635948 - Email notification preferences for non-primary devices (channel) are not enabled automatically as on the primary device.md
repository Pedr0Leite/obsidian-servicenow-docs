---
title: "Email notification preferences for non-primary devices (channel) are not enabled automatically as on the primary device"
aliases:
  - KB0635948
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635948
kb_number: KB0635948
last_modified: 2026-03-04
---

## Email notification preferences for non-primary devices (channel) are not enabled automatically as on the primary device

  

### Issue

When a notification is sent to secondary notification devices like Push, Voice, SMS or additional emails, the secondary devices do not receive the notification if it is not explicitly selected on the user notification preferences.

 ![to add the new channer (device)](sys_attachment.do?sys_id=0cae70a2db0ab450e515c22305961988 "to add the new channer (device)")

### Symptoms

You are facing this issue if:

-   Users are complaining they are not receiving notifications, for example, Push, Voice or SMS messages.
-   Users have more than one device enabled and they receive notifications only on the primary device.
-   Users stop receiving notifications when new notifications are added to the instance on the non-primary devices.

### Release

### Cause

Email Notifications validate recipients against the cmn\_notif\_message table. All matching records for the notification for that user will receive it. If the user does not have a record in the table, records are created on the table only for the primary devices. Without a cmn\_notif\_message record, users will not receive a notification on the device.

<table class="noteTable" style="border: 1px solid #e0e0e0; width: 100%; border-spacing: 5px; background-color: #f5f5f5;"><tbody><tr><td style="text-align: center; padding: 5px;" width="25"><img title="Warning" src="/Warning_25x.pngx" alt="Note icon" align="bottom"></td><td style="text-align: left; padding: 5px;"><strong>Warning</strong>: Secondary devices do not receive notifications automatically. The notifications must be selected manually.</td></tr></tbody></table>

   
The following figure shows that when a notification is sent, only the primary device (channel) is created on the cmn\_notif\_message table.  
  
 ![automatically created](sys_attachment.do?sys_id=8cae70a2db0ab450e515c2230596198d "automatically created")

### Resolution

Keep user primary devices current. Any additional (secondary device) notification needs to be added manually to the user list of active notifications.

Users who create a secondary device (for example, SMS or extra email) need to manually select the notifications that will be received with those devices using the User Notification interface.

-   Starting with Jakarta:
    1.  Click the gear icon and access the Notification section.
    2.  Click the notifications you want to receive.
    3.  Activate the secondary devices by setting the slider to green (on).
-   For versions prior to Jakarta:
    1.  Go to the User profile.
    2.  On the notification preferences, select the notifications you want to receive.
    3.  Activate the secondary devices by setting the slider to green (on).

A new record on cmn\_notif\_message is created with the activated devices (channel).

![secondary device activated](sys_attachment.do?sys_id=ccae70a2db0ab450e515c22305961992 "secondary device activated")
