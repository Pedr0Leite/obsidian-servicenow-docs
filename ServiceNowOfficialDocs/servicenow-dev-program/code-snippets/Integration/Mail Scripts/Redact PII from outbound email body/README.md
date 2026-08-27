---
title: "Redact PII from outbound email body"
aliases:
  - Redact PII from outbound email body
tags:
  - servicenow-dev-program
  - code-snippet
  - redact-pii-from-outbound-email-body
  - mail-scripts
---

# Redact PII from outbound email body

## What this solves
Notifications sometimes leak personal data into emails. This mail script replaces common identifiers in the email body with redacted tokens before send.

## Where to use
Notification or Email Script record, Advanced view, "Mail script" field. Invoke the function to get a safe body string and print it.

## How it works
- Applies regex patterns to the email text for emails, phone numbers, IP addresses, NI number style patterns, and 16-digit card-like numbers
- Replaces matches with descriptive placeholders
- Leaves HTML tags intact by operating on the plain text portion you pass in

## Configure
- Extend or tighten patterns for your organisation
- Toggle specific scrubs on or off in the config block

## References
- Email Scripts  
  https://www.servicenow.com/docs/bundle/zurich-platform-administration/page/administer/notification/reference/email-scripts.html
- Notifications  
  https://www.servicenow.com/docs/bundle/zurich-platform-administration/page/administer/notification/concept/c_EmailNotifications.html

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Add Checklist/README|Add Checklist]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Add HTML Table for Requested Item Variables/README|Add HTML Table for Requested Item Variables]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Add Users in Watchlist to CC/README|Add Users in Watchlist to CC]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Add a link which opens ticket in Service Portal/README|Add a link which opens ticket in Service Portal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Call Script Include in Notification Mail Script/README|Call Script Include in Notification Mail Script]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Mail Scripts/Call UI Message or System Property in Notification Mail Script/README|Call UI Message or System Property in Notification Mail Script]]
