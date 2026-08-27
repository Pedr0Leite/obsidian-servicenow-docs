---
title: "Forwarded emails and SPAM SPF_SOFTFAIL or SPF_HARDFAIL"
aliases:
  - KB0817647
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0817647
kb_number: KB0817647
last_modified: 2026-06-29
---

## Forwarded emails and SPAM SPF\_SOFTFAIL or SPF\_HARDFAIL

  

### Issue

Every now and then it happens that legitimate messages we receive are flagged as spam.

In most of the cases it is because, among other things, we get an SPF soft fail score of 4.

After an investigation of the possible causes of the issue, it was concluded that it was due to the fact that on the <domain>.com DNS (emails are automatically forwarded to <instance>@service-now.com from that domain).

### Symptoms

A common source of SPF authentication failures in ServiceNow occurs when internal email addresses are configured to forward messages to the ServiceNow instance rather than delivering them directly. In this scenario, an end user sends an email to a helpdesk or support address hosted on the company's own mail infrastructure — such as `helpdesk@mycompany.com` — which is then automatically forwarded by an Exchange transport rule, mail alias, or distribution group to the instance's inbound email address, for example `mycompany@service-now.com`. Because the message is re-delivered by the customer's mail server rather than the original sending MTA, the receiving ServiceNow infrastructure evaluates SPF against the forwarding server's IP address rather than the IP of the original sender.

Since the forwarding mail server is not listed as an authorized sender in the original sender's SPF record, the SPF check fails or returns a softfail, which can cause the message to be flagged, scored as spam, or in some cases silently dropped before it reaches the instance's inbound email processing pipeline. This is not an indication that the original email was malicious or spoofed — it is a structural consequence of how SPF is designed to bind authentication to the delivering IP address rather than the originating one. In most cases, DKIM will continue to pass since the signature travels intact through the forwarding hop, however this alone is insufficient to satisfy DMARC alignment if SPF is the only passing mechanism configured for the domain.  
  
  
  

### Release

All

### Cause

Forwarded emails to an instance can receive SPF FAILS if forwarding is not set up properly.

If the forwarding on the customer server is not set up properly the original email mail server is used as the origin of the email and the SPF record is checked against the SPF record of the forwarding mail server.  This results in a SPF SOFt/HARD FAIL and could result in email being flagged as SPAM.

### Resolution

The following external link describes the issue and how to implement forwarding properly: [Forwarding and SPF](https://support.google.com/mail/forum/AAAAK7un8RUos_pye9rUlM/?hl=en-GB "Forwarding and SPF") or  [Forwarding Broke Your SPF/DMARC? Here’s How SRS and ARC Save the Day](https://www.dchost.com/blog/en/forwarding-broke-your-spf-dmarc-heres-how-srs-and-arc-save-the-day-without-tears/)

This is an issue on how mail forwarding is configured and can only be addressed by mail adminitrators.  
  
It is also possible to set up your own mailservers in an instance, then you will not run into the issue: [Configure an email account](https://docs.servicenow.com/csh?topicname=t_ConfigureAnEmailAccount.html&version=latest "Configure an email account")

## Related

- [[KB0749811 - ServiceNow implementation of DMARC for Cloud Email Services]]
- [[KB0749826 - Unable To fetch Email Address of actual sender in the forwarded emails]]
