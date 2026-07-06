---
title: "Sys_Email records switching between state \"send-ready\" and \"some sys_id\" and notifications delayed"
aliases:
  - KB0793106
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793106
kb_number: KB0793106
last_modified: 2025-06-17
---

## Sys\_Email records switching between state "send-ready" and "some sys\_id" and notifications delayed

  

### Issue

-   When using your own SMTP server different than the default SMTP Server provided from ServiceNow, messages are not sent out for a period of time. This duration could be a few minutes to many hours.

-   Checking the sys\_email table, records seem to be regularly switching between the type **send-ready** and an unknown sys\_id not related to any sys\_email records.

-   The messages are eventually delivered and then the state changes to **Sent** as expected but the message arrives later than expected by the customer.

### Cause

When an email is to be processed, it first goes to the SMTP sender job queue, and then once processed, it goes to the sent or send-ignored or received queue.   
  
In this case, you can see the sys\_id of the two SMTP jobs that you have because there is either a huge email queue to process or an SMTP Server delay.

The two sys\_ids are the sys\_ids of the SMTP jobs. So the fact that you see the sys\_id means that the message is not sent yet. 

### Resolution

Contact your email administrator as this delay is usually due to lack of availability of the external (non-ServiceNow) SMTP server.

Check the creation date and update date of the sys\_email records for the duration of the issue. If the time difference between creation and last update of the sys\_email record is taking longer than usual (for example, 20 minutes or even hours), it means it is likely that you have an issue in your SMTP server (timeout or unresponsive).

For more information on how to test your SMTP connection, see the product documentation topic, [Enable using your own SMTP server.](https://docs.servicenow.com/csh?topicname=t_ConfAltEmailUsgOwnSMTP.html&version=latest "Enable using your own SMTP")
