---
title: Sending email using client credential flow
description: Use the client credential flow to send emails from Microsoft Exchange Online.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/send-email-client-credential-flow.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Advanced email setup, Configure, Email Administration, Notifications, Configure core features, Administer the ServiceNow AI Platform]
---

# Sending email using client credential flow

Use the client credential flow to send emails from Microsoft Exchange Online.

Email account administrators, who are users that have the email\_account\_admin role, can configure ServiceNow AI Platform to send emails from an Microsoft Exchange Online tenant. The email account administrators can use SMTP by authenticating with a client ID and client secret or with certificates.

-   **[[activate-oauth-plugin|Activate OAuth support]]**  
You can activate the Email:OAUTH support for IMAP, Microsoft Graph \(Receiving\), and SMTP plugin \(com.glide.email.oauth\) for [[notifications|Notifications]] if you have the admin role.
-   **[[configure-client-id-secret-email-auth|Configure client credential flow for SMTP OAuth2 using a client id and secret]]**  
Configure [[ia-outbound-email-il|outbound email]] accounts in a ServiceNow instance using a client id and secret.
-   **[[register-oauth-cred-flow|Register an OAuth provider]]**  
Use the information generated during the Microsoft Azure account configuration to [[register-application-oauth-send-msgraph|register an application as an OAuth provider]].
-   **[[config-credential-flow-certificate|Configure client credential flow for SMTP OAuth2 using certificate-based authentication]]**  
Configure an OAuth application profile to authenticate using certificates for outbound email.
-   **[[create-email-account-smtp|Create an email account with SMTP OAuth2.0]]**  
[[t_ConfigureAnEmailAccount|Create an email account]] from Microsoft Exchange Online with SMTP OAuth2.0.

**Parent Topic:**[[c_AlternateEmailConfigurations|Advanced email setup]]

## Related

- [[activate-oauth-plugin|activate oauth plugin]]
- [[configure-client-id-secret-email-auth|Configure client credential flow for SMTP OAuth2 using a client id and secret]]
- [[register-oauth-cred-flow|Register an OAuth provider]]
- [[config-credential-flow-certificate|Configure client credential flow for SMTP OAuth2 using certificate-based authentication]]
- [[create-email-account-smtp|Create an email account with SMTP OAuth2.0]]
- [[c_AlternateEmailConfigurations|Advanced email setup]]
- [[notifications|Notifications]]
- [[ia-outbound-email-il|Outbound email]]
- [[register-application-oauth-send-msgraph|Register an application as an OAuth provider]]
- [[t_ConfigureAnEmailAccount|Create an email account]]
