---
title: Maintain custom table and application mappings at renewal in Subscription Management
description: Ensure custom table and application mappings remain consistent throughout the renewal process.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/maintain-mappings-renewal.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Managing custom tables and apps, Subscription Management, Get started, Administer the ServiceNow AI Platform]
---

# Maintain custom table and application mappings at renewal in Subscription Management

Ensure custom table and application mappings remain consistent throughout the renewal process.

## Before you begin

Role required: usage\_admin, sn\_sub\_man.admin, oradmin

## About this task

When a subscription renews, a new product SKU might be added to your account. This SKU is treated as a new product subscription in [[subscription-management-landing-page-v2|Subscription Management]], requiring you to re-map custom applications and [[custom-tables|custom tables]] to the subscription to stay in compliance.

## Procedure

1.  Before the renewal date, monitor the subscription end dates and document the current list of custom application and custom table mappings.

    See [[subscription-details-v2|Viewing product subscription details in Subscription Management]].

2.  After the renewal date, map the documented tables and applications to the renewed subscription in Subscription Management.

    See [[map-custom-applications-v2|Map a custom application to a product subscription in Subscription Management]] and [[allocate-custom-table-subsc-app-v2|Map custom tables to a product subscription in Subscription Management]].


## What to do next

Continue to monitor subscription renewal dates to ensure that your mappings are accurate throughout each renewal.

**Parent Topic:**[[allocating-custom-tables-subscr-apps-v2|Managing custom tables and applications in Subscription Management]]

## Related

- [[subscription-details-v2|Viewing product subscription details in Subscription Management]]
- [[map-custom-applications-v2|Map a custom application to a product subscription in Subscription Management]]
- [[allocate-custom-table-subsc-app-v2|Map custom tables to a product subscription in Subscription Management]]
- [[allocating-custom-tables-subscr-apps-v2|Managing custom tables and applications in Subscription Management]]
- [[subscription-management-landing-page-v2|Subscription Management]]
- [[custom-tables|Custom tables]]
