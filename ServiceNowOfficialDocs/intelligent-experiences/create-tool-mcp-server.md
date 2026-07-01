---
title: Create a tool for a Model Context Protocol server
description: Create a tool from various tool categories, to expose it to Model Context Protocol \(MCP\) clients from an MCP server.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/intelligent-experiences/create-tool-mcp-server.html
release: australia
topic_type: task
last_updated: "2026-06-08"
reading_time_minutes: 3
keywords: [Create tool for MCP server]
breadcrumb: [Configure, MCP Server Console, Enable AI experiences]
---

# Create a tool for a Model Context Protocol server

Create a tool from various tool categories, to expose it to Model Context Protocol \(MCP\) clients from an MCP server.

## Before you begin

If you aren't using the Quickstart Server, create a server to which you can add tools. For more information, see [[create-mcp-server|Create a Model Context Protocol server]].

Role required: sn\_mcp\_server.tools\_admin, sn\_mcp\_server.admin, or admin

## About this task

Each server must include at least one tool.

-   Tools define which functionality and data a server exposes to clients and the actions that can be performed on an instance by clients. Tools are based on capabilities, such as [[knowledge-graph-landing|Knowledge Graph]], Subflows, Action, REST APIs and [[now-assist-skills|Now Assist skills]], including custom skills created with [[now-assist-skill-kit-landing|Now Assist Skill Kit]]. For a list of Now Assist skills that can be used as tools, see [[now-assist-skill-support-mcp|Now Assist skill support in MCP Server Console]].
-   Tools include inputs that correspond to the fields of the existing capability. Inputs that are enabled for a tool are exposed to clients.

**Note:** The minimum version required is: Zurich patch 9 and Australia patch 2.

## Procedure

1.  Navigate to **All** &gt; **[[mcp-platform-manager-landing|MCP Server Console]]**.

2.  From the Configuration tab, select **Tools**.

    If you add inputs to a [[platform-now-assist-landing|Now Assist]] skill after a tool has been created, you must create another tool to include the additional inputs and replace the existing tool.

3.  View and manage the tools created from various categories, and their associated attributes. \[Omitted image "mcp-server-console-toolspec.png"\] Alt text: Tools attributes

4.  Select **Create tool**.

5.  Select a tool type you want to create from these categories: REST API, Action, Knowledge graph, Subflow and Now Assist skill.

    \[Omitted image "mcp-create-tool-moveworks.png"\] Alt text: Tool creation

    The steps are similar for any category you use for tool creation.

6.  See one of these to learn more:

    -   [[create-subflow-tool|Create a tool from Subflow]]
    -   [[create-a-tool-from-rest-api|Create a tool from REST API]]
    -   [[create-a-tool-from-knowledge-graphs|Create a tool from Knowledge Graph]]
7.  Turn off inputs from the tool that you don't want to expose.

    1.  In the Tool inputs section, locate the tool input.

    2.  From the Enabled column, select the toggle to turn off the input.

        **Note:** Some tool inputs are required and can't be turned off.

8.  Select **Create**.


## What to do next

Configure clients to connect to the server and use the tool. For more information, see [[connect-mcp-server-client|Connecting to an MCP server from an MCP client]].

**Related topics**  


[Now Assist skills](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/now-assist-skills/now-assist-skills.md)

[Now Assist Skill Kit](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/now-assist-skill-kit/now-assist-skill-kit-landing.md)

## Related

- [[create-mcp-server|Create a Model Context Protocol server]]
- [[now-assist-skill-support-mcp|Now Assist skill support in MCP Server Console]]
- [[create-subflow-tool|Create a tool from Subflow]]
- [[create-a-tool-from-rest-api|Create a tool from REST API]]
- [[create-a-tool-from-knowledge-graphs|Create a tool from Knowledge Graph]]
- [[connect-mcp-server-client|Connecting to an MCP server from an MCP client]]
- [[knowledge-graph-landing|Knowledge Graph]]
- [[now-assist-skills|Now Assist skills]]
- [[now-assist-skill-kit-landing|Now Assist Skill Kit]]
- [[mcp-platform-manager-landing|MCP Server Console]]
- [[platform-now-assist-landing|Now Assist]]
