---
title: Configuring MCP Server Console
description: Create a Model Context Protocol \(MCP\) server and configure the tools and inputs it exposes to MCP clients.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/intelligent-experiences/configuring-mcp-server-console.html
release: australia
topic_type: concept
last_updated: "2025-08-08"
reading_time_minutes: 1
keywords: [configure]
breadcrumb: [MCP Server Console, Enable AI experiences]
tags:
  - intelligent-experiences
  - type-concept
---

# Configuring MCP Server Console

Create a Model Context Protocol \(MCP\) server and configure the tools and inputs it exposes to MCP clients.

## Configuration overview

1.  [[create-mcp-server|Create a Model Context Protocol server]]

    An AI administrator creates a server and adds tools to the server.

2.  [[create-tool-mcp-server|Create a tool for a Model Context Protocol server]]

    If additional tools are needed, the AI administrator identifies which functionality to expose and creates tools based on [[now-assist-skills|Now Assist skills]]. From the tools, they configure which fields are exposed to clients as tool inputs.


After configuring a server, the AI administrator creates an OAuth inbound integration for each client and configures clients to connect to the server using the server and authentication details. For more information, see [[connect-mcp-server-client|Connecting to an MCP server from an MCP client]].

## Related

- [[create-mcp-server|Create a Model Context Protocol server]]
- [[create-tool-mcp-server|Create a tool for a Model Context Protocol server]]
- [[connect-mcp-server-client|Connecting to an MCP server from an MCP client]]
- [[now-assist-skills|Now Assist skills]]
