---
title: Configure outbound foundation data sync as consumers
description: Foundation data sync \(FDS\) consumers share foundational data with a provider by creating FDS definitions, acknowledging requests, and publishing subscriptions.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/service-exchange/using-provider-bound-fds-consumer.html
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure for consumers, Service Exchange for Consumers, Service Exchange]
---

# Configure outbound foundation data sync as consumers

Foundation data sync \(FDS\) consumers share foundational data with a provider by creating FDS definitions, acknowledging requests, and publishing subscriptions.

<table id="table_msw_fm4_4hc"><thead><tr><th>

Step

</th><th>

Action

</th><th>

Description

</th></tr></thead><tbody><tr><td>

1.

</td><td>

[[service-bridge-v2-create-provider-bound-fds-consumer|Create an FDS Definition.]]

</td><td>

Define the data that you share with your provider.After you create and publish an FDS definition, wait for your provider to request FDS offerings based on the published definition.

</td></tr><tr><td>

2.

</td><td>

[[service-bridge-v2-con-acknowledge-fds-request|Acknowledge FDS requests and send a sample payload.]]

</td><td>

After receiving an FDS request from your provider, acknowledge it and send a sample payload for each subscription. After you send the payload, your provider configures the incoming data for each subscription and accepts it.

</td></tr><tr><td>

3.

</td><td>

[[service-bridge-v2-publish-con-fds-subscription|Publish subscriptions.]]

</td><td>

After the provider accepts the subscription, publish it. After the FDS configuration is complete, data starts synchronizing with the provider based on the defined cadence.

</td></tr></tbody>
</table>**Related topics**  


[[service-bridge-v2-explore-foundation-data-sync|Foundation data sync]]

## Related

- [[service-bridge-v2-create-provider-bound-fds-consumer|Create and publish a provider-bound FDS offering definition]]
- [[service-bridge-v2-con-acknowledge-fds-request|Acknowledge an FDS offering request from your provider]]
- [[service-bridge-v2-publish-con-fds-subscription|Publish an outbound FDS subscription as a consumer]]
- [[service-bridge-v2-explore-foundation-data-sync|Foundation data sync]]
