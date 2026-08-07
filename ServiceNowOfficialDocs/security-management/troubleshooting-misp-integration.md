---
title: Troubleshooting MISP integration
description: This section covers important troubleshooting tips that can help you resolve common issues you can encounter when setting up or running MISP integration.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/troubleshooting-misp-integration.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [MISP administration, MISP integration for Security Operations, Threat Intelligence integrations, Threat Intelligence, Enterprise security case management applications, Security Operations]
tags:
  - security-management
  - type-concept
---

# Troubleshooting MISP integration

This section covers important troubleshooting tips that can help you resolve common issues you can encounter when setting up or running MISP integration.

## SSL issues

When connecting through the MISP integration, ensure that you’ve installed a valid CA certificate on the MISP server, which hasn’t expired. You can import RSA or your own certificates into the platform and ensure that the common name of the certificate matches the host name. For more information, see [[install-and-configure-misp|Install and configure the MISP integration for Security Operations]] and [[misp-user-roles-and-permissions|MISP user roles and permissions]].

**Parent Topic:**[[misp-administration|MISP administration]]

**Related topics**  


[Getting started with MISP integration for Security Operations]()

[Install and configure the MISP integration for Security Operations]()

[Review the MISP integration settings]()

[Configure MISP sighting searches]()

[Configure how an automatic event is created]()

[MISP event data]()

[Associated MISP events]()

[MISP user information]()

[Domain separation and MISP]()

## Related

- [[install-and-configure-misp|Install and configure the MISP integration for Security Operations]]
- [[misp-user-roles-and-permissions|MISP user roles and permissions]]
- [[misp-administration|MISP administration]]
