---
title: AI Agent Advisor in Now Assist Center
description: AI Agent Advisor automatically discovers automation opportunities in your instance based on actual operational data and helps you to deploy AI agents to implement them.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/intelligent-experiences/now-assist-center-ai-agent-advisor.html
release: australia
topic_type: concept
last_updated: "2026-06-05"
reading_time_minutes: 3
keywords: [AI Agent Advisor, AI agents, Now Assist, Now Assist Center, Gen AI, Generative AI]
breadcrumb: [Explore, Now Assist Center, Enable AI experiences]
tags:
  - intelligent-experiences
  - type-concept
---

# AI Agent Advisor in Now Assist Center

AI Agent Advisor automatically discovers automation opportunities in your instance based on actual operational data and helps you to deploy AI agents to implement them.

## Overview of AI Agent Advisor

AI Agent Advisor analyzes your instance data to identify the most frequent and impactful opportunities for efficiency gains in your workflows. For each identified opportunity, it proposes AI agents that can automate the solution, and generates new agents when no existing match is available.

This gives the [[platform-now-assist-landing|Now Assist]] administrator a data-driven starting point for AI adoption, eliminating the guesswork of deciding where to apply automation.

## How it works

The following diagram shows the AI Agent Advisor workflow.

\[Omitted image "mmasset0022026-ai-agent-advisor-workflow.png"\] Alt text: AI Agent Advisor workflow and activities.

AI Agent Advisor operates through three sequential phases:

-   **Mine**

    The system analyzes the records in your instance \(for example, incident and case records\) on a scheduled basis to identify recurring problems that are candidates for automation.

    You can configure the data sources, filters, and schedule to target the most relevant records for your organization.

-   **Match**

    For each identified opportunity, the system maps the resolution steps to existing AI agents, tools, and agentic workflows already available on your platform.

-   **Make**

    When no existing agent is a strong match for a resolution step, the system generates a new AI agent tailored to that specific problem.


The result is a prioritized list of automation opportunities. Each opportunity displays the estimated time and cost savings, number of records analyzed, and available [[ai-assets|AI assets]]. AI Agent Advisor generates the resolution steps using the data from existing records on your instance. You can use this list to decide which opportunities to act on first.

For more information on the AI Agent Advisor application, see [[ai-agent-advisor-landing-page|AI Agent Advisor]].

## Accessing AI Agent Advisor in Now Assist Center

AI Agent Advisor displays automation opportunities in several places in [[now-assist-center-landing-page|Now Assist Center]].

-   **[[now-assist-center-home-page|Home page]]**

    The home page displays the top automation opportunities as summary cards, ranked by relevance, volume, and estimated return on investment \(ROI\).

-   **Automation opportunities page**

    The Automation opportunities page provides the complete list of opportunities, along with a summary of aggregate metrics.

-   **Resolution steps page**

    The resolution steps page displays the automation opportunity details and includes a set of proposed resolution steps that show how to automate it.


For more information on using AI Agent Advisor in Now Assist Center, see [[now-assist-center-using-ai-agent-advisor|Using AI Agent Advisor in Now Assist Center]].

**Parent Topic:**[[exploring-now-assist-center|Exploring Now Assist Center]]

**Related topics**  


[Now Assist Center workspace]()

[Now Assist Readiness Evaluation in Now Assist Center]()

[Supporting information for Now Assist Center]()

## Related

- [[ai-agent-advisor-landing-page|AI Agent Advisor]]
- [[now-assist-center-using-ai-agent-advisor|Using AI Agent Advisor in Now Assist Center]]
- [[exploring-now-assist-center|Exploring Now Assist Center]]
- [[platform-now-assist-landing|Now Assist]]
- [[ai-assets|AI assets]]
- [[now-assist-center-landing-page|Now Assist Center]]
- [[now-assist-center-home-page|Home page]]
