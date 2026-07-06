---
title: "Inbound emails not creating tickets in the instance"
aliases:
  - KB0792534
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0792534
kb_number: KB0792534
last_modified: 2024-04-08
---

## Inbound emails not creating tickets in the instance

  

### Issue

-   Tickets not being created from some or all inbound emails in the instance
-   Some or all emails not reaching the instance

### Cause

External misconfiguration (not related to the instance) preventing emails from reaching ServiceNow servers.

### Resolution

Inspect the logging information from the "bounce" emails and amend the misconfiguration preventing emails from reaching ServiceNow servers.

Refer to Additional Information for details.

### Related Links

**Troubleshooting steps:**

* * *

-   Complete an initial observation on the \[**sys\_email**\] table in the instance.
-   Narrow the search with a more specific timeframe and confirm whether the emails are present or not:
-   Emails are present -> issue would be related to inbound actions or some other configuration within the instance. Further investigation would be required.
-   Emails cannot be located in \[**sys\_email**\] table:
-   A potential root cause would be that the emails sent to the instance have not reached ServiceNow servers. (if the instance is using the ServiceNow configured **POP3** and **SMTP**). 
-   Check a mailbox from which an email has been sent to the instance and look for any "bounce" emails stating Undelivered message or Delivery failure.
-   If these cannot be found or have been deleted, attempt to send an email to the instance from a mailbox and check the same.
-   Review the information from the "bounce" email -> it will contain detailed logging specifying why the email sending was unsuccessful and will further aid in determining the root cause.
-   This kind of issues are often is not related to the ServiceNow platform and is caused by external misconfiguration. If the logs from the "bounce" email point to the email being denied by ServiceNow servers, Technical Support will be available to assist further.

* * *
