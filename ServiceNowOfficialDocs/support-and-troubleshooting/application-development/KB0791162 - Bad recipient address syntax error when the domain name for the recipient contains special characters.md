---
title: "\"Bad recipient address syntax\" error when the domain name for the recipient contains special characters "
aliases:
  - KB0791162
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791162
kb_number: KB0791162
last_modified: 2026-01-06
---

## "Bad recipient address syntax" error when the domain name for the recipient contains special characters

  

### Issue

When the domain section of the email address of a user in an instance is an Internationalised Domain Name (IDN), the instance will not be able to send emails to that user. 

"501 5.1.3 Bad recipient address syntax" will be noted in the error log.

### Release

All releases.

### Cause

ServiceNow email system does not support Internationalised Domain Names (IDNs). 

### Resolution

Please convert IDNs to Punycode and save the email address in your instance with the Punycode equivalent.

For example, test@özelalanadı.com must be saved as test@xn--zelalanad-z7a27d.com

### Related Links

What is Punycode?

Punycode is a special encoding used to convert Unicode characters to ASCII, which is a smaller, restricted character set.

[Wikipedia](http://en.wikipedia.org/wiki/Punycode "Learn about Punycode on Wikipedia")

There are several sites and libraries available for Punycode conversation.
