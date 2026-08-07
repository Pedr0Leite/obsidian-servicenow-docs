---
title: High Assurance for SSO login
description: Establish high assurance session for SSO login using ServiceNow's continuous authentication.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/high-assurance-sso-logins.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [High Assurance, Continuous Authentication \(CA\), Zero Trust Access, Access Management]
tags:
  - platform-security
  - type-concept
---

# High Assurance for SSO login

Establish high assurance session for SSO login using ServiceNow's continuous [[c_Authentication|authentication]].

A high assurance session is a session that requires a user to verify their [[identity-landing|identity]] and authenticate with a specific identity or Identity Providers for a specific time frame.

ServiceNow's [[ca-homepage|continuous authentication \(CA\)]] feature enables you to create [[ca-policies|policies]] that creates a high assurance session to the [[users|users]] who access Personally Identifiable Information \(PII\), sensitive data, or restrict the access to explicit data that you want to protect.

When the user re-authenticates, there's a high assurance session that is established, which provides the ability for the users to access the data protected by the CA administrator based on the CA policy [[sc-configuration|configuration]].

You can create CA policies to verify the users identity and authentication the users to access the data that you've protected. You can configure the CA policy and provide the Identity Providers details in the Identity Providers record to establish high assurance session.

\[Omitted image "ca-tab.png"\] Alt text: Continuous Authentication - tab information

The users who are performing SSO based login \([[c_SAML2.0WebBrowserSSOProfile|SAML]] or OIDC\) and whenever there is an attempt to access the protected data, re-authentication screen is prompted with the same SSO that was used by the user during the initial login.

\[Omitted image "ca-sso-screen.png"\] Alt text: SSO - Screen

After successful SSO authentication, the protected data is displayed to the users for a certain time frame. You can configure the properties to change the time limit based on your requirement. To know more, see [[high-assurance-ca|High Assurance session with Continuous Authentication]].

Performing re-authentication with SSO login \(SAML or OIDC\), creates a high assurance session establishing a secure and trusted connection with the identities \(users\) who are accessing the protected data.

An high assurance session established for the user is limited to the High Assurance session length \(**glide.zta.high\_assurance.session.timeout**\) system property. If the high assurance session time exceeds the property length, the user is prompted for re-authentication or step up authentication.

**Related topics**  


[High Assurance session with Continuous Authentication](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/high-assurance-ca.md)

[[pre-work-ca|Pre-work for Continuous Authentication]]

[[configure-ca|Configuring Continuous Authentication]]

## Related

- [[high-assurance-ca|High Assurance session with Continuous Authentication]]
- [[pre-work-ca|Pre-work for Continuous Authentication]]
- [[configure-ca|Configuring Continuous Authentication]]
- [[c_Authentication|Authentication]]
- [[identity-landing|Identity]]
- [[ca-homepage|Continuous Authentication \(CA\)]]
- [[ca-policies|Policies]]
- [[users|Users]]
- [[sc-configuration|Configuration]]
- [[c_SAML2.0WebBrowserSSOProfile|SAML]]
