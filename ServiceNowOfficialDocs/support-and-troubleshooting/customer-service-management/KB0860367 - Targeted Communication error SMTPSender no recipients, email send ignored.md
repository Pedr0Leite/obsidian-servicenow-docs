---
title: "Targeted Communication error \"SMTPSender: no recipients, email send ignored\"
aliases:
  - KB0860367
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0860367
kb_number: KB0860367
last_modified: 2025-05-13
---

## Issue

A publication with a condition to fetch the recipient list, when published, the email fails to be sent, with the error:

"SMTPSender: no recipients, email send ignored"

## Resolution

Change the 'ServiceNow SMTP' From, to be the same as the expected user name and avoiding the SMTPSender issue.

Alternatively, consider customizing the Script Include **PublicationUtils**, commenting out line 24:  
// gr\_notif.setValue('recipient\_users',smtp\_address);

This will not add the email to the notification and avoid the issue.
