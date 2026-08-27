---
title: Universal linking for mobile
description: Mobile universal links enable you to drive users to specific screens within a mobile app, that they would not be able to access via the ServiceNow platform web experience.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/mobile/universal-links-mobile.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Mobile URLs, Configuring the Mobile Platform, Mobile Platform]
tags:
  - mobile
  - now-mobile
  - apps
  - platform
  - type-concept
---

# Universal linking for mobile

Mobile universal links enable you to drive users to specific screens within a mobile app, that they would not be able to access via the ServiceNow platform web experience.

Mobile universal linking is a method to redirect your users from using the ServiceNow platform web experience on their mobile device. Instead it promotes using the faster, more responsive, and location-specific ServiceNow [[mobile-config-navigation|Mobile Platform]] experience via mobile apps. Universal linking works by presenting the user with a web banner at the top of designated screens, while they work within a ServiceNow platform web experience. For the user to proceed, they must select **View** in the banner, where the following occurs:

-   If the user has already installed the required ServiceNow mobile app and is logged in to the instance - then the user is directed to a defined location within the specific mobile app.
-   If the user has already installed the required ServiceNow mobile app and is not logged in to the instance - then the user is required to log in to the instance and is then directed to a defined location within the specified mobile app.
-   If the user has not installed the required ServiceNow mobile app - they are directed to either the Apple Store or Google Play Store, and must download the ServiceNow app. Once the app is downloaded, the user must log in to the instance and is then directed to a defined location within the newly installed app.

After the user taps **View** in the banner, direct them to any [[form-screen|record screen]], form screen, or browser screen within a specified mobile app. For form and record screens, you can direct the user to a specific location based on a defined table.

\[Omitted image "universal-link-on-phone.png"\] Alt text: Universal link shown on phone image.

-   **[[universal-linking-enable|Enable mobile universal linking]]**  
Enable the universal linking option if you want a web banner displayed on specified pages of the ServiceNow platform website. By default the mobile universal linking option is not available in the base system.
-   **[[universal-linking-unsupported|Enable expansion of universal linking to mobile browser \(MESP\) pages]]**  
Enable the expanded universal linking option to display the web banner on mobile browser pages when the user does not have the appropriate mobile app installed. By default this mobile universal linking option is not available in the base system.
-   **[[universal-linking-support-urls|Mobile universal linking for supported URLs]]**  
Use mobile universal linking to display a web banner on specified platform web pages to encourage users to work within a ServiceNow mobile app. Configure the supported URLs that facilitate this functionality to ensure that the banners are displayed on the correct web pages. These URLs also direct users to a defined location within the appropriate mobile app.

**Parent Topic:**[[mobile-urls|Mobile URLs]]

## Related

- [[universal-linking-enable|Enable mobile universal linking]]
- [[universal-linking-unsupported|Enable expansion of universal linking to mobile browser \(MESP\) pages]]
- [[universal-linking-support-urls|Mobile universal linking for supported URLs]]
- [[mobile-urls|Mobile URLs]]
- [[mobile-config-navigation|Mobile Platform]]
- [[form-screen|Record screen]]
