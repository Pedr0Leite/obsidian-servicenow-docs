---
title: AI agents in Setup Hub
description: Refer to the following information about the Platform AI agents in Setup Hub.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/ia-agents-platform.html
release: australia
topic_type: reference
last_updated: "2026-04-03"
reading_time_minutes: 1
breadcrumb: [Reference, Setup Hub, Get started, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - type-reference
---

# AI agents in Setup Hub

Refer to the following information about the Platform AI agents in Setup Hub.

**Note:** The **Configure with Now Assist** button appears only for console items that are backed by AI capabilities.

<table id="table_ckp_xzv_t3c"><thead><tr><th>

AI Agent

</th><th>

Description

</th></tr></thead><tbody><tr><td class="sub-head" colspan="2">

Admin [[clone-configurations-tab|configurations]]

</td></tr><tr><td>

[[ai-search-configuration|AI Search Configuration]] Agent

</td><td>

Configures [[ia-ai-search|AI search]] for ServiceNow internal tables by defining internal search sources, search profiles, and table mappings through conversation.

</td></tr><tr><td>

AI Search XCC Agent

</td><td>

Configures [[ext-cont-connectors-landing-page|external content connectors]] for AI Search for public websites \(for example, Zoom, Apple Support, and Okta\) and SharePoint repositories.

 The agent guides with connector discovery that aligns with user requirements, authentication, content scope, crawl scheduling, search profile mapping, and error recovery.

</td></tr><tr><td>

Group and [[ia-roles-assignment|roles assignment]] agent

</td><td>

Provides user access through group-based associations. Creates a user group, manages users in a group, assigns roles to a group, and adds users to a role.

</td></tr><tr><td>

IA [[ia-operational-data-il|Operational Data]] Workflow Agent

</td><td>

Automates bulk data imports into ServiceNow for departments, users, locations, and groups. Supports both file-based and LDAP-based imports. Reduces the time and effort needed to migrate operational data during implementation.

</td></tr><tr><td>

SSO Configuration Agent

</td><td>

Automates Single Sign-On setup \(OIDC and SAML\) in ServiceNow using identity provider configuration data. Supports Q&amp;A and troubleshooting throughout the setup process.

</td></tr></tbody>
</table>**Parent Topic:**[[ia-reference|Setup Hub references]]

## Related

- [[ia-reference|Setup Hub references]]
- [[clone-configurations-tab|Configurations]]
- [[ai-search-configuration|AI Search configuration]]
- [[ia-ai-search|AI Search]]
- [[ext-cont-connectors-landing-page|External Content Connectors]]
- [[ia-roles-assignment|Roles assignment]]
- [[ia-operational-data-il|Operational data]]
