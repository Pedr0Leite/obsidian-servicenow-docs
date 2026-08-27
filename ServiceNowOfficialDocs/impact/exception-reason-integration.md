---
title: Exception reason integration
description: You can synchronize exception reasons from non-production to Production instances once a record is created or updated.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/impact/exception-reason-integration.html
release: australia
topic_type: concept
last_updated: "2026-05-05"
reading_time_minutes: 1
breadcrumb: [Scan Engine integrations, Configure the Impact Store Application, Configuring Impact, Impact]
tags:
  - impact
  - type-concept
---

# Exception reason integration

You can synchronize exception reasons from non-production to Production instances once a record is created or updated.

When a developer creates or updates an exception reason on a non-production instance, the integration automatically propagates that change to the production instance. If production approvals are enabled, the exception reason enters a Requested state and triggers an approval workflow before taking effect.

## Approval workflow

When **Enable approvals in production** is selected in Scan Engine Properties, the following workflow applies:

1.  A developer creates or updates an exception reason on the non-production instance.
2.  The exception reason is synced to production in a `Requested` state.
3.  An approval request is sent to the configured Approval Group\(s\).
4.  Once approved or rejected, the status syncs back to the developer instance.

## Prerequisites

-   My SN Instances registration is complete. See [[register-your-instance|Register your instance]].
-   Authentication is configured. See [[configure-basic-auth-method|Configure the Basic authentication method]] or [[configure-oauth-auth-method|Configure the OAuth authentication method development instance]].
-   Role required: `sn_se.scan_engine_admin`.

-   **[[syncing-exception-reasons|Sync exception reasons]]**  
Configure the Exception reason integration to automatically synchronize exception reasons between your non-production and production instances.

**Parent Topic:**[[instance-integration-scan-engine|Scan Engine integrations]]

## Related

- [[register-your-instance|Register your instance]]
- [[configure-basic-auth-method|Configure the Basic authentication method]]
- [[configure-oauth-auth-method|Configure the OAuth authentication method development instance]]
- [[syncing-exception-reasons|Sync exception reasons]]
- [[instance-integration-scan-engine|Scan Engine integrations]]
