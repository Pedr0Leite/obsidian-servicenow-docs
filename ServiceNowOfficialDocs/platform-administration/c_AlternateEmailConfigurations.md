---
title: Advanced email setup
description: With an advanced email setup, you can use your own SMTP server, POP3 server, or both.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/c\_AlternateEmailConfigurations.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure, Email Administration, Notifications, Configure core features, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - type-concept
---

# Advanced email setup

With an advanced email setup, you can use your own SMTP server, POP3 server, or both.

Setting up your own email environment can be useful if you want to use existing filtering, retention, or compliance aspects of your internal email architecture. You can set up email in several ways:

-   Use your own SMTP server to forward email to ServiceNow servers.
-   Use your own SMTP server to send email.
-   Use your own POP3 server to receive email.
-   Use your own SMTP and POP3 servers to send and receive email.
-   Use an OAuth 2.0-enabled SMTP server to send email from a third-party service.
-   Use an OAuth 2.0-enabled IMAP server to receive email from a third-party service.

The following procedures assume that you [[t_ConfiguringStandardEmail|enabled basic email properties]].

-   **[[t_ConfAltEmailUsgOwnSMTP|Enable using your own SMTP server]]**  
Enable using your own SMTP server so that you can leverage the existing filtering, retention, or compliance aspects of your own SMTP server while also using the ServiceNow POP3 server.
-   **[[t_ConfAltEmailConfPOP3Server|Enable using your own POP3 server]]**  
You can use your own POP3 server to store and receive email for the instance.
-   **[[t_ConfAltEmailConfServers|Enable using your own SMTP and POP3 servers]]**  
You can use your own SMTP and POP3 servers to send email from the instance and to store and receive email for the instance.
-   **[[email-bounce|Email bounce management]]**  
Help prevent sending emails to addresses that are known to generate bounces by monitoring and filtering them out while sending emails.
-   **[[c_OAuthEmailAuthentication|OAuth email authentication]]**  
OAuth enables your instance to receive and send email through a third-party email account.
-   **[[system-address-filters|System address filters]]**  
Prevent your system from communicating with untrusted domains and email addresses.
-   **[[read-send-emails-ms-graph|Read or send emails using Microsoft Graph]]**  
Use Microsoft Graph endpoints to read or send emails from Microsoft Exchange Online.
-   **[[send-email-client-credential-flow|Sending email using client credential flow]]**  
Use the client credential flow to send emails from Microsoft Exchange Online.
-   **[[personal-corporate-mailbox|Personal corporate mailbox]]**  
Enables sales agents to integrate their personal corporate mail boxes to send and receive emails.

**Parent Topic:**[[configuring-email-admin|Configure email administration]]

## Related

- [[t_ConfiguringStandardEmail|Enable basic email]]
- [[t_ConfAltEmailUsgOwnSMTP|Enable using your own SMTP server]]
- [[t_ConfAltEmailConfPOP3Server|Enable using your own POP3 server]]
- [[t_ConfAltEmailConfServers|Enable using your own SMTP and POP3 servers]]
- [[email-bounce|Email bounce management]]
- [[c_OAuthEmailAuthentication|OAuth email authentication]]
- [[system-address-filters|System address filters]]
- [[read-send-emails-ms-graph|Read or send emails using Microsoft Graph]]
- [[send-email-client-credential-flow|Sending email using client credential flow]]
- [[personal-corporate-mailbox|Personal corporate mailbox]]
- [[configuring-email-admin|Configure email administration]]
