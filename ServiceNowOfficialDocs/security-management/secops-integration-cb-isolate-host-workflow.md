---
title: Security Operations Carbon Black Integration - Isolate Host Flow
description: The Security Operations Carbon Black Integration - Isolate Host is the implementation for the Carbon Black integration launched by the Security Operations Integration - Isolate Host flow.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/secops-integration-cb-isolate-host-workflow.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Security Operations Integration- Isolate Host capability, Integration capabilities, Security Operations Integration Reference, Security Operations common functionality, Security Operations]
---

# Security Operations Carbon Black Integration - Isolate Host Flow

The [[security-operations-landing-page|Security Operations]] [[carbon-black-landing-page|Carbon Black Integration]] - Isolate Host is the implementation for the Carbon Black integration launched by the Security Operations Integration - Isolate Host flow.

## Before you begin

Role required: sn\_si.analyst

## About this task

The flow process activities include:

-   [[execution-tracking-begins-cis-activity|Execution Tracking - Begin \(CIs\) Flow Action]]
-   [[get-ip-from-ci-activity|Get IP from CI]]
-   [[collect-cb-config-activity|Collect Carbon Black configurations]]
-   [[capability-execution-tracking-failure|Capability Execution Tracking- Failure Flow Action]]
-   [[get-sensor-id-activity|Get Sensor ID]]
-   [Set Network Isolation Enabled activity](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown)
-   [[update-sensor-activity|Update Sensor]] - returns Isolate Host result.
-   [[capability-execution-tracking-complete|Capability Execution Tracking - Complete Flow Action]]

\[Omitted image "carbon-black-integration-isolate-host-flow-v1.png"\] Alt text: Flow designer for Security Operations Carbon Black Integration - Isolate Host\[Omitted image "carbon-black-integration-isolate-host-flow-v1-2.png"\] Alt text: Flow designer for Security Operations Carbon Black Integration - Isolate Host

Activities specific to this flow are described here. For more information on other activities, see [[common-wf-activities|Common Security Operations integration flows and orchestration activities]].

-   **[Get Sensor ID Flow Action](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/get-sensor-id-activity.md)**  
The Get Sensor ID flow action gathers sensor identifiers to use in the flow.
-   **[Set Network Isolation Enabled activity](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown)**  
The Set Network Isolation Enabled workflow activity enables network isolation.
-   **[Update Sensor activity](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/update-sensor-activity.md)**  
The Update Sensor workflow activity updates the sensor to isolate hosts or endpoints.

**Parent Topic:**[[isolate-host-capability|Security Operations Integration- Isolate Host capability]]

## Related

- [[execution-tracking-begins-cis-activity|Execution Tracking - Begin \(CIs\) Flow Action]]
- [[get-ip-from-ci-activity|Get IP from CI activity]]
- [[collect-cb-config-activity|Collect Carbon Black Configurations Flow Action]]
- [[capability-execution-tracking-failure|Capability Execution Tracking- Failure Flow Action]]
- [[get-sensor-id-activity|Get Sensor ID Flow Action]]
- [[update-sensor-activity|Update Sensor activity]]
- [[capability-execution-tracking-complete|Capability Execution Tracking - Complete Flow Action]]
- [[common-wf-activities|Common Security Operations integration flows and orchestration activities]]
- [[isolate-host-capability|Security Operations Integration- Isolate Host capability]]
- [[security-operations-landing-page|Security Operations]]
- [[carbon-black-landing-page|Carbon Black integration]]
