---
title: Sensitive data redaction
description: Redact sensitive data such as Social Security number, credit card details, email address, phone number, and other personal information from inbound emails to help protect data and privacy.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/sensitive-data-redaction.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Use, Inbound email, Notifications, Configure core features, Administer the ServiceNow AI Platform]
---

# Sensitive data redaction

Redact sensitive data such as Social Security number, credit card details, email address, phone number, and other personal information from inbound emails to help protect data and privacy.

When an [[ia-inbound-email-il|inbound email]] is received, the sensitive data is masked. The sensitive data is redacted from the body, body\_text, subject in the \[sys\_email\] table after flows and inbound actions are executed.

**Note:** Data that has been redacted can’t be recovered.

Redact sensitive data option is available in [[actions-inbound-email|inbound email actions]] once the following is activated:

-   [[activate-data-redaction-emails-plugin|Sensitive Data Redaction for Inbound Emails plugin]]
-   [Data Discovery application](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/activate-data-discovery.md)

    **Note:** Data Discovery application does not require a paid subscription when used along with sensitive data redaction for inbound emails plugin.


To create inbound email actions, see [[t_CreatingAnInboundEmailAction|Create an inbound email action]].

Redaction time for the record can be viewed by checking the **Email Log**. For more information, see [System email log and mailboxes](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/r_EmailLogs.md).

-   **[Activate sensitive data redaction for inbound emails plugin](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/activate-data-redaction-emails-plugin.md)**  
You can activate the Sensitive Data Redaction for Inbound Emails plugin \(com.glide.email\_inbound.redaction\) for [[notifications|Notifications]] if you have the admin role. The application installs related plugins if they are not already installed.
-   **[[customize-data-redaction|Customize behavior for sensitive data redaction]]**  
Customize sensitive data redaction behavior by creating [[r_SetArchiveRuleProcessingBehavior|system properties]] for flows that are triggered by inbound emails, sys\_email record, and inbound actions.

**Parent Topic:**[[use-inbound-email-action|Use Inbound email actions]]

## Related

- [[activate-data-redaction-emails-plugin|Activate sensitive data redaction for inbound emails plugin]]
- [[t_CreatingAnInboundEmailAction|Create an inbound email action]]
- [[customize-data-redaction|Customize behavior for sensitive data redaction]]
- [[use-inbound-email-action|Use Inbound email actions]]
- [[ia-inbound-email-il|Inbound email]]
- [[actions-inbound-email|Inbound email actions]]
- [[notifications|Notifications]]
- [[r_SetArchiveRuleProcessingBehavior|System properties]]
