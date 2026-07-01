---
title: Location tracking for mobile
description: Location tracking enables you to track the activity and positioning of agents while they perform tasks. You can also use the feature to make sure your agents are safe and can be easily located.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/mobile/mobile-location-tracking.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Before implementation, Configuration detail, Configuring the Mobile Platform, Mobile Platform]
---

# Location tracking for mobile

Location tracking enables you to track the activity and positioning of agents while they perform tasks. You can also use the feature to make sure your agents are safe and can be easily located.

## Location tracking options

There are two options available for location tracking. You can either select one option for users or you can make both options available to users who then must select a location tracking option. The location tracking option that you select applies to the instance.

The two location tracking options are:

-   Manual tracking – This option enables users to select whether to start location tracking for a defined period or for users ￼￼to be continuously tracked. This type of location tracking is only supported on the [[mobile-experience|Mobile Agent app]]. For information about the manual tracking option, see [[location-tracking-manual-config|Configuring manual location tracking]].
-   Action-based tracking – You can use this option to configure functions to start or stop location tracking, based on actions a user performs. This type of location tracking is supported on both the Mobile Agent app and the [[now-mobile-app|Now Mobile app]]. For information about the action-based tracking option, see [[location-tracking-action-config|Configuring action-based location tracking]].

## Activating plugins

As an administrator, you must activate geolocation tracking for your  users by installing the Geolocation plugin \(com.snc.geolocation\). This plugin enables the manual tracking option. To enable action-based location tracking, the Mobile Location Tracking plugin \(com.glide.sg.location.tracking\) must be installed.

**Note:** To install the Mobile Location Tracking plugin \(com.glide.sg.location.tracking\), you must first install the Geolocation plugin \(com.snc.geolocation\).

For details on plugin activation, see [Activate a plugin](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/t_ActivateAPlugin.md).

## Location tracking and your users

After activating the plugins and performing the various configurations, you must enable location tracking for users. For more information, see [[location-tracking-add-user|Enabling location tracking for users]].

On the users-side, after configuring the location tracking options, users will see the geolocation location tracking settings in the  **Settings**  tab of their mobile devices. Users can enable or disable location tracking on their device. For more information, see [[mobile-location|Using location tracking for mobile]].

## Location tracking in offline

Location tracking is supported in offline. While offline, the user’s location and activity is collected and stored in the device. When the user goes back online, all the collected tracking data is synchronized to their instance.

-   **[[location-tracking-enable|Enabling and selecting location tracking options]]**  
Learn how to enable location tracking for the Mobile Agent and select the location tracking option best suited for your users.
-   **[Enabling location tracking for users](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/mobile/location-tracking-add-user.md)**  
Enable location tracking for specified users. The same tracking location settings apply to all the selected users on the instance.

**Parent Topic:**[[imp-considerations|Considerations before implementation]]

## Related

- [[location-tracking-manual-config|Configuring manual location tracking]]
- [[location-tracking-action-config|Configuring action-based location tracking]]
- [[location-tracking-add-user|Enabling location tracking for users]]
- [[mobile-location|Using location tracking for mobile]]
- [[location-tracking-enable|Enabling and selecting location tracking options]]
- [[imp-considerations|Considerations before implementation]]
- [[mobile-experience|Mobile Agent app]]
- [[now-mobile-app|Now Mobile app]]
