---
title: "How to setup a SMS Email Notification in ServiceNow"
aliases:
  - KB0712569
tags:
  - servicenow
  - support-kb
  - notifications
  - SMS
  - email-notifications
  - Notify
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0712569
kb_number: KB0712569
last_modified: 2026-05-07
---

## How to setup a SMS Email Notification in ServiceNow

  

### Issue

ServiceNow supports standard Email, SMS, and Push notifications. SMS notifications can be sent either through _Notify_ or via _Email Notification_ using an email-to-text gateway.

_Notify_ is a separate and more robust solution that requires integration with third-party software, such as _Twilio_, along with specific workflows to send out SMS notifications. For details on integrating Twilio with ServiceNow, refer to this [Twilio blog post](https://www.twilio.com/en-us/blog/create-notification-system-servicenow-using-twilio-sms-and-voice).

**Important Update:** The delivery of SMS via Email Notification may be impacted, as some service providers are beginning to deprecate the "email-to-text" functionality. For instance, AT&T will discontinue support for its "email-to-text" service starting June 17th, 2025 ([AT&T article](https://www.att.com/support/article/wireless/KM1061254/)), and Verizon may follow suit.

**Additional Important Update:** Some SMS messages coming from ServiceNow will change their shortcode From number in May 2026. Messages that had previously been received on AT&T handsets from 87843431 will now be coming from 34271.

For more reliable and future-proof SMS delivery, it is recommended to use _Notify_. More information about _Notify_ can be found [here](https://www.servicenow.com/docs/bundle/yokohama-servicenow-platform/page/product/notify2/reference/notify-landing-page.html).

This article focuses specifically on how to configure and troubleshoot SMS Notifications that rely on standard email configurations within ServiceNow.

### Procedure

1.  **Create an email notification**  
    
    -   It's necessary to create a normal email notification on the instance.
    -   SMS messages are normally limited to 140 characters so make sure the message length in the email notification is under this limit otherwise it may be truncated.
    -   **Note:** There is an "**SMS alternate**" field on the \[**What it will contain**\] tab in the Advanced view of any email notification.
    -   Users can create a brief short message dedicated for SMS when this email notification could be used for multiple purposes, both email and SMS device, at the same time.
    
    ![screenshot1](sys_attachment.do?sys_id=cdd520089330079cdef533527cba100d "screenshot1")
    
2.  **Create an SMS service provider**  
    -   Please consult the documentation: [Create a service provider](https://docs.servicenow.com/csh?topicname=t_CreateAServiceProvider.html&version=latest "Create a service provider (London)")
    -   All the created notification service provider records are stored in the table **cmn\_notif\_service\_provider.list** on the instance.
    -   **Note 2.1:** Make sure the **Active** box is checked for the service provider used to send the SMS notification.
        
        ![screenshot2](sys_attachment.do?sys_id=cdd520089330079cdef533527cba102c "screenshot2")
        
    -   **Note 2.2:** When troubleshooting any SMS notification issue it is necessary to narrow down the scope to check whether the SMS notification or the SMS service provider have any issues. In that case, you can test SMS notifications by switching to any OOB service provider.
    -   If the email notification can be triggered successfully then the system will always create an SMS notification record in the **sys\_email** table, just like an email record. This will prove email notification has no wrong configuration and the issue is related to the SMS service provider. If not, then it is easy to know something wrong must be in the email notification configuration.
3.  **Create and select an SMS device for a specific user**  
    -   When any specific user is chosen to receive the SMS notification then it is necessary to create an SMS device for this user if there is no one on the instance.
    -   Steps can be referred from the below docs link. [Select a service provider](https://docs.servicenow.com/csh?topicname=t_SelectingAServiceProvider.html&version=latest "Select a service provider (London)")
    -   **Note 3.1:** When creating a new SMS device, please make sure you use the following values:  
        
        -   -   **Type: SMS**
            -   **User:** sys\_user record which is being selected as the recipient for the SMS notification
            -   **Phone number:** the phone number to receive the SMS notification, SMS will be sent to address with format **_<phone number>@<SMS Provider Email Suffix>_**. The latter part after @ is the email suffix configured on the SMS service provider record in step 2. In the below screenshot, the address would be "123-456-7890@example.com".
            -   **Service provider:** service provider record created in step 2
            -   **Primary email:** **false** (because this device is used for SMS only)
            -   **Active: true**
        
        ![screenshot4](sys_attachment.do?sys_id=c9d520089330079cdef533527cba1036 "screenshot4")
        
    -   **Note 3.2:** In ServiceNow, all the notification-related devices are stored in the **cmn\_notif\_device.list** table. This includes standard email, SMS, and Push notification devices.
    -   When troubleshooting SMS notification issues it is necessary to look up the customer's SMS notification device record in this table to see if any misconfigurations.
4.  **Enable the SMS device and the SMS Notification in User Notification Preference**  
    -   **Note 4.1:** Make sure the SMS device is enabled in the Notification Preference for the recipient user. In this screenshot, the "Mobile" SMS device is enabled.
        
        ![screenshot5](sys_attachment.do?sys_id=49d520089330079cdef533527cba103b "screenshot5")
        
    -   **Note 4.2:** Make sure SMS email notification is enabled for this SMS device in user Notification Preference as well.
    -   In this screenshot, the email notification "Incident commented\_1" is enabled for the "Mobile" SMS device.3
    -   **Note 4.3:** This steps must be performed by each user or by impersonating the user. [Create notification channels.](https://docs.servicenow.com/bundle/utah-platform-administration/page/administer/notification/task/create-channel.html)
    -   ![screenshot6](sys_attachment.do?sys_id=c5d520089330079cdef533527cba1040 "screenshot6")
        

### Set up an SMS Email Notification Subscription

Sometimes users may only want to subscribe to an SMS email notification without being selected as a recipient in the SMS email notification.

The configuration steps are nearly the same with only two differences.

1.  **Create an email notification**  
    -   Same as the previous step 1. The only difference is to make the notification subscribable by checking the \[**Subscribable**\] check box on the \[**Who will receive**\] tab in the email notification.
        
        ![screenshot3](sys_attachment.do?sys_id=4dd520089330079cdef533527cba1031 "screenshot3")
        
2.  Create a **Notification Subscription record**
    
    For notification subscription, ServiceNow stores all user subscription records in **sys\_notif\_subscription.list** table for all notifications.
    
    The user needs to create a new one if there is no subscription record in this table. Please make sure these values are used:
    
    -   **User:** sys\_user record which subscribed to the SMS notification
    -   **Notification:** SMS notification name. In the below screenshot, the notification name is "Incident commented\_1"
    -   **Send to:** SMS device name. In the below screenshot, the SMS device name is "Mobile"
    -   **Table:** Table name on which the SMS notification is created. In the below screenshot, the table name is "incident"
    -   **Active:** **true**
        
        ![screenshot7](sys_attachment.do?sys_id=45d520089330079cdef533527cba1045 "screenshot7")
        

**Note:** When troubleshooting SMS Notification Subscription issues, first check if there is a corresponding SMS subscription record created in the **sys\_notif\_subscription.list** table. If any, then continue to check to see if there is any misconfiguration in that SMS subscription record.

After all the above steps are completed correctly, trigger the SMS notification. A new **sys\_email** record will be created and sent to the SMS email address.

![screenshot8](sys_attachment.do?sys_id=d1d520089330079cdef533527cba104a "screenshot8")

### Release

SMS notification is a core function of the ServiceNow platform available from all the supported versions starting from Geneva.

### Resolution

For more reliable and future-proof SMS delivery, it is recommended to use _Notify_. More information about _Notify_ can be found [here](https://www.servicenow.com/docs/bundle/yokohama-servicenow-platform/page/product/notify2/reference/notify-landing-page.html). For details on integrating Twilio with ServiceNow, refer to this [Twilio blog post](https://www.twilio.com/en-us/blog/create-notification-system-servicenow-using-twilio-sms-and-voice).

## Related

- [[KB0694768 - Email client only supports one email client template per table]]
- [[KB0716520 - Notification emails are not generated when the Message HTML field contains a hyperlink]]
- [[KB0722504 - Using ServiceNow blackhole or dummy email addresses]]
