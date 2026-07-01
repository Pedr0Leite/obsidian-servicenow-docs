---
title: Dynamic translation
description: Using dynamic translation, you can customize email notifications automatically for users across multiple regions based on their preferred language.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/dynamic-translation.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Multilingual email notifications, Email and SMS notifications, System notifications, Notifications, Configure core features, Administer the ServiceNow AI Platform]
---

# Dynamic translation

Using dynamic translation, you can customize email [[notifications|notifications]] automatically for users across multiple regions based on their preferred language.

## About dynamic translation for email notifications

Dynamic content notifications are user-specific. You can use dynamic translation to translate notifications automatically based on the language selected by the recipient.

For example, a requester whose language is set to French will automatically receive notification emails in French, while a Spanish requester would be notified in Spanish.

Using dynamic translation involves the following tasks:

1.  [Activate Dynamic Translation](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/dynamic-translation/activate-dynamic-translation.md)
2.  [[enable-email-notification-translation|Set system property for dynamic translation]]
3.  [[enable-dynamic-translation|Enable dynamic translation]]

After dynamic translation is enabled, you can send emails and view or preview the translated email in the preferred languages of the recipients by accessing the **Translated Email Contents** tab.

**Note:** The language preference of users mentioned in **cc** and **bcc** fields is not considered.

-   **[Enable dynamic translation](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/enable-email-notification-translation.md)**  
Enable dynamic translation of notifications for the instance.
-   **[[config-email-notification-banner|Configure the note banner for translated emails]]**  
Configure the content for a translated email note banner displayed at the top of the page to display a customized message to the recipient.
-   **[Enable dynamic translation for email notifications](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/enable-dynamic-translation.md)**  
Enable dynamic translation for a notification to send dynamically translated emails to recipients in their preferred language.

**Parent Topic:**[[c_EmailNotifications|Email and SMS notifications]]

**Related topics**  


[Static translation]()

## Related

- [[enable-email-notification-translation|Enable dynamic translation]]
- [[enable-dynamic-translation|Enable dynamic translation for email notifications]]
- [[config-email-notification-banner|Configure the note banner for translated emails]]
- [[c_EmailNotifications|Email and SMS notifications]]
- [[notifications|Notifications]]
