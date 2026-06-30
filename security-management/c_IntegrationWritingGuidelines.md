---
title: ServiceNow Security Operations integration development guidelines
description: The ServiceNow platform provides several mechanisms for developing integrations with external systems. The ServiceNow Security Operations product suite adds integration capabilities intended to streamline the process of integrating with security-focused external systems.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/c\_IntegrationWritingGuidelines.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Security Operations Integration Reference, Security Operations common functionality, Security Operations]
---

# ServiceNow Security Operations integration development guidelines

The ServiceNow platform provides several mechanisms for developing integrations with external systems. The ServiceNow [[security-operations-landing-page|Security Operations]] product suite adds [[integration-capabilities|integration capabilities]] intended to streamline the process of integrating with security-focused external systems.

Most of the concepts in this guide assume some familiarity with standard ServiceNow functionality. To [[integrating-threat-intelligence-security-center|integrate]] with the Security Operations suite, at a minimum, knowledge of the following ServiceNow concepts is required:

-   Script includes
-   Inbound/outbound web services
-   [[data-sources|Data sources]]
-   Import sets
-   Transform maps

**Technology Partner Program**

Any requirements for application certification or guidelines given in the Technology Partner Program literature supersede any information in this guide. This guide is not a replacement for the Technology Partner Program literature and serves only as a supplement to existing documentation.

For more information, see [Technology Partner Program training course blog post](https://community.servicenow.com/community/develop/app-publisher/blog/2015/10/19/the-technology-partner-program-training-course).

-   **[[c_TypesOfIntegrationsProv|Types of ServiceNow integrations provided]]**  
The Security Operations applications \([[sir-landing-page|Security Incident Response]], [[threat-intel-landing-page|Threat Intelligence]], and [[vuln-landing-page|Vulnerability Response]]\) can be seamlessly integrated with other ServiceNow applications to enhance their functionality.
-   **[[third-party-integrations|Security Operations Integration Configurations]]**  
Many of the integrations included in the base system require little or no setup, and operate in the same way. Certain integrations, such as the Qualys Cloud Platform, however, require separate steps for setting up the integration. Others support different sets of scan and lookup types and different rate limits.
-   **[[c_BestPractisesIntegrations|Tips for writing integrations]]**  
Avoid some of the pitfalls you can encounter when writing your own integrations by following these guidelines.
-   **[[c_IntegrationTroubleshooting|Integration troubleshooting]]**  
These troubleshooting suggestions can help you resolve common issues you can encounter when setting up or running integrations.

**Parent Topic:**[[secops-integ-ref|Security Operations Integration Reference]]

## Related

- [[c_TypesOfIntegrationsProv|Types of ServiceNow integrations provided]]
- [[third-party-integrations|Security Operations Integration Configurations]]
- [[c_BestPractisesIntegrations|Tips for writing integrations]]
- [[c_IntegrationTroubleshooting|Integration troubleshooting]]
- [[secops-integ-ref|Security Operations Integration Reference]]
- [[security-operations-landing-page|Security Operations]]
- [[integration-capabilities|Integration capabilities]]
- [[integrating-threat-intelligence-security-center|Integrate]]
- [[data-sources|Data Sources]]
- [[sir-landing-page|Security Incident Response]]
- [[threat-intel-landing-page|Threat Intelligence]]
- [[vuln-landing-page|Vulnerability Response]]
