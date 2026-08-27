---
title: View information in a security incident
description: You can perform several other actions on an existing security incident using the related links.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/security-incident-response/perform-addtl-tasks-on-si.html
release: australia
product: Security Incident Response
classification: security-incident-response
topic_type: task
last_updated: "2026-06-25"
reading_time_minutes: 3
breadcrumb: [Managing security incidents and inbound requests, Security Incident Response, Enterprise security case management applications, Security Operations]
tags:
  - security-management
  - sir
  - security-incidents
  - investigation
  - soar
  - type-task
---

# View information in a security incident

You can perform several other actions on an existing security incident using the related links.

## Before you begin

Role required: sn\_si.basic

## Procedure

1.  If it is not already open, open the security incident you want to update.

2.  Within **Related Links**, you can perform the following tasks,

<table id="choicetable_k4s_q45_c5"><tbody><tr><td id="d217482e56">

**[View Manual Runbook](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/security-incident-response/setup-assistant-reference.md)**

</td><td>

View a list of runbooks available for this security incident.

</td></tr><tr><td id="d217482e72">

**Response Workflow**

</td><td>

View any workflow associated with this incident.

</td></tr><tr><td id="d217482e81">

**[Add Multiple Observables](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/security-incident-response/add-multiple-si-observables.md)**

</td><td>

Adds a list of [[c_Observables|observables]] in comma, new line, tab, or pipe delimited formats.

</td></tr><tr><td id="d217482e97">

**[[case-mgmt|Add to Security Case]]**

</td><td>

Adds the security incident to one or more security cases. You can also create a new security case and add this security incident to it.

</td></tr><tr><td id="d217482e115">

**Get QRadar IP Summaries**

</td><td>

If a QRadar integration is available, and contains valid CIs, source, and destination IP addresses, it triggers the QRadar workflows and displays the results in work notes.

</td></tr><tr><td id="d217482e125">

**Run Orchestration**

</td><td>

Choose and run a [[security-operations-landing-page|Security Operations]] workflow.

</td></tr><tr><td id="d217482e134">

**[View SLA timeline](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/t_ViewSLATimeline.md)**

</td><td>

You can view an SLA timeline from a Task SLA record or from an SLA definition.

</td></tr><tr><td id="d217482e148">

**Show All Related Lists**

</td><td>

Displays all standard related lists and any lists added manually. **Note:** Manually added items are available only in this view.

</td></tr><tr><td id="d217482e160">

**[Show Affected Items](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/security-incident-response/show-affected-items-for-si.md)**

</td><td>

Displays the lists of CIs, users, and services directly affected by this incident

</td></tr><tr><td id="d217482e176">

**[Show Related Items](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/security-incident-response/show-related-items-for-si.md)**

</td><td>

Displays the lists of related incidents, CIs, users, and groups affected by this incident.

</td></tr><tr><td id="d217482e192">

**[Show IoC](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/security-incident-response/show-ioc-info-for-si.md)**

</td><td>

Displays the lists of observables, [[indicator|indicators]], [[threat-intelligence-malware|malware]], modes and methods, and security scan requests associated with this incident.

</td></tr><tr><td id="d217482e209">

**[Show Enrichment Data](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/security-incident-response/show-enrich-data-for-si.md)**

</td><td>

Displays the lists of enrichment data, processes, services, statistics, lookups, firewall logs, and compromised user information associated with this incident.

</td></tr><tr><td id="d217482e225">

**[Show Response Tasks](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/security-incident-response/show-response-tasks-for-si.md)**

</td><td>

Displays the lists of tasks, SLAs, risk score audits, outages, and Exchange searches associated with this incident.

</td></tr><tr><td id="d217482e241">

**View Details in External System**

</td><td>

If this security incident was generated from an external application, directly or by events, and a link to the originating data was provided, the **View Details in External System** action opens the URL. You can view and search through the logs that generated this incident.

</td></tr><tr><td id="d217482e256">

**[Scan for Vulnerabilities](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/security-incident-response/t_SubmitThrtReqFromSecInc.md)**

</td><td>

If [[vuln-landing-page|Vulnerability Response]] is activated, and you have selected at least one affected CI for the security incident, you can submit a scan request to determine what [[vulnerabilities|vulnerabilities]] exist on the CI.

</td></tr></tbody>
</table>

## Related

- [[case-mgmt|Security Case Management]]
- [[c_Observables|Observables]]
- [[security-operations-landing-page|Security Operations]]
- [[indicator|Indicators]]
- [[threat-intelligence-malware|Malware]]
- [[vuln-landing-page|Vulnerability Response]]
- [[vulnerabilities|Vulnerabilities]]
