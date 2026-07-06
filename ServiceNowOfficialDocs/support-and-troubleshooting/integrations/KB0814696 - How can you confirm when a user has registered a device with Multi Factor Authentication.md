---
title: "How can you confirm when a user has registered a device with Multi Factor Authentication?"
aliases:
  - KB0814696
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814696
kb_number: KB0814696
last_modified: 2025-10-02
---

## How can you confirm when a user has registered a device with Multi Factor Authentication?

  

### Issue

For all users set to have Multi Factor Authentication enabled, you want to know what users have already registered a device by reading the QR code at login time.

### Release

Any supported release.

### Resolution

In order to know if a user enabled to use MFA has already scanned the MFA QR code during login, then list table named \[user\_multifactor\_auth\]. Observe that:  
  
\- This table will have an entry for a user  if the user has been prompted for **multi\_factor\_auth\_setup\_page.do**  
\- The column 'Validated' will have the value "true" ONLY if the user already scanned the QR code. Otherwise, the value will be "false".

In the example below, user "Pepito Pepas" has already scanned the QR code since the 'Validated'  field is set to "true". In contrast, user "Abel Tuter" has visited the login page, but has not yet scanned the QR code with a phone.  
  
  
![user\_multifactor\_auth](sys_attachment.do?sys_id=68e08c859373aed45736b25d6cba1031)
