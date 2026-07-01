---
title: Configure Build Agent
description: Configure Build Agent on your instance by installing Build Agent and connecting to the Figma MCP server to enable AI-powered design workflows.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-development/configure-build-agent.html
release: australia
topic_type: concept
last_updated: "2026-06-09"
reading_time_minutes: 1
keywords: [Now Assist, AI Agents, generative AI, agentic AI]
breadcrumb: [Build Agent, Agentic development on the ServiceNow AI Platform, Building applications]
tags:
  - application-development
  - type-concept
---

# Configure Build Agent

Configure Build Agent on your instance by installing Build Agent and connecting to the Figma MCP server to enable AI-powered design workflows.

**Note:** Build Agent is enabled by default to create apps with AI, for example in [[servicenow-studio-landing|ServiceNow Studio]]. To use other Now Assist products, such as the [[sns-now-assist-app-gen-landing|app generation]] skill, disable Build Agent. For example, using the setting in your ServiceNow Studio preferences. For more information, see [Use the app generation skill to generate apps](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/now-assist-for-creator/sns-app-gen-use-app-gen-skill.md).

Configuring Build Agent involves several sequential steps:

-   Installing the [[now-assist-for-creator-landing|Now Assist for Creator]] application from the ServiceNow Store \(Paid version only\)
-   Activating the required plugins for your version
-   Establishing MCP server connections

Complete these steps to ensure that all dependencies and integrations are in place before using Build Agent.

-   **[[install-build-agent|Install Build Agent]]**  
For the Paid version of Build Agent, install the Now Assist for Creator application from the ServiceNow Store.
-   **[[build-agent-plugins|Build Agent plugins]]**  
The plugins for Build Agent depend on whether you're using the free/trial version or premium version.
-   **[[ba-connct-mcp-server|Connect Build Agent to a supported MCP server]]**  
Connect a supported MCP server to Build Agent to access external tools and resources in the chat panel when building and editing apps.
-   **[[connect-figma-mcp-server-to-build-agent|Connect Build Agent to a Figma MCP server]]**  
Connect the Figma Model Context Protocol Server Console \(MCP\) server to Build Agent to convert Figma designs into enterprise-grade applications on the ServiceNow AI Platform.

**Parent Topic:**[[build-agent|Build Agent]]

## Related

- [[install-build-agent|Install Build Agent]]
- [[build-agent-plugins|Build Agent plugins]]
- [[ba-connct-mcp-server|Connect Build Agent to a supported MCP server]]
- [[connect-figma-mcp-server-to-build-agent|Connect Build Agent to a Figma MCP server]]
- [[build-agent|Build Agent]]
- [[servicenow-studio-landing|ServiceNow Studio]]
- [[sns-now-assist-app-gen-landing|App generation]]
- [[now-assist-for-creator-landing|Now Assist for Creator]]
