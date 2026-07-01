---
title: Maintain per-user subscription allocations in Subscription Management at renewal
description: Ensure subscription allocations remain consistent throughout the renewal process.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/maintain-allocations-renewal.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Managing per-user subscriptions, Subscription Management, Get started, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - type-task
---

# Maintain per-user subscription allocations in Subscription Management at renewal

Ensure subscription allocations remain consistent throughout the renewal process.

## Before you begin

Role required: usage\_admin, sn\_sub\_man.admin, oradmin

## About this task

When a per-user subscription renews, a new product SKU might be added to your account. This SKU is treated as a new product subscription in [[subscription-management-landing-page-v2|Subscription Management]].If you've manually allocated user-based subscriptions in the past, you must re-allocate renewed subscriptions by adding groups with measured roles to the subscription.

If you haven't manually allocated user-based subscriptions before, allocations are made automatically based on user and group roles. No action is necessary to maintain allocations after renewal.

## Procedure

1.  Before the renewal date, monitor the subscription end dates on the details page and document the current group allocations.

    See [[subscription-details-v2|Viewing product subscription details in Subscription Management]].

2.  After the renewal date, add the documented groups to the renewed subscription in Subscription Management.

    See [[allocate-subscriptions-v2|Allocate subscriptions in Subscription Management]].


## What to do next

Continue to monitor subscription renewal dates to ensure that your allocations are accurate throughout each renewal.

**Parent Topic:**[[managing-user-subscriptions-v2|Managing per-user subscriptions in Subscription Management]]

## Related

- [[subscription-details-v2|Viewing product subscription details in Subscription Management]]
- [[allocate-subscriptions-v2|Allocate subscriptions in Subscription Management]]
- [[managing-user-subscriptions-v2|Managing per-user subscriptions in Subscription Management]]
- [[subscription-management-landing-page-v2|Subscription Management]]
