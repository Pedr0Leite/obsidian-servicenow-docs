---
title: Domain separation and MCP Server Console
description: If any conkeyrefs are broken, re-add them from the doc/source/reuse/domain-separation/domain-separation-overview.dita file.Domain separation is supported for MCP Server Console. Domain separation enables you to separate data, processes, and administrative tasks into logical groupings called domains. You can control several aspects of this separation, including which users can see and access data.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/intelligent-experiences/mcp-server-console-domain-separation.html
release: australia
topic_type: concept
last_updated: "2025-11-12"
reading_time_minutes: 2
breadcrumb: [Reference, MCP Server Console, Enable AI experiences]
tags:
  - intelligent-experiences
  - type-concept
---

# Domain separation and MCP Server Console

Domain separation is supported for [[mcp-platform-manager-landing|MCP Server Console]]. Domain separation enables you to separate data, processes, and administrative tasks into logical groupings called domains. You can control several aspects of this separation, including which users can see and access data.

## Support level: Standard

-   Includes all aspects of **Basic** level support.
-   Application properties are domain-aware as needed.
-   Business logic: The service provider \(SP\) creates or modifies processes per customer. The use [[cases|cases]] reflect proper use of the application by multiple SP customers in a single instance.
-   The instance owner must configure the minimum viable product \(MVP\) business logic and data parameters per tenant as expected for the specific application.

Sample use case: An admin must be able to make comments required when a record closes for one tenant, but not for another.

For more information on support levels, see [Application support for domain separation](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/domain-separated-apps.md).

## Overview

## How domain separation works in 

## Use cases

**Parent Topic:**[[mcp-server-console-reference|MCP Server Console reference]]

**Related topics**  


[Domain separation for service providers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/domain-sep-landing-page.md)

## Related

- [[mcp-server-console-reference|MCP Server Console reference]]
- [[mcp-platform-manager-landing|MCP Server Console]]
- [[cases|Cases]]
