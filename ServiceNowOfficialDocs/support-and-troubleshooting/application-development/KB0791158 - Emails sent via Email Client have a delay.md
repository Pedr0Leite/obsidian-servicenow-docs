---
title: "Emails sent via Email Client have a delay"
aliases:
  - KB0791158
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791158
kb_number: KB0791158
last_modified: 2026-01-06
---

## Emails sent via Email Client have a delay

  

### Issue

Emails sent via the Email Client show a delay of 5 minutes or more while emails created by email notifications are sent as expected.

### Release

All releases

### Cause

The Email Client creates the sys\_email record when a user clicks on Email on the record form. However the email will be queued to be sent when the user clicks the Send button. The time the user takes to compose the email will not be shown on the sys\_email record. The time between sys\_created and sys\_updated will not accurately show the time it took the instance to process and send that sys\_email record because it also includes the time spent composing the email.

A notification creates the sys\_email record and queues it immediately. Therefore the time between sys\_created and sys\_updated will show the time it took the instance to process and send that sys\_email record.

### Resolution

This behaviour is by design. If you would like to check how long an email took to be delivered, please check the headers from the recipient's copy of the email. This will include when it was created and what steps/servers were used to relay that email.
