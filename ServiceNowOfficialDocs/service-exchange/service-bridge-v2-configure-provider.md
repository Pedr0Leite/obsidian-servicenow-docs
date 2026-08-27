---
title: Configure Service Exchange for Providers
description: To set up and configure the Service Exchange for Providers application, follow these steps.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/service-exchange/service-bridge-v2-configure-provider.html
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Service Exchange for Providers, Service Exchange]
tags:
  - service-exchange
  - marketplace
  - spokes
  - apps
  - type-concept
---

# Configure Service Exchange for Providers

To set up and configure the [[service-bridge-providers-landing-page|Service Exchange for Providers]] application, follow these steps.

## Pre-installation checks

**Check glide.servlet.uri property**: Ensure that the `glide.servlet.uri` property in the Glide instance is set to the correct instance URL. An issue can occur when an instance is cloned from production, but still refers to the production URL for the `glide.servlet.uri` property.

|Task|Link|
|----|----|
|Install the Service Exchange for Providers application.|See [[install-service-bridge-v2-provider|Install Service Exchange for Providers]].|
|Set up a new provider record.|See [[service-bridge-v2-new-provider|Set up a Service Exchange provider record]].|
|Assign Service Exchange roles for providers.|See [[service-bridge-v2-personas|User roles for providers]].|
|Create catalog personas.|See [[service-bridge-v2-create-catalog-persona|Create catalog personas]].|
|Create remote choice definitions.|See [[service-bridge-v2-create-remote-choice-fld-defs|Create remote choice definitions in Service Exchange for Providers]]|
|Create remote catalog items.|See [[service-bridge-v2-remote-catalog|Create remote catalogs in Service Exchange for providers]].|
|Create remote task definitions.|See [[service-bridge-v2-create-remote-tasks-defs|Create a remote task definition in Service Exchange for Providers]].|
|Create transforms.|See [[service-bridge-v2-create-transform|Create a transform in Service Exchange]].|
|Update Authorized Users settings.|See [[service-bridge-v2-configure-settings|Update settings for authorized users]]|

If you’re a consumer, see [[service-bridge-v2-install|Configure Service Exchange for Consumers]].

**Related topics**  


[Configure Service Exchange for Consumers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-install.md)

[[tmt-service-bridge-both-landing-page|Service Exchange]]

## Related

- [[install-service-bridge-v2-provider|Install Service Exchange for Providers]]
- [[service-bridge-v2-new-provider|Set up a Service Exchange provider record]]
- [[service-bridge-v2-personas|User roles for providers]]
- [[service-bridge-v2-create-catalog-persona|Create catalog personas]]
- [[service-bridge-v2-create-remote-choice-fld-defs|Create remote choice definitions in Service Exchange for Providers]]
- [[service-bridge-v2-remote-catalog|Create remote catalogs in Service Exchange for providers]]
- [[service-bridge-v2-create-remote-tasks-defs|Create a remote task definition in Service Exchange for Providers]]
- [[service-bridge-v2-create-transform|Create a transform in Service Exchange]]
- [[service-bridge-v2-configure-settings|Update settings for authorized users]]
- [[service-bridge-v2-install|Configure Service Exchange for Consumers]]
- [[tmt-service-bridge-both-landing-page|Service Exchange]]
- [[service-bridge-providers-landing-page|Service Exchange for Providers]]
