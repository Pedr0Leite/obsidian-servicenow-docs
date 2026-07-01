---
title: Security Operations Integration- Isolate Host capability
description: The Isolate Host capability restricts system connections to other devices. Isolate host is executed against a configuration item \(CI\).
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/isolate-host-capability.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Integration capabilities, Security Operations Integration Reference, Security Operations common functionality, Security Operations]
tags:
  - security-management
  - type-concept
---

# Security Operations Integration- Isolate Host capability

The **Isolate Host** capability restricts system connections to other devices. Isolate host is executed against a configuration item \(CI\).

The **Isolate Host** capability has a flow, [[secops-integration-isolate-host-workflow|Security Operations - Isolate Host Flow]] that accepts one or more CIs and optionally an implementation. You can specify an implementation to use to isolate the host or for the flow to attempt to isolate the host using all implementations.

**Note:** While not integrated with a capability, a flow, [[secops-integration-cb-remove-host-isolation-workflow|Security Operations Carbon Black Integration- Remove Host Isolation Flow]] is available for orchestration to restore communication with an isolated host.

**Note:** If no implementations are available, capability actions are not displayed in product menus.

-   **[[run-isolate-host|Run Isolate Host]]**  
**Isolate Host** restricts system connections to other devices.
-   **[Security Operations - Isolate Host Flow](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/secops-integration-isolate-host-workflow.md)**  
The **[[security-operations-landing-page|Security Operations]] - Isolate Host** flow is a high-level flow independent of integrations. It uses the configured queries to search for a set of configuration items. Use it to fulfill an integration, such as Carbon Black.
-   **[[secops-integration-cb-isolate-host-workflow|Security Operations Carbon Black Integration - Isolate Host Flow]]**  
The Security Operations [[carbon-black-landing-page|Carbon Black Integration]] - Isolate Host is the implementation for the Carbon Black integration launched by the Security Operations Integration - Isolate Host flow.
-   **[Security Operations Carbon Black Integration- Remove Host Isolation Flow](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/secops-integration-cb-remove-host-isolation-workflow.md)**  
The **Security Operations Carbon Black Integration - Remove Host Isolation** flow unblocks communication with a specified host or endpoint in a Carbon Black system.

**Parent Topic:**[[integration-capabilities|Integration capabilities]]

**Related topics**  


[Security Operations Integration- Block Request capability]()

[Security Operations Integration- Email Search and Delete capability]()

[Security Operations Integration- Enrich CI capability]()

[Security Operations Integration- Enrich Observable capability]()

[Security Operations Integration- Get Network Statistics capability]()

[Security Operations Integration- Get Running Processes capability]()

[Security Operations Integration- Publish to Watchlist capability]()

[Security Operations Integration- [[indicator-sightings|Sightings]] Search capability]()

[Security Operations Integration - [[tisc-threat-lookup|Threat Lookup]] capability]()

[Change the order of flow execution]()

## Related

- [[secops-integration-isolate-host-workflow|Security Operations - Isolate Host Flow]]
- [[secops-integration-cb-remove-host-isolation-workflow|Security Operations Carbon Black Integration- Remove Host Isolation Flow]]
- [[run-isolate-host|Run Isolate Host]]
- [[secops-integration-cb-isolate-host-workflow|Security Operations Carbon Black Integration - Isolate Host Flow]]
- [[integration-capabilities|Integration capabilities]]
- [[security-operations-landing-page|Security Operations]]
- [[carbon-black-landing-page|Carbon Black integration]]
- [[indicator-sightings|Sightings]]
- [[tisc-threat-lookup|Threat Lookup]]
