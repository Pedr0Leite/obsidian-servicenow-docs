---
title: Execution Tracking - Begin Flow Action
description: The Execution Tracking - Begin flow action starts the auditing process for a Security Operations Integration flow that operates on observables.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/execution-tracking-begin.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Common Security Operations integration flows and orchestration activities, Security Operations Integration Reference, Security Operations common functionality, Security Operations]
tags:
  - security-management
  - type-concept
---

# Execution Tracking - Begin Flow Action

The Execution Tracking - Begin flow action starts the auditing process for a [[security-operations-landing-page|Security Operations]] Integration flow that operates on [[c_Observables|observables]].

The Execution Tracking - Begin flow action can be used with any flow to begin recording the progress of the flow in an audit.

## Results

Possible results for this flow action are:

|Result|Description|
|------|-----------|
|Success|An audit record is created.|

## Input variables

Input variables determine the initial behavior of the flow action.

<table id="table_pgm_tfy_jr"><thead><tr><th>

Variable

</th><th>

Description

</th></tr></thead><tbody><tr><td>

capabilityId

</td><td>

System identifier of the Integration Capability being executed.

</td></tr><tr><td>

isImpl

</td><td>

Flag that specifies whether auditing is done for an Integration Capability flow or an Integration Capability implementation flow. Possible values are: -   false - denotes auditing on an abstract Integration Capability flow such as [[indicator-sightings|Sightings]] Search. \(default.\)
-   true - denotes auditing on an Integration Capability implementation flow. For example, Splunk or Elasticsearch.

</td></tr><tr><td>

taskId

</td><td>

System identifier for any task associated with the flow.

</td></tr><tr><td>

observableList

</td><td>

One or more observable SysIDs to perform the desired action. Used as a flow input.

</td></tr><tr><td>

flowContextId

</td><td>

System identifier of the associated flow context record. Supplied by the system.

</td></tr><tr><td>

flowName

</td><td>

Name of the flow. Supplied by the system.

</td></tr><tr><td>

parentCapabilityExcutionId

</td><td>

System identifier of the audit record that launched the implementation flow. Only required for Integration Capability implementation flows such as Splunk, Elasticsearch, and VirusTotal.

</td></tr></tbody>
</table>## Output variables

The output variables contain data that can be used in subsequent actions.

|Variable|Description|
|--------|-----------|
|capabilityExecutionId|System identifier of the audit record.|

-   [[get-supported-security-capabilities-activity|Get Supported Security Capabilities action]]
-   [[execution-tracking-noimpls-activity|Capability Execution Tracking- No Impls action]]

**Parent Topic:**[[common-wf-activities|Common Security Operations integration flows and orchestration activities]]

## Related

- [[get-supported-security-capabilities-activity|Get Supported Security Capabilities action]]
- [[execution-tracking-noimpls-activity|Capability Execution Tracking- No Impls action]]
- [[common-wf-activities|Common Security Operations integration flows and orchestration activities]]
- [[security-operations-landing-page|Security Operations]]
- [[c_Observables|Observables]]
- [[indicator-sightings|Sightings]]
