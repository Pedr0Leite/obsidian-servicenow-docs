---
title: Common Security Operations integration flows and orchestration activities
description: Many of the flows associated with third-party integrations include the same activities. For example, activities for beginning and completing processing.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/common-wf-activities.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Security Operations Integration Reference, Security Operations common functionality, Security Operations]
tags:
  - security-management
  - type-concept
---

# Common Security Operations integration flows and orchestration activities

Many of the flows associated with third-party integrations include the same activities. For example, activities for beginning and completing processing.

-   **[[execution-tracking-begin|Execution Tracking - Begin Flow Action]]**  
The Execution Tracking - Begin flow action starts the auditing process for a [[security-operations-landing-page|Security Operations]] Integration flow that operates on [[c_Observables|observables]].
-   **[[capability-execution-tracking-complete|Capability Execution Tracking - Complete Flow Action]]**  
The Capability Execution Tracking - Complete flow action updates the audit record when the flow is complete.
-   **[[capability-execution-tracking-failure|Capability Execution Tracking- Failure Flow Action]]**  
The Capability Execution Tracking - Failure flow action records a failure to the audit record.
-   **[[determine-cis-activity|Capability - Determine CIs activity]]**  
The Capability - Determine CIs workflow activity determines which configuration items \(CIs\) to include in the workflow.
-   **[[create-enrich-data-records|Create Enrichment Data records Flow Action]]**  
The **Create enrichment data records** flow action creates or updates enrichment records to use in the flow.
-   **[[get-config-FQDN-activity|Get Configuration Item FQDN Flow Action]]**  
The **Security Common Orchestration** &gt; **Get Configuration Item FQDN** flow action retrieves the fully qualified domain name \(FQDN\) of a configuration item. This flow action can accelerate the investigation and remediation process.
-   **[[determine-observables-activity|Determine Observables activity]]**  
The **Determine Observables** workflow activity determines which observable to include in the workflow
-   **[[get-supported-security-capabilities-activity|Get Supported Security Capabilities action]]**  
The Get Supported Capabilities flow action retrieves the name and number of integrations that are active and support the requested capability.
-   **[[execution-tracking-noimpls-activity|Capability Execution Tracking- No Impls action]]**  
The Capability Execution Tracking - No Impls flow action creates an error record when no integration capability implementation is found.
-   **[[get-email-details-from-exch-server|Create Compliance Search Action]]**  
The Create Compliance Search action creates a compliance search for emails in the designated Exchange server\(s\) using the search queries defined and returns the name of compliance search created.
-   **[Get IP from CI activity](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown)**  
This workflow activity determines the IPV4 address associated with a configuration item \(CI\).
-   **[[get-network-stats-netstat-activity|Get Network Statistics via netstat Flow Action]]**  
The Security Common Orchestration - Get Network Statistics via netstat flow action retrieves the network statistics for an affected resource on a Windows-based system. This flow action can accelerate the investigation and remediation process.
-   **[[get-running-process-WMI-activity|Get running processes via WMI activity]]**  
The**Get Running Processes** workflow activity retrieves the running processes of a configuration item on a Windows-based system. This activity can accelerate the investigation and remediation process.
-   **[[search-delete-email-threat-exchange|Check Compliance Search Status Action]]**  
The Check Compliance Search Status action check the status of created compliance search on exchange server and if the status is completed return the information regarding email search found for the compliance search.
-   **[[update-task-worknotes-activity|Update Task Worknotes activity]]**  
The **Security Common Orchestration - Update Task Worknotes** workflow activity updates the **Activity** section \(work notes\) of a task record. This is useful for logging information.
-   **[[r_RollUpScanInfoSI|Roll up lookup info to security incident activity]]**  
The **Roll up lookup info to security incident** activity can be used with any workflow to gather information from a [[tisc-threat-lookup|threat lookup]] and output a summary of the contents as well as the ID of the originating security incident in task work notes.
-   **[[t_UpdateSecIncScanResults|Update security incident with lookup results workflow]]**  
The **Update security incident with lookup results** workflow updates existing security incidents with lookup results.
-   **[[filter-whitelisted-observables-activity|Filter Allowlisted Observables activity]]**  
The Filtered Allowlisted Observables workflow activity removes observables that can be ignored from the list of observables. This activity can accelerate the investigation and remediation process.
-   **[[write-content-record-attachment-activity|Write content to record as attachment activity]]**  
This activity writes the content passed in from an input and creates a designated attachment to a given record.
-   **[[get-ip-from-ci-activity|Get IP from CI activity]]**  
The Get IP from CI flow activity gathers the IP address from configuration items \(CIs\) to use in the flow.

**Parent Topic:**[[secops-integ-ref|Security Operations Integration Reference]]

## Related

- [[execution-tracking-begin|Execution Tracking - Begin Flow Action]]
- [[capability-execution-tracking-complete|Capability Execution Tracking - Complete Flow Action]]
- [[capability-execution-tracking-failure|Capability Execution Tracking- Failure Flow Action]]
- [[determine-cis-activity|Capability - Determine CIs activity]]
- [[create-enrich-data-records|Create Enrichment Data records Flow Action]]
- [[get-config-FQDN-activity|Get Configuration Item FQDN Flow Action]]
- [[determine-observables-activity|Determine Observables activity]]
- [[get-supported-security-capabilities-activity|Get Supported Security Capabilities action]]
- [[execution-tracking-noimpls-activity|Capability Execution Tracking- No Impls action]]
- [[get-email-details-from-exch-server|Create Compliance Search Action]]
- [[get-network-stats-netstat-activity|Get Network Statistics via netstat Flow Action]]
- [[get-running-process-WMI-activity|Get running processes via WMI activity]]
- [[search-delete-email-threat-exchange|Check Compliance Search Status Action]]
- [[update-task-worknotes-activity|Update Task Worknotes activity]]
- [[r_RollUpScanInfoSI|Roll up lookup info to security incident activity]]
- [[t_UpdateSecIncScanResults|Update security incident with lookup results workflow]]
- [[filter-whitelisted-observables-activity|Filter Allowlisted Observables activity]]
- [[write-content-record-attachment-activity|Write content to record as attachment activity]]
- [[get-ip-from-ci-activity|Get IP from CI activity]]
- [[secops-integ-ref|Security Operations Integration Reference]]
- [[security-operations-landing-page|Security Operations]]
- [[c_Observables|Observables]]
- [[tisc-threat-lookup|Threat Lookup]]
