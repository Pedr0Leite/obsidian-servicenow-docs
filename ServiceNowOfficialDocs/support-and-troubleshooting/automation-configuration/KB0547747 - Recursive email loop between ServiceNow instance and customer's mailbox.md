---
title: "Recursive email loop between ServiceNow instance and customer's mailbox"
aliases:
  - KB0547747
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547747
kb_number: KB0547747
last_modified: 2024-04-30
---

## Issue

Recursive email loop between ServiceNow instance and customer's mailbox

  

Problem

* * *

Some customers may have a mailbox set up with an email address and a forward rule that sends any email received by the mailbox to the ServiceNow instance. Unknowingly, sometimes this mailbox address is used as the recipient in the instance notification table. This creates a recursive email loop between the ServiceNow instance and customer's mailbox, and causes new incidents to be created recursively.

Symptoms

* * *

These are the symptoms the customer might experience:  

-   new incidents created recursively
-   inbox and outbox flooded with emails
-   emails in inbox showing the email came from the instance itself

Cause

* * *

A forward rule is set up in customer's mailbox, and the mailbox email address is one of the recipients in the instance notification table. This leads to a recursive email between the ServiceNow instance and the customer's mailbox, creating new incidents recursively. 

Resolution

* * *

Based on customer needs/requirements, either:

-   Remove the forward rule in the customer's mailbox.
-   Remove the customer's mailbox address from the **recipient** field of the notification.
