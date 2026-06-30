---
title: Configuring inbound foundation data sync as providers
description: As a provider, receive the foundation data from your provider using foundation data sync \(FDS\).
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/service-exchange/service-bridge-v2-configure-inboun-fds-providers.html
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Configuring inbound foundation data sync as providers

As a provider, receive the foundation data from your provider using foundation data sync \(FDS\).

Before you use FDS, you must request and configure foundation data. After your consumer creates and publishes FDS definitions, request and configure FDS.

<table id="table_tqf_wwj_5de"><thead><tr><th>

Step

</th><th>

Action

</th><th>

Description

</th></tr></thead><tbody><tr><td>

1.

</td><td>

[[service-bridge-v2-request-fds-offering-consumers|Request a foundation data offering from your consumer.]]

</td><td>

Requests FDS offerings from your consumer based on the published offerings.After you request a foundation data offering, your consumer acknowledges your FDS request and sends a sample payload for each subscription.

</td></tr><tr><td>

2.

</td><td>

[[service-bridge-v2-fds-validate-subs-items-provider|Configure the sample data and validate subscription items.]]

</td><td>

Configure the incoming data based on the CMDB or non-CMDB table to validate subscription items.After you validate subscription items, you must accept the subscription.

</td></tr><tr><td>

3.

</td><td>

[[service-bridge-v2-fds-accept-sups-provider|Accept the subscription.]]

</td><td>

Accept the subscription.After you accept the subscription, your consumer publishes the subscription and data synchronizes according to the defined cadence.

</td></tr></tbody>
</table>**Related topics**  


[[service-bridge-v2-explore-foundation-data-sync|Foundation data sync]]

[[using-provider-bound-fds-consumer|Configure outbound foundation data sync as consumers]]

## Related

- [[service-bridge-v2-request-fds-offering-consumers|Request foundation data sync offerings from a consumer]]
- [[service-bridge-v2-fds-validate-subs-items-provider|Validate FDS subscriptions items as a provider]]
- [[service-bridge-v2-fds-accept-sups-provider|Accept a foundation data sync subscription as a provider]]
- [[service-bridge-v2-explore-foundation-data-sync|Foundation data sync]]
- [[using-provider-bound-fds-consumer|Configure outbound foundation data sync as consumers]]
