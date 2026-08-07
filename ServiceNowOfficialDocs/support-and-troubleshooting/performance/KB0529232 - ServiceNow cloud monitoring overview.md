---
title: "ServiceNow cloud monitoring overview"
aliases:
  - KB0529232
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0529232
kb_number: KB0529232
last_modified: 2026-04-20
---

## ServiceNow cloud monitoring overview

  

### Issue

Explore the monitoring infrastructure for ServiceNow cloud services. This article provides a high-level overview of the monitoring framework, describes what is monitored, and explains how the system continues to evolve.

### Release

All supported releases

### Resolution

### In this section

-   [Overview](#Overview)
-   [Definitions](#Definitions)
-   [Monitoring tools and integration](#How_We_Monitor)
-   [Monitoring framework](#Monitoring_Framework)
-   [System evolution](#How_We_Are_Evolving)
-   [Customer communication](#Customer_Communication)

### Overview

The robust monitoring and diagnostics framework for ServiceNow cloud services considers the dependencies involved in delivering cloud service to end users. The framework includes components that help detect, respond to, predict, and prevent issues at each layer of service dependency.

From a monitoring perspective, cloud service consists of three layers:

-   **Infrastructure:** Data centers and servers
-   **Application**: Software that delivers functionality to end users
-   **Network access**: Connections that allow end users to access applications

The framework continuously monitors all three layers. The approach to service monitoring includes the ability to:

1.  Detect an event
2.  Send an alert for an event
3.  Respond to an event
4.  Predict an event
5.  Prevent an event

![Pillars of monitoring](400px-pillars.pngx "Pillars of monitoring")

### Definitions

| Term | Meaning |
| --- | --- |
| Event | An outcome triggered in the system by a programmatically set condition. For example, when a service starts or fails to start.  |
| Alert | A notification raised by the system because an event has occurred and an action is required. |
| Detect | Identification of a problem in the system, typically accomplished by comparing values against predefined conditions and rules.  |
| Respond | Reaction to a detected problem. Responses can include auto-healing, manual intervention, or escalation for further analysis.  |
| Predict | The ability to anticipate a future event based on data collected over time.  |
| Prevent | Action taken to stop a future event from occurring. |

### Monitoring tools and integration

ServiceNow monitors cloud services using internally developed systems and industry-leading software. Third-party tools include:

-   OpManager
-   APG
-   Thousand Eyes

ServiceNow has built monitoring components on top of the Now Platform for task-based event management. The monitoring system integrates with ServiceNow applications including Incident, Problem, and Change Management for seamless connection between layers.

### Monitoring framework

The monitoring framework covers all layers of cloud service delivery. For details about specific monitoring components and metrics, refer to the diagram in this section.

![Image: 800 pixels](800px-Monitoring_FrameworkI.pngx "Monitoring framework")

### System evolution

The Now Platform continues to grow quickly, and providing an optimal customer experience remains a priority. The monitoring infrastructure is designed to resolve issues before they affect users. ServiceNow continuously works to predict and prevent events that could adversely affect the user experience.

![Image: 800 pixels](800px-evolution.pngx "Evolution of monitoring and alerting")

### Customer communication

Monitoring is a core competency of ServiceNow cloud infrastructure. As the system evolves, ServiceNow makes changes to the monitoring infrastructure to respond to customer requirements more quickly. These changes reflect a commitment to continuous enhancement of the monitoring service.

Infrastructure changes are designed to avoid interrupting cloud service delivery. When changes do not affect service availability, ServiceNow may not communicate these changes to customers.
