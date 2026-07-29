---
title: "After overriding the \"From\" in a notification the resulting email still shows the \"Email user label\" from SMTP Email Account and the overridden email"
aliases:
  - KB0780972
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0780972
kb_number: KB0780972
last_modified: 2024-04-08
---

## After overriding the "From" in a notification the resulting email still shows the "Email user label" from SMTP Email Account and the overridden email

  

### Issue

After updating the "From" and "Reply To" field in the 'what will it contain' tab to a different email address, the email notification in sent mailbox has the "Email user label" from Email Account for SMTP and the overridden email address.

Example:

Email Account for SMTP has:

Email user label: IT Service Desk

From: <instance>@service-now.com

In the Notifications "What it will contain" tab, we have:

From: [test@example.com](mailto:test@example.com)

Reply-To: [test@example.com](mailto:test@example.com)

The resulting email will have:

From: IT Service Desk< [test@example.com](mailto:test@example.com)\>

Reply-To: IT Service Desk< [test@example.com](mailto:test@example.com)\>

### Cause

This is because in the Email Account for SMTP you have the "Email user label" set as 'IT Service Desk'  
and in the Notification you are overriding just the email with< [test@example.com](mailto:test@example.com)\>

### Resolution

  
To override the label as well, please update the "From" and the Reply-To in the notification with the Label <email address>

In the example above it will be:

IT Service Desk <test@example.com>
