---
title: "Selecting the approve link in approval emails displays a blank browser screen"
aliases:
  - KB0787305
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0787305
kb_number: KB0787305
last_modified: 2025-06-18
---

## Selecting the approve link in approval emails displays a blank browser screen

  

### Issue

When selecting the approval link in an approval email, it no longer works and instead a blank page displays.

Following is an example of a script that contains this link:

https://<instance-name>.service-now.com/nav\_to.do?uri=sysevent\_email\_action.do?sys\_id=f1fae7b6c0a8011b004aad7f89c7d00f%26sysparm\_view=advanced

This script should open the email client. Instead, the browser shows the following URL:

mailto:<instance-name>@service-now.com?subject=Re%3ACHG0046148%20-%20approve&body=%0A%0ARef%3AMSG8421705%20

![](sys_attachment.do?sys_id=9bc182904796aa58c4e1a325126d43ed)

### Cause

This happens when the user's computer is configured to open **mailto** links with the browser instead of the email client.

### Resolution

This is not a ServiceNow issue. Check with your desktop team on how to configure **mailto** links with the email client.
