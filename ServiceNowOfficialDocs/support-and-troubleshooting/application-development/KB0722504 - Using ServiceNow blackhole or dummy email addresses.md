---
title: "Using ServiceNow blackhole or dummy email addresses"
aliases:
  - KB0722504
tags:
  - servicenow
  - support-kb
  - email
  - smtp
  - sub-production
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0722504
kb_number: KB0722504
last_modified: 2026-01-15
---

## Using ServiceNow blackhole or dummy email addresses

  

### Issue

A blackhole email address is as an email address that immediately discards the emails when they are received. 

This is particularly useful for sub-production instances where you want emails to be sent or processed but do not want them to leave the ServiceNow mail servers.

<table style="border-collapse: collapse; border-color: #000000; background-color: #ffff26;" border="1" cellpadding="5"><tbody><tr><td><strong>IMPORTANT:&nbsp;</strong>This will ONLY work if your instance is configured to use ServiceNow's mail server for SMTP.</td></tr></tbody></table>

Most of the time, this is configured on SMTP mail servers by specifying certain email addresses or a domain.

### Resolution

ServiceNow has the following configured on the SMTP mail servers.

\# blackhole domains 
example.com discard: 
.example.com discard: 
test.com discard: 
.test.com discard: 
nobody.com discard: 
.nobody.com discard: 
dummy.com discard: 
.dummy.com discard: 
yourcompany.com discard: 
.yourcompany.com discard:

As long as the email address ends with any of the previously mentioned domains, it will be discarded by ServiceNow's SMTP mail server.

For example, nobody@example.com; john.smith@dev.example.com; blackhole@acme.yourcompany.com

## Related

- [[KB0724199 - Localhost and loopback IPs are not allowed in SMTP accounts]]
- [[KB0695182 - Using DKIM for Emails from the service-now.com Domain]]
