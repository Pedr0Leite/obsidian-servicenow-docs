---
title: "For some users email notifications are not sending an SMS message to the recipient's phone number"
aliases:
  - KB0748029
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748029
kb_number: KB0748029
last_modified: 2026-05-05
---

## For some users email notifications are not sending an SMS message to the recipient's phone number

  

### Issue

 

Resolve missing SMS messages by checking the recipient's phone number, notification preferences, and SMS channel configuration. SMS messages sent from the ServiceNow instance are not received by the recipient, even after following the steps in [KB0712569](https://hi.service-now.com/kb_view.do?sysparm_article=KB0712569 "KB0712569 - How to setup a SMS Email Notification in ServiceNow?").

### Symptoms

After having read and followed the KB article [KB0712569](https://hi.service-now.com/kb_view.do?sysparm_article=KB0712569 "KB0712569 - How to setup a SMS Email Notification in ServiceNow?"), the user is not able to retrieve SMS messages sent from the ServiceNow instance.

You will find there is no record under the sys\_email table is created for the recipient's email \[recipient\_number\]@\[mobile domain\]

### Release

Starting from Jakarta 

### Cause

There are a number of possible reasons as to why the user is not receiving SMS messages from the instance:

-   The user's profile does not have the **associated** **phone numbe**r
-   The users **allow notifications** is not switched on in the notification settings
-   The **SMS channel** is not created within the user's notification settings
-   The user's phone channel is not enabled against the said notification in the notification settings

### Resolution

Make sure the notification fires an SMS message to the recipient's number:

1.  Head over to the \[sys\_user\] table and review the user's record in question to verify if a phone/work number is established
2.  Impersonate the user and verify in their notifications has an existing SMS channel with the phone number
3.  Review the notification setting and search for the notification in question to determine if the SMS channel is enabled against it

<table class="noteTable" align="left"><tbody><tr><td class="c3"><img class="c2" title="Note" src="/Note_25x.pngx" align="bottom" border="border" hspace="" vspace=""></td><td class="c4"><strong>Note</strong>:&nbsp; If you can't impersonate the user, then head over to the [cmn_notif_message] table as it stores all the email preferences for the user.</td></tr></tbody></table>
