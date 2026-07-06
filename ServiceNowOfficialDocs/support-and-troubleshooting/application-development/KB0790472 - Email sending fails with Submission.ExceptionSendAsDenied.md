---
title: "Email sending fails with Submission.Exception:SendAsDenied"
aliases:
  - KB0790472
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790472
kb_number: KB0790472
last_modified: 2024-04-08
---

## Email sending fails with Submission.Exception:SendAsDenied

  

### Issue

Email sending from an instance is failing with the following error in the logs:

```
WARNING: XXXX.Submission.Exception:SendAsDeniedException.MapiExceptionSendAsDenied
```

### Cause

The issue will occur when the instance is integrated with external SMTP server. (Not default one provided and configured by ServiceNow)

The SMTP server record under System Mailboxes > Administration > Email Accounts will be configured with a default "From" value (ex. [abc@companyA.com](mailto:abc@companyA.com))

When notifications are set up with the Advanced view, there will be an option to modify the "From" and "Reply to" headers of the emails triggered from this specific notification. These fields will be available under the "What it will contain" tab.

These fields will be most likely be set up with a different address (ex. [def@companyA.com](mailto:efg@companyA.com))

When the notification triggers, these fields cause the "User" field of the notification to be populated with the [def@companyA.com](mailto:def@companyA.com) address.  
Since the default email set on the SMTP server record is [abc@companyA.com](mailto:abc@companyA.com) there is a discrepancy in the headers of the emails:  
  
The SMTP server sees this email as sent by [def@companyA.com](mailto:def@companyA.com) on behalf of [abc@companyA.com](mailto:abc@companyA.com)

This is why we are receiving the error stating `SendAsDenied`.

### Resolution

The issue can be tackled at both SMTP server side and ServiceNow side.

**SMTP server side:**  
  

-   Specifically create a permission on the SMTP server which allows [def@companyA.com](mailto:def@companyA.com) to send an email as [abc@companyA.com](mailto:abv@companyA.com)
-   Emails triggered by the notifications will then be sent out without any further errors and modifications required.

  
**ServiceNow side:**  
  

-   Remove the "From" and "Reply to" modified values of the notifications which are causing the discrepancy.
-   When these values are left blank, the emails will be sent out by the default email address [abc@companyA.com](mailto:abc@companyA.com) and the issue will no longer occur.

### Related Links

SMTP

SendAsDenied

email

Storedrv
