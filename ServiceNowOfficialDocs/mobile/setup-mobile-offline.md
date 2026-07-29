---
title: Set up offline mode for mobile apps
description: Setup offline mode for your mobile applications so that users can work without an internet connection.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/mobile/setup-mobile-offline.html
release: australia
topic_type: task
last_updated: "2026-06-09"
reading_time_minutes: 1
breadcrumb: [Offline mobile apps, Align apps, screens, and functions, Offline mode setup options, Offline mode, Before implementation, Configuration detail, Configuring the Mobile Platform, Mobile Platform]
tags:
  - mobile
  - now-mobile
  - apps
  - platform
  - type-task
---

# Set up offline mode for mobile apps

Setup [[mobile-offline-mode|offline mode]] for your mobile applications so that users can work without an internet connection.

## Before you begin

Role required: mobile\_admin, admin

## About this task

Decide which mobile apps support offline mode to set the foundation for the entire offline experience. The offline capability defined at the app level, whether for the [[mobile-experience|Mobile Agent app]], [[now-mobile-app|Now Mobile app]], or a custom apps, determine whether that app can function without network connectivity. All screens and functions configured as offline within the app inherit this setting, ensuring a consistent experience across navigation tabs, layouts, and UI sections.

**Note:** Offline mode must be enabled at the app level for any screens or functions configured as offline to be available to users without network connectivity.

## Procedure

1.  Navigate to **All** &gt; **System Mobile** &gt; **[[mab-concept|Mobile App Builder]]**.

    The Mobile App Builder opens in a new browser tab and displays the application scope selection screen.

2.  Search for the application scope you are working in and then select the name of the application scope.

    The [[mab-menu-screen|Mobile App Builder categories home screen]] displays.

3.  Select **Mobile app configs**, and then select the mobile app record you wish to configure offline mode in.

4.  Under **Mobile push application**, select which app type the offline scheduled download should be associated with.

    For more information, see [[scheduled-offline-caching|Configure scheduled offline caching]].

5.  Under **Settings**, select **Offline enabled**.

6.  Select **Save**.


**Parent Topic:**[[apps-offline|ServiceNow mobile applications for offline mode]]

## Related

- [[scheduled-offline-caching|Configure scheduled offline caching]]
- [[apps-offline|ServiceNow mobile applications for offline mode]]
- [[mobile-offline-mode|Offline mode]]
- [[mobile-experience|Mobile Agent app]]
- [[now-mobile-app|Now Mobile app]]
- [[mab-concept|Mobile App Builder]]
- [[mab-menu-screen|Mobile App Builder categories home screen]]
