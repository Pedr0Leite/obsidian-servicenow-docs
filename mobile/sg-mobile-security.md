---
title: Device security for ServiceNow Mobile apps
description: This document applies to current ServiceNow apps for iOS and Android for Australia. This document may be subject to change for future mobile releases.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/mobile/sg-mobile-security.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Mobile security, Configuring the Mobile Platform, Mobile Platform]
---

# Device security for ServiceNow Mobile apps

This document applies to current ServiceNow apps for iOS and Android for Australia. This document may be subject to change for future mobile releases.

-   **[[sg-mobile-security-components-architecture|Components and architecture]]**  
The ServiceNow mobile apps consist of the ServiceNow server instance and native apps for iOS and Android. The apps use fully native code and are not a hybrid approach. The mobile client applications communicate over a wireless connection with the server and pull live data for the end user.
-   **[[sg-mobile-ID-access-mgmt|Identity and access management]]**  
Learn about user authentication, third party authentication, and user session termination for mobile applications.
-   **[[sg-security-mobile-data-flow|Mobile data flow for ServiceNow mobile apps]]**  
Data can be retrieved, downloaded from, and written back to a mobile device.
-   **[[sg-mobile-security-app-distro|Internal mobile app distribution]]**  
Internal distribution of ServiceNow mobile apps is supported through all major EMM vendors.
-   **[[sg-mobile-security-data|Data security for ServiceNow mobile apps]]**  
ServiceNow mobile apps use SSL/TLS for Over-the-Air \(OTA\) communication encryption for data security. The OAuth authorization endpoints are HTTPS.
-   **[[sg-mobile-security-push-notif|Push notifications]]**  
Administrators create push notifications and users are able to receive them.
-   **[[sg-mobile-security-practices|Mobile security practices]]**  
Mobile security practices include mobile-specific system properties, attachment control, password reinforcement, [[sg-mobile-security-patching|security patching]], and controlling [[sg-mobile-security-shared-data|shared data]].
-   **[[sg-edge-encryption|Edge Encryption for ServiceNow mobile]]**  
Users can view and edit data protected with Edge Encryption within their mobile device. The data appears in readable form on the mobile device but is encrypted in the database.

## Related

- [[sg-mobile-security-components-architecture|Components and architecture]]
- [[sg-mobile-ID-access-mgmt|Identity and access management]]
- [[sg-security-mobile-data-flow|Mobile data flow for ServiceNow mobile apps]]
- [[sg-mobile-security-app-distro|Internal mobile app distribution]]
- [[sg-mobile-security-data|Data security for ServiceNow mobile apps]]
- [[sg-mobile-security-push-notif|Push notifications]]
- [[sg-mobile-security-practices|Mobile security practices]]
- [[sg-edge-encryption|Edge Encryption for ServiceNow mobile]]
- [[sg-mobile-security-patching|Security patching]]
- [[sg-mobile-security-shared-data|Shared data]]
