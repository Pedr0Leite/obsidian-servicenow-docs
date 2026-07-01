---
title: Exploring Log Export Service \(LES\)
description: The LES service provides a highly scalable and near real-time integration with your analytic tools that is easy to set up and maintain. If you're new to LES, read this overview section to learn what the tool can do.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/les-landing-page.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Log Export Service \(LES\), Platform Security]
tags:
  - platform-security
  - type-concept
---

# Exploring Log Export Service \(LES\)

The LES service provides a highly scalable and near real-time integration with your analytic tools that is easy to set up and maintain. If you're new to LES, read this overview section to learn what the tool can do.

Check your entitlements to determine whether you have access to Log [[export|Export]] Service.

## Log Export Service overview

The integration tool allows you to leverage your analytic solutions to perform the following:

-   Detect ServiceNow security threats and analyze security incidents
-   Troubleshoot and optimize ServiceNow app performance
-   Monitor and optimize ServiceNow user experience

LES leverages a ServiceNow AI Platform capability called the Hermes Messaging Service, which is a multi-tenant, multi-cluster, data transport, and queuing service built on Apache Kafka that enables your instance to produce and consume large volumes of Kafka events. Apache Kafka is an open-source data streaming platform that provides a single integration point for exchanging data across business systems in your organization.

\[Omitted image "les-architecture.png"\] Alt text: Log Export Service

LES forwards a copy of the log events as they're generated to the Hermes Messaging Service.

The Hermes Messaging Service is a multi-tenant, multi-cluster, data transport, and queuing service built on Apache Kafka that enables your instance to produce and consume large volumes of Kafka events. The Hermes Messaging Service is a ServiceNow AI Platform capability that is available as part of Stream Connect, Log Export Service \(LES\), and Instance Data Replication \(IDR\).

The external log analytic systems, either in the cloud or on-prem, can use and consume the log events from the Hermes Messaging Service. LES provides three connectivity options to consume the [[logs|logs]]:

-   Dedicated MID Server: A dedicated MID Server is installed on-prem or in the cloud that automatically connects to Hermes Messaging Service, pulls log events from it continuously and then pushes them to log analytic tools via a REST connection.
-   Leverage Kafka connector from your log analytic solution \(for example, Splunk\): A Kafka connector from your log analytics product of choice is installed on-prem or in the cloud that automatically connects to Hermes Messaging Service, pulls log events from it continuously and then pushes them to log analytics tools.
-   Directly from your Kafka system: Your Kafka system connect directly with the Hermes Messaging Service and use its native Kafka protocol commands and connectivity to pull logs events from it.

**Note:** If your Kafka message exceeds the configured memory buffer, Hermes may return an error indicating that it's larger than the total memory buffer you've configured.

To configure and manage LES you need to install it from ServiceNow Store. The LES application provides Guided Setups to help you install the service, pages to configure the service \(log sources, consumers and destinations\) and reports to understand log creation and consumption.

\[Omitted image "les-module.png"\] Alt text: Navigation filter

**Note:** You can also create a new source [[sc-configuration|configuration]]. See [[les-create-source-configuration|Create a log source configuration]] for more information.

## Log Export Service users

Log Export Service has the following [[users|users]].

|Users|Description|
|-----|-----------|
|Application admin \[sn\_logstoanalytics.admin\]|This role is installed along with the LES application and allows a non-admin to use the application.|
|System administrator \[admin\]|Admin role is required for the setup of the LES store application.|

## Log Export Service benefits

|Benefit|Feature|Users|
|-------|-------|-----|
|Create log source configuration to set filters on the logs|[Create a log source configuration](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/les-create-source-configuration.md)|Application admin|
|Experience guided setup for Kafka consumers|[[les-guided-setup-kafka|Guided setup for Kafka consumers]]|System administrator|
|Experience guided setup for MID server consumers|[[les-guided-setup-mid-server|Guided setup for MID Server consumers]]|System administrator|
|Examine the log report dashboard to analyze the size of each data log|[[les-use|Review log report]]|System administrator or Application admin|

## What to explore next

To learn more about using Log Export Service, see:

-   [[les-administer|Administering Log Export Service \(LES\)]]
-   [[les-configure|Configuring Log Export Service \(LES\)]]
-   [Using Log Export Service \(LES\)](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/les-use.md)
-   [[les-references|Log Export Service \(LES\) references]]

-   **[[les-log-sources-export|Log sources]]**  
Log Export Service \(LES\) can export log sources from some [[r_SystemLogs|System Log]] Tables, the Audit Table, and Application Node Log Files.

**Parent Topic:**[[les-intro|Log Export Service \(LES\)]]

## Related

- [[les-create-source-configuration|Create a log source configuration]]
- [[les-guided-setup-kafka|Guided setup for Kafka consumers]]
- [[les-guided-setup-mid-server|Guided setup for MID Server consumers]]
- [[les-use|Using Log Export Service \(LES\)]]
- [[les-administer|Administering Log Export Service \(LES\)]]
- [[les-configure|Configuring Log Export Service \(LES\)]]
- [[les-references|Log Export Service \(LES\) references]]
- [[les-log-sources-export|Log sources]]
- [[les-intro|Log Export Service \(LES\)]]
- [[export|Export]]
- [[logs|Logs]]
- [[sc-configuration|Configuration]]
- [[users|Users]]
- [[r_SystemLogs|System log]]
