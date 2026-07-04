---
title: "Resolve client from ignoring user email and outgoing display name system properties"
aliases:
  - KB0635952
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635952
kb_number: KB0635952
last_modified: 2025-06-05
---

## Resolve client from ignoring user email and outgoing display name system properties

  

### Issue

Emails from the client ignore the values from the user email (glide.email.user) and outgoing email display name (glide.email.username) system properties correctly.

For example, emails from the client are set to be sent from ITSM Service Desk (itsm.servicedesk@company.com). However, they are being sent as IT Service Desk (instance@service-now.com).

Some symptoms are:

-   You have activated the Email Accounts plugin.
-   You have upgraded the instance to the latest release.
-   Your email accounts have been reprovisioned or migrated.

### Cause

When the Email Accounts plugin is installed, the system ignores the glide.email.user and glide.email.username system properties.

### Resolution

Modify the email account records instead of the the sys\_properties records.

**Note:** Only newly generated outbound notifications after the change will reflect the new **Email user** label and **From** setting.

1.  Go to **System Mailboxes > Administration > Email Accounts**
2.  Select the active SMTP account (ServiceNow SMTP).
3.  Change the **Email user** label field to ITSM Service Desk (or the required value).
4.  Change the **From** field to 'itsm.servicedesk@company.com' (or the required value).
5.  **Save** the record.

 ![email account SMTP](sys_attachment.do?sys_id=d2026d88978666504638f6e11153af05 "email account SMTP")
