---
title: Security Operations Integration - Enrich Observable flow
description: The Security Operations Integration - Enrich Observable sub flow allows you to enrich observables with additional information from a variety of sources using implementation flow designer.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/secops-integration-enrich-observ-wf.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Security Operations Integration- Enrich Observable capability, Integration capabilities, Security Operations Integration Reference, Security Operations common functionality, Security Operations]
tags:
  - security-management
  - type-task
---

# Security Operations Integration - Enrich Observable flow

The [[security-operations-landing-page|Security Operations]] Integration - Enrich Observable sub flow allows you to enrich [[c_Observables|observables]] with additional information from a variety of sources using implementation flow designer.

## Before you begin

Role required: sn\_si.analyst

## About this task

This flow can be triggered from either [[sir-landing-page|Security Incident Response]] or [[threat-intel-landing-page|Threat Intelligence]] in two ways.

-   by selecting one or more observables from the Observables list and selecting **[[tisc-run-observable-enrichment|Run observable enrichment]]** from the **Actions on selected rows** choice list.
-   by opening an observable record and clicking the **Run observable enrichment** related link.

Either method then allows you to specify which implementations to be used to enrich the selected observables. The associated implementation flows are executed to perform the enrichment.



\[Omitted image "flows-enrich-observables.png"\] Alt text: Security Operations Integration - Enrich Observable

Actions specific to this flow are described here. For more information on other actions, see [[common-wf-activities|Common Security Operations integration flows and orchestration activities]].

The flow process actions include:

-   [[execution-tracking-noimpls-activity|Capability Execution Tracking- No Impls action]]
-   [[get-supported-security-capabilities-activity|Get Supported Security Capabilities action]][Capability Execution Tracking- No Impls action](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/execution-tracking-noimpls-activity.md)

**Parent Topic:**[[enrich-observable-capability|Security Operations Integration- Enrich Observable capability]]

## Related

- [[common-wf-activities|Common Security Operations integration flows and orchestration activities]]
- [[execution-tracking-noimpls-activity|Capability Execution Tracking- No Impls action]]
- [[get-supported-security-capabilities-activity|Get Supported Security Capabilities action]]
- [[enrich-observable-capability|Security Operations Integration- Enrich Observable capability]]
- [[security-operations-landing-page|Security Operations]]
- [[c_Observables|Observables]]
- [[sir-landing-page|Security Incident Response]]
- [[threat-intel-landing-page|Threat Intelligence]]
- [[tisc-run-observable-enrichment|Run Observable Enrichment]]
