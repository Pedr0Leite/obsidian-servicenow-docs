---
aliases:
  - "Integration Design - How to choose the best patter"
tags:
  - knowledge-base
  - platform
  - integrations
  - integration-hub
  - ai-agents
---

# Integration Design - How to choose the best pattern to integrate ServiceNow with other systems

n the world of ServiceNow, seamless integration is key to achieving operational efficiency and driving digital transformation.

However, as ServiceNow offers many integration possibilities with third-party systems, this article aims to guide you through the labyrinth of available integration choices, focusing on maintaining a lean and scalable platform primed for future development. We will investigate when and why specific integration patterns are recommended over others.

By the end of this article, you will have a comprehensive understanding of choosing the best integration approach for connecting ServiceNow to a third-party system.

# **ServiceNow Integration Pattern Decision Tree**

*Please note: This article covers product capabilities as of the Zurich (September 2025) release that are generally available for all commercial customers. Please contact your Account Team if you have any entitlement or subscription questions.*

The ServiceNow Integration Decision Tree below is a flowchart that guides you through choosing the best integration pattern for connecting to a 3rd party system. Here’s how to read it:

1. **Start at the Top and Follow the Arrows**: Each arrow leads you from one decision to the next.
2. **Answer the Questions**: The blue boxes contain questions you need to answer about your specific integration needs. Depending on your answers, you will follow the corresponding arrow to the next step.
3. **Reach an Outcome**: The round boxes represent integration patterns. These are the recommended integration patterns based on your answers to the previous questions. The color coding represents the overall alignment to integration best practices. If you end up with a pattern marked orange or red, you may want to revisit your decisions to see if a better pattern is within the realm of possibility.

