---
title: Subscriptions for IT Operations Management
description: The ServiceNow AI Platform uses a licensing method where your organization is billed for using the following IT Operations Management products: ServiceNow ITOM Visibility, ServiceNow ITOM Discovery, ServiceNow ITOM AIOps, ServiceNow Health Log Analytics, ServiceNow ITOM Optimization, ServiceNow ITOM Cloud Accelerate, ServiceNow Service Reliability Management, ServiceNowSLO Management, ServiceNow Service Observability, and ServiceNow synthetic monitoring.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/it-operations-management/itom-license-module.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 6
breadcrumb: [Exploring ITOM/OT SU Licensing, ITOM/OT SU Licensing and subscriptions, IT Operations Management]
tags:
  - it-operations-management
  - type-concept
---

# Subscriptions for IT Operations Management

The ServiceNow AI Platform® uses a licensing method where your organization is billed for using the following [[r_ITOMApplications|IT Operations Management]] products: ServiceNow® [[itom-visibility-landing-page|ITOM Visibility]], ServiceNow® ITOM [[r-discovery|Discovery]], ServiceNow® [[itom-health-landing-page|ITOM AIOps]], ServiceNow® [[hla-landing-page|Health Log Analytics]], ServiceNow® [[itom-optimization-landing-page|ITOM Optimization]], ServiceNow® [[itom-cloud-accelerate-landing-page|ITOM Cloud Accelerate]], ServiceNow® [[sr-landing-page|Service Reliability Management]], ServiceNow®SLO Management, ServiceNow® [[service-observability|Service Observability]], and ServiceNow® [[synthetic-monitoring-landing-page|synthetic monitoring]].

For licensing purposes, licensable resources are assigned to CI categories. License usage is measured using subscription units, which may cover a different number of resources, depending on the resource CI category. The customer contract for your organization determines the CI categories from the available options, and also the ratios of CI allocation for subscription units in each CI category. Information from the customer contract is synchronized with the ServiceNow platform. The latest version of ServiceNow® ITOM/OT SU Licensing supports the following CI categories:

-   Containers
-   PaaS
-   FaaS
-   Servers
-   Unresolved Monitored Object
-   Unclassed category
-   End User Devices
-   IoT
-   Customer Prem Devices
-   Container Images
-   APIs
-   AI Agents
-   GPUs
-   Service Instances

You have the option to buy subscriptions for individual ITOM products separately \(a la carte\) or as part of a bundle with multiple products. You can also purchase both—a bundle subscription that covers most required applications and an a la carte subscription for applications that consume more subscription units. For more information, see [[itom-licensing-subscription-types|ITOM/OT SU Licensing subscription types]].

ServiceNow® charges for the following IT Operations Management products:

-   **ITOM Visibility**

    The ServiceNow® ITOM Visibility product consists of ServiceNow® [Discovery](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-operations-management/discovery/r-discovery.md), [Firewall Audits and Reporting](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-operations-management/discovery/firewall-audit-reporting.md), [Certificate Inventory and Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-operations-management/discovery/cert-inventory-mgmt.md), [Service Mapping](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-operations-management/service-mapping/c_ServiceMappingOverview.md), [AI Agent Topology Mapping](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-operations-management/itom-visibility/ai-agent-topology-mapping-landing.md), [ITOM Content Service](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-operations-management/itom-visibility/discovery-content-services.md), [Tag Governance](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-operations-management/tag-governance/landing-page-tag-governance.md), [Cloud Discovery Workspace](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-operations-management/cloud-discovery-workspace/cow-landing-page.md), and [Cloud License Estimator](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-operations-management/cloud-license-estimator/cloud-license-estimator-landing.md) applications. Discovery and [[c_ServiceMappingOverview|Service Mapping]] give you a unified, connected view of your entire IT network and the services that it supports. The [Service Graph Connectors](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/cmdb-sgc-available.md) and [CMDB 360](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/multisource-cmdb.md) applications provide data to ITOM Visibility.

    In addition, Service Graph Connectors populate the CMDB by bringing in data from third-party monitoring and management systems. CMDB 360 enables you to track how the CMDB contains various discovery sources at the CI attribute level. Use [[cert-inventory-mgmt|Certificate Inventory and Management]] to avoid service outages due to expired TLS certificates. [[firewall-audit-reporting|Firewall Audits and Reporting]] helps you to discover and manage your firewall security policies to heighten the security awareness for [[Firewall-audits|firewall audits]].

    For licensing purposes, ITOM Visibility provides the CI count it discovers, both during horizontal and top-down discovery. It also reports CIs that the Service Graph Connectors populate the CMDB with.

    You can also use limited [[landing-page-tag-governance|Tag Governance]] functionality under the ITOM Visibility subscription. You can identify on-premises resources that are inconsistent and don't comply with the tag policies of your organization.

