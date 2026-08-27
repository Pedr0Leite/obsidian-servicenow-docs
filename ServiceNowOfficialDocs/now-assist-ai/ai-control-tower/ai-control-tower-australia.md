---
title: AI Control Tower
subtitle: Implementation Guide
release: Australia
source_date: July 2026
source_file: AI-Control-Tower.pdf
source_pages: 247
publisher: ServiceNow
tags:
  - servicenow
  - ai-control-tower
  - ai-governance
  - ai-risk-compliance
  - australia-release
---

# AI Control Tower

*ServiceNow — July 2026 — Australia release. © ServiceNow 2026. All Rights Reserved.*

> [!note] About this conversion
> Generated from `AI-Control-Tower.pdf` (247 pages).
> Images are **not embedded**. Every original screenshot or diagram is replaced, in its
> original position, by a blockquote of the form
> `> **[Figure N — p.X]** <description>` summarising what that image showed.
> Tables that span a page break in the PDF have been stitched back together.


> **[Figure 1 — p.1]** ServiceNow wordmark logo on the document cover page.

---

## AI Control Tower

July 2026

Australia release

---

# Table of Contents

- General - Overview
- General - Personas, Roles, and Responsibilities
- Core Personas
- Supporting Personas
- Identifying Relevant Stakeholders
- Persona-to-Role Mapping
- Access Control Implementation
- General - Technical and Functional Considerations
- Required Activation Sequence
- Additional Plugins
- Data Import
- Data Source Imports
- Native Data Sources (Now Platform)
- Workspace Configuration
- AI Risk and Compliance — Configuration Overview
- Access Control
- Out-of-the-Box Roles and Permissions
- Custom ACL Implementation Guidance
- Indicators and Continuous Monitoring
- General - Prelaunch
- How to Use This Checklist
- Stakeholder Identification
- Initial Inventory Scope
- Plugin Activation
- Core Role Provisioning
- Workspace Verification
- Initial Inventory Population
- Basic Lifecycle Validation
- Discover - Data Models
- Overview
- Audience
- User Roles and Responsibilities
- AI Asset Inventory Structure
- AI Asset Definitions
- AI Tools (Agentic Context)
- Understanding Interdependencies
- Implementation Considerations
- Examples of AI Asset Inventory by Industry, Use Case, and AI Type
- Why Organizations Require an AI Asset Inventory
- Ownership and Responsibility for AI Asset Inventory
- Determining the Scope of AI Asset Inventory
- Pre-Implementation Discovery Questions
- Discovery and Population of AI Assets
- Manual Intake Configuration – Record Producers and Workspace
- Record Producers for AI Asset Intake
- Record Producer: Request an AI Use Case
- Record Producer: Request an AI Model
- Record Producer: Request a Dataset
- Option II: Workspace-Based Intake
- UI Builder Experience Configuration
- UI Builder Page Configuration
- Page Parameters and Dynamic Behavior
- Intake Form Architecture
- Stepper-Based User Experience
- Form Controller and Dynamic Rendering
- Client Script Behavior
- Configuration Recommendations
- Discover - Discovery
- Overview
- Key Capabilities
- Managed vs. Unmanaged
- AI Service Graph Connectors for AI Control Tower
- AI Service Graph Connector for Amazon
- AWS APIs Used
- Amazon Data Mapping
- AI Service Graph Connector for Microsoft
- Azure Foundry Connection
- Microsoft Copilot Connection
- Shared Microsoft Target Tables
- Microsoft APIs Used
- Copilot APIs Used
- Data Flow Summary
- AI Service Graph Connector for Google Cloud Platform Vertex AI
- AI Service Graph Connector for LangGraph
- AI Service Graph Connector for n8n
- AI Service Graph Connector for Salesforce
- Additional Connector Properties
- Implementation Considerations
- Appendix
- Govern - Risk and Controls
- Intended Audience
- Understanding the AI Risk & Compliance Solution
- AI Artifacts Informational Records
- AI Model
- Dataset
- External Regulations
- Regulatory Agencies
- Authority Documents
- Citations
- Internal Business Operations
- Controls
- Policies
- Risk Exposure
- Risk Statements
- Risks
- Monitoring
- Issues
- Policy Exceptions
- AI Risk & Compliance Landscape
- Business Configuration
- Risk Assessment Methodology
- Residual Risk
- Assessment Template
- AI Risk & Compliance Onboarding Lifecycle
- Initiate AI System Intake & Explore the AI Control Tower
- Assess – Evaluate AI Use Case Impacts
- Build and Test – Implement Controls
- Deploy - Review the AI System Record and Finalize All Pre-Deployment Activities
- Monitoring, maintenance, and retirement
- Appendices
- B. End-User Documentation
- Govern - Now Assist Governance (Now Assist)
- Overview
- Automated AI Asset Synchronization
1. Sync Model Assets
2. Sync Dataset Assets
3. Sync Prompt Assets
4. Sync Agentic AI Assets
5. Sync AI Agents
6. Sync AI Use Cases
- Configuration Guidance
1. AI Model Sync
2. Dataset Sync
3. Prompt Sync
4. Agentic AI Asset Sync
- Configuration and Customization
- Govern - Lifecycle
- AI Control Tower Lifecycle
- AI Asset Lifecycle Overview
- Lifecycle
- Architectural summary
- AI Asset Lifecycle Data Flow and Object Relationships
- Technical summary
- Technical Implementation: Playbooks
- Deploy:
- Summary of AI System asset - State Transitions & Tasks
- Customization Guide
- Observe - Trace Collectors
- Prerequisites
- Configuration Steps
- Downstream Impact in AI Control Tower
- Troubleshooting
- References & Related Resources
- Measure - Value
- Value Management
- Release Compatibility
- Roles and Responsibilities
- Real-World Time Savings (RWTS) and AI Value
- Value Templates
- Value Calculation Framework
- Performance Analytics (PA) Integration
- Multi-Instance Framework (MIF) Configuration
- Data Architecture
- System Behavior and Automation
- Third-Party AI Asset Handling
- Operational Considerations
- Cross - Product Integration AI Strategy
- Required Plugins and Licensing
- Defining AI Strategies
- Navigating to AI Strategy Records
- Creating a Goal
- Cross Product Integration - AI Gateway
- Key Capabilities
- Pillars of AI Gateway
- AI Gateway in the ServiceNow AI Ecosystem
- Personas, Roles, and Responsibilities
- Technical and Functional Considerations
- AI Gateway
- Cross Product Integration - AI Case Management
- Intended Audience
- Understanding the AI Case Management Solution
- Solution Architecture
- Configurations
- Cross Product Integration - CMDB
- Asset Type to CMDB Class Mapping
- How AI Assets Enter the CMDB
- Automated Risk Classification at Intake (Q1 2026)
- Connecting AI Assets to Business Applications and Services
- Managed vs. Unmanaged Assets
- AI Implementation Patterns
- Gate 1: Architecture Review Board (Planning Stage)
- Gate 2: Digital Product Release (Deployment Stage)
- Process Flow Summary
- Critical Prerequisites
- Agent Identity and Chain of Custody
- Agent Platform Maturity
- MCP Discovery and Governance
- Blending Discovery Sources
- Regulatory Gaps
- AI-Specific Security Testing
- Frequently Asked Questions (FAQ)
- Govern - Risk and Control
- Value

# General - Overview

ServiceNow's AI Control Tower (AICT) provides enterprises with complete visibility into their AI footprint, enabling them to manage the full lifecycle of AI assets and identify and mitigate risks associated with AI investments. It ensures AI initiatives are governed, optimized, and aligned with overall business strategy.

The platform includes the AI Risk and Compliance application, which ships with pre-built content aligned with the EU AI Act and the NIST AI Risk Management Framework (AI RMF), helping organisations accelerate compliance and implement responsible AI practices from day one.

AICT is designed to equip AI Centers of Excellence (CoEs) and Chief AI Officers (CAIOs) with the capabilities needed to oversee and govern organizational AI operations. Built on the ServiceNow AI Platform, it offers a comprehensive suite of tools for managing, governing, and optimizing AI systems, models, datasets, prompts, and their inputs and outputs.

Whether AI solutions are developed in-house, sourced from third-party providers, or embedded within SaaS platforms, AI Control Tower functions as a centralized hub supporting the full lifecycle of AI assets from onboarding through retirement.

The AI Centre of Excellence (AI CoE)

The AI Centre of Excellence (AI CoE) drives responsible, scalable AI adoption across the organization. It sets standards, best practices, and governance for AI development, working closely with product teams to guide AI use cases, ensure ethical design, and provide tools, models, and expertise to accelerate delivery.

In parallel, the CoE collaborates with enterprise architects, PMOs, risk, compliance, and security teams to ensure AI systems align with enterprise architecture, project governance, regulatory compliance, and cybersecurity standards. This dual collaboration ensures AI solutions are innovative and enterprise-ready — balancing agility with control.

AI Control Tower connects the AI CoE/CAIO with relevant enterprise stakeholders through integrated workflows. These stakeholders include Risk, Legal, Audit, Security, Compliance, Third-Party Risk, Enterprise PMO, Data Governance, Enterprise Architecture, Product Teams, and Business Users.

#### Functional Framework

AI Control Tower is organized around five interconnected functional areas, anchored by AI Inventory Management in the CMDB as the foundational layer. Each area addresses a distinct governance dimension while sharing a common data foundation.

| **Function** | **Description** |
| --- | --- |
| AI Inventory (Foundation) | All AI assets — systems, models, prompts, datasets, agents, and MCP servers — are tracked within the CMDB as configuration items. This centralized inventory provides business context by connecting AI initiatives to enterprise services and assets. It serves as the foundation for all five functional areas. |
| Discover | Automatically discover AI assets across the enterprise from hyperscalers, SaaS platforms, and development environments. Build a complete inventory of AI systems, agents, models, data, prompts, and MCP servers. Map dependencies and business context. Assets are maintained in the CMDB within out-of-the-box CI classes. |
| Govern | Establish AI strategy, manage risk across the AI lifecycle, deploy and enforce integrated controls, and demonstrate compliance. Includes impact assessments, risk classification, control attestation, policy management, and regulatory reporting aligned to the EU AI Act and NIST AI RMF. |
| Secure | Track AI access, security posture metrics, and guardrails. Take action through automated workflows to maintain control across the AI landscape. Security scores surface urgent issues across hyperscalers, including monitoring data leaks, prompt injections, model vulnerabilities, privileged agents, and dormant agents. |
| Observe | Continuously monitor, and evaluate AI agent performance through metrics and log traces. Supports identification of performance degradation, operational anomalies, and behavioral drift. |
| Measure | Track AI's business impact with metrics covering adoption rates, realized value, and ROI. Consolidates productivity, cost avoidance, and risk reduction into a single view with configurable value templates and drill-down from portfolio level to individual model performance. |

#### Key Capabilities

The following capabilities span all five functional areas and represent the core value delivered by the AI Control Tower platform.

| **Capability** | **Description** |
| --- | --- |
| AI Governance & Compliance | Supports adherence to internal policies and global regulations, including privacy, data governance, and ethical AI requirements. Pre-built content aligned to EU AI Act and NIST AI RMF, with Smart Assessment Engine templates for impact, conformity, and fundamental rights assessments. |
| Lifecycle Management | Manages the complete AI asset lifecycle — onboarding, assessment, build & test, deployment, and retirement — powered by configurable Playbook workflows that coordinate tasks across AI Stewards, Product Owners, and Risk & Compliance teams. |
| Visibility & Risk Management | Provides visibility and control over AI systems, models, prompts, datasets, and workflows. Identifies potential risks and supports the implementation of controls. Risk heatmaps, compliance scoring, and regulatory change management support audit readiness. |
| AI Asset Inventory | Populated via automated discovery (Now Assist, Amazon Bedrock, Azure AI Foundry, Copilot Studio, GCP Vertex AI), manual intake through record producers and workspace, or API integration. Assets are maintained as out-of-the-box CMDB classes. |
| AI Strategy | When integrated with Strategic Portfolio Management (SPM), it supports AI demand management, roadmaps, portfolios, scenario planning, and investment tracking. A foundational Goals Framework is available out-of-the-box to all AICT customers. |
| AI Value Measurement | Consolidates ROI, productivity, cost avoidance, and risk reduction metrics into a single dashboard. Configurable value templates allow organizations to standardize how teams report and measure AI value. |
| Security & Privacy | AI Security Scores track overall AI health with AI-generated insights surfacing urgent issues. Monitors data leaks, prompt injections, model vulnerabilities, privileged and dormant agents. Includes an access map using node-graph visualization. |
| Health & Evaluation | Monitors and evaluates AI agent performance through metrics, log traces, and health indicators. Supports identification of performance degradation, operational anomalies, and behavioral drift. |
| AI Case Management | Provides centralized handling of AI-related cases and inquiries submitted via the Employee Center Portal. Includes investigation workflows, evidence management, regulatory violation tracking, and root cause analysis. |
| MCP Governance | Provides governance of Model Context Protocol (MCP) servers and connections through the AI Gateway, supporting oversight of agentic AI tool access and external AI source integration. |

##### Workspaces Overview

AICT provides two primary workspaces that serve different personas and governance functions, each designed to deliver role- appropriate visibility and action.

##### AI Control Tower Workspace

Provides centralized visibility for AI Stewards and Product Owners into all AI assets and related activity across the organization.

| **Tab** | **Description** |
| --- | --- |
| Overview | Displays all AI systems by lifecycle phase, type (Agentic, Generative, Classic), risk classification, provider, compliance status, and AI cases by priority. |
| AI Strategy | Displays AI-related priorities, goals, planning items, and execution activities such as projects and demands. |
| AI Asset Inventory | Lists all AI-related assets including models, prompts, systems, and datasets, with related assets, risk & compliance status, and KPIs & metrics. |
| Value | Shows total productivity gained, average AI users, top AI systems by value, task closure efficiency, success rates, and creator skills metrics. |
| Health | Provides AI system health monitoring and performance indicators. |
| Evaluation | Supports continuous evaluation of AI agent performance through metrics and log traces. |
| Risk & Compliance | Displays risk classification and compliance posture. |
| Security & Privacy | Shows AI Security Score, access issues, autonomous vs. supervised tool metrics, privileged agent counts, dormant agent detection, and AI-generated security insights. |
| AI Cases | Provides a dashboard of open and active cases and inquiries related to AI risks or compliance events. |

#### AI Risk & Compliance Workspace

Provides AI Risk & Compliance Managers with visibility into the risk and compliance posture of all AI assets, including systems, models, and datasets.

| **Tab** | **Description** |
| --- | --- |
| Risk and Compliance | Displays the risk classification of the AI asset inventory and compliance posture based on authority documents (EU AI Act, NIST AI RMF) and internal policies. Includes risk overview, risk heatmap, and compliance scoring. |
| Operations | Shows AI systems segmented by state and department, with visibility into risk assessments, AI assessments, control assurance, issues, policy exceptions, and AI cases. |
| AI Cases | Provides cases and inquiries dashboards with trends, tracking, action tasks, and issue management. |

#### Related Platform Integrations

AICT integrates with several ServiceNow platform capabilities to extend governance, security, strategy, and data management across the AI landscape. The following table summarizes key integration points by domain.

| **Domain** | **Capabilities & Integration Points** |
| --- | --- |
| AI Strategy (SPM) | Goals Framework (OOB) for managing AI strategies, goals, and targets. Strategic Planning plugin (requires SPM Pro license) adds AI demand management with Investment Type set to Artificial Intelligence, portfolio plans with AI-specific filtering, capacity planning and financial analysis, scenario planning, and visibility into all work mapped to strategic goals. |
| Security (SecOps) | AI Security Score evaluates AI asset security posture against ServiceNow best practices (Good 80– 100%, Fair 50–79%, Bad <50%). AI Identity & Access Governance (Veza) for AI agent identity and access controls. AI Security Incident Response (SIR) for incidents impacting AI systems. AI Exposure Management (USEM) for vulnerability tracking across AI assets. |
| AI Gateway | MCP (Model Context Protocol) governance for oversight and control of AI agent connections to external tools, data sources, and AI services. Manages approved third-party model providers (AWS Anthropic, Azure OpenAI, Google Gemini) and enforces global/regional data routing policies. Related integrations include Privacy (PRM) and Data Governance (DDW + WDF + Vault). |
| CMDB / CSDM | AI asset inventory natively built within the CMDB. All AI assets tracked as configuration items using OOB CI classes — no custom classes required. Supports hierarchical AI system relationships and related asset linkages. Integrates with Enterprise Architecture (EA) for mapping AI systems to business capabilities. Automated discovery from Amazon Bedrock, Azure AI Foundry, Copilot Studio, GCP Vertex AI, and Now Assist maintains inventory on an ongoing basis. |

# General - Personas, Roles, and Responsibilities

This section describes the key personas involved in the end-to-end implementation and management of AI assets within AI Control Tower. It maps organizational personas to their corresponding AICT system roles and outlines the responsibilities associated with each. It is particularly important that these stakeholders are educated on the key principles of responsible AI and informed on what to expect as AI is introduced to their workflows.

## Core Personas

AICT is designed around three core personas that correspond to the primary organizational roles responsible for AI governance. Each persona maps to one or more out-of-the-box system roles in the platform.

### AI Steward

This persona is accounatble for [SC1] the platform’s data assets and AI capabilities, ensuring data quality, integrity, and ethical use. The steward implements governance policies to maintain compliance, security, and responsible AI practices across ServiceNow applications and workflows. They oversee AI governance, aligning AI initiatives with organizational values, legal standards, and risk management practices. The role includes monitoring AI performance, bias, and compliance, fostering transparency, and promoting fairness.

They collaborate across departments to implement best practices, educate teams on AI usage, and guide decision-making about AI adoption. The AI Steward acts as a bridge between technical teams, leadership, and external stakeholders to ensure AI serves both business goals and societal good.

Example titles: Chief AI Officer (CAIO), VP of AI Strategy, Head of AI Governance, AI Program Director, Director of Data & AI, AI Centre of Excellence Lead

### AI Product Owner

The AI Product Owner drives the development and delivery of AI-powered products, aligning them with business goals and user needs. They define product vision, prioritize features, and manage the AI product backlog. Working closely with data scientists, engineers, and stakeholders, they translate business requirements into technical deliverables.

They ensure the AI solution is viable, valuable, and ethical, balancing innovation with compliance. Throughout the product lifecycle, they validate performance, gather feedback, and adjust priorities to optimize outcomes and deliver measurable value.

Example titles: AI Product Manager, ML Product Owner, AI Solutions Lead, Technical Product Manager – AI, AI Use Case Owner, AI Applications Manager

### AI Risk / Compliance Manager

The AI Risk and Compliance Manager identifies, assesses, and mitigates risks related to AI use in the business. They ensure AI systems comply with laws, regulations, and internal policies, addressing issues such as bias, privacy, and transparency. Within the AI Centre of Excellence, they develop frameworks, standards, and controls for safe AI deployment across teams.

They collaborate with legal, IT, and business units to monitor AI governance, conduct audits, and manage incidents. Their role ensures responsible AI use, minimizes liability, and builds trust in AI solutions organization-wide.

Example titles: Chief Risk Officer (CRO), Chief Compliance Officer (CCO), VP of AI Risk, Director of AI Compliance, GRC Manager – AI, AI Ethics & Compliance Lead, Head of Responsible AI

## Supporting Personas

In addition to the three core personas, AICT includes several supporting roles that participate in specific areas of AI governance, risk management, and case resolution. These personas typically operate under the direction of a core persona and are scoped to a narrower set of responsibilities.

### AI Risk / Compliance Analyst

The AI Risk and Compliance Analyst performs hands-on risk and compliance work on assigned AI systems. Unlike the Manager role, the Analyst’s access is limited to records specifically assigned to them. They execute impact assessments, manage lifecycle tasks, perform risk assessments, and complete control attestations within their assigned scope.

Example titles: GRC Analyst, IT Risk Analyst, AI Compliance Analyst, Technology Risk Analyst, AI Audit Analyst

### AI Governance Stakeholder

AI Governance Stakeholders are business users, subject matter experts, or team members who participate in AI governance activities but do not manage AI assets or lead risk assessments. They may submit AI cases, complete assigned tasks such as control attestations, or require read-only visibility into AI systems and assessments for oversight or reporting purposes.

Example titles: Business Unit Leader, Department Head, Legal Counsel, Privacy Officer, Internal Auditor, Data Governance Lead, Enterprise Architect, Security Analyst

### AI Case Submitter

AI Case Submitters are employees or business users who report AI-related cases or raise inquiries through the Employee Center. They do not investigate or manage cases but initiate the case management process by submitting relevant details and supporting documentation.

Example titles: Any employee or business user who interacts with AI systems and needs to report an issue, concern, or question

### AI Case Analyst

The AI Case Analyst reviews and investigates AI cases and inquiries assigned to them. They identify impacted areas such as policies, regulations, and enterprise-wide compliance risks, and manage issues related to those areas to address root causes.

Example titles: Compliance Case Analyst, AI Incident Investigator, GRC Analyst, AI Compliance Specialist

### AI Case Manager

The AI Case Manager has full visibility into all AI cases and inquiries across the organization. They oversee case resolution, monitor case volume and severity, and ensure timely investigation and closure.

Example titles: Compliance Case Manager, AI Governance Manager, AI Operations Manager, Head of AI Case Management

### AI Case Admin

The AI Case Admin has full administrative access to case management functions, including configuration of case types, state models, and assessment templates. This role is typically held by a platform administrator responsible for configuring the AI Case Management module.

Example titles: ServiceNow Platform Administrator, AI Governance Platform Admin, GRC System Administrator

## Identifying Relevant Stakeholders

In addition to the personas listed above, organizations should identify additional stakeholders who may need to participate in AI governance activities. The following questions can help determine whether a given role should be involved in designing, implementing, or monitoring a new AI-driven use case. If the answer to any of these questions is “yes,” that stakeholder should be included:

• Does this role have oversight over users interacting with an AI workflow or application?

• Does this role have oversight or control over resources that an AI workflow or application will interact with?

• Does this role have an interest in the security of the AI workflow or resources accessed by the agent?

## Persona-to-Role Mapping

The following table maps organizational personas to their corresponding out-of-the-box system roles, role IDs, and key capabilities within AICT.

| **Persona** | **System Role** | **Role ID** | **Key Capabilities** |
| --- | --- | --- | --- |
| AI Steward | AI Steward | sn_ai_governance.ai_steward | Executes AICT initiatives; manages policies; configures multi-instance management |
| AI Steward | AI Control Tower Workspace User | sn_ai_governance.workspace_user | Owns and manages AI assets; accesses AI Portfolio |
| AI Product Owner | AI Asset Owner | sn_ai_asset_mgmt.ai_asset_owner | Manages asset lifecycle (intake to retirement); includes Assessment Admin role; SAE administrator |
| AI Risk / Compliance Manager | AI Risk and Compliance Manager | sn_grc_ai_gov.ai_risk_and_compliance_manager | Access to all AI systems; initiates impact/risk assessments; manages lifecycle; initiates control attestations |
| AI Risk / Compliance Manager | AI Risk and Compliance Admin | sn_grc_ai_gov.ai_risk_and_compliance_admin | Full configuration access; sets up risk/impact frameworks and templates; defines automation rules; profiles AI case types; deletes AI systems |
| AI Risk / Compliance Analyst | AI Risk and Compliance Analyst | sn_grc_ai_gov.ai_risk_and_compliance_analyst | Access to assigned AI system records only; initiates impact/risk assessments; manages lifecycle; performs control attestations |
| AI Governance Stakeholder | AI Risk and Compliance User | sn_grc_ai_gov.ai_risk_and_compliance_business_user | Creates AI cases via Employee Center; works on assigned tasks; performs control attestations |
| AI Governance Stakeholder | AI Risk and Compliance Reader | sn_grc_ai_gov.ai_risk_and_compliance_reader | Read-only access to AI systems and AI impact assessments |
| AI Governance Stakeholder | AI System Reader | sn_grc_ai_gov.ai_risk_and_compliance_ai_system_reader | Read-only access to AI systems in both AICT and AI Risk & Compliance workspaces |
| AI Case Submitter | AI Case Business User | sn_ai_case_mgmt.ai_case_business_user | Creates AI cases and inquiries in Employee Center |
| AI Case Analyst | AI Case Analyst | sn_ai_case_mgmt.ai_case_analyst | Reviews assigned cases/inquiries; manages related compliance areas; addresses root cause issues |
| AI Case Manager | AI Case Manager | sn_ai_case_mgmt.ai_case_manager | Full visibility into all AI cases and inquiries |
| AI Case Admin | AI Case Admin | sn_ai_case_mgmt.ai_case_admin | Full administrative access to case management functions |

## Access Control Implementation

The following guidance applies when configuring access control for AI Control Tower roles.

Implementation Considerations:

• Provision multiple out-of-the-box roles to user groups (e.g., assign AI System Reader to a Compliance Reader group).

• Modify ACLs sparingly to maintain upgradeability and ensure compatibility with future AICT features.

Leading Practices:

• Apply the principle of least privilege.

• Assign roles to groups, not individual users.

• Use the condition builder and scripts for complex scenarios.

• Reuse logic using script includes for consistency.

• Comment custom ACL logic clearly and document their purpose and associated roles.

• Use field-level ACLs for sensitive data; use table-level ACLs for general control.

• Avoid duplicating ACLs for the same operation.

• Conduct thorough access testing by user type and scenario.

• Always enforce data protection with server-side ACLs—do not rely on client-side scripts or policies.

# General - Technical and Functional Considerations

## Required Activation Plugin

| **Plugin Name** | **Scope ID** | **Purpose** |
| --- | --- | --- |
| AI Control Tower Core | com.sn_aict | Enables management, optimization, governance, security, and value measurement of AI investments with embedded risk and compliance lifecycle management. |

> [!important] Important
> Confirm version compatibility with your ServiceNow release before activating. Always validate against the current store listing for the version available on your instance.

## Additional Plugins

Depending on your implementation scope, additional plugins may be present in your ServiceNow instance. These extend AI Control Tower with capabilities for security and privacy monitoring, AI asset discovery, Now Assist integration, performance dashboards (value, health, and engagement), and the AI Lens reporting module.

| **Plugin** | **Scope ID** | **Notes** |
| --- | --- | --- |
| AI Security and Privacy | sn_ai_security | Covered in the Secure section of this guide. |
| AI Discovery | sn_ai_disc | Covered in the Discover section of this guide. |
| AI Control Tower for Now Assist | sn_aict_nowassist | Required to sync Now Assist AI skills into AICT. |
| Value Dashboard for AICT | sn_ai_value | Covered in the Measure section of this guide. |
| Health Dashboard for AICT | sn_ai_health | Covered in the Observe section of this guide. |
| Engagement Dashboard for AICT | sn_ai_engagement | Covered in the Observe section of this guide. |
| AWH for AI Control Tower | sn_awh_config | Agent Workspace Hub configuration. |
| ServiceNow AI Lens | sn_ai_lens | AI reporting and lens capabilities. |

## Data Import

Populating the AI Control Tower with your organization's AI inventory is typically the first implementation task after plugin activation. There are three primary patterns for importing AI asset data, and most implementations use a combination of all three. The appropriate pattern depends on whether your organization needs real-time synchronization, bulk batch loading, or native platform integration.

### Import Patterns

| **Pattern** | **Best For** | **Considerations** |
| --- | --- | --- |
| API Integration | Organizations maintaining a live AI registry in another system requiring real-time synchronization. | Use Scripted REST APIs for complex payload structures. Requires development effort for initial setup. |
| Data Source Imports | Bulk one-time or scheduled batch loads from spreadsheets or external databases using import sets with transform maps. | Works well for organizations that do not require real-time sync. Requires field mapping configuration. |
| Native Data Sources | Organizations already on the Now Platform are seeking the most seamless path with no manual mapping required. | Record Producers and the Now Assist Sync job offer the lowest-friction path. MCP server assets can be synced automatically. |

### Key Field Mappings

When importing AI assets, organizations should map source data to out-of-the-box (OOB) fields to ensure consistency. The following fields are critical to establish lifecycle accountability and governance coverage from day one.

| **Field** | **OOB Field Name** | **Purpose** |
| --- | --- | --- |
| Model Category | model_category | Distinguishes between AI systems, models, and datasets. |
| Provider/Manufacturer | manufacturer | Enables vendor oversight and third-party risk tracking. |
| Managed By | managed_by | Assigns lifecycle accountability to a named owner. |

### API Integration

The AI Assets API provides OOTB endpoints for CRUD operations (Create, Read, Update, Delete) across AI asset types. This integration pattern is best suited for organizations that maintain a live AI registry in another system and require real-time synchronization.

> [!important] Important
> The AI Assets API requires the Asset Classes (sn_ent) plugin to be installed. Confirm this dependency is satisfied before configuring API-based integrations.

#### OOTB API Endpoints

| **Asset Type** | **Method** | **Endpoint** | **Purpose** |
| --- | --- | --- | --- |
| AI System | GET | /sn_ent/asset/ai_system/{sys_id} | Retrieves data for a specified AI system asset. |
| AI Model | GET | /sn_ent/asset/ai_model/{sys_id} | Retrieves data for a specified AI model asset. |
| AI Dataset | GET | /sn_ent/asset/ai_dataset/{sys_id} | Retrieves data for a specified AI dataset asset. |
| AI Prompt | GET | /sn_ent/asset/ai_prompt/{sys_id} | Retrieves data for a specified AI prompt asset. |
| AI System | POST | /sn_ent/asset/ai_system | Creates a new AI system asset entry across the AI System Digital Asset and Product Model tables. |
| AI Model | POST | /sn_ent/asset/ai_model | Creates a new AI model asset entry. |
| AI Dataset | POST | /sn_ent/asset/ai_dataset | Creates a new AI dataset asset entry. |
| AI Prompt | POST | /sn_ent/asset/ai_prompt | Creates a new AI prompt asset entry. |
| AI System | PUT | /sn_ent/asset/ai_system/{sys_id} | Updates a specific AI system record. |
| AI Model | PUT | /sn_ent/asset/ai_model/{sys_id} | Updates a specific AI model asset record. |
| AI Dataset | PUT | /sn_ent/asset/ai_dataset/{sys_id} | Updates a specific AI dataset asset record. |
| AI Prompt | PUT | /sn_ent/asset/ai_prompt/{sys_id} | Updates a specific AI prompt asset record. |

> [!tip] Tip
> For complex payload structures or custom authentication requirements, use the Scripted REST API to define your own service endpoints, query parameters, and headers. This option provides the most control over data structure but carries the highest implementation complexity.

## Data Source Imports

Import sets with transform maps provide a structured mechanism for loading AI asset data from external sources. This approach is well-suited for bulk one-time migrations or scheduled batch loads from spreadsheets, databases, or third-party AI registries.

Supported data source types are listed below. After defining the data source, create the import set table, configure a transform map to map fields to the AICT target tables, and, alternatively, set up scheduled imports for ongoing synchronization.

| **Data Source Type** | **Description** |
| --- | --- |
| OIDC | Data accessible via OpenID Connect. |
| JDBC | Data in a database accessible via JDBC. Supported drivers include Oracle, MySQL, Sybase, DB2 Universal, and MS SQL Server. |
| File | Data in a recognized file format, accessible locally or remotely through several file retrieval methods. |
| REST (Integration Hub) | Data in a REST API, accessible through Integration Hub. |
| LDAP | Data from an LDAP server accessible through ports 389 (LDAP) or 636 (LDAPS). |
| Data Stream Integration Hub | Data loaded from a Data Stream Action via Integration Hub. |
| Custom (Load by Script) | Data obtained using a custom script. |

## Native Data Sources (Now Platform)

For organizations already on the Now Platform, native data sources offer the most seamless path with no manual field mapping required. Record Producers guide asset owners through structured intake forms, while the Now Assist sync job automatically populates the AI asset inventory from existing AI skills.

| **Native Source** | **What It Populates** |
| --- | --- |
| Request an AI System | Creates an AI System record via the AI System Record Producer. |
| Request an AI Use Case | Creates an AI Use Case intake record linked to a system. |
| Request an AI Model | Creates an AI Model record linked to a system. |
| Request a Dataset | Creates an AI Dataset record and associates it with a model. |
| Sync Now Assist AI Assets (Scheduled Job) | Automatically populates AI models, datasets, prompts, and agentic AI assets from Now Assist AI Skills. Requires the AI Control Tower for Now Assist plugin (sn_aict_nowassist). |

> [!tip] Tip
> MCP server assets can also be added natively via the AI Control Tower workspace. This capability was introduced in recent releases and surfaces AI gateway configurations directly within AICT.

## Workspace Configuration

The AI Control Tower workspace is the primary interface for AI stewards, risk managers, and executive stakeholders. Rather than prescribing a fixed layout, the platform is designed to be configured to reflect your organization's priorities. Home page widgets can be arranged to surface the metrics most relevant to each role.

Configuration decisions should be driven by your defined personas and their day-to-day workflows. For example, a risk manager may want the Risk Heatmap and Compliance Overview front and center, while a program manager may prioritize AI Systems by State and Open AI Cases. Refer to the Personas, Roles, and Responsibilities section of this guide when determining widget placement.

> [!tip] Tip
> Key configuration points include the home page widget arrangement, heatmap workbench thresholds, list view filters, and the strategic priorities view (filterable by strategic priority or department). Configuration should be customer-driven. Avoid prescribing specific settings that may not align with the organization's operating model.

### AI Control Tower Workspace Tabs

The AI Control Tower workspace is organized into the following tabs. Each tab is designed for a specific set of personas and use cases.

| **Tab** | **What It Surfaces** |
| --- | --- |
| Overview | Summary information, including AI systems by state, type, risk classification, providers, and trends. |
| AI Strategy | Visuals for monitoring and tracking AI strategies — goals, priorities, cost figures, efficiency, quality, and engagement outcome dimensions. Filterable by strategic priority or department. |
| AI Asset Inventory | A unified view into the composition of the organization's AI inventory by type, state, provider, and department alignment. |
| Value | Guides decision-making on AI system value through visibility into productivity metrics, AI user counts, and daily usage patterns. |
| Adoption | Provides an overview of overall user engagement using daily AI actions, average daily user engagement, and AI feedback data points. |
| Risk and Compliance | Surfaces key information on the management of risk and compliance topics for AI systems — including risk classification, compliance posture by authority document, and policy exceptions. |
| Security and Privacy | Monitors and manages AI security and access, including access requests and dormant AI system identification. |
| AI Cases | Enables case managers and analysts to monitor and act on formal AI-related cases and inquiries across the organization. |
| AI Gateway | Surfaces AI gateway configurations and MCP server visibility managed within AI Control Tower (available in recent releases). |

### AI Risk and Compliance Workspace

The AI Risk and Compliance workspace enables the AI risk and compliance manager to view the complete risk posture of the AI asset inventory. It is organized into three primary tabs and provides a detailed operational view that complements the summary- level information in the main AICT workspace.

> [!important] Important
> AI risk and compliance details are also accessible under the Risk and Compliance tab in the AICT workspace. Ensure both workspaces are configured before conducting risk reviews.

| **Tab** | **What It Surfaces** |
| --- | --- |
| Risk and Compliance | Risk classification of the AI asset inventory and compliance posture across selected authority documents and policies. Includes the Risk Heatmap and AI systems by aggregated risk score. |
| Operations | Overview of AI systems by state and department. Surfaces risk assessments, AI assessments, control assurance, issues by priority, policy exceptions by risk rating, and AI cases by priority. |
| AI Cases | Provides visibility into active AI cases by type, priority, and trends, alongside AI inquiries by type, priority, and trends. |

#### Operations Tab — Widget Reference

The Operations tab provides the most detailed operational view in the Risk and Compliance workspace. The following widgets are available for configuration.

| **Widget** | **Description** |
| --- | --- |
| AI Systems by State | Displays the number of AI systems in states such as New, Assess, Build, Review for Deployment, Live, and Monitor. |
| AI Systems by Department | Displays AI systems per department (HR, Sales, Customer Support, IT). Can be filtered by risk classifications, including High, Medium, Low, Unacceptable, and To Be Determined. |
| Risk Assessments | Number of assessments that are open, in progress, overdue, and due within 7 days. |
| AI Assessments | Number of assessments in draft, assigned, and work-in-progress states, with overdue and 7-day due indicators. |
| Control Assurance | Attestations and control tests that are open or overdue, plus indicators open and failed in the last 6 months. |
| Issues | Number of ssues that are open, overdue, and due within 7 days, with a pie chart breakdown by priority. |
| Policy Exceptions | Policy exceptions open, overdue, and due within 7 days, with a pie chart by risk rating. |
| AI Cases | Active AI cases that are overdue and due in 7 days, with a pie chart by priority. |

## AI Risk and Compliance — Configuration Overview

To use the AI Risk and Compliance application, you must complete the following configuration steps in order. Assessment templates must be published before risk scores can be calculated accurately, and automation flows must be reviewed to confirm correct behavior for your implementation.

> [!important] Important
> Configuration of the AI Risk and Compliance workspace requires completing all four steps below. Skipping the publish step for assessment templates will result in inaccurate risk assessment scores.

| **Configuration Step** | **Guidance** | **Reference** |
| --- | --- | --- |
| Install AI Risk and Compliance | Activate the AI Risk and Compliance plugin and confirm dependencies are satisfied. | Yokohama GRC documentation |
| Install Content Pack | Activate the AI Risk and Compliance Content plugin to load EU AI Act and NIST AI RMF frameworks. | Yokohama GRC documentation |
| Publish Assessment Templates | Assessment templates must be published before risk and impact scores can be calculated correctly. | Yokohama GRC documentation |
| Review Activated Flows | Note the flows that are activated automatically and confirm they align with your automation requirements. | Yokohama GRC documentation |

## Access Control

AI Control Tower ships with a set of out-of-the-box roles designed to support the key personas involved in AI governance, risk management, case handling, and asset oversight. These roles are applied to groups aligned to a given persona — for example, a group containing AI stewards would be provisioned the AI Steward role.

> [!tip] Tip
> AI risk and compliance details are accessible under the Risk and Compliance tab in the AICT workspace. Ensure role assignments align with workspace configuration to avoid personas landing in views they cannot act on.

## Out-of-the-Box Roles and Permissions

| **Role** | **Scope ID** | **Responsibilities** |
| --- | --- | --- |
| AI Steward | sn_ai_governance.ai_steward | • Leads execution of AI Control Tower initiatives. • Understands AI assets and AICT policies. • Coordinates cross-functional teams to confirm policy adherence. • Configures Multi-instance Management for AI Control Tower. |
| AI Control Tower Workspace User | sn_ai_governance.workspace_user | • Owns and manages AI assets. • Accesses the AI Portfolio on the AICT home page. |
| AI Asset Owner | sn_ai_asset_mgmt.ai_asset_owner | • Manages AI assets (systems, models, datasets, prompts) through the asset |
|  |  | lifecycle from intake to retirement. • Includes Assessment Admin platform role and is an administrator for the SAE application. • Automatically assigned a Deploy phase task; does not independently change asset state. |
| AI Risk and Compliance Admin | sn_grc_ai_gov.ai_risk_and_compliance_admin | • Configures risk assessment methodologies, contribution factors, and impact assessment templates. • Defines automation rules for impact assessments. • Sets up and profiles AI case types. |
| AI Risk and Compliance Manager | sn_grc_ai_gov.ai_risk_and_compliance_manager | • Accesses all AI systems on the instance. • Initiates impact assessments, risk assessments, and control attestations. • Manages the lifecycle of AI systems. |
| AI Risk and Compliance Analyst | sn_grc_ai_gov.ai_risk_and_compliance_analyst | • Same capabilities as the Manager role, but scoped only to assigned records. |
| AI Risk and Compliance User | sn_grc_ai_gov.ai_risk_and_compliance_business_user | • Creates AI cases via the Employee Center. • Works on assigned tasks and performs control attestations. |
| AI Risk and Compliance Reader | sn_grc_ai_gov.ai_risk_and_compliance_reader | Read access to AI systems and AI impact assessments. |
| AI System Reader | sn_grc_ai_gov.ai_risk_and_compliance_ai_system_reader | Read access to AI systems in both the AICT workspace and AI Risk and Compliance workspace. |
| AI Case Business User | sn_ai_case_mgmt.ai_case_business_user | Creates AI cases and AI inquiries via the Employee Center. |
| AI Case Analyst | sn_ai_case_mgmt.ai_case_analyst | • Reviews AI cases and inquiries assigned to them. • Identifies and manages impacted policies, regulations, and compliance risks. • Manages issues related to impacted areas to eliminate root causes. |
| AI Case Manager | sn_ai_case_mgmt.ai_case_manager | Reviews all AI cases, AI inquiries, and associated information. |
| AI Case Admin In addition to the roles listed above, implementers should consider whether AI Model Owners and AI Dataset Owners need to be represented as distinct roles. These are not currently defined as separate OOTB roles but can be implemented by provisioning the AI Asset Owner role to groups scoped to model or dataset record types. Confirm the current role list with the product team as role definitions evolve across releases. | sn_ai_case_mgmt.ai_case_admin | Full administrative access to case management, including configuration of case types, state models, and assessment templates. |

## Custom ACL Implementation Guidance

When out-of-the-box roles do not fully address an organization's access requirements, ACLs can be modified to change the baseline permission set. Implementation teams should limit the overall number of custom ACLs to maintain upgradability and ensure organizations can leverage the latest AICT features with minimal rework.

| **Leading Practice** | **Guidance** |
| --- | --- |
| Principle of Least Privilege | Grant only the minimum access necessary for users to perform their tasks. |
| Role-Based Assignment | Define and assign roles to groups, not directly to users. Avoid hard-coding user- specific logic in ACLs. |
| Condition Builder for Complex Scenarios | Use the condition builder and advanced script for context-based, complex access scenarios. |
| Reusable Logic | Move reusable logic into the script includes. Keep ACLs clean and consistent. |
| Document Custom ACLs | Clearly comment any custom logic in script-based ACLs. Document their purpose and associated roles. |
| Field vs. Table Level ACLs | Use field-level ACLs for sensitive fields such as financial data. Use table-level ACLs for broader access control. |
| Avoid Duplicate ACLs | Do not duplicate ACLs for the same operation and table/field combination. |
| Test Thoroughly | Test access for different types of users and groups. Test every possible use case before deployment. |
| Server-Side Validation | Use server-side validation or ACLs for all sensitive data changes. Do not rely solely on client scripts or UI policies. |

## Indicators and Continuous Monitoring

Indicators enable continuous monitoring of the risks contributing to risk classification of the AI asset inventory, as well as the controls contributing to compliance scores by authority document and policy. Within the Risk and Compliance section of AICT, indicators are the primary mechanism for automating governance oversight at scale.

### Core Concepts

| **Concept** | **Description** |
| --- | --- |
| Indicator | Collects data to monitor a single control or risk. Used to gather audit evidence and track compliance status continuously. |
| Indicator Template | Allows for the creation of multiple indicators for similar controls or risks. One indicator template can be associated with many specific indicators for a given risk or control. |

### Data Sources for Indicators

Indicator data is sourced from two sources: metrics generated natively within ServiceNow and data imported from external integrations. Before configuring indicators, identify which data source applies.

| **Data Source** | **Integration Requirement** |
| --- | --- |
| Native ServiceNow metrics | No additional integration required. Examples include control states, risk scores, and assessment completion rates. |
| External integrations | Requires a configured data source or Integration Hub spoke. Examples include AI gateway logs, external monitoring tools, and CMDB CI health signals. |

### Example: Continuous Compliance Monitoring

The following example illustrates how indicators function in practice. If an indicator is configured for a control linked to the NIST AI Risk Management Framework, it will automatically run at an established interval and analyze data to determine whether the control remains in compliance.

If the control falls out of compliance, it is automatically set to a Non-Compliant state and surfaces within the Risk and Compliance Compliance by Authority Documents and Policies section of the workspace. This is immediately visible to the AI Steward, who can monitor the latest developments for control and ensure corrective action is on track

> [!tip] Tip
> Indicator templates are the most efficient way to monitor similar controls across multiple AI assets. Define a single template and generate asset-specific indicators from it to reduce configuration overhead.

# General - Prelaunch

## How to Use This Checklist

This checklist is divided into two deployment levels. Begin with foundational items to establish a functioning AICT deployment with core governance capabilities. After that, progress to Full Functionality items according to your organization's governance maturity and priorities.

| **Foundational** | **Full Functionality** |
| --- | --- |
| Minimum steps to get AICT operational with core governance capabilities. | Complete AICT capability set, built on a working Foundational deployment. |
| • Stakeholder identification | • Full stakeholder alignment |
| • Plugin activation | • Governance framework configuration |
| • Core role provisioning | • Hyperscaler discovery |
| • Inventory intake configuration | • AI case management |
| • Out-of-the-box lifecycle validation | • Value and adoption tracking |

> [!tip] Tip
> Roles should be assigned to user groups, not individual users. This simplifies ongoing access management and ensures consistent permissions across your AICT deployment.

Foundational Level Deployment Complete these steps first. It is a must-have to bring AICT operational with core governance and inventory capabilities.

## Stakeholder Identification

Identify the core personas required for initial AICT deployment before activating any plugins or provisioning roles. Refer to the Personas, Roles, and Responsibilities section of the AICT Implementation Guide for detailed role definitions.

| **✓ Core Stakeholders** |
| --- |
| ☐ Identify the AI Steward (or equivalent) who will own AICT governance and oversight |
| ☐ Identify AI Product Owners responsible for managing AI asset lifecycles |
| ☐ Identify the AI Risk and Compliance Manager (or equivalent) for risk assessments and compliance activities |
| ☐ Confirm executive sponsor for the AI governance program (e.g., CIO, CAIO, CRO) |

## Initial Inventory Scope

Define the initial boundaries for the AI asset inventory before populating records. A scoped initial deployment reduces complexity and can be expanded during the Full Functionality phase.

| **✓ Inventory Scope** |
| --- |
| ☐ Define what qualifies as an AI asset for the initial deployment (e.g., start with AI systems and models; expand to datasets and prompts in a later phase) |
| ☐ Identify the initial set of AI assets to populate in the inventory |
| ☐ Determine the primary intake method for initial population: manual intake via workspace, Record Producers, AI Discovery connectors, or automated Now Assist sync |
| ☐ Confirm whether Now Assist auto-discovery should be active (enabled by default; runs hourly) |

## Plugin Activation

| **✓** | **Plugin Name** | **Plugin ID** | **Required?** |
| --- | --- | --- | --- |
| ☐ | AI Control Tower | sn_aict | AICT enterprise SKU |
| ☐ | AI Control Tower | sn_aict_foundation | AI Native SKU for Enterprise AI |

## Core Role Provisioning

Create user groups and assign out-of-the-box roles for core personas. Roles must be assigned to groups, not individual users.

| **✓ Core Roles** |
| --- |
| ☐ Create a user group for AI Stewards and assign the AI Steward role [sn_ai_governance.ai_steward] |
| ☐ Assign the AI Control Tower Workspace User role [sn_ai_governance.workspace_user] to the AI Stewards group |
| ☐ Create a user group for AI Product Owners and assign the AI Asset Owner role [sn_ai_asset_mgmt.ai_asset_owner] |
| ☐ Create a user group for AI Risk and Compliance and assign the AI Risk and Compliance Manager role [sn_grc_ai_gov.ai_risk_and_compliance_manager] |
| ☐ Assign the AI Risk and Compliance Admin role [sn_grc_ai_gov.ai_risk_and_compliance_admin] to platform administrators responsible for AICT configuration |
| ☐ Verify that each persona can access their respective workspace |

## Workspace Verification

Verify that both workspaces are accessible and displaying correctly for the provisioned roles before populating the inventory.

| **✓ Workspace Verification** |
| --- |
| ☐ Verify AI Control Tower Workspace is accessible at URL path: ai-governance-workspace |
| ☐ Verify AI Risk & Compliance Workspace is accessible for risk and compliance personas |
| ☐ Confirm the Overview tab displays AI system counts, type breakdown, and risk classification |
| ☐ Confirm the AI Asset Inventory tab displays the initial set of AI assets |

## Initial Inventory Population

Populate the AI asset inventory using at least one intake method and verify that records are created correctly in the CMDB.

| **✓ Initial Inventory** |
| --- |
| ☐ If using Now Assist sync: confirm the Sync Now Assist AI Assets scheduled job is active and has run successfully |
| ☐ If using manual intake via workspace: test adding an AI System, AI Model, Dataset, and Prompt from the AI Control Tower Workspace list pages |
| ☐ If using Record Producers: verify that Request an AI Use Case, Request an AI Model, and Request a Dataset are available in the Service Catalog |
| ☐ Verify that submitted assets appear in the AI Asset Inventory tab with correct metadata |
| ☐ Verify that an AI Asset Governance Details record is created for each asset |

## Basic Lifecycle Validation

Test the out-of-the-box AI Asset Lifecycle for AI Systems to confirm that the playbook, flows, and tasks are functioning correctly before expanding to Full Functionality.

| **✓ Lifecycle Validation** |
| --- |
| ☐ Submit an AI Use Case (AI System) via the Employee Center or Workspace |
| ☐ As an AI Steward, navigate to the AI System record and click Start Review to initiate the lifecycle |
| ☐ Verify that the AI System record [sn_grc_ai_gov_ai_system] and Related Entity in IRM are created |
| ☐ Verify that the AI Asset Lifecycle playbook displays with three stages: Assess, Build & Test, Deploy |
| ☐ Verify that out-of-the-box tasks are created in the Assess phase (Impact Assessment, collaboration tasks, architecture review) |
| ☐ Progress through at least the Assess phase to confirm task completion and state transitions |

Foundational Complete If all Foundational checklist items are complete, your AICT deployment is operational with core AI asset inventory, lifecycle management, and workspace access. Proceed to Full Functionality when your organization is ready to expand governance capabilities.

### Full Functionality Deployment

Complete the Foundational checklist first. Then work through these sections based on your organization’s governance maturity and priorities.

### Full Stakeholder Alignment

Expand stakeholder identification beyond core personas to include supporting roles and cross-functional teams. Full stakeholder alignment should be completed before configuring governance frameworks or workflows that depend on cross-team participation.

| **✓ Extended Stakeholders** |
| --- |
| ☐ Identify supporting personas: AI Risk/Compliance Analysts, AI Governance Stakeholders (readers, business users), AI Case Analysts, AI Case Managers |
| ☐ Identify cross-functional stakeholders: Legal, Security, Privacy, Enterprise Architecture, PMO, Data Governance |
| ☐ Confirm all identified stakeholders have been briefed on responsible AI principles and AICT workflows |
| ☐ Provision supporting roles (Analyst, User, Reader, Case roles) to appropriate user groups |

### Pre-Implementation Discovery

Answer the following questions to inform configuration decisions across risk, compliance, inventory, and integration. Discovery answers should be documented and shared with configuration owners before proceeding.

| **✓ General Discovery** |
| --- |
| ☐ Where is AI currently being used across the organization? |
| ☐ Are we leveraging third-party tools or APIs with embedded AI? |
| ☐ Are employees independently using generative AI tools (e.g., ChatGPT, GitHub Copilot)? |
| ☐ Which business functions are actively experimenting with AI? |
| ☐ Do our products or services include embedded AI functionality? |
| ☐ Which stakeholders (IT, Legal, Procurement, Risk, HR, etc.) should be involved in discovery? |
| ☐ Are procurement and vendor risk processes equipped to evaluate AI functionality? |
| ☐ Are business units developing their own AI solutions (shadow AI)? |
| ☐ How will new AI assets be onboarded, validated, and inventoried going forward? |
| ☐ What reporting, dashboards, and search/filter capabilities are needed? |

| **✓ Risk and Compliance Discovery** |
| --- |
| ☐ What are the business or compliance risks associated with our AI usage? |
| ☐ What regulatory frameworks must the inventory align with (e.g., EU AI Act, NIST AI RMF, ISO/IEC 42001)? |
| ☐ Are we subject to AI-specific regulatory mandates? |
| ☐ Do we need differentiated governance for high-, medium-, and low-risk AI? |
| ☐ Do we have defined accountability and ownership for each AI system? |

### Governance Framework Configuration

Configure the risk and compliance components of AICT, including authority documents, risk frameworks, assessment templates, and policies. This section depends on completed Pre-Implementation Discovery.

| **✓ Governance Framework** |
| --- |
| ☐ Install the AI Risk and Compliance Content Accelerator [com.sn_grc_ai_gov_cont] for pre-built EU AI Act and NIST AI RMF content |
| ☐ Configure regulatory agencies (e.g., European Commission, NIST) or add additional agencies |
| ☐ Configure authority documents (EU AI Act, NIST AI RMF, or custom) |
| ☐ Configure citations for applicable authority documents |
| ☐ Map control objectives to authority documents and/or internal policies |
| ☐ Configure risk frameworks and risk statements (use the AI Risk Statement Library or create custom statements) |
| ☐ Configure Risk Assessment Methodologies (RAMs): Risk Classification for AI Systems, Risk Assessment for AI Inventory, Risk Classification for AI Models/Datasets |
| ☐ Configure impact assessment templates (or adopt pre-built templates: High-Risk AI Assessment Questionnaire, EU AI Act Conformity Assessment, FRIA, General AI Impact Assessment) |
| ☐ Publish assessment templates so they can be initiated from workflows |
| ☐ Configure Smart Assessment Engine automations for risk and control mapping based on assessment responses |
| ☐ Configure entity scoping and entity filters for AI systems, models, and datasets in the CMDB |
| ☐ Define and create AI policies with associated control objectives |
| ☐ Configure regulatory intelligence feeds (RSS) if continuous regulatory monitoring is required |

### Expanded Inventory and Discovery

Expand the AI asset inventory beyond the initial population to include external AI platforms, API integrations, and additional data sources. Confirm foundational inventory is stable before expanding scope.

| **✓ Expanded Inventory** |
| --- |
| ☐ Establish guardrails for in-scope vs. out-of-scope assets (e.g., excluded vendor tools, prohibited AI systems, in- production systems that must be governed) |
| ☐ Identify integration points with existing systems: CRM, ITSM, HRIS, SAM tools, vendor/procurement management |
| ☐ Configure hyperscaler discovery connections (Amazon Bedrock, Azure AI Foundry, Copilot Studio, GCP Vertex AI) |
| ☐ Test hyperscaler discovery connections and verify assets are populated in the CMDB |
| ☐ Activate the Asset Classes plugin [sn_ent] if using the AI Assets API for programmatic integration |
| ☐ Configure custom Scripted REST API endpoints for advanced integration needs |
| ☐ If using data imports from external sources (JDBC, OIDC, LDAP, REST, file), configure data sources, import set tables, and transform maps |
| ☐ Define and configure scheduled imports if applicable |
| ☐ Validate that all discovered and imported assets appear correctly in the inventory with proper metadata and relationships |

### Lifecycle and Playbook Customization

Customize the AI Asset Lifecycle playbook beyond the out-of-the-box AI System configuration. Only AI Systems include preconfigured tasks out of the box; other asset types require manual task creation or flow cloning.

| **✓ Lifecycle Customization** |
| --- |
| ☐ Review and confirm lifecycle phase names (Assess, Build & Test, Deploy); if renaming is required, update the AI Asset Lifecycle table, list view, and metadata files in sys_ux_list |
| ☐ Determine whether custom lifecycle tasks are needed for AI Models, Datasets, or Prompts |
| ☐ If custom tasks are needed, clone existing AI System flows and adjust trigger conditions; reuse subflows where possible |
| ☐ Review out-of-the-box flows for the Assess phase (Impact Assessment, collaboration tasks, architecture review, risk assessment generation) |
| ☐ Review out-of-the-box flows for the Build & Test phase (Control Attestation, deployment region collection, deployment details sharing) |
| ☐ Review out-of-the-box flows for the Deploy phase (Review Issues/Policy Exceptions, Conformity Assessment, Deploy Asset Task) |
| ☐ Do not deactivate any out-of-the-box tasks; clone for customization instead |
| ☐ Test the full lifecycle end-to-end for AI Systems: intake → Start Review → Assess → Build & Test → Deploy |
| ☐ If customized, test the lifecycle for each additional asset type (AI Models, Datasets, Prompts) |

### Case Management Configuration

Configure the AI Case Management module for handling AI-related cases and inquiries. Configuration of case types and SLA definitions should align with your organization’s risk and compliance governance framework.

| **✓ Case Management** |
| --- |
| ☐ Define and configure AI case types and sub-types (e.g., Model Performance, Data Issues, Compliance & Regulatory, Ethical Concerns, Operational Incidents) |
| ☐ Define and configure inquiry types (e.g., Regulatory Requests, Internal Audits, Ethical Concerns) |
| ☐ Configure state models and state transitions for cases and inquiries |
| ☐ Configure assessment templates for case investigations (or use the pre-built AI Case Assessment Questionnaire) |
| ☐ Publish case assessment templates |
| ☐ Define causes and consequences for root cause analysis |
| ☐ Configure document templates for regulatory and audit reporting |
| ☐ Define SLA definitions for case response and resolution times by priority level |
| ☐ Configure Employee Center Portal record producers for case and inquiry submission |
| ☐ Verify that the AI Case Business User role provides access to submit cases and inquiries via Employee Center |

### AI Strategy Configuration (SPM)

If using Strategic Portfolio Management for AI strategy, intake, and execution, complete the following steps. The Goals Framework is included out-of-the-box for all AICT customers. The Strategic Planning plugin requires an SPM Pro license.

| **✓ AI Strategy (SPM)** |
| --- |
| ☐ Verify the Goals Framework is active (included out-of-the-box for all AICT customers) |
| ☐ Test creating a Strategic Priority, Goal, and Target from the AICT List section |
| ☐ If SPM Pro is licensed: activate the Strategic Planning plugin |
| ☐ Test creating a Demand with Investment Type set to Artificial Intelligence |
| ☐ Verify that Demands can be converted into Projects and Epics |
| ☐ Verify that the Strategic Planning Workspace displays AI-related work with capacity planning, financial analysis, and scenario planning |
| ☐ Verify that the AI Strategy tab in the AICT Workspace displays strategies, goals, targets, costs, and prioritized work |

### Value and Adoption Configuration

Configure the Value and Adoption dashboards to track AI impact and usage metrics. The daily value calculation job must be active and the historical backfill script must have run before meaningful data will display.

| **✓ Value and Adoption** |
| --- |
| ☐ Verify the daily value calculation scheduled job is active (runs daily, 1–3pm) |
| ☐ Confirm the historical data backfill script has run on installation (populates past 30 days) |
| ☐ Review and configure value templates for each AI system (defaults: 15 min time saved per invocation, 50% acceptance rate for third-party agents) |
| ☐ Configure custom value metrics if the organization requires goals beyond the four out-of-the-box categories (ROI, Productivity, Cost Avoidance, Risk Reduction) |
| ☐ If using multi-instance deployment, configure the Multi-Instance Framework (MIF) for centralized value rollup |
| ☐ Verify the Value tab displays total productivity gained, average AI users, and top AI systems by value |
| ☐ Verify the Adoption tab displays usage data (daily AI actions, daily unique users, department-level usage) |

### Workspace Customization

Customize workspace layouts and dashboards beyond the default configuration to meet organizational needs. Complete role provisioning and inventory population before customizing workspace views.

| **✓ Workspace Customization** |
| --- |
| ☐ Configure homepage widgets on the AI Control Tower Workspace (risk heatmaps, compliance overview, case summaries) |
| ☐ Configure homepage widgets on the AI Risk & Compliance Workspace |
| ☐ Configure list view filters for each workspace tab |
| ☐ Configure role-based dashboard views as needed |
| ☐ Verify the Security & Privacy tab displays AI Security Score, access metrics, and AI-generated insights |

### Access Control Refinement

Refine access control configuration beyond initial role provisioning to enforce least-privilege access and protect sensitive governance data.

| **✓ Access Control** |
| --- |
| ☐ Verify all ACLs follow the principle of least privilege |
| ☐ Use field-level ACLs for sensitive data; use table-level ACLs for general control |
| ☐ Document any custom ACLs with purpose, roles, and conditions |
| ☐ Test access for each persona type to confirm appropriate visibility and restrictions |
| ☐ Avoid duplicating ACLs for the same operation |
| ☐ Enforce data protection with server-side ACLs; do not rely on client-side scripts or policies |

### Pre-Go-Live Validation

Complete the following validation steps before making AICT fully available to all users. All previous checklist sections should be complete before beginning pre-go-live validation.

| **✓ Pre-Go-Live Validation** |
| --- |
| ☐ Test AI asset intake via each configured method (Record Producer, Workspace, API, automated discovery, hyperscaler connections) |
| ☐ Test the full AI System lifecycle end-to-end: intake → Start Review → Assess → Build & Test → Deploy |
| ☐ Verify that impact assessments, risk assessments, and control attestations complete successfully |
| ☐ Verify that AI cases and inquiries can be submitted from Employee Center and routed to analysts |
| ☐ Verify workspace access for each persona type (AI Steward, Product Owner, Risk/Compliance Manager, Analyst, Reader) |
| ☐ Verify that the AI Strategy tab displays strategic priorities, goals, and targets correctly |
| ☐ Verify that the Value and Adoption tabs display metric data |
| ☐ Verify that the Security & Privacy tab displays AI Security Score and access metrics |
| ☐ Confirm all regulatory content (authority documents, citations, control objectives) is loaded and mapped |
| ☐ Confirm all custom ACLs are documented and tested |
| ☐ Conduct user acceptance testing (UAT) with representatives from each persona group |
| ☐ Document any known issues, workarounds, or deferred configuration items |

Full Functionality Complete: When all pre-go-live validation items pass, AICT is ready for full production deployment. Document any deferred items as post-go-live backlog and assign owners before go-live.

# Discover - Data Models

## Overview

The AI Asset Inventory serves as the authoritative catalog of all AI-related components deployed within an organization. It captures AI systems, models, datasets, prompts, MCP servers, inputs/outputs, and their interdependencies to support enterprise AI governance.

This document provides:
- A structured approach to AI asset intake and representation
- Technical considerations to enable scalable implementation
- Governance-aligned best practices for AI Control Tower deployments

The inventory is foundational to enabling traceability, risk management, and lifecycle governance across AI initiatives.

## Audience

This document is intended for the following stakeholders responsible for implementing and governing AI within ServiceNow AI Control Tower and AI Risk and Compliance:
- Administrators, Architects, Developers – configuring and deploying AICT modules
- Implementation Partners – supporting customer rollouts and integrations
- AI Product Owners – ensuring asset accuracy and lifecycle completeness
- AI Stewards / AI CoE – driving governance adoption and operational alignment
- AI Risk & Compliance Teams – managing regulatory, risk, and audit requirements

## User Roles and Responsibilities

| **Persona** | **Role** | **Responsibility** |
| --- | --- | --- |
| AI Product / Asset Owners | AI Asset Owner `[sn_ai_asset_mgmt.ai_asset_owner]` | Maintain accurate, up-to-date AI asset records across lifecycle stages |
| AI Stewards / AI CoE | AI Steward `[sn_ai_governance.ai_steward]` | Enforce governance standards and ensure alignment with AICT policies |
| AI Risk & Compliance Managers | AI Risk & Compliance Manager `[sn_grc_ai_gov.ai_risk_and_compliance_manager]` | Oversee risk identification, compliance mapping, and governance controls |

## AI Asset Inventory Structure

The AI Asset Inventory catalogs all components required to deliver AI-enabled functionality. Organizations may govern one or more of the following asset types.

### Core AI Asset Types

- AI Systems
- AI Models
- AI Datasets
- MCP Servers
- AI Prompts

### Supporting Data Structures

- Inputs / Outputs – Defines how AI systems interact with data
- AI Tools – Capabilities enabling agentic execution (linked to systems, not standalone assets)
- Model Lineage – Tracks model evolution, training datasets, and evaluation history

## AI Asset Definitions

### AI Systems

AI systems are engineered or machine-based solutions that perform tasks such as decision-making, prediction, content generation, or analysis.

Key characteristics:
- Operate with varying levels of autonomy
- May learn and adapt over time
- Can be composed of multiple interconnected subsystems

Hierarchical Systems- AI systems may depend on other systems (sub-systems). Capturing these relationships enables:
- Accountability tracking
- Dependency mapping
- Risk propagation analysis

> [!note] Note
> AI Control Tower tracks system relationships to support auditability and risk assessments.

### AI Models

AI models are the computational engines powering AI systems. They are trained on datasets to perform specific tasks such as classification, prediction, or generation.

Common training approaches:
- Supervised learning
- Unsupervised learning
- Reinforcement learning

Governance Value- Tracking models enables monitoring of:
- Accuracy and performance
- Bias and fairness
- Model-specific risk exposure

### AI Datasets

Datasets are collections of structured or unstructured data used to train, test, or evaluate AI models.

They may include:
- Tabular data
- Images, audio, or video
- Text corpora

Governance Value- Mapping datasets ensures visibility into:
- Data provenance
- Ownership and stewardship
- Regulatory and privacy implications

### MCP Servers (Model Context Protocol)

MCP servers act as standardized connectors between AI systems and external tools, data sources, or services.

They enable:
- Secure data access
- Tool invocation
- Cross-platform interoperability

Governance Value- Tracking MCP servers provides insight into:
- External system dependencies
- Data access pathways
- Security and privacy risks

### AI Prompts

Prompts are structured inputs or instructions provided to AI systems to generate outputs.

They are particularly critical in generative AI use cases.

Governance Value- Tracking prompts enables:
- Understanding user interaction patterns
- Monitoring output quality and appropriateness
- Identifying misuse or risk scenarios

### Inputs and Outputs

Inputs represent the data provided to an AI system, while outputs represent the resulting actions or responses.

Examples include:
- Inputs: text, images, sensor data
- Outputs: summaries, predictions, decisions, recommendations

Governance Value- Defining inputs and outputs supports:
- Behavioral transparency
- Decision traceability
- Risk and impact analysis

## AI Tools (Agentic Context)

AI tools are capabilities that enable AI systems—particularly agentic systems—to perform actions.
- Tools are attributes of AI systems, not standalone governed assets
- They are discovered through integrations (e.g., AWS, Azure)
- They do not have independent lifecycle governance within AICT

## Understanding Interdependencies

AI governance requires explicit mapping of relationships between:
- AI System (business function)
- AI Model (decision logic)
- Dataset (training and evaluation source)

Failure to capture these relationships can lead to:
- Incomplete risk assessments
- Gaps in audit readiness
- Weak compliance alignment

### Best Practice

For each AI capability:
1. Inventory the AI system
2. Identify associated models
3. Document datasets used for training and evaluation

This structured mapping ensures end-to-end traceability and governance coverage.

## Implementation Considerations

- Establish standardized intake processes for all AI assets
- Enforce role-based ownership across lifecycle stages
- Integrate discovery sources (e.g., AWS, Azure) for automated population
- Maintain lineage tracking for models and datasets
- Align inventory data with AI Risk & Compliance frameworks (e.g., EU AI Act, NIST AI RMF)

> **[Figure 2 — p.44]** Dark-themed hierarchy diagram of a loan-approval AI System, branching to two AI Models (ServiceNow Now LLM, Open AI GPT 5.0) and an MCP Server (Credit Bureau / Fico scores), each Model in turn linked to three Datasets: Financial Info, Public Records and Financial Behavior.

## Examples of AI Asset Inventory by Industry, Use Case, and AI Type

Understanding how AI assets manifest across industries is critical to properly configuring the AI Asset Inventory. The following examples illustrate how AI Systems, Models, Datasets, Prompts, Inputs, and Outputs are represented across different domains and AI types.

### Financial Services – Loan Decisioning

Scenario: A retail bank uses AI to automate home loan approvals.

| **Category** | **Example** |
| --- | --- |
| Business Application | Loan Origination System |
| AI Type | Traditional AI |
| AI System | Risk Classification |
| AI Model | Credit Scoring Model |
| Dataset | Customer credit history, income, employment, repayment behavior |
| Input | Credit score, income documentation, employment details |
| Prompt | Not applicable (non-GenAI use case) |
| Output | Risk classification (e.g., Medium Risk), Loan approval/denial |

### Technology – Incident Management Automation

Scenario: A technology provider uses Generative AI to summarize IT incidents and assign ownership.

| **Category** | **Example** |
| --- | --- |
| Business Application | Now Assist for ITSM |
| AI Type | Generative AI |
| AI System | Incident Summarization |
| AI Model | LLM (e.g., Mixtral, GPT-4 via Azure OpenAI) |
| Dataset | Ticket data (title, description, activity, resolution notes) |
| Input | Ticket ID, description, category, assignment history |
| Prompt | “Summarize this incident in under 250 words” |
| Output | Incident summary |

### Manufacturing – Predictive Maintenance

Scenario: A manufacturing organization predicts equipment failure using AI.

| **Category** | **Example** |
| --- | --- |
| Business Application | Asset Management |
| AI Type | Traditional AI |
| AI System | Predictive Maintenance Engine |
| AI Model | Time-series forecasting model |
| Dataset | Sensor logs, maintenance records, machine usage |
| Input | Machine telemetry data |
| Prompt | Not applicable |
| Output | Predictive alert (e.g., failure within 48 hours) |

### Agentic AI – Customer Support Automation

Scenario: A virtual agent autonomously handles customer inquiries end-to-end.

| **Component** | **Example** |
| --- | --- |
| Business Application | AI-powered Customer Support Agent |
| AI Type | Agentic AI |
| AI System | Customer Support Agent |
| Sub-Systems | Issue Summarization, Owner Assignment, Knowledge Retrieval |
| AI Models | LLM (summarization), classification model (urgency), retrieval model (KB lookup), dialogue model |
| Dataset | Historical tickets, chat logs, escalation cases, knowledge base |
| Input | Customer query, account metadata |
| Prompt | Instruction to resolve queries, summarize issues, retrieve KB content |
| Output | Issue summary, automated response, escalation when required |

> [!important] Important
> Agentic AI introduces multi-system orchestration and multi-model dependencies, requiring more granular tracking of relationships and execution flows within AICT.

### Healthcare & Life Sciences – Patient Intake Triage

Scenario: A hospital uses GenAI to summarize patient symptoms and determine urgency.

| **Category** | **Example** |
| --- | --- |
| Business Application | Electronic Health Record (EHR) |
| AI Type | Generative AI |
| AI System | Symptom Summarization |
| AI Model | Medical LLM (fine-tuned) |
| Dataset | Patient intake notes, diagnosis history |
| Input | Patient symptoms, prior records, demographics |
| Prompt | “Summarize symptoms and recommend triage category” |
| Output | Clinical summary and urgency classification |

## Why Organizations Require an AI Asset Inventory

As AI adoption scales, organizations require a centralized mechanism to govern AI usage across business functions.

AI Asset Inventory enables:
- Centralized tracking of AI systems and use cases
- Visibility into models, datasets, and decision logic
- Alignment with governance, risk, and compliance frameworks

It supports:
- AI Product Owners in lifecycle management
- AI Stewards / CoE in governance enforcement
- Risk & Compliance teams in identifying and mitigating risk

Outcome: A single source of truth for AI, enabling transparency, accountability, and regulatory readiness.

## Ownership and Responsibility for AI Asset Inventory

Responsibility for maintaining the AI Asset Inventory typically resides with:
- AI Stewards / AI CoE (governance oversight)
- AI Asset Owners (data accuracy and lifecycle updates)

### Operational Reality

AI asset data is often:
- Distributed across multiple tools and platforms
- Siloed across teams (IT, Data Science, Risk, Legal)
- Stored in informal repositories (spreadsheets, email, shared drives)

This fragmentation results in:
- Incomplete or outdated asset records
- Manual and time-intensive discovery processes
- Increased risk of governance gaps and audit failure

## Determining the Scope of AI Asset Inventory

A structured, governance-driven approach is required to define scope.

### 1. Define AI Assets

Establish clear criteria based on:
- AI technology type (ML, NLP, GenAI, Agentic AI)
- Organizational standards
- Regulatory requirements

### 2. Classify AI Use Cases as AI Systems

Each use case should be mapped to an AI System based on:
- Business purpose
- Criticality and impact
- Regulatory exposure

### 3. Establish Inventory Scope

Define:
- Asset types to be tracked
- Source systems and platforms
- Lifecycle coverage (intake → build → deploy → retire)

### 4. Integrate with Enterprise Systems

Ensure alignment with:
- CRM, ITSM, HR systems
- Vendor and procurement systems
- Software asset management tools

## Pre-Implementation Discovery Questions

### General Discovery

- Where is AI currently deployed?
- Are third-party AI tools in use?
- Are employees using unsanctioned GenAI tools?
- Which business units are developing AI solutions?
- How are AI assets onboarded and validated?

### Risk and Compliance Discovery

- What risks are associated with AI usage?
- Which regulatory frameworks must be supported?
- Are AI systems categorized by risk level?
- Is ownership clearly defined for each system?

## Discovery and Population of AI Assets

AI Asset Inventory can be populated using multiple methods. A hybrid approach is recommended.

### Auto Discovery – ServiceNow Assets

- Scheduled job: Sync Now Assist AI Assets
- Runs periodically (hourly)
- Discovers:
- AI models
- Datasets
- Prompts
- Agentic AI assets
- Covers both out-of-box and custom AI skills

### API-Based Integration

Used for large-scale environments requiring automation.

Capabilities:
- Create, update, and retrieve AI asset records
- Integrate with external systems
- Maintain real-time inventory accuracy

Requirements:
- Appropriate roles (asset, model_manager)
- Asset Classes plugin enabled

### Manual Intake of AI Asset Inventory

Recommended when:
- Discovery mechanisms are incomplete
- Governance maturity requires controlled onboarding
- External or custom AI solutions exist

### ServiceNow Capabilities Supporting Manual Intake

#### Record Producers

- Provides simplified data entry for AI asset creation
- Accessible via Employee Center
- Automatically creates backend records and relationships

Usage Context:
- AI Asset Owners submit:
- AI Systems
- AI Models
- Datasets

#### Workspace (AI Control Tower)

- Provides a centralized operational interface
- Built using Next Experience UI
- Enables efficient asset management and governance workflows

### Example Intake Workflow

- Role: AI Asset Owner
- Navigate: Employee Center → Technology Services → AI Assets
- Submit request for:
- AI System
- AI Model
- Dataset

> **[Figure 3 — p.51]** Employee Center 'AI assets' catalogue page (Home > Technology services > AI assets) showing five record producer tiles: Request an AI use case, Raise an AI inquiry, Report an AI case, Request a dataset and Request an AI model, with Filter by / Sort by controls.

- *Figure 2: AICT Risk and Compliance Record Producers*

## Manual Intake Configuration – Record Producers and Workspace

To support controlled onboarding of AI assets, AI Control Tower provides Record Producers (Service Catalog) and Workspace- based intake mechanisms. These capabilities enable structured ingestion of AI Systems, Models, Datasets, and Prompts into the AI Asset Inventory.

## Record Producers for AI Asset Intake

Record Producers facilitate standardized intake of AI assets via the Service Catalog (Governance, Risk, and Compliance category).

### Available Record Producers

| **Name** | **Table** | **Intake Channel** |
| --- | --- | --- |
| Request an AI Use Case | AI System Digital Asset `[alm_ai_system_digital_asset]` | Service Catalog |
| Request an AI Model | AI Model Digital Asset `[alm_ai_model_digital_asset]` | Service Catalog |
| Request a Dataset | AI Dataset Digital Asset `[alm_ai_dataset_digital_asset]` | Service Catalog |
| Add an AI System | AI System Digital Asset `[alm_ai_system_digital_asset]` | AI Control Tower Workspace |
| Add an AI Model | AI Model Digital Asset `[alm_ai_model_digital_asset]` | AI Control Tower Workspace |
| Add a Dataset | AI Dataset Digital Asset `[alm_ai_dataset_digital_asset]` | AI Control Tower Workspace |
| Add a Prompt | AI Prompt `[alm_ai_prompt_digital_asset]` | AI Control Tower Workspace |

### Access and Role Requirements

All record producers are available to users with AI Request User access, which includes:
- Role: `sn_grc_ai_gov.ai_risk_and_compliance_business_user`
- Inherited by: `sn_ai_asset_mgmt.ai_asset_owner`

This ensures that AI Asset Owners can manage assets across their lifecycle—from intake through retirement—within governed workflows.

## Record Producer: Request an AI Use Case

This intake form captures AI use case details and creates the foundational AI System Digital Asset.

### Key System Actions

- Creates
- AI System Digital Asset
- `[alm_ai_system_digital_asset]`
- Sets class, state, ownership, and model category
- Stores associated models and datasets
- Creates
- AI System Component Product Model
- `[cmdb_ai_system_component_product_model]`
- Establishes attributes (name, version, provider)
- Defaults asset tracking and lifecycle status
- Links product model to digital asset (1:1 relationship)
- Triggers
- AI System Generation Workflow
- Subflow: `Generate AI System [sn_grc_ai_gov.generate_ai_system]`
- Creates AI System of record `[sn_grc_ai_gov_ai_system]` upon review approval
- Establishes governance lifecycle foundation
- Creates
- AI Asset Governance Details
- Table: `[sn_ai_governance_asset_governance_details]`
- Supports lifecycle stages: Assess → Build → Deploy

> [!note] Note
> AI System record is created only after AI Steward / CoE review initiation

- No Configuration Item (CI) is created during intake

## Record Producer: Request an AI Model

This intake form creates and governs AI models independently of systems.

### Key System Actions

- Creates
- AI Model Digital Asset
- `[alm_ai_model_digital_asset]`
- Defaults category to AI Model
- Captures datasets (training and evaluation)
- Creates
- AI Model Product Model
- `[cmdb_ai_model_product_model]`
- Establishes model attributes and lifecycle state
- Links product model to digital asset (many-to-one relationship)
- Creates
- AI Asset Governance Details
- Enables lifecycle tracking within AICT

> [!note] Note
> No Configuration Item (CI) is created during intake

## Record Producer: Request a Dataset

This intake form captures datasets used in training and evaluation.

### Key System Actions

- Creates
- AI Dataset Digital Asset
- `[alm_ai_dataset_digital_asset]`
- Defaults category to AI Dataset
- Captures dataset relationships
- Creates
- AI Dataset Product Model
- `[cmdb_ai_dataset_product_model]`
- Establishes dataset attributes and lifecycle state
- Links product model to digital asset
- Creates
- AI Asset Governance Details
- Enables lifecycle governance and traceability

> [!note] Note
> No Configuration Item (CI) is created during intake

## Option II: Workspace-Based Intake

AI Control Tower Workspace provides a direct, role-based interface for asset creation and management.

### Roles Required

- AI Asset Owner `[sn_ai_asset_mgmt.ai_asset_owner]`
- AI Steward / AI CoE `[sn_ai_governance.ai_steward]`

### Capabilities

- Add and manage:
- AI Systems
- AI Models
- AI Datasets
- AI Prompts
- Navigate via:
- AI Control Tower Workspace → List Pages
- “Add AI System / Model / Dataset” actions
- Prompt Creation Constraint
- Prompts can only be added via Workspace (not Service Catalog)

### Operational Flow

1. User navigates to AI Control Tower Workspace
2. Selects asset type (e.g., AI System)
3. Initiates “Add” action
4. Completes structured form
5. Asset is created and enters governance lifecycle

> **[Figure 4 — p.55]** AI Control Tower workspace list view 'AI asset inventory - Managed - AI systems' with columns for Display name, Provider, Vendor, Managed by, Lifecycle phase, State, Lifecycle status and Risk classification, plus the 'Add AI system' button and the left-hand inventory tree (AI systems, AI models, Prompts, Datasets, MCP servers, Lifecycle, Requests, Cases, Inquiries, AI strategies and goals, AI Task).

- *Figure 3: Add assets in AI asset inventory from AICT workspace*

AI Control Tower leverages the Now Experience Framework (UI Builder) to deliver a modern, role-based workspace for managing AI Asset Inventory. This section outlines the core UI Builder configurations that enable asset intake and management from the workspace perspective.

## UI Builder Experience Configuration

The AI Control Tower Workspace is configured as a UI Builder experience with the following attributes:

| **Attribute** | **Configuration** |
| --- | --- |
| Workspace | AI Control Tower |
| Application Scope | AI Control Tower Core |
| App Shell | Workspace App Shell |
| Experience Name | AI Control Tower |
| URL Path | `ai-governance-workspace` |
| Role Required | `sn_ai_governance.workspace_user` |

## UI Builder Page Configuration

The intake experience is driven by a reusable UI Builder page.

| **Attribute** | **Configuration** |
| --- | --- |
| Page Name | Intake-form |
| Variant | Default |
| Application Scope | AI Asset Management |
| URL Path | `/intake-form/{table}/{sys_id}` |

## Page Parameters and Dynamic Behavior

The Intake-form page is parameterized to dynamically render forms based on the AI asset type being created.
- Parameters:
- `table` → Defines the asset type
- `sys_id` → Set to `-1` for new records

### Asset-Specific Parameter Mapping

| **Action** | **Parameter Value (table)** | **Purpose** |
| --- | --- | --- |
| Add AI System | `alm_ai_system_digital_asset` | Captures AI System (use case) details |
| Add AI Model | `alm_ai_model_digital_asset` | Captures AI Model details |
| Add Dataset | `alm_ai_dataset_digital_asset` | Captures dataset details |
| Add Prompt | `alm_ai_prompt_digital_asset` | Captures prompt details |

> [!tip] Tip
> A single configurable page supports multiple asset types through parameter-driven rendering, ensuring scalability and maintainability.

## Intake Form Architecture

The Intake-form is composed of three primary Form components, orchestrated through a stepper-based experience.

###Form Components

#### Form 1: Model Form

Captures information required to create Product Models:
- AI System Component Product Model
- `[cmdb_ai_system_component_product_model]`
- AI Model Product Model
- `[cmdb_ai_model_product_model]`
- AI Dataset Product Model
- `[cmdb_ai_dataset_product_model]`
- AI Prompt Product Model
- `[cmdb_ai_prompt_product_model]`

#### Form 2: Asset Form

Captures information required to create Digital Assets:
- AI System Digital Asset
- `[alm_ai_system_digital_asset]`
- AI Model Digital Asset
- `[alm_ai_model_digital_asset]`
- AI Dataset Digital Asset
- `[alm_ai_dataset_digital_asset]`
- AI Prompt Digital Asset
- `[alm_ai_prompt_digital_asset]`

#### Form 3: Related Assets Form

Captures relationships between AI assets:
- AI Systems → associated Models and Datasets
- AI Models → associated Datasets
- Datasets → base datasets
- AI Systems of record → associated Models, Datasets, and Prompts

## Stepper-Based User Experience

The intake experience is structured into steps:
- Details Step
- Combines Model Form and Asset Form
- Related Assets Step
- Captures relationships via Related Assets Form

This approach ensures:
- Logical separation of concerns
- Improved usability and data quality
- Progressive data capture aligned to governance needs

## Form Controller and Dynamic Rendering

- The Form Controller dynamically determines:
- Target table
- Form layout
- View configuration
- Form components are driven by:
- Table parameter ( `table` )
- Configured views (e.g., *Intake view*)
- Client-side scripts

## Client Script Behavior

Client scripts play a critical role in:
- Dynamically setting the model table
- Controlling form behavior based on asset type
- Managing stepper progression
- Updating client state parameters

> [!note] Note
> The model table assignment logic is central to switching between AI System, Model, Dataset, and Prompt intake experiences.

## Configuration Recommendations

### Form Customization

- Modify the “Intake” view to add new attributes
- Avoid removing out-of-box (OOTB) fields, as they represent minimum governance requirements

### State Management

- Use Draft for new (undeployed) AI assets
- Use Deployed for existing assets being onboarded

### Stepper Configuration

- Controlled via client state parameters
- Validate dependencies with client scripts before making changes

### Governance Alignment

- Ensure required fields align with:
- AI Risk & Compliance requirements
- Regulatory frameworks (EU AI Act, NIST AI RMF)
- Maintain consistency across:
- Product Model
- Digital Asset
- AI System of record

### Implementation Considerations – AI Asset Inventory (AICT)

##### 1. Governance and Operating Model

- Establish a clear ownership model:
- AI Asset Owner → lifecycle accuracy
- AI Steward / CoE → governance enforcement
- Risk & Compliance → oversight and controls
- Define RACI across lifecycle stages (Intake → Review → Build → Deploy → Monitor → Retire)
- Implement approval gates (e.g., Steward review before AI System activation)
- Align governance with regulatory frameworks (EU AI Act, NIST AI RMF, ISO 42001)
- Classify AI systems by risk tier (low / medium / high) and apply differentiated controls

### 2. Inventory Scope and Strategy

- Define what qualifies as an AI Asset (ML, GenAI, Agentic, embedded AI)
- Standardize classification of AI use cases as AI Systems
- Determine scope across:
- Business applications
- Third-party tools
- Shadow/unsanctioned AI usage
- Continuously refine scope as AI adoption evolves
- Ensure inclusion of agentic architectures and multi-model systems

### 3. Data Model and Asset Relationships

- Enforce structured mapping between:
- AI System → AI Model → Dataset
- Maintain explicit relationship tracking:
- System ↔ Models
- Models ↔ Datasets
- Systems ↔ Prompts
- Enable model lineage tracking (training, evaluation datasets, versions)
- Maintain separation between:
- Digital Assets (inventory layer)
- AI System of Record (governance layer)
- Align with CMDB product model architecture for consistency

### 4. Intake and Onboarding Strategy

- Use a hybrid intake model:
- Record Producers → structured, auditable intake
- Workspace → operational efficiency
- APIs → large-scale automation
- Standardize intake forms with minimum required governance attributes
- Ensure mandatory metadata capture:
- Ownership
- Business purpose
- Risk classification
- Data sources
- Default lifecycle states appropriately:
- Draft → new assets
- Deployed → existing assets
- Prevent bypass of intake via governed entry points only

### 5. Discovery and Integration

- Combine:
- Auto-discovery (Now Assist, AI Agents)
- Service Graph Connectors (external platforms)
- Manual intake (gap coverage)
- Integrate with enterprise systems:
- ITSM, CRM, HR, Vendor Management
- Ensure discovery captures:
- Metadata
- Relationships
- Dependencies
- Account for third-party AI and embedded AI capabilities

### 6. UI Builder and Workspace Configuration

- Maintain single intake experience using parameter-driven UI ( `table` parameter)
- Use Intake view for all form customizations
- Avoid removing OOTB fields (minimum governance baseline)
- Validate all UI changes against:
- Lifecycle workflows
- Data model dependencies
- Carefully manage:
- Client scripts (model table logic)
- Stepper behavior (client state parameters)
- Restrict prompt creation to Workspace (not Service Catalog)

### 7. Lifecycle and Governance Enforcement

- Align all assets to lifecycle stages:
- Assess → Build → Test → Deploy → Monitor → Retire
- Ensure AI Asset Governance Details are automatically created
- Link assets to:
- Risk assessments
- Compliance controls
- AI cases and inquiries
- Enforce state transitions through governance workflows
- Ensure readiness for:
- Audit
- Risk reviews
- Regulatory reporting

### 8. Data Quality and Standardization

- Enforce consistent:
- Naming conventions
- Versioning standards
- Provider attribution
- Standardize model categories and asset classifications
- Implement validation rules to prevent:
- Duplicate assets
- Incomplete records
- Regularly audit inventory for:
- Accuracy
- Completeness
- Redundancy

### 9. Reporting and Observability

- Enable dashboards for:
- AI system inventory
- Risk exposure
- Model usage and performance
- Provide filtering by:
- Business unit
- Risk level
- AI type
- Support export and reporting for:
- Regulatory compliance
- Internal audits
- Ensure traceability from:
- Input → Model → Output → Decision

### 10. Change Management and Adoption

- Establish intake governance policies across business units
- Train users on:
- Asset onboarding processes
- Governance expectations
- Monitor and address:
- Shadow AI usage
- Non-compliant asset creation
- Iterate on processes based on:
- Adoption maturity
- Feedback loops
- Position AICT as the system of record for all AI assets

### 11. Security and Risk Considerations

- Track data access via:
- MCP Servers
- External integrations
- Ensure visibility into:
- Sensitive datasets
- Model outputs impacting decisions
- Apply controls for:
- Bias and fairness
- Data privacy
- Model explainability
- Align with enterprise security and data governance policies

# Discover - Discovery

## Overview

Enterprise AI discovery is a fundamental feature of the AI Control Tower offering a unified and comprehensive view of all AI assets —including AI systems, agents, models, prompts, and tools— across various hyperscalars, AI apps, and Agentic AI frameworks via Service Graph Connectors (SGC).

This process is foundational for effective AI governance, security, compliance, and operational efficiency within large enterprises, where AI is deployed across diverse business units, cloud environments, and platforms.

Enterprise AI Discovery enables organizations to integrate and manage AI assets—such as agents, models, prompts, and tools— from major cloud providers, AI Apps and Frameworks within a single, unified registry. The solution eliminates silos, provides full visibility and control to AI stewards, and supports selective synchronization of assets across environments.

> **[Figure 5 — p.64]** Marketing-style slide 'Enterprise AI is Everywhere—and Evolving', showing fragmented AI asset environments (hyperscalers, embedded SaaS, shadow AI, vendor logos) converging via a green arrow into a single AI Asset Inventory covering Agentic AI, Gen AI and Classical AI.

## Key Capabilities

- Unified Registry: Aggregate AI assets from hyperscalars, AI apps, and Agentic AI frameworks such as AWS Bedrock, Azure AI Foundry, Copilot Studio, Google Cloud Platform (GCP) Vertex AI, ServiceNow agents, Salesforce, Databricks, n8n and more.

> [!note] Note
> Identify Assets and CIs (Configuration Item) using their unique source IDs, such as ARN (Amazon Resource Names) for AWS and Product Models are identified by the associated asset.

- Automatic Discovery: Seamlessly discover and incorporate agents, models, prompts, and tools into the AI Control Tower's AI asset inventory.
- Comprehensive Meta data: Capture detailed information for each asset, including relationships, versions, and operational status.
- Visibility & Control: Eliminates silos by aggregating AI assets from all major platforms, enabling holistic management and oversight, across cloud, on-premises, and hybrid environments. The AI steward has visibility into all the connections and integrations that the admin has set to be able to maintain oversight and get access to active connections. Enabling AI stewards to selectively synchronize assets and environments.

> **[Figure 6 — p.65]** AI Control Tower Configurations > AI connections page listing Integrations and Legacy connections, with schedule name, connection status, source system, run frequency and last-run columns for the configured discovery integrations.

## Managed vs. Unmanaged

The following APIs are available with OOTB capabilities to integrate with the AI Assets Inventory. AI Assets API provides endpoints to retrieve, update, and create several types of AI assets, such as AI systems, AI data sets, prompts, and models.

AI assets in the inventory fall into two categories: managed and unmanaged. By default, assets in AI Control Tower are unmanaged — all assets created via the AI Assets API land as unmanaged. When an asset is marked managed, it gains access to AICT capabilities including governance, lifecycle management, value assessment, risk classification, security, and privacy; reverting to unmanaged removes those capabilities. Only AI stewards can move assets between states. The AI Assets API operates on AI asset records regardless of managed/unmanaged status; the managed flag controls which workflows and assessments run against the record, not API accessibility.

The AI Assets API supports actions that you can perform on AI Asset records in the Expanded Model and Asset Classes application. It requires the Asset Classes (sn_ent) plugin to access it. You must have the asset and model_manager roles to call the endpoints provided by the AI Assets API.

The data included in AI Asset records may be spread across several tables like Product Model, Configuration Item, and others. To reduce complexity when calling this API, however, the AI Assets API inserts data into only the Asset, Product Model and Configuration Item tables. Specifics about table updates are provided under each endpoint.

## AI Service Graph Connectors for AI Control Tower

### Overview

AI Service Graph Connectors enable AI Control Tower to discover AI assets and related usage data from external AI platforms. These connectors help populate the AI inventory with AI systems, agents, models, prompts, tools, subcomponents, and execution or usage data.

Discovered usage data is consumed by the AI Control Tower value dashboard to support visibility into AI activity, adoption, and value realization.

## AI Service Graph Connector for Amazon

### Purpose

The AI Service Graph Connector for Amazon is used to discover AI assets and usage data from AWS services into ServiceNow AI Control Tower. Supported assets may include AI systems, agents, models, tools, prompts, and usage records.

### Required Roles

- `sn_ai_disc.discovery_admin`
- `sn_cmdb_int_util.sgc_admin`

### AWS Prerequisites

Before creating an Amazon AI connection, confirm that your organization has:
- An active AWS account.
- IAM credentials with the required read permissions.
- API access enabled for the AWS services being connected, including Amazon Bedrock, Amazon SageMaker, Amazon CloudWatch, and Amazon Bedrock AgentCore, as applicable.

### Required IAM Permissions

| **AWS Service** | **Required Permissions** |
| --- | --- |
| Amazon Bedrock | `bedrock:List*` , `bedrock:Get*` |
| Amazon SageMaker | `sagemaker:List*` , `sagemaker:Describe*` |
| Amazon CloudWatch | `logs:DescribeLogGroups` , `logs:DescribeLogStreams` , `cloudwatch:GetMetricData` |
| Amazon Bedrock AgentCore | `bedrock:ListAgents` , `bedrock:GetAgent` |

### Supported AWS Services

The Amazon connector supports discovery and usage data from:
- Amazon Bedrock
- Amazon Bedrock AgentCore
- Amazon SageMaker
- Amazon CloudWatch Logs

### Connection Outcome

After the Amazon AI connection is created, AI Control Tower can import AWS AI asset metadata and usage data into the AI inventory and related usage tables.

## AWS APIs Used

### Amazon Bedrock Agents

| **Action Name** | **AWS API** |
| --- | --- |
| `sgawsbedrock_agent` | GetAgent |
| `sgawsbedrock_get_agent` | GetAgent |
| `sgawsbedrock_list_agent` | ListAgents |
| `sgawsbedrock_list_agent_aliases` | ListAgentAliases |
| `sgawsbedrock_list_versions` | ListAgentVersions |
| `sgawsbedrock_get_agent_action_group` | GetAgentActionGroup |
| `sgawsbedrock_list_agent_action_groups` | ListAgentActionGroups |
| `sgawsbedrock_list_agent_collaborators_stream` | ListAgentCollaborators |
| `sgawsbedrock_test_connection` | ListAgents |

### Amazon Bedrock Foundation

| **Action Name** | **AWS API** |
| --- | --- |
| `sgawsbedrock_get_inference_profile` | GetInferenceProfile |
| `sgawsbedrock_get_foundation_model` | GetFoundationModel |

### Amazon Bedrock AgentCore Control

| **Action Name** | **AWS API** |
| --- | --- |
| `look_up_gateways_stream` | ListGateways |
| `look_up_gateway_by_id` | GetGateway |
| `look_up_gateway_targets_stream` | ListGatewayTargets |
| `look_up_gateway_target_by_id` | GetGatewayTarget |
| `look_up_agent_runtimes_stream` | ListAgentRuntimes |
| `look_up_agent_runtime_by_id` | GetAgentRuntime |
| `look_up_code_interpreters_stream` | ListCodeInterpreters |
| `look_up_code_interpreter_by_id` | GetCodeInterpreter |
| `look_up_browsers_stream` | ListBrowsers |
| `look_up_browser_by_id` | GetBrowser |
| `sgaws_agentcore_test_connection` | ListGateways |

### Amazon CloudWatch Logs

| **Action Name** | **AWS API** |
| --- | --- |
| `look_up_cloudwatch_startquery` | StartQuery |
| `sgawscloudwatch_startquery` | StartQuery |
| `sgawscloudwatch_getqueryresults` | GetQueryResults |
| `look_up_cloudwatch_getquery` | GetQueryResults |
| `sgawscloudwatch_test_connection` | StartQuery |
| `sgaws_agentcore_cloudwatch_test_connection` | StartQuery |

### Amazon SageMaker

| **Action Name** | **AWS API** |
| --- | --- |
| `aws_sagemaker_model_discovery` | ListModels |
| `aws_sagemaker_model_card_discovery` | ListModelCards |
| `aws_sagemaker_describe_model_card` | DescribeModelCard |
| `aws_sagemaker_test_connection` | ListModels |

---

## Amazon Data Mapping

| **Data Source** | **Staging Table** | **Target Table** |
| --- | --- | --- |
| SGawsBedrockAIAssetDSUtilSNC | `sn_ai_disc_aws_sgc_bedrock_ai_asset` | `sn_ai_disc_aws_sgc_bedrock_ai_system` |
| SGawsBedrockAISystemDSUtilSNC | `sn_ai_disc_aws_sgc_bedrock_ai_system` | `alm_ai_system_digital_asset` |
| SGawsBedrockAIModelDSUtilSNC | `sn_ai_disc_aws_sgc_bedrock_ai_model` | `alm_ai_model_digital_asset` |
| SGawsBedrockAIToolDSUtilSNC | `sn_ai_disc_aws_sgc_bedrock_ai_tool` | `sn_ent_ai_tool` |
| SGawsBedrockAIPromptDSUtilSNC | `sn_ai_disc_aws_sgc_bedrock_ai_prompt` | `alm_ai_prompt_digital_asset` |
| SGawsBedrockAISbcompM2mDSUtilSNC | `sn_ai_disc_aws_sgc_bedrock_sbcomp_m2m` | `sn_ent_ai_system_subcomponent_m2m` |
| SGawsBedrockAIUsageDSUtilSNC | `sn_ai_disc_aws_sgc_bedrock_ai_usage` | `sn_ai_disc_ai_usage` |
| SGAgentCoreDataSourceUtil | `sn_ai_disc_aws_sgc_agentcore_ai_system` | `alm_ai_system_digital_asset` |
| SGAgentCoreDataSourceUtil | `sn_ai_disc_aws_sgc_agentcore_ai_tool` | `sn_ent_ai_tool` |
| SGAgentCoreDataSourceUtil | `sn_ai_disc_aws_sgc_agentcore_ai_usage` | `sn_ai_disc_ai_usage` |
| SGSageMakerAIModelDSUtilSNC | `sn_ai_disc_aws_sgc_sg_awssagemaker_model` | `alm_ai_model_digital_asset` |
| SGSageMakerModelCardDSUtilSNC | `sn_ai_disc_aws_sgc_sg_awssagemaker_model` | `alm_ai_model_digital_asset` |

## AI Service Graph Connector for Microsoft

### Purpose

The AI Service Graph Connector for Microsoft is used to discover AI assets and usage data from Azure Foundry and Microsoft Copilot into ServiceNow AI Control Tower. Supported assets may include AI systems, agents, models, prompts, tools, subcomponents, and execution data.

### Required Roles

- `sn_ai_disc.discovery_admin`
- `sn_cmdb_int_util.sgc_admin`

## Azure Foundry Connection

### Purpose

The Azure Foundry connection enables AI Control Tower to discover Azure Foundry assets and retrieve execution data for supported AI services.

### Azure Foundry Prerequisites

Before creating the Azure Foundry connection, confirm that:
- OAuth credentials are available from Azure.
- The Azure client application has at least the `User.Contributor` role on the AI Hub or ML Services API.
- A workspace has been created.
- The Azure client application has at least the `Azure AI User` role on the Azure Foundry or Cognitive Services API.
- An Azure Foundry account or resource name has been created.
- Both Discovery and Execution import schedules are enabled.

### Connection Outcome

After the Azure Foundry connection is created, AI Control Tower can discover Azure Foundry agents, models, prompts, tools, subcomponents, and execution data.

### Azure Foundry Data Mapping

| **Data Source** | **Staging Table** | **Target Table** |
| --- | --- | --- |
| SG-Azure Foundry AI Discovery | `sn_azure_sg_foundry_ai_system` | Parent data source |
| SG-Azure Foundry AI Agents | `sn_azure_sg_foundry_agent` | `alm_ai_system_digital_asset` |
| SG-Azure Foundry AI Model | `sn_azure_sg_foundry_model` | `alm_ai_model_digital_asset` |
| SG-Azure Foundry AI Prompt | `sn_azure_sg_foundry_prompt` | `alm_ai_prompt_digital_asset` |
| SG-Azure Foundry AI Tool | `sn_azure_sg_foundry_tool` | `sn_ent_ai_tool` |
| SG-Azure Foundry AI Subcomponents | `sn_azure_sg_foundry_subcomponent` | `sn_ent_ai_system_subcomponent_m2m` |
| SG-Azure Foundry Execution | `sn_azure_sg_foundry_execution` | `sn_ai_disc_ai_usage` |

## Microsoft Copilot Connection

### Purpose

The Copilot connection enables AI Control Tower to discover Copilot Studio agents and retrieve related execution or usage data from the Microsoft environment.

### Copilot Prerequisites

Before creating the Copilot connection, confirm that:
- An application is registered in Microsoft Entra ID.
- The Client ID and Client Secret are available.
- The application user has been added in the Power Platform Admin Center.
- The application user has the Basic User and System Administrator roles.
- The Organization ID and Tenant ID are available.
- Usage tracking is performed in a non-developer environment.
- Both Discovery and Execution import schedules are enabled.
- The Discovery scheduled job is executed before the Execution scheduled job.

### Connection Outcome

After the Copilot connection is created, AI Control Tower can discover Copilot agents, models, prompts, tools, subcomponents, and execution data.

### Copilot Data Mapping

| **Data Source** | **Staging Table** | **Target Table** |
| --- | --- | --- |
| SGC-Copilot Discovery | `sn_msft_copilot_ai_agent_staging` | Parent data source |
| SGC-Copilot AI System | `sn_msft_copilot_ai_agent_asset_staging` | `alm_ai_system_digital_asset` |
| SGC-Copilot AI Model | `sn_msft_copilot_ai_agent_model_staging` | `alm_ai_model_digital_asset` |
| SGC-Copilot AI Prompt | `sn_msft_copilot_ai_agent_prompt_staging` | `alm_ai_prompt_digital_asset` |
| SGC-Copilot AI Tools | `sn_msft_copilot_ai_agent_tool_staging` | `sn_ent_ai_tool` |
| SGC-Copilot AI Subcomponents M2M | `sn_msft_copilot_ai_agent_sbcomp_m2m_staging` | `sn_ent_ai_system_subcomponent_m2m` |
| SGC-Copilot Execution | `sn_msft_copilot_ai_agent_usage_staging` | `sn_ai_disc_ai_usage` |

## Shared Microsoft Target Tables

Both Azure Foundry and Copilot use the following target tables.

### Digital Asset Tables

| **Table** | **Purpose** |
| --- | --- |
| `alm_ai_system_digital_asset` | Stores AI system digital assets |
| `alm_ai_prompt_digital_asset` | Stores AI prompt digital assets |
| `alm_ai_model_digital_asset` | Stores AI model digital assets |

### Entity Tables

| **Table** | **Purpose** |
| --- | --- |
| `sn_ent_ai_tool` | Stores AI tools |
| `sn_ent_ai_system_subcomponent_m2m` | Stores AI system subcomponent relationships |

### Usage Table

| **Table** | **Purpose** |
| --- | --- |
| `sn_ai_disc_ai_usage` | Stores AI usage and execution data |

---

## Microsoft APIs Used

### Azure Foundry — Discovery and Usage

| **API** | **Endpoint** | **Purpose** |
| --- | --- | --- |
| List Projects | Azure Management API | Lists Azure AI Foundry projects in a resource group |
| List Deployments | Azure AI Services project deployment endpoint | Lists model deployments within a Foundry project |
| List Agents | Azure AI Services agents endpoint | Lists agents in a Foundry project |
| List Agent Versions | Azure AI Services agent versions endpoint | Lists versions of a specific agent |
| List Conversations | Azure AI Services conversations endpoint | Lists conversation threads in a Foundry project |
| List Conversation Items | Azure AI Services conversation items endpoint | Lists messages or items within a conversation |

### AI Services Classic

| **API** | **Endpoint** | **Purpose** |
| --- | --- | --- |
| List Projects | Azure Management API | Lists AI Services projects in a resource group |
| List Deployments | Azure AI Services deployment endpoint | Lists model deployments within a project |
| List Assistants | Azure AI Services assistants endpoint | Lists assistants or agents in a project |
| List Threads | Azure AI Services threads endpoint | Lists execution threads in a project |

### ML Services / AI Hub

| **API** | **Endpoint** | **Purpose** |
| --- | --- | --- |
| List Subscriptions | Azure Management API | Lists available Azure subscriptions |
| List Resource Groups | Azure Management API | Lists resource groups within a subscription |
| List ML Workspaces | Azure Machine Learning Services API | Lists Azure ML workspaces in a resource group |
| List Deployments | Azure AI Services deployment endpoint | Lists model deployments within an ML project |
| List Assistants | Azure ML agents endpoint | Lists agents or assistants from an Azure ML workspace |
| List Threads | Azure ML threads endpoint | Lists threads from an Azure ML workspace |
| List Thread Runs | Azure ML thread runs endpoint | Lists runs within a specific thread |

---

## Copilot APIs Used

| **API** | **Endpoint** | **Purpose** |
| --- | --- | --- |
| List Agents | Dataverse bots endpoint | Returns metadata for Copilot Studio bots registered in a Dataverse environment |
| List Components per Agent | Dataverse botcomponents endpoint | Returns authoring components such as topics, entities, variables, and trigger phrases |
| List Conversations | Dataverse conversationtranscripts endpoint | Retrieves conversation transcripts between users and Copilot Studio bots |

## Data Flow Summary

AI Service Graph Connector data follows a standard flow:

External AI Platform → Data Source → Staging Table → Transform Map → Target Table → AI Control Tower Inventory and Dashboards

Staging tables temporarily hold imported data from AWS or Microsoft sources. Target tables store the transformed AI asset, relationship, and usage records used across AI Control Tower.

## AI Service Graph Connector for Google Cloud Platform Vertex AI

### Purpose

The AI Service Graph Connector for GCP Vertex AI is used to discover AI assets and usage data from Google Cloud Vertex AI into ServiceNow AI Control Tower. Supported assets include AI systems, models, prompts, tools, system subcomponents, and execution data.

Usage information imported through the connector is consumed by the AI Control Tower value dashboard.

### Required Roles

- `sn_ai_disc.discovery_admin`
- `sn_cmdb_int_util.sgc_admin`

### Prerequisites

Before creating a GCP Vertex AI connection, confirm that the organization has completed the required Google Cloud setup, including:
- Creating a service account.
- Assigning and binding the required roles.
- Enabling the required APIs.
- Creating a JKS file.
- Registering the JKS file in the ServiceNow instance.

Refer to the related ServiceNow setup instructions and API documentation for the detailed external platform requirements.

### Connection Outcome

After the GCP Vertex AI connection is created, AI Control Tower can discover Vertex AI assets and related execution data for inventory, lifecycle visibility, and value dashboard reporting.

### GCP Vertex AI Data Mapping

| **Data Source** | **Staging Table** | **Target Table** |
| --- | --- | --- |
| SG-GCPVertexAI - Execution | `sn_ai_disc_gcp_sgc_sg_gcp_execution` | `sn_ai_disc_ai_usage` |
| SG-GCPVertexAI - System | `sn_ai_disc_gcp_sgc_sg_gcp_ai_system` | `cmdb_ai_system_component_product_model` ; `alm_ai_system_digital_asset` ; `cmdb_ci_function_ai` ; `cmdb_rel_asset_ci` |
| SG-GCPVertexAI - Model | `sn_ai_disc_gcp_sgc_sg_gcp_ai_model` | `cmdb_ai_model_product_model` ; `alm_ai_model_digital_asset` |
| SG-GCPVertexAI - Tool | `sn_ai_disc_gcp_sgc_sg_gcp_ai_tool` | `sn_ent_ai_tool` |
| SG-GCPVertexAI - Prompt | `sn_ai_disc_gcp_sgc_sg_gcp_ai_prompt` | `cmdb_ai_prompt_product_model` ; `alm_ai_prompt_digital_asset` |
| SG-GCPVertexAI - System Subcomponent M2M | `sn_ai_disc_gcp_sgc_sg_gcp_ai_system_subcomponent_m2m` | `sn_ent_ai_system_subcomponent_m2m` |

## AI Service Graph Connector for LangGraph

### Purpose

The AI Service Graph Connector for LangGraph is used to discover AI assets and usage data from LangGraph and LangSmith into ServiceNow AI Control Tower. Supported assets include AI systems, models, prompts, tools, agents, and usage records.

Usage information imported through this connector is consumed by the AI Control Tower value dashboard.

### Required Roles

- `sn_ai_disc.discovery_admin`
- `sn_cmdb_int_util.sgc_admin`

### Prerequisites

Before creating a LangGraph connection, confirm that an API key has been created in LangSmith. The API key must provide access to the workspaces where AI assets and usage data should be discovered.

For self-hosted LangSmith environments, the organization should also confirm the appropriate LangSmith API and host API URLs.

### Connection Outcome

After the LangGraph connection is created, AI Control Tower can discover LangGraph agents and usage data, then map those records into AI digital asset, usage, and CMDB tables.

### LangGraph Data Mapping

| **Data Source** | **Import Set Table** | **Target Table** |
| --- | --- | --- |
| SG-LangGraph Agents | `sn_langgraph_integ_agents` | `alm_ai_system_digital_asset` ; `alm_ai_prompt_digital_asset` ; `cmdb_ci_function_ai` |
| SG-LangGraph Usage | `sn_langgraph_integ_usage` | `alm_ai_model_digital_asset` ; `sn_ai_disc_ai_usage` |

### LangGraph Target Tables

| **Table** | **Purpose** |
| --- | --- |
| `alm_ai_system_digital_asset` | Stores AI system digital assets |
| `alm_ai_prompt_digital_asset` | Stores AI prompt digital assets |
| `alm_ai_model_digital_asset` | Stores AI model digital assets |
| `sn_ai_disc_ai_usage` | Stores AI usage and execution data |
| `cmdb_ci_function_ai` | Stores AI function or agent CI records |

### LangSmith APIs Used

| **API** | **Endpoint Example** | **Purpose** |
| --- | --- | --- |
| List Workspaces | `https://api.smith.langchain.com/api/v1/workspaces/` | Lists workspaces available to the API key or user |
| List Deployments | `https://api.host.langchain.com/v2/deployments` | Lists agent deployments for a workspace |
| List Tracer Sessions | `https://api.smith.langchain.com/api/v1/sessions` | Lists tracer sessions for a workspace |
| Get Run Stats | `https://api.smith.langchain.com/api/v1/runs/stats` | Retrieves run statistics, including LLM invocations |

### LangGraph Agent Deployment APIs Used

| **API** | **Endpoint Example** | **Purpose** |
| --- | --- | --- |
| Search Assistants | `{{endpoint_url}}/assistants/search` | Lists assistants in each deployment |
| Search Threads | `{{endpoint_url}}/threads/search` | Lists threads for each deployment |

---

## AI Service Graph Connector for n8n

### Purpose

The AI Service Graph Connector for n8n is used to discover AI workflow assets and execution data from n8n into ServiceNow AI Control Tower. Supported assets include AI systems, models, tools, prompts, system subcomponents, and execution data.

### Connection Outcome

After the n8n connection is established, AI Control Tower can import n8n AI workflow records into AI digital asset, CMDB, entity, and usage tables.

### n8n Data Mapping

| **Data Source** | **Staging Table** | **Target Table** |
| --- | --- | --- |
| SG-n8n Execution | `sn_n8n_integ_sg_n8n_ai_execution` | `sn_ai_disc_ai_usage` |
| SG-n8n AI System | `sn_n8n_integ_sg_n8n_ai_system` | `cmdb_ai_system_component_product_model` ; `alm_ai_system_digital_asset` ; `cmdb_ci_function_ai` |
| SG-n8n AI Model | `sn_n8n_integ_sg_n8n_ai_model` | `cmdb_ai_model_product_model` ; `alm_ai_model_digital_asset` |
| SG-n8n AI Tool | `sn_n8n_integ_sg_n8n_ai_tool` | `sn_ent_ai_tool` |
| SG-n8n AI Prompt | `sn_n8n_integ_sg_n8n_ai_prompt` | `cmdb_ai_prompt_product_model` ; `alm_ai_prompt_digital_asset` |
| SG-n8n AI System Subcomponent M2M | `sn_n8n_integ_sg_n8n_ai_subcomp_m2m` | `sn_ent_ai_system_subcomponent_m2m` |

---

## AI Service Graph Connector for Salesforce

### Purpose

The AI Service Graph Connector for Salesforce is used to discover AI assets and usage data from Salesforce into ServiceNow AI Control Tower. Supported assets include AI systems, models, prompts, tools, and AI agent usage data.

Usage information imported through this connector is consumed by the AI Control Tower value dashboard.

### Required Roles

- `sn_ai_disc.discovery_admin`
- `sn_cmdb_int_util.sgc_admin`

### Prerequisites

Before creating a Salesforce connection, confirm that the organization has the required Salesforce connection details and OAuth credentials, including:
- Salesforce connection URL.
- OAuth Client ID.
- OAuth token URL.
- Required access to Salesforce AI agent, Einstein model, prompt, tool, and usage data.

### Connection Outcome

After the Salesforce connection is created, AI Control Tower can discover Salesforce AI agents, Einstein models, tools, prompts, and usage information.

### Salesforce APIs Used

| **API** | **Endpoint** | **Purpose** |
| --- | --- | --- |
| Bot Definition and Bot Version | Salesforce query API for `BotDefinition` and related `BotVersions` | Fetches AI agents created in Salesforce |
| Configured Einstein Models | Salesforce configured models endpoint | Fetches models configured in Salesforce Einstein Studio |
| GenAiFunctionDefinition | Salesforce query API for `GenAiFunctionDefinition` | Fetches tool details used by AI agents |
| GenAiPluginDefinition and GenAiPluginInstructionDef | Salesforce query API for plugin and instruction definitions | Fetches prompt information associated with or used by AI agents |
| ConversationDefinitionId and ConversationDefinitionEventLog | Salesforce query API for conversation event logs | Fetches AI agent usage information |

---

## Additional Connector Properties

### Microsoft Azure Foundry Usage Properties

| **Property** | **Description** | **Default Value** |
| --- | --- | --- |
| `sn_ai_msft_integ.usage_data_lookback` | Number of days to look back for fetching threads before the run collection window start time | `3` |
| `sn_ai_msft_integ.usage_first_run_lookback_days` | Number of days to look back for usage data on the first run when no `last_success_import_time` exists | `30` |

Both properties are stored in the System Property `[sys_properties]` table.

Organizations should validate the following before enabling connector-based discovery. For the required configuration values, refer to the Configuration specifications section for each connector.

| **Consideration** | **Guidance** |
| --- | --- |
| Connector readiness | Confirm which external AI platforms are in scope: AWS, Azure Foundry, Copilot, GCP Vertex AI, LangGraph, n8n, and Salesforce. |
| Required roles | Validate that the appropriate ServiceNow roles are assigned before connection setup, including `sn_ai_disc.discovery_admin` and `sn_cmdb_int_util.sgc_admin` , where applicable. |
| Credential strategy | Confirm that each connector uses the correct authentication method, such as AWS access keys, Azure OAuth credentials, GCP service account and JKS certificate, LangSmith API key, or Salesforce OAuth credentials. |
| Configuration specifications | Link each connector to its related configuration section: AWS configuration specifications, Microsoft Azure Foundry configuration specifications, Microsoft Copilot configuration specifications, GCP Vertex AI configuration specifications, LangGraph configuration specifications, n8n configuration specifications, and Salesforce configuration specifications. |
| External platform access | Validate that the external platform account has access to the AI assets and usage data intended for discovery. |
| API enablement | Confirm that required APIs are enabled before discovery. This is especially important for GCP Vertex AI, Azure Foundry, LangGraph/LangSmith, and Salesforce. |
| Usage data availability | Confirm whether the source platform supports usage or execution data and whether that data is available in the connected environment. |
| Schedule activation | Review Discovery and Execution import schedules. Where both are available, execute Discovery before Execution so asset records exist before usage records are imported. |
| First-run data window | For Azure Foundry, review system properties that control lookback behavior, including `sn_ai_msft_integ.usage_data_lookback` and `sn_ai_msft_integ.usage_first_run_lookback_days` . These determine how much historical usage data is retrieved during scheduled imports. |
| Data mapping validation | Validate that records flow from the external platform to the staging table, transform map, and target table as expected. |
| Target table alignment | Confirm that imported records align with the AI Control Tower asset model, including AI systems, models, prompts, tools, subcomponents, and usage records. |
| CMDB relationship quality | For connectors that populate CMDB-related tables, validate whether relationships are created correctly between AI systems, models, functions, prompts, tools, and related assets. |
| Value dashboard readiness | Confirm that usage records are imported into `sn_ai_disc_ai_usage` , since this table supports downstream AI Control Tower value dashboard reporting. |
| Environment limitations | Confirm connector-specific limits, such as Copilot usage being tracked only in non-developer environments. |
| Data uniqueness | Validate naming and deduplication behavior for discovered tools, prompts, agents, and models, especially when the same asset name exists across tenants, workspaces, projects, or environments. |
| Security and credential handling | Store all secrets, API keys, certificates, and OAuth credentials securely. Limit access to only the teams responsible for connector administration. |
| Post-import validation | After the first import, review discovered records in the AI inventory and confirm that asset classification, relationships, ownership, lifecycle state, and usage records are accurate. |

## Implementation Considerations

Organizations should validate the following before enabling connector-based discovery:
- Required roles are assigned in ServiceNow.
- External platform credentials are available and securely managed.
- Required API permissions are granted.
- Discovery and execution schedules are reviewed and activated where needed.
- Usage data is available in the source platform.
- Imported records are validated in the AI inventory after the first scheduled import.
- Data mappings align with the expected AI asset lifecycle model in AI Control Tower.

See AWS Configuration Specifications for Amazon Bedrock, Bedrock AgentCore, SageMaker, and CloudWatch requirements.

See Microsoft Azure Foundry Configuration Specifications for OAuth, AI Hub, ML Services, Azure AI User role, and usage lookback properties.

See Microsoft Copilot Configuration Specifications for Entra ID, Power Platform Admin Center, Dataverse, and non-developer environment requirements.

See GCP Vertex AI Configuration Specifications for service account, role binding, enabled APIs, JKS certificate, and organization ID requirements.

See LangGraph Configuration Specifications for LangSmith API key, workspace access, hosted versus self-hosted URL requirements, and MID Server considerations.

See n8n Configuration Specifications for workflow asset discovery, execution data, and target table mapping.

See Salesforce Configuration Specifications for OAuth, Salesforce AI agent, Einstein model, prompt, tool, and usage data access.

## Appendix

### Quick-Reference Checklist

Use the following checklist when configuring the Discovery layer for AI Control Tower.

| **Pre-Go-Live Discovery Checklist** |
| --- |
| ☐ AI Control Tower SKU and sn_ent plugin are provisioned and active. |
| ☐ Users requiring API access hold asset and model_manager roles. |
| ☐ AI asset record types (System, Model, Dataset, Prompt) are defined and scoped. |
| ☐ Record Producer forms are limited to required fields; UI policies replace client scripts where possible. |
| ☐ Variable sets are configured for reuse across asset intake forms. |
| ☐ Post-submission logic is routed to Flow Designer or Subflows (not inline producer scripts). |
| ☐ UI Builder layouts use OOTB components; no unnecessary custom components. |
| ☐ Data Resources are filtered — no wildcard queries in production. |
| ☐ All UI Builder experiences tested with real user personas and role simulations. |
| ☐ AWS Bedrock and Azure AI Foundry integration docs reviewed when available. |

# Govern - Risk and Controls

This guide provides implementers with a structured, step-by-step approach to configure, and operationalize an AI Risk & Compliance solution that supports effective AI governance. It ensures technical teams can deploy the solution in alignment with regulatory requirements, organizational policies, and best practices, enabling consistent risk management, compliance monitoring, and audit readiness across the AI lifecycle.

## Intended Audience

The intended audience for the AI Risk & Compliance Implementation Guide would be:
- Implementation Engineers / Solution Integrators – responsible for installing and configuring the solution
- Compliance & Risk Technology Specialists – bridging technical setup with governance and regulatory requirements
- AI Stewards – overseeing solution deployment in alignment with organizational AI governance strategy

## Understanding the AI Risk & Compliance Solution

### Overview of AI Governance Frameworks

AI Governance Frameworks provide structured guidance for ensuring that artificial intelligence systems are developed, deployed, and operated in a responsible, compliant, and risk-aware manner. These frameworks translate high-level principles— such as fairness, transparency, accountability, safety, and human oversight—into practical governance requirements that organizations can operationalize.

The purpose of this section is to establish a common reference point for aligning the AI Governance solution with recognized global standards and regulatory expectations. Frameworks such as the EU AI Act, ISO/IEC 42001, and the NIST AI Risk Management Framework (AI RMF) define what must be governed, why it matters, and which outcomes regulators and stakeholders expect.

| **Aspect** | **EU AI Act** | **NIST AI RMF** |
| --- | --- | --- |
| Nature | Legally binding regulation (EU law) | Voluntary risk management guidance |
| Key Driving Force | Ensure AI is safe, trustworthy, and respects fundamental rights; risk-based regulatory obligations | Provide a structured approach to manage AI risks across the lifecycle |
| Risk Classification | Four-tier risk system: Unacceptable, High, Limited, Minimal | Flexible, organization-defined risk taxonomy |
| Compliance Obligations | Conformity assessments, documentation, risk management, transparency, human oversight | Map–Measure–Manage–Govern functions, continuous improvement |
| Key Value Benefits | Legal certainty, consumer trust, clear obligations based on risk | Practical, flexible, lifecycle-based AI risk governance |
| Implementation Focus for AI Risk & Compliance Solution | Map AI use cases to risk categories, automate conformity checks, manage technical documentation | Integrate risk identification & measurement workflows, track mitigation progress |
| Adoption Timeline | Gradual enforcement from 2024–2026 | Ongoing voluntary adoption |
| Enforcement | Regulatory authorities & penalties for non- compliance | None – voluntary |

### Core Modules & Capabilities

The core modules outlined in this section represent the foundational building blocks for managing AI risk, compliance, and accountability. They support key governance activities such as entity scoping, AI inventory management, risk identification and assessment, control implementation, compliance monitoring, workflow automation, and reporting. Each module contributes specific capabilities, but value is realized when they are configured and integrated as part of a cohesive operating model.

| **AI Risk and Compliance Management** | **Assessments (FRIA, Conformity etc.) with chat collaboration** |
| --- | --- |
| AI Risk and Compliance Workspace – Dashboards and Reports |  |
| Smart Assessment Engine | Create Assessment templates and trigger assessments |
| Policy and Compliance Management | Manage policies, authority documents, citations, control objectives, controls, control attestation, policy acknowledgements, policy exceptions and issues |
| Content Accelerators | Content: NIST AI RMF, EU AI Act Content Pack |
| Risk Management | Establish Risk Frameworks, Risk Statements, Risk Instances and Risk response. Perform risk assessments (using classic) on AI Systems, AI Models & Data Sets. |
| Advanced Risk Management | Advanced Risk Assessments (Limited) on AI Systems, AI Models & Data Sets. Roll risks up the hierarchy and Heatmap report. |

### Roles & Responsibilities

The purpose of this section is to establish a common role model that aligns governance, risk, compliance, technical, and business stakeholders. AI governance spans multiple disciplines—legal, compliance, risk management, data science, IT, and business leadership—and without clearly defined responsibilities, critical governance activities such as risk assessments, approvals, monitoring, and issue remediation may be delayed or inconsistently applied.

The roles and responsibilities outline the key stakeholders involved in implementing and operating the AI Risk & Compliance solution, defining their accountabilities across installation, configuration, governance, and ongoing compliance monitoring. Clear role assignment ensures effective collaboration, regulatory alignment, and sustained operational ownership of the solution.

System-defined Roles ([link](https://www.servicenow.com/docs/bundle/zurich-governance-risk-compliance/page/product/grc-ai-risk-compliance/reference/roles-installed-with-ai-risk-and-compliance.html))

## AI Artifacts Informational Records

### AI System/ Use case

#### Overview

The AI System / Use Case Registry is a central inventory of all AI-enabled business use cases within the organization.

#### Key Value Benefits

It provides visibility, ownership, and accountability for each AI system and serves as the starting point for governance, risk assessment, and compliance activities.

Example: An “Automated Loan Approval System” used by the Retail Banking entity to support customer credit decisions.

#### Procedure

Request an AI use case/ system ([link](https://www.servicenow.com/docs/r/governance-risk-compliance/ai-risk-management/request-ai-system.html))

#### Configuration

Refer to the Govern – Lifecycle topic in this document.

## AI Model

### Overview

The AI Model Registry is a catalog of the AI models that support one or more AI systems or use cases.

### Key Value Benefits

It enables technical transparency, version tracking, and model-level governance, ensuring changes to models are controlled and traceable.

Example: A machine-learning classification model used to predict loan default risk, version 2.3, deployed in production.

### Procedure

Request an AI Model ([link](https://www.servicenow.com/docs/r/governance-risk-compliance/ai-risk-management/request-ai-model.html))

### Configuration

Refer to Govern – Lifecycle topic.

## Dataset

### Overview

The Dataset Registry is an inventory of datasets used to train, test, or operate AI models.

### Key Value Benefits

It supports data transparency, privacy, and quality management by documenting where data comes from and how it is used.

### Procedure

Request a Dataset ([link](https://www.servicenow.com/docs/r/governance-risk-compliance/ai-risk-management/request-dataset.html))

### Configuration

Refer to Govern – Lifecycle topic

## External Regulations

External regulations are rules and laws created by governments and regulators that control how artificial intelligence can be used. Their main goal is to make sure AI systems are safe, fair, transparent, and do not cause harm to people or organizations.

These regulations explain what organizations are allowed to do, what they must do, and what they must avoid when designing, using, or deploying AI. They often place extra requirements on AI systems that can significantly affect people’s lives, such as systems used for hiring, lending, healthcare, or public services.

## Regulatory Agencies

### Overview

Agencies are external regulatory, supervisory, or standard-setting bodies that issue requirements applicable to AI systems. Regulatory Agency is an independent agency responsible for exercising laws or standards or guidelines in a specific field or activity or business operations.

### Key Value Benefits

It establishes a centralized library of agencies for identifying relevant regulatory authorities that are responsible for overseeing industries or sectors within each jurisdiction.
- European Commission
- National financial regulators overseeing AI credit decisions

### Procedure

A. Add a Regulatory Agency ([link](https://www.servicenow.com/docs/bundle/yokohama-governance-risk-compliance/page/product/grc-compliance-case-mgmt/task/add-regulatory-agency.html))

B. Relate Authority Document ([link](https://www.servicenow.com/docs/r/governance-risk-compliance/grc-common-functions/add-authority-document-agency.html))

### Configuration

Not Applicable

> [!note] Note
> In Authority Document, use the form field “Regulated By” to build a relation with the Agency

360-degree view association is not supported

## Authority Documents

### Overview

Authority Documents are official regulatory texts, standards, or guidance issued by an agency.

### Key Value Benefits

They serve as the source of compliance obligations.
- EU Artificial Intelligence Act
- ISO/IEC 42001 AI Management System
- NIST AI Risk Management Framework

### Procedure

Create Authority Document ([link](https://www.servicenow.com/docs/r/governance-risk-compliance/policy-and-compliance-management/t_CreateAnAuthorityDocument.html))

### Configuration

Not Applicable

> [!note] Note
> · In Authority Document, use the form field “Regulated By” to build a relation with the Agency

- Community Post ([link](https://www.servicenow.com/community/grc-articles/servicenow-introduction-to-grc-module-along-with-authority/ta-p/2426341))
- Compliance Score for an AD is based on average of the children control objectives, which themselves are based on averages of their children controls. This is one of the core functionalities in Policy & Compliance.

## Citations

### Overview

Citations are specific, actionable requirements or clauses within an authority document.

### Key Value Benefits

They define what must be complied with.
- EU AI Act Article requiring human oversight for high-risk AI systems
- ISO 42001 clause on AI risk assessment

### Procedure

A. Create a Citation ([link](https://www.servicenow.com/docs/bundle/yokohama-governance-risk-compliance/page/product/grc-policy-and-compliance/task/t_CreateCitations.html))

B. Citation to Control Mapping ([link](https://www.servicenow.com/docs/r/governance-risk-compliance/policy-and-compliance-management/citation-to-control-mapping.html))

> [!note] Note
> Community Post ([link](https://www.servicenow.com/community/grc-articles/servicenow-introduction-to-grc-module-along-with-authority/ta-p/2426341))

## Internal Business Operations

Internal business objectives describe what the organization wants to achieve by using AI. These goals may include improving efficiency, reducing costs, increasing accuracy, enhancing customer experience, or supporting better decision-making.

This section explains how AI is used to support business goals, policies and control measures while ensuring it is done responsibly and safely. It helps align AI initiatives with company values, risk tolerance, and legal responsibilities, so AI delivers benefits without creating unintended harm or risk.

### Overview

Control Objectives describe what outcome a set of controls is intended to achieve, without prescribing how. In the AI Control Tower, clients can define and manage their own Policies based on their internal governance, regulatory requirements, and risk tolerance. These policies serve as a foundation for responsible AI usage, outlining acceptable practices, ethical considerations, and compliance expectations. The Control Tower’s control objectives are designed to be flexible and can be directly mapped to each client’s AI Policies, enabling automated monitoring and validation of policy adherence. This mapping provides transparency and traceability, ensuring organizations can demonstrate compliance with both internal standards and external regulations.

To ensure relevance and effectiveness within each organization’s unique context, clients are expected to map the AI Risk Statements to the corresponding Control Objectives. This mapping enables traceability, ensures that controls effectively mitigate identified risks, and supports comprehensive risk management tailored to the client's specific AI use cases and regulatory landscape.

| **What it is** | **A statement describing something the organization must do or should do to govern an AI system. It is something you actively measure and test against.** |
| --- | --- |
| What it does | Provides a specific, actionable requirement that the Business Owner must attest to. Linked to authority documents (your internal AI standards, EU AI Act, NIST AI RMF) via citations. |
| Who does it | Pre-configured by Platform Admin during implementation. Attached to AI Systems automatically via Impact Assessment answers. |
| Output | A control instance on the AI System record. A control attestation task assigned to the Business Owner. |

### Key Value Benefits

Foundation for Responsible & Ethical AI Usage. They provide a governance bridge between regulatory requirements and operational controls.

Example: “Ensure AI systems are monitored for discriminatory outcomes throughout their lifecycle.”

### Procedure

A. Create a Control Objective ([link](https://www.servicenow.com/docs/bundle/yokohama-governance-risk-compliance/page/product/grc-policy-and-compliance/task/t_CreateAPolicyStatement.html))

B. Map a Control Objective to a Citation ([link](https://www.servicenow.com/docs/bundle/yokohama-governance-risk-compliance/page/product/grc-policy-and-compliance/task/t_RelatePSToACitation.html))

## Controls

### Overview

Controls are specific policies, procedures, or technical measures designed to mitigate risks and meet control objectives.

### Key Value Benefits

They operationalize governance and compliance requirements. Examples include below:
- Mandatory bias testing before model deployment
- Human review required for AI-assisted decisions

### Procedure

Create Control ([link](https://www.servicenow.com/docs/r/aUYojakX2btrvRdtS_~doA/y1DWnDBJ03KqyZYJU18_xw))

> [!note] Note
> Compliance Score Calculation for Entity ([link](https://www.servicenow.com/docs/r/governance-risk-compliance/grc-compliance-management-workspace/compliance-score-calculation-pc-ws.html))

Compliance Score calculation for Citation ([link](https://www.servicenow.com/docs/r/yokohama/governance-risk-compliance/policy-and-compliance-management/compliance-score-calculation-for-a-citation.html))

## Policies

### Overview

Policies are formal organizational statements that define expectations, principles, and rules. Policies are internal to organization. Usually, all the policy statements that requires to be measured in the policy document will be created as control objectives. When creating control objectives under policies, it is AI compliance manager responsibility to map the control objectives to external regulations (specifically, the citations) such as the EU AI Act and NIST AI RMF.

Companies use their own template for defining Policy Documents. A sample policy may contain sections such as Content and Purpose, Definitions, Controls in Policies, Responsibilities, Revisions and References. Among these sections, Controls section in the policy are the one to be considered for control objectives of the policy.

### Key Value Benefits

They set the tone and governance standards for AI use.

Example: Enterprise Responsible AI Policy defining fairness, transparency, and accountability principles.

### Procedure

A. Create Policy ([link](https://www.servicenow.com/docs/r/governance-risk-compliance/grc-compliance-management-workspace/create-policy-ws.html))

B. Publish Policy ([link](https://www.servicenow.com/docs/r/governance-risk-compliance/grc-compliance-management-workspace/approve-and-publish-policy-ws.html))

### Configuration

Not Applicable

### Things to Note

Not Applicable

## Risk Exposure

The Risk Framework and Risk Statements tables are used to define and group various risks. While Risk Frameworks serve more as high-level categories or containers, Risk Statements describe specific risks. With Advanced Risk enabled, organizations can create hierarchical risk structures, meaning one risk can be broken down into several sub-risks, allowing for more detailed and structured risk analysis. For example, an "Information Technology Risk" might include sub-risks like IT operations, infrastructure, and performance, helping stakeholders drill down into precise risk areas.

## Risk Statements

### Overview

Risk Statements describe a specific AI-related risk in a structured format, typically including cause, event, and impact. The AI Risk Statement Library in ServiceNow AI Risk and Compliance provides a centralized, structured collection of pre-defined AI risk statements that organizations can use to identify, assess, and manage AI risks consistently across the enterprise.

| **What it is** | **A pre-defined description of a risk that may apply to an AI system. It is part of a risk library that is configured before any AI systems go through the workflow.** |
| --- | --- |
| What it does | Describes a risk that needs to be monitored and managed. When attached to an AI System via the Impact Assessment questions and answers, it creates an individual risk record for that specific system. |
| Who does it | Pre-configured by Platform Admin. Sourced from your organization's authority documents and risk library. Attached to AI Systems automatically via Impact Assessment answers. |
| Output | Individual risk records created on the AI System. These feed the Risk Assessment (residual risk) process later. |

### Key Value Benefits

They ensure risks are clearly and consistently articulated.

### Procedure

Create Risk Statement ([link](https://www.servicenow.com/docs/bundle/yokohama-governance-risk-compliance/page/product/grc-risk/task/t_CreateRiskState.html))

## Risks

### Overview

Risks are recorded, assessed risk instances that are actively managed.

### Key Value Benefits

They enable prioritization, treatment, and monitoring.

Example: Bias risk associated with an automated credit approval model used in multiple jurisdictions.

### Procedure

Create Risk ([link](https://www.servicenow.com/docs/bundle/yokohama-governance-risk-compliance/page/product/grc-workspace-risk/task/create-risk-stmt-workspace.html))

## Monitoring

### Indicators

#### Overview

Indicators are metrics used to monitor risk exposure or control performance over time. Indicators collect data to monitor controls and risks, and to collect audit evidence. Indicators monitor a single control or risk. They are used to enhance and facilitate the monitoring, mitigation, and reporting of risks.
- Control Indicators: These are metrics or measures used to assess the effectiveness of controls. They can be created at any stage of the control lifecycle.
- Draft Stage: While a control is in the Draft stage, it's typically not finalized or implemented. However, ServiceNow allows creating control indicators during this stage.
- Monitor Stage: Controls in the Monitor stage are actively implemented and ready for assessment. This stage is the most logical time to start using control indicators and generating indicator tasks.

#### Key Value Benefits

They support ongoing oversight and early warning.

#### Procedure

A. Create Control Indicator ([link](https://www.servicenow.com/docs/r/governance-risk-compliance/policy-and-compliance-management/create-control-indicator-2.html))

B. Manage Control Indicator ([link](https://www.servicenow.com/docs/r/governance-risk-compliance/policy-and-compliance-management/manage-indicators-policy-comp.html))

## Issues

### Overview

Issues represent identified control failures, compliance gaps, or unacceptable risk levels. The ServiceNow Issue Management process provides a comprehensive framework for identifying, tracking, and resolving issues that could impact business objectives, compliance, or organizational reputation. This process integrates seamlessly with other modules including AI Risk Management, AI Policy and Compliance.

### Key Value Benefits

They drive remediation and accountability.

Example: Failure to document training data lineage for a high-risk AI model.

### Procedure

A. Create Issue ([link](https://www.servicenow.com/docs/r/governance-risk-compliance/policy-and-compliance-management/t_CreateAnIssue-2.html))

B. Remediate Issue ([link](https://www.servicenow.com/docs/r/governance-risk-compliance/policy-and-compliance-management/remediate-issue.html))

### Configuration

Configure Issue Mapping ([link](https://www.servicenow.com/docs/r/governance-risk-compliance/grc-common-functions/enable-or-disable-issue-relationship-configuration.html))

## Policy Exceptions

### Overview

Policy Exceptions are formally approved deviations from established policies or controls. A policy exception allows for a formal, authorized deviation from established policies, typically for a specific duration and user. These exceptions are granted when a justified business need arises, and they are managed through a lifecycle with defined stages, including analysis, review, and approval.

### Key Value Benefits

They allow controlled flexibility while maintaining governance oversight. Examples include below:
1. Use of Non-Approved Training Data – AI model trained on datasets not cleared under the organization’s data governance policy.
2. Bypassing Model Validation Steps – Deployment without completing required fairness or robustness testing.
3. Third-Party AI Service Without Review – Integrating an external AI API without security and compliance clearance.

### Procedure

Request for Policy Exception ([link](https://www.servicenow.com/docs/r/governance-risk-compliance/policy-and-compliance-management/request-policy-exception.html?contentId=Ie3vFO6Of9izmC5jME8eww))

## AI Risk & Compliance Landscape

### Overview

Every governance requirement in AICT traces back through the same chain. Understanding this chain helps explain why configuration happens in a specific order and why each component depends on the ones above it.

| **Level** | **Component** | **What It Is** | **Created By** |
| --- | --- | --- | --- |
| 1 | Authority Document | The regulatory framework or internal standard | Platform Admin loads via content pack or manual creation |
| 2 | Citation | A specific article, section, or clause within the authority document | Loaded automatically with content pack or manually created |
| 3 | Control Objective | The actionable thing your organization must DO to comply with a citation | Platform Admin uploads from your AI Standards. Mapped to citations. |
| 3 | Risk Statement | A description of what could go WRONG — your risk library | Platform Admin uploads from your risk register. Also mapped to citations. |
| 4 | Individual Risk Record | The instance of a risk statement mapped to one specific AI System | Created automatically when an Impact Assessment answer triggers a risk statement |
| 5 | Residual Risk Score | How much risk remains after controls are attested | Calculated automatically: Inherent Risk × Control Effectiveness |

Control Objectives and Risk Statements both sit at Level 3. They are separate things but both relate to citations. The Impact Assessment is the engine that connects them to individual AI Systems.

## Business Configuration

### AI Risk & Compliance Content

#### Overview

Your one-stop shop for AI risk and compliance content, Browse, Search and easily download AI Regulations or Frameworks to link to your internal control objectives or risk statements and run audits or assessments against them. Currently, the application offers the following:
1. EU AI Act: The EU AI Act is a regulatory framework that sets common rules for the use of artificial intelligence in the European Union. It follows a risk-based approach, classifying AI systems into unacceptable, high, limited, and minimal risk categories. Higher-risk AI systems are subject to stricter requirements such as risk management, transparency, human oversight, and ongoing monitoring.
- a. Structural Units: The content pack is structured into 13 chapters and contains 113 Articles covering risk based regulatory requirements for AI systems.
- b. Note: Control Objectives mapping with EU AI Act is planned for future releases to align requirements to operational objectives.
2. NIST AI RMF: The NIST AI Risk Management Framework (AI RMF) provides voluntary guidance for managing risks associated with AI systems throughout their lifecycle. It focuses on building trustworthy AI by addressing risks related to governance, fairness, reliability, security, privacy, and transparency.
- a. Structural Units: 4 Core functions (Govern, Map, Measure, Manage) provide the backbone.
- b. Control Objectives: Preventive controls dominate in Govern, Map, and Manage, as these functions focus on policies, risk identification, and mitigation planning. Detective controls are concentrated in Measure and the monitoring aspects of Manage, focusing on ongoing assessments, audit trails, and reporting.
- c. Risk Statements: AI-Specific Risk Libraries - What risks should be included in a risk library that addresses both common and AI-specific risks (e.g., algorithmic bias, model drift, data integrity, cybersecurity threats)?

#### Key Value Benefits

- Provides the ability to choose the framework you want to use and activate.
- Helps you to choose the citations that are associated with a particular framework and install them in the active state in your instance.
- Enables you to choose control objectives, which are associated with the selected citations.
- Helps you to select the risk statements.

#### Procedure

A. Install (store) | ([link](https://store.servicenow.com/store/app/f9e3123c1b956ed47d31ed7a234bcb96))

B. Activate EU AI Act ([link](https://www.servicenow.com/docs/r/governance-risk-compliance/ai-risk-management/activate-or-update-eu-artificial-intelligence-act.html))

C. Activate NIST AI RMF ([link](https://www.servicenow.com/docs/r/governance-risk-compliance/ai-risk-management/activate-or-update-nist-using-the-content-accelerator.html))

#### Configuration

A. Import: Users can import control objectives in bulk using an Excel spreadsheet by following the step-by-step instructions provided in the community post ([link](https://www.servicenow.com/community/grc-forum/is-there-a-tutorial-on-how-to-import-and-map-controls-from-a/m-p/1294959/page/3))

> [!note] Note
> Regulatory Support Statement

*ServiceNow's Risk products are built to help our customers address regulatory requirements under various jurisdictions across the globe. ServiceNow aims to provide software updates for new or updated major regulations and requirements within twelve to eighteen months of the regulation's publication.*

*For the regulations that ServiceNow provides a level of support out of the box, software updates for minor regulatory changes are aimed to be provided within 12 months. For major regulatory changes, we may require up to eighteen months to deliver updates, depending on scope and impact. We differentiate between typical regulatory content updates (which do not require software updates or enhancements) and regulatory updates which do require software updates or enhancements. Content updates are generally delivered on a shorter cadence than if software update or enhancement is required for the regulatory update or change.*

*ServiceNow's Risk products do not guarantee compliance. Our products are intended to help provide guidance and input on regulations, and customers are ultimately responsible for their own compliance with applicable regulations.*

> [!important] Important
> The pre-packaged content included in this product is provided solely for informational and guidance purposes to assist with the initial setup of AI Risk & Compliance frameworks. It does not constitute legal advice or assurance of regulatory compliance. Customers are solely responsible for ensuring that all use of the content complies with applicable laws, regulations, directives, and industry standards in their jurisdictions. By using this content, the Customer acknowledges that it must independently validate, customize, and maintain the accuracy and relevance of all information based on its specific legal, regulatory, and operational context. The provider disclaims any liability for decisions made based on the use of such content.

## Risk Assessment Methodology

### Overview

The Risk Assessment Methodology (RAM) is used for assessing either the risks or objects in your organization. A RAM is configured to specify the types of risk assessments and the entities on which risk assessment is performed. A configured RAM is an object with associated assessment types that have associated factors.

About Regulatory Risk Classification (using Object-based RAM)

| **What it is** | **A questionnaire scored against your organization's pre-configured risk factors to calculate an inherent risk tier for the AI System as a whole.** |
| --- | --- |
| What it does | Determines HOW RISKY the AI system is overall. Primary factors set the base tier. Control factors can escalate the tier. Produces: Low / Medium / High / Unacceptable. |
| Who does it | Business Owner fills it out. The task can be reassigned to R&C Manager if needed. |
| Output | Inherent risk tier applied to AI System record: Low / Medium / High / Unacceptable. |

About Risk Assessment (using Risk-based RAM)

| **Factor Name** | **What It Considers** | **Scoring Range** |
| --- | --- | --- |
| Regulation Complexity | How complicated the regulatory requirement is to understand and comply with, including history of changes and pending updates | Low: Simple and easy to understand / Moderate: Requires legal opinion / High: Extremely complex, requires third-party expertise / Unacceptable: Significant regulatory implications |
| Number of Businesses Impacted | How many business units are impacted by the regulatory requirement, directly or indirectly, across business functions | Low: Less than 30% of business / Moderate: 30–60% / High: 60–90% / Unacceptable: More than 90% of business |
| Financial Impact | Potential monetary fines, penalties, legal judgments, and financial exposure from litigation as a result of non-compliance | Low: Less than $100K / Moderate: $100K–$500K / High: $500K–$1M / Unacceptable: More than $1M |
| Operational Impact to Business | Compliance risk arising from complexity of business processes and changes to products, services, or staffing that may impact compliance risk | Low: Little to no regulatory scrutiny / Moderate: Additional scrutiny, no significant action / High: Significant regulatory action or fines / Unacceptable: Intolerable operational impact |
| Reputational Impact | Potential impact on organizational reputation from being non-compliant | Low: No social media or news mention / Moderate: Local impact, no national coverage / High: National coverage and social media / Unacceptable: Significant brand damage |
| Regulatory Scrutiny | Overall trends in enforcement activity from regulators and current focus from regulators and industry groups on the requirement | Low: No likelihood of regulatory scrutiny / Moderate: Additional scrutiny, no significant action / High: Regulatory scrutiny certain with significant action / Unacceptable: Significant regulatory implications |
| Likelihood | How likely the risk event is to occur, based on history and current circumstances | Rare / Possible / Likely / Immediate |

## Residual Risk

| **What it is** | **The final calculation showing how much risk remains AFTER controls have been attested. Combines Inherent Risk score with Control Effectiveness score.** |
| --- | --- |
| What it does | Produces a residual risk score per individual risk record. Shows whether the AI system is still at risk after controls are in place. Rolls up to AI System level. |
| Who does it | Calculated automatically by the system. No manual input required. |
| Output | Residual risk per individual risk: Critical / High / Medium / Low. Rolled up to AI System record. |

### Key Value Benefits

This allows organizations to apply different methodologies for assessing risk — with distinct processes and approaches tailored to each scenario. Whether conducting a BIA, RCSA, PRCSA, application assessment, site assessment, or any other framework, the possibilities are virtually endless.

### Procedure

Configure RAM ([link](https://www.servicenow.com/docs/bundle/yokohama-governance-risk-compliance/page/product/grc-risk/task/configure-ram.html))

### Configuration

A. Configure RAM ([link](https://www.servicenow.com/docs/bundle/yokohama-governance-risk-compliance/page/product/grc-risk/task/configure-ram.html)): AI Risk and Compliance ships with out-of-the-box risk assessment methodologies to help organizations evaluate and manage AI-related risks efficiently. These include:

| **Name** | **Description** |
| --- | --- |
| Automated risk classification for AI system | Type: Object-based A First-Principles Approach: Classify Risks by What Really Matters. Instead of asking "Which regulatory category does this belong to?" we ask: "What risks does this system actually introduce into the organization and to affected people?" The framework evaluates seven core dimensions/ risk factors, each scored 1-4: These automated risk factors are intentionally rooted in Responsible AI principles (fairness, accountability, safety, transparency, robustness, human agency) - Impact on people & society - How it's used (context) - Human oversight - Data & model risks - Cybersecurity risks - Governance & compliance |
| Risk classification for AI system | Type: Object-based Evaluate AI assets against applicable regulatory requirements, identifying the level of regulatory risk based on factors such as Operational Impact, Financial Impact, Reputational Impact, Regulation Complexity, Regulatory Scrutiny and Likelihood—enabling appropriate classification and prioritization of compliance actions. The outcome of this assessment drives the Regulatory Risk Classification on the overview page of the AI Asset. This classification guides compliance priorities and risk mitigation efforts. This is driven by calculating a risk score for an AI Asset record based on two vectors: likelihood and impact. - Impact o Operational Impact o Business Impact o Financial Impact o Reputational Impact o Regulation |
|  | Complexity o Regulatory Scrutiny - Likelihood |
| Risk assessment for AI inventory | Type: Risk-based Assess inherent and residual risks tied to each asset. Risk Assessment for AI Asset Inventory is used for assessment of the Inherent/Residual risks for impact and likelihood of the AI Asset once categorized. The risk assessment methodology for the risks includes an automated factor for the Control Assessment factor. This is a scripted factor that pulls the related control compliance scores to determine the Control effectiveness score for the risk assessment. - Impact - Likelihood |
| Risk classification for AI Model or Dataset B.    Download Risk Assessment Methodologies | Type: Object-based Categorize AI assets such as AI Models or Datasets based on factors like impact, sensitivity, and usage in the onboarding process - Impact o Operational Impact o Business Impact o Financial Impact o Reputational Impact o Regulation Complexity o Regulatory Scrutiny - Likelihood |

1. Login as Admin
2. For Risk Assessment Methodologies, go the ALL (Application Navigator) – search ‘sn_risk_advanced_risk_assessment_methodology.list’
3. Apply Filter search by setting Show Matching search result on Domain Area as “AI Risk and Compliance”
4. You will see 4 OOTB Risk Assessment Methodologies applied to support the following
5. Object-based Risk Assessment (AI Assets ONLY)
6. Object-Risk-based Risk Assessment (AI Asset-Risk)
7. Set Key Reporting Columns for Extraction
8. From there, you should be able to export into the following formats ([link](https://www.servicenow.com/docs/bundle/zurich-platform-administration/page/administer/exporting-data/concept/c_ExportData.html))

> [!note] Note
> A. Migrate to Advanced Risk Assessments to validate risk aggregation/ risk roll-up. Once activated, this cannot be reverted.

B. Risk Scoring: Risk Scoring helps us understand how risky an AI system could be by evaluating how serious a problem would be and how likely it is to happen, so we can apply the right safeguards. It Risk Scoring functions similarly to how enterprises evaluate risks associated with AI systems, models, and datasets. We consider two key questions:
- `a. What would be the severity of the impact?`
- `b. How probable is it that this will occur?`

By combining these responses, it determines a Risk Score, which guides decisions on whether additional controls, monitoring, or approvals are necessary for the AI asset. The inherent and residual scores for risk are calculated using the industry recognized risk criteria, likelihood, and impact. These are defined while setting up the Risk Assessment Methodology.

Within AI Control Tower, the risk score is typically a configurable, weighted composite score based on overall impact by looking into Operational, Financial, Reputational, Regulatory, and business impact and likelihood. Organizations adjust these weightings to fit their specific AI risk management frameworks.

C. Risk Aggregation: Aggregation of the scores can happen on entity hierarchy, statement hierarchy or both. The aggregation can be based on sum, average, maximum, minimum. The individual assessment scores gets aggregated at the entity and risk statement level and reports can be generated on them ([link](https://www.servicenow.com/docs/r/washingtondc/governance-risk-compliance/grc-risk-management-workspace/risk-rollup-ara-concept.html)).

D. Best practices video tutorials for your Risk Management adoption ([link](https://www.servicenow.com/community/grc-articles/best-practices-videos-tutorials-for-your-irm-risk-management/ta-p/3397311))

E. In ServiceNow, once a Risk Assessment Methodology (RAM) is being used by active assessments, it cannot be moved back to Draft because the system protects historical data and scoring integrity. The recommended and safest approach is not to force any changes on the existing RAM, but instead to create or clone a new version of the RAM and make the required factor updates there. The old RAM should remain published so that current assessments can finish without impact, while all new assessments automatically use the updated RAM. This versioning approach ensures historical data remains intact, audit reports stay accurate, and users experience a smooth transition without disruption.

## Assessment Template

### Overview

The AI Control Tower offers a robust suite of assessment tools, including the AI Impact Assessment, which evaluates AI use cases to identify potential risks such as copyright issues, bias, privacy breaches, misinformation, and surveillance. Additionally, the AI Control Tower provides AI Impact Assessments specifically designed for EU AI Act conformity.

The AI Impact assessment determines the mappings of the Risks and Controls to the AI Assets. These are outline in the risk mapping section below. This is triggered during the assess stage of the onboarding process of the AI Asset.

The AI Impact Assessment for Conformity is to ensure that high-risk AI systems do not pose harm to users, society, or the environment, and meet regulatory obligations as per the AI Act. This is triggered via the playbook during the pre-deployment checks.

### Key Value Benefits

- Offers an intuitive user experience
- Ensure information is accurate, easier to analyze, and drives better decisions on your risk program
- Assessments that used to take weeks to develop can now be created in hours or days

### Procedure

A. Create Assessment Template ([link](https://www.servicenow.com/docs/r/governance-risk-compliance/smart-assessment-engine/sae-asmnt-template-create.html))

B. Copy Assessment Template ([link](https://www.servicenow.com/docs/r/governance-risk-compliance/smart-assessment-engine/sae-asmnt-template-duplicate.html))

C. Scoring Assessment ([link](https://www.servicenow.com/docs/r/governance-risk-compliance/smart-assessment-engine/scoring-in-assessments.html))

D. Automate Response ([link](https://www.servicenow.com/docs/r/governance-risk-compliance/smart-assessment-engine/automate-response.html))

E. Post Assessment Automation ([link](https://www.servicenow.com/docs/r/governance-risk-compliance/smart-assessment-engine/impact-automation.html))

### Configuration

A. System-defined: AI Risk and Compliance ships with out-of-the-box risk assessment templates in Draft state to help organizations evaluate and manage AI-assets ethically and responsibly. These include:

| **Name** | **Description** |
| --- | --- |
| Fundamental Rights Impact Assessment for AI Assets (FRIA) | The Fundamental Rights Impact Assessment (FRIA) for AI assets is a systematic evaluation process designed to identify, assess, and mitigate potential risks that AI assets may pose to fundamental rights such as privacy, non-discrimination, freedom of expression, and due process. |
| High-risk AI assessment questionnaire | A structured set of targeted questions designed to evaluate AI systems classified as “high- risk” under regulatory frameworks. It captures details on intended use, potential harms, technical safeguards, and governance measures to ensure compliance and mitigate elevated risks before deployment. |
| AI impact assessment for EU AI Act conformity assessment | A specialized assessment template aligning with the EU AI Act’s conformity assessment requirements, focusing on risk classification, transparency obligations, human oversight, technical documentation, and post-market monitoring measures to demonstrate compliance readiness. |
| AI impact assessment | A general-purpose assessment template for evaluating the potential impacts of any AI system, covering ethical, legal, operational, and societal dimensions. It helps identify risks, assess likelihood and severity, and propose mitigation strategies across the AI lifecycle. |
| EU AI Act Conformity Assessment | A compliance-focused template that guides implementers through the formal steps required under the EU AI Act to assess, document, and verify conformity for AI systems— especially high-risk ones—ensuring that all mandatory controls, documentation, and testing are in place. |
| Fundamental Rights Impact Assessment for High-Risk AI Systems (FRIA) | An assessment specifically aimed at identifying and evaluating potential impacts of high- risk AI systems on fundamental rights, including privacy, non-discrimination, freedom of expression, and access to services. It ensures human rights considerations are integrated into AI governance processes. |
| AI Impact Assessment on AI asset inventory | A template that links impact assessments directly to the organization’s AI asset inventory, enabling risk evaluations to be tracked at the individual system or model level. This supports lifecycle governance by maintaining up-to-date compliance status for all AI assets. |

Create ([link](https://www.servicenow.com/docs/csh?topicname=smart-assessment-engine-cf-config.html&version=latest)): Building AI Impact Assessment templates involves designing standardized, reusable assessment forms within the AI Risk & Compliance solution to evaluate the ethical, legal, operational, and societal impacts of AI systems. These templates ensure assessments are consistent, aligned with regulatory requirements, and adaptable to various AI risk levels and use cases. By predefining sections for risk identification, impact categories, mitigation measures, and approval workflows, organizations can streamline evaluation processes, improve governance quality, and maintain an auditable record of AI risk decisions.

> **[Figure 7 — p.98]** Assessment Workspace, AI impact assessment > Questions tab: Question 1 editor ('Does your AI system use personal data?') with the section tree on the left, Yes/No choices, and question description / guidance panels.

A. Publish ([link](https://www.servicenow.com/docs/csh?topicname=publish-the-assessment-templates.html&version=latest)): When creating a new AI system or updating an existing one, publish the assessment templates before initiating the required assessments such as impact assessment and conformity assessment. You must publish an assessment template so that the assessments can be initiated.

B. New Action Type creation for Post Assessment Automation: The action types used in a post automation rule are sub-flow created in flow designer. For a new action type, user will need to create their own flow first and this flow should have the following items present for it to work similar to current flows present in the demo data (refer the existing sub-flows for more understanding: Map AI Risk Statements to AI System, Map AI Control objectives to AI System, Map Use and Purpose to AI system):
1. Inputs on the sub-flow:
- `Required: Reference to the AI asset task record (Assessment record)`

Any kind of input required for that specific automation. Example is the List of risk statement references in the below image.
1. Open All Navigation -> Process Automation -> Flow Designer
2. Select the “Subflows” pill.
3. Click on “New” -> “Subflow” (Search for one of the existing subflows mentioned above for reference, if required.)
4. Inputs on the sub-flow:
- a. Required: Reference to the AI asset task record (Assessment record)
- b. Any kind of input required for that specific automation. Eg: List of risk statement references in the below

> **[Figure 8 — p.99]** Flow Designer 'Subflow Inputs & Outputs' panel showing two inputs — Risk statements list (List Risk Statement) and AI assessment record (Reference to AI asset task) — both mandatory, with no outputs defined.

2. Mapping logic: A task action record needs to be created for each automation, this record is used for mapping the records selected in the automation rule to the AI asset record, once the assessment is reviewed and marked as closed complete. The records which are needed to be mapped are added to the payload. For further understanding, refer the existing sub-flows to understand how the payload is created.

> **[Figure 9 — p.99]** Flow Designer ACTIONS pane for a subflow: a 'Create Task action Record' step with Action Inputs (Table, Fields, Action = MAP_RS_TO_AIS, Task, Payload, Smart assessment instance), annotated to explain that the action name must be unique per new action type.

3. Mapping the assessment category to the sub-flow: Select the sub-flow category as AI Risk and Compliance.

> **[Figure 10 — p.100]** Workflow Studio 'Map AI Risk Statements to AI System' subflow with the Subflow properties dialog open — Description, Application (AI Risk and Compliance Management), Accessible from (All application scopes) and Category (AI Risk and Compliance, highlighted in red).

4. Post assessment review script logic: Add the logic to process the task action payload data on completion of assessment in the following method: Script include -> AIGovernanceAssessmentUtilsBase -> processDataOnAssessmentClosure (Refer to other methods like: _createControls, _createRisks, _updateUseAndPurpose)

C. Configure Post Assessment Automations ([link](https://www.servicenow.com/docs/csh?topicname=impact-automation.html&version=latest)): The mappings of both risk and controls can be configured depending on the requirements of the client. To amend these mappings will need updates to the assessment configurations. For adding a new post assessment automation (automation rule), follow the following steps:
- For creating new automations, the assessment templates should be published
- If planning to use a custom action type, make sure the category is mapped in the new sub-flow created
- Open the published template where new automations are to be added, in the Assessment Workspace
- In the Automations tab, click on Create automation
- Add the Name and Description for the automation in the modal and click Create. A new draft automation will be added.

> **[Figure 11 — p.101]** Assessment Workspace > AI impact assessment > Automations tab with 'Create automation' highlighted and the empty-state 'Select or create an automation' panel; the left list shows Demo Automation, Map Privacy Controls, Non-discrimination and fairness, Privacy control objectives mapping, Risk statements mapping, Transparency and accountability.

- Set response-based condition for when an automation should be triggered.

> **[Figure 12 — p.101]** Automations tab for 'Demo Automation' with red annotations pointing to 'Set condition' (add a question-based condition) and 'Set action' (select action type and inputs), plus buttons to add a conditional or standalone action set.

> **[Figure 13 — p.102]** 'Set conditions' modal for an automation: a Response based condition on Section 'Non-Discrimination and Fairness' with a dropdown listing the available assessment sections and their questions.

- Select the action type after clicking on Set action, once the action type is selected; the input fields for the specific action will be visible.

> **[Figure 14 — p.102]** 'Set actions' modal for Demo automation with Action type 'Map AI Risk Statements to AI System' and empty Risk statements list / AI assessment record inputs.

- Map the assessment record from the Scope based fields as shown below:

> **[Figure 15 — p.103]** 'Set actions' modal with the AI assessment record field being populated from a Scope based > AI asset task reference (highlighted in red), showing the reference picker.

Once every input is set, close the modal and activate the automation. Going forward, every assessment created using this template will trigger the automation if the condition to trigger it is fulfilled.

D. Post Assessment Automation > Action Type (Risk Statement Mapping) ([link](https://www.servicenow.com/docs/bundle/yokohama-governance-risk-compliance/page/product/assessment-engine/concept/impact-automation.html)): The mapping of risks to the AI Asset is determined by the answers to the questions in the AI Impact assessment. The workflow utilizes the automation capabilities built into the smart assessment engine to initial actions/ sub flows to map the risks to the entity created. Action Type - Map AI Risk Statements to AI System.

> **[Figure 16 — p.103]** Close-up of the published 'AI impact assessment for Related Entity, AI system task' header with General / Questions / Automations tabs and four Active automations: Non-discrimination and fairness, Privacy control objectives mapping, Risk statements mapping, Transparency and accountability.

- The configurations of these are shown here:

> **[Figure 17 — p.104]** 'Risk statements mapping' automation showing Action set 1: a filter condition (Response based > Section: Privacy and Data Protection > 'Does your AI system use personal data?' is Yes) mapped to the action 'Map AI Risk Statements to AI System'.

- The mapping of risks is shown here:

> **[Figure 18 — p.104]** Expanded 'Set actions' dialog for the Risk statements mapping automation, with Action type 'Map AI Risk Statements to AI System' and the full Risk statements list as chips — Operational Continuity and Downtime, Unintended Consequences, Reputational Damage, Regulatory Non-compliance, Privacy Violations, Overfitting and Underfitting, Model Poisoning, Model Performance Degradation (Model Drift), Lack of Transparency and Accountability, Lack of Transparency and Explainability, Inadequate Data Protection, Failure to Address Ethical Standards, Data Security, Data Bias, Data Integrity, Algorithmic Bias and Discrimination, Data Breaches and Theft, Adversarial Attacks, Unauthorised Access to AI Models — and the AI assessment record set to Scope based > AI asset task.

E. Post Assessment Automation > Action Type (Control Objective Mapping) ([link](https://www.servicenow.com/docs/bundle/yokohama-governance-risk-compliance/page/product/assessment-engine/concept/impact-automation.html)): The mapping of controls to the AI Asset is determined by the answers to the questions in the AI Impact assessment. The workflow utilizes the automation capabilities built into the smart assessment engine to initial actions/ sub flows to map the controls to the entity. Action Type - Map AI Control objectives to AI System.

> **[Figure 19 — p.105]** 'Transparency and accountability' automation showing Action set 1 with a response-based filter on the Transparency and Accountability section ('Can the decisions made by your AI system be explained in a way that is understandable to a non-expert?' = No) mapped to 'Map AI Control objectives to AI System'.

> **[Figure 20 — p.105]** 'Set actions' dialog for the Transparency and accountability automation with Action type 'Map AI Control objectives to AI System' and control objective chips (Interpret AI System Output, Design/Test Metrics, Practise Measurement Effect) plus the Scope based AI asset task reference.

F. Download Assessment Templates
1. Login as Admin
2. For Assessment Templates, go the ALL (Application Navigator) – search ‘sn_smart_asmt_question.list’

> **[Figure 21 — p.105]** Platform list view of Assessment Metric Template questions with the 'Assessment template' column highlighted, alongside Active, Allow multiselect, Attachment mandatory, Columns to display, Filter condition, Data type, Display field, Enable attachment and Enable justification columns.

3. Set Key Reporting Columns for Extraction (Ex: Assessment template, Section, Display name, Question type)
4. From there, you should be able to export into the following formats (link)

> **[Figure 22 — p.106]** Same questions list with the context menu open on the Export option, showing Export > Excel / CSV / XML / JSON / PDF sub-options for extracting the assessment question configuration.

> [!note] Note
> · The identification of risks and controls for AI systems or assets is conducted through Post Assessment Automation Rules. The configuration process involves mapping assessment questions to the risk and control library, which should be thoroughly reviewed and aligned with the specific requirements of the enterprise and the AI use case. This approach facilitates the provision of relevant risks and controls based on assessment responses.

- When creating a new AI system or updating an existing one, publish the assessment templates before initiating the required assessments such as impact assessment and conformity assessment. You must publish an assessment template so that the assessments can be initiated.
- Currently conditional visibility is only for questions and not sections.
- If the template is unpublished, you can certainly make changes. Once it is published, it is recommended to create a copy and then apply post-automation changes.

## AI Risk & Compliance Onboarding Lifecycle

AI Control Tower enforces a structured lifecycle to ensure AI initiatives cannot bypass governance controls. A step-by-step way of managing AI. It breaks the whole thing down into a multi-stage lifecycle to make sure governance is part of the process from beginning to end.

The lifecycle actively governs or clarifies where you are in your AI journey:
- Asset: Where do we track AI assets today and where do we want to do so in the future (e.g., spreadsheets, integrations, etc.)? What actions are allowed? What are all the AI capabilities inside the enterprise?
- Lifecycle: What is in the AI Asset pipeline? How do you discover new AI assets? What mechanisms are in place to retire inventory safely? When can AI move to production? Which tasks must be completed? Did we approve attrition prediction?
- Risk: What potential risks and regulations do we need to manage for? Do we have a team in place to track this? Are we compliant with EU AI Act? Are we adhering with latest AI governance/ regulations/ frameworks or standards?
- Operations: How do we monitor AI incidents? (e.g., hallucinations, model drift) and track customer cases?
- Value: Who is using what AI? How do we measure AI productivity? What appears on dashboards?

> **[Figure 23 — p.107]** 'AI Control Tower Solution Overview' diagram — 'Ethically and responsibly manage AI throughout its life cycle' — laying out the Demand, Build & Validate and Deploy/Monitor/Assess Value phases across the Intake, Assess, Build & Test, Pre-deployment Review, Monitor and Value columns, with each activity tagged as AICT, AIRC or SPM, and the AI Lifecycle Governance / AI Risk & Compliance bands at the bottom.

## Initiate AI System Intake & Explore the AI Control Tower

### Overview

It all starts in a central idea portal where anyone in the company can submit their ideas for AI projects. This usually connects to ServiceNow's Innovation or Demand Management tools. The point is to capture every single potential use case, from a new marketing chatbot to a predictive model for the finance department, all in one place.

| **What it is** | **A service catalog request form submitted by the Business Owner through the Employee Center to register a new AI system or use case model or dataset** |
| --- | --- |
| What it does | Creates the AI System/Dataset or Model record in ServiceNow in Draft state. Collects identifying information - who owns it, what it does, what type of AI, process compliance checks. Kicks off the governance workflow so the AI Steward can begin review |
| Who does it | Business Owner or Product Owner - submitted at the very beginning of the process before any review starts. |
| Output | AI System record created in Draft state. AI COE notification sent. Record visible in AI Steward workspace. Other states can be chosen but for the purposes of the lifecycle they will only be in draft state since we haven’t gone through the lifecyle yet. |

### Procedure

Requesting an AI Use Case: This ensures AI initiatives originate from real business needs rather than ad-hoc experimentation.

Request new AI Asset from Employee Portal ([link](https://www.servicenow.com/docs/r/governance-risk-compliance/ai-risk-management/request-ai-system.html))

### Configuration

A. Intake Request – Use & Purpose Deterministic Evaluation/ Risk-based AI System Classification

The “Use & Purpose” section is designed to help the AI Product Owner clearly articulate the overall objective, functional scope, and operational characteristics of the AI system at the Intake stage. Through structured screening questions—covering intended outcomes, usage areas, output types, impacted stakeholders, human involvement, interaction model, and system autonomy level—the section ensures a consistent and comprehensive understanding of how the AI solution will function within the organization.

This structured input enables early transparency regarding the AI system’s role, boundaries, and impact.

Below table outlines the system-defined screening questions applied during AI system intake request submission:

| **Field** | **Type** | **Choice** | **Tooltips** |
| --- | --- | --- | --- |
| Intended Outcome of the AI System | Single Select | Not Applicable [0] Efficiency Boost [1] Quality Enhancement [1] Decision Guidance [1] Automation of Tasks [2] Customer Experience Upgrade [2] Insight Generation [3] | Identifying the purpose ensures the AI aligns with expected business outcomes. |
| Area Where the AI System Is Used | Multi- Select | Not Applicable [0] Internal Operations [1] Customer Services [1] Sales & Marketing [2] Finance & Accounting [2] IT & Security [2] Supply Chain [2] HR & Workforce [3] External Partner Ecosystem [3] | Different areas have different expectations, visibility, and user needs. |
| Type of Output Produced | Multi- Select | Not Applicable [0] Simple Alerts [1] Insights & Summaries [1] Rankings & Scores [2] Recommendations [2] Generated Content [2] Automated Decisions [3] System Actions [3] | The output determines how users interpret the system’s results and actions. |
| People Affected by the AI System | Multi- Select | Not Applicable [0] Internal Team [1] Specific Customer Groups [1] General Customer Base [2] External Partners [2] Public or Large Audiences [3] | The scope of impact influences expectations around clarity and dependability. |
| Level of Human Involvement | Single Select | Not Applicable, Full User Control, User-Guided with AI Support, Shared Control, AI-Initiated with User Approval, Fully Automated Workflow | This helps describe when and how people guide or confirm AI activities. |
| Data Used by the System | Multi- Select | Not Applicable, Public or General Info, Business Operational Data, Customer Interaction Data, Behavioral or Usage Data, Profile or Account Data, Sensitive Business Data | Different kinds of data shape how the system processes inputs and produces outputs. |
| Interaction Type With End Users | Single Select | Not Applicable, No Direct Interaction, Background Support, Notifications & Prompts, Chat-Based Interaction, User-Facing Recommendations, Interactive Experience | More direct interactions call for clearer expectations about responses or guidance. |
| System Autonomy Level | Single Select | Not Applicable, Assistive (AI suggests), Semi-Automated (AI acts with confirmation), Condition-Based Automation, Event- Triggered Automation, Fully Automated Execution | Autonomy level helps describe how much the system acts on its own. |

B. Intake Request – Configure Screening Questions

For capturing use and purpose of a AI system asset, a record is created in Al asset use and purpose (sn_ai_governance_asset_use_purpose), for adding a new use and purpose field, user will need to follow these steps:
1. Create the new field on the AI : A new integer (single select)/List (multi-select) field needs to be created in the Al asset use and purpose (sn_ai_governance_asset_use_purpose) table, add choices to these field with the response as label and some numeric value, which can be used for risk factor calculations.

> **[Figure 24 — p.109]** Platform Table definition form for the 'AI use case and purpose' table (`sn_ai_governance_asset_use_purpose`) in the AI Control Tower Core application, with the Table Columns dictionary list showing column labels, types, references, max length, defaults and mandatory flags.

2. Add field to the record producer (Request an AI use case intake form): In the navigation Service Catalog -> Catalog Definition -> Record Producer, open the Request an AI use case record and click on the Edit in Catalog Builder action.

> **[Figure 25 — p.109]** Record Producer form 'Request an AI use case' — Table name (AI System Digital Asset), Application (AI Risk and Compliance Management), Active, State Published, plus the short/full description rich-text editor on the 'What it will contain' tab.

3. Add a new question in the Use and purpose section for the new field added in the Al asset use and purpose (sn_ai_governance_asset_use_purpose) table. Refer to the existing dropdown/multi-choice questions present for existing table fields. Note the variable name created for the new question, as it will be required to map the question response to the record’s field.

> **[Figure 26 — p.110]** Catalog Builder view of the 'Request an AI use case' record producer, Questions step, with the 'Use and purpose' container highlighted and the 'Insert component' panel open (New question, Question set, Downloaded questions, Single-column container, Line break).

4. Map the question response to the record’s field: Open the record producer record and update the Post insert script logic as shown in the image below:

> **[Figure 27 — p.110]** Record Producer script editor showing the onSubmit/producer server-side script that instantiates a GlideRecord on the product model table and sets fields (`model_category`, `manufacturer`, intended outcome, usage detail, data used, interaction type, autonomy level, etc.), with the key mapping block outlined in red.

B. Update Assessment Template

Update Fundamental Rights Impact Assessment for AI Assets (FRIA) smart assessment template (if being used): This template has use and purpose related questions for the existing fields of the Al asset use and purpose (sn_ai_governance_asset_use_purpose) table. For the new custom field, a new question and corresponding automations will be required, to handle the field mapping based on the assessment response. Refer to the existing questions, in the Use and purpose section and there corresponding automations with Action type: Map Use and Purpose to AI system.

C. Update Automated Risk Classification/ Risk Scoring Logic

In the new Automated risk classification for AI system RAM, there are 6 automated risk factors
1. Update automated risk calculation logic (if the RAM is being used):
2. Open Automated risk classification for AI system RAM record by navigating AI risk and compliance -> Risk assessments -> Risk Assessment Methodologies
3. Open Inherent Assessment record in the Assessment Types related list.
4. Currently we have provided 6 risk factors, these have scripted logic present based on the OOTB fields. Refer the existing logic for understanding the current implementation and update it according to the requirement.

> [!note] Note
> · To make change or corrections to system-defined flows/ sub-flows, create a copy version for upgrade safety measures.

- The responses from the screening questions collected during the AI system Intake Request are aligned with the Impact Assessment [Fundamental Rights Impact Assessment for AI Assets (FRIA)]. After the assessment, automation maps the use and purpose to the AI system, applying relevant risk factors to determine the Regulatory Risk Classification or Risk Tiering for the requested AI system.
- Risk score is only calculated when an AI system is Managed

## Assess – Evaluate AI Use Case Impacts

### Overview

Once an AI asset is submitted, it does not move forward right away. First, it goes through a formal assessment to check its feasibility, potential value, and any risks involved. This is where people with titles like "AI Steward" or "Risk and Compliance Analyst" step in. They review the proposal to make sure it aligns with company policies and external regulations, like the NIST AI Risk Management Framework or EU AI Act.

| **What it is** | **A smart questionnaire answered by the Business Owner after the AI Steward clicks Start Review. It uses if-then logic to automatically attach control objectives and risk statements to the AI System record based on each answer.** |
| --- | --- |
| What it does | Determines WHICH controls apply to this AI system and WHICH risks need to be managed. Each answer triggers specific control objectives and risk statements via automation. |
| Who does it | Business Owner — triggered after AI Steward clicks Start Review. |
| Output | Control objectives and risk statements attached to AI System record. Control attestation tasks automatically generated. Note: Setup Automation Rules as per enterprise preference to identify applicable risk statements and control objectives. |

Reviewing and Governing the Use Case: An AI Accountable Officer (typically aligned with AI Stewardship) reviews the request, assigns required assessments (e.g. FRIA) to an AI Asset Owner. The response answered in reference to FRIA by the AI Asset Owner will determine the applicability of Risk Statements and Control Objectives.

### Procedure

A. Lifecycle Flow: Perform Impact Assessment: Once the AI asset is managed for risk & compliance evaluation, further onboarding lifecycle tasks are triggered and assigned to various stakeholders for response collection and collaboration. These tasks can be accessed from the AI Control Tower Workspace, the Risk Portal, or the Reports/ Dashboards
- Respond to Impact Assessment by AI Product Owner from AI Control Tower Workspace > Tasks

> **[Figure 28 — p.112]** AI Control Tower workspace home page 'Welcome to AI Control Tower' — My overview with three donut widgets (Assets by AI type, Assets by lifecycle status, AI cases by state) and a Tasks/Cases list showing an open Impact assessment task.

- Respond to Impact Assessment by AI Product Owner from Risk Portal > Tasks > My pending tasks > AI asset tasks

> **[Figure 29 — p.112]** GRC Portal home page (Service Portal) with 'My to-dos' 25 open / 15 overdue / 16 new / 9 in progress, 'My teams' to-dos' and a Related resources panel linking to My requests, Risk resources and Service Portal.

> **[Figure 30 — p.113]** GRC Tasks workspace Tasks list, My pending tasks tab, AI asset tasks filter — two rows for Classic attestations and an EU AI Act conformity impact assessment on Generative AI assets, both Assigned, priority 2 - High.

- o Respond to Impact Assessment by AI Product Owner from AI Asset

> **[Figure 31 — p.113]** AI Control Tower asset record 'ServiceNow Email Assistant AI Agent for Corporate 1.0' on the Lifecycle tab, Assess phase, showing the AI Asset Onboarding stepper (Assess / Build and test / Deploy) and four open Assess tasks including Impact assessment and Architecture review.

- Respond to Impact Assessment (Acknowledge) by AI Product Owner

> **[Figure 32 — p.113]** AI Control Tower task form for the 'Impact assessment' task (TASK0022695) with Priority 2 - High, State Open, Assigned to Val Osborne, and Take assessment / Save buttons.

- Respond to Impact Assessment (Welcome) by AI Product Owner

> **[Figure 33 — p.114]** Assessment landing page 'Hi, Val — Welcome to the AI assessment' for the ServiceNow Email Assistant AI Agent for Corporate 1.0 AI impact assessment, with the assessment description, Reassign / Start buttons and a Compose / Activity stream on the right.

- Respond to Impact Assessment (Instructions) by AI Product Owner

> **[Figure 34 — p.114]** AI impact assessment Instructions page listing the eight evaluation areas (identify the AI system; assess privacy and data protection; ensure non-discrimination and fairness; assess transparency and explainability; verify human oversight; review impact on freedom of expression and information; monitor and mitigate risks; document and report), with the section tree on the left and a Details panel showing scope, AI asset task and dates.

- Respond to Impact Assessment (Completed) by AI Product Owner

> **[Figure 35 — p.115]** AI impact assessment 'Privacy and Data Protection' section with a submit confirmation modal — 'I have reviewed my answers. I understand I may no longer be able to edit the answers after submitting.' — over the answered questions.

B. Flow: Review Impact Assessment
- Review Impact Assessment response by AI Risk & Compliance Manager from AI Risk & Compliance Workspace > Operations > AI System in Assess state

> **[Figure 36 — p.115]** AI Risk and Compliance Workspace home, Operations tab: 'AI systems by state' counters (New 19, Assess 19, Build 2, Review for deployment 2, Live and Monitor 5, Offboard 0) beside an 'AI systems by department' bar chart.

- Review Impact Assessment response by AI Risk & Compliance Manager from AI Risk & Compliance Workspace > Operations > AI Assessments in Review state

> **[Figure 37 — p.116]** AI Risk and Compliance Workspace Assessments view with Risk assessments tiles (33 Open, 33 Overdue, 0 Due in 7 days) and a completion donut, alongside AI assessments tiles (17 Open, 10 Overdue, 1 Due in 7 days) and a status donut by Draft / Assigned / Work in progress / Review.

> **[Figure 38 — p.116]** AI Risk and Compliance Workspace 'AI assessments' list view with a single row (AIA0001054) showing Priority, State Review, Assigned to, Asset type Generative AI, Name, Related entity and Assessment template columns.

Review Impact Assessment response by AI Risk & Compliance Manager from AI Asset > AI Assessments

> **[Figure 39 — p.116]** AI asset record for 'ServiceNow Email Assistant AI Agent for Corporate 1.0' in the AI Risk and Compliance Workspace, AI assessments related list, with the left navigation tree (Overview, Related to: AI models / Datasets / Related entities, Applies to: Risks / Controls, Assessments: AI assessments / Risk assessments / Regulatory risk assessments / Bulk risk assessments).

- Review applicable Risk Statements and Control Objectives based on the response to each question. For more details, refer to the Post Assessment Automation Rule topic.

> **[Figure 40 — p.117]** AI impact assessment record, Outcomes tab, 'Preview outcomes' > Control objectives: three generated objectives (Collect and Analyse Data, Analyse Field Data, Ensure Data Quality) with Description, Classification (Detective / Preventive), Active flag and Compliance score.

Acknowledge for further Risk & Compliance evaluation by marking Update State as Closed Complete

> **[Figure 41 — p.117]** AI impact assessment record with the 'Update state' modal open, State set to 'Closed complete' plus an Additional comments box, over the assessment summary showing Draft/Assign/Review/Closed progress, control objectives (3) and risk statements (19).

- Use View Assessment action to preview the response answered by the AI Product Owner

> **[Figure 42 — p.118]** AI impact assessment, Privacy and Data Protection section in the AI Risk and Compliance Workspace, showing answered questions on personal data and sensitive/special-category data with the Details side panel (scope, AI asset task, due date, priority).

- Reading Article ([link](https://www.servicenow.com/docs/r/governance-risk-compliance/ai-risk-management/perform-impact-assessment-of-ai-use-case.html))

C. Lifecycle Flow: Perform Risk Assessment
- AI Steward View

> **[Figure 43 — p.118]** AI Control Tower asset record on the Lifecycle tab, Assess phase, with five tasks listed (Perform risk assessment, Architecture review, Collaboration for security clearance, Collaboration with legal team, Impact assessment) and a 'Mark as complete' button.

- Respond to Risk Assessment by AI Risk & Compliance Manager from Risk Portal > GRC Tasks > My pending tasks > Risk assessments

> **[Figure 44 — p.119]** GRC Tasks workspace Tasks list filtered to Risk assessments, showing one risk assessment (RASMT0010112) whose assessable entity is the ServiceNow Email Assistant AI Agent for Corporate 1.0, State New.

- Respond to Risk Assessment by AI Risk & Compliance Manager from AI Risk & Compliance Workspace > Tasks > My pending tasks > Risk assessments

> **[Figure 45 — p.119]** AI Risk and Compliance Workspace Tasks list, Risk assessments filter, showing the same 'All - Risk assessments' row with Applies-to entity tooltip, Risk, Status, Start date and Due date columns.

- Respond to Risk Assessment by AI Risk & Compliance Manager from AI Risk & Compliance Workspace > AI Asset > Regulatory Risk Assessments

> **[Figure 46 — p.119]** AI asset record with the 'Regulatory risk assessments' related list selected, showing assessment RASMT0010112 with Risk assessment methodology 'Risk classification for AI system', Applies to record, Inherent risk and Control effectiveness columns.

- Respond to Risk Assessment by AI Risk & Compliance Manager from AI Risk & Compliance Workspace > Operations > Risk Assessments > New

> **[Figure 47 — p.120]** AI Risk and Compliance Workspace Assessments view after a new assessment was created — Risk assessments now 34 Open / 33 Overdue / 1 Due in 7 days with a 34-assessment donut, beside AI assessments 16 Open / 10 Overdue / 1 Due in 7 days.

Respond to Risk Assessment (Welcome) by AI Risk & Compliance Manager

> **[Figure 48 — p.120]** Risk assessment record 'Related Entity: ServiceNow Email Assistant AI Agent for Corporate 1.0' (methodology: Risk classification for AI system, due in 5 days, assessor Josh Warner, State New) with Start assessment and Reassign buttons.

- Respond to Risk Assessment (Completed) by AI Risk & Compliance Manager

> **[Figure 49 — p.120]** Regulatory risk classification questionnaire for the AI Based Credit Scoring for Loan Approvals asset — the Impact section with contribution factors Operational Impact to Business, Number of business impacted and Financial Impact, each rated High, and a qualitative weight of 100%.

> **[Figure 50 — p.121]** Same regulatory risk classification, scrolled to 'Other factors' (Likelihood = Likely) and the Scoring section showing the computed regulatory risk classification result.

> **[Figure 51 — p.121]** Completed risk assessment for the Email Assistant AI Agent: Impact 100% qualitative weight, computed regulatory risk classification High (9.00), an 'I would like to change the computed score' checkbox and priority comments 'Risk Assessment Completed', with Submit / View summary buttons.

D. Lifecycle: Architecture review for AI use case [AI Steward View]

> **[Figure 52 — p.122]** AI Control Tower Lifecycle > Assess tab with three of five tasks ticked (Architecture review, Collaboration for security clearance, Collaboration with legal team) and Impact assessment already Completed, ready for 'Mark as complete'.

> **[Figure 53 — p.122]** AI Control Tower home overview with the three donut widgets and a Tasks list of three 1-Critical open tasks (Collaboration with legal team, Collaboration for security clearance, Architecture review) for the Email Assistant AI Agent.

- Assigned to AI Product Owner as a reminder notice for further review and collaboration with cross-functional workstreams such as Architects. This lifecycle task is intended for demonstration purpose only.

> **[Figure 54 — p.123]** Task form 'Architecture review for AI use case' (TASK0022698, Onboarding task, 1 - Critical) showing the full description of the architecture-review responsibilities and the State dropdown open with Open / In progress / Completed / Closed skipped.

E. Lifecycle: Collaboration for security clearance on AI use case development. Assigned to AI Product Owner as a reminder notice for further review and collaboration with cross-functional workstreams such as Security. This lifecycle task is intended for demonstration purpose only.

> **[Figure 55 — p.123]** Task form 'Collaboration for security clearance on AI use case development' (TASK0022697) with description, parent approval record, priority 1 - Critical, assignee Val Osborne and State Open / Status Requested.

F. Lifecycle: Collaboration with legal team for AI use case. Assigned to AI Product Owner as a reminder notice for further review and collaboration with cross-functional workstreams such as Legal. This lifecycle task is intended for demonstration purpose only.

> **[Figure 56 — p.124]** Task form 'Collaboration with legal team for AI use case' (TASK0022696) with the equivalent legal-clearance description, parent approval record and Open / Requested state.

### Configuration

A. For more details to modify Flow and associated Sub-Flows belonging to Assess phase, refer to the Govern - Lifecycle topic.

> [!note] Note
> To make change or corrections to system-defined flows/ sub-flows, create a copy version for upgrade safety measures

## Build and Test – Implement Controls

### Overview

After an AI asset is assessed and approved, it heads to the development phase. Here, data scientists and developers get to work building and testing the AI asset. The AI Control Tower functions as a project management tool, keeping track of progress, collecting documentation, and logging test results. The focus is on creating a detailed audit trail for compliance.

Design & Develop Controls: Control attestation is a formal process where business units or system owners confirm—via structured surveys or smart assessments—that required governance, technical safeguards, and compliance measures are implemented and effective for each AI system. This is particularly vital for high-risk AI under emerging regulatory frameworks (e.g., EU AI Act, NIST AI RMF, ISO/IEC standards).

The final review checkpoints before deployment, how conformity assessments validate readiness, and how AI Control Tower supports monitoring after launch. Final production approval is granted. Monitoring, adoption, and value tracking begin.

Before AI can go live, it must pass one last review and approval workflow. A whole cast of characters, from legal and security to business leaders must sign off. They must confirm that every governance box has been ticked. Only after getting all the approvals the model can be deployed.
1. Lifecycle Flow: Review issues, policy exception, control attestation and detailed risk assessment
2. Lifecycle Flow: Conformity assessment

| **What it is** | **A task assigned to the Business Owner to provide evidence that a specific control objective has been met for their AI system.** |
| --- | --- |
| What it does | The Business Owner reviews each control objective attached to their AI system, confirms whether it is in place, and provides evidence. Happens in the Build and Test phase. |
| Who does it | Business Owner — one attestation task per attached control objective. |
| Output | Control Effectiveness score: Effective (100%) / Needs Improvement (60-100%) / Ineffective (below 60%). |

Choice of Attestation Method:
- Platform Survey (Classic): Useful for broad, organization-wide attestation cycles with standardized questions and consistent scoring, suitable for tracking maturity and compliance baselines.
- Smart Assessment: Ideal for adaptive, risk-driven assessments where the questionnaire adjusts dynamically based on responses, allowing deeper focus on higher-risk areas without overburdening low-risk asset owners.

### Procedure

A. Create Control Attestation: During the Build & Test phase, a Lifecycle Task called "Create Control Attestation" is assigned to the AI Risk and Compliance Analyst. Their role is to scope relevant controls and initiate the Attestation Request, essentially reminding them to create Control Attestations.

> **[Figure 57 — p.125]** AI Control Tower Lifecycle tab with Assess complete and Build and test in progress: the Development plan lists four tasks (Perform control attestation, Implement value templates to derive usage and adoption metrics, Collect information on the deployment regions of the AI system, Create control attestation) and a collapsed Pre-deployment assessments section.

- Work on assigned request by AI Risk & Compliance Manager from AI Risk & Compliance Workspace > Tasks

> **[Figure 58 — p.126]** AI Risk and Compliance Workspace Tasks list, AI asset tasks filter, showing a 'Create control attestations' task (AIA0001164) for a Generative AI asset, Assigned, 4 - Low, owner Josh Warner.

- Monitor assigned request by AI Risk & Compliance Manager from Risk Portal > Tasks >

> **[Figure 59 — p.126]** GRC Portal home page with My to-dos at 62 total tasks — 62 open, 53 overdue, 44 new, 18 in progress.

> **[Figure 60 — p.126]** GRC Tasks workspace Tasks list, AI asset tasks filter, showing the 'Create control attestations' task (AIA0001164) for a Generative AI asset.

- Work on assigned request for control attestation by AI Risk & Compliance Manager

> **[Figure 61 — p.127]** 'Create control attestations' AI asset task record in the AI Risk and Compliance Workspace showing the five-stage state tracker (Draft Completed, Assigned In progress, Work in progress, Review, Closed) with Update state and Accept work buttons.

- Work on assigned request for control attestation > Scope Key Controls by AI Risk & Compliance Manager

> **[Figure 62 — p.127]** AI asset record 'ServiceNow Email Assistant AI Agent for Accounting & Finance' with the Controls related list open — five controls (Collect and Analyse Data, Analyse Field Data, Ensure Data Quality, Establish Risk Acceptance Criteria, Establish Risk Management Framework) with Attestation method, State Draft, Classification and Owner — plus the 'Add controls from control objective' button.

- Complete creation of Control Attestation by AI Risk & Compliance Manager

> **[Figure 63 — p.128]** 'Create control attestations' AI asset task with the Update state modal open (State = Closed complete, Additional comments) and the activity stream showing the state change history.

B. Perform Control Attestation: This task is then assigned to the Product Owner or Submitter of the AI Asset request, triggered once the previous task (Create control attestation) is completed. Control owners, business users, or Product Owners can work on their assigned Control Attestation Request either from Risk Portal or AI Control Tower Workspace

> **[Figure 64 — p.128]** AI asset record with the AI asset tasks related list showing three tasks: Create control attestations (Closed complete), Share deployment details of the AI system (Assigned) and Perform control attestation (Assigned).

- Using Classic Survey from Risk Portal

> **[Figure 65 — p.129]** GRC Portal home page with My to-dos at 30 total tasks — 30 open, 15 overdue, 19 new, 11 in progress.

> **[Figure 66 — p.129]** GRC Tasks workspace Tasks list, Classic attestations filter, grouped by entity — three GRC Classic Attestation instances (Collect and Analyse Data, Ensure Data Quality, Analyse Field Data) for the Email Assistant AI Agent, all Ready to take.

- Using Classic Survey from AI Control Tower Workspace

> **[Figure 67 — p.129]** Assessment Instance record AINST0010016 (Metric type: GRC Classic Attestation, Assigned to Val Osborne, due 2026-03-18, expiration 2026-03-05) with Take assessment / Save / View user's response buttons.

> **[Figure 68 — p.130]** AI Control Tower home overview with the three donut widgets and a Tasks list containing the single open 'Perform control attestation' task (TASK0022706, 2 - High).

> **[Figure 69 — p.130]** Task form 'Perform control attestation' (TASK0022706, 2 - High, State Open, Status Requested) with an 'Accept work' button.

- Work Accepted

> **[Figure 70 — p.131]** The same 'Perform control attestation' task now In progress, with a 'Classic attestations (3)' related tab and a 'Ready for review' button.

- Individual Assessment

> **[Figure 71 — p.131]** 'Perform control attestation' task, Classic attestations tab, listing the three GRC Classic Attestation instances (Ensure Data Quality, Collect and Analyse Data, Analyse Field Data) all Ready to take, with a 'Group assessments' button.

- Individual Classic Attestation (Acceptance)

> **[Figure 72 — p.131]** Assessment Instance AINST0010017 opened from the task, showing Metric type GRC Classic Attestation, State Ready to take, assignee, due and expiration dates.

- Individual Classic Attestation (Response)

> **[Figure 73 — p.132]** 'Take Assessment' modal for the GRC Classic Attestation on control 'Ensure Data Quality' — 'Is the control implemented?' answered Not Applicable with a matching Explain field, and Submit / Save / Cancel buttons.

- Individual Classic Attestation (Completed)

> **[Figure 74 — p.132]** Assessment Instance AINST0010017 detail form (GRC Classic Attestation, Ready to take) reached from the control attestation task.

- Using Classic Survey in Group from Employee Portal

> [!note] Note
> For the “Perform Control Attestation” lifecycle task assigned to AI Product Owner with scoped set of Controls identified for Attestation, the user can selectively identify one or more number of controls to be grouped with similar response in bulk for ease of quick response completion.

> **[Figure 75 — p.133]** GRC Tasks workspace Tasks list, Classic grouped attestations filter, showing one grouped attestation instance (AINST0010020) Ready to take.

- Request for Grouping Classic Attestations in Bulk

> **[Figure 76 — p.133]** 'Perform control attestation' task, Classic attestations tab with the first attestation selected and the 'Group assessments' action available.

- Response Evaluation

> **[Figure 77 — p.133]** 'Group assessments' modal — Response type 'Same response for all attestations', Group by 'AI asset', with a Group previews panel showing Group 1 (Email Assistant AI Agent, GRC Classic Attestation, 2 assessments) and Cancel / Group buttons.

- Work on Grouped Classic Attestation Task (Ready to Accept)

> **[Figure 78 — p.134]** 'Perform control attestation' task with the new 'Classic grouped attestations' tab showing the single grouped instance AINST0010019 (GRC Classic Attestation, Ready to take).

- Work on Grouped Classic Attestation Task (Ready to Accept)

> **[Figure 79 — p.134]** Assessment Instance AINST0010019 — the grouped attestation instance — in Ready to take state with Take assessment / Save / View user's response buttons.

- Respond to Grouped Classic Attestation Task (Respond)

> **[Figure 80 — p.134]** 'Take Assessment' modal for the grouped attestation: 'Provide one response for all assessments', with the control-implemented question answered Not Applicable and a matching explanation.

- Acknowledgement Response

> **[Figure 81 — p.135]** Assessment Instance AINST0010019 after submission, showing the banner 'You have completed this attestation', State Complete and a 'View user's response' button.

- Submitted for Review

> **[Figure 82 — p.135]** 'Perform control attestation' task (TASK0022706) form view with State Open / Status Requested and the 'Accept work' button, showing task type and parent approval record.

- Review by AI Risk & Compliance Manager

> **[Figure 83 — p.136]** AI asset record, AI asset tasks related list, with 'Create control attestations' Closed complete and two remaining Assigned tasks (Share deployment details of the AI system, Perform control attestation).

- Review completed by AI RC Mgr.

> **[Figure 84 — p.136]** 'Perform control attestation' AI asset task with the Update state modal open (Closed complete) and the activity stream showing the assignment and state history.

- Using Smart Assessment from Employee Portal

Controls Applicability for GRC Attestation powered by Smart Assessment

> **[Figure 85 — p.137]** AI asset record, Controls related list, with 'Establish Risk Acceptance Criteria' and 'Establish Risk Management Framework' selected (Attestation method: Attestation, State Draft, Classification Preventive) and the Attest / Remove (2) actions available.

GRC Attestation Tasks assigned to AI Product Owner for Response

> **[Figure 86 — p.137]** AI Control Tower asset record, Risk & compliance tab, Attestations related list showing two GRC attestation instances (ASMT0001018, ASMT0001019) both Completed for user Val Osborne.

Respond to GRC Attestation Tasks by AI Product Owner from Risk Portal

> **[Figure 87 — p.138]** GRC Portal home page with My to-dos at 24 total tasks — 24 open, 11 overdue, 15 new, 9 in progress.

Respond to GRC Attestation Tasks by AI Product Owner from Risk Portal > Tasks > My pending tasks > Attestations

> **[Figure 88 — p.138]** GRC Tasks workspace Tasks list, Attestations filter, showing two GRC attestation instances (ASMT0001018, ASMT0001019) in Open state.

Respond to GRC Attestation Task powered by Smart Assessment by AI Product Owner

> **[Figure 89 — p.138]** 'GRC attestation' smart assessment for the control 'Establish Risk Acceptance Criteria' — question 1 'Is the control implemented?' answered No and question 2 'Explain' answered 'Needs improvement', with a Details panel showing scope, control, control objective, owner, key control, enforcement and classification.

Respond to GRC Attestation Task powered by Smart Assessment by AI Product Owner from AI Control Tower Workspace > AI Asset Record > Risk & Compliance > Attestations

> **[Figure 90 — p.139]** AI Control Tower asset record, Risk & compliance tab, Attestations related list with both attestation instances now Completed.

Work on Control Attestations powered by Smart Assessment in Group. For the “Perform control attestation” task assigned to AI Product Owner/ Requestor of the AI Use case; to simplify the respondent experience in sharing a similar attestation result to the applicable controls identified. Go to Attestations > Select Key Controls > Combine

> **[Figure 91 — p.139]** 'Perform control attestation' task, Attestations tab, with two GRC attestation instances (ASMT0001023, ASMT0001022) selected in Open state and a 'Combine (2)' button.

> **[Figure 92 — p.140]** 'Grouped Smart Attestation' assessment view: the left tree lists the two controls (Establish Risk Acceptance Criteria, Establish Risk Management Framework) and the GRC attestation questions ('Is the control implemented?' Yes/No/Not Applicable and Explain) with a Details panel and Next button.

C.. Review Control Attestation Results
- Review Control Attestation response by AI Risk & Compliance Mgr. from AI Risk & Compliance Workspace > Tasks > My group’s tasks

> **[Figure 93 — p.140]** AI Risk and Compliance Workspace Tasks list, My group's tasks tab, AI asset tasks filter, showing a 'Perform control attestation' task (AIA0001032) for a Generative AI asset in Review state.

- Review Control Attestation response by AI Risk & Compliance Mgr. from Risk Portal > GRC Tasks > My items > AI asset tasks

> **[Figure 94 — p.141]** GRC Tasks workspace Tasks list, My items tab, AI asset tasks filter, showing a mixed backlog of AI governance tasks — Data Governance Review, Product Owner Review for Market Fitment, Share deployment details, AI conformity assessment, High-risk AI assessment, Perform control attestation and credit-scoring EU AI Act conformity assessment — across AI dataset, Classic AI and Generative AI asset types.

D. Development Plan Lifecycle Task: Collect information on the deployment regions of the AI system. Assigned to AI Product Owner as a reminder notice for further review and collaboration with cross-functional workstreams. This lifecycle task is intended for demonstration purpose only.

> **[Figure 95 — p.141]** AI Control Tower Lifecycle tab, Build and test phase, with two of three Development plan tasks ticked (Implement value templates, Collect information on the deployment regions) and Create control attestation still open.

E. Development Plan Lifecycle Task: Implement value templates to derive usage and adoption metrics. Assigned to AI Product Owner as a reminder notice for further review and collaboration with cross-functional workstreams. This lifecycle task is intended for demonstration purpose only.

> **[Figure 96 — p.142]** AI Control Tower Lifecycle tab with the asset now 'Approved for deployment': all four Development plan tasks show Completed/Open states and the Deploy stage is active in the stepper.

F. Pre-deployment Lifecycle Task: Conformity assessment

> **[Figure 97 — p.142]** AI Control Tower Lifecycle tab, Build and test phase 'Ready for deployment', showing the Pre-deployment assessments section with two tasks — Conformity assessment and Review issues and policy exceptions.

- Respond to Conformity Assessment by AI Product Owner from Risk Portal > Tasks > My pending tasks > AI asset tasks

> **[Figure 98 — p.143]** GRC Tasks workspace Tasks list, AI asset tasks filter, showing the 'EU AI Act conformity assessment' AI asset task (AIA0001061) for a Generative AI asset, Assigned, 2 - High.

- Respond to Conformity Assessment by AI Product Owner from AI Control Tower Workspace > Tasks

> **[Figure 99 — p.143]** AI Control Tower home overview with the three donut widgets and a Tasks list containing the single open 'Conformity assessment' task (TASK0022724, 4 - Low).

- Ready to Take acceptance by AI Product Owner

> **[Figure 100 — p.143]** Task form 'Conformity assessment' (TASK0022724) with short description, parent approval record and a 'Take assessment' button.

- Respond to Conformity Assessment by AI Product Owner (Welcome)

> **[Figure 101 — p.144]** Assessment landing page 'Hi, Val' for the 'AI impact assessment for EU AI Act conformity assessment' on the Email Assistant AI Agent, with the assessment description explaining the structured EU AI Act conformity process, plus Reassign / Start buttons and the Activity stream.

- Response completion by AI Product Owner (In Progress)

> **[Figure 102 — p.144]** EU AI Act conformity assessment, 'Safety and Robustness' section — questions on reliability/robustness testing in high-stakes scenarios, safeguards to minimise harm (automated error detection, fallback mechanisms) and design to prevent misuse — with the section tree and Details panel.

- Review Conformity Assessment Response by AI Risk & Compliance Manager from AI Risk & Compliance Workspace > Tasks > My pending tasks > AI asset tasks

> **[Figure 103 — p.145]** AI Risk and Compliance Workspace Tasks list, AI asset tasks filter, showing the EU AI Act conformity impact assessment task (AIA0001061) in Review state, 2 - High.

- Review Conformity Assessment Response by AI Risk & Compliance Manager from AI Risk & Compliance Workspace > Operations > AI Assessments in Review state

> **[Figure 104 — p.145]** AI Risk and Compliance Workspace Assessments view showing Risk assessments (34 Open, 33 Overdue, 1 Due in 7 days) with a 34-assessment donut and AI assessments (19 Open, 10 Overdue, 1 Due in 7 days) with a 19-assessment status donut.

G. Pre-deployment Lifecycle: Review issues and policy exceptions. Assigned to AI Risk & Compliance Manager as a reminder notice for reviewing outstanding issues or policy exceptions. This lifecycle task is intended for demonstration purpose only.

> **[Figure 105 — p.146]** AI Control Tower Lifecycle tab, Build and test 'Ready for deployment', Pre-deployment assessments with the Conformity assessment task selected and Review issues and policy exceptions still open.

Pre-deployment Review: Perform Residual Risk Assessment

### Configuration

For more details on modifying Flow and associated Sub-Flows belonging to Build & test phase, refer to the Govern - Lifecycle topic.

> [!note] Note
> · Enable Smart Assessments: Set the system property sn_grc.enable_smart_assessment_on_control to true to utilize advanced assessment functionality

- To make change or corrections to system-defined flows/ sub-flows, create a copy version for upgrade safety measures

## Deploy - Review the AI System Record and Finalize All Pre-Deployment Activities

### Overview

Finalize all compliance activities, confirm that risks and issues have been addressed, and move an AI system into the deployed state with active monitoring for ongoing governance.

### Procedure

Lifecycle Task – Deploy Asset assigned to Product Owner as a reminder notice.

> **[Figure 106 — p.147]** AI Control Tower Lifecycle tab with the asset 'Approved for deployment': Assess and Build and test complete, Deploy phase in progress with a single open 'Deploy Asset' task (TASK0022725).

### Configuration

Fore more details on modifying Flow and associated Sub-Flows belonging to Deploy phase, refer to the Govern – Lifecycle topic.

> [!note] Note
> To make change or corrections to system-defined flows/ sub-flows, create a copy version for upgrade safety measures

## Monitoring, maintenance, and retirement

### Overview

It tracks technical things like accuracy and model drift, as well as business outcomes like ROI and adoption. This stage also covers ongoing work like retraining the model and eventually retiring it when it's no longer useful or costs too much to keep running. Report AI-related incidents or ask enquiries that seek clarification from AI Council.

AI behavior is continuously observed to detect drift, bias, or performance degradation.

More details
- Continuous Controls Monitoring: As with any AI system
- Define Indicator Templates
- Measurement of AI Performance
- Measurement of AI Safety
- Measurement of AI Harm Category
- Map Indicator Templates to Control
- Interpret AI System Output

AI Cases - Implementation

Once an AI is live, the Control Tower provides dashboards to monitor how it's doing. It gains insights into the value realized from multiple types of AI systems, view data about user engagement and feedback, and adoption of every type of AI system in your organization.

For more details, refer to the AI Value - Implementation topic.

### Procedure

A. Bulk Action: AI Assessment:

> **[Figure 107 — p.148]** AI Risk and Compliance Workspace 'AI asset inventory - AI systems' list (47 records) with Number, Name, Asset type, State, Risk classification and Residual rating columns, two rows selected, and the AI assessment / Edit actions available; the left tree shows AI asset inventory, Scoping, Library (Authority documents, Citations, Control objectives, AI controls, Risk statements, AI risks, Risk indicator templates, AI policies) and Regulatory information.

> **[Figure 108 — p.149]** 'Send AI assessment' wizard, step 1 'Related entities': a checkbox tree of selected AI assets (ServiceNow Regulatory Document Automation 2025, AI Based Credit Scoring for Loan Approvals 6.4) with Business owner, Risk classification and Residual rating columns, and Cancel / Next buttons.

> **[Figure 109 — p.150]** 'Send AI assessment' wizard, step 2 'Assessment details': Assessment template 'High-risk AI assessment questionnaire', Due Date 2026-03-13, Assessment title 'High Risk AI Asset', an 'Add related entity name as suffix' checkbox and a Description field, with Previous / Cancel / Send assessment buttons.

B. Bulk Action: Risk Assessment

> **[Figure 110 — p.150]** AI asset inventory AI systems list with two rows selected and the 'AI assessment (2)' dropdown open showing the 'Risk classification (2)' bulk action.

> **[Figure 111 — p.151]** 'Send regulatory risk classification assessment' wizard, step 1 'Related entities': two AI assets selected (AI Based Credit Scoring for Loan Approvals 1.0 High score 9, Email Assistant AI Agent for Corporate 1.0 High score 8) with Analyst Josh Warner.

> **[Figure 112 — p.152]** 'Send regulatory risk classification assessment' wizard, step 2 'Assessment details': Risk assessment methodology 'Risk classification for AI system', Due Date 2026-03-10, Assessor Josh Warner, an 'Assign risk assessment to asset analyst' checkbox and an Approver field.

> **[Figure 113 — p.152]** AI asset inventory list with an information banner explaining that assessments are being generated for the selected entities and that a new assessment will not be generated for an entity that already has an open assessment with the chosen methodology.

C. Bulk Risk Assessment ([link](https://www.servicenow.com/docs/r/governance-risk-compliance/ai-risk-management/risk-assessment-project-airc.html))

> **[Figure 114 — p.152]** AI asset record with the 'AI assessment' dropdown open showing three options — Risk classification, Risk assessment and Bulk risk assessment (highlighted).

> **[Figure 115 — p.153]** 'Create bulk risk assessment' modal over an AI asset record: Related entity (Email Assistant AI Agent for Corporate 1.0) and Risk assessment methodology 'Risk assessment for AI inventory', with Cancel / Create buttons.

> **[Figure 116 — p.153]** Risk assessment project 'Risk assessment for ServiceNow Email Assistant AI Agent for Corporate 1.0 - March 2026' on the Define > Context > Details step, with Name and Description fields and Save / Next buttons; the phase tracker shows Define, Scope risk, Assess and Approvals.

> **[Figure 117 — p.154]** The same risk assessment project on the Define > Stakeholders step — Owner Josh Warner, Assignee type Users, Assignee Josh Warner, Watchlist type Entity stakeholder — with Save / Next buttons.

> **[Figure 118 — p.154]** Risk assessment project on the 'Scope risk' step: a Risks related list mapped from the assessable entity showing RK0020444 Unintended Consequences and RK0020450 Model Performance Degradation (Model Drift) with Description, Risk Statement, Owner and State Draft, plus 'Create from risk statements', New and Add risk actions.

> **[Figure 119 — p.155]** Risk assessment project on the 'Assess' step, offering Stacked view or Grid view for assessing the identified risks together, with a 'Start assessment' button.

> **[Figure 120 — p.155]** Risk assessment grid for RAP0001002 showing the two risks with Inherent assessment (Impact, Likelihood), Final computed score (Inherent risk), Control assessment (Applicable, Associated Controls, AI-System control effectiveness) columns — both currently unrated with 'Ineffective' control effectiveness.

> **[Figure 121 — p.156]** The completed risk assessment grid: Unintended Consequences scored Medium impact / Likely likelihood → Medium inherent risk, and Model Performance Degradation scored Critical / Highly likely → High inherent risk, with View summary / Submit buttons.

## Appendices

### A. Learning Courses

ServiceNow offers comprehensive certification and training programs for those looking to become proficient in Integrated Risk Management (IRM). These programs are designed to equip professionals with the necessary skills to implement and manage IRM effectively within their organizations.

Here are some fundamental certification and training options available:
1. GRC: Integrated Risk Management (IRM) Fundamentals
2. GRC: Integrated Risk Management (IRM) Implementation
3. GRC Risk - Process Guide
4. IRM Workspace Overview Video
5. GRC Issue Management Process Guide: Provides detailed guidance on the way that ServiceNow intends the process to- be, for GRC Issue Management
6. GRC Product Architecture Blueprint: Describes the inherent functionality of the Governance, Risk & Compliance (GRC) and outlines the technical components in the form of a diagram

## B. End-User Documentation

- Reading Article ([link](https://www.servicenow.com/docs/bundle/zurich-governance-risk-compliance/page/product/grc-ai-risk-compliance/reference/ai-risk-and-compliance.html))
- Reading Article ([link](https://www.servicenow.com/docs/bundle/yokohama-intelligent-experiences/page/administer/ai-governance-workspace/concept/ai-governance-landing.html))
- Reference Demo Data click here.

Reference Demo Data is provided to support demonstration and ease of use within the product. It contains sample or illustrative information intended to help users understand the structure, format, and potential application of the data. Users may download this file for reference and customization within their environment. The content is not intended to represent complete or authoritative regulatory information. Customers are responsible for verifying the accuracy of the information and for ensuring compliance with applicable laws, regulations, directives, and/or standards, including replacing the reference content with the relevant requirements as needed.

# Govern - Now Assist Governance (Now Assist)

> [!important] Important
> Manual AI asset tracking is error-prone and quickly becomes stale. AICT's auto-discovery eliminates that risk by continuously syncing AI Models, Datasets, Prompts, and Agentic AI assets directly from your live Now Assist configuration.

## Overview

When ServiceNow Now Assist is implemented within your organization, AI Control Tower (AICT) can automatically discover and register AI assets used by Now Assist skills.

This capability eliminates the need for manual asset entry and ensures that the AI inventory remains accurate, current, and aligned with deployed AI functionality.

## Automated AI Asset Synchronization

AICT maintains inventory accuracy through a scheduled job titled “Sync Now Assist AI Assets.”

This job performs continuous synchronization by identifying and mapping AI assets generated or utilized by Now Assist skills into the AICT inventory.

### High-Level Process Flow

At a high level, the synchronization process:
1. Iterates through Now Assist configuration tables
2. Identifies AI assets and associated metadata
3. Determines whether corresponding AICT digital assets exist
4. Creates or updates AICT digital assets
5. Synchronizes associated Product Models (CMDB records)
6. Establishes relationships across AI Systems, Models, Prompts, and Use Cases

## 1. Sync Model Assets

### Source

- *Generative AI Model Configurations* $sys_generative_ai_model_config$

### Process

- Iterate through all model configurations
- For each configuration:
- Identify or create an AI Model Digital Asset $alm_ai_model_digital_asset$
- Prepare model metadata using *NAAssetsStaticContent*
- Update or create the associated AI Model Product Model $cmdb_ai_model_product_model$
- Map configuration and model information to the digital asset

### Model Digital Asset Updates

- Model Card
- Required Infrastructure
- Evaluation Metrics Report

### Product Model Attributes

Model Configuration
- Name
- Model Category
- Supported Languages
- Context Window

Model Information
- Documentation
- Manufacturer
- Parameters
- Model Size (MB)
- Source
- Deployment Guideline
- Training Procedure

## 2. Sync Dataset Assets

### Source

- *OneExtend Test Dataset* $sys_one_extend_test_dataset$ (run type = *eval_run*)

### Process

- Iterate through dataset records
- For each dataset:
- Identify or create an AI Dataset Digital Asset $alm_ai_dataset_digital_asset$
- Update or create the associated AI Dataset Product Model $cmdb_ai_dataset_product_model$

### Base Dataset Handling

- If a parent (base dataset) exists:
- Apply the same create/update logic
- If not:
- Create the base dataset and associated product model

### Product Model Attributes

- Name
- Description
- Model Category

## 3. Sync Prompt Assets

### Source

- *Generative AI Configurations* $sys_generative_ai_config$ (Prompt Templates)

### Process

- Iterate through prompt configurations
- For each prompt:
- Identify or create an AI Prompt Digital Asset $alm_ai_prompt_digital_asset$
- Update or create the associated AI Prompt Product Model $cmdb_ai_prompt_product_model$
- Associate prompts with relevant AI systems and models

### Relationship Mapping

- AI Model Digital Asset
- Associated AI System Digital Assets

### Product Model Attributes

- Name
- Version
- Model Category

## 4. Sync Agentic AI Assets

Agentic AI synchronization includes AI Tools, AI Agents, and AI Use Cases derived from Now Assist configurations.

### Sync AI Tools

Source: $sn_aia_tool$ Target: $sn_ent_ai_tool$

Mapped Attributes
- Name
- Description
- Type
- Active Status
- Topic

## 5. Sync AI Agents

Source: $sn_aia_agent$

### Process

- Identify associated AI System
- Sync with AI System Component Product Model $cmdb_ai_system_component_product_model$
- Map agent metadata to the AI system

Mapped Attributes
- Name
- Description
- Model Category
- Documentation
- Manufacturer

> [!note] Note
> Prompt product models are also synchronized for each associated AI Prompt Digital Asset.

## 6. Sync AI Use Cases

### Process

- Identify associated AI System
- Sync with AI System Component Product Model
- Map use case metadata to the AI system

Mapped Attributes
- Name
- Description
- Model Category
- Documentation
- Manufacturer

> [!note] Note
> Prompt product models are also synchronized for associated AI Prompt Digital Assets.

## Configuration Guidance

### Default Recommendation

It is strongly recommended to keep the scheduled job enabled to ensure:
- Continuous inventory accuracy
- Alignment between deployed AI capabilities and governance records
- Reduced operational overhead

### Optional Deactivation

If automatic discovery is not desired:
- The scheduled job may be deactivated
- Manual asset management will be required to maintain inventory completeness

### Key Implementation Notes

- Synchronization is idempotent (safe to run repeatedly without duplication)
- Asset relationships (Model ↔ Prompt ↔ System ↔ Use Case) are automatically maintained
- Product Models serve as the CMDB backbone for AI asset standardization
- Prompt synchronization is tightly coupled with agent and system relationships

### Asset Sync Detail

Each sync method follows the same create-or-update logic: if an asset already exists in AICT, it is updated; if it does not exist, it is created. The sections below describe what is synced for each asset type.

## 1. AI Model Sync

Iterates all Generative AI Model Configurations and maps them to AI Model Digital Assets in AICT. Both the digital asset record and its associated AI Model Product Model are updated.

| **Record Updated** | **Fields Synced** |
| --- | --- |
| AI Model Digital Asset | Model Card, Required Infrastructure, Evaluation Metrics Report |
| AI Model Product Model | Name, Model Category, Supported Languages, Context Window, Documentation, Manufacturer, Parameters, Model Size (MB), Source, Deployment Guideline, Training Procedure |

## 2. Dataset Sync

Iterates OneExtend Test Datasets with run type eval_run and maps them to AI Dataset Digital Assets. If a Base Dataset (parent) exists, it is also synced; if not, it is created.

| **Record Updated** | **Fields Synced** |
| --- | --- |
| AI Dataset Product Model | Name, Description, Model Category |
| Base Dataset Product Model (if applicable) | Same fields as above; created if Base Dataset does not yet exist in AICT |

## 3. Prompt Sync

Iterates Generative AI Configurations (which contain Prompt Templates) and maps them to AI Prompt Digital Assets. After syncing the asset, AICT links the Prompt to the relevant AI Systems via the AI Model Digital Asset and AI System Digital Asset references.

| **Record Updated** | **Fields Synced** |
| --- | --- |
| AI Prompt Product Model | Name, Version, Model Category |
| AI System linkage | Updates AI Systems in AICT with associated Prompts using AI Model Digital Asset and AI System Digital Asset references |

## 4. Agentic AI Asset Sync

Syncs three types of Agentic AI assets from the NowAssist configuration. This is the most complex sync operation and is central to maintaining governance visibility over agentic deployments.

| **Asset Type** | **Source** | **Fields Synced** |
| --- | --- | --- |
| AI Tools | sn_aia_tool | Name, Description, Type, Active, Topic |
| AI Agents | sn_aia_agent | Name, Description, Model Category, Documentation, Manufacturer; also syncs associated AI Prompt Product Models |
| Agent Use Cases | Use Case configurations | Name, Description, Model Category, Documentation, Manufacturer; also syncs associated AI Prompt Product Models |

Note: For every AI Agent and Use Case synced, the associated AI Prompt Product Models (cmdb_ai_prompt_product_model) are also synced for each AI Prompt Digital Asset (alm_ai_prompt_digital_asset).

## Configuration and Customization

### Default Configuration

The Sync Now Assist AI Assets scheduled job is enabled by default. No additional setup is required for standard Now Assist deployments. The job runs automatically and maintains continuous inventory sync.

### Disabling Auto-Discovery

You may deactivate the scheduled job if your organization does not use Now Assist or has a separate inventory management process. To disable:

• Navigate to System Definition > Scheduled Jobs

• Locate Sync Now Assist AI Assets

• Set the job status to Inactive

Recommendation: Keep the scheduled job active. Disabling it means your AI inventory will no longer reflect deployed Now Assist assets, creating governance gaps and potential compliance risk.

### Customizing Sync Behavior

If your implementation requires non-standard sync logic — for example, filtering which assets are synced or adding custom field mappings — customize using the standard ServiceNow Script Include inheritance pattern:

| **Step** | **Action** |
| --- | --- |
| 1 | Create a new Script Include that extends NowAssistAIAssetsUtil |
| 2 | Override only the methods you need to change (e.g., syncAIModels, syncAIPrompts) |
| 3 | Do not modify the base NowAssistAIAssetsUtil directly — preserve base functionality |
| 4 | Test in a sub-production environment before deploying changes |

### Governance Considerations

Auto-discovery addresses the most common AI governance failure point: an incomplete or stale AI inventory. The following table maps AICT inventory completeness to common governance requirements.

| **Governance Requirement** | **How Auto-Discovery Supports It** |
| --- | --- |
| AI Inventory Accuracy | Continuous sync ensures all deployed Now Assist AI assets are reflected in AICT without manual entry |
| Model Traceability | Model Card, Manufacturer, Training Procedure, and Deployment Guidelines are captured per model |
| Prompt Governance | Prompt Templates are versioned and linked to the AI Systems that use them |
| Agentic AI Visibility | AI Tools, Agents, and Use Cases are captured along with their associated Prompts — critical for agentic governance |
| Audit Readiness | A complete and current inventory is the foundation for AI impact assessments, risk reviews, and regulatory reporting |

### Implementation Checklist

Use this checklist to confirm your Now Assist AI Governance auto-discovery is correctly configured and active.

| **Task** | **Owner** |
| --- | --- |
| ☐ Confirm Sync Now Assist AI Assets scheduled job is Active | Platform Admin |
| ☐ Verify Now Assist skills are deployed and in active use | Implementation Lead |
| ☐ Run the scheduled job manually and confirm assets appear in AICT inventory | Platform Admin |
| ☐ Confirm AI Models, Datasets, Prompts, and Agentic Assets are all represented | AI Governance Owner |
| ☐ Review any customization requirements; if needed, extend NowAssistAIAssetsUtil | Platform Admin |
| ☐ Brief Risk & Compliance Lead on inventory and how to use it for AI risk assessments | AI Governance Owner |
| ☐ Document any deviations from default configuration in your governance runbook | Implementation Lead |

### Related Resources

| **Resource** | **Description** |
| --- | --- |
| AI Control Tower Implementation Guide | Full AICT lifecycle implementation guide covering Intake, Assess, Build & Test, and Deploy phases |
| Now Assist Administration Guide | Now Assist skill configuration and deployment reference |
| NowAssistAIAssetsUtil API Reference | Script Include method signatures and extension patterns |
| AICT AI Asset Inventory | Navigate to: AI Control Tower > AI Assets to view the live inventory |

# Govern - Lifecycle

ServiceNow AI Control Tower is engineered to empower AI Center of Excellence and Chief AI Officers (CAIOs) in overseeing organizational AI operations. Built on the ServiceNow AI Platform, it delivers comprehensive tools for the management, governance, and optimization of AI systems, models, datasets, prompts, and its inputs and outputs. ServiceNow AI Control Tower is built on the ServiceNow® AI Platform and designed to empower AI Centers of Excellence (CoEs) and Chief AI Officers (CAIOs) with the tools they need to manage, govern, and optimize AI operations at scale. The platform provides centralized oversight of AI models, datasets, prompts, and their inputs and outputs — across both cloud-based and on- premises environments.

Regardless of how AI solutions are sourced — whether developed internally, acquired from third-party vendors, or embedded within SaaS platforms — AI Control Tower serves as a single intelligence hub that governs AI assets from initial onboarding through retirement. A native AI asset inventory within the Configuration Management Database (CMDB) anchors this hub, delivering business context by linking AI initiatives directly to enterprise services and assets — something few standalone governance tools can offer.

This foundation supports end-to-end workflows that span the full AI lifecycle, enabling seamless collaboration across strategy, IT, risk, legal, and business teams. The result is holistic AI management — not siloed oversight — with every stakeholder working from a shared system of record.

To support this, AI Control Tower provides specialized workspaces tailored to every role within the AI CoE — including AI stewards, product owners, and risk and compliance managers — enabling robust asset tracking and effective lifecycle and risk management.
- Figure 1. AI Systems at each stage of its lifecycle

> **[Figure 122 — p.167]** AI Risk and Compliance Workspace home combining the 'AI systems by state' counters (New 0, Assess 16, Build 9, Review for deployment 1, Live and Monitor 2, Offboard 0), an 'AI systems by department' bar chart, and the Assessments panel with Risk assessments (29 Open / 29 Overdue) and AI assessments (13 Open / 12 Overdue) donuts.

## AI Control Tower Lifecycle

The AI Control Tower lifecycle outlines the governance and management process for AI assets within your organization. This workflow is divided into distinct stages that ensure responsible development, deployment, and oversight of AI assets.

> **[Figure 123 — p.168]** End-to-end AI governance process diagram across Demand, Build & Validate and Deploy/Monitor/Assess Value, showing the persona swim lanes (AI Risk & Compliance Manager, AI Steward, Product Owner, other AI governance teams) and the flow from AI asset request through analysis, AI lifecycle tasks, regulatory risk classification, controls implementation and risk mitigation, continuous control monitoring, tracking and triage of AI cases, to resolution and closure.

- Figure 1. AI Asset High-level Lifecycle

### The AI Asset Lifecycle

The AI Control Tower lifecycle defines the governance and management process for AI assets within your organization. It is divided into distinct stages that ensure responsible development, deployment, and ongoing oversight — covering any AI asset type, including AI systems, models, datasets, and prompts, from initial onboarding through retirement.

Understanding Asset State, Lifecycle Phase, and Lifecycle Status

## AI Asset Lifecycle Overview

The AI asset lifecycle defines the series of phases required to manage any AI asset — including AI systems, models, datasets, and prompts — from initial intake through retirement. Each phase has defined activities, responsible personas, and governance checkpoints to ensure responsible development, deployment, and ongoing oversight.

### Phase 1: Intake / Onboard Primary Persona: AI Product Owner

#### AI Asset Lifecycle Overview

#### Intake / New / Onboard

Primary Persona: AI Product Owners

AI Product Owners initiate the AI asset lifecycle by submitting AI use case requests through the Employee Center. These requests capture key details related to the AI models, datasets, and intended business use.

AI assets may be introduced through:
- Manual intake: Submission of AI use case requests, including onboarding of models and datasets into the AI Inventory
- Automated discovery:
- AI assets identified from Now Assist
- External integrations (e.g., AWS Bedrock, Microsoft Azure, other cloud AI services)

Upon submission, the AI asset enters the “New” stage, representing its formal registration within the organization. At this stage, foundational metadata is captured, including:
- Versioning
- Documentation
- Business and technical context

AI Stewards initiate governance by starting the review, which advances the asset into the Assess phase.

#### Assess

Primary Persona: AI Steward (AI CoE) Supporting Stakeholders: Risk & Compliance, Security, Legal, and other cross-functional teams

During the Assess phase, AI assets undergo structured evaluation across key dimensions:
- Performance and technical viability
- Business value and expected impact
- Risk posture
- Regulatory and policy compliance

The AI Steward (CoE) coordinates assessment activities, ensuring alignment with enterprise principles such as:
- Privacy
- Ethics
- Transparency
- Protection of fundamental rights

AI Control Tower enables:
- Identification and tracking of risks
- Definition and mapping of required controls

Following completion of assessments, AI Stewards review progress and approve advancement to the Build & Test phase.

#### Build & Test

The lifecycle begins when an AI Product Owner submits an AI use case request through the Employee Center, capturing key details about the AI models, datasets, and intended business use. AI assets may enter the inventory through two paths:
- Manual intake: Submission of AI use case requests, including direct onboarding of models and datasets into the AI Inventory
- Automated discovery: AI assets identified from Now Assist, or through external integrations such as AWS Bedrock, Microsoft Azure, and other cloud AI services

Upon submission, the asset enters the New stage — representing its formal registration within the organization. At this stage, foundational metadata is captured, including versioning, documentation, and business and technical context.

Once registered, the AI Steward initiates governance review, advancing the asset into the Assess phase.

### Phase 2: Asses Primary Persona AI Steward (AI CoE) | Supporting: Risk & Compliance, Security, Legal, and cross-functional teams

During the Assess phase, the AI asset undergoes structured evaluation across four key dimensions: performance and technical viability, business value and expected impact, risk posture, and regulatory and policy compliance.

The AI Steward coordinates all assessment activities, ensuring alignment with enterprise principles including privacy, ethics, transparency, and the protection of fundamental rights. AI Control Tower supports this work by enabling identification and tracking of risks and the definition and mapping of required controls.

Upon completion, the AI Steward reviews findings and approves advancement to the Build & Test phase.

### Phase 3: Build & Test Primary Personas: AI Product Owners, AI Risk & Compliance Teams

This phase covers the development, integration, and validation of the AI asset. Core activities include:
- Design and development of models and algorithms
- Integration with required data sources
- Functional and performance testing for reliability and accuracy

Risk and compliance activities are embedded throughout — addressing identified risks and implementing recommended controls during development. Prior to deployment, a pre-deployment review validates:
- Compliance with external frameworks (e.g., NIST AI RMF, EU AI Act)
- Alignment with internal policies (e.g., AI SDLC policies)
- Resolution of open issues and closure of any policy exceptions

The AI Steward reviews readiness and approves progression to the Deploy phase.

### Phase 4: Deploy & Operate Primary Personas: AI Steward (governance oversight), AI Product Owners (asset ownership), AI Risk & Compliance Teams

In this phase, the AI asset is operationalized within business environments. Deployment may follow a phased or limited release strategy or proceed as a full-scale enterprise rollout.

Post-deployment, continuous monitoring tracks performance and effectiveness, user adoption, and emerging risks and compliance posture. AI Stewards maintain ongoing governance oversight while AI Product Owners ensure sustained lifecycle management and adherence to governance standards.

AI Control Tower also supports value realization tracking, enabling measurement of AI adoption and business impact over time.

### Deploy (Monitor & Operate)

*References: AI Risk and Compliance (link) · AI Value (link)*

Detailed Lifecycle – AI System

> **[Figure 124 — p.171]** 'AICT Architecture' diagram organised by the Discover / Observe / Secure / Govern / Measure pillars: the AI Asset Inventory (CMDB) feeding input guardrails, LLM and output guardrails with tracing, AI Observability Traces, security widgets (Security Scores, Access Map, Risk Posture, Security Alerts, Model security, Risk scores, Security Evals), governance widgets (AI Risk Assessment, continuous risk monitoring, regulatory risk classification, compliance status, risk response, policies/regulations/control objectives/legal reviews), measurement widgets (Value Templates, Adoption Metrics, Engagement and Productivity) and an Agentic Intelligence Foundation layer (Conversational Agent, Knowledge Graph, Lifecycle Action Recommender, Reg./Control Failure Insights, Value Assistant, Productivity Insights).

- *Figure 2. AI System Detailed Lifecycle*

### Lifecycle Implementation

AI Control Tower's lifecycle governance is powered by Playbook — a ServiceNow feature that enables users to interact with a defined business process through a visual, task-oriented workspace experience. The AI Asset Lifecycle Playbook orchestrates a series of flows and subflows that drive the end-to-end process, while adding a UI layer that automates and streamlines execution within the AI Control Tower workspace.

Before Publish: Review existing content and incorporate Onboarding and Offboarding Lifecycle Tasks from other workstreams before finalizing this section.

A note on AI asset types: All AI asset types — AI Systems, AI Models, Datasets, Prompts, and Inputs and Outputs — share the same lifecycle, powered by the same playbook. However, only AI Systems have lifecycle tasks pre-configured out of the box. For all other asset types, AI Stewards are expected to manually create tasks, or optionally replicate AI System tasks by cloning the relevant Flows and modifying trigger conditions. When doing so, reuse Subflows wherever possible; clone only when reuse is not feasible.

#### Intake and Onboarding

Role required: AI Asset Owner `[sn_ai_asset_mgmt.ai_asset_owner]`

The lifecycle begins when an AI Product Owner submits an AI use case request — either through the Employee Center or directly via the AI Control Tower workspace. See the AI Inventory Implementation Guide *(link)* for step-by-step intake instructions.

What happens upon submission:

When an AI System request is submitted, the platform automatically creates the following records:
- AI System Digital Asset `[alm_ai_system_digital_asset]` — Represents the AI System asset on the platform
- AI System Product Model `[cmdb_ai_system_component_product_model]` — The product model associated with the asset

As part of AI Asset Governance setup (established when the AI Control Tower SKU is installed), the platform also creates:
- AI Asset Governance Details `[sn_ai_governance_asset_governance_details]` — The system of record that powers governance and lifecycle oversight of the AI System

Initiating the lifecycle:

The AI Steward activates the lifecycle by navigating to AI Control Tower > Lists > AI Asset Inventory > AI Systems, opening the relevant AI System record (which launches the associated AI Asset Governance Details record), and clicking Start Review. This action creates:
- `[sn_grc_ai_gov_ai_system]` — The operational record that powers risk and compliance use cases
- Related Entity in IRM — Entities are the foundational objects of Integrated Risk Management workflows, analogous to what assets are in configuration and asset management

#### Lifecycle Architecture

AI Asset Owner[sn_ai_asset_mgmt.ai_asset_owner]

AI Steward [sn_ai_governance.ai_steward]

Submitting an AI Use Case (AI System) request performs the following prior to kicking-off the lifecycle
- Creates an AI System Digital Asset [alm_ai_system_digital_asset] – Represents AI System ‘asset’ in platform
- Creates an AI System Product Model [cmdb_ai_system_component_product_model] – Is a product model of the AI System asset

As part of establishing the AI Asset Governance, when the AI Control Tower SKU is installed, the below system of record is setup as well.
- Creates an AI Asset Governance Details [sn_ai_governance_asset_governance_details] – Is a system of record that powers the governance of the AI system including overseeing the lifecycle of the AI System

The AI System must be accepted by the AI Steward by navigating to the AI Control Tower > Lists > AI Asset Inventory > AI Systems by opening the AI System (launches the related AI Asset Governance Details record) and clicking ‘Start Review’. This action performs the following:
- Create an AI System [sn_grc_ai_gov_ai_system] (Is a system of record that powers different use cases, in this case, the AI Risk and Compliance use case)
- Create a ‘Related entity in IRM’. Entities are the foundational objects of Integrated risk workflows like what assets are to configuration and asset management

## Lifecycle

### AI Control Tower and AI Risk & Compliance Object Alignment

Within the AI Control Tower architecture, lifecycle governance and risk/compliance execution are handled through distinct but interconnected records.
- The AI Asset Governance Details record
- `[sn_ai_governance_asset_governance_details]`
- serves as the primary lifecycle governance record
- within AI Control Tower. It provides AI Stewards with:
- End-to-end lifecycle visibility
- Governance state tracking
- Oversight across all lifecycle phases
- The AI System record
- `[sn_grc_ai_gov_ai_system]`
- is the operational record leveraged by AI Risk and Compliance (GRC) to:
- Execute risk assessments
- Manage compliance workflows
- Track regulatory alignment

Together, these records ensure separation of concerns:
- AICT: Lifecycle governance and orchestration
- GRC: Risk, compliance, and control execution

### Approval Request and Lifecycle Execution

#### Object Alignment: AI Control Tower and AI Risk & Compliance

AI Control Tower uses two distinct but interconnected records to separate lifecycle governance from risk and compliance execution:

| **Record** | **Purpose** |
| --- | --- |
| AI Asset Governance Details `[sn_ai_governance_asset_governance_details]` | Primary lifecycle governance record — provides end-to-end lifecycle visibility, governance state tracking, and oversight across all phases |
| AI System (GRC) `[sn_grc_ai_gov_ai_system]` | Operational record used by AI Risk & Compliance — drives risk assessments, compliance workflows, and regulatory tracking |

This separation ensures AICT owns lifecycle governance and orchestration, while GRC owns risk, compliance, and control execution — with clear traceability between the two.

#### Approval Request and Lifecycle Execution

The AI Asset Approval Request `[sn_ai_governance_assessment_request]` is the execution layer that operationalizes the lifecycle defined in the Governance Details record.
- Each Approval Request references the AI Asset Governance Details record and acts as the container for lifecycle execution activities
- Approval Requests are configured with `Type = "AI Governance Lifecycle"` to scope them explicitly for AI Control Tower lifecycle orchestration
- The Approval Request drives progression across all lifecycle phases

#### Lifecycle Task Framework

AI Asset Approval Tasks `[sn_ai_governance_assessment_task]` are created within the Approval Request to drive lifecycle execution. These tasks:

### Lifecycle Task Framework

- Represent discrete governance and compliance activities across the Assess, Build & Test, and Deploy phases
- Enable structured tracking and accountability
- Apply across all AI asset types: AI Systems, AI Models, Datasets, Prompts, and Inputs and Outputs

## Architectural summary

### Key Architectural Principle

AI Control Tower leverages:
- Governance Details → lifecycle system of record
- Approval Requests + Tasks → lifecycle execution engine
- AI System (GRC) → risk and compliance execution

This layered design ensures clear separation between governance and compliance domains, end-to-end traceability, and scalable lifecycle management across all asset types.

This layered design ensures:
- Clear separation between governance and compliance domains
- End-to-end traceability across systems
- Scalable lifecycle management for all AI asset types

## AI Asset Lifecycle Data Flow and Object Relationships

> [!note] Note
> This block diagram is intended to illustrate high-level object interactions and process flow. It is not a representation of the underlying data model.

At a high level, the diagram depicts how core records interact to:
- Maintain synchronization of AI asset status
- Enable lifecycle progression from intake through deployment
- Support execution within AI Control Tower and associated workspaces

### Core Object Interactions

- AI Asset Approval Request Initiation
- An AI Asset Approval Request is generated when the AI Steward selects Start Review
- This request references the Asset Governance Details record
- Establishes the primary linkage between lifecycle execution and governance tracking
- Asset Governance Details Relationship
- The Asset Governance Details record and the Approval Request exist as independent tables
- The Approval Request maintains a parent-to-child (hierarchical) reference to the Governance Details record
- Governance Details act as the system of record for lifecycle state, controls, and oversight
- Lifecycle Task Management
- Tasks are generated within the Approval Request and executed across lifecycle phases
- These tasks are associated with the Asset Governance Details record
- Collectively, these are referred to as Lifecycle Tasks, driving execution from Assess through Deploy
- Integration with AI Risk and Compliance (GRC)
- Tasks created within
- AI Risk and Compliance (GRC)
- are linked to Lifecycle Tasks via:
- `Related Record ID`
- `Related Record Table`
- This linkage ensures traceability between governance activities and lifecycle execution
- Bidirectional Synchronization
- Lifecycle Tasks in AI Control Tower and corresponding GRC tasks are synchronized bidirectionally
- Updates (e.g., status changes, task completion) in one system are reflected in the other
- Ensures consistency across governance, risk, and operational workflows
- Lifecycle Progression Flexibility
- AI Stewards can progress assets through lifecycle stages even if certain tasks are incomplete
- Tasks may be marked as:
- Closed Complete
- Closed Skipped
- This supports operational flexibility while maintaining auditability

## Technical summary

### Playbooks

#### AI Asset Lifecycle Data Flow and Object Relationships

Note: The block diagram illustrates high-level object interactions and process flow. It is not a representation of the underlying data model.

The diagram depicts how core records interact to maintain synchronization of AI asset status and enable lifecycle progression from intake through deployment.

Core interactions

Before you begin: Review the existing content and make necessary changes to incorporate Onboarding and Offboarding Lifecycle Tasks from other workstreams.

ServiceNow Playbooks are interactive, guided experiences enabled on workspaces, portals, mobile and so on that help users to follow predefined, step-by-step processes to complete complex tasks—especially used in areas like Customer Service Management (CSM), HR, Field Service, and Risk/Compliance. They are part of the Playbook Experience framework, built on ServiceNow's Now Experience UI and use UI Builder for configuration.
1. Approval Request initiation — When the AI Steward selects Start Review, an AI Asset Approval Request is generated. This request references the Asset Governance Details record, establishing the primary linkage between lifecycle execution and governance tracking.
2. Governance Details relationship — The Asset Governance Details record and the Approval Request exist as independent tables. The Approval Request maintains a parent-to-child reference to the Governance Details record, which acts as the system of record for lifecycle state, controls, and oversight.
3. Lifecycle task management — Tasks are generated within the Approval Request and executed across lifecycle phases. These tasks are associated with the Asset Governance Details record and collectively referred to as Lifecycle Tasks.
4. GRC integration — Tasks created within AI Risk & Compliance (GRC) are linked to Lifecycle Tasks via `Related Record ID` and `Related Record Table` , ensuring traceability between governance activities and compliance execution.
5. Bidirectional synchronization — Lifecycle Tasks in AI Control Tower and corresponding GRC tasks are synchronized bidirectionally. Status changes and task completions in one system are reflected in the other.
6. Lifecycle progression flexibility — AI Stewards can advance assets through lifecycle stages even if certain tasks are incomplete, by marking tasks as Closed Complete or Closed Skipped. This supports operational flexibility while maintaining full auditability.

## Technical Implementation: Playbooks

### AI Asset Lifecycle Playbook

*Figure 4 — AI Asset Lifecycle Playbook (insert here)*

ServiceNow Playbooks are interactive, guided experiences built on the Now Experience UI framework and configured via UI Builder. They are used across ServiceNow products — including CSM, HR, Field Service, and Risk & Compliance — to guide users through predefined, step-by-step processes for complex tasks.

AI Control Tower implements the AI Asset Lifecycle Playbook, which is associated with the AI Asset Approval Request

`[sn_ai_governance_assessment_request]` at the time a lifecycle record is created.
- The Approval Request is filtered with `Type = "AI Governance Lifecycle"`
- It maintains a relationship with the AI Asset Governance Details record `[sn_ai_governance_asset_governance_details]`
- This relationship enables the Playbook to surface within the AI Control Tower workspace on the Governance Details record

### Playbook Initiation

### Playbook Initiation and Structure

The lifecycle playbook is triggered when an AI Steward selects Start Review on an AI asset. This action:
- Initiates the lifecycle process
- Activates the Lifecycle tab on the AI Asset record
- Loads the Playbook within the workspace

The Playbook is organized into three standard lifecycle stages — Assess, Build & Test, and Deploy — each containing defined phases, associated lifecycle tasks, and stage-specific governance activities.

### Playbook Architecture

The playbook consists of two core components:

Automation Layer Drives lifecycle execution and workflow logic — determining task completion status, triggering required actions and transitions, and managing phase progression. Implemented using Flows and Subflows.

Each stage contains:
- Defined phases
- Associated lifecycle tasks
- Stage-specific governance and execution activities

### Lifecycle Task Model

- Out-of-the-box (OOB), AI System assets are preconfigured with lifecycle tasks
- For other AI asset types (e.g., models, datasets, prompts):
- Tasks may be manually created by the AI Steward
- Or programmatically enabled through configuration

### Customization and Extensibility

Customers can extend and tailor the playbook through Flow Designer:
- Recommended approach:
- Clone existing Flows and Subflows
- Modify triggers and conditions to support additional AI asset types
- Task customization options:
- Define new lifecycle tasks using Flow Designer conditions
- Adjust task sequencing where needed
- Best practice guidance:
- Avoid deactivating out-of-the-box (OOB) tasks
- Maintain the standard lifecycle stage order (Assess → Build & Test → Deploy)
- Use cloning rather than direct modification to preserve upgrade compatibility

### Lifecycle Phase Configuration Considerations

- Lifecycle stages (Assess, Build & Test, Deploy) are defined with static references in the playbook configuration
- While customers can rename phases, this requires updates in multiple locations

Important considerations:
- Updating phase names in the AI Asset Lifecycle table `[sn_ai_governance_lifecycle]` does not automatically update playbook references
- Static references must be updated manually to maintain consistency

Key areas requiring alignment:
- Lifecycle phase definitions
- Workspace list views
- UX metadata configurations (e.g., `sys_ux_list` records)

Administrative support may be required for these updates.

### Playbook Architecture

The playbook consists of two core components:

#### 1. Automation Layer

UI Layout Defines how lifecycle steps and tasks are presented in the workspace. Implemented as a list view of lifecycle tasks, including status and progression indicators.

The underlying automation framework is powered by a central subflow — the AI Asset Lifecycle Assessment Flow — which orchestrates lifecycle phases, manages task creation and progression, and ensures alignment between governance and execution layers. Each lifecycle phase has specific flows and subflows triggered based on conditions defined in Flow Designer.

#### 2. UI Layout - Customization and Extensibility

Customers can extend the playbook through Flow Designer. Following is the underlying workflow design
- Clone, don't modify — Clone existing Flows and Subflows and adjust triggers and conditions to support additional AI asset types. Avoid deactivating OOB tasks or modifying them directly to preserve upgrade compatibility.
- Task customization — Define new lifecycle tasks using Flow Designer conditions and adjust sequencing as needed.
- Lifecycle stage order — Maintain the standard Assess → Build & Test → Deploy sequence.

> [!important] Important
> static lifecycle references: Lifecycle stages are defined with static references in the playbook configuration. Renaming phases in the AI Asset Lifecycle table `[sn_ai_governance_lifecycle]` does not automatically update playbook references — manual updates are required across lifecycle phase definitions, workspace list views, and UX metadata configurations (e.g., `sys_ux_list` records). Administrative support may be needed for these changes.

### Lifecycle Flows by Phase

The following flows and subflows execute automatically as an AI System asset progresses through the lifecycle. Each flow is triggered by a specific lifecycle status change and creates the tasks that drive governance and compliance activities.

#### Assess Phase

Flow: AIRC Flow — AI Governance Details Enters Assess

*Trigger: AI Governance Details record transitions to Assess phase*

| **Step** | **Action** | **Details** |
| --- | --- | --- |
| 1 | Flow initiation | Triggers when AI Governance Details enters Assess phase |
| 1.1 | Transition to Assess phase | Trigger point: AI Governance Details record moves to Assess |
| 1.2 | Create Impact Assessment task | AI asset approval task — type: *Impact Assessment* |
| 1.3 | Assign Impact Assessment task | Task assigned to AI Risk & Compliance Managers |
| 1.4 | Complete and review Impact Assessment | AI Asset Owner completes; AI Risk & Compliance Manager reviews and closes |
| 1.5 | Sync Impact Assessment tasks | AICT and AIRC assessment tasks kept in sync |
| 2 | Create Legal Collaboration task | AI approval task — type: *AI Governance Task* |
| 3 | Create Security Clearance task | AI approval task — type: *AI Governance Task* |
| 4 | Create Architecture Review task | AI approval task — type: *AI Governance Task* |

1. Subflows called during Assess:
- Trigger Smart Assessment — initiates the Impact Assessment
- Map AI Control Objectives to AI System — upon Impact Assessment completion, when sent for AIRC review; adds controls after review is complete
- Map AI Risk Statements to AI System — upon Impact Assessment completion, when sent for AIRC review; adds risks after review is complete
- Change Assessment State — updates Impact Assessment state
- Assign Analyst to AI System — upon assessment review completion, captures the reviewing analyst on the AI System record
- Generate Risk Assessment — upon assessment completion, generates a risk assessment for the AIRC analyst
- Note: From AICT, the Impact Assessment task moves to *In Review*. In AIRC, the AI Impact Assessment progresses to
- *Review* simultaneously. The AIRC user persona closes the AI Impact Assessment, which marks it as closed in AICT as
- well.
- Flow: Assign Analyst to AI System
- *Trigger: AI System Impact Assessment is closed*

| **Step** | **Action** | **Details** |
| --- | --- | --- |
| 1 | Flow initiation | Triggers when AI System Impact Assessment is closed |
| 1.1 | Update AI System record | Assigns the Risk Analyst field to the user who closed the task |

---

- Flow: Generate Risk Assessment
- *Trigger: AI System record is updated*

| **Step** | **Action** | **Details** |
| --- | --- | --- |
| 1 | Flow initiation | Triggers when AI System record is updated |
| 1.1 | Create Perform Risk Assessment task | AI approval task — type: *Risk Assessment* |
| 1.2 | Create object-based Risk Assessment | Generated for the AI System and assigned to an AI Risk & Compliance user |
| 2 | Complete Risk Assessment | Task completed by AI Risk & Compliance user |
| 3 | Sync Risk Assessments | AI approval task and object-based assessment in AICT and AIRC kept in sync |

#### Build & Test Phase

- Flow: AIRC Flow — AI Governance Details Approved for Development
- *Trigger: Lifecycle status changes to Approved for Development*

| **Step** | **Action** | **Details** |
| --- | --- | --- |
| 1 | Flow initiation | Triggers when lifecycle status changes to *Approved for Development* |
| 1.1 | Create Control Attestation task | AI asset approval task — type: *Create Control Attestation* |
| 1.2 | Assign Control Attestation task | Assigned to AI Risk & Compliance Managers |
| 1.3 | Complete Control Attestation | Completed and closed by AI Risk & Compliance Manager |
| 2 | Sync Control Attestations | Control attestations in AICT and AIRC kept in sync |
| 3 | Create Collect Deployment Region Information task | AI asset approval task — type: *Information Collection* |
| 4 | Create Share Deployment Details task | Assigned to AI Risk & Compliance Managers |

- Subflows called:
- Create Control Attestation Lifecycle Task — creates the control attestation lifecycle task within the flow
- Note: From AICT, the *Collect Information on Deployment Regions* task moves to *In Review*. In AIRC, the *Share*
- *Deployment Details* task progresses to complete — completing the task in both systems. Control attestations and risk
- assessments are completed from AIRC.
- Flow: AIRC Flow — AI Governance Details Ready for Deployment
- *Trigger: Lifecycle status changes to Ready for Deployment*

| **Step** | **Action** | **Details** |
| --- | --- | --- |
| 1 | Flow initiation | Triggers when lifecycle status changes to *Ready for Deployment* |
| 1.1 | Create Review Issues and Policy Exceptions task | AI asset approval task — type: *Other* |
| 1.2 | Assign review task | Assigned to AI Risk & Compliance Managers — covers issues, policy exceptions, control attestations, and detailed risk assessment |
| 1.3 | Complete review task | AI Risk & Compliance Manager completes and closes |
| 2 | Sync task records | Records kept in sync across AICT and AIRC |
| 3 | Create Conformity Assessment task | AI asset approval task — type: *Conformity Assessment* |
| 4 | Create AI Impact Assessment for EU AI Act conformity | Assigned to AI Risk & Compliance Managers to monitor, review, and close |
| 5 | Add deployment-related entities | Assigned to AI Risk & Compliance Managers |

#### Deploy Phase

- Flow: Deploy AI Asset Task Flow
- Trigger: AI Asset phase changes to Deploy

| **Step** | **Action** | **Details** |
| --- | --- | --- |
| 1 | Flow initiation | Triggers when AI Asset phase changes to *Deploy* |
| 1.1 | Create Deploy Asset task | AI asset approval task — type: *AI Governance Task* |

- Subflow called:
- Deploy AI Asset Task — executes asset deployment in the customer environment

#### Summary: AI System State Transitions and Tasks

- The table below provides a consolidated reference for all lifecycle stages, their triggering actions, responsible personas, and resulting state transitions. AIRC-specific tasks are italicized to distinguish them from AICT-native tasks.

| **# Application** | **Action Taken** | **Action Taken By** | **Lifecycle Stage** | **Lifecycle Status** | **State** |
| --- | --- | --- | --- | --- | --- |
| 1 Employee Center | Intake | AI Asset Owner | New | AI Steward Review | Draft |
| 2 AI Control Tower | Start Review | AI Steward | Assess | In Review | Draft |
| 2.1 AI Control Tower | Task: Impact Assessment | AI Asset Owner | Trigger: Assess/In Review — type: *Impact Assessment* |  |  |
| *2.1.1 AI Risk & Compliance* | *Task: AI Impact Assessment* | *AI Risk & Compliance Manager* | *Trigger: Assess/In Review — type: AI Assessment* |  |  |
| 2.2 AI Control Tower | Task: Legal Collaboration | AI Asset Owner | Trigger: Assess/In Review — type: AI Governance Task |  |  |
| 2.3 AI Control Tower | Task: Security Clearance Collaboration | AI Asset Owner | Trigger: Assess/In Review — type: AI Governance Task |  |  |
| 2.4 AI Control Tower | Task: Architecture Review | AI Asset Owner | Trigger: Assess/In Review — type: AI Governance Task |  |  |
| *2.5 AI Risk & Compliance* | *Task: Perform Risk Assessment* | *AI Risk & Compliance Manager* | *Trigger: Impact Assessment complete — type: Risk Assessment* |  |  |
| 3 AI Control Tower | Mark Assess Complete | AI Steward | Build & Test | Approved for Development | Draft |
| 3.1 AI Control Tower | Task: Create Control Attestations | (System) Auto-sync with AIRC | Trigger: Build & Test/Approved for Development — type: *Create Control Attestation* |  |  |
| *3.1.1 AI Risk & Compliance* | *Task: Create Control Attestation* | *AI Risk & Compliance Manager* | *Trigger: Build & Test/Approved for Development — type: AI System Task* |  |  |
| 3.2 AI Control Tower | Task: Collect Deployment Region Information | AI Asset Owner | Trigger: Build & Test/Approved for Development — type: *Information Collection* |  |  |
| *3.2.1 AI Risk & Compliance* | *Task: Share Deployment Details* | *AI Risk & Compliance Manager* | *Trigger: Build & Test/Approved for Development — type: AI System Task* |  |  |
| 4 AI Control Tower | Mark Development Plan Complete | AI Steward | Build & Test | Ready for Deployment | Build |
| 4.1 AI Control Tower | Task: Review Issues and Policy Exceptions | (System) Auto-sync with AIRC | Trigger: Build & Test/Ready for Deployment — type: *Other* |  |  |
| *4.1.1 AI Risk & Compliance* | *Task: Review Issues, Policy Exceptions, Control Attestation, and Risk Assessment* | *AI Risk & Compliance Manager* | *Trigger: Build & Test/Ready for Deployment — type: AI System Task* |  |  |
| 4.2 AI Control Tower | Task: Conformity Assessment | AI Asset Owner | Trigger: Build & Test/Ready for Deployment — type: *Conformity Assessment* |  |  |
| *4.2.1 AI Risk & Compliance* | *Task: AI Impact Assessment for EU AI Act Conformity* | *AI Risk & Compliance Manager* | *Trigger: Build & Test/Ready for Deployment — type: AI Assessment* |  |  |
| 4.3 AI Risk & Compliance | Task: Add Deployment- Related Entities | AI Risk & Compliance Manager | Trigger: Build & Test/Ready for Deployment — type: AI System Task |  |  |
| 5 AI Control Tower | Mark Pre-Deployment Plan Complete | AI Steward | Deploy | Approved for Deployment | Build |
| 5.1 AI Control Tower | Task: Deploy Asset | AI Product Owner | Trigger: Deploy phase — type: AI Governance Task |  |  |

### Customization Guide

#### Intake Form Configuration — AICT Workspace

- To make custom fields available on the AICT workspace intake form:
1. As an admin, open the form view for the table containing your custom fields in UI16
2. Change the form view to Intake — the view should match what appears in the AICT intake form
3. Right-click the form header and open Form Builder to update the Intake view
4. Add the custom field to the form layout and save
5. Open the intake form in AICT — the custom field should now be visible

> [!note] Note
> These are tables for AI system, AI Model, Prompt, Dataset etc. and their corresponding product model tables.

#### Lifecycle Configuration

##### Adding, Modifying, or Deleting Lifecycle Phases

- The guidance below is based on draft notes and should be reviewed for accuracy and completeness before publishing.
- Before making changes to lifecycle phases, note the following constraints:
- Do not delete OOB phases — deletion of out-of-the-box lifecycle phases is not recommended
- Do not reorder OOB phases — avoid placing Assess after Build & Test or otherwise altering the standard sequence; see the *Playbook: AI Asset Lifecycle* section for more detail
- Adding new phases — AI Stewards can add entries to the `sn_ai_governance_lifecycle` table, then update the playbook accordingly
- Steps to add a new lifecycle phase:
1. Add a new lifecycle phase entry to the AI Asset Lifecycles table `[sn_ai_governance_lifecycle]`
- Complete remaining steps for adding, modifying, and deleting lifecycle phases.

### Assess

#### Flow: AIRC flow once AI Gov Details is in assess phase

| **Step** | **Action / Task** | **Details / Task Type** |
| --- | --- | --- |
| 1 | Flow initiation | Triggers once AI Governance Details enter *Assess* phase |
| 1.1 | Transition to Assess phase | Trigger point: AI Governance Details record moves to Assess |
| 1.2 | Create AI system *Impact Assessment* task | AI asset approval task of type *Impact Assessment* |
| 1.3 | Assign AI Impact Assessment task | Task created for AI Risk and Compliance managers |
| 1.4 | Complete and review Impact Assessment task | AI Asset Owner completes it; AI Risk & Compliance Manager reviews and closes |
| 1.5 | Sync Impact Assessments tasks | AICT and AIRC assessments tasks kept in sync |
| 2 | Create Collaboration with legal team for AI use case task | Create AI approval task of type *AI Governance Task* |
| 3 | Create Collaboration for security clearance on AI use case development task | Create AI approval task of type *AI Governance Task* |
| 4 | Create Architecture review for AI use case task | Create AI approval task of type *AI Governance Task* |

#### Flow: Assign analyst to AI System

| **Step** | **Action / Task** | **Details / Task Type** |
| --- | --- | --- |
| 1 | Flow initiation | When AI system impact assessment is closed |
| 1.1 | Update AI system record (i.e assign analyst field to the user who closed the task) | Assign risk analyst on AI system to the user who closed the task |

#### Flow: Generate Risk Assessment

| **Step** | **Action / Task** | **Details / Task Type** |
| --- | --- | --- |
| 1 | Flow initiation | Generate risk assessment triggers when AI system record is updated |
| 1.1 | Create ‘Perform risk assessment’ task | AI approval task of type *Risk assessment* |
| 1.2 | Create object-based Risk Assessment ‘Generate risk assessment’ | For the AI System, and assign to AI Risk and Compliance user |
| 2 | Complete Risk Assessment | Task completed by AI Risk and Compliance user |
| 3 | Sync Risk Assessments | AI approval task and object-based assessment in AICT and AIRC are kept in sync |

The 'AIRC flow once AI Gov Details’ flow calls several Sub-flows during this process in the assess phase
- Calls: Trigger Smart Assessment- to initiate Impact assessment
- Calls: Map AI Control objectives to AI System - upon completion of impact assessment, when it is sent for AIRC review and adds controls after review complete
- Calls: Map AI Risk Statements to AI System - upon completion of impact assessment, when it is sent for AIRC review and adds risks after review complete
- Calls: Change assessment state - updates impact assessment state
- Calls: Assign analyst to AI system - upon completion of the assessment review captures the analyst that completed the review on the ai system record
- Calls: Generates risk assessment - upon completion of the assessment generates a risk assessment for the AIRC analyst to determine risk

> [!note] Note
> From AICT the Impact assessment is taken and TASK moves to In Review. In AIRC the AI Impact Assessment progresses to Review as well. This is when AIRC user persona closes the AI Impact assessment which marks the Impact assessment to closed in AICT.

#### Build and Test:

Review for Development: Flow: AIRC flow once AI Gov details is approved for development

| **Step** | **Action** | **Details / Task Type** |
| --- | --- | --- |
| 1 | Flow initiation | Triggers when lifecycle status changes to *Approved for development* |
| 1.1 | Create ‘ *Create Control Attestation’* task | AI asset approval task of type *Create Control Attestation* |
| 1.2 | Assign Control Attestation task | Task assigned to AI Risk and Compliance managers |
| 1.3 | Complete Control Attestation | Completed and closed by AI Risk and Compliance manager |
| 2 | Sync Control Attestations | Control attestations in AICT and AIRC are kept in sync |
| 3 | Create Collect deployment region information task | Create AI asset approval task of type *Information Collection* |
| 4 | Create Share deployment details task | Task for AI Risk and Compliance managers |

The ‘AIRC flow once AI Gov details is approved for development’ flow calls several Sub-flows during this process in the assess phase
- Calls: Create control attestation lifecycle task -sub-flow responsible for creating the control attestation lifecycle task in the flow
- From AICT the Collect information on the deployment regions of the AI system is addressed moving it to in review a. In AIRC the Share deployment details of the AI system progresses to complete. This is what completes the task in both AIRC and AICT.
- From AIRC Creates control attestations is completed.From AIRC Risk assessment is completed
- Review for Deployment- Flow: AIRC flow once AI Gov details is ready for deployment**

| **Step** | **Action** | **Details / Task Type** |
| --- | --- | --- |
| 1 | Flow initiation | Triggers when lifecycle status changes to *Ready for Deployment* |
| 1.1 | Create *Review Issues and Policy Exceptions* task | AI asset approval task of type *Other* |
| 1.2 | Assign task to review issues, policy exceptions, control attestation, and detailed risk assessment | Assigned to AI Risk and Compliance managers |
| 1.3 | Complete review task | AI Risk and Compliance Manager completes and closes it |
| 2 | Sync task records | Records kept in sync across AICT and AIRC |
| 3 | Create *Conformity Assessment* task | AI asset approval task of type *Conformity Assessment* |
| 4 | Create *AI Impact Assessment for EU AI Act conformity* | Task for AI Risk and Compliance Managers to monitor, review, and close |
| 5 | Add deployment-related entities | Task assigned to AI Risk and Compliance Managers |

## Deploy:

### Flow: Deploy AI Asset Task Flow

| **Step** | **Action** | **Details / Task Type** |
| --- | --- | --- |
| 1 | Flow initiation | Triggers when AI Asset phase changes to *Deploy* |
| 1.1 | Create *Deploy Asset* task | AI asset approval task of type *AI Governance Task* |

Calls: Deploy AI Asset Task – to deploy AI asset in the customer environment

## Summary of AI System asset - State Transitions & Tasks

|  | **Application** | **Action *taken*** | **Action** ***taken by*** | ***Lifecycle stage transitioned to*** |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| New Lifecycle phase | Lifecycle status | State |  |  |  |  |
| 1 | Employee | Intake | AI Asset | New | AI steward | Draft |
|  | Center |  | Owner |  | review |  |
| 2 | AI Control Tower | Start review | AI Steward | Assess | In review | Draft |
| 2.1 | AI Control Tower | Task: Impact Assessment | AI Asset Owner | Trigger: Flow transition to Assess, In review Task type: Impact assessment |  |  |
| *2.1.1* | *AI Risk and Compliance* | *Task: AI impact assessment* | *AI Risk and Compliance Manager* | *Trigger: Flow transition to Assess, In review Task type: AI assessment* |  |  |
| 2.2 | AI Control Tower | Task: Collaboration with legal team for AI use case | AI Asset Owner | Trigger: Flow transition to Assess, In review Task type: AI governance task |  |  |
| 2.3 | AI Control Tower | Task: Collaboration for security clearance on AI use case development | AI Asset Owner | Trigger: Flow transition to Assess, In review Task type: AI governance task |  |  |
| 2.4 | AI Control Tower | Task: Architecture review for AI use case | AI Asset Owner | Trigger: Flow transition to Assess, In review Task type: AI governance task |  |  |
| *2.5* | *AI Risk and Compliance* | *Task: Perform risk assessment* | *AI Risk and Compliance Manager* | *Trigger: Task Impact Assessment complete Task type: Risk assessment* |  |  |
| 3 | AI Control Tower | Mark as Complete (“Assess”) | AI Steward | Build and test | Approved for development | Draft |
| 3.1 | AI Control Tower | Task: Create control attestations | (System) Auto sync with AIRC | Trigger: Flow transition to Build and test, Approved for deployment Task type: Create control attestation |  |  |
| *3.1.1* | *AI Risk and Compliance* | *Task: Create control attestation* | *AI Risk and Compliance Manager* | *Trigger: Flow transition to Build and test, Approved for deployment Task type: AI system task* |  |  |
| 3.2 | AI Control Tower | Task: Collect information on the deployment regions of the AI system | AI Asset Owner | Trigger: Flow transition to Build and test, Approved for deployment Task type: Information collection |  |  |
| *3.2.1* | *AI Risk and Compliance* | *Task: Share deployment details of the AI system* | *AI Risk and Compliance Manager* | *Trigger: Flow transition to Build and test, Approved for deployment Task type: AI system task* |  |  |
| 4 | AI Control Tower | Mark as Complete (“Development plan”) | AI Steward | Build and test | Ready for deployment | Build |
| 4.1 | AI Control Tower | Task: Review issues and policy exceptions | (System) Auto sync with AIRC | Trigger: Flow transition to Build and test, Ready for deployment Task type: Others |  |  |
| *4.1.1* | *AI Risk and Compliance* | *Task: Review issues, policy exception, control attestation and detailed risk assessment* | *AI Risk and Compliance Manager* | *Trigger: Flow transition to Build and test, Ready for deployment Task type: AI system task* |  |  |
| 4.2 | AI Control Tower | Task: Conformity assessment | AI Asset Owner | Trigger: Flow transition to Build and test, Ready for deployment Task type: Conformity assessment |  |  |
| *4.2.1* | *AI Risk and Compliance* | *Task: AI impact assessment for EU AI Act conformity assessment* | *AI Risk and Compliance Manager* | *Trigger: Flow transition to Build and test, Ready for deployment Task type: AI assessment* |  |  |
| 4.3 | AI Risk and Compliance | Task: Add the deployment related entities | AI Risk and Compliance Manager | Trigger: Flow transition to Build and test, Ready for deployment Task type: AI system task |  |  |
| 5 | AI Control Tower | Mark as Complete (“Pre- deployment plan”) | AI Steward | Deploy | Approved for deployment | Build |
| 5.1 | AI Control Tower | Task: Deploy Asset | AI Product Owner | *Trigger: Flow transition to Deploy Task type: AI governance task* |  |  |

## Customization Guide

### Intake Form Configuration – AICT Workspace

If customers choose to add custom fields to the AI asset tables or product model tables for various types of AI Assets, they can make these fields available on the AICT workspace’s asset intake form by following the steps below:
1. As an admin user, open the form view for the table containing your custom fields in UI16.
2. Change the form view to “Intake”. The new form view should resemble what you see in the AICT intake form.
3. Right click on the form header and open form builder to update the "Intake” view.
4. Add your custom field to the form layout and save it.
5. Open the intake form in AICT and your custom field should now be visible on the page.

Intake Form Configuration – Employee Centre[MS1]

### Lifecycle configuration

#### Add/Delete/Modify Lifecycle Phases

Rough notes:
- Deletion of an OOB phase is not recommended at all
- It is ideal to not update the Order of the OOB phases. I.e. do not place Assess after Build. For more information on editing existing phases please refer to the “Playbook: AI Asset Lifecycle” section
- To add new lifecycle phases, an AI steward can add more entries to the sn_ai_governance_lifecycle table, then update the playbook

If customer wants to add, modify or delete lifecycle phases, they can follow the below steps:
1. Add a new lifecycle phase to AI Asset Lifecycles (sn_ai_governance_lifecycle) table.

> **[Figure 125 — p.190]** Platform form for an 'AI Asset Lifecycle - Risk Evaluation' record with Lifecycle phase = Risk Evaluation, Domain = global, and Update / Delete buttons.

2. Navigate to flow designer > Playbooks.
3. Find the relevant playbook. Click on the Add icon in the required position and fill the form. E.g:

> **[Figure 126 — p.190]** Workflow Studio 'AI Asset Onboarding' playbook (Diagram view) with the '3. New Stage properties' panel open — Label 'Risk Evaluation', Description, and a Schedule section set to 'After specific stages' starting after '2. Build and test' — plus Cancel / Save and close.

4. Save and close
5. Click on the Add icon in step 3 and select ‘Add an activity'

> **[Figure 127 — p.191]** Workflow Studio 'AI Asset Onboarding' playbook diagram view showing the stage sequence with a sticky note attached to one of the middle stages.

6. Select any of the activity under AI Asset Management as shown below

> **[Figure 128 — p.191]** Workflow Studio 'AI Asset Onboarding' playbook with the 'Add activity' dialog open, searching 'ai asset' and showing the AI Asset Management category with 'AI asset lifecycle list activity' and 'AI asset offboard list activity' options, plus Create new activity / Create new automation buttons.

7. Fill the form as below

> **[Figure 129 — p.192]** Workflow Studio 'AI Asset Onboarding' playbook with the '3.1 Risk Evaluation properties' Details tab open — Label 'Risk Evaluation', Description, Activity definition, and a Schedule set to 'When stage starts'.

> **[Figure 130 — p.192]** The same activity's Automation tab: Automation 'AI asset lifecycle assessment flow' with Inputs for Process, Assignment Group (AI Stewards), Assigned To, Wait for user input (Yes), Assessment request, Current task phase (Risk Evaluation), Entry lifecycle phase (Risk Evaluation) and Entry lifecycle status.

> **[Figure 131 — p.193]** The same activity's UI Layout tab: UI View, Table 'AI Asset Governance Details', Title 'Risk Evaluation', List Title 'AI Asset Governance Details', Associated record, Associated table, Empty state heading label 'No risk evaluation task created', Row Count and List Query / Add Condition.

#### Add new tasks to a particular phase

1. Onboarding and Offboarding Lifecycle Tasks (Demo vs OOTB/ System-defined) [MS1]
2. Scheduler Jobs, if any
3. Synchronization Jobs, if any
4. Map AI Risk Statements to AI System,
5. Map AI Control objectives to AI System
6. Map Use and Purpose to AI system**[MS2]**

### Resources - Workflow Automation Center of Excellence

#### Playbook Resources

1. Playbook best practices
2. Getting started
3. Playbooks Academy
4. ServiceNow Trainings

#### Flows and Sub-Flows

1. Flow Designer best practices
2. Getting Started with Flows
3. Recommendations

# Observe - Trace Collectors

Traces provide end-to-end visibility into AI agent activity as requests travel through distributed systems—microservices, databases, and APIs. Within AI Control Tower (AICT), the Trace Collectors feature enables teams to establish connections with cloud hyperscalers to collect structured trace data from externally hosted AI agents and route it to ServiceNow's observability service.

This guide covers the configuration, management, and governance of trace collectors across the following supported cloud providers:

| **Release** | **Cloud Provider** | **Scope** |
| --- | --- | --- |
| Feb Innovation Lab | AWS AgentCore | Trace collection from AWS-hosted AI agents |
| Feb Innovation Lab | GCP Vertex AI | Trace collection from Google Cloud AI agents |
| Mar Innovation Lab | Azure AI Foundry | Trace collection from Azure-hosted AI agents |

> [!important] Important
> Why Traces Matter in AICT Trace data flows into three core AICT capabilities: AI Evaluations (observability metrics), AI Discovery (supplemental agent metadata), and Security & Privacy (Galileo-driven security metrics). A single trace configuration surfaces value across all three areas.

## Prerequisites

Complete the following before configuring a trace collector. Incomplete prerequisites are the most common cause of failed connections.

| **Requirement** | **Details** | **Owner** |
| --- | --- | --- |
| Cloud Credentials Authentication credentials for the target cloud provider (AWS, GCP, or Azure) | Must be pre-created in the ServiceNow Credentials module before starting configuration. | Platform Admin |
| Active MID Server ServiceNow MID Server installed, validated, and in Active status | The MID Server acts as a secure intermediary between ServiceNow and the cloud provider. See MID Server Installation docs. | Platform Admin |
| Collection Frequency Defined polling interval in minutes | Work with AI agent owners to align on an appropriate collection frequency before configuring. | AI Program Lead |
| Credential Alias (Feb Release only) API Key credential alias for the observability service | Required only for the February Innovation Lab release. Not required for the March release onwards. | Platform Admin |
| AWS Region (AWS only) Specific AWS region where AI agents are deployed | Required only for AWS AgentCore connections. Confirm the region with your cloud team before proceeding. | Cloud/Platform Team |

## Configuration Steps

Follow this procedure to configure a trace collector in AI Control Tower. Steps apply to all supported cloud providers unless noted.

### Step 1 Access Trace Configuration

1. Navigate to the AI Control Tower workspace in your ServiceNow instance.
2. Go to Configurations > AI Evaluations > Traces.
3. Click Add.
4. Select your cloud provider connector (AWS, GCP, or Azure).

### Step 2 Fill In Trace Configuration Fields

Complete all required fields in the trace configuration form. The table below describes each field, its purpose, and guidance for implementation teams.

| **Field** | **Req.** | **Description** | **Implementation Guidance** |
| --- | --- | --- | --- |
| Name | ✓ | A descriptive label for this trace configuration. | Use a naming convention that identifies the provider, environment, and purpose. Example: AWS-Prod- AgentCore-1 |
| Credential | ✓ | Authentication credentials for your cloud provider. | Pre-create in the Credentials module. Test connectivity before saving the trace config. Feb release: AWS and GCP only. Mar release: Azure added. |
| Collection Frequency (minutes) | ✓ | Polling interval (in minutes) for the MID Server to collect new trace data from the cloud provider. | Align with AI agent owners on frequency. Higher frequency increases data freshness but adds load. Start with 15–30 minutes and adjust. |
| MID Server | ✓ | The ServiceNow MID Server that executes the trace collection process. | Verify MID Server status is Active and validated before selecting. Reference: MID Server Installation Docs. |
| Credential Alias | * | API Key: Credential alias for routing trace data to the ServiceNow observability service. | Feb Innovation Lab release only. Create the credential alias in advance. Not required for Mar release. |
| AWS Region | * | AWS region where AI agents are deployed. | AWS AgentCore connections only. Confirm with your cloud team. Using the wrong region will result in no traces collected. |

- Required only for specific releases or providers as noted.

### Step 3 Submit and Verify

1. Submit the form after all required fields are complete.
2. The new trace connection appears in the Connections table.
3. Click the connection to review its details and execution logs.
4. Confirm trace data begins populating in AI Evaluations after the first collection interval.

## Downstream Impact in AI Control Tower

Trace data collected through this configuration flows into three distinct AICT capabilities. Implementers should ensure stakeholders in each area are informed during rollout.

| **AICT Capability** | **How Traces Are Used** | **Primary Stakeholder** |
| --- | --- | --- |
| AI Evaluations | Trace data is forwarded to the monitoring service to generate observability metrics—latency, performance, error rates—for externally hosted AI agents. | AI Program Lead / AI Operations |
| AI Discovery | Traces surface AI agent metadata (e.g., AWS AgentCore agent info) not captured through standard discovery connections, enabling comprehensive inventory management. | AI Asset Manager |
| Security & Privacy | Trace data is routed to Galileo for security metric generation, enabling risk and compliance teams to evaluate AI agent behavior against defined security policies. | Risk & Compliance Lead |

## Troubleshooting

| **Issue** | **Likely Cause** | **Resolution** |
| --- | --- | --- |
| Credential not appearing in dropdown | Credential has not been created in the ServiceNow Credentials module. | Create the credential in the Credentials module first. Then return to the trace configuration. |
| MID Server cannot be selected or is unavailable | MID Server is not Active or has not been validated. | Verify the MID Server status and run validation. See MID Server Installation reference documentation. |
| No trace data appearing after first collection | Wrong AWS region selected, or cloud credentials lack required permissions. | Confirm the AWS region with your cloud team. Review credential permissions for trace collection APIs. |
| Trace connection created but execution logs show errors | Credential alias not configured (Feb release) or observability service is unreachable. | Verify the Credential Alias field is populated (Feb release). Confirm observability service connectivity from the MID Server. |

## References & Related Resources

• MID Server Installation Documentation: https://www.servicenow.com/docs/r/servicenow-platform/mid-server/mid-server-install ation.html

• AI Control Tower Overview — AI Control Tower workspace in your ServiceNow instance

• Credentials Module — ServiceNow Platform > Connections & Credentials > Credentials

• AI Evaluations documentation — AI Control Tower > Configurations > AI Evaluations

# Measure - Value

The Value Management capability in AI Control Tower (AICT) enables organizations to quantify and visualize the business impact of AI assets across environments.

## Value Management

The Value Management capability in AI Control Tower (AICT) enables organizations to quantify and visualize the business impact of AI assets across environments.

The Value tab provides standardized dashboards that measure:
- Productivity gains
- User engagement
- System utilization
- Return on investment (ROI)

Value insights are driven by Value Templates, which define the formulas and metrics applied to AI assets, including:
- AI Skills
- AI Agents
- Agentic Workflows
- Third-party integrations

## Release Compatibility

| **Release** | **Version Availability** |
| --- | --- |
| May | Innovation Lab only (YP3) |
| July | YP6, ZP1 |
| December | YP11, ZP4 |

## Roles and Responsibilities

| **Role** | **Description** |
| --- | --- |
| AI Steward ( `sn_ai_governance.ai_steward` ) | Oversees execution of AICT initiatives, ensures adherence to governance policies, and manages cross-functional coordination |
| AI Asset Owner ( `sn_ai_governance.ai_asset_owner` ) | Owns lifecycle management of AI assets and ensures value measurement alignment |

## Real-World Time Savings (RWTS) and AI Value

### Overview

Real-World Time Savings (RWTS) is a core metric used in AI Control Tower (AICT) value reporting to estimate human effort avoided through AI-assisted work. RWTS should be positioned as a standardized, assumption-based proxy metric designed for scalable value measurement and portfolio-level trending—not as a literal stopwatch or precise measure of user productivity.

Customers commonly question how RWTS translates into “minutes saved,” particularly for summarization and assist-based skills. Most confusion stems from misunderstanding what the metric represents, how assumptions are applied, and how AI usage correlates to measurable business value.

### What RWTS Measures

RWTS estimates time savings by converting AI input and output token volumes into time-equivalent estimates using standardized reading and writing speed assumptions.

The RWTS calculation is based on:

$RWTS = \left(\frac{\text{Total Read Tokens}}{\text{Reading Speed}}\right) + \left(\frac{\text{Total Write Tokens}}{\text{Writing Speed}}\right)$

This produces an estimated average time savings per skill execution, which is why the metric is often presented as an “average RWTS per skill.”

For assist-based or non-generative skills, AICT uses a directional guideline of:

$1\ \text{Assist} \approx 1\ \text{Minute Saved}$

This approximation is intentionally simplified to support scalable value reporting across large AI portfolios.

### Why RWTS Uses Assumptions

RWTS relies on standardized assumptions—such as approximately 300 words per minute for reading and 80 words per minute for writing—to normalize value calculations across varying users, tasks, industries, and use cases.

These assumptions exist to:
- Enable consistent cross-customer and cross-skill comparisons
- Support portfolio-level AI value trending
- Create a repeatable and scalable reporting model
- Provide directional ROI insights without requiring task-by-task manual measurement

Without normalization assumptions, value comparisons across AI implementations would become inconsistent and operationally difficult to measure.

RWTS is therefore intended for strategic trending and governance reporting rather than precise per-user productivity measurement.

### RWTS and Task Complexity

Customers may question whether assist counts or AI interactions directly correlate to actual productivity gains. Product guidance acknowledges that real-world task duration varies significantly depending on complexity, context, and user behavior.

As a result:
- RWTS should be treated as a proxy indicator of effort avoided
- Assist-based estimates are directional rather than deterministic
- The metric is not intended to represent guaranteed productivity gains for every interaction

The value model is intentionally abstracted to support scalable enterprise reporting while maintaining reasonable defensibility.

### Recommended Customer Positioning

When discussing RWTS with customers, position the metric as:

“A standardized estimate of human effort avoided, used to compare AI value consistently across skills and use cases—not a promise of exact minutes saved for every user.”

It is also important to reinforce that:
- RWTS is designed for comparative and trending analysis
- AICT value reporting emphasizes consistency over exact precision
- Customers may contextualize or refine assumptions using their own operational benchmarks for executive ROI discussions

### Implementation Considerations

- Ensure stakeholders understand that RWTS is an estimated value metric, not a direct productivity audit
- Use RWTS primarily for trend analysis, adoption reporting, and portfolio-level value measurement
- Align executive reporting with the directional nature of the metric
- Avoid positioning RWTS as a contractual or guaranteed time-savings claim
- Supplement RWTS with customer-specific KPIs where higher precision is required

## Value Templates

### Definition

Value Templates define the calculation logic used to measure AI-driven productivity and value realization.

### Out-of-Box Templates

- Third-party Assets
- ServiceNow Skills
- ServiceNow Agents
- Agentic Workflows

Adding a New template
1. Go to: Workspaces > AI Control Tower->AI Asset-> Productivity-> Value templates
2. Click: New Template

> **[Figure 132 — p.201]** 'Add value template' wizard on the Formula step for an Agentic AI asset: a Calculation builder mapping Process → Agent, Time-unit type → Constant, Exclusions rate type → Constant, with Stage 'AiValue - Daily Agent Executions', and Template details (Template name 'AI agent - Change', Template category 'Productivity', Description).

3. Fill in required fields and click next

> **[Figure 133 — p.201]** 'Add value template' wizard on the Map step: AI system type Agentic AI with a Select dropdown listing candidate agents (Assess conflicts for a change request, Assess quality of a Change Request, Change CI suggestion AI agent, Change conflict session AI agent, Change outage assistant AI agent, Change quality session AI agent, Change Request Plans AI Agent, Control Objective Change Agent) and no data yet displayed.

4. Add mapping: select the AI system type and AI system to be mapped.
5. Preview the value estimate using the test feature for all mapped AI systems.
6. Select the AI system for preview and click Validate and calculate

> **[Figure 134 — p.202]** 'Add value template' wizard on the Test step: a Calculation output banner showing testing in progress for a named instance, formula 'AiValue - Daily Agent Executions * 10 Minutes * 70%', data collection frequency Daily, and a Selected assets and estimates table listing four Agentic AI agents with Testing status, Current Productivity (0 Hours), New Productivity and Change (%) all N/A, plus a 'Publish alert' button.

7. If the result are satisfactory, Click Publish
- Note: Upon Publish, Value daily job will trigger and calculate productivity and usage metrics surfacing in the Value dashboard.
- Edit an Existing Template
1. Navigate to: Workspaces > AI Control Tower->AI Asset-> Productivity-> Value templates
2. Select a template to edit, AI Agent change
- Behaviour depends on the template current state

| **Template State** | **Permitted Actions** |
| --- | --- |
| Published | • Metric fields cannot be edited.  • Template details (Department,  Description) can be updated.  • Mapping records can be added or  removed.  •  Use the Duplicate action to clone the template (with or without mapping  records). Cloned templates start in Draft state. |
| Draft | • All fields (metrics, template  details, mapping records) are editable.  •  Draft templates can be deleted or published. |

3. Edit fields as needed
4. Save as Draft → Validate → Publish
- Template Mapping
1. Navigate to: Workspaces > AI Control Tower-->AI Asset-> Productivity-> Template mapping
2. Click New record,
- a. Select the template, the persona filed is auto-populated from selected template
- b. Select the AI system type
- c. Select the Asset name to be mapped.

> **[Figure 135 — p.203]** AI Control Tower 'Productivity - Templates mapping' list (50 records) showing template records for AI agents and Now Assist skills, with the 'New mapping record' modal open (Template name, Persona, Asset value) and a 'Create mapping record' button.

Default Template
1. Navigate to: Configuration-> Controls-> Value templates-> Assign Default templates
2. Click – Assign default templates
3. Choose the template name and vendor
4. If vendor is ServiceNow, Select the AI system category (AI skill, AI agent or AI workflow)
5. If Vendor is other than ServiceNow, Select the template and vendor

> **[Figure 136 — p.203]** AI Control Tower Configurations > Value templates page, 'Default template mapping' list (Templates, Persona, Asset type, Skill type, Vendor, Updated, Updated by) with the 'Assign default template' modal open — Template name 'Amazon Default Template', Vendor 'Amazon' — and an 'Assign as default' button.

## Value Calculation Framework

AICT calculates productivity using a standardized formula:

$\text{Productivity} = \text{Usage} \times \text{Time Saved per Invocation} \times \text{Acceptance Rate}$

### Metric Definitions

| **Metric** | **Definition** |
| --- | --- |
| Persona | User role associated with the AI asset (e.g., Agent, Developer, Requestor) |
| Usage | Number of times an AI capability is invoked (tracked daily via PA indicators) |
| Time Saved | Estimated reduction in manual effort per invocation |
| Acceptance Rate | Percentage of AI outputs accepted by users |

### Metric Behavior

- Usage
- Derived from daily PA indicators
- Requires completion before scheduled value calculations
- Time Saved
- Can be:
- Static value (e.g., 15 minutes)
- Indicator-based
- Acceptance Rate
- Formula: Accepted Outputs ÷ Total Outputs
- Configurable as static or indicator-driven

### Sample Calculation (Illustrative)

| **Metric** | **Value** |
| --- | --- |
| Usage | 2,250 |
| Acceptance Rate | 30% |
| Time Saved | 5 minutes |

Outcome: Represents aggregate productivity gained from AI-assisted interactions.

## Performance Analytics (PA) Integration

| **Metric** | **Indicator** |
| --- | --- |
| Usage – Agents | AIValue - Daily Agent Executions |
| Usage – Skills | AIValue - Daily Skill Executions |
| Usage – Workflows | AIValue - Daily Agent Workflow Executions |
| Time Saved | AIValue - Daily Average Assist |
| Acceptance Rate | AIValue.CreatorMetrics.AcceptedCalls |

> [!warning] Warning
> Only daily indicators are supported

- Indicators must complete before value calculation jobs execute

## Multi-Instance Framework (MIF) Configuration

### Purpose

Enables value aggregation across production and sub-production environments

### Setup Steps

1. Register production instance in sub-production
2. Wait for auto-approval
3. Configure instance relationships in AICT workspace
4. Add sub-production instances under Multi-instance setup

> **[Figure 137 — p.206]** AI Control Tower Configurations > Multi-instance setup page: Sync rules tab with an 'AI inventory information' panel for adding managed instances, a Syncing instances field, a Data sharing preference section (currently Active, with Deactivate), and an FAQ panel on multi-instance framework, why to sync, what information syncs and how to configure MIF.

## Data Architecture

| **Table** | **Purpose** |
| --- | --- |
| `sys_gen_ai_usage_log` | Stores AI usage and assist metrics |
| `sn_ai_disc_ai_usage` | Tracks third-party AI usage |

## System Behavior and Automation

- Daily Jobs
- Calculate usage and productivity metrics
- Historical Data Job
- Generates 30 days of baseline data for new instances
- Indicator Dependency
- Value dashboards depend on successful PA indicator execution

### Default Value Assumptions

Place this first to establish baseline logic:
- 15-minute time saved
- 50% acceptance rate
- Clarify these are:
- OOB template assumptions
- Overridable via Value Templates

### Data Initialization and Historical Data Generation

This is where the bulk of your content belongs.

Include:
- AIValue Generate Historical Data job behavior
- Hourly execution logic
- Dependency on PA indicators
- Auto-deactivation after 30-day backfill

### Post-Clone and New Instance Data Availability

This is the exact home for your troubleshooting content.

Include:
- Why dashboards appear empty
- Required system conditions
- Dependency chain explanation

### Required Jobs for Data Visibility

Break this out clearly:
- PA indicator jobs must run
- `aivalue.valuedashboard.HistoricalJob`
- AIValue historical script must be active

## Third-Party AI Asset Handling

- Usage tracked via `sn_ai_disc_ai_usage`
- Default calculation model:

Invocation Count × 15 minutes × 50% acceptance

> [!note] Note
> Default assumptions are configurable via custom templates

## Operational Considerations

### Indicator Breakdown

- Required for asset-level accuracy
- Prevents aggregation errors across assets

### Data Availability Issues

If dashboards show no data:
- Verify PA indicators have executed
- Trigger historical data job manually
- Confirm scheduled jobs are active

#### Key Takeaways

- Value Management is template-driven and indicator-dependent
- Accurate measurement requires:
- Proper mapping
- Valid PA indicators
- Completed daily jobs
- Governance is enforced through:
- Role-based ownership
- Template lifecycle controls
- Standardized calculation models

#### Implementation Note

Value dashboard population depends on a sequential dependency chain:
1. PA indicators execute
2. Historical data is generated
3. Value calculations are applied
4. Dashboards are populated

Failure at any stage will result in missing or incomplete data visibility.

# Cross - Product Integration AI Strategy

ServiceNow is the single platform for managing AI strategy, intake, and execution. By combining AI Control Tower (AICT) with Strategic Portfolio Management (SPM), organizations can define AI goals, track AI investments as portfolio demands, and maintain end-to-end visibility from strategy through delivery.

| **WHY THIS INTEGRATION MATTERS** |
| --- |
| • Connect AI strategy to execution — not just monitoring |
| • Categorize and track AI investments alongside other portfolio work |
| • Give AI Stewards financial, risk, and pipeline visibility in one workspace |
| • Enable prioritization decisions with full organizational context |

## Required Plugins and Licensing

This integration requires the following plugins. Capabilities expanded as additional licenses are activated.

| **Plugin** | **License Required** | **Capability Unlocked** |
| --- | --- | --- |
| AI Control Tower | AICT License | AI strategy management, goals, targets, AI Steward dashboard |
| Goals Framework | Included — all customers | Create and align strategic goals with qualitative/quantitative targets |
| Strategic Planning | SPM Pro License | AI demand intake, project execution, portfolio planning, capacity and financial analysis |

> [!note] Note
> Without Strategic Planning (SPM Pro), organizations can define AI strategies and monitor goals in AICT, but cannot manage intake or execution within the same platform.

## Defining AI Strategies

AI strategies, goals, and targets are managed within AICT and serve as the north star for all AI investment decisions. This section covers setup and configuration.

> **[Figure 138 — p.210]** AI Control Tower 'AI strategies and goals - Strategic priorities' list showing three strategic-priority records (STR0001001/1003/1005) with Name, Description, Owner, Parent, Start date, End date and Type 'Artificial Intelligence' columns, plus Export and New buttons.

## Navigating to AI Strategy Records

From the AICT application, navigate to list. This section surfaces three record types used to build an AI strategy:

• AI Strategies — top-level strategic priorities for AI

• Goals — measurable objectives aligned to each strategy

• Strategic Plans — execution roadmaps tied to goals

## Creating a Goal

Users can open a Strategic Priority and select New Goal to define a goal aligned with their AI strategy.

Within the goal record:
- (Optional) The Category field may be set to Artificial Intelligence.
- Both qualitative and quantitative targets can be defined to measure success.

Optionally, the goal can be linked to an existing AI system:
- Set Assigned Entity to Product Model
- Select the relevant AI system

> **[Figure 139 — p.211]** 'Create New Strategic Priority' form with Name, Parent, Owner (System Administrator), Start/End date, Type 'Artificial Intelligence', Strategic Plan and a rich-text Description field, alongside a Comments / Activity stream.

create a target using the related list under the goal record

> **[Figure 140 — p.211]** SPM Goal record 'Deploy ServiceNow Case Summarization' with Details, Quantitative Targets, Qualitative Targets, Sub-goals, Planning Items and Other items tabs — Parent goal, Strategic priority, Start/End date 2025-07-01 to 2025-10-01, Owner, Category 'Artificial Intelligence', Status None, Impact on parent goal '(1) Neutral', Assigned entity type 'Product Model' and Assigned entity 'ServiceNow case summarization 1.0'.

AI Stewards can go to the Dashboard and, within the AI Strategy tab, monitor the progress of their strategic priorities, goals, and targets.

> **[Figure 141 — p.212]** 'AICT ROAD Dashboard' Strategy tab showing an 'AI goals status' donut, an 'AI targets to goal' stacked bar chart, and a 'Targets by AI strategic priorities' list of strategic priorities with Status and Progress indicators.

Required Plugins to Manage AI Strategy, Intake, and Execution
- AI Control Tower
- Goals Framework *(comes out-of-the-box for all customers)*
- Strategic Planning *(requires SPM Pro license)*

Managing AI Intake

Once Strategic Planning has been installed, customers can begin creating Demands with the Investment Type set to Artificial Intelligence. This enables categorization and tracking of AI-related intake items, ensuring they are aligned with the broader AI strategy.

These demands can then be converted into relevant execution items such as Projects and Epics for delivery and tracking.

> **[Figure 142 — p.213]** SPM 'Demand - New Record' form in Draft state with the Prioritization stepper (Draft, Submitted, Screening, Qualified, Approved, Completed), Name 'AI case summarization', Category Strategic, Type Project, and the Details tab where Investment Type is set to 'Artificial Intelligence' (highlighted in red).

> **[Figure 143 — p.213]** SPM Project record 'AI case summarization' (PRJ0010001) with Project Name, Project manager, State Pending, Percent complete, and the Details tab where Investment type is set to 'Artificial Intelligence' (highlighted), plus Portfolio, Program, Department, Phase Initiating and Execution type Waterfall.

Both Projects and Demands can be tracked using the Strategic Planning Workspace, where users can:
- View and prioritize AI-related work aligned to strategic goals
- Perform capacity planning, financial analysis, and scenario planning
- Explore trade-off decisions and investment options for AI initiatives
- Create Portfolio Plans and include the Investment Type column to filter and analyze AI-specific work
- Visualize all work—AI and non-AI—mapped to strategic goals and make informed prioritization decisions

This workspace empowers organizations to continuously align execution with AI strategy and optimize resource allocation.

> **[Figure 144 — p.214]** Strategic Planning Workspace 'ACME 2025 year plan' Planning view, Prioritization tab, listing demands (FY25 Seal Contracts Search and Analytics, Replace Legacy CS with ServiceNow, Offer Request Form, HR Information System Implementation, HR Service Portal, Migrate to ADP Payroll, and others) with Planning state, Planning item type, MoSCoW and Approved start columns, plus 'Scenario planning' and 'New demand' buttons.

> **[Figure 145 — p.214]** Strategic Planning Workspace 'Scenario: Optimize benefits' in SIMULATION MODE, showing a Portfolio outcomes / Financials panel (Capex and Opex targets and budgets, Total Benefit) and Strategic Alignment metrics beside the prioritised demand list, with an 'Approve scenario' button.

#### AI Control Tower Monitoring

AI Stewards can access the AI Control Tower Workspace and navigate to the AI Strategy tab to monitor:
- The status of their strategies, goals, and targets
- Associated costs and financial performance
- The prioritized work currently in progress

The pipeline of upcoming AI initiatives

Additionally, AI Stewards gain visibility into all execution-related governance elements, including:
- Risks
- Issues
- Decisions
- Actions
- Change Requests

Work items such as Demands, Projects, Epics, or other planning records can also be optionally associated with a specific AI system. This can be done by opening the relevant work record and using the Product field to link it to the appropriate AI system. This association provides traceability between strategic goals and the systems delivering them, while remaining flexible and non- mandatory

> **[Figure 146 — p.215]** 'Prioritized AI work' dashboard showing 'Ongoing AI work' and 'Upcoming AI work' horizontal bar charts grouped by planning state, plus an 'AI ROAD' section with Active Items counters (Risks 9, Assets 10, Obstacles 0, Actions 6, Changes 3) and a risk impact-by-probability heat strip.

> **[Figure 147 — p.216]** Browser view of the 'AICT ROAD Dashboard' Strategy tab listing strategic priorities with status badges, and a Goals section with a grouped bar chart of goal progress by AI strategic priority.

For more information, see SPM implementation learning program.

# Cross Product Integration - AI Case Management

This guide provides implementers with a structured, step-by-step approach to configure, and operationalize an AI Case Management solution that supports effective AI governance.

## Intended Audience

The intended audience for the AI Case Management Implementation Guide would be:
- Implementation Engineers / Solution Integrators – responsible for installing and configuring the solution
- AI Stewards – overseeing solution deployment in alignment with organizational AI governance strategy

## Understanding the AI Case Management Solution

### Overview of AI Case/ Inquiry

AI Case Management provides a centralized system for managing AI-related cases and inquiries — from initial submission through investigation, resolution, and regulatory reporting. The solution is designed to improve response times, strengthen oversight, and ensure issues are resolved at their root cause.

### Key capabilities

Include a single intake point for all AI cases and inquiries submitted through the Employee Center Portal, structured workflows for investigations and assessments, evidence and observation collection, regulatory violation tracking from initial report through to lodgement, and identification and resolution of issues in affected areas.

### Roles & Responsibilities

The roles and responsibilities outline the key stakeholders involved in implementing and operating the AI Case Management solution, defining their accountabilities across installation, configuration, governance, and ongoing compliance monitoring. Clear role assignment ensures effective collaboration, regulatory alignment, and sustained operational ownership of the solution.

Reading Article ([link](https://www.servicenow.com/docs/bundle/zurich-governance-risk-compliance/page/product/grc-ai-risk-compliance/reference/roles-installed-with-ai-risk-and-compliance.html))

## Solution Architecture

##### High-Level Architecture

The high-level architecture diagram below illustrates the core components, data flows, and integration points of the AI Case Management solution. It shows how AI Cases move through investigation or assessment to determine the corrective and preventive actions needed for resolution. Use this diagram as your primary visual reference when planning deployment and system integration.

> **[Figure 148 — p.218]** Dark-themed conceptual diagram of the AI Risk & Compliance data model: Employee Center intake (Report AI case, Raise an AI Inquiry) and internal goals/objectives, policies, control objectives and enterprise regulations/authority documents on the left, feeding the AI Asset Inventory (CMDB) of AI systems, models, datasets and prompts, which resolves to an Entity (AI system / model / dataset) and then to AI cases and inquiries with Impacted areas, Causes and consequences, Action tasks, and an Issue accept/remediate outcome.

> **[Figure 149 — p.218]** 'AI Control Tower SKU' plugin hierarchy tree: AI Control Tower (`sn_aict`) at the root, with AI Asset Management (`sn_ai_asset_mgmt`), AI Governance Risk & Compliance Integration (`sn_grc_ai_gov_integ`), AI Value / Productivity (`sn_ai_value`), AI Security (`sn_ai_security`) and Enterprise AI Discovery (`sn_ai_disc`) beneath it, plus AI Control Tower Core (`sn_ai_governance`), AI Risk & Compliance (`sn_grc_ai_gov`), AI Control Tower Core (`sn_ai_governance`) and CMDB Data Foundation (`sn_cmdb_foundation`) in the supporting chain.

Technical architecture and process flows here on seismic. Click here

Please see tables installed here: https://www.servicenow.com/docs/csh?topicname=tables-installed-with-ai-risk-and-complianc e.html&version=latest

## Configurations

### Case Types

Defining AI case types and sub-types creates a structured taxonomy that organizes cases consistently, improves reporting accuracy, and enables trend analysis across AI-related issues. Proper categorization supports automated routing and prioritization, leading to faster resolution. It also ensures governance and regulatory compliance by establishing consistent handling for similar cases — and scales as AI use cases and risk management needs evolve.

Common examples include Accuracy Degradation, Unexpected Behavior, Model Drift, and Data Quality.

For configuration steps, click here.

#### Inquiry Type

Defining AI inquiry types organizes incoming inquiries into clear categories for efficient tracking and resolution. It improves reporting accuracy, helps identify patterns in AI governance issues, and ensures inquiries are routed to the right teams with appropriate prioritization. This structure supports compliance monitoring, promotes consistent handling across AI-related questions, and adapts as regulatory landscapes evolve.

Common examples include Regulatory Requests, Data Privacy Clarification, and Bias Testing Documentation.

For configuration steps, click here.

#### State Models

A state model defines the workflow of a record by specifying the states a case or inquiry moves through, along with the conditions that govern each transition. Each case type or inquiry type follows the workflow states and transition conditions assigned to it.

There are three components to configure:

State Model — The state model establishes the overall framework of states and transitions for a given case or inquiry type. For configuration steps, click here.

Workflow State — Workflow states define the lifecycle stages of a case or inquiry within AI Case Management. To add new states, administrators create them directly in the State field of the AI Case table. For configuration steps, click here.

State Transitions — State transitions define the conditions that control how a case moves between workflow states. Using the condition builder in the State Transitions table, administrators can specify the required conditions for entering or exiting each state. For configuration steps, click here.

> **[Figure 150 — p.219]** Dark-themed matrix of industry case types and their state models: Financial (Credit Card Operations, Loan Operations) → New / In Progress / Complete; Public Sector (Service Request, Information Request) → New / In Progress / Investigate / Complete; Technology (Product Support, Account Onboarding) → New / In Progress / Investigate / Post Case / Complete; HealthCare (Device Onboarding) → New / In Progress / Complete.

#### Assessment Templates

Assessment templates provide a structured, repeatable way to gather information during the investigation of reported AI cases. They ensure consistent data collection, support comprehensive analysis, and help maintain compliance with governance and regulatory standards. Standardized formats enable investigators to identify root causes, assess risks, and recommend corrective actions while keeping documentation audit-ready.

The AI Risk and Compliance content accelerator includes a pre-defined template — the AI Case Assessment Questionnaire — designed to support thorough investigation of reported AI cases. Additional examples include an AI Bias Investigation Questionnaire, which captures data sources, bias detection methods, and remediation steps, and a Model Performance Deviation Assessment, which evaluates causes of accuracy drops, drift, or unexpected outputs.

Two important configuration steps accompany assessment templates. To make assessments available for use, the template must first be published — click here for steps. Post-assessment automation can also be configured to execute decision-making rules based on specific conditions, or to run automatically without conditions — click here for steps.

#### Causes

Causes are the underlying reasons or triggers behind an AI-related incident, inquiry, or compliance concern. Identifying causes accurately supports root-cause analysis, preventive action planning, and reduces the likelihood of recurrence.

Common examples include poor-quality or biased training data, inadequate model testing or validation, misconfigured AI workflows or decision rules, regulatory requirement changes that were not implemented, and unauthorized changes to AI model parameters.

For configuration steps, click here.

#### Consequences

Consequences are the effects or outcomes that result from an identified cause. These may be operational, regulatory, financial, reputational, or ethical in nature. Documenting consequences supports impact assessment, helps prioritize response efforts, and ensures remediation actions align with governance and compliance priorities.

Common examples include incorrect or biased AI decisions affecting customers, regulatory non-compliance leading to fines or sanctions, operational delays or service disruptions, loss of stakeholder trust, and ethical breaches impacting public perception.

For configuration steps, click here.

#### Document Templates

Standardized document templates ensure consistent data extraction for regulatory and audit reporting. They reduce manual effort, improve accuracy, and accelerate compliance submissions. Predefined formats align reports with specific regulatory requirements and audit scopes, and can be reused across similar reporting needs for greater efficiency.

Examples include a Regulatory Compliance Report Template such as EU AI Act conformity evidence, and an AI Model Bias Assessment Summary Template.

For configuration steps, click here.

#### SLA Definition

A Service Level Agreement (SLA) sets measurable commitments for case response and resolution, ensuring AI-related issues, inquiries, and compliance concerns are addressed within defined timeframes. SLAs align service performance with business, governance, and regulatory expectations, and include automated monitoring and escalation when commitments are at risk of being missed.

SLAs are typically structured by priority. A high-priority case such as a regulatory inquiry may require a response within 4 hours and full resolution within 2 business days. A medium-priority case such as a model performance issue may allow 8 hours for response and 5 business days for resolution. A low-priority general inquiry may allow 24 hours for response and 10 business days for resolution. Thresholds should be aligned to any applicable legal or regulatory deadlines.

For configuration steps, click here.

#### Applicability

Applicability configuration identifies the impacted and related areas that can be associated with a reported AI case or inquiry. These associations provide broader context, support impact analysis, and should be configured according to enterprise preferences.

Impacted areas include User, Company, Entity, Location, and AI Asset. Related areas include Control, Citation, Policy, Control Objective, and Risk Event. Cause-related associations can be linked to Department, Entity, and User.

### AI Case Management

AI Cases are structured records used to manage, track, and resolve inquiries, incidents, or investigations related to AI assets. They centralize relevant data, actions, and decisions to support faster resolution, greater transparency, and compliance with governance policies.

Primary actors include business users or AI asset owners who report cases, compliance officers who ensure regulatory adherence, AI model owners who provide technical context, and case managers who oversee resolution and closure.

Cases can be submitted through three channels. Employees can use the Employee Center Portal to submit AI-related cases by providing relevant details and supporting documents, ensuring timely routing and tracking — click here for steps. AI Risk and Compliance analysts can also submit cases manually through dedicated workspaces, enabling direct logging with supporting evidence — click here for steps. Cases can additionally be mapped to affected AI assets including AI systems, models, and datasets to enable reporting insights that support effective decision-making by AI Stewards and the AI Risk and Compliance team.

Common use cases include investigating potential bias in an AI model's decision output, responding to a regulator's request for AI asset documentation, managing change requests for retraining or updating AI models, and tracking remediation efforts for an AI system compliance gap.

#### Lifecycle of AI Cases

No content was provided for this section. Please supply the source content so it can be incorporated consistently with the rest of the guide.

> **[Figure 151 — p.221]** AI case lifecycle diagram: an Employee reports a potential bias in an AI model's decision output via the Employee Center, creating an AI Case; the Compliance Case Analyst then moves it through Investigation, Triage & Investigate, Resolve, Post Case Review and Close, with the activities in each stage listed and a collaboration band showing Finance, Employee, HR and Legal contributing to the evidence and resolution plan.

### Lifecycle of AI Cases

AI Risk and Compliance case analysts manage AI-related cases through five stages: triage, investigation, resolution, post-case review, and closure.

Cases enter the workflow when employees report an AI-related concern through the Employee Center Portal or submit anonymously via the Anonymous Reporting Center. Once received, analysts perform investigations, assess potential breaches, gather supporting evidence, and initiate remediation actions. Cases involving fraud or financial process failures follow dedicated workflows that bring in compliance, risk, and financial analysts as needed. Security breaches follow a parallel process in which security analysts and compliance case analysts collaborate on analysis, containment, eradication, and closure.

Throughout the investigation, the AI Risk and Compliance team reviews reports, assesses risks, and coordinates evidence collection, interviews, and legal counsel where required. Once findings are established, outcomes are documented and corrective actions are determined — these may include training, disciplinary measures, or policy updates. Affected parties are notified of case resolution in a manner that maintains appropriate confidentiality.

All activity is captured in a full audit trail to ensure transparency and support regulatory compliance. Following closure, post-case reviews are conducted to identify any systemic issues and drive continuous improvement of compliance policies and reporting mechanisms.

#### Workspace

> **[Figure 152 — p.222]** AI Risk and Compliance Workspace home, AI cases tab, with 'AI cases status by state' (7 active: Investigate, New, Resolve, Triage) and 'AI cases status by priority' (Critical, Moderate, Planning) donut charts and a 'Create AI case' button.

This dashboard provides the key metrics, trends, and actionable tasks that you can use to track your AI risks, case activities, compliance tracking, and governance enforcement

> **[Figure 153 — p.223]** AI cases list view with counters (All 7, Overdue 4, Due in 7 days 0, Unassigned 0) and rows for Bias in Loan Approvals (Data Poisoning), Challenges in Commercial Environments Due to Domain Adaptation Issues (Unauthorised AI Model Usage), Credit Scoring Algorithm Glitch (AI System Malfunction) and Discriminatory Interest Rates Based on Credit Score (Autonomy & Human Oversight), with case analyst and priority.

This dashboard shows summarized list of AI cases reported

> **[Figure 154 — p.224]** AI Risk and Compliance Workspace 'Trends' view: an 'AI cases by subtype' horizontal bar chart grouped by business area (Finance, IT, Legal, Sales) and an 'Open and closed cases' line chart across April–June 2025.

This dashboard shows Visual patterns and historical data that are associated with the AI cases

> **[Figure 155 — p.225]** AI Risk and Compliance Workspace 'Tracking' view for AI case tasks and issues, with Action tasks counters (Overdue 2, Due in 0, Unassigned 0) and a by-state donut (Draft, Work in progress), beside Issues counters (Overdue 3, Due in 0, Unassigned 0) and a by-state donut (New, Respond, Review).

This dashboard shows AI case progress at the task and issue level

#### Inquiries

AI-related inquiries are formal requests for information, clarification, or investigation about AI systems, their decisions, or compliance status. They are a critical component of AI governance, ensuring transparency, accountability, and adherence to regulatory and ethical standards.

Inquiries typically originate from AI asset owners, business users, or employees seeking compliance evidence, internal governance teams validating AI practices, business stakeholders requesting explanations of AI decisions, and AI system owners providing technical responses.

Inquiries can be submitted through three channels. Employees can use the Employee Center Portal to submit an inquiry by providing relevant details and supporting documents, ensuring timely routing and tracking — click here for steps. Where confidentiality is required, concerns can be submitted anonymously through the Anonymous Reporting Center. Compliance analysts can also submit inquiries manually from dedicated workspaces, enabling them to request information, clarification, or evidence about AI systems in a documented and trackable way — click here for steps.

Inquiries can be mapped to affected AI assets — including AI systems, models, and datasets — providing reporting insights that support effective decision-making by AI Stewards and the AI Risk and Compliance team.

Effective inquiry management leads to faster, well-documented responses, strengthens trust with regulators and stakeholders, improves overall compliance posture, and reduces risks associated with misaligned AI practices. Typical examples include a regulator requesting proof of bias testing for a high-risk AI model, an internal audit team asking for explainability reports on AI decision-making, a business unit querying the data sources used for AI training, and an ethics committee requesting documentation on fairness and transparency measures.

#### Lifecycle of Inquiries

> **[Figure 156 — p.226]** AI inquiry lifecycle diagram: an Employee submits a portal form asking how to ensure an AI model complies with the EU AI Act (with an optional additional-clarification form), creating a Compliance Request / Employee Inquiry that the Compliance Request Analyst moves through Triage, Work In Progress and Approve/Reject, with the validation, identification, and approval activities listed for each stage.

#### Lifecycle of AI Inquiries

AI Risk and Compliance analysts and AI Stewards manage AI-related inquiries through four stages: triage, resolution, approval, and closure.

Inquiries enter the workflow when employees submit them through the Employee Center Portal. Once received, the responsible analyst or AI Steward reviews the inquiry, assesses its implications for any affected AI assets, and prepares a response. Where decisions require broader input, approval requests are initiated with the relevant stakeholders before the inquiry is resolved and closed.

#### Workspace

> **[Figure 157 — p.227]** AI Risk and Compliance Workspace home, AI cases tab with the Inquiries sub-tab selected, showing 'Inquiries status by state' (11 active: Approved, In progress, New, Triage) and 'Inquiries status by priority' donut charts and a 'Create inquiry' button.

This dashboard provides you with a structured view of the AI inquiry workflow

> **[Figure 158 — p.228]** AI inquiries list view with counters (All 11, Active 10, High priority 4, Unassigned 3) and rows such as 'How do I ensure that the AI model we are using is compliant with the EU AI Act?', 'Am I allowed to use sensitive personal data in training our AI model...', 'How do I check if our AI model is biased...' and 'AI Model Lifecycle Management', with Requested by, Assigned to, State and Priority columns.

This dashboard shows summarized list of all inquiries

##### Learning Courses

ServiceNow offers comprehensive certification and training programs for those looking to become proficient in Integrated Risk Management (IRM). These programs are designed to equip professionals with the necessary skills to implement and manage IRM effectively within their organizations.

Here are some fundamental certification and training options available:
1. GRC: Integrated Risk Management (IRM) Fundamentals
2. GRC: Integrated Risk Management (IRM) Implementation
3. GRC: Introduction to Compliance Case Management
4. GRC Risk - Process Guide
5. IRM Workspace Overview Video
6. GRC Issue Management Process Guide: Provides detailed guidance on the way that ServiceNow intends the process to- be, for GRC Issue Management.
7. GRC Product Architecture Blueprint: Describes the inherent functionality of the Governance, Risk & Compliance (GRC) and outlines the technical components in the form of a diagram.

For end-user documentation covering Compliance Case Management, click here.

# Cross Product Integration - CMDB

AI Control Tower (AICT) stores all AI assets as configuration items (CIs) in the ServiceNow CMDB, within OOTB AI-specific CI classes. This approach gives AI assets the same lifecycle management, relationship mapping, and reconciliation capabilities as all other enterprise infrastructure.

This guide covers how AICT asset types map to CMDB classes, how AI CIs are connected to business applications and services through CSDM, when CIs are created during discovery or intake, supported AI implementation patterns, and the recommended two-gate process flow for integrating AICT into existing governance and release management practices.

## Asset Type to CMDB Class Mapping

AICT registers AI assets across three primary CMDB classes. Each class captures a distinct layer of the AI asset hierarchy, from top- level systems and agents down to the supporting digital assets that models depend on.

| **CMDB Table** | **AICT Asset Types** | **What It Stores** |
| --- | --- | --- |
| cmdb_ci_ai_system | AI Systems, Agents | Top-level container. Groups models, prompts, and datasets. Maps to business applications via CSDM. |
| cmdb_ci_ai_model | AI Models | Individual models (foundation, fine-tuned, custom). Tracks provider, version, and risk classification. |
| cmdb_ci_ai_digital_asset | Datasets, Prompts, Knowledge Bases | Supporting digital assets: training data, prompt templates, and RAG knowledge bases. |

> [!note] Note
> MCP Servers and Agents MCP servers and agents are also registered as CIs. The AICT application layer (sn_aict_* tables) manages governance workflows—intake, risk assessments, approvals, and value metrics—on top of these CMDB records.

## How AI Assets Enter the CMDB

AI CIs are created through five paths: automated discovery (scheduled or event-driven), connector-based discovery for hyperscaler platforms, manual intake via the AICT Workspace, and programmatic API registration. The discovery method determines when the CI is created and whether it enters as managed or unmanaged.

| **Method** | **What It Does** | **When CI Is Created** |
| --- | --- | --- |
| Now Assist Discovery | Hourly scheduled job discovers ServiceNow-native AI skills and agents automatically. | At discovery. No manual intervention required. |
| Hyperscaler Connectors | OOTB connectors for Amazon Bedrock, AWS AgentCore, Azure AI Foundry, Copilot Studio, and GCP. Creates new CIs and updates existing ones. | At discovery. Assets appear as unmanaged until governance onboarding is complete. |
| Trace-Based Discovery (Q1 2026) | Collects runtime traces from AWS AgentCore, GCP, and Azure. Supplements API-based discovery with prompts, datasets, and agent details. | Supplementary: enriches existing CIs and surfaces net-new assets from trace data. |
| Manual Intake | Form-based submission via AICT Workspace. Captures attributes, assigns CMDB class, and routes through governance. | At intake submission. Primary path for third-party tools and internally developed AI. |
| API Registration | Programmatic via CMDB IRE endpoint. Supports CI/CD pipeline integration and bulk operations. | At API call. |

## Automated Risk Classification at Intake (Q1 2026)

Risk assessment questions are now embedded in the intake form. High-risk or non-compliant submissions are auto-flagged for AI Steward review, ensuring CIs entering the CMDB carry an initial risk classification from day one—without requiring a separate triage step.

## Connecting AI Assets to Business Applications and Services

AI CIs are linked to business applications, services, and owning teams through CSDM. These relationships are visible directly in the AICT Workspace alongside governance status, evaluation scores, and security posture.

Key relationships in the CSDM model:

• AI systems are mapped to the business applications they power

• Models are linked to their parent AI systems

• Datasets, prompts, and knowledge bases are linked to the models that consume them

• All assets are associated with owning teams and business units

## Managed vs. Unmanaged Assets

Every CI in AICT exists in one of two governance states. The distinction determines which workflows, assessments, and measurement capabilities are active for that asset.

| **State** | **What It Means** | **What’s Enabled** |
| --- | --- | --- |
| Managed | Asset has completed AICT governance onboarding: intake, risk assessment, and approval. | Workflows, risk assessments, value measurement, monitoring, and evaluation scoring. |
| Unmanaged | Discovered or registered but not yet through governance. Visible to AI Stewards only. | Visible in inventory. No active governance workflows. AI Stewards move assets to Managed when ready. |

The Q1 2026 workspace provides dedicated navigation lists by asset type—AI systems, models, prompts, datasets, and MCP servers—for both managed and unmanaged inventories.

## AI Implementation Patterns

AI assets are deployed across three primary implementation patterns. Each pattern carries different implications for how CIs are discovered, registered, and related in the CMDB.

| **Pattern** | **Examples** | **CMDB Implications** |
| --- | --- | --- |
| Embedded AI | Now Assist skills in ServiceNow, AI features in CRM or ERP, intelligent document processing | AI system CI relates to the parent business application. Often auto- discovered (Now Assist) or submitted via manual intake (third- party). |
| Dedicated AI Platform | Amazon Bedrock, Azure AI Foundry, GCP Vertex AI, Copilot Studio | Platform is registered as a business applications. Individual models and agents are child CIs. OOTB connectors auto-discover. |
| Agent-to- Agent / MCP | Agents calling other agents via MCP, multi-agent orchestration, external tool access | Dependencies between agents are the primary governance concern. Capture agent topology in Enterprise Architecture. MCP is a gateway/integration technology; align governance with API Insights. |

### Recommended Process Flow: Two Governance Gates

For organizations with established Architecture Review Board (ARB) and release management processes, AICT should be integrated at two key gates. This approach ensures AI asset details are captured early, before deployment, and validated as complete before go-live.

## Gate 1: Architecture Review Board (Planning Stage)

The Architecture Review Board (ARB) is where the AI initiative intent is captured. Discovery cannot provide intent: it can surface what exists, but cannot answer why an asset was built, what business outcome it serves, or what its risk profile is. The ARB gate closes that gap.

• Identify which business applications have AI in them, or which platforms are acting as AI hosts

• Capture AICT details early: models, prompts, datasets, and integration patterns

• Register the business application in CMDB and CSDM

• Use Enterprise Architecture to document agent dependencies and MCP topologies

• Capture the ‘why’: business outcome, risk profile, purpose, and data sensitivity classification

## Gate 2: Digital Product Release (Deployment Stage)

The release gate ensures AICT governance is complete before any AI asset goes live in production. All required fields, discovery configurations, and CMDB relationships should be validated at this gate.

• Verify all required AICT governance fields are complete: risk classification, compliance mapping, and data sensitivity

• Confirm automated discovery sources are configured and returning expected results

• Finalize deployment details: endpoints, monitoring configuration, and value metrics

• Validate CMDB relationships are accurate and CSDM mappings reflect actual runtime behavior

## Process Flow Summary

| **Stage** | **CSDM Domain** | **Key Actions** | **AICT Artifacts** |
| --- | --- | --- | --- |
| Ideation | Ideation & Strategy | AI demand captured in SPM | SPM demand record created |
| ARB (Gate 1) | Design & Planning | Business application registered. AI system and models created. Dependencies documented in EA. | CMDB CIs created. AICT intake initiated. |
| Build & Test | Build & Integration | Development, testing, risk assessment, and compliance review. | AICT lifecycle: Assess, Build & Test stages. |
| Release (Gate 2) | Service Delivery | Final governance fields validated. Discovery confirmed. Deployment approved. | AICT records finalized. Discovery sources confirmed. |
| Production | Service Delivery | Live. Monitoring, performance measurement, and value tracking active. | Deploy stage. Value metrics active. |

## Critical Prerequisites

The following conditions must be in place for AICT and CMDB integration to function effectively. Missing prerequisites typically result in duplicate CIs, ungoverned assets, or incomplete relationship maps.

| **Prerequisite** | **Why It Matters** |
| --- | --- |
| CMDB health: identification rules, reconciliation, and data quality processes are active | Without healthy identification rules, discovery creates duplicates. Reconciliation ensures authoritative source wins. |
| CSDM adoption: business applications and services are defined | AI assets must relate upward to business applications and services. Undefined CSDM structure leaves AI CIs as orphans. |
| Hyperscaler credentials configured | Cloud infrastructure teams must establish platform connections before connector-based discovery can run. |
| AI CoE roles assigned | AI Stewards, Product Owners, and Risk/Compliance personas require AICT roles and clear responsibility assignments before governance workflows can execute. |
| ARB process updated to include AI | Architecture Review Board must capture AI initiatives at the planning stage. Retrofitting AICT after deployment produces incomplete records. |
| IRE identification rules extended | Rules must cover the new AI CI classes (cmdb_ci_ai_system, cmdb_ci_ai_model, cmdb_ci_ai_digital_asset) to prevent duplicates during discovery. |
| Release gate includes AICT validation | Digital Product Release process must validate AICT governance completeness before approving go-live. |

### Emerging Considerations

The following topics are active areas of evolution. Implementation teams should monitor these and incorporate into governance processes as practices mature.

## Agent Identity and Chain of Custody

Agents can task other agents and spin up new agents on demand, crossing organizational and supplier boundaries. Unlike individual agent inventory, the dependency chain between agents is the primary governance concern. No global identification standard for AI agents currently exists (analogous to an ISBN for books). ServiceNow’s acquisition of Veza (closed March 2026) adds identity intelligence across human, machine, and AI identities, which may address part of this gap.

## Agent Platform Maturity

Many third-party agent platforms are not yet enterprise-ready. They cannot easily accommodate discovery or support migrating agents through an SDLC process with corporate gate provisions. Expect manual-intensive processes for these platforms until they mature.

## MCP Discovery and Governance

MCP is a gateway and integration technology, not a new category of AI asset. Its governance should be aligned with existing API management practices. Organizations implementing MCP-based multi-agent orchestration should engage the API Insights team to define discovery scope, data model alignment, and authoritative source rules.

## Blending Discovery Sources

AICT discovery connectors and ITOM/Service Graph connectors serve different purposes and may both return data about the same infrastructure. When both are active, define which source is authoritative for each attribute class to prevent reconciliation conflicts and data quality degradation.

## Regulatory Gaps

ISO 42001 (2023) provides useful governance guidance but was written before the current pace of AI development and cannot be implemented through automation as written. Supplement OOTB EU AI Act and NIST AI RMF content with organization-specific controls. Treat regulatory frameworks as guidance baselines, not complete implementations.

## AI-Specific Security Testing

AI-specific threat vectors—including prompt injection, data leakage, and model poisoning—require integration into existing SecOps and vulnerability management processes. Evidence of security testing should be attached to AI system records in AICT and included in release gate validation.

#### Reference Resources

| **Resource** | **Link** |
| --- | --- |
| AICT Product Docs (Zurich) | docs.servicenow.com/r/_yCRwrQYX6H0b46tCsDNZA/ozwAYVStOQg78g8iEY6Nsw |
| AI Inventory Documentation | docs.servicenow.com/r/intelligent-experiences/ai-control-tower/ai-inventory.html |
| AICT Workspace / Dashboard | docs.servicenow.com/bundle/zurich-intelligent-experiences/page/administer/ai-governance- workspace/concept/ai-governance.html |

# Frequently Asked Questions (FAQ)

## Govern - Risk and Control

### How Authority Documents, Citations, Control Objectives, Risk Statements, and Individual Risks Connect

This explains the full chain - from the regulatory framework sitting at the top, all the way down to the individual risk record that gets scored for residual risk at the bottom.

AUTHORITY DOCUMENT

(EU AI Act, NIST AI RMF, ISO Standards)

↓

CITATIONS

(EU AI Act Article 14, NIST AI RMF GOVERN 1.1)

↓

CONTROL OBJECTIVES RISK STATEMENTS

(What you must DO) ←→ (What could go WRONG)

↓ ↓

└──────────── Both mapped to AI System via Impact Assessment ──┘

↓

INDIVIDUAL RISK RECORDS

(one per risk statement per AI System)

↓

RISK ASSESSMENT

(inherent × control effectiveness

= residual risk per record)

Every governance requirement traces back through the same chain. Understanding this chain helps explain why configuration happens in a specific order and why each component depends on the ones above it.

| **Level** | **Component** | **What It Is** | **Created By** |
| --- | --- | --- | --- |
| 1 | Authority Document | The regulatory framework or internal standard | Platform Admin loads via content pack or manual creation |
| 2 | Citation | A specific article, section, or clause within the authority document | Loaded automatically with content pack or manually created |
| 3 | Control Objective | The actionable thing your organization must DO to comply with a citation | Platform Admin uploads from your AI Standards. Mapped to citations. |
| 3 | Risk Statement | A description of what could go WRONG — your risk library | Platform Admin uploads from your risk register. Also mapped to citations. |
| 4 | Individual Risk Record | The instance of a risk statement mapped to one specific AI System | Created automatically when an Impact Assessment answer triggers a risk statement |
| 5 | Residual Risk Score | How much risk remains after controls are attested | Calculated automatically: Inherent Risk × Control Effectiveness |

### Are the AI Impact Assessment and Risk Classification connected?

The impact assessment enables the risk classification, but they are two separate questionnaires, they are two separate items. The risk classification is just coming from those Risk factors (either OOB or your own). You can review the impact assessment that has been filled out to inform that risk classification. But it is a subjective measurement.
- Impact Assessment answers do NOT automatically feed into the Risk Classification score
- The AI Risk & Compliance Manager or Business Owner can read Impact Assessment answers as context but manually selects each factor score
- A system can trigger many unfavorable Impact Assessment answers and still score Medium in Risk Classification based on the risk scoring methodology applied

In summary: There are two different results.
- One from the impact assessment — how many control objectives were compliant versus not.
- And the second from the risk classification — low, medium, high risk based upon risk factors.

> **[Figure 159 — p.238]** AI asset record 'ServiceNow AI Based Credit Scoring for Loan Approvals 1.0' in the AI Risk and Compliance Workspace, AI assessments related list showing AIA0001003 (2 - High, Closed complete) with its related AI impact assessment.

> **[Figure 160 — p.238]** AI impact assessment for the credit-scoring asset, Outcomes tab, 'Preview outcomes' > Control objectives listing four generated objectives (Prioritise Measurement Efforts, Document Test Sets, Conduct Safety Evaluation, Develop New Metrics) with Description, Classification (Preventive / Detective), Active and Compliance score.

> **[Figure 161 — p.239]** AI impact assessment for the credit-scoring asset, 'Privacy and Data Protection' section, showing the personal-data question answered Yes with the Details panel (scope, AI asset task, related entity).

> **[Figure 162 — p.239]** AI asset record for the credit-scoring asset with the 'Regulatory risk assessments' related list showing RASMT0010006A (Risk classification for AI system) with Risk, Applies to record, Inherent risk 'High (Score: 9)' and Control effectiveness columns.

> **[Figure 163 — p.239]** Risk assessment summary view for 'Related Entity: ServiceNow AI Based Credit Scoring for Loan Approvals 1.0' — Assessment summary tab with a 'Risk rating trend by Regulatory risk classification' chart, a Section/Rating/Comments table, and a generated risk assessment summary noting that the AI system requires careful oversight due to its High-risk classification under regulatory frameworks.

### Does the Risk Assessment connect to the Impact Assessment?

Yes - indirectly, through risk statements:
- Impact Assessment answers trigger risk statements → individual risk records created
- Risk Classification scores the AI System overall for inherent risk tier (separate process)
- Control Attestations → control effectiveness score
- Risk Assessment = individual risk inherent score x control effectiveness → residual risk

The impact assessment helps feed your risk statements, so you can conduct individual risk assessments on those identified risks.

### How Do Risk Statements Connect to the Risk Assessment?

Those risk statements are then used when you get to a point where you are conducting a risk assessment on the asset.
- Impact Assessment answers trigger risk statements to be attached to the AI System based on Automation Rules configured
- Each risk statement belonging to an AI System creates an individual risk record — a one-to-one mapping between the risk statement and that specific AI system
- Those individual risk records are what the Risk Assessment scores for inherent/ residual risk

### Why does the Business Owner fill out the Risk Classification?

Risk Classification is typically completed by the AI COE or AI Risk & Compliance team using the impact assessment answers as context. However, organizations are increasingly asking the Business Owner to fill it out directly since they have the most context about their system. Either approach is valid — the key is that whoever scores the factors has sufficient knowledge of the system to score accurately.

Risk Statements vs Risk Factors — what is the difference?

|  | **Risk Statement** | **Risk Factor** |
| --- | --- | --- |
| What it is | A description of a risk — e.g. 'AI systems may be targeted for cyber attacks' | A scoring dimension — e.g. Level of Autonomy, Data Sensitivity |
| Where used | Impact Assessment — attached when IA answer triggers it | Risk Classification — scored for each AI System |
| Output | Individual risk record. Feeds Risk Assessment (residual risk). | Component of inherent risk tier. Feeds Risk Classification score. |

### Why can't we combine Impact Assessment and Risk Classification?

It uses two different back-end functions. They are completely separate technologies. At a product functional level, they are separate items.

### Why Intake and Impact Assessment Are Separate?

The most common question from Business Owners is: why do I have to fill out two forms? Here is the plain language answer:
- The Intake Form uses a Service Catalog engine that accepts any field type — text, dropdowns, dates, file attachments. Its job is to create the record and start the process. It cannot trigger governance automation.
- The Impact Assessment uses the Smart Assessment Engine which can only work with structured answer choices (Yes/No or multi-choice dropdowns). Free text answers cannot trigger control objectives. The trade-off is that while it is more restrictive in format, it is vastly more powerful in what it can automate.
- If you put all the governance questions in the Intake Form, none of the automation would work — you would just have a form with answers that sit there and do nothing. The governance value comes from the Impact Assessment's ability to fire if-then rules and automatically attach the right controls and risks.

This is why some questions appear to be duplicated between the forms — they are not exact duplicates. The intake version is for tracking and context. The impact assessment version is for automation. They serve different masters.

The Core Technical Reason: The ServiceNow platform uses completely different back-end engines for each component. This is not a configuration choice — it is a fundamental platform architecture decision:

| **Component** | **Engine Used** | **What This Means** |
| --- | --- | --- |
| Intake Form | Service Catalog (Record Producer) | A standard form that creates a database record. Flexible, allows free text, dropdowns, multi-select. Cannot trigger governance automation. |
| Impact Assessment | Smart Assessment Engine | An if-then logic engine. Each answer fires automation rules that attach control objectives and risk statements. Cannot generate a numerical risk score. |
| Risk Classification | Risk Assessment Methodology (RAM) Engine | A structured scoring engine. Takes factor scores and calculates an inherent risk tier. Cannot read answers from the Smart Assessment Engine. |
| Risk Assessment (Residual) | RAM Engine (different workflow) – Can reuse the same RAM or a new RAM | Same RAM engine as Risk Classification but runs on individual risk records (not the AI System object). Combines inherent score with control effectiveness. |

### Why Impact Assessment and Risk Classification Are Not Connected?

A system can trigger many unfavorable answers in the Impact Assessment and still score Medium in Risk Classification. Here is why this is intentional and not a flaw:

| **Impact Assessment** | **Risk Classification** |
| --- | --- |
| Answers the question: WHAT controls and risks apply? | Answers the question: HOW RISKY is this system overall? |
| Questions driven by authority documents (ISO, EU AI Act, NIST) — what does the regulation require? | Questions driven by your organization's risk factors — how does your organization assess AI risk? |
| Many controls can apply to a low-risk system — e.g. a low-risk internal tool may still need privacy controls if it touches any personal data | The risk tier is the overall judgment of severity — a system can have many applicable controls but still be low risk because the severity factors are all low |
| Output: list of controls and risks to manage | Output: one inherent risk score — Low / Medium / High / Unacceptable |

In summary - Your impact assessment should be any question that will help you identify what controls might be in scope or what risks might be in scope for this system that you are going to want to then assess later on. Your risk classification is going to be more of — what questions help us determine an inherent risk of the system? So there they serve two different purposes.

The important implication here is that the risk factors your organization has defined must themselves be comprehensive enough to correctly classify high-risk systems. If a system is genuinely high risk, the 6 or 8 or custom factors should capture that through questions like Level of Autonomy, Decision Impact Type, and Business Impact — not through the Impact Assessment answers.

We just want to make sure from a legal standpoint that we are properly classifying something that is high risk, that should be high risk. And ideally there should be linkage between all three.

The risk factors are your organization's own — if there are gaps in those factors, the risk tier may not accurately reflect reality. Customers need to validate and verify if the factors are comprehensive before go live.

### How Risk Assessment (Residual Risk) Connects — But Indirectly?

The Risk Assessment for residual risk is the one place where the Impact Assessment does feed into a downstream calculation — but indirectly, through risk statements:

### What the Impact Assessment Looks Like Out of the Box

The OOB Impact Assessment in ServiceNow AICT comes with 7 pre-built sections containing 22 smart questions. These are oriented toward fundamental rights and EU AI Act compliance themes. Your organization will extend these sections with additional questions and add new sections based on their governance requirements.

| **Section Name** | **OOB Questions** | **What It Covers** |
| --- | --- | --- |
| Privacy and Data Protection | 6 | Personal data use, sensitive data processing, consent, data minimization, transparency about data collection, individual access rights |
| Non-Discrimination and Fairness | 5 | Bias testing, discrimination against protected characteristics, high-impact decisions affecting rights, human intervention for unfair decisions |
| Transparency and Accountability | 3 | Explainability of decisions, information to users about how decisions are made, appeal mechanism for contested decisions |
| Human Oversight and Control | 2 | Human operator override capability, guidelines for human intervention in AI decision-making |
| Freedom of Expression and Information | 2 | Free flow of information, prevention of undue censorship or viewpoint restriction |
| Impact Monitoring and Mitigation | 2 | Post-deployment monitoring of AI impact on fundamental rights, measures to address negative impacts |
| Right to Remain Anonymous and Consent | 2 | User anonymity options, use of services without revealing PII where possible |
| TOTAL OOB | 22 | All 22 questions are Yes/No or multi-choice dropdowns. All 22 are pre- configured to trigger control objectives and risk statements. |

> [!important] Important
> The OOB sections are primarily oriented toward fundamental rights and EU AI Act compliance. They do not cover all of your organization's governance requirements. Your organization will need to add questions to existing sections and create new sections for areas like data quality, model transparency, tech stack governance, deployment geography, system failure impact, and vulnerable groups.

### What Your Organization Will Add

Based on your configuration design work, your organization may extend the OOB 7 sections and add new sections. Additions like the following coded in green might be included.

| **Section** | **Status** | **Why Needed** |
| --- | --- | --- |
| Privacy and Data Protection | OOB — extend | Add organization-specific data type questions and synthetic vs production data question |
| Human Oversight and Control | OOB — extend | Add level of autonomy multi-choice question and standalone vs integrated question |
| Transparency and Accountability | OOB — extend | Add model as-is vs fine-tuned question and original intended use question |
| Non-Discrimination and Fairness | OOB — extend | Add scope of who uses the AI system as multi-choice |
| NEW: Data Quality and Provenance | New section | Data quality level, lineage visibility, DPIA requirement, bias evaluation of dataset |
| NEW: Model Transparency and Robustness | New section | Model type, customization approach, bias in outputs, PII generation check, data drift process |
| NEW: Tech Stack and Platform | New section | Model ownership type, third-party data reliance type |
| NEW: Deployment Geography | New section | Geographic regions deployed — triggers EU AI Act compliance controls |
| NEW: System Failure and Misuse | New section | Business impact if AI fails (multi-choice), misuse scenarios documented, safeguards in place |
| NEW: Interested Parties and Vulnerable Groups | New section | External parties affected, vulnerable groups impacted, internal teams identified |

### An Important Clarification — Risk Statements vs Risk Factors vs Risk Register

This section clarifies each one and records the key decisions made.

|  | **Risk Statement** | **Risk Factor** |
| --- | --- | --- |
| What it is | A pre-configured description of a potential risk — e.g. 'AI systems may be targeted for cyber attacks' | One of your organization's scoring dimensions used to calculate inherent risk — e.g. Level of Autonomy |
| Where used | Impact Assessment — attached to AI Systems when IA answers trigger them | Risk Classification — scored by Business Owner for each AI System |

The risk statements your organization needs to author should be:
- General enough to apply to multiple AI systems — not specific to one use case
- Aligned with authority document citations — your internal AI standards, EU AI Act, NIST AI RMF
- Descriptive of a potential harm or failure mode — e.g. 'AI systems processing personal data may expose individuals to privacy violations if data minimization controls are not in place'
- Risk register – is what gets generated after residual risk is calculated with what risks remain.

### Putting It All Together — The Full Flow

Now that each component is defined and the disconnects are explained, here is the complete end-to-end flow with all five components in sequence:

| **# Step** | **Engine** | **Who** | **What Happens / Output** |
| --- | --- | --- | --- |
| 1 Intake Form | Service Catalog | Business Owner submits | AI System record created in Draft. AI COE notified. No automation fired yet. |
| 2 Impact Assessment | Smart Assessment Engine | Business Owner answers after AI Steward clicks Start Review | If-then rules fire. Control objectives attached. Risk statements attached. Individual risk records created. Control attestation tasks generated. NOTE: No risk score produced. |
| 3 Risk Classification | RAM Engine | Business Owner scores 18 factors | Scripted calculator runs. Inherent risk tier applied to AI System: Low / Medium / High / Unacceptable. NOTE: Not influenced by IA answers. |
| 4 Control Attestations | Task engine | Business Owner attests to each control | Control Effectiveness % calculated: Effective / Needs Improvement / Ineffective. |
| 5 Risk Assessment | RAM Engine (different workflow) | System calculates automatically | Residual Risk = Inherent Risk x Control Effectiveness. Per individual risk record. Rolls up to AI System. Output: Critical / High / Medium / Low. |

### Classic Attestation vs Smart Attestation

ServiceNow supports two attestation approaches. This is an important configuration decision for the Build and Test phase task story.

|  | **Classic Attestation (Platform Assessment Engine)** | **Smart Attestation (Smart Assessment Engine)** |
| --- | --- | --- |
| Record prefix | AINST | ASMT |
| Link visibility | Records appear only after assessment completion | Attestation link visible before and after completion |
| Advanced features | Standard assessment engine Group | Auto-save, reassignment triggers, question-level instructions, domain separation Combine |
| Recommendation | Legacy approach | Recommended for all new implementations |

NOTE: For Use Smart Attestation (SAE). This is consistent with the Impact Assessment which also uses the Smart Assessment Engine, and gives Business Owners access.

### How Residual Risk scoring is calculated?

ServiceNow supports three methods for calculating residual risk. The Matrix Method is the most common approach and is recommended for new implementations.

| **Method** | **How It Works** | **Your Organization's Usage** |
| --- | --- | --- |
| 1. Matrix Method | Combines Inherent Risk (X-axis) with Control Effectiveness (Y-axis) in a predefined matrix to output residual risk rating. | Most common method. High Inherent + Ineffective or Needs Improvement = Critical. High Inherent + Effective = Low. |
| 2. Arithmetic (Subtract or Divide) | Subtract: Inherent minus Control Effectiveness. Divide: Inherent divided by Control Effectiveness. | Not typically used for new implementations. |
| 3. Factor Response Method | Residual scored independently via its own factor responses. Not dependent on inherent and control assessments. | Not used in Release 1. Most flexible for complex risk scenarios. |

### How is Control Effectiveness Scoring calculated?

How the Control Effectiveness percentage is calculated from attestation results. Feeds directly into the Residual Risk matrix.

| **Score Range** | **Rating** | **What It Means** |
| --- | --- | --- |
| 100% | Effective | All control attestations passed |
| 60% to 99% | Needs Improvement | Most attestations passed but some have gaps |
| Below 60% | Ineffective | Majority of attestations failed or not completed |

> [!note] Note
> If a Business Owner does not complete a control attestation task, that control counts as not attested and reduces the effectiveness score below threshold. This is why overdue attestation escalation (the overdue escalation story) is directly tied to residual risk accuracy.

## Value

### How are the core value metrics calculated?

AICT calculates value using three primary metrics:
- Usage Represents the number of AI invocations within a defined daily window. Derived from event records in the `sys_generative_ai_usage_log` table (or equivalent).
- Time Saved
- Estimates the reduction in manual effort per invocation.
- This can be configured as:
- A fixed value (e.g., 15 minutes), or
- A Performance Analytics (PA) indicator
- Acceptance Rate Measures the proportion of AI-generated outputs accepted by users. Calculated as: *(Accepted AI outputs ÷ Total AI outputs) × 100* Can be defined as a constant or a PA indicator

### How does Performance Analytics (PA) indicator breakdown work?

PA indicators may be shared across multiple AI assets. To ensure accurate value calculations:
- Indicators must include a breakdown by asset
- This enables the value calculation engine to retrieve asset-specific scores

Important: If an indicator is used without a breakdown:
- The system retrieves aggregated data
- In this case, the indicator must be scoped to a single asset to avoid inaccurate calculations

### How are third-party (external) AI agents handled?

Third-party agents are:
- Registered within the AI Inventory
- Tracked using the `sn_ai_disc_ai_usage` table

Current capability:
- Only usage (invocation count) is captured for external agents

Default value calculation:

`EnterpriseAgents.InvocationCount.DailyLink × 15 mins × 50%`
- 15 minutes = default time saved per invocation
- 50% = default acceptance rate

These are out-of-box assumptions and can be overridden using custom Value Templates

### No data is visible in Value dashboards on a new or cloned instance. What should I do?

This behavior is expected when required data dependencies have not yet been established.

System Behavior:
- AICT installs a scheduled script:
- AIValue Generate Historical Data
- This job runs hourly and performs the following:
1. Verifies that required PA indicators have executed
2. If not, triggers the OOB Value indicator jobs
3. On the next execution (after indicators complete), generates 30 days of historical data
4. Automatically deactivates after completion

For demo environments:
- Install and run the Demo Data application prior to AICT Value setup
- Follow: KB2552362 for demo data generation

### What jobs are required to make data visible after cloning?

To ensure Value dashboards populate correctly:
- Run all OOB Performance Analytics indicators at least once
- If data is still not visible:
- Manually trigger:
- `aivalue.valuedashboard.HistoricalJob`
- Verify that the following scheduled script is active:
- AIValue Generate Historical Data
