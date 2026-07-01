---
title: Security Operations Integrations - Get Network Statistics flow
description: The Security Operations Integrations - Get Network Statistics flow retrieves a list of active network connections from a host or endpoint.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/secops-integration-get-network-stats-workflow.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Security Operations Integration- Get Network Statistics capability, Integration capabilities, Security Operations Integration Reference, Security Operations common functionality, Security Operations]
tags:
  - security-management
  - type-task
---

# Security Operations Integrations - Get Network Statistics flow

The Security Operations Integrations - Get Network Statistics flow retrieves a list of active network connections from a host or endpoint.

## Before you begin

Role required: sn\_si.analyst

## About this task

This flow runs automatically when a configuration item is added to a security incident.

\[Omitted image "get-network-statistics-flow.png"\] Alt text: Security Operations Integrations - Get Network Statistics flow

Actions specific to this flow are described here. For more information on other actions, see [[common-wf-activities|Common Security Operations integration flows and orchestration activities]].

The flow actions include:

-   [[determine-cis-activity|Capability - Determine CIs activity]]
-   
.

-   **[[execution-tracking-begins-cis-activity|Execution Tracking - Begin \(CIs\) Flow Action]]**  
The **Execution Tracking - Begin \(CIs\)** flow action starts the auditing process for a [[security-operations-landing-page|Security Operations]] Integration flow that operates on configuration items \(CIs\).

**Parent Topic:**[[get-network-statistics-capability|Security Operations Integration- Get Network Statistics capability]]

## Related

- [[common-wf-activities|Common Security Operations integration flows and orchestration activities]]
- [[determine-cis-activity|Capability - Determine CIs activity]]
- [[execution-tracking-begins-cis-activity|Execution Tracking - Begin \(CIs\) Flow Action]]
- [[get-network-statistics-capability|Security Operations Integration- Get Network Statistics capability]]
- [[security-operations-landing-page|Security Operations]]
