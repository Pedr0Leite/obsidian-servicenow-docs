---
title: Mismatched version support
description: Providers and consumers using different versions of the Service Exchange applications can exchange and synchronize data between their ServiceNow instances.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/service-exchange/service-bridge-v2-mismatch-version.html
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-05-13"
reading_time_minutes: 1
keywords: [mismatched version, version compatibility, provider upgrade, consumer upgrade]
breadcrumb: [Explore, Service Exchange]
---

# Mismatched version support

Providers and consumers using different versions of the [[tmt-service-bridge-both-landing-page|Service Exchange]] applications can exchange and synchronize data between their ServiceNow instances.

-   Providers can upgrade their Service Exchange application and deploy new capabilities without interrupting services to consumers who haven’t upgraded to their application.
-   Consumers who haven’t upgraded can use existing entitlements from their provider, as well as new entitlements at or below their current compatibility level. However, they can’t activate entitlements on newer compatibility levels until they upgrade to the latest version.

The following is an example scenario:

-   The provider and consumer are [[service-bridge-v2-administer|using Service Exchange for Providers]] 1.0 and [[service-bridge-consumers-landing-page|Service Exchange for Consumers]] 1.0. The provider has created some configurations \(such as remote task definitions, remote record producers, or [[service-bridge-v2-explore-foundation-data-sync|foundation data sync]] offerings\) and the consumer is using these entitlements.
-   The provider decides to upgrade to [[service-bridge-providers-landing-page|Service Exchange for Providers]] 2.0 but the consumer is still using the older version. In this case, the consumer can continue to use the entitlements created using the older version of Service Exchange and sync data with the provider.
-   To use the latest configuration revisions \(created with the upgraded application\), the consumer must upgrade to a version that is compatible with the provider.

**Related topics**  


[[service-bridge-v2-config-revision|Configuring revisions]]

## Related

- [[service-bridge-v2-config-revision|Configuring revisions]]
- [[tmt-service-bridge-both-landing-page|Service Exchange]]
- [[service-bridge-v2-administer|Using Service Exchange for providers]]
- [[service-bridge-consumers-landing-page|Service Exchange for Consumers]]
- [[service-bridge-v2-explore-foundation-data-sync|Foundation data sync]]
- [[service-bridge-providers-landing-page|Service Exchange for Providers]]
