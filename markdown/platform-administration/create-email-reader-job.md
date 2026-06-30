---
title: Create an email reader job
description: If you created email account groups to fine-tune inbound email account processing, you can create an email reader job to process those account groups concurrently, in addition to the default email reader job.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/create-email-reader-job.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Multiple email readers, Email accounts, Create, Email Administration, Notifications, Configure core features, Administer the ServiceNow AI Platform]
---

# Create an email reader job

If you created email account groups to fine-tune [[ia-inbound-email-il|inbound email]] account processing, you can create an email reader job to process those account groups concurrently, in addition to the default email reader job.

## Before you begin

1.  [[create-email-account-group|Create email account groups]].
2.  [[enable-group-processing|Enable email account group processing]]

Role required: email\_account\_admin or admin

## Procedure

1.  In the Navigation filter, type `sys_trigger.list`.

2.  In the sys\_trigger table, select the Email Reader job record.

3.  In the Email Reader job form:

    1.  Enter a unique name for the email reader job to be added so that you can differentiate it from the default email reader job.
    2.  If needed, change the time interval for this email reader job.
4.  From the form context menu, click **Insert**.

    Another email reader job is created. This job runs concurrently with the default email reader job to process email account groups.


## What to do next

[[monitor-email-account-groups|Monitor email account group processing]] and determine if the additional reader job reduces processing time. If needed, you can continue fine-tuning email account processing. For example, you might consider adding another email account group.

## Related

- [[create-email-account-group|Create email account groups]]
- [[enable-group-processing|Enable email account group processing]]
- [[monitor-email-account-groups|Monitor email account groups]]
- [[ia-inbound-email-il|Inbound email]]
