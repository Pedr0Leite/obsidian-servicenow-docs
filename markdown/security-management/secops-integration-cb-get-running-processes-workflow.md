---
title: Security Operations Carbon Black Integration - Get Running Processes Flow
description: The Security Operations Carbon Black Integration - Get Running Processes is the implementation for the Carbon Black integration launched by the Security Operations Integration - Get Running Process flow.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/secops-integration-cb-get-running-processes-workflow.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Security Operations Integration- Get Running Processes capability, Integration capabilities, Security Operations Integration Reference, Security Operations common functionality, Security Operations]
---

# Security Operations Carbon Black Integration - Get Running Processes Flow

The [[security-operations-landing-page|Security Operations]] [[carbon-black-landing-page|Carbon Black Integration]] - Get Running Processes is the implementation for the Carbon Black integration launched by the Security Operations Integration - Get Running Process flow.

Role required: sn\_si.analyst

\[Omitted image "carbon-black-get-running-proccess-1.png"\] Alt text: Flow Design for Security Operations Carbon Black Integration - Get Running Processes 1 \[Omitted image "carbon-black-get-running-proccess-2.png"\] Alt text: Flow Design for Security Operations Carbon Black Integration - Get Running Processes 2 \[Omitted image "carbon-black-get-running-proccess-3.png"\] Alt text: Flow Design for Security Operations Carbon Black Integration - Get Running Processes 3 \[Omitted image "carbon-black-get-running-proccess-4.png"\] Alt text: Flow Design for Security Operations Carbon Black Integration - Get Running Processes 4 \[Omitted image "carbon-black-get-running-proccess-5.png"\] Alt text: Flow Design for Security Operations Carbon Black Integration - Get Running Processes 5

Actions specific to this flow are described here. For more information on other actions, see [[common-wf-activities|Common Security Operations integration flows and orchestration activities]].

-   **[[collect-cb-config-activity|Collect Carbon Black Configurations Flow Action]]**  
The Collect Carbon Black Configurations flow action gathers configuration information to use in the flow.
-   **[[check-mid-server-status|Check MID Server Status]]**  
Determines whether the MID Server identified in the **MID Server Host** field of the integration's configuration is up and running. If the field is set to **Any**, the flow action verifies that any MID Server is up and running.
-   **[[get-sensor-id-activity|Get Sensor ID Flow Action]]**  
The Get Sensor ID flow action gathers sensor identifiers to use in the flow.
-   **[[create-session-activity|Create Session Flow Action]]**  
The Create Session flow action establishes a Carbon Black session to use in the flow.
-   **[[check-session-status-activity|Check Session Status Flow Action]]**  
Determines the status of a Carbon Black session within the flow.
-   **[[create-command-process-activity|Create Command Process Flow Action]]**  
The Create Command Process flow action create a Carbon Black command process to use in the flow .
-   **[[check-command-status-get-process-activity|Check Command Status and Get Process Flow Action]]**  
Checks the Carbon Black command status and retrieves processes to use in the flow.
-   **[[map-processes-data-activity|Map Processes Data Flow Action]]**  
The Map Processes Data flow action maps Carbon Black process data within the flow.
-   **[[capability-execution-tracking-complete|Capability Execution Tracking - Complete Flow Action]]**  
The Capability Execution Tracking - Complete flow action updates the audit record when the flow is complete.
-   **[[close-session-activity|Close Session Flow Action]]**  
Closes a Carbon Black session within the flow.

**Parent Topic:**[[get-running-processes-capability|Security Operations Integration- Get Running Processes capability]]

## Related

- [[common-wf-activities|Common Security Operations integration flows and orchestration activities]]
- [[collect-cb-config-activity|Collect Carbon Black Configurations Flow Action]]
- [[check-mid-server-status|Check MID Server Status]]
- [[get-sensor-id-activity|Get Sensor ID Flow Action]]
- [[create-session-activity|Create Session Flow Action]]
- [[check-session-status-activity|Check Session Status Flow Action]]
- [[create-command-process-activity|Create Command Process Flow Action]]
- [[check-command-status-get-process-activity|Check Command Status and Get Process Flow Action]]
- [[map-processes-data-activity|Map Processes Data Flow Action]]
- [[capability-execution-tracking-complete|Capability Execution Tracking - Complete Flow Action]]
- [[close-session-activity|Close Session Flow Action]]
- [[get-running-processes-capability|Security Operations Integration- Get Running Processes capability]]
- [[security-operations-landing-page|Security Operations]]
- [[carbon-black-landing-page|Carbon Black integration]]
