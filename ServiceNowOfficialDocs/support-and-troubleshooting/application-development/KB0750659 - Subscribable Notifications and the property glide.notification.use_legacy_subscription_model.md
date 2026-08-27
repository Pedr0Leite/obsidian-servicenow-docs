---
title: "Subscribable Notifications and the property \"glide.notification.use_legacy_subscription_model\"
aliases:
  - KB0750659
  - Subscribable Notifications legacy subscription model
tags:
  - servicenow
  - support-kb
  - notifications
  - subscriptions
  - sys_notif_subscription
  - cmn_notif_message
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750659
kb_number: KB0750659
last_modified: 2024-04-07
---

## Issue

## Overview

This article explains the original motivation for the 'glide.notification.use\_legacy\_subscription\_model' property, and describes the behaviors resulting when setting 'true' and 'false'.

This property controls where Subscribable notification preferences are stored and system behavior for each setting.

## What is the recommended setting?

On upgrade into Helsinki or later the property defaults to 'false', and a fix script locates all subscribable notifications at upgrade time and migrates their corresponding 'cmn\_notif\_message' records to the new 'sys\_notif\_subscription' table.

The recommended setting is 'false'.

## Why would I set to 'true'?

Some instances might have a customization that prevented the feature from working and broke some customization functionality on upgrade in to Helsinki or later. If that is the case, admins could set to 'true' temporarily to keep functionality running, while they determine what needs to change in the customizations to align with the existence of the new preference model. 

Once fixed, the property should be set back to 'false', and an optional re-migrate performed.

It is not recommended to flip this back and forth - its intent is to facilitate migration to the new model. 

**Note:** If you choose to leave this as 'true', you must accept the flaws described in the next section.

## Why is the "Legacy" data model mode deprecated?

Prior to the new data model, all preferences - for both subscribable and non-subscribable notifications - were stored in the table 'cmn\_notif\_message'. This legacy model has an ambiguity that has caused P1/P2 issues.

A non-subscribable notification is addressed to specific users configured in the notification record. When a user receives a non-subscribable notification the first time, a 'cmn\_notif\_message' preference is created for that user.  Because such a notification usually fires to a different set of users each time, many 'cmn\_notif\_message' records are created over time.

In the legacy model, the system can only tell whether a 'cmn\_notif\_message' record is a 'subscribe' preference by looking at whether its related notification is 'subscribable'.

Thus if a notification is changed from non-subscribable to subscribable, all of the cmn\_notif\_message 'preferences' associated with it are now interpreted as 'subscriptions'. Every user who ever received that notification when it was non-subscribable is now treated as if they had subscribed to it. If the changed notification already existed as non-subscribable for a long time, then there are many user preferences that have accumulated. When later changed to 'subscribable', the instance will likely experience a P1 or P2 incident -  a huge number of users receiving the notification email they did not expect.

## Behaviors

### glide.notification.use\_legacy\_subscription\_model == false 

-   a user's choice to subscribe is stored in the sys\_notif\_subscription table
-   a user's preference on a non-subscribable notification is stored in cmn\_notif\_message. 
-   The system queries 'sys\_notif\_subscription' when the notification is subscribable, and 'cmn\_notif\_message' when not.

###   
glide.notification.use\_legacy\_subscription\_model == true 

-   a user's choice to subscribe is stored in the cmn\_notif\_message table
-   a user's preference on a non-subscribable notification is stored in cmn\_notif\_message. 
-   The system queries only the 'cmn\_notif\_message' table to determine preferences, and distinguishes subscribable preferences by checking the related notification's setting.

##   
Side effects of switching from one value to another

The tables are mutually exclusive. Preferences set by users in the system while the property is one setting are not reflected in the other table when the property is changed.

After an admin changes the property value, a user might complain that a previously set preference for a subscribable notification has been 'lost' because that table is no longer in effect.

Because the intent of the property is to facilitate a 'one-way' migration, the system does not keep the two tables in sync in normal operation.

## Manually running the Migration fix script after addressing customization issues

The fix script upon upgrade to Helsinki performed a one-time migration of 'cmn\_notif\_message' records for subscribable notifications at the time into new 'sys\_notif\_subscription' records, and set the property to 'false'

var migrator = new SubscriptionMigrator();  
migrator.migrateSubscriptions();

  
If an instance had customizations and the admin decided to revert back to legacy mode at some point, they can re-run functionality to re-migrate subscribable notification preferences and move to the recommended mode. 

**Re-Run Warning**

This was already run one time when the system upgraded into H or later. 

Thus the 'sys\_notif\_subscription table will contain some migrated records from that original upgrade fix script, as well as subsequent user preference activity while the property was in 'false' mode after upgrade.  
  
If the instance admin changed the property back to legacy subscription mode, user preference activity reverted to using the 'cmn\_notif\_message' table, where continued updates/inserts occurred.

The migration functionality does not 'merge' with pre-existing 'sys\_notif\_subscription' records, which will result in undesirable duplication - This must be avoided.

If this is the case, before rerunning migration again, any 'sys\_notif\_subscription' records should be deleted before running the migration functionality.

Test on a non-prod clone first.

### Performance Considerations 

Some larger instances may have very large 'cmn\_notif\_message' tables and the migration process might take awhile.  Therefore the process of migration should be tested first on a non-production clone.

## Related

- [[KB0750584 - Troubleshoot notification issues with cmn_notif_device and cmn_notif_message tables]]
- [[KB0755067 - How to fix business rule conditions that can cause multiple notifications]]
- [[KB0752062 - SLA emails are not sent to assigned to user]]
- [[KB0791868 - How to fix event notifications that fail to trigger]]

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0715790 - Users see an error message Record doesn't exist or ACL restricts the record retrieval when making changes to their Notif|Users see an error message \"Record doesn't exist or ACL restricts the record retrieval\" when making changes to their Notifications settings]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0750584 - Troubleshoot notification issues with cmn_notif_device and cmn_notif_message tables|Troubleshoot notification issues with cmn_notif_device and cmn_notif_message tables]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/notifications/pe-bootstrap-notify/README|pe-bootstrap-notify]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Notifications/Add KB Article Link Dynamic Email Script to Notification/readme|Add KB Article Link Dynamic Email Script to Notification]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Notifications/Conditional Trigger/README|Conditional Trigger]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Notifications/Modern Email Layout Designs/Readme|Modern Email Layout Designs]]
