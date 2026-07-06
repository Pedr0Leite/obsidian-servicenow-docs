---
title: "Unable to select custom email template and use mail script "
aliases:
  - KB0814638
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814638
kb_number: KB0814638
last_modified: 2026-05-05
---

## Unable to select custom email template and use mail script

  

### Issue

Symptoms 

\-The email notification is created, but only OOB templates are selectable under "what it will contain"

\-A mail script is written on the email template and notification

### Release

All releases

### Cause

In order to select an email template for a notification, the template must be created on the same table as the notification. Mail scripts that are written inside of the email notification "Message HTML" will override the script in the template that is attached to the notification. 

### Resolution

1.  Create a template on the same table as the email notification. 
2.  When writing scripts, note that any mail script written in the "Message HTML" body of the email notification will override the mail scripts that were added in the template.
