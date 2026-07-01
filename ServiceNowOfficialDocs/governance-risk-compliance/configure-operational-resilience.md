---
title: Configuring Operational Resilience
description: Configure the Operational Resilience application to identify risks, failed controls, monitor services and processes, and ensure a complete resilience of your organization.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/governance-risk-compliance/configure-operational-resilience.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Operational Resilience, Governance, Risk, and Compliance]
---

# Configuring Operational Resilience

Configure the [[grc-opres-landing-page|Operational Resilience]] application to identify risks, failed controls, monitor services and processes, and ensure a complete resilience of your organization.

## Operational Resilience configuration overview

A typical configuration of the Operational Resilience application consists of the following steps:

1.  Download the Operational Resilience application in your instance. For instructions, see [[download-opres|Install Operational Resilience application]].
2.  Pillar configuration: Configure the pillars in Operational Resilience. You can also add new pillars or modify the existing pillars, but it is suggested to retain the pillars that come with the base system. For information, see [[setting-up-hierarchy|Setting up pillars, entity types, entity filters, and entities]].
3.  Entity type and entity filter configuration: Activate the [[entity-type-in-risk-ws|entity types]] and [[what-is-an-entity-filter|entity filters]]. For information, see [[set-up-from-ws|Set up pillars and entity types from Workspace UI]].
4.  Main node configurations: Update the main node configurations that are available with the base system or add more main node configurations. For information, see [[set-up-main-node|Configure the Main node configurations]].
5.  Properties: Configure the properties to suit your business needs. For information, see [[configure-opres-prop|Configure Operational Resilience properties]].
6.  Dashboard customization: Customize the dashboard by adding or removing reports as needed to suit your requirements. For more information, see [[flexible-data-model-changes|Using the flexible data model]] and [[setup-homepage|Landing page and dashboard views]].

## Sample Main node configurations

For creating new Main node configurations in the Operational Resilience application, refer to the following end-to-end examples:

-   To create a Services to dependencies sample Main node configuration, see [[configure-ser-to-dep-main-node-config|Sample Services to dependencies configuration]].
-   To create an Application service to dependencies sample Main node configuration, see [[configure-app-ser-to-dep-config|Sample Application service to dependencies configuration]].
-   To configure an end-to-end workflow for a business service and fetch its CSDM dependencies and red flags data to Operational Resilience, see [[configure-end-to-end-wf-bs|Sample end-to-end workflow for a business service]].
-   To configure an end-to-end workflow for a service and fetch its CSDM dependencies and red flags data to Operational Resilience, see [[conf-end-to-end-wf-for-ser|Sample end-to-end workflow for services]].

For other general administrative setup tasks, see [[admin-module-tasks|Completing general administrative tasks]].

## Related

- [[download-opres|download opres]]
- [[setting-up-hierarchy|Setting up pillars, entity types, entity filters, and entities]]
- [[set-up-from-ws|Set up pillars and entity types from Workspace UI]]
- [[set-up-main-node|Configure the Main node configurations]]
- [[configure-opres-prop|Configure Operational Resilience properties]]
- [[flexible-data-model-changes|Using the flexible data model]]
- [[setup-homepage|Landing page and dashboard views]]
- [[configure-ser-to-dep-main-node-config|Sample Services to dependencies configuration]]
- [[configure-app-ser-to-dep-config|Sample Application service to dependencies configuration]]
- [[configure-end-to-end-wf-bs|Sample end-to-end workflow for a business service]]
- [[conf-end-to-end-wf-for-ser|Sample end-to-end workflow for services]]
- [[admin-module-tasks|Completing general administrative tasks]]
- [[grc-opres-landing-page|Operational Resilience]]
- [[entity-type-in-risk-ws|Entity types]]
- [[what-is-an-entity-filter|Entity filters]]
