---
title: "Push Notifications not visible on Android nor Iphone on ServiceNow Agent Mobile App"
aliases:
  - KB0747510
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0747510
kb_number: KB0747510
last_modified: 2026-04-02
---

## Push Notifications not visible on Android nor Iphone on ServiceNow Agent Mobile App

  

### Issue

# Symptoms

* * *

-   A user sends a message to another user via connect chat 
-   The recipient of the message was using ServiceNow Classic Mobile app 
-   The recipient started using ServiceNow Agent MobileApp instead of Classic
-   Push notifications from connect Chat to Classic App work fine
-   Push notifications from connect Chat to Agent App is not visible in the Mobile app on Iphone or Android

# Release

* * *

Madrid

# Cause

* * *

The mobile app for Madrid has to be configured

Previous versions of the application are now named Classic

Push Application ServiceNow Classic Mobile Application corresponds to classic App and ServiceNow Mobile Application corresponds to ServiceNow Agent App

# Resolution

* * *

1) Install the required plugins for Mobile Agent as per documentation

2)Make sure ChatRecv notification is set to true in the Push Notification menu

![](sys_attachment.do?sys_id=486ce46edb42b450e515c223059619e3)

3) If the user is authorized to receive the push notification, it will be seen in the homescreen of the mobile phone:

![](sys_attachment.do?sys_id=c86ce46edb42b450e515c223059619e8)

<table class="noteTable" align="left"><tbody><tr><td class="c3" style="width: 26.4px;"><img class="c2" title="Note" src="/Note_25x.pngx" align="bottom" border="border" hspace="" vspace=""></td><td class="c4" style="width: 424.8px;"><strong>Note</strong>: The mobile user has to authorize the push notification for ServiceNow Agent app, otherwise the push notification will be ignored.</td></tr></tbody></table>
