---
title: Security Operations Integration - CI Enrichment flow
description: The Security Operations Integration - CI Enrichment flow allows you to enrich data in configuration items \(CI\) associated with a security incident.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/secops-integ-enrich-ci-wf.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Security Operations Integration- Enrich CI capability, Integration capabilities, Security Operations Integration Reference, Security Operations common functionality, Security Operations]
tags:
  - security-management
  - type-task
---

# Security Operations Integration - CI Enrichment flow

The Security Operations Integration - CI Enrichment flow allows you to enrich data in configuration items \(CI\) associated with a security incident.

## Before you begin

Role required: sn\_si.analyst

## About this task

This flow is triggered from [[sir-landing-page|Security Incident Response]] in two ways.

-   by selecting one or more CIs from the **Configuration Items** tab \(under the **Affected Items** related link\) and selecting **Run CI enrichment** from the **Actions on selected rows** choice list.
-   by opening a CI record and clicking the **Run CI enrichment** related link.

Either method then allows you to specify which implementations to be used to enrich the selected CIs. The associated implementation flows are executed to perform the enrichment.

**Note:** The base system does not include an implementation flow for this capability. To enrich CIs, you must create your own implementation [flow](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/build-workflows/c_WorkflowOverview.md).

\[Omitted image "enrich-ci-flow.png"\] Alt text: Security Operations Integration - CI Enrichment flow

Actions specific to this flow are described here. For more information on other actions, see [[common-wf-activities|Common Security Operations integration flows and orchestration activities]].

The flow process actions include:

-   [[execution-tracking-begin|Execution Tracking - Begin Flow Action]]
-   [Security Operations Integration - CI Enrichment flow](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/secops-integ-enrich-ci-wf.md)
-   [[execution-tracking-noimpls-activity|Capability Execution Tracking- No Impls action]]
-   [[get-supported-security-capabilities-activity|Get Supported Security Capabilities action]]

**Parent Topic:**[[enrich-ci-capability|Security Operations Integration- Enrich CI capability]]

## Related

- [[common-wf-activities|Common Security Operations integration flows and orchestration activities]]
- [[execution-tracking-begin|Execution Tracking - Begin Flow Action]]
- [[execution-tracking-noimpls-activity|Capability Execution Tracking- No Impls action]]
- [[get-supported-security-capabilities-activity|Get Supported Security Capabilities action]]
- [[enrich-ci-capability|Security Operations Integration- Enrich CI capability]]
- [[sir-landing-page|Security Incident Response]]
