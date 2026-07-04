---
title: "Subscribable notifications with affected and event field empty will trigger for all subscribed users"
aliases:
  - KB0635959
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635959
kb_number: KB0635959
last_modified: 2025-04-07
---

## Subscribable notifications with affected and event field empty will trigger for all subscribed users

  

### Issue

Subscribable notifications with affected and event field empty will trigger for all subscribed users

  
  

# Problem

* * *

Attempts to subscribe to a notification and receive it without having to subscribe to a CMDB Configuration Item (CI) are unsuccessful. Everyone subscribed to the notification will receive it every time it triggers. In some cases, it will stop working.

# Symptoms

* * *

You could experience the need to validate your subscribable notifications if:

-   You have upgraded to the latest product version.
-   You are no longer using the legacy subscribable engine.
-   Users stop receiving the notifications they are subscribed to.

# Cause

* * *

After an upgrade, several forms related to subscription will be modified or updated.

# Resolution

* * *

To receive a subscribable notification without having to relate a CI:

1.  Go to sys\_properties\_list.do and set the _**glide.notification.use\_legacy\_subscription**_ system property value to false.
    
2.  Navigate to **System Notification > Email > Notifications** and open the notification.
    
3.  Select the **Subscribable** checkbox.
    
4.  Leave the **Affected** field on the event field empty.
    
5.  Leave the **Item table** field empty.
    
6.  Click **Update**.
    
7.  On the user preferences, subscribe to the notification and it will not ask you to add a Configuration Item (CI).
    
    ![Subscribable notifications with affected and event field empty will trigger for all subscribed users for the notification](sys_attachment.do?sys_id=ac4960eedb02b450e515c223059619b6 "Subscribable notifications with affected and event field empty will trigger for all subscribed users for the notification")
    

<table class="noteTable" align="left"><tbody><tr><td class="c3"><img class="c2" title="Note" src="/Note_25x.pngx" align="bottom" border="border" hspace="" vspace=""></td><td class="c4"><strong>Note</strong>: Every time the notification triggers, all the subscribed users will receive the notification as well</td></tr></tbody></table>

![When adding a subscribable notification, it will not ask for a CI](sys_attachment.do?sys_id=b449e0eedb02b450e515c22305961971 "When adding a subscribable notification, it will not ask for a CI")
