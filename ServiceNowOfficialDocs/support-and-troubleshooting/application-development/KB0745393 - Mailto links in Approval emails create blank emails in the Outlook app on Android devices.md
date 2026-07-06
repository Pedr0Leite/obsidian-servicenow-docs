---
title: "Mailto links in Approval emails create blank emails in the Outlook app on Android devices"
aliases:
  - KB0745393
tags:
  - servicenow
  - support-kb
  - approvals
  - notifications
  - email-client
  - mobile
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745393
kb_number: KB0745393
last_modified: 2026-05-05
---

## Mailto links in Approval emails create blank emails in the Outlook app on Android devices

  

### Issue

Approval emails using the default templates sent from ServiceNow include **_mailto_** links so that the approval can be approved or rejected by a reply email.

![](/sys_attachment.do?sys_id=a132e0b747b2e614c2488d01426d434c)

These hyperlinks have the following HTML behind them:

<a href="mailto:**<instance email address>**?subject&#61;Re%3ACHG0030003%20-%20approve&amp;body&#61;%0A%0ARef%3AMSG0000461\_5e1w4D7N24JkTa3P9ErO%20" rel="nofollow">Click here to approve CHG0030003</a>

<a href="mailto:**<instance email address>**?subject&#61;Re%3ACHG0030003%20-%20reject&amp;body&#61;%0A%0ARef%3AMSG0000461\_5e1w4D7N24JkTa3P9ErO%20" rel="nofollow">Click here to reject CHG0030003</a>

These mailto links are not handled correctly when a user clicks on them using the [Outlook app for Android devices](https://play.google.com/store/apps/details?id=com.microsoft.office.outlook&hl=en "Outlook app for Android devices"). The app will create a new email message but it will not copy the subject or the instance email address from the **_mailto_** link.

### Release

Not available.

### Resolution

If you run into this issue, please contact Microsoft to report it. There is currently no workaround to make sure that the Outlook app creates the reply correctly.

## Related

- [[KB0727617 - Access referenced fields in a notification record against the Approval table]] - approval notification body configuration
- [[KB0725194 - Approval emails are not being generated for requested items]] - approval notification troubleshooting

