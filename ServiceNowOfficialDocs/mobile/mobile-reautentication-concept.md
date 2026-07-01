---
title: Configure mobile re-authentication system properties
description: Set mobile re-authentication system properties so users must re-authenticate their login credentials when performing specific actions.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/mobile/mobile-reautentication-concept.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [System properties, Before implementation, Configuration detail, Configuring the Mobile Platform, Mobile Platform]
tags:
  - mobile
  - now-mobile
  - apps
  - platform
  - type-concept
---

# Configure mobile re-authentication system properties

Set mobile re-authentication system properties so users must re-authenticate their login credentials when performing specific actions.

To activate the re-authentication option, select `Re-authentication` in the **Preconditions** field within the [[mobile-actions|Action functions]] table. See, [[sg-studio-config-action-function|Configure an action function]].

-   **[[mobile-reauthentication-login-method|Configure mobile re-authentication login method]]**  
Define the re-authentication method to be either single sign-on \(SSO\) or local login, depending on your security requirements.
-   **[[mobile-reauthentication-login-sso|Configure mobile re-authentication SSO login]]**  
Define which identity provider to use for the SSO login. If this property is not defined, the system reuses the default identity provider used for a regular login.
-   **[[mobile-reauthentication-logout|Configure mobile re-authentication logout option]]**  
Configure this parameter to force your users to log out each time before they re-authenticate.
-   **[[mobile-reauthentication-usage-token|Configure mobile re-authentication for single or multiple use]]**  
Define whether each mobile action requires re-authentication. Alternatively, define whether the user can perform multiple actions without the need to re-authenticate each time.
-   **[[mobile-reauthentication-token-lifespan|Configure mobile re-authentication login timespan]]**  
Define a time period in seconds that a user is not required to re-authenticate themselves. This parameter only applies when a user has permission to re-authenticate multiple times.

**Parent Topic:**[[additional-mobile-configuration|Mobile system property configurations]]

## Related

- [[sg-studio-config-action-function|Configure an action function]]
- [[mobile-reauthentication-login-method|Configure mobile re-authentication login method]]
- [[mobile-reauthentication-login-sso|Configure mobile re-authentication SSO login]]
- [[mobile-reauthentication-logout|Configure mobile re-authentication logout option]]
- [[mobile-reauthentication-usage-token|Configure mobile re-authentication for single or multiple use]]
- [[mobile-reauthentication-token-lifespan|Configure mobile re-authentication login timespan]]
- [[additional-mobile-configuration|Mobile system property configurations]]
- [[mobile-actions|Action functions]]
