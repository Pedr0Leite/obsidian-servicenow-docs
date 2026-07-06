---
title: "Attachments from Email Client saved to the target record"
aliases:
  - KB0793391
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793391
kb_number: KB0793391
last_modified: 2024-04-08
---

## Attachments from Email Client saved to the target record

  

### Issue

Post New York upgrade, attachments from the email client are being saved to the target record.

Example:

1.  From a record (Incident, RITM etc.) open the Email Client.
2.  In the Email Client include an attachment to be sent.
3.  Send the email
4.  Attachment is saved to the target record and also displayed in the Activity Log

### Release

New York

### Cause

The default configuration of the Email Client has been updated.

The default behavior of the new configuration has been set up to save attachments from the Email Client directly to the target record.

### Resolution

In the instance navigate to `Email Client` > `Email Client Configuration` > `Default` > `Attachment Handling`

We can observe that the `Attachment Send Action` field has been set up with the `Attach to Target Record` option.

By clicking on it, we are presented with a drop-down menu containing 3 options:

```
[-] Attach to Email Record[-] Attach to Target Record[-] Conditionally Attach to Target Record
```

In order to prevent future attachments from being saved directly to the record, please select the `Attach to Email Record` option.   
By utilising this option, attachments from the Email Client will be saved on the `sys_email` table where all emails sent or received from the instance reside.  
Attachments in email records residing on the `sys_email` table will be visible under the `Email Attachments` tab.

### Related Links

`Conditionally Attach to Target Record` -> this option allows you to save attachments from the Email Client if they fit a specific condition. This option can be useful for tailoring the behavior of attachment saving to your business specifications.
