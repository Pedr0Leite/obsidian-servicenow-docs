---
title: Security Operations Integration - Threat Lookup Flow
description: The Security Operations Integration - Threat Lookup capability flow accesses available threat lookup implementations and executes the implementation flows associated with each to perform threat lookups of selected observables.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/sec-ops-integ-threat-lookup.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Security Operations Integration - Threat Lookup capability, Integration capabilities, Security Operations Integration Reference, Security Operations common functionality, Security Operations]
---

# Security Operations Integration - Threat Lookup Flow

The **[[security-operations-landing-page|Security Operations]] Integration - [[tisc-threat-lookup|Threat Lookup]]** capability flow accesses available threat lookup implementations and executes the implementation flows associated with each to perform threat lookups of selected [[c_Observables|observables]].

## Before you begin

Role required: sn\_ti.write

## About this task

This flow can be triggered in these ways.

-   by selecting one or more observables from the Observables list and selecting **[[tisc-run-threat-lookup|Run threat lookup]]** from the **Actions on selected rows** choice list.
-   by opening an observable record and clicking the **Run threat lookup** related link.
-   From the Observables related list in a security incident.

Each method then allows you to specify which lookup implementations to be used to scan the selected observables. The associated implementation flows are executed to perform the lookups.

\[Omitted image "threat-lookup-flow.png"\] Alt text: Security Operations Integration - Threat Lookup

Actions specific to this flow are described here. For more information on other actions, see [[common-wf-activities|Common Security Operations integration flows and orchestration activities]].

The flow process actions include:

-   [[get-supported-security-capabilities-activity|Get Supported Security Capabilities action]]
-   [[execution-tracking-noimpls-activity|Capability Execution Tracking- No Impls action]]

**Parent Topic:**[[sec-ops-threat-lookups-capability|Security Operations Integration - Threat Lookup capability]]

## Related

- [[common-wf-activities|Common Security Operations integration flows and orchestration activities]]
- [[get-supported-security-capabilities-activity|Get Supported Security Capabilities action]]
- [[execution-tracking-noimpls-activity|Capability Execution Tracking- No Impls action]]
- [[sec-ops-threat-lookups-capability|Security Operations Integration - Threat Lookup capability]]
- [[security-operations-landing-page|Security Operations]]
- [[tisc-threat-lookup|Threat Lookup]]
- [[c_Observables|Observables]]
- [[tisc-run-threat-lookup|Run Threat Lookup]]
