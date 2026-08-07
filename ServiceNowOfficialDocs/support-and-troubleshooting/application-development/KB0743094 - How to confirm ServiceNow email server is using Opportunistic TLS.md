---
title: "How to confirm ServiceNow email server is using Opportunistic TLS"
aliases:
  - KB0743094
tags:
  - servicenow
  - support-kb
  - email
  - tls
  - smtp
  - security
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743094
kb_number: KB0743094
last_modified: 2025-10-01
---

## How to confirm ServiceNow email server is using Opportunistic TLS

  

### Issue

How to confirm ServiceNow email servers are using Opportunistic TLS

### Release

All versions

### Resolution

From external network we can confirm that ServiceNow email servers are accepting TLS connection by sending **ehlo** message to one of our inbound MX records.

    ![](/sys_attachment.do?sys_id=d156e408db7dd918e515c223059619af)

Alternately, go to public websites as below and enter the domain i.e. **service-now.com** to check the same:

[https://luxsci.com/smtp-tls-checker](https://luxsci.com/smtp-tls-checker) (This is a third-party page, not sponsored or supported by ServiceNow.)

## Related

- [[KB0725655 - Only ServiceNow Mail Servers are allowed to send emails for service-now.com domain]] - related outbound email server behavior
- [[KB0538106 - Confirming that your email is RFC compliant]] - email deliverability troubleshooting

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0695182 - Using DKIM for Emails from the service-now.com Domain|Using DKIM for Emails from the service-now.com Domain]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0722504 - Using ServiceNow blackhole or dummy email addresses|Using ServiceNow blackhole or dummy email addresses]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0724199 - Localhost and loopback IPs are not allowed in SMTP accounts|Localhost and loopback IPs are not allowed in SMTP accounts]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0725655 - Only ServiceNow Mail Servers are allowed to send emails for service-now.com domain|Only ServiceNow Mail Servers are allowed to send emails for \"service-now.com\" domain]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0541355 - How Access Control List (ACL) evaluation works in ServiceNow|How Access Control List (ACL) evaluation works in ServiceNow]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0656366 - Relationship between Business Rules and Access Control Rules (ACLs)|Relationship between Business Rules and Access Control Rules (ACLs)]]
