---
title: "How to manage email and SMS notifications on Now Support"
aliases:
  - KB0547254
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547254
kb_number: KB0547254
last_modified: 2026-06-02
---

## How to manage email and SMS notifications on Now Support

  

### Issue

As a registered instance user, Now Support notifications keep you informed of events that concern you. Now Support sends notifications through email and SMS text messages. This article shows how to manage your notification preferences. 

  

### Release

All releases

### Resolution

### Managing notifications using notification preferences

**Note:** This option is currently unavailable for partners.

**Notification preferences** is a Now Support page where you can configure your notifications. You can select your preferred communication options, for example, which channels (email, SMSM), what kinds of messages, and in what areas.   

-   [Email Notifications](#email)
-   [SMS Notifications](#sms)
-   [Verifying Mobile Number](#verify)

### Email Notifications

Email notifications are Now Support updates that you receive via email. You cannot turn off email notifications entirely, but you can adjust what you get notified about and how you get notified.

To change your email notifications:

1.  Go to the Now Support home page and select the **Notifications icon** at the top.  
    ![Go to the Now Support home page and select the Notifications icon at the top.](/sys_attachment.do?sys_id=b0cc66a097ddcf50f69577121153afad)  
      
    
2.  Select the **gear icon**.  
      
    
3.  Next to each notification category, select or or unselect the **Email** option to choose which email notifications you want to receive.

**Note:** You cannot turn off all notifications. Some mandatory notifications cannot be unsubscribed. These mandatory notifications are checked by default and appear greyed out on the Notification Preferences page.   
  
![Some mandatory notifications cannot be unsubscribed. These mandatory notifications are checked by default and appear greyed out on the Notification Preferences page.](/sys_attachment.do?sys_id=78cca6a097ddcf50f69577121153af1e)  
  

### SMS Notifications

SMS notifications are Now Support updates that you receive through SMS. You can opt-in or out of SMS notifications for cases and change requests.

Users can set up SMS notifications using the **Notification Preference** page.

1.  Go to the Now Support home page and select the Notifications icon at the top. 
2.  Select **Notification Preferences**.
3.  Select **SMS** next to any case or change request notification.
4.  Verify your mobile number to receive SMS notifications. For mobile number verification, see [Verifying mobile number](#verify).
5.  To unsubscribe, unselect **SMS** next to the notification category.

**Note:**

-   SMS notifications can only be activated for case and change request notifications.
-   SMS text message notifications are sent as quickly as possible, but sometimes delays can occur. Mobile network congestion or other processing delays and errors on your mobile carrier's side can result in delivery delays or failures.
-   To receive notifications for all cases opened and cases updated with comments, add the user to the notification list on the **Manage Accounts** page.

### Verifying Mobile Number

You need to verify your mobile number to receive SMS notifications.

To verify your mobile phone number:

1.  Go to the Now Support home page and select the **Notifications** icon at the top. 
2.  Select **Notification Preferences**.
3.  Select **SMS** next to any case or change request notification, or select **Edit Mobile Number**. 
    -   In the **Mobile Verification** dialog, select the country code and enter your 10-digit mobile number. Your mobile number auto-populates if it already exists in your user profile.   
          
        ![In the Mobile Verification dialog, select the country code and enter your 10-digit mobile number. Your mobile number auto-populates if it already exists in your user profile. ](/sys_attachment.do?sys_id=7ccc66a097ddcf50f69577121153afb1)  
          
        
4.  Select **Send Verification Code**. A 6-digit code is sent to the mobile phone number you provided. If you do not receive a 6-digit code within a few minutes, select **Resend Code**.
5.   In the **Mobile Verification** dialog box, enter the 6-digit code.   
      
    ![In the Mobile Verification dialog box, enter the 6-digit code. ](/sys_attachment.do?sys_id=bccc26a097ddcf50f69577121153af4e)  
      
    
6.  Select **Verify**.

If the verification is successful, you can start opting in for SMS notifications. 

### Case Notifications

Based on events and priority levels, users listed in specific fields on the Case record receive email notifications. If the case is related to a mass outage or maintenance window, see the Key contact notifications section of this article.

#### Case customer notifications

<table style="width: 100%; border-collapse: collapse; border: 1px solid rgb(149, 165, 166);" border="1"><tbody><tr style="height: 15.4018px;"><td style="width: 33.3333%; height: 15.4018px; padding: 10px; border-color: rgb(149, 165, 166);"><strong>Case Notifications</strong></td><td style="width: 33.3333%; height: 15.4018px; padding: 10px; border-color: rgb(149, 165, 166);"><strong>Priority</strong></td><td style="width: 33.3333%; height: 15.4018px; padding: 10px; border-color: rgb(149, 165, 166);"><strong>Recipients Notified&nbsp;</strong></td></tr><tr style="height: 15.4018px;"><td style="width: 33.3333%; height: 15.4018px; padding: 10px; border-color: rgb(149, 165, 166);">Case Created</td><td style="width: 33.3333%; height: 15.4018px; padding: 10px; border-color: rgb(149, 165, 166);">All</td><td style="width: 33.3333%; height: 15.4018px; padding: 10px; border-color: rgb(149, 165, 166);">Case Contact, Users on the Watchlist&nbsp;</td></tr><tr style="height: 15.4018px;"><td style="width: 33.3333%; height: 15.4018px; padding: 10px; border-color: rgb(149, 165, 166);">Case Closed</td><td style="width: 33.3333%; height: 15.4018px; padding: 10px; border-color: rgb(149, 165, 166);">All</td><td style="width: 33.3333%; height: 15.4018px; padding: 10px; border-color: rgb(149, 165, 166);">Case Contact, Users on the Watchlist&nbsp;</td></tr><tr style="height: 15.4018px;"><td style="width: 33.3333%; height: 15.4018px; padding: 10px; border-color: rgb(149, 165, 166);">Case Commented</td><td style="width: 33.3333%; height: 15.4018px; padding: 10px; border-color: rgb(149, 165, 166);">All&nbsp;</td><td style="width: 33.3333%; height: 15.4018px; padding: 10px; border-color: rgb(149, 165, 166);">Case Contact, Users on the Watchlist&nbsp;</td></tr><tr style="height: 15.4018px;"><td style="width: 33.3333%; height: 15.4018px; padding: 10px; border-color: rgb(149, 165, 166);">Case Solution Proposed</td><td style="width: 33.3333%; height: 15.4018px; padding: 10px; border-color: rgb(149, 165, 166);">All</td><td style="width: 33.3333%; height: 15.4018px; padding: 10px; border-color: rgb(149, 165, 166);">Case Contact, User(s) on the Watchlist&nbsp;</td></tr><tr style="height: 15.4018px;"><td style="width: 33.3333%; height: 15.4018px; padding: 10px; border-color: rgb(149, 165, 166);">Temporary Relief</td><td style="width: 33.3333%; height: 15.4018px; padding: 10px; border-color: rgb(149, 165, 166);">P1</td><td style="width: 33.3333%; height: 15.4018px; padding: 10px; border-color: rgb(149, 165, 166);">Case Contact, User(s) on the Watchlist&nbsp;</td></tr></tbody></table>

### Key contact notifications

For more information about contacts, their focus areas, and which communications they receive, see [Managing company contacts on Now Support](/kb_view.do?sysparm_article=KB0547262 "Managing company contacts on Now Support").

### Related Links

Learn more about:  
[Notification Preferences](https://www.servicenow.com/docs/r/platform-administration/preferences-landing.html)
