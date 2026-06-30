---
title: Configuring Code Signing
description: Activate and configure Code Signing to verify the authenticity and integrity of your data.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/config-code-signing.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Code Signing, Platform Security]
---

# Configuring Code Signing

Activate and configure [[code-signing-landing|Code Signing]] to verify the authenticity and integrity of your data.

\[Omitted image "cse-process.png"\] Alt text: Overall process for [[code-signing-configuration|Code Signing configuration]]

Code Signing Enterprise requires an initial trust relationship between trusted and protected instances that helps to prevent any unauthorized user with any authorization level from accessing unapproved activities.

Refer to each topic to complete the [[sc-configuration|configuration]] steps to establish the Circle of Trust with Code Signing Enterprise:

-   **[[cse-assign-roles|Assign the Code Signing Administrator Role]]**

    Assign the Code Signing Administrator role to a user to access the Code Signing configuration experience.

-   **[[cse-turn-on-cse|Configure Code Signing Enterprise on your trusted instance]]**

    [[enable-codesiging|Turn on Code Signing]] on your trusted instance.

-   **[[cse-upload-cs-config|Upload your Code Signing configuration file to your protected instance]]**

    Upload the configuration file generated on your trusted instance.

-   **[[cse-ppi-config|Configure Code Signing Enterprise on your protected instance]]**

    Turn on and configure Code Signing on your protected instance.

-   **[[cse-turn-on-cert-validation|Turn on certificate validation]]**

    Turn on certificate validation on your instance.

-   **[[cse-turn-off-cse|Turn off Code Signing]]**

    Disable code signing on your protected instance.

    **Note:** This optional step isn’t part of the initial configuration for Code Signing

## Related

- [[cse-assign-roles|Assign the Code Signing Administrator Role]]
- [[cse-turn-on-cse|Configure Code Signing Enterprise on your trusted instance]]
- [[cse-upload-cs-config|Upload your Code Signing configuration file to your protected instance]]
- [[cse-ppi-config|Configure Code Signing Enterprise on your protected instance]]
- [[cse-turn-on-cert-validation|Turn on certificate validation]]
- [[cse-turn-off-cse|Turn off Code Signing]]
- [[code-signing-landing|Code Signing]]
- [[code-signing-configuration|Code Signing Configuration]]
- [[sc-configuration|Configuration]]
- [[enable-codesiging|Turn on Code Signing]]
