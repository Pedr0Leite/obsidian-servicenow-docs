---
title: "Identify the source of emails sent from ServiceNow"
aliases:
  - KB0745172
tags:
  - servicenow
  - support-kb
  - email
  - sys_email
  - notifications
  - troubleshooting
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745172
kb_number: KB0745172
last_modified: 2025-06-06
---

## Identify the source of emails sent from ServiceNow

  

### Issue

Follow these steps to determine where an email in the Sent mailbox on your instance originated from.  

### Resolution

1.  Open the sent sys\_email record. 
2.  Scroll to the **Headers** field. 
3.  Look for **X-ServiceNow-Source:**

-   -   If the email originated from a notification, it shows **Notification-<SYS\_ID\_OF\_NOTIFICATION>**. 
    -   If the email originated from the email client, it shows **EmailClient**.

## Related

- [[KB0725655 - Only ServiceNow Mail Servers are allowed to send emails for service-now.com domain]] - outbound email server behavior
- [[KB0724449 - Duplicate email notification were sent from the instance when it was not intended]] - notification/email troubleshooting