You may also want to refer to the [Now Create: Integrations Workshop Presentation](https://learning.servicenow.com/nowcreate/en/pages/assets?id=nc_asset&asset_id=85b250e2db3450d077c0ce46b99619d3) to learn more about ServiceNow integration design.

[ServiceNow Integration Pattern Decision Tree - 3.1 - Jochen Geist](https://www.servicenow.com/community/image/serverpage/image-id/470017i4A42A2618AFF1E7A/image-size/large?v=v2&px=999)

*ServiceNow Integration Pattern Decision Tree - 3.1 - Jochen Geist*

You can download a PDF version of the image via this link: [ServiceNow Integration Pattern Decision Tree - 3.1 - Jochen Geist.pdf](https://www.servicenow.com/community/s/cgfwn76974/attachments/cgfwn76974/architect-blog/171/1/ServiceNow%20Integration%20Pattern%20Decision%20Tree%20-%203.1%20-%20Jochen%20Geist.pdf)

The key decision points have been marked with a blue circle and a letter and will be explained below.

# **[A] Web Service Integrations**

Web services are the preferred method for system integrations, mainly because of their widespread industry adoption and proven interoperability standards. Their inherent flexibility allows organizations to connect disparate platforms efficiently, adapting to various use cases and evolving business requirements.

# **[A1] Usage of an ESB or Integration Middleware**

One popular approach is leveraging an Enterprise Service Bus (ESB) or middleware to facilitate system-to-system integration. ESBs provide a unified platform for connecting diverse applications, allowing seamless data flow and communication across systems. While discussing the advantages and disadvantages of such an approach would qualify for a whitepaper on its own, there are a few considerations to keep in mind:

- Most ServiceNow Plugins, Store Apps, and Integration Hub Spoke are designed to work with the API structure and behavior of the respective 3rd party tool. If the middleware solution does not mirror this API fully, extensive customization is required, which increases complexity, delays implementation, and raises the total cost of ownership for the integration.
- Any middleware adds additional points of failure regarding system stability and security.
- Some ITOM Solutions, such as Discovery, Service Mapping, and Orchestration, do not work without a MID Server.

# **[A2] ServiceNow Instance Integration Options**

There are four recommended options when an integration between two ServiceNow instances is desired:

Service Bridge:

Service Bridge provides capabilities targeted to the telecommunication and technology industries for providers supporting their consumers, partners collaborating with providers, and inter-service operations. It is designed explicitly for Telco/Tech/MSP, where one instance represents the customer and one instance the provider. However, it has limited flexibility for data synchronization and requires agreement between the parties regarding the integration approach.

Instance Data Replication (IDR):

IDR copies data updates from one instance to one or more others, maintaining consistent data across different ServiceNow instances. It supports unidirectional and bidirectional replication and allows for limited data modification during replication. This solution is ideal for real-time replication of large data sets. However, IDR can only sync reference fields if IDR also synchronizes the target table of the reference. It is limited to 3 million records per replication set. For a complete list of limitations, please refer to the documentation.

Remote Process Sync (RPS):

RSP enables one-way or bidirectional integrations between instances to keep processes in sync. With RPS, you design flows on both instances using Flow Designer and synchronize them. It is ideal for real-time task-based process replication, ensuring message order execution despite connectivity issues. However, it requires separate creation and planning for each integration, which may be excessive for simple use cases.

Remote Instance Spoke:

This is a set of out-of-the-box actions for creating ad hoc integrations between instances. It is simple for ad hoc integrations but is not recommended for heavy integration use, as all flow logic, security, and error handling need to be implemented.

If none of these options fit your requirements, please follow the decision tree to explore other data transfer capabilities, such as Integration Hub Import.

# **[A3] Using an OOTB Solution**

Wherever possible, an Out-of-the-box approach shall be used. There are three patterns to distinguish between:

Native Integration (ServiceNow Plugin or Store App):

For some third-party applications, ServiceNow provides native connectors as well; for example, HR comes with a SuccessFactors integration. These are usually ready-made and require only a few configurations, so they should be used if applicable.

Integration Hub Spokes:

Integration Hub enables the execution of third-party APIs as part of a Flow when a specific event occurs in ServiceNow. These integrations, referred to as Spokes, are easy to configure and enable you to quickly add powerful actions without writing a script. However, more effort is usually required compared to the “ready-made” integrations mentioned above.Extending an existing Spoke using Spoke Generator:If the use case only partially matches an existing Spoke, extending the existing Spoke using the Spoke Generator is still better. This can be done by either importing an OpenAPI specification or using Now Assist with the third-party API documentation snippet as input. This simplifies the integration process compared to starting from scratch but still provides flexibility to accommodate specific requirements.

ServiceNow Technology Partner Store App:

ServiceNow Technology partners provide ready-to-use Integration solutions via the ServiceNow Store. Check on the ServiceNow store to see whether an integration product is already offered to serve your needs.

# **[A4]&[A5] Initiating system and Pull vs Push**

Two key concepts regarding ServiceNow integrations are the initiating system and the direction of data flow (pull vs push). Understanding these concepts is essential for designing and implementing effective integrations.

Initiating System:

The initiating system starts or triggers the integration process. Depending on the use case and chosen integration method, it can be either ServiceNow or a third-party system.

For instance, if ServiceNow needs to fetch data from an external database, ServiceNow acts as the initiating system. Conversely, if a third-party system needs to create a ticket in ServiceNow, the third-party system becomes the initiating system.

Pull vs. Push:

The terms ‘pull’ and ‘push’ refer to the direction of data flow between the systems.

A ‘pull’ integration occurs when ServiceNow retrieves or ‘pulls’ data from a third-party system. An example is when ServiceNow uses a REST API to fetch foundation data from an external system and store it in a ServiceNow table.

On the other hand, a ‘push’ integration happens when ServiceNow sends or ‘pushes’ data to a third-party system. For example, if ServiceNow, acting as the initiating system, replicates ticket data into a data warehouse, it’s a push integration.

There are pros and cons to having ServiceNow take control over an integration, e.g., pulling foundation data into the platform, compared to just waiting for the following data load to be pushed in by the other system at an inconvenient time.

The best possible combination of these two patterns depends on various factors, such as the frequency, volume, and complexity of the data exchange, the security and performance requirements, and the availability and capabilities of the 3rd-party system. You should establish a platform-wide guideline to ensure a consistent approach is followed by everyone building integrations for your organization.

# **[A6] Process (REST) APIs**

ServiceNow offers process-specific APIs for some use cases (e.g., Service Catalog or Change Management).

As the Process APIs require data to be in a specific format, it is impossible to transform it. Additionally, the Process API may skip certain validations (which you could implement in a Transform Map or RTE), which may have a negative impact on your process. Therefore, please confirm on a use-case-per-use-case basis if the Process API is a good match.

# **[A7] Choice of Web Service Protocol**

Different web service protocols can be used when integrating ServiceNow with external systems. However, not all protocols are equally suitable for every scenario. The following guidelines can help you choose the best protocol for your integration needs:

REST:

This is the most recommended protocol for ServiceNow integration. It is widely adopted in the industry, easy to use, and offers great low-code and debugging capabilities in the platform. REST uses JSON as the data format, which is lightweight and flexible.

GraphQL:

This newer protocol allows clients to specify the data they need from the server, reducing the amount of data transferred and improving performance. GraphQL can be used with ServiceNow through a custom GraphQL schema, but it requires more development and testing effort than REST.

SOAP:

This older protocol uses XML as the data format, which is more complex and verbose than JSON. SOAP should be avoided unless a specific requirement or legacy system only supports SOAP.

Open Database Connectivity (ODBC):

This protocol allows direct access to the ServiceNow database through an ODBC driver. This should only be considered a last-resort fallback, as it requires more maintenance and troubleshooting than web service protocols.

# **[A8] Table API vs. Scripted REST API**

When granting read access via REST or SOAP  to data in ServiceNow, two choices are available:

Standard Web Service (Table API):

This predefined API does not require further configuration, allowing for out-of-the-box integration capabilities for most platform tables.

Scripted REST/SOAP API:

This is a custom API that developers can script according to specific requirements. It offers more flexibility but requires more effort to set up and maintain.

The aim should always be for systems to retrieve data from ServiceNow in the original structure and move potential transformation into the responsibility of the 3rd-party system. If this is not possible, the preferred method would be a Scripted REST API calling a Subflow, which is primarily low-code. It involves creating a subflow containing the API's logic and calling this Subflow from the Scripted REST API. This approach reduces the required scripting and makes the API easier to maintain.

# **[B] Persist data in ServiceNow**

There are two reasons why you may not want to store data in ServiceNow:

- Very high data volume or change velocity: For extremely large or frequently changing datasets, storing data in ServiceNow may not be feasible. Remote tables ensure access without compromising performance.
- Legal or compliance constraints: Some data must remain within specific boundaries due to legal constraints. Remote tables enable compliance by allowing interaction without violating regulations.

# **[B1] Data Sources supported by Zero Copy Connectors**

Zero Copy Connectors allow retrieving data from 3rd party systems into Data Fabric tables. These tables can then be used to support business workflows. Like Remote Tables, Zero Copy Connectors cannot populate data in an existing table.

There are two types of connectors available:

- ServiceNow develops and supports primary connectors, with enhancements to improve Glide queries and list views, enabling most queries to run at the data source.
- Community connectors are created by the open-source community and provided by ServiceNow. They are certified for core functions but not supported by ServiceNow.

[Currently supported source systems and database types are listed on docs](https://www.servicenow.com/docs/csh?topicname=managing-connections-wdf.html&version=latest).

When the system is not supported by Zero Copy, but offers a web service, then Remote Tables are an alternative. Remote Tables also allow write operations to change data in the source system.

However, as they are significantly more complex to set up and maintain and limited in processable record counts, they should be considered a less favorable choice.

# **[C] Event-driven architecture (EDA)**

Event-driven architecture (EDA) is a design pattern that enables systems to communicate and react to events in real-time. By decoupling the producers and consumers of events, EDA can improve your applications' scalability, performance, and reliability. Usually, this is an existing or even mandated architecture principle organization-wide. Stream Connect lets you connect your ServiceNow instance to your existing Kafka environment and stream data bidirectionally between them.

# **[C1] Direction of data flow**

The first step is to determine the direction of the data flow relative to ServiceNow:

- Producing Data: ServiceNow needs to send data to Kafka, which then external systems subscribe to.
- Consuming Data: ServiceNow needs to receive data from Kafka, which an external system has streamed to an existing Kafka topic.

# **[C2] Consuming external data**

When ServiceNow needs to ingest data from a Kafka topic, the primary consideration is what you intend to do with the incoming data: Flows can be triggered via the Kafka Message trigger, whereas data can be transformed with either Transform Maps or ETL, depending on the target. Similar to the Scripted REST API, a Script Consumer can address any other use cases.

# **[C3] Streaming ServiceNow data**

When ServiceNow needs to push data out to a Kafka topic, consider the nature and volume of the data:

- There is a pre-built capability called Log Export Service for log and audit data.
- To stream any other data from ServiceNow to Kafka, using the Scriptable ProducerV2 API in a Business Rule provides better performance, whereas the Kafka Producer Action Step is easier to setup and maintain.

# **[D] AI Agents**

AI Agents in ServiceNow use automation and intelligence to streamline processes, offer personalized support, and enhance decision-making. Integrating these agents into systems boosts cross-platform efficiency and real-time insights, increasing AI value and enabling quick adaptation for competitiveness. Due to their non-deterministic behavior, AI agents require flexible, adaptive integrations rather than predictable, rule-based ones to maintain consistency and reliability.

On the Now Platform, you have four primary integration patterns for AI agents:

- REST/Web services (often via IntegrationHub Spokes)
- MCP (Model Context Protocol) — agent-to-tool
- A2A (Agent-to-Agent) — cross-platform agent interoperability
- Agentic Spokes and per-agent Tools within AI Agent Studio

# **[D1] A deterministic Web service might be the better choice**

RESTful APIs provide clear contracts and predictable schemas, making them ideal for deterministic integrations that need stability, auditability, and compliance. While MCP enables dynamic tool discovery and flexible orchestration, it introduces variability. Variability in MCP refers to the dynamic discovery and invocation of tools at runtime, which can cause differences in available capabilities, response formats, and execution paths between sessions. This can lead to risks like inconsistent outcomes, decreased predictability for compliance‑critical processes, and increased difficulty in ensuring auditability or deterministic behavior. For critical or regulated workflows, use REST for reliability.

# **[D2] MCP vs A2A**

MCP (Model Context Protocol) standardizes how agents discover and invoke tools, enabling quick capability extensions. It suits scenarios valuing flexibility and tool variety over strict determinism. A2A (Agent-to-Agent) manages collaboration between autonomous agents across platforms, exchanging plans and results. While MCP handles tool invocation, A2A manages inter-agent dialogue and task delegation. MCP simplifies adding functions; A2A offers complex workflows. Use MCP to extend a single agent; use A2A when multiple agents coordinate. Both can work together in layered systems for maximum adaptability.

# **[D3] When to Use an Agentic Spoke as an Agent and When to Add a Tool**

An Agentic Spoke (Now Assist for Spokes) is a ready-to-use solution for adding an agent capable of interacting with a third-party system to an agentic workflow.

[Currently available AI agents for Integration Hub are listed in ServiceNow docs](https://www.servicenow.com/docs/csh?topicname=available-spk-ai-agents.html&version=latest).

These are directly usable and require less maintenance, so they are preferred over a custom solution.

If an Agentic Spoke is unavailable, a custom agent needs to be equipped with a tool capable of performing the integration. While this can also be scripted, a Flow Action containing the web service logic is the better choice.

# **[E] UI-level Integrations**

When the need arises to display ServiceNow data or processes within a different application's user interface (UI), the ServiceNow platform offers several distinct capabilities.

# **[E1] CRM Components**

For Customer Service use cases, verify first if Engagement Messenger covers your use case, as this is a ready-to-use integration capability that just needs to be plugged into an existing website. If the external system is Adobe Experience Manager, then a set of predefined components exists as well.

# **[E2] UI Integration within a Mobile App**

If the objective is to embed ServiceNow functionality or display ServiceNow data directly within an existing native mobile application (iOS or Android), the Mobile SDK is the appropriate choice. It provides the tools and libraries necessary for developers to build ServiceNow integrations into their mobile app UIs.

# **[E3] iFrame**

It's best to use iFrames only when absolutely necessary, as they can sometimes introduce security concerns and make communication between embedded and host applications a bit tricky. Plus, they can affect how users experience and access the content, so considering other options might often be a better choice.

If none of the specific UI integration capabilities are applicable, you need to consider other integration methods.

# **[F] Fallback Solutions**

File-based integrations, robotic process automation (RPA), and email are available methods of integrating ServiceNow with other systems. However, these methods have some limitations and drawbacks, such as:

- File-based integrations require manual or scheduled data transfers, which can be slow, error-prone, and insecure.
- RPA relies on mimicking user actions on the user interface, which can be brittle, inefficient, and hard to maintain compared to a web service.
- While Email is a simple and widely used communication channel, it has limited capabilities for structured data exchange and processing and limited scalability.
- ServiceNow Lens may speed up data entry, but it requires installing a local client and taking a screenshot of the data.

Therefore, these three approaches should only be treated as fallback technologies for ServiceNow integrations. Whenever possible, ServiceNow integrations should use more robust and reliable methods, such as the options described on the left side of the decision tree.

# **Acknowledgments**

I want to thank the following people for providing feedback and improvement suggestions:

- Bruno De Graeve, ServiceNow
- David Skowronek, ServiceNow
- Ian Leu, ServiceNow

# **Changelog**

Version 3.1: Zurich September 2025

- Added a dedicated section for AI Agent Integrations with Spokes, MCP, and A2A
- Added a dedicated section for copyless integrations via Zero Copy Connector
- Added Portable Virtual Agent chat widget
- Added iFrame
- Added ServiceNow Lens
- Formatting changes and added more explanations to various decision points

Version 3.0: Yokohama April 2025

- Added a dedicated section for event-driven architecture
- Added a dedicated section for UI integrations
- Added the following capabilities
    - Flow Designer Action JDBC step
    - JDBC Data Source
    - Document Intelligence
    - External Content Connectors for AI Search
    - HR Multi-Instance Integration
    - MetricBase Time Series API
- Reworked Table API recommendation to include security requirements
- Updated ERP Canvas to reflect name change

Version 2.0: January 2025

- Reworked decision on data persistence requirements
- Clarified options for integration patterns between 2 ServiceNow instances
- Added ERP Data Hub
- Added Generative AI Controller
- Added Process Mining for External Data
- Added Performance Analytics with external data
- Added a remark to Spoke Generator

[ServiceNow Integration Pattern Decision Tree - 3.1 - Jochen Geist.pdf](Integration%20Design%20-%20How%20to%20choose%20the%20best%20patter/ServiceNow_Integration_Pattern_Decision_Tree_-_3.1_-_Jochen_Geist.pdf)

## Related

- [[Platform]]
- [[Knowledge Base Articles – Integrations]]
- [[ServiceNow – Integrations]]
- [[REST]]
- [[DevOps]]