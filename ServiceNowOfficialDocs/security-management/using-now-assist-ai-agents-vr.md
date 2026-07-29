---
title: Using agentic workflows
description: Use AI agents to complete your tasks autonomously.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/using-now-assist-ai-agents-vr.html
release: australia
topic_type: concept
last_updated: "2026-05-26"
reading_time_minutes: 3
keywords: [AI agents, agentic AI]
breadcrumb: [Now Assist in Unified Security Exposure Management, Explore, Unified Security Exposure Management, Security Operations]
tags:
  - security-management
  - type-concept
---

# Using agentic workflows

Use AI agents to complete your tasks autonomously.

**Note:** Depending on your license, you will have access to certain application features, generative AI skills, agentic workflows, and AI agents. For more information, see [ServiceNow product tiers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/ai-native-sku-overview.md).

<table id="table_lpw_nx2_r2c"><thead><tr><th>

Agentic workflow name

</th><th>

Description

</th><th>

Available AI agents

</th><th>

Supported workspaces

</th></tr></thead><tbody><tr><td>

Security Exposure 360

</td><td>

[[now-assist-review-vulnerability-exposure-data|Evaluate vulnerability exposure data with Security Exposure 360]].Vulnerability analysts and remediation owners can enter questions in plain language and receive comprehensive answers about all types of findings that include host, container, and test results [[vulnerabilities|vulnerabilities]].

</td><td>

Data Analysis AI Agent

</td><td>

Legacy and [[unified-security-exposure-management-landing-page|Unified Security Exposure Management \(USEM\)]]

</td></tr><tr><td>

Guardrails detector agentic workflow

</td><td>

[[exploring-ai-security-exposure|Manage potential AI exposures]]Use the AI agent to ask about the guardrails that were identified by the AI skill component in the AI Guardrails Helper, automatically defer findings with existing mitigations in the form of guardrails, or create exception rules to auto-defer future findings.

</td><td>

Guardrails detector agentic workflow

</td><td>

Unified Security Exposure Management \(USEM\)

</td></tr><tr><td>

Assess vulnerability exposure

</td><td>

[[assess-exposure-vr-aiagent|Assess your vulnerability exposure]]-   Determine if your configuration items \(CIs\) and business services are exposed to known vulnerabilities.
-   Determine the potential impact that a specific vulnerability might have throughout your environment.
-   Check CIs for any new Cybersecurity and [[threat-intelligence-infrastructure|Infrastructure]] Security Agency \(CISA\) exploitable \(zero-day\) vulnerabilities.
-   Create watch topics in the [[vulnerability-manager-workspace-landing-page|Vulnerability Manager workspace]] to remediate vulnerable items.

</td><td>

-   CISA vulnerability analysis AI agent
-   Vulnerability exposure analysis AI agent
-   Watch topic creation AI agent

</td><td>

Legacy and Unified Security Exposure Management \(USEM\)

</td></tr><tr><td>

Retrieve vulnerability and exposure data

</td><td>

[[retrieve-vr-data|Retrieve Vulnerability and exposure data with generative AI]].Ask questions in natural language to help you quickly retrieve vulnerability and exposure data across legacy sources and Unified Security Exposure Management \(USEM\).

</td><td>

Retrieve VR data agent

</td><td>

Legacy and Unified Security Exposure Management \(USEM\)

</td></tr><tr><td>

Analyze vulnerability remediation status

</td><td>

[[sla-targets-vr-aiagent|Analyze vulnerability remediation status]]-   Gain insights into your compliance metrics and statistics for how well you're meeting remediation target dates on vulnerable item \(VIT\) records.
-   View your monthly VIT record remediation totals and identify missed targets.
-   Break down remediation data on VITs by **Severity**, **Assignment group**, **Configuration item**, and **Vulnerability** for your monthly Service Level Agreement \(SLA\) compliance reviews.

</td><td>

Remediation compliance analysis AI Agent

</td><td>

Legacy and Unified Security Exposure Management \(USEM\)

</td></tr></tbody>
</table>**Important:** By default, all agentic workflows and AI agent records are read-only.

To modify an agentic workflow, you must first [duplicate the agentic workflow](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/clone-aia-usecase.md), and then proceed with the following steps:

-   Activate the agentic workflow. The [[now-assist-for-vulnerability-response-landing|Now Assist for Vulnerability Response]] AI agents included with the application are activated by default.
-   If required, you can add a trigger to invoke the agentic workflow automatically.
-   See [[now-assist-vr-acticvate-agentic-workflow|Configure an agentic workflow]] for more information.

There might be AI agents installed with the Now Assist application that are not used in agentic workflows. To learn how to see all agents that are available to you, see [Find AI agents](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/find-ai-agents.md).

## Related

- [[now-assist-review-vulnerability-exposure-data|Evaluate vulnerability exposure data with Security Exposure 360]]
- [[exploring-ai-security-exposure|Exploring AI Security Exposure Management]]
- [[assess-exposure-vr-aiagent|Assess your vulnerability exposure with generative AI]]
- [[retrieve-vr-data|Retrieve Vulnerability and exposure data with generative AI]]
- [[sla-targets-vr-aiagent|Analyze vulnerability remediation status with generative AI]]
- [[now-assist-vr-acticvate-agentic-workflow|Configure an agentic workflow]]
- [[vulnerabilities|Vulnerabilities]]
- [[unified-security-exposure-management-landing-page|Unified Security Exposure Management \(USEM\)]]
- [[threat-intelligence-infrastructure|Infrastructure]]
- [[vulnerability-manager-workspace-landing-page|Vulnerability Manager Workspace]]
- [[now-assist-for-vulnerability-response-landing|Now Assist for Vulnerability Response]]
