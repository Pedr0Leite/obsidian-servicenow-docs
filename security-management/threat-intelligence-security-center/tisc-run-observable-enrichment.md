---
title: Run Observable Enrichment
description: Select one or more implementations as applicable to run threat lookup on observables.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/threat-intelligence-security-center/tisc-run-observable-enrichment.html
release: australia
product: Threat Intelligence Security Center
classification: threat-intelligence-security-center
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Run Enrichment operations in TISC, Observables, TISC Library Repository, Threat Intelligence Security Center Library, Use, Threat Intelligence Security Center, Security Operations]
---

# Run Observable Enrichment

Select one or more implementations as applicable to [[tisc-run-threat-lookup|run threat lookup]] on [[c_Observables|observables]].

## Before you begin

Role required: sn\_sec\_tisc.admin

## Procedure

1.  Navigate to **Workspaces** &gt; **[[tisc-landing-page|Threat Intelligence Security Center]]**.

2.  Click **[[threat-analyst-workbench|Threat Analyst Workbench]]** icon.

3.  Go to **Observables** &gt; **All Observables**.

4.  Open any observable record.

5.  Click **Run Observable Enrichment**.

    The Run Observable Enrichment **[[implementation-selection|Select Implementations]]** modal screen is displayed.

    **Note:** Only supported records will be submitted against the selected implementation\(s\)

6.  Select the required implementation\(s\) \(for example, WHOIS\) from the list.

    \[Omitted image "tisc-run-observable-enrichment.png"\] Alt text: Run Observable Enrichment

7.  Click **Submit**.

    The selected enrichment action will be executed and an information message is displayed that [[tisc-threat-lookup|Threat lookup]] execution has started.

    **Note:**

    -   Once the execution initiated or completed, a work notes is posted on the activity stream of the form view.
    -   The enrichment results pushed from SIR workspace can be found in the **Enrichment Results** tab of that corresponding Observables details page in [[view-threat-intelligence-security-center-homepage|TISC Workspace]].
    -   The enrichment results pushed from SIR workspace can be identified using **Source** field of the enrichment result table.

**Parent Topic:**[Run Enrichment operations in TISC](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/tisc-unified-experience-capabilities-and-modal-screens.md)

## Related

- [[tisc-run-threat-lookup|Run Threat Lookup]]
- [[c_Observables|Observables]]
- [[tisc-landing-page|Threat Intelligence Security Center]]
- [[threat-analyst-workbench|Threat Analyst Workbench]]
- [[implementation-selection|Select implementations]]
- [[tisc-threat-lookup|Threat Lookup]]
- [[view-threat-intelligence-security-center-homepage|TISC Workspace]]
