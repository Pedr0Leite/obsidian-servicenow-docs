---
title: Email service
description: The Email Service API provides endpoint to install the Email API on the instance.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/email-service.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Create, Email Administration, Notifications, Configure core features, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - type-concept
---

# Email service

The Email Service API provides endpoint to install the Email API on the instance.

By default, Email Service only allows admin users to access the [Email API](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/email-api.md). Administrators can [[grant-access-to-email-api|grant access to the Email API]] by:

1.  Adding an access control for creating records in the Email \[sys\_email\] table linked to the email\_api\_send role.
2.  Assigning the email\_api\_send role to the non-admin user.
3.  Verifying the non-admin user has read access to the notification target table. For example, an email notification for an incident, requires read access to the Incident table.

Non-admin users with the email\_api\_send role can access the Email API from the [REST API Explorer](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/use-REST-API-Explorer.md).

-   **[[create-system-address-filter|Create a system address filter]]**  
Define how email address filters apply to inbound and [[ia-outbound-email-il|outbound email]].

**Parent Topic:**[[using-email-admin|Creating an email account]]

## Related

- [[grant-access-to-email-api|Grant access to the Email API]]
- [[create-system-address-filter|Create a system address filter]]
- [[using-email-admin|Creating an email account]]
- [[ia-outbound-email-il|Outbound email]]
