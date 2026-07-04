---
title: "Verify that the SMS Sender scheduled job is running"
aliases:
  - KB0541878
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0541878
kb_number: KB0541878
last_modified: 2025-04-08
---

## Issue

Verify that the SMS Sender scheduled job is running

  
  
  
Overview

* * *

If an SMS message is listed in the **Outbox** for an unusual amount of time (the exact amount of time varies by instance and configuration), there may be an issue with the Short Message Service (**SMS) Sender** scheduled job. The **SMS Sender** scheduled job determines when a duplicate notification is going to be sent. Once an _action_ or _business rule_ is triggered, SMS messages are placed in the Outbox. All messages remain in a **State** of **Ready** until the **events process** job handles the request.

## Resolution

Procedure

* * *

To check if the SMS message is stuck in the Outbox:

1.  Navigate to **System Mailboxes > Outbound > Outbox**.
2.  Add the following filter condition: **\[Notification type\] \[is\] \[SMS\]**

The Outbox should be empty or contain messages less than a few minutes old.

![](/sms_outbox.jpgx)

Click **Emails \[Outbox view\]** and choose **Refresh List**.

If the same messages are listed in the Outbox, verify that the **SMS Sender** job is running.

To verify that the **SMS Sender** scheduled job is running:

1.  Navigate to **System Scheduler > Today's Scheduled Jobs**.
2.  In the **Go to** field, select **Name** and search for **\*SMS Sender**.
3.  Open the **SMS Sender** record.
4.  Check the **Next action** field. When notifications function properly, the value of this field, which indicates the next time the job runs, is not more than a few minutes from the time you opened the record. If it is more than a few minutes, look at the **State**.
5.  To check the **State** field:
    1.  **Error** or **Queued**: Change the state to **Ready** and click **Update**.
    2.  **Ready** or **Running**: If the value of the **Next action** field is more than a few minutes from the time you opened the record, open an incident ticket and include the **Next action** value.
6.  Right-click the form header and choose **Reload form**.  
      
    The **Next action** field value should update. If the value is unchanged, open an incident ticket and include the value.
