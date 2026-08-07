---
title: "Email Bounce Alert System"
aliases:
  - Email Bounce Alert System
tags:
  - servicenow-dev-program
  - code-snippet
  - email-bounce-alert-system
  - server-side
---

📧 Email Bounce Alert System
📘 Overview

The Email Bounce Alert System automatically detects bounced-back emails in the Junk Mail module and alerts administrators or support teams about affected recipients. It helps identify communication failures quickly and ensures that important client messages aren’t missed due to IP blacklisting or delivery issues.

🧩 Problem Statement

In large organizations, emails sometimes bounce back because of mail server issues, blacklisted IPs, or invalid addresses.
Currently, identifying which users didn’t receive an important message requires manual checking of the Junk Email module, leading to delays in response and potential loss of critical communication.

💡 Solution

This email script automates the detection and notification process.

The email script is called from a Notification configured on the sys_email table.

Email Script:

Extracts affected recipient email addresses from the email body using RegEx pattern matching.

Generates an automatic notification alert listing all affected users.

Provides a direct link to the bounced email record for quick investigation.

Notification settings:

When to send: Record inserted or updated

Inserted checkbox: Marked

Condition: Mailbox is Junk AND Body is not empty

Proper recipient(s) and subject line set in the notification.


🚀 Benefits

⚡ Immediate visibility of bounced or undelivered emails.

🧠 Automated extraction of recipient information — no manual tracking required.

📩 Faster communication recovery, ensuring critical business messages reach the intended audience.

🔗 Direct record access for faster troubleshooting and action.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CallScriptIncludeWithParameters/README|CallScriptIncludeWithParameters]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CheckTableExtension/README|CheckTableExtension]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Create Admin Users/README|Create Admin Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Create Tiny Url with API's/README|Create Tiny Url with API's]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/CreateUpdateCIThroughIRE/README|CreateUpdateCIThroughIRE]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/Custom Relationship/README|Custom Relationship]]
