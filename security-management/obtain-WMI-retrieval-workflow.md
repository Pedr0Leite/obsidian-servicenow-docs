---
title: Security Operations System Command Integration- Get Running Processes flow
description: The Security Operations System Command Integration - Get Running Processes flow retrieves the running processes of a configuration item when added or updated to a Windows or Unix-based security incident in the Analysis state.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/obtain-WMI-retrieval-workflow.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Security Operations Integration- Get Running Processes capability, Integration capabilities, Security Operations Integration Reference, Security Operations common functionality, Security Operations]
---

# Security Operations System Command Integration- Get Running Processes flow

The [[security-operations-landing-page|Security Operations]] System Command Integration - Get Running Processes flow retrieves the running processes of a configuration item when added or updated to a Windows or Unix-based security incident in the **Analysis** state.

## Before you begin

Role required: sn\_si.analyst

## About this task

For new security incidents, the flow runs automatically when you submit the incident with a selected configuration item, when the state automatically changes to **Analysis**. If it remains in the **Draft** state, then it does not run.

Existing security incidents are automatically updated when you are in the **Analysis** state and you add a new configuration item.

The flow process actions include:

-   [[get-config-FQDN-activity|Get Configuration Item FQDN Flow Action]]
-   [Determine Shell Script by OS activity](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/security-incident-response/determine-shell-script-by-os-activity.md)
-   [[execution-tracking-begin|Execution Tracking - Begin Flow Action]]
-   [[get-running-processes-via-pwrshell-activity|Get Running Processes via PowerShell]]
-   [[execute-shell-script-activity|Execute Shell Script activity]]
-   [[capability-execution-tracking-failure|Capability Execution Tracking- Failure Flow Action]]
-   [[extract-shell-script-mid-script-activity|Extract Shell Script from MID Script activity]]
-   [[combine-results-activity|Combine Results]] and return values in an array
-   [[create-enrich-data-records|Create Enrichment Data records Flow Action]]
-   [[capability-execution-tracking-complete|Capability Execution Tracking - Complete Flow Action]]

\[Omitted image "get-running-processes-flows.png"\] Alt text: Security Operations System Command Integration- Get Running Processes flow

## Procedure

1.  Open a security incident.

2.  Update the **State** to **Analysis**, if necessary.

3.  Add a configuration item \(computer, server, or similar\).

4.  Click **Update**.

    [[c_SecIncRespOrchestration|Security Incident Response Orchestration]] provides running process information in the **Related Link** &gt; **Security Incident Enrichments**tab. For more information, see [[enrichment-data-mapping|Security Operations enrichment data mapping]].

    Actions specific to this flow are described here. For more information on other actions, see [[common-wf-activities|Common Security Operations integration flows and orchestration activities]].


-   **[Combine results activity](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/combine-results-activity.md)**  
The Combine results workflow activity merges the results from third-party integrations to use in the workflow.
-   **[Execute Shell Script activity](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/execute-shell-script-activity.md)**  
The Execute Shell Script workflow activity runs a MID server shell script within the workflow.
-   **[Extract Shell Script from MID Script activity](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/extract-shell-script-mid-script-activity.md)**  
The Extract Shell Script from MID script workflow activity pulls a MID server shell script to use with in the workflow.
-   **[Get Running Processes via PowerShell activity](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/get-running-processes-via-pwrshell-activity.md)**  
The Get Sensor ID workflow activity gathers running processes using PowerShell to use in the workflow.

**Parent Topic:**[[get-running-processes-capability|Security Operations Integration- Get Running Processes capability]]

## Related

- [[get-config-FQDN-activity|Get Configuration Item FQDN Flow Action]]
- [[execution-tracking-begin|Execution Tracking - Begin Flow Action]]
- [[get-running-processes-via-pwrshell-activity|Get Running Processes via PowerShell activity]]
- [[execute-shell-script-activity|Execute Shell Script activity]]
- [[capability-execution-tracking-failure|Capability Execution Tracking- Failure Flow Action]]
- [[extract-shell-script-mid-script-activity|Extract Shell Script from MID Script activity]]
- [[combine-results-activity|Combine results activity]]
- [[create-enrich-data-records|Create Enrichment Data records Flow Action]]
- [[capability-execution-tracking-complete|Capability Execution Tracking - Complete Flow Action]]
- [[enrichment-data-mapping|Security Operations enrichment data mapping]]
- [[common-wf-activities|Common Security Operations integration flows and orchestration activities]]
- [[get-running-processes-capability|Security Operations Integration- Get Running Processes capability]]
- [[security-operations-landing-page|Security Operations]]
- [[c_SecIncRespOrchestration|Security Incident Response Orchestration]]
