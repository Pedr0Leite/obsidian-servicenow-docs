---
title: Security Operations Integration - Sightings Search Flow
description: Security Operations Integration - Sightings Search flow is a high-level flow independent of integrations. It uses the configured queries to search for a set of observables based on the configured integrations which support the capability. Use it to fulfill an integration such as Splunk or Elasticsearch.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/secops-integration-sightings-search-workflow.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Create sightings search configuration records, Security Operations Integration- Sightings Search capability, Integration capabilities, Security Operations Integration Reference, Security Operations common functionality, Security Operations]
tags:
  - security-management
  - type-task
---

# Security Operations Integration - Sightings Search Flow

**[[security-operations-landing-page|Security Operations]] Integration - [[indicator-sightings|Sightings]] Search** flow is a high-level flow independent of integrations. It uses the configured queries to search for a set of [[c_Observables|observables]] based on the configured integrations which support the capability. Use it to fulfill an integration such as Splunk or Elasticsearch.

## Before you begin

Role required: sn\_si.analyst

## About this task

If a security incident has an observable attached to it, this flow is triggered when you click on **[[tisc-run-sighting-search|Run Sighting Search]]** in the **Actions on selected rows...** drop-down menu in the **Security Incident Observables** tab.

\[Omitted image "integration-sightings-search.png"\] Alt text: Flow design for Security Operations Integration- Sightings Search

Activities specific to this flow are described here. For more information on other activities, see [[common-wf-activities|Common Security Operations integration flows and orchestration activities]].

-   **[[determine-observables-sightings-search-activity|Sightings Search - Determine Observables activity]]**  
The **Sightings Search - Determine Observables** workflow activity determines which observables to include in the workflow.
-   **[[persistent-observable-sightings-activity-arcsight-wf|Persistent Observable Sightings activity]]**  
The **Persistent Observable Sightings** workflow activity retrieves observables from the third-party integration.
-   **[[get-observable-sightings-queries-activity|Get Observable Sightings Queries activity]]**  
The **Get Observable Sightings Queries** workflow activity retrieves queries from the integration configuration.
-   **[[secops-integration-sightings-search-arcsight-workflow|Security Operations - Arcsight Logger Sightings Search Flow]]**  
**Security Operations - ArcSight Logger Sightings Search** flow is the implementation for the Splunk integration launched by the **Security Operations Integration - Sightings Search Flow**.
-   **[[secops-integration-sightings-search-es-workflow|Security Operations - Elasticsearch Sightings Search Flow]]**  
**Security Operations - Elasticsearch Sightings Search** flow is the Elasticsearch implementation launched by the **Security Operations Integration - Sightings Search** flow.
-   **[[secops-integration-sightings-search-mcafee-workflow|Security Operations - McAfee ESM Sightings Search Flow]]**  
**Security Operations - McAfee ESM Sightings Search** flow is the implementation for the McAfee Sighting Search implementation launched by the **Security Operations Integration - Sightings Search Flow**.
-   **[[secops-integration-sightings-search-qradar-workflow|Security Operations - QRadar Sightings Search Flow]]**  
**Security Operations - QRadar Sightings Search** flow is the implementation for the IBM QRadar integration launched by the **Security Operations Integration - Sightings Search flow**.
-   **[[secops-integration-sightings-search-splunk-workflow|Security Operations Integration - Splunk Sightings Search Flow]]**  
**Security Operations - Splunk Sightings Search** flow is the implementation for the Splunk integration launched by the **Security Operations Integration - Sightings Search flow**.

**Parent Topic:**[[sightings-search-configurations|Create sightings search configuration records]]

## Related

- [[common-wf-activities|Common Security Operations integration flows and orchestration activities]]
- [[determine-observables-sightings-search-activity|Sightings Search - Determine Observables activity]]
- [[persistent-observable-sightings-activity-arcsight-wf|Persistent Observable Sightings activity]]
- [[get-observable-sightings-queries-activity|Get Observable Sightings Queries activity]]
- [[secops-integration-sightings-search-arcsight-workflow|Security Operations - Arcsight Logger Sightings Search Flow]]
- [[secops-integration-sightings-search-es-workflow|Security Operations - Elasticsearch Sightings Search Flow]]
- [[secops-integration-sightings-search-mcafee-workflow|Security Operations - McAfee ESM Sightings Search Flow]]
- [[secops-integration-sightings-search-qradar-workflow|Security Operations - QRadar Sightings Search Flow]]
- [[secops-integration-sightings-search-splunk-workflow|Security Operations Integration - Splunk Sightings Search Flow]]
- [[sightings-search-configurations|Create sightings search configuration records]]
- [[security-operations-landing-page|Security Operations]]
- [[indicator-sightings|Sightings]]
- [[c_Observables|Observables]]
- [[tisc-run-sighting-search|Run Sighting Search]]
