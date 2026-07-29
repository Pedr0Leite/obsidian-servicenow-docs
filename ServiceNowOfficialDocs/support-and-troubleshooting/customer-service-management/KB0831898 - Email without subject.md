---
title: "Email without subject"
aliases:
  - KB0831898
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0831898
kb_number: KB0831898
last_modified: 2023-07-12
---

## Issue

If the customer receives an email without a subject from a sub prod environment. Kindly follow the below steps to identify the cause:

1.  Get the message-id of the email.
2.  Search the sys\_email table with the message\_id.
3.  If the email is found, then check the Notification type of the email. If it is "SMS" then the property "Send all email to this test email address" in email properties.
4.  If it is set to a testing email address, then it is expected behavior. 

  

Notification Type in sys\_email table:

![sys\_email table](sys_attachment.do?sys_id=ac0744c5dbd6d890a08a1ea668961955 "Notification Type")

Email properties:

![Email Properties](sys_attachment.do?sys_id=600704c5dbd6d890a08a1ea6689619c8 "Email Properties")

  

Normally, in sub-prod environments, email property "Send all email to this test email address" will be enabled in order to avoid email sending to the actual user.   

  

-   In the configured notification, if "SMS Alternate" is checked under "What it will contain" tab and if the user has set up the device for receiving mobile notifications in SMS then SMS will be sent to the customer along with the email when notification triggered.  
    
-   In sub-prod environments, if the email property "Send all email to this test email address" is enabled then we are not allowed to send an SMS notification to the actual user device.
-   So, instead of doing that, the instance will send an email to the configured test email address instead of SMS which will be confusing to the customer.
-   But this is expected behavior and will be seen in only in the instance where email property "Send all email to this test email address" is enabled. This is to make sure there are no issues in the notification part.

  

## Resolution

Basically, this is not an issue and this is expected behavior and will not occur in the production instance.
