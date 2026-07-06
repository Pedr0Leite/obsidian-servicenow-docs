---
title: "Email Reader Job stuck/running for more than 2 hours alerts"
aliases:
  - KB0755063
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755063
kb_number: KB0755063
last_modified: 2025-06-13
---

## Email Reader Job stuck/running for more than 2 hours alerts

  

### Issue

Our monitoring system automatically creates cases titled "Email Reader Job stuck/running for more than 2 hours" when the Email Reader Job runs for longer than 2 hours. This is a scheduled job that runs every 2 minutes and is responsible for reading emails from any POP3 or IMAP servers that are registered in **Email Accounts**. It will continue running until there are no more emails to be read from the POP3/IMAP server. Common causes and additional remedies are listed below. 

### Cause

Common Causes for the alert:

-   Large influx of incoming email that needs to be read from the POP3/IMAP server. If this is coming from one user and is unwanted, you can disable the user so that the emails are ignored.
-   Email loop between the instance and a user that has an auto-reply email sent back that is processed. This can be stopped by disabling the notification/inbound action or using email filters on the instance or can also be addressed on the user side to stop the auto-replies.
-   Email bounce backs. This is similar to email looping but the user is instead an email server sending an error response back to the instance which in turn causes a loop. This will require investigation from the admin of that email server.
-   Slow business rule on the sys\_email table. If there are any slow business rules that run when new emails come in then this will delay the email reader from reading new emails as it must wait until the sys\_email record has been created before reading the next email from the server.

### Resolution

A few ways you can self-solve:

-   Validate the emails received and possible email loops by going to **Emails (sys\_email)** on the instance to check the recent emails.
-   Inspect any business rules for the sys\_email table that were recently changed that could cause a delay in reading new emails. For example, a big or complex query in such a business rule would slow new emails from being added to the sys\_email table.
