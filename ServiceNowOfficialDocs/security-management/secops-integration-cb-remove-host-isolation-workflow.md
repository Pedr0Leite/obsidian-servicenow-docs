---
title: Security Operations Carbon Black Integration- Remove Host Isolation Flow
description: The Security Operations Carbon Black Integration - Remove Host Isolation flow unblocks communication with a specified host or endpoint in a Carbon Black system.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/secops-integration-cb-remove-host-isolation-workflow.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Security Operations Integration- Isolate Host capability, Integration capabilities, Security Operations Integration Reference, Security Operations common functionality, Security Operations]
tags:
  - security-management
  - type-task
---

# Security Operations Carbon Black Integration- Remove Host Isolation Flow

The **[[security-operations-landing-page|Security Operations]] [[carbon-black-landing-page|Carbon Black Integration]] - Remove Host Isolation** flow unblocks communication with a specified host or endpoint in a Carbon Black system.

## Before you begin

Role required: sn\_si.analyst

## About this task

This flow is not part of a capability and needs a custom orchestration in order to run.

The flow process activities include:

-   [[get-ip-from-ci-activity|Get IP from CI activity]]
-   If successful- [[collect-cb-config-activity|Collect Carbon Black Configurations Flow Action]]
-   [[get-sensor-id-activity|Get Sensor ID Flow Action]][Get Sensor ID](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/get-sensor-id-activity.md)
-   If- Device supports isolation- and device is not isolated to disabled.
-   [[update-sensor-activity|Update Sensor activity]]- returns Isolate Host result.

\[Omitted image "RemoveHostIsolationWorkflow.png"\] Alt text: Remove Host Isolation low diagram

**Parent Topic:**[[isolate-host-capability|Security Operations Integration- Isolate Host capability]]

## Related

- [[get-ip-from-ci-activity|Get IP from CI activity]]
- [[collect-cb-config-activity|Collect Carbon Black Configurations Flow Action]]
- [[get-sensor-id-activity|Get Sensor ID Flow Action]]
- [[update-sensor-activity|Update Sensor activity]]
- [[isolate-host-capability|Security Operations Integration- Isolate Host capability]]
- [[security-operations-landing-page|Security Operations]]
- [[carbon-black-landing-page|Carbon Black integration]]
