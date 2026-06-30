---
title: Security Operations Integration- Sightings Search capability
description: The Sightings Search capability accepts a set of observables, finds any integrations that support a Sightings Search, then executes these searches.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/sightings-search-capability.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Integration capabilities, Security Operations Integration Reference, Security Operations common functionality, Security Operations]
---

# Security Operations Integration- Sightings Search capability

The **[[indicator-sightings|Sightings]] Search** capability accepts a set of [[c_Observables|observables]], finds any integrations that support a Sightings Search, then executes these searches.

The Sightings Search capability has a workflow, [[secops-integration-sightings-search-workflow|Security Operations Integration - Sightings Search Flow]], that executes the sightings search. This workflow accepts a list of observables, finds any implementing capabilities, creates the queries based on Sightings Search Configurations, and executes the searches based on the configured workflow. Once the search is complete, a note is added to the incident Work notes including whether any sightings were found and if so, how many.

To view Sightings Search Configurations, navigate to **[[security-operations-landing-page|Security Operations]]** &gt; **Integrations** &gt; **Sightings Search Configurations**.

**Note:** If no implementations are available, capability actions are not displayed in product menus.

-   **[[sightings-search-configurations|Create sightings search configuration records]]**  
Create multiple sightings search configuration records and use them while querying multiple log stores or varying the search parameters.

**Parent Topic:**[[integration-capabilities|Integration capabilities]]

**Related topics**  


[Security Operations Integration- Block Request capability]()

[Security Operations Integration- Email Search and Delete capability]()

[Security Operations Integration- Enrich CI capability]()

[Security Operations Integration- Enrich Observable capability]()

[Security Operations Integration- Get Network Statistics capability]()

[Security Operations Integration- Get Running Processes capability]()

[Security Operations Integration- Isolate Host capability]()

[Security Operations Integration- Publish to Watchlist capability]()

[Security Operations Integration - [[tisc-threat-lookup|Threat Lookup]] capability]()

[Change the order of flow execution]()

## Related

- [[secops-integration-sightings-search-workflow|Security Operations Integration - Sightings Search Flow]]
- [[sightings-search-configurations|Create sightings search configuration records]]
- [[integration-capabilities|Integration capabilities]]
- [[indicator-sightings|Sightings]]
- [[c_Observables|Observables]]
- [[security-operations-landing-page|Security Operations]]
- [[tisc-threat-lookup|Threat Lookup]]
