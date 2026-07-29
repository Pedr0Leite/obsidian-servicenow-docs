---
title: "Only ServiceNow Mail Servers are allowed to send emails for \"service-now.com\" domain"
aliases:
  - KB0725655
tags:
  - servicenow
  - support-kb
  - email
  - spf
  - dns
  - mail-servers
  - security
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725655
kb_number: KB0725655
last_modified: 2025-12-17
---

## Only ServiceNow Mail Servers are allowed to send emails for "service-now.com" domain

  

### Issue

Some cases would like to allow-list external email servers to use the service-now domain and request to add them to domain SPF records.

### Release

All

### Resolution

Only ServiceNow email servers will be allowed to send emails from @service-now.com and this will not change.

There is an option of using external email servers and configure them in the instances. However, you will need to use your own domain for those emails instead of using the @service-now.com domain.

## Related

- [[KB0743094 - How to confirm ServiceNow email server is using Opportunistic TLS]] - related outbound mail server configuration
- [[KB0745172 - Identify the source of emails sent from ServiceNow]] - tracing where an email originated
- [[KB0538106 - Confirming that your email is RFC compliant]] - email deliverability troubleshooting
- [[KB0528658 - Verifying the outbound mail server received the email]] - outbound mail server verification

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0743094 - How to confirm ServiceNow email server is using Opportunistic TLS|How to confirm ServiceNow email server is using Opportunistic TLS]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow|How Access Control List (ACL) evaluation works in ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0656366 - Relationship between Business Rules and Access Control Rules (ACLs)|Relationship between Business Rules and Access Control Rules (ACLs)]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0686244 - When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window show|When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window shows an error Failed API level ACL Validation]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0687701 - Admin user is being asked to elevate to admin role after logging in|Admin user is being asked to elevate to \"admin\" role after logging in]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0691876 - Mutual Authentication Overview|Mutual Authentication: Overview]]
