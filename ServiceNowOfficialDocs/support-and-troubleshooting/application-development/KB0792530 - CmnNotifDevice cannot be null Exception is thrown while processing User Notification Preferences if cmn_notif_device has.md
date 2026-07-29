---
title: "\"CmnNotifDevice cannot be null\" Exception is thrown while processing User Notification Preferences if cmn_notif_device has No Read Access"
aliases:
  - KB0792530
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792530
kb_number: KB0792530
last_modified: 2024-04-08
---

## "CmnNotifDevice cannot be null" Exception is thrown while processing User Notification Preferences if cmn\_notif\_device has No Read Access

  

### Issue

One of the personal subscriptions does not consistently works and error "CmnNotifDevice cannot be null" Exception is thrown

### Release

New York patch 4 Hotfix 1 and onwards

### Cause

The issue happens while processing User Notification Preferences for a device, when we try to fetch a device by Id and we have an ACL check on cmn\_notif\_device for read access

This also can happen when CmnNotifMessage record is not correctly configured and has an invalid sys\_id.

If the above mentioned condition is met on cmn\_notif\_device then we pass null for CmnNotifDevice in NotificationRecipientBuilder#processUserNotificationMessageForADevice, which throws an exception as "CmnNotifDevice cannot be null: java.lang.NullPointerException: CmnNotifDevice cannot be null: ".

After fix is determined, regression test Notification Preview functionality and Notification Preferences functionality

### Resolution

There can be two work arounds

Workaround 1 : To adjust / revisit the ACL on cmn\_notif\_device that restrict read access.

Workaround 2 : Correct references for cmn\_notif\_device on cmn\_notif\_message which points to invalid cmn\_notif\_device which do not exist for the notification which was triggered and causing issue in preview.

### Related Links

Path 1:  
1\. Create No Read Access ACL on cmn\_notif\_device with admin override flag as false.  
2\. Create a subscribable notification for incident on update.  
3\. Set "glide.notification.use\_legacy\_subscription\_model" property as false.  
4\. Create a cmn\_notif\_message for a specific user and with the created subscribed notification.  
5\. Trigger the Notification.  
An Exception is thrown

CmnNotifDevice cannot be null: java.lang.NullPointerException: CmnNotifDevice cannot be null: com.google.common.base.Preconditions.checkNotNull(Preconditions.java:787)  
com.glide.notification.cmn.NotificationDevice.<init>(NotificationDevice.java:42)  
com.glide.notification.cmn.UserNotificationPreference.<init>(UserNotificationPreference.java:30)  
com.glide.notification.cmn.NotificationRecipientsBuilder.processUserNotificationMessageForADevice(NotificationRecipientsBuilder.java:722)  
com.glide.notification.cmn.NotificationRecipientsBuilder.processUserNotificationMessage(NotificationRecipientsBuilder.java:696)  
com.glide.notification.cmn.NotificationRecipientsBuilder.querySubscribedUsers(NotificationRecipientsBuilder.java:321)  
com.glide.notification.cmn.NotificationRecipientsBuilder.build(NotificationRecipientsBuilder.java:190)  
com.glide.notification.cmn.NotificationActionHandler.send(NotificationActionHandler.java:87)  
com.glide.notification.cmn.NotificationActionHandler.process(NotificationActionHandler.java:72)  
com.glide.policy.EventProcessor.processEventDuringNormalOperation(EventProcessor.java:213)  
com.glide.policy.EventProcessor.processEvent(EventProcessor.java:138)  
com.glide.policy.EventProcessor.process(EventProcessor.java:92)  
com.glide.policy.EventManager.processEvents(EventManager.java:291)  
com.glide.policy.EventManager.\_process(EventManager.java:166)  
com.glide.policy.EventManager.process(EventManager.java:148)  
sun.reflect.GeneratedMethodAccessor446.invoke(Unknown Source)  
sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)

Path 2:  
1\. Create a subscribable notification for incident on update.  
2\. Set "glide.notification.use\_legacy\_subscription\_model" property as false.  
3\. Create a cmn\_notif\_message pointing a subscribed notification / user / cmn\_notif\_device  
4\. Delete the cmn\_notif\_device record, the cmn\_notif\_message now points an invalid device which does not exists.  
5\. Preview the notification, the recipients for that notification will not be added in the preview.  
6\. An Exception would be see in sys\_log  
CmnNotifDevice cannot be null: java.lang.NullPointerException: CmnNotifDevice cannot be null: com.google.common.base.Preconditions.checkNotNull(Preconditions.java:787)  
com.glide.notification.cmn.NotificationDevice.<init>(NotificationDevice.java:42)  
com.glide.notification.cmn.UserNotificationPreference.<init>(UserNotificationPreference.java:30)  
com.glide.notification.cmn.NotificationRecipientsBuilder.processUserNotificationMessageForADevice(NotificationRecipientsBuilder.java:722)  
com.glide.notification.cmn.NotificationRecipientsBuilder.processUserNotificationMessage(NotificationRecipientsBuilder.java:696)  
com.glide.notification.cmn.NotificationRecipientsBuilder.querySubscribedUsers(NotificationRecipientsBuilder.java:321)  
com.glide.notification.cmn.NotificationRecipientsBuilder.build(NotificationRecipientsBuilder.java:190)  
com.glide.notification.cmn.NotificationActionHandler.send(NotificationActionHandler.java:87)  
com.glide.notification.cmn.NotificationActionHandler.process(NotificationActionHandler.java:72)  
com.glide.policy.EventProcessor.processEventDuringNormalOperation(EventProcessor.java:213)
