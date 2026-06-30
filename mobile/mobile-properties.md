---
title: Mobile properties
description: Mobile properties enable admins to turn on or turn off features in ServiceNow apps without upgrading the ServiceNow instance.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/mobile/mobile-properties.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [Before implementation, Configuration detail, Configuring the Mobile Platform, Mobile Platform]
---

# Mobile properties

Mobile properties enable admins to turn on or turn off features in ServiceNow apps without upgrading the ServiceNow instance.

The ServiceNow Platform server controls the features that are available on your mobile app. The server instance is released with new features for every family release. New versions of the mobile apps are released to the Apple Store and the Google Play Store every month. These monthly releases of mobile apps usually contain bug fixes but can also contain new features. These new features can be turned on or off with mobile properties.

Mobile properties can be configured to set flags on your ServiceNow instance. These "flags" are records structured as key/value pairs in the sys\_sg\_properties table. They can turn on or turn off features on your mobile client apps. The ServiceNow instance sends the mobile property to mobile client apps after authentication.

Mobile properties are available starting with the San Diego release.

## Application scope and mobile properties

When you create a mobile property, you select the application scope for which the property is available in the Mobile Properties New record form. To change the list of available application scopes, select the globe icon \(\[Omitted image "globe-icon.png"\] Alt text: Globe icon.\) on the instance banner and then select **Application scope:_application\_scope_**.

## Application scope precedence

When multiple mobile properties of the same name are defined for multiple application scopes, the system applies precedence rules to select a mobile property to use. The following scenarios use the **clientRefresh** mobile property as an example to show how the precedence rules work.

-   **Scenario 1: Global application scope always takes precedence**

    If a mobile property is defined for multiple application scopes and one of those is the global application scope, then the property defined for global application scope always takes precedence. In this case, the following actions occur:

    1.  The system calls for the **clientRefresh** property on an instance.
    2.  The system finds three **clientRefresh** properties defined for this instance:

        |Property name|Application scope|Updated \(date and time\)|
        |-------------|-----------------|-------------------------|
        |clientRefresh|Global|2021-12-06 10:41:00|
        |clientRefresh|Now Mobile|2021-12-06 10:38:41|
        |clientRefresh|Agent Workspace|2021-12-06 10:42:06|

    3.  The system chooses the **clientRefresh** property defined for the global application scope.
    In scenario 1, the **clientRefresh** property defined for the global application scope takes precedence.

-   **Scenario 2: If the mobile property isn't defined for global application scope, then the most recently updated property takes precedence**

    If a mobile property is defined for multiple application scopes but if there is no property with global application scope, then the system uses the most recently updated property. In this case, the following actions occur:

    1.  The system calls for the **clientRefresh** property on an instance.
    2.  The system finds three **clientRefresh** properties defined for this instance:

        |Property name|Application scope|Updated \(date and time\)|
        |-------------|-----------------|-------------------------|
        |clientRefresh|Now Mobile|2021-12-06 10:38:41|
        |clientRefresh|Asset Management for mobile|2021-12-06 10:42:06|
        |clientRefresh|Agent Workspace|2021-12-06 12:06:20|

    3.  The system chooses the **clientRefresh** property that was most recently updated.
    In scenario 2, the **clientRefresh** property defined for the agent workspace application scope was the most recently updated. All three mobile properties were updated on 2021-12-06. The property defined for the agent workspace application scope was updated at 12:06:20. That time is almost one and a half hours after the other two. The system chooses the **clientRefresh** property defined for the agent workspace application scope because it's the most recently updated **clientRefresh** property.


