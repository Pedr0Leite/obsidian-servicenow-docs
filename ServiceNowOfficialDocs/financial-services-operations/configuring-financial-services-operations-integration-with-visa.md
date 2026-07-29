---
title: Configuring Financial Services Operations Integration with Visa
description: Plan and configure your Financial Services Operations Integration with Visa implementation.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/financial-services-operations/configuring-financial-services-operations-integration-with-visa.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Visa, Integrate, Financial Services Operations \(FSO\)]
tags:
  - financial-services-operations
  - type-concept
---

# Configuring Financial Services Operations Integration with Visa

Plan and configure your Financial Services Operations Integration with Visa implementation.

**Important:** Set the `sn_bom_credit_card.is_visa_integration_enabled` property to `True` to enable Financial Services Operations Integration with Visa. By default, this property is set to `False`, so you need to update it manually. Financial Services Operations Integration with Visa will not function until this property is enabled.

## Configuration overview

To configure Financial Services Operations Integration with Visa on your ServiceNow instance, you need to set up a sequence of tasks.

1.  [Request Integration Hub subscription](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/integrate-applications/request-ih-overview.md).

    Use the Integration Hub to integrate a Visa account with your ServiceNow instance.

2.  [[install-financial-services-operations-integration-with-visa|Install Financial Services Operations Integration with Visa]].

    You can install the Financial Services Operations Integration with Visa \(com.sn\_fso\_intg\_visa\) application from the ServiceNow Store. The application installs related applications and plugins if they are not already installed.

3.  [[activate-visa-spoke|Set up Visa Spoke]].

    IntegrationHub enables execution of third-party APIs as a part of a flow when a specific event occurs in ServiceNow. These integrations, referred to as spokes, are easy to configure and enable you to quickly add powerful actions without the need to write a script.

4.  [[set-up-financial-services-operations-integration-with-visa|Set up instance credentials]].

    Configure the Financial Services Operations Integration with Visa application by using the Visa connection and credential record to authenticate ServiceNow requests.

5.  [[properties-installed-with-fso-integration-with-visa|Configure properties]].

    Customize properties that control settings for features in the Financial Services Operations Integration with Visa application, such as integration with specific APIs.


-   **[Install Financial Services Operations Integration with Visa](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/install-financial-services-operations-integration-with-visa.md)**  
If you have the admin role, you can install the Financial Services Operations Integration with Visa application.
-   **[Set up Visa Spoke](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/activate-visa-spoke.md)**  
Activate the Visa spoke in IntegrationHub from the ServiceNow Store, and enable the quick access to payment and security data. You can use the spoke to search for transactions, collaborate with merchants, manage disputes and perform other functions with enhanced security
-   **[[activate-visa-queue-scheduler-flow|Configure the Visa Queue Scheduler Flow]]**  
Use the Visa Queue Scheduler Flow to control the frequency at which Visa batch queues are processed. This flow runs as a scheduled job at a predefined time interval, triggering the subflow that processes incoming batch queues.
-   **[Set up Financial Services Operations Integration with Visa](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/set-up-financial-services-operations-integration-with-visa.md)**  
Configure the Financial Services Operations Integration with Visa application by using the Visa connection and credential record to authenticate ServiceNow requests.

**Parent Topic:**[[financial-services-operations-integration-with-visa-landing-page|Financial Services Operations Integration with Visa]]

## Related

- [[install-financial-services-operations-integration-with-visa|Install Financial Services Operations Integration with Visa]]
- [[activate-visa-spoke|Set up Visa Spoke]]
- [[set-up-financial-services-operations-integration-with-visa|Set up Financial Services Operations Integration with Visa]]
- [[properties-installed-with-fso-integration-with-visa|Properties installed with Financial Services Operations Integration with Visa]]
- [[activate-visa-queue-scheduler-flow|Configure the Visa Queue Scheduler Flow]]
- [[financial-services-operations-integration-with-visa-landing-page|Financial Services Operations Integration with Visa]]
