---
title: Mobile system property configurations
description: Several system properties are available for you to further configure the mobile app. For example, use system properties to require a PIN, hide the image on the app homepage, configure the blur in background option, or disable sharing attachments from the mobile app.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/mobile/additional-mobile-configuration.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Before implementation, Configuration detail, Configuring the Mobile Platform, Mobile Platform]
---

# Mobile system property configurations

Several system properties are available for you to further configure the mobile app. For example, use system properties to require a PIN, hide the image on the app homepage, configure the blur in background option, or disable sharing attachments from the mobile app.

-   **[[require-app-pin|Require an app PIN for the mobile app]]**  
Require users to enter a PIN when the application has been inactive for five minutes. To require the mobile user to set and enter a local application PIN, add the system property **glide.sg.require\_mobile\_application\_pin**.
-   **[[mobile-reautentication-concept|Configure mobile re-authentication system properties]]**  
Set mobile re-authentication system properties so users must re-authenticate their login credentials when performing specific actions.
-   **[[t_BlurApp|Configure the blur app option to improve security]]**  
As a security feature, administrators can configure the mobile app to blur or appear blackened, depending on the operating system, when not in focus on a mobile device. When you double-click the home button on your mobile device to close apps or navigate back to where you left off, the ServiceNow app appears blurred or blackened.
-   **[[configure-rooted-jailbroken-devices|Configure the status for rooted and jailbroken devices]]**  
Define whether jailbroken \(iOS\) and rooted \(Android\) devices are permitted on your mobile device. The default value is set to `false` to increase security and to minimize possible disruption to your system.
-   **[[configure-copy-paste|Configure the mobile app to clear the copy/paste clipboard and block ability to share content]]**  
To have the mobile app clear the pasteboard when the app enters the background, as well as block the ability to share content, add the system property **glide.sg.clear\_pasteboard\_when\_backgrounded**.
-   **[[configure-data-item-row-count|Configure the maximum number of records returned for data items]]**  
To set the maximum number of rows retrieved for the table defined in the data item, add the system property **glide.sg.data\_item.row\_count**.
-   **[[configure-pagination-size|Configure pagination size for search lists]]**  
To configure the amount of search list results that load to the screen as the user scrolls down, add the system property **glide.sg.choice\_list.window\_size**.
-   **[[configure-max-ui-param|Configure the maximum number of records returned for list UI parameters]]**  
To configure the maximum number of records returned for a list of parameters, add the system property **glide.sg.list.max\_items\_number**.
-   **[[set-default-missing-image|Configure a placeholder image for missing images in mobile apps]]**  
You can specify an image on your instance as a placeholder for missing images. This image appears in your mobile apps when a record has an image field with an empty value, such as a user avatar or catalog item. You can select a different image to use for each table on your instance.
-   **[[mobile-allow-deeplink|Configure which external apps are available for deep linking]]**  
Administrators can define which external apps can be used in deep links with the **glide.sg.allowed\_external\_deeplinks** property.
-   **[[block-users-download-shar-attach|Block users from downloading or sharing attachments]]**  
Set the **glide.sg.block\_mobile\_attachments\_sharing** system property to `true` to hide the sharing button in the mobile app native viewer.
-   **[[config-grp-acl-4-aggreg-req|Configure group ACL for aggregation requests]]**  
Use the **glide.sg.group\_acl.enabled** system property to control the validation of access control lists \(ACL\) during aggregation requests that are related to displaying results from [[sg-data-item|data items]] that use grouping.
-   **[[vu-attach-extapp-android|Control whether users can view attachments in external applications on Android devices]]**  
Set the **glide.sg.block\_mobile\_attachments\_external\_viewing** system property to true to prevent Android users from opening attachments in third-party applications.

**Parent Topic:**[[imp-considerations|Considerations before implementation]]

## Related

- [[require-app-pin|Require an app PIN for the mobile app]]
- [[mobile-reautentication-concept|Configure mobile re-authentication system properties]]
- [[t_BlurApp|Configure the blur app option to improve security]]
- [[configure-rooted-jailbroken-devices|Configure the status for rooted and jailbroken devices]]
- [[configure-copy-paste|Configure the mobile app to clear the copy/paste clipboard and block ability to share content]]
- [[configure-data-item-row-count|Configure the maximum number of records returned for data items]]
- [[configure-pagination-size|Configure pagination size for search lists]]
- [[configure-max-ui-param|Configure the maximum number of records returned for list UI parameters]]
- [[set-default-missing-image|Configure a placeholder image for missing images in mobile apps]]
- [[mobile-allow-deeplink|Configure which external apps are available for deep linking]]
- [[block-users-download-shar-attach|Block users from downloading or sharing attachments]]
- [[config-grp-acl-4-aggreg-req|Configure group ACL for aggregation requests]]
- [[vu-attach-extapp-android|Control whether users can view attachments in external applications on Android devices]]
- [[imp-considerations|Considerations before implementation]]
- [[sg-data-item|Data items]]
