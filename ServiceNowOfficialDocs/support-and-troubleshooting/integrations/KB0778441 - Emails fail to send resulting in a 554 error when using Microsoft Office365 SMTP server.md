---
title: "Emails fail to send resulting in a 554 error when using Microsoft Office365 SMTP server"
aliases:
  - KB0778441
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778441
kb_number: KB0778441
last_modified: 2025-06-05
---

## Emails fail to send resulting in a 554 error when using Microsoft Office365 SMTP server

  

### Issue

When sending emails from the instance using a Microsoft Office365 SMTP server, and using different email addresses in the **From** field, some **From** field settings work, while others fail, resulting in a send-failed state. The following error message displays: 

554 error: 554 5.2.0 STOREDRV.Submission.Exception:SendAsDeniedException.MapiExceptionSendAsDenied; Failed to process message due to a permanent exception with message Cannot submit message.

### Release

Applies to any release.

### Cause

The Microsoft Office365 SMTP server is rejecting the set **From** address.

### Resolution

This issue needs to be addressed by Microsoft.

Contact Microsoft Support, show them the error, and ask how to configure the email server to accept multiple **From** addresses.
