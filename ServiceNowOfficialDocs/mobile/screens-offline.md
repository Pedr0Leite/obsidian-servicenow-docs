---
title: Supported screens for offline mode
description: Consider which screen types to use in offline mode.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/mobile/screens-offline.html
release: australia
topic_type: reference
last_updated: "2026-05-31"
reading_time_minutes: 1
breadcrumb: [Align apps, screens, and functions, Offline mode setup options, Offline mode, Before implementation, Configuration detail, Configuring the Mobile Platform, Mobile Platform]
tags:
  - mobile
  - now-mobile
  - apps
  - platform
  - type-reference
---

# Supported screens for offline mode

Consider which screen types to use in [[mobile-offline-mode|offline mode]].

## Consider which screen types to use in offline mode

Screens are the building blocks of your mobile experience. Each screen defines what information is shown, what actions are available, and how users navigate between tasks. Screen types are designed for different kinds of action.

|Screen type|Description|
|-----------|-----------|
|List screen|Browse through a list of records, such as incidents, work orders, or approvals. Tap any record to open its details.|
|Record screen|Shows the details of a single record, like a specific work order or task. Read information, view related tasks, add attachments, or post comments from this screen.|
|Input form screen|Fill in information, answer questions, or submit data through input fields, checkboxes, sliders, and more.|
|Launcher screen|Displays shortcuts, [[sg-config-quick-actions|quick actions]], or grouped sections of information.|

## How screens relate to mobile apps and offline mode

Each mobile app has its own configuration. Within that configuration, you decide which screens to include in the app.

Offline mode is supported in the following screens. For more information about screen types in mobile, see [[sg-mobile-applet|Mobile screen types]].

-   [[parameter-input-screen|Input form screen]]
-   [[list-screen|List screen]]
-   [[map-screen|Map screen]]
-   [[calendar-screen|Calendar screen]]
-   [[form-screen|Record screen]]

    The following screen segments are available within the record screen:

    -   Sections screen
    -   Related list screen
    -   Details screen
    -   Activity stream screen

-   **[[setup-screens-offline|Setup screens for offline mode]]**  
Setup ofﬂine mode for your mobile screen so that users can work without an internet connection.
-   **[[config-offline-data-item|Configure data items in offline mode]]**  
Define a separate data item for offline mode, giving you the flexibility to define the amount of data to display when a user is offline.
-   **[[config-offline-record-number|Define the number of displayed records in offline mode]]**  
Define the number of records to display to users in offline mode. Choose between 0 through 1000 records. This range gives you the flexibility to display different amounts to the user in online and offline modes.

**Parent Topic:**[[align-app-screen-function|Set up and align the app, screen, and function hierarchy for offline mode]]

## Related

- [[sg-mobile-applet|Mobile screen types]]
- [[setup-screens-offline|Setup screens for offline mode]]
- [[config-offline-data-item|Configure data items in offline mode]]
- [[config-offline-record-number|Define the number of displayed records in offline mode]]
- [[align-app-screen-function|Set up and align the app, screen, and function hierarchy for offline mode]]
- [[mobile-offline-mode|Offline mode]]
- [[sg-config-quick-actions|Quick actions]]
- [[parameter-input-screen|Input form screen]]
- [[list-screen|List screen]]
- [[map-screen|Map screen]]
- [[calendar-screen|Calendar screen]]
- [[form-screen|Record screen]]
