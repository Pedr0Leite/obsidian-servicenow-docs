---
title: "Using DKIM for Emails from the service-now.com Domain"
aliases:
  - KB0695182
tags:
  - servicenow
  - support-kb
  - DKIM
  - SPF
  - email
  - email-notifications
  - smtp
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695182
kb_number: KB0695182
last_modified: 2025-07-31
---

## Using DKIM for Emails from the service-now.com Domain

  

### Issue

Support for DKIM was added to the service-now.com domain in late 2017. With DKIM enabled, the ServiceNow (service-now.com) email servers sign outgoing messages using a private key.

Receiving mail servers can then use a public key, published on the service-now.com DNS record, to verify the signatures on any emails sent out from the ServiceNow (service-now.com) email servers.

By default, DKIM signing will only work for emails where the _From:_ address is _something@service-now.com_. For customer domains while using ServiceNow email servers, please see [KB1002273](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1002273 "Requesting Public key for DKIM custom domain via Service Catalog on Now Support").

### Release

NA 

### Resolution

### DKIM public Keys are stored the Service-now.com DNS:

The current DKIM Public key records are found using the "DKIM Selector" value with in the DNS.   
The "DKIM Selector" values are referenced in the  header information sent by ServiceNow Email Servers.

### How to obtain the "DKIM Selector" value from an email header: 

Example email header:  
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=service-now.com; s=20210504; t=1641841077;  
  

The "DKIM Selector" is referenced with in the "s=" value, (s=20210504) so in this example it is: 20210504  
  

There are many websites that let you check DNS-related records such as SPF or DKIM for a domain.

So using the  "DKIM Selector value" (example: 20210504) and the sender domain "service-now.com"

You can run a DNS check on this website: [https://www.mail-tester.com/spf-dkim-check](https://www.mail-tester.com/spf-dkim-check)

#### Retrieving the  "DKIM public key" from the service-now.com DNS using the command line: 

This "DKIM Selector" value can be used running the following command from a UNIX/MacOS computer to retrieve the public Key:

dig 20210504.\_domainkey.service-now.com TXT +short

"v=DKIM1; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwZZerAE5ghMvKjbmPHLB282v5ugk9ll9vyJJtSc72Ttx2J6wAmL1pE50UQeapDgruYUou6BPQXMhVi3LfOU/uRuhY2D9x0PXHio2cjzqO/Kmd+jDm7mSztTfMrsdd9FthAMfcSemt65ElAfDbjH/" "erK1TR5jqN5Ng0WUsGf6PiO7sIYL09asf5n4UK+AjVheYl5ZJefSDVae2XYfjmfHGGYbJrR4MaRrlOF2FQgOpWhU8buy0TwAKPalOAgjXLWWYxDa7w+iU7YrTNjucTwGHEpGvPt8WqbtlivH0JNHWYM3vJ5PgxVW9JRx6SalYfb3B0OH4lBi2dgOv6okIWNFJwIDAQAB"

### Related Links

Some companies request DKIM keys so that they can send emails with **From:** addresses such as _something@customer.com_ while using the ServiceNow SMTP server. Please see [KB1002273](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1002273 "Requesting Public key for DKIM custom domain via Service Catalog on Now Support") on how to request this.

## Related

- [[KB0722504 - Using ServiceNow blackhole or dummy email addresses]]
- [[KB0724199 - Localhost and loopback IPs are not allowed in SMTP accounts]]
