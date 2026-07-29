---
title: Configure Financial Services Operations AI agents
description: Configure Financial Services Operations AI agents to define their tools, access controls, triggers, and active status. You can also review Knowledge Graph tag records that supply structured and unstructured data to improve AI agent performance.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/financial-services-operations/now-assist-for-financial-services-operations-fso/configure-fso-ai-agents.html
release: australia
product: Now Assist for Financial Services Operations \(FSO\)
classification: now-assist-for-financial-services-operations-fso
topic_type: concept
last_updated: "2026-05-29"
reading_time_minutes: 2
keywords: [Financial Services Operations, AI agents, AI Agent Studio, Knowledge Graph, agentic AI, ACH dispute, banking CSR, insurance CSR, agent configuration, triggers, access controls]
audience: administrator
breadcrumb: [Configure, Now Assist for FSO, Financial Services Operations \(FSO\)]
tags:
  - financial-services-operations
  - now-assist
  - ai
  - fso
  - generative
  - type-concept
---

# Configure Financial Services Operations AI agents

Configure Financial Services Operations AI agents to define their tools, access controls, triggers, and active status. You can also review Knowledge Graph tag records that supply structured and unstructured data to improve AI agent performance.

## Access the AI agent configuration

To access the agent configuration:

1.  Navigate to **All** &gt; **AI Agent Studio** &gt; **Overview**.
2.  Select **AI Agents** and then select appropriate agent.

    The **Define the specialty** screen is displayed.

3.  In the **Add tools and information** step, review the AI agent's capabilities, scripts, and subflows.
4.  In the **Define user access** and **Define data access** steps, review which roles can access the AI agent and the AI agent's user identity.
5.  In the **Add triggers** step, perform the following for the AI agent you're configuring:

    |Agent|Configuration|
    |-----|-------------|
    |ACH dispute AI agents|Define triggers for the AI agent. By default, the trigger is deactivated and must be enabled.|
    |Banking CSR customer insights AI agent|This step is not required.|
    |Banking CSR support AI agent|Define triggers for the AI agent. By default, the trigger is deactivated and must be enabled.|
    |Insurance CSR customer insights AI agent|This step is not required.|
    |Insurance CSR support AI agent|Define triggers for the AI agent. By default, the trigger is deactivated and must be enabled.|

    To enable the trigger:

    1.  Select the trigger name.
    2.  Enable **Trigger is ON**.
    3.  Select **Save**.
6.  In the **Select channels and status** step, make sure that the **This AI agent is active** field is enabled to activate the AI agent.

## Access Knowledge Graph Tags configuration

Knowledge Graphs enhance the performance of AI agents using the structured and unstructured data from ServiceNow records, knowledge bases, and external sources.

The following shows each FSO application's knowledge graph tag records that list the tables referenced in the Knowledge Graph:

-   **[[agentic-contact-center-for-banking-landing|Agentic Contact Center for Banking]]**
    -   FSO Core Personal
    -   FSO Core Business
-   **[[landing-agentic-contact-centre-for-insurance|Agentic Contact Center for Insurance]]**

    -   FSO Insurance Policies
    -   FSO Insurance Product Catalog
    The following graphs are added if the respective [[insurance-claims-flow|insurance claims]] or servicing application is installed:

    -   FSO Insurance [[personal-lines-claims-landing-page|Personal Lines Claims]]
    -   FSO Insurance [[commercial-lines-claims-landing-page|Commercial Lines Claims]]
    -   FSO Insurance [[individual-life-claims-landing-page|Individual Life Claims]]
    -   FSO Insurance Generic Claims
    -   FSO Insurance [[fso-ins-personal-policy-ops-landing-page|Personal Lines Servicing]]
    -   FSO Insurance [[fso-ins-commercial-policy-ops-landing-page|Commercial Lines Servicing]]
    -   FSO Insurance [[individual-life-servicing|Individual Life Servicing]]
    -   FSO Insurance [[group-life-servicing|Group Life Servicing]]

**Parent Topic:**[Configuring Now Assist for Financial Services Operations \(FSO\)](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/now-assist-for-financial-services-operations-fso/configuring-now-assist-skills-for-fso.md)

**Related topics**  


[Knowledge Graph](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/knowledge-graph-landing.md)

[Tagging in Knowledge Graph Designer](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/tagging-in-knowledge-graph.md)

## Related

- [[agentic-contact-center-for-banking-landing|Agentic Contact Center for Banking]]
- [[landing-agentic-contact-centre-for-insurance|Agentic Contact Center for Insurance]]
- [[insurance-claims-flow|Insurance claims]]
- [[personal-lines-claims-landing-page|Personal Lines Claims]]
- [[commercial-lines-claims-landing-page|Commercial Lines Claims]]
- [[individual-life-claims-landing-page|Individual Life Claims]]
- [[fso-ins-personal-policy-ops-landing-page|Personal Lines Servicing]]
- [[fso-ins-commercial-policy-ops-landing-page|Commercial Lines Servicing]]
- [[individual-life-servicing|Individual Life Servicing]]
- [[group-life-servicing|Group Life Servicing]]