-   **ITOM Discovery**

    ServiceNow® ITOM Discovery is an entry-level package alternative where customers can build a healthy data platform. This package measures licensed usage of the Discovery feature and Service Graph Connectors. Discovery is a "subset" of ITOM Visibility that is also based on subscription units. ITOM Discovery includes the following basic features: ServiceNow® Discovery, Service Graph Connectors, and CMDB 360. ServiceNow® Discovery finds applications and devices on your network, and then updates the CMDB. Service Graph Connectors supplement the population of the CMDB, while CMDB 360 retains the complete history of discovery sources and proposed values.

    ITOM Discovery provides the count of CIs found by ServiceNow® Discovery and brought in by Service Graph Connectors.

-   **ITOM AIOps**

    The ServiceNow® ITOM AIOps product includes the ServiceNow® [[c_EM|Event Management]] and ServiceNow® [[operational-metrics|Metric Intelligence]] applications, which help you track and maintain the health of services in your organization.

    ITOM AIOps reports the number of CIs, where it captures alerts, events, and metric data. ITOM AIOps reports the CI count for all CI categories.

-   **Health Log Analytics**

    Health Log Analytics CI count is based on log data received from licensable resource types. The consumption is reflected in ITOM AIOps as well as in Health Log Analytics. For that reason, you need the ITOM AIOps subscription in addition to the Health Log Analytics subscription.

-   **ITOM Cloud Accelerate**

    The ITOM Cloud Accelerate product consists of the following workflow applications: Tag Governance, [[cloud-migration-landing-page|Cloud Migration Assessment]], [[cloud-configuration-governance|Cloud Configuration Governance]], and [[cloud-actions-library-landing-page|Cloud Action Library]]. In Tag Governance, you can update CI tags in the cloud environment, in addition to updating them in the CMDB.

    For licensing purposes, the ITOM Cloud Accelerate license provides the CI count for CIs managed and monitored by Cloud Migration Assessment, Cloud Configuration Governance, or Cloud Action Library. If different ITOM Cloud Accelerate features report the same CIs as their resources, the CI count is manipulated to remove the duplication.

-   **ITOM Optimization**

    The ServiceNow® ITOM Optimization application provides automation for the cloud workflows used to manage the cloud resources throughout their life cycle. It enables certified and enterprise-compliant cloud deployment, cost visibility, and other cloud management processes.


-   **Service Observability**

    The ITOM Service Observability feature creates actionable [[otto-aiops-dashboards|dashboards]] and observability tabs that centralize data from existing third-party monitoring tools. It allows you to track the performance of business-critical services, enables faster root cause analysis, and reduces mean time to resolution \(MTTR\). Application and platform telemetry insights from multiple observability tools are combined into a centralized workflow.


**Parent Topic:**[[explore-itom-licensing|Exploring ITOM/OT SU Licensing]]

**Related topics**  


[Subscription Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/subscription-management-landing-page-v2.md)

## Related

- [[itom-licensing-subscription-types|ITOM/OT SU Licensing subscription types]]
- [[explore-itom-licensing|Exploring ITOM/OT SU Licensing]]
- [[r_ITOMApplications|IT Operations Management]]
- [[itom-visibility-landing-page|ITOM Visibility]]
- [[r-discovery|Discovery]]
- [[itom-health-landing-page|ITOM AIOps]]
- [[hla-landing-page|Health Log Analytics]]
- [[itom-optimization-landing-page|ITOM Optimization]]
- [[itom-cloud-accelerate-landing-page|ITOM Cloud Accelerate]]
- [[sr-landing-page|Service Reliability Management]]
- [[service-observability|Service Observability]]
- [[synthetic-monitoring-landing-page|Synthetic monitoring]]
- [[c_ServiceMappingOverview|Service Mapping]]
- [[cert-inventory-mgmt|Certificate Inventory and Management]]
- [[firewall-audit-reporting|Firewall Audits and Reporting]]
- [[Firewall-audits|Firewall audits]]
- [[landing-page-tag-governance|Tag Governance]]
- [[c_EM|Event Management]]
- [[operational-metrics|Metric Intelligence]]
- [[cloud-migration-landing-page|Cloud Migration Assessment]]
- [[cloud-configuration-governance|Cloud Configuration Governance]]
- [[cloud-actions-library-landing-page|Cloud Action Library]]
- [[otto-aiops-dashboards|Dashboards]]
