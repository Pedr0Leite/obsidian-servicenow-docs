---
title: "Enabling Email Sending"
aliases:
  - KB0521768
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0521768
kb_number: KB0521768
last_modified: 2025-02-05
---

## Issue

If an email notification fails to send from your instance and does not appear in the Outbox, the system properties that control email notifications may not be configured properly. For more information, see [Email properties](https://docs.servicenow.com/csh?topicname=c_EmailProperties.html&version=latest "Email properties") in the ServiceNow product documentation.

## Resolution

To verify that the system properties are accurately configured:

1.  Log in to your instance.
2.  Navigate to **System Properties > Email**.
3.  Verify that the **Enable email sending (SMTP)** property is marked as **Yes**.
4.  Click **Save**.

 **Note:** For details on other email properties that are used to configure email processing, refer to [Email Properties](https://docs.servicenow.com/csh?topicname=c_EmailProperties.html&version=latest "Email Properties") in the ServiceNow product documentation
