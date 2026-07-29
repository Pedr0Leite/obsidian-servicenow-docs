---
title: Configure Service Exchange for Consumers
description: As a consumer, follow these steps to set up the Service Exchange for Consumers application in your own instance.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/service-exchange/service-bridge-v2-install.html
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Service Exchange for Consumers, Service Exchange]
tags:
  - service-exchange
  - marketplace
  - spokes
  - apps
  - type-concept
---

# Configure Service Exchange for Consumers

As a consumer, follow these steps to set up the [[service-bridge-consumers-landing-page|Service Exchange for Consumers]] application in your own instance.

## Pre-installation checks

**Check glide.servlet.uri property**: Ensure that the `glide.servlet.uri` property in the Glide instance is set to the correct instance URL. An issue can occur when an instance is cloned from production, but still refers to the production URL for the `glide.servlet.uri` property.

|Task|Link|
|----|----|
|Install the Service Exchange for Consumers application.|See [[install-service-bridge-v2-customer|Install Service Exchange for Consumers]].|
|Add Service Exchange roles for consumers.|See [[service-bridge-v2-customer-roles|Personas for consumers]].|
|Register with a provider.|See [[service-bridge-v2-register|Connect to a provider]].|
|Activate entitlements.|See [[service-bridge-v2-activate-entitlements|Activate a remote record producer in Service Exchange]].|
|Configure consumer pre-flows.|See [[service-bridge-v2-conf-consumer-flow|Service Exchange consumer pre-flows]].|
|Add authorized users.|See [[service-bridge-v2-create-auth-user|Add an authorized user]].|
|Create transforms.|See [[service-bridge-v2-create-transform|Create a transform in Service Exchange]].|
|Create [[service-bridge-v2-remote-task-overview|remote tasks]] to sync data.|See [[service-bridge-v2-remote-task-create|Create remote tasks to sync data]].|
|Configure settings.|See [[service-bridge-v2-configure-consumer-settings|Configure settings on the consumer instance]].|

**Related topics**  


[[tmt-service-bridge-both-landing-page|Service Exchange]]

[[se-consumer-using|Use for consumers]]

## Related

- [[install-service-bridge-v2-customer|Install Service Exchange for Consumers]]
- [[service-bridge-v2-customer-roles|Personas for consumers]]
- [[service-bridge-v2-register|Connect to a provider]]
- [[service-bridge-v2-activate-entitlements|Activate a remote record producer in Service Exchange]]
- [[service-bridge-v2-conf-consumer-flow|Service Exchange consumer pre-flows]]
- [[service-bridge-v2-create-auth-user|Add an authorized user]]
- [[service-bridge-v2-create-transform|Create a transform in Service Exchange]]
- [[service-bridge-v2-remote-task-create|Create remote tasks to sync data]]
- [[service-bridge-v2-configure-consumer-settings|Configure settings on the consumer instance]]
- [[tmt-service-bridge-both-landing-page|Service Exchange]]
- [[se-consumer-using|Use for consumers]]
- [[service-bridge-consumers-landing-page|Service Exchange for Consumers]]
- [[service-bridge-v2-remote-task-overview|Remote tasks]]
