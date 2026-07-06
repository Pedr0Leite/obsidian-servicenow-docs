---
title: "Troubleshoot notification issues with cmn_notif_device and cmn_notif_message tables"
aliases:
  - KB0750584
  - Troubleshoot notification issues with cmn_notif_device and cmn_notif_message tables
tags:
  - servicenow
  - support-kb
  - notifications
  - cmn_notif_device
  - cmn_notif_message
  - email-devices
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750584
kb_number: KB0750584
last_modified: 2025-11-10
---

## Troubleshoot notification issues with cmn\_notif\_device and cmn\_notif\_message tables

  

### Issue

This article explains how the Notification Device \[cmn\_notif\_device\] table and the Notification Messages \[cmn\_notif\_message\] tables work and helps you resolve common user configuration errors that cause notification failures. Notification issues relating to misconfigured users can include messages like the following:

-   "Email validation failed: Email has no recipients"
-   "Flow Designer Action 'Send Email' not including user in CC"
-   "Excluded recipients because user has no usable devices" 

### Release

All supported releases

### Resolution

#### **Notification Device** **\[cmn\_notif\_device\]** **table** 

When you create a record in the User \[sys\_user\] table, the system automatically creates a corresponding record in the cmn\_notif\_device table. Updates follow the same pattern.

For example:

-   When you update a user's email address in the sys\_user table, the email address is updated in the cmn\_notif\_device table by running the Update email devices business rule. 
-   The primary address in the cmn\_notif\_device table is used to send notifications. This overrides the email address configured in the sys\_user table.
-   If a user lacks an active or valid cmn\_notif\_device record when referenced in notifications, flows, or sub-flows, they cannot receive notifications. This applies to users in the To, CC, or BCC fields.

**Resolve missing notifications due to inactive or invalid cmn\_notif\_device records**

Add the primary email device.

**As a user**, you can do the following:

1.  Go to **Self-Service** > **My Notification Preferences.**
2.  Select **Create New Device.**
3.  Enter your primary email address.
4.  Select the **Primary Email** check box to set it as your primary notification channel.

**As an admin**, add a primary email device a user:

1.  Go to the cmn\_notif\_device table
2.  Select **New**.
3.  Complete all details to create a new primary email device record.
4.  If a record already exists but is inactive, simply activate it.

#### **Notification Messages \[cmn\_notif\_message\] table**

Notifications are defined in the Email Notifications \[sysevent\_email\_action\] table. Notifications with \[Subscribable\] \[=\] \[true\] conditions are available for subscription. When you receive a notification for the first time, it appears in your subscriptions and can be modified from there. 

Subscriptions are stored in the Notification Messages \[cmn\_notif\_message\] table.

To subscribe to certain notifications by default:

-   Configure a business rule that creates the necessary entries in the cmn\_notif\_message table when a user record is inserted.
-   To subscribe existing users, use a scheduled job or a background script. 

If multiple users subscribed to the same email notification, there will be one record created for each user for this email notification in this table.

## Related

- [[KB0750659 - Subscribable Notifications and the property glide.notification.use_legacy_subscription_model]]
- [[KB0749713 - Email template sc_req_item.itil using incorrect reference to comments]]
- [[KB0750361 - How to verify inclusion of Outlook actionable messages in email notifications]]
- [[KB0792530 - CmnNotifDevice cannot be null Exception is thrown while processing User Notification Preferences if cmn_notif_device has]]
