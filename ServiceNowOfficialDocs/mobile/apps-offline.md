---
title: ServiceNow mobile applications for offline mode
description: Consider which native applications are available in offline mode. The available apps are Mobile Agent app, Now Mobile app or a custom branded app created through the Mobile Publishing plugin.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/mobile/apps-offline.html
release: australia
topic_type: concept
last_updated: "2026-05-31"
reading_time_minutes: 1
breadcrumb: [Align apps, screens, and functions, Offline mode setup options, Offline mode, Before implementation, Configuration detail, Configuring the Mobile Platform, Mobile Platform]
tags:
  - mobile
  - now-mobile
  - apps
  - platform
  - type-concept
---

# ServiceNow mobile applications for offline mode

Consider which native applications are available in [[mobile-offline-mode|offline mode]]. The available apps are [[mobile-experience|Mobile Agent app]], [[now-mobile-app|Now Mobile app]] or a custom branded app created through the Mobile Publishing plugin.

Deciding which mobile apps support offline mode determines the foundation from which screens and functions inherit their offline behavior. Supporting offline mode at the app level allows for a consistent user experience.

**Note:**

-   Offline mode must be enabled at the app level for any screens or functions configured as offline to be available to users without network connectivity.
-   Setting the app as available offline does not automatically enable all offline flows, as every screen and function involved must also be configured as available offline.

The ServiceNow [[mobile-config-navigation|Mobile Platform]] suite includes two mobile apps, **Mobile Agent** and **Now Mobile**, as well as the ability to create custom app types tailored to specific business needs. This is known as Mobile Branding or Mobile Publishing. For more information, see [[mobile-publishing|Publish mobile apps with custom branding]].

At the app level, administrators define how the mobile app \(also known as native client\) behaves, including its navigation structure, user access rules, theme and branding, and other core settings. One key configuration at this level determines whether the entire app experience is available for offline use.

## How applications \(native clients\) relate to mobile apps and offline mode

The offline capability defined at the app \(native client\) level determines whether the app type Mobile Agent, Now Mobile, or custom, can function without network connectivity. All screens and functions configured as available offline within this app inherit these settings, ensuring a seamless and consistent experience across both online and offline modes, including shared navigation tabs, layouts, and UI sections.

-   **[[setup-mobile-offline|Set up offline mode for mobile apps]]**  
Setup offline mode for your mobile applications so that users can work without an internet connection.

**Parent Topic:**[[align-app-screen-function|Set up and align the app, screen, and function hierarchy for offline mode]]

## Related

- [[mobile-publishing|Publish mobile apps with custom branding]]
- [[setup-mobile-offline|Set up offline mode for mobile apps]]
- [[align-app-screen-function|Set up and align the app, screen, and function hierarchy for offline mode]]
- [[mobile-offline-mode|Offline mode]]
- [[mobile-experience|Mobile Agent app]]
- [[now-mobile-app|Now Mobile app]]
- [[mobile-config-navigation|Mobile Platform]]
