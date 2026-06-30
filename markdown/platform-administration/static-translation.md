---
title: Static translation
description: Using static translation, you can customize email notifications for recipients across multiple regions based on their preferred language.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/static-translation.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Multilingual email notifications, Email and SMS notifications, System notifications, Notifications, Configure core features, Administer the ServiceNow AI Platform]
---

# Static translation

Using static translation, you can customize email [[notifications|notifications]] for recipients across multiple regions based on their preferred language.

## About static translation for email notifications

Author localized content for the various content fields on notifications, [[c_EmailTemplates|email templates]], and email layout forms using static translation after activating the [[activate-translation-plugin|translation plugin]].

For static translation, the translation request goes to a translator. The translator provides translations for notification content in different languages.

Not all of the fields on the notification forms are translatable.

|Table name|Translatable fields|
|----------|-------------------|
|Email Notification|Subject, message, message\_html, and message\_text|
|Email Template|Subject, message, message\_html, and message\_text|
|Email Layout|Layout|

**Note:**

-   The static content that needs to be translated in mail scripts must be present inside **gs.getMessage\(\)** and translations for the strings must be available in the Message \[sys\_ui\_message\] table​.

-   You can stop the translation of tokens by creating the **glide.email.outbound.static\_translation.session.language.change.enabled** system property and setting it to false.


## Localization Framework

Use the [Localization Framework settings](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/localization-framework/localization-settings.md) to [[language-picker-ui|request translations]] for the following [[framework-configuration|artifact configurations]]:

-   Email Layout Configuration
-   Email Notification Configuration
-   Email Template Configuration

-   **[[enable-static-translation|Enable static translation]]**  
Enable static translation of notifications for the global application.
-   **[[request-translation-and-send-email-notification|Request a translation for an email notification, template or layout]]**  
Request a translation to send an email in the recipient’s preferred language.

**Parent Topic:**[[c_EmailNotifications|Email and SMS notifications]]

**Related topics**  


[Dynamic translation]()

[Request a translation for an email notification, template or layout](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/request-translation-and-send-email-notification.md)

## Related

- [[activate-translation-plugin|activate translation plugin]]
- [[enable-static-translation|Enable static translation]]
- [[request-translation-and-send-email-notification|Request a translation for an email notification, template or layout]]
- [[c_EmailNotifications|Email and SMS notifications]]
- [[notifications|Notifications]]
- [[c_EmailTemplates|Email templates]]
- [[language-picker-ui|Request translations]]
- [[framework-configuration|Artifact configurations]]
