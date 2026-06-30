---
title: Configuring Hermes Messaging Service
description: Learn how the Hermes Messaging Service is activated. Set up a secure connection to the Hermes Messaging Service.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/multi-instance-framework-hermes/configuring-hermes-messaging-service.html
release: australia
product: Multi-Instance Framework - Hermes
classification: multi-instance-framework-hermes
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Hermes Messaging Service, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
---

# Configuring Hermes Messaging Service

Learn how the [[hermes-messaging-service|Hermes Messaging Service]] is activated. [[set-up-secure-connection-to-hermes|Set up a secure connection to the Hermes Messaging Service]].

## Configuration overview

The Hermes Messaging Service is a ServiceNow AI Platform capability that is available as part of Stream [[c_Connect|Connect]], Log Export Service \(LES\), and [[instance-data-replication|Instance Data Replication]] \(IDR\).

To successfully set up and configure Stream Connect or Log Export Service, you must complete the steps in [Set up a secure connection to the Hermes Messaging Service](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/multi-instance-framework-hermes/set-up-secure-connection-to-hermes.md).

-   **[Activating the Hermes Messaging Service](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/multi-instance-framework-hermes/hermes-messaging-service-activation.md)**  
The Hermes Messaging Service is enabled when the Glide Hermes Message Queue plugin \(com.glide.hermes\) is activated.
-   **[Set up a secure connection to the Hermes Messaging Service](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/multi-instance-framework-hermes/set-up-secure-connection-to-hermes.md)**  
Secure your Kafka topics by generating a ServiceNow® instance-signed certificate.
-   **[Revoke a Hermes certificate](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/multi-instance-framework-hermes/revoke-certificate.md)**  
Revoke a ServiceNow® instance-signed certificate so that it can't be used in secure connections to the Hermes Messaging Service.
-   **[Restricting access to Hermes](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/multi-instance-framework-hermes/restricting-access-hermes-topics.md)**  
[[t_ContrlAccessByCDGUOrLoc|Restrict access]] to Hermes by [[ip-address|IP address]].

**Parent Topic:**[[manage-services|Manage service capabilities]]

## Related

- [[manage-services|Manage service capabilities]]
- [[hermes-messaging-service|Hermes Messaging Service]]
- [[set-up-secure-connection-to-hermes|Set up a secure connection to the Hermes Messaging Service]]
- [[c_Connect|Connect]]
- [[instance-data-replication|Instance Data Replication]]
- [[t_ContrlAccessByCDGUOrLoc|Restrict access]]
- [[ip-address|IP Address]]
