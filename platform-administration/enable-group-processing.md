---
title: Enable email account group processing
description: Enable the email reader job to start processing your email account groups so that you can reduce the time it takes to process inbound email accounts.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/enable-group-processing.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Multiple email readers, Email accounts, Create, Email Administration, Notifications, Configure core features, Administer the ServiceNow AI Platform]
---

# Enable email account group processing

Enable the email reader job to start processing your email account groups so that you can reduce the time it takes to process [[ia-inbound-email-il|inbound email]] accounts.

## Before you begin

[[create-email-account-group|Create email account groups]].

Role required: admin

## Procedure

1.  [[t_AddAPropertyUsingSysPropsList|Add a system property]] with the following settings:

    -   Name: **glide.email.inbound.account\_group\_processing**
    -   Type: true \| false
    -   Value: **true**

## What to do next

Check the status of your email account groups to see if processing time has been reduced. For more information, see [[monitor-email-account-groups|Monitor email account groups]].

To further reduce processing time, consider creating another email reader job to process inbound email accounts. For more information, see [[create-email-reader-job|Create an email reader job]].

## Related

- [[create-email-account-group|Create email account groups]]
- [[t_AddAPropertyUsingSysPropsList|Add a system property]]
- [[monitor-email-account-groups|Monitor email account groups]]
- [[create-email-reader-job|Create an email reader job]]
- [[ia-inbound-email-il|Inbound email]]