-   **[[enable-disable-auto-app-refresh|Turn on or turn off automatic app refresh]]**  
Use the **clientRefresh** mobile property on your ServiceNow instance to turn on or turn off automatically refreshing your mobile apps. You can also use the **clientRefresh** property to adjust the scope of refresh on your mobile app.
-   **[[enable-ext-users-attach-access|Enable external users to access attachments]]**  
Enable users who have been assigned the snc\_external role to be able to view, upload, and download attachments on their ServiceNow mobile app.
-   **[[switch-date-time-timezone-utc|Switch the date/time fields between device time zone and UTC]]**  
Use the **ShowDateTimeInUTC** mobile property to determine whether the date/time field values in the [[now-mobile-app|Now Mobile app]] are displayed in the time zone of the user's device \(default\) or are converted to UTC.
-   **[[config-apps2use-devicedatetimeform|Configure mobile apps to use the date/time format of mobile devices]]**  
Set the **useDeviceSettingsForDateTimeFormats** mobile property to `True` to configure the date/time fields in mobile apps to use the date/time format that is used on the mobile device.
-   **[[hide-secs-mobcds-recscreen-actstrem|Hide seconds in date/time fields on mobile cards, record screen details pages, or activity streams]]**  
Set the **mobileCardsShowSeconds**, **recordScreenDetailsShowSeconds**, or the **activityStreamShowSeconds** mobile properties to `False` to hide the display of seconds in date/time fields.
-   **[[extend-embedded-web-sessions|Extend embedded web sessions]]**  
Extend embedded web sessions to keep mobile users logged in until the mobile OAuth token expires.
-   **[[enable-enhanced-barcode-scan|Enable enhanced barcode scanning]]**  
Add the **EnableCameraFocusEnhancement** and the **EnableMaxCameraResolution** mobile properties to enhance barcode scanning for Android devices.
-   **[[enable-external-barcode-scanner|Enable barcode scanning with an external scanner]]**  
Set the **externalScanEnabled** mobile property to `True` to enable barcode scanning with an external scanner while the device camera is available in other parts of the mobile app.
-   **[[mob-attachments-android|Configure different mobile attachment capabilities on Android devices based on user roles]]**  
Use a combination of system properties and mobile properties to enable different users on Android devices to share, download, or view attachments in external applications based on roles.
-   **[[active-authentication-android|Keep native apps active during authentication on Android devices]]**  
Use the **preventAppKillOnAuth** property on your ServiceNow instance to help prevent Android devices from killing the mobile app when put to background during login. Use this configuration to allow for a smoother authentication experience by keeping the app active until users complete or cancel the login process.
-   **[[turn-off-zta-banner|Turn off the Zero Trust Access banner on mobile apps]]**  
Learn how to turn off the banner on mobile app screens where Zero Trust Access \(ZTA\) is enabled.
-   **[[pin-timeout|PIN timeout]]**  
Configure the PINIdleTimeout property to define the PIN timeout for different ServiceNow mobile apps. You can use this property to enhance security by controlling how long users are allowed to remain inactive before being required to reenter their PIN.
-   **[[asynchronous-attachment-uploads|Asynchronous attachment uploads]]**  
Set the `AsyncAttachmentsUploadEnabled` mobile property to true to turn on background file uploads in the ServiceNow mobile app.

**Parent Topic:**[[imp-considerations|Considerations before implementation]]

## Related

- [[enable-disable-auto-app-refresh|Turn on or turn off automatic app refresh]]
- [[enable-ext-users-attach-access|Enable external users to access attachments]]
- [[switch-date-time-timezone-utc|Switch the date/time fields between device time zone and UTC]]
- [[config-apps2use-devicedatetimeform|Configure mobile apps to use the date/time format of mobile devices]]
- [[hide-secs-mobcds-recscreen-actstrem|Hide seconds in date/time fields on mobile cards, record screen details pages, or activity streams]]
- [[extend-embedded-web-sessions|Extend embedded web sessions]]
- [[enable-enhanced-barcode-scan|Enable enhanced barcode scanning]]
- [[enable-external-barcode-scanner|Enable barcode scanning with an external scanner]]
- [[mob-attachments-android|Configure different mobile attachment capabilities on Android devices based on user roles]]
- [[active-authentication-android|Keep native apps active during authentication on Android devices]]
- [[turn-off-zta-banner|Turn off the Zero Trust Access banner on mobile apps]]
- [[pin-timeout|PIN timeout]]
- [[asynchronous-attachment-uploads|Asynchronous attachment uploads]]
- [[imp-considerations|Considerations before implementation]]
- [[now-mobile-app|Now Mobile app]]
