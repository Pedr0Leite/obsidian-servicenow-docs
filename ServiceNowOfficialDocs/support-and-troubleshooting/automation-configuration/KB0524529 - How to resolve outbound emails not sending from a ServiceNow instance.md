---
title: "How to resolve outbound emails not sending from a ServiceNow instance"
aliases:
  - KB0524529
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0524529
kb_number: KB0524529
last_modified: 2026-03-27
---

## How to resolve outbound emails not sending from a ServiceNow instance

  

### Issue

Resolve outbound email delivery failures in ServiceNow when notifications, scheduled emails, or manually triggered emails remain in the Outbox or are not delivered to recipients.

### Release

All supported releases

### Cause

Email sending is controlled by the glide.email.smtp.active system property. When this property is set to **No** or is not configured, the instance does not send outbound emails.

This commonly occurs in the following scenarios:

-   Newly provisioned instances, where email sending is disabled by default
-   Cloned or refreshed instances, where email sending is disabled to prevent unintended delivery
-   Instances where email was manually disabled for troubleshooting or security purposes

### Resolution

### Step 1: Enable email sending

1.  Go to **System Properties** \> **Email Properties.**
2.  Locate the **Email sending enabled** (glide.email.smtp.active) property.
3.  Set the value to **Yes**.
4.  Select **Save**.

By default, ServiceNow uses a managed SMTP server. No additional configuration is required unless you are using a custom SMTP server.

![emailProperties.png](sys_attachment.do?sys_id=1f5d70879737b65c24a7739c1253af3a "Email Properties")

### Step 2: Configure test email routing (non-production only)

To prevent emails from reaching real recipients on a non-production instance:

1.  Go to **System Properties** > **Email Properties.**
2.  Locate the **Send all email to this test email address** (glide.email.test.user) property.
3.  Enter a test email address.
4.  Select **Save.**

All outbound emails will be redirected to the specified address. Remove this value before promoting instance to production.

### Step 3: Verify email diagnostics

1.  Go to **System Diagnostics** \> **Email Diagnostics**.
2.  Verify that **Sending status** is set to **Enabled**.
3.  If applicable, check the **Receiving status**.
4.  Review logs for any errors or blocked activity.

### Related Links

[Enable basic email](https://www.servicenow.com/docs/r/platform-administration/t_ConfiguringStandardEmail.html "Enable basic email")

[Advanced email setup](https://www.servicenow.com/docs/r/platform-administration/c_AlternateEmailConfigurations.html "Advanced email setup")
