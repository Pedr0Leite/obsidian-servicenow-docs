---
title: Security and compliance in offline mode
description: Learn how to manage offline mode access and determine which users can use it, helping to secure sensitive data.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/mobile/security-offline.html
release: australia
topic_type: concept
last_updated: "2026-06-01"
reading_time_minutes: 1
breadcrumb: [Offline mode setup options, Offline mode, Before implementation, Configuration detail, Configuring the Mobile Platform, Mobile Platform]
tags:
  - mobile
  - now-mobile
  - apps
  - platform
  - type-concept
---

# Security and compliance in offline mode

Learn how to manage [[mobile-offline-mode|offline mode]] access and determine which users can use it, helping to secure sensitive data.

Offline mode stores data locally on the device. Configure offline rules to align data access with your security requirements. Use the glide.sg.offline.roles system property to restrict offline access to users who require it, limiting the amount of sensitive data stored on devices in the field.

The following system properties are available when managing attachments in offline mode:

|Property|Description|
|--------|-----------|
|glide.sg.ofﬂine.roles|A comma-separated list of role names that are allowed to work in ofﬂine mode.|
|glide.sg.ofﬂine.expiration|Defines how long an offline cache remains valid on the device.|

For more information on these and other related offline system properties, see [[mobile-system-properties|System properties in offline mode]].

-   **[[general-guidelines-offline-security|General guidelines for offline mode security and compliance]]**  
When working offline mode, keep these security and compliance general guidelines in mind for usability and a good user experience.

**Parent Topic:**[[offline-setup-options|Offline mode setup options]]

## Related

- [[mobile-system-properties|System properties in offline mode]]
- [[general-guidelines-offline-security|General guidelines for offline mode security and compliance]]
- [[offline-setup-options|Offline mode setup options]]
- [[mobile-offline-mode|Offline mode]]
