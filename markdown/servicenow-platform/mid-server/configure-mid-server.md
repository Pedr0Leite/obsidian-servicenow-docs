---
title: Configuring MID Server
description: Before MID Server installation can begin, the network must be prepared to access the instance and download site. There are several installation procedures depending on the host operating system and scale of deployment. Once installed, MID Servers can be configured with many capabilities and features.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/mid-server/configure-mid-server.html
release: australia
product: MID Server
classification: mid-server
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [MID Server, Manage instance data sources, Extend ServiceNow AI Platform capabilities]
---

# Configuring MID Server

Before [[mid-server-landing|MID Server]] installation can begin, the network must be prepared to access the instance and download site. There are several installation procedures depending on the host operating system and scale of deployment. Once installed, MID Servers can be configured with many capabilities and features.

-   **[Prepare network connections for MID Servers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/c_MIDServerConnectionPrerequisites.md)**  
Before you install the MID Server, perform the necessary prerequisites that it needs to [[c_Connect|connect]] to elements inside and outside your network. This includes network privileges and security considerations.
-   **[Installing the MID Server](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/mid-server-installation.md)**  
Download and install the MID Server on the host machine, test the connection, and then [[t_ValidateAMIDServer|validate the MID Server]]. Use the manual procedures or the guided setup. Set up multiple MID Servers for load balancing and [[domain-separation-relationship-formatter-editor|domain separation]]. These procedures prepare it for use with any application.
-   **[Configuring MID Servers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/c_MIDServerConfiguration.md)**  
After installing and validating your MID Servers, ensure that they have access to sufficient system resources, probe the proper targets, and communicate with the instance as expected. Configure [[c_MIDServerSelector|MID Server selection]] criteria, create clusters for failover protection, and set up MID Servers in different domains to protect data.

**Parent Topic:**[[manage-data-sources|Manage instance data sources]]

## Related

- [[manage-data-sources|Manage instance data sources]]
- [[mid-server-landing|MID Server]]
- [[c_Connect|Connect]]
- [[t_ValidateAMIDServer|Validate the MID Server]]
- [[domain-separation-relationship-formatter-editor|Domain separation]]
- [[c_MIDServerSelector|MID Server selection]]
