---
title: "Email Notifications will not create an outbound email record if there is an invalid script reference"
aliases:
  - KB0754244
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0754244
kb_number: KB0754244
last_modified: 2023-08-03
---

## Email Notifications will not create an outbound email record if there is an invalid script reference

  

### Issue

Email Notification is not creating the outbound sys\_email record as expected.

-   Source record is updated that meets the notifications condition.
-   Email address exists for a specific user.
-   SMTP processes are active and running.

  

### Cause

If the HTML field of a Notification record has a script reference where the script does not exist in the 'sys\_script\_email' table.  The email will fail to send.

Example:    ${mail\_script:bogus\_script}

### Resolution

1.  Create a Notification Email Script that matches the one in the HTML field being referenced . (ie:  bogus\_script)
2.  OR, Remove the invalid script reference from the HTML field on the Notification record.

  

For additional Notification troubleshooting tips, please refer to [KB0679999](https://hi.service-now.com/kb_view.do?sysparm_article=KB0679999 "KB0679999")
