---
title: "Verify email sending configurations"
aliases:
  - KB0521748
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0521748
kb_number: KB0521748
last_modified: 2025-06-05
---

## Verify email sending configurations

  

### Issue

### Symptoms

-   After cloning an instance, the instance does not send emails.
-   The instance does not send any notifications at all.
-   Emails are marked as send-failed and an error message appears saying the mail server cannot connect to the POP server.
-   Cannot customize the name that appears on emails.
-   The email queue is backed up with messages that keep trying to resend to the Simple Mail Transfer Protocol (SMTP) server. They should simply fail and move on to the next message.

### Cause

-   Email-sending property is disabled.
-   SMTP server settings are not appropriately configured.
-   SMPT server is returning unexpected error codes.

### Resolution

The ServiceNow application uses the ServiceNow SMTP server to process outbound email messages to users (user@yourdomain.com). These messages are sent from the ServiceNow data center, routed as standard SMTP traffic to your primary mail exchanger (MX) server, and processed internally within the organization.

If the SMTP Server settings are not correctly configured, this may prevent emails from being sent. This means it is important for you to know the sign in user name, the email server address, and the password. Prior to modifying the SMTP Server settings, verify that the **Enable email sending** (SMTP) property is enabled.

**Note**: Once an instance is cloned by ServiceNow, the email configurations must be enabled. The **Email sending** property is purposely disabled to prevent users from sending unwanted emails.

To verify that email sending configurations are properly set:

-   Confirm that the email sending property is enabled. For more information, refer to [Enabling Email Sending](https://support.servicenow.com/kb_view.do?sysparm_article=KB0521768 "Enabling Email Sending").
-   Verify that the SMTP server settings are correctly configured. For more information, refer to [Configuring the Outbound SMTP Mail Server Settings](https://www.servicenow.com/docs/csh?topicname=c_EmailAccounts.html&version=latest "Configuring the Outbound SMTP Mail Server Settings").
-   Optionally, configure the instance to handle customer error codes that are coming back from the SMTP server. For more information, refer to [Configuring Error Codes.](https://www.servicenow.com/docs/csh?topicname=c_EmailProperties.html&version=latest)

### Related Links

<table class="noteTable" align="left"><tbody><tr><td style="width: 50px; vertical-align: middle; text-align: center;"><img class="documentation" style="border: 0px solid black;" title="Internal Processes" src="/Plus_24x.pngx" alt="Additional Information" width="25" height="25" align="bottom" border="0"></td><td style="vertical-align: middle; text-align: left;">For details on other properties that are used to configure email processing in ServiceNow, refer to <a title="Email Properties" href="https://docs.servicenow.com/csh?topicname=c_EmailProperties.html&amp;version=latest" target="_blank" rel="noopener noreferrer">Email Properties</a> in the ServiceNow product documentation.&nbsp;</td></tr></tbody></table>
