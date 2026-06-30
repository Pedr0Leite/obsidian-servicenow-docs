---
title: MITRE-ATT&amp;CK framework overview
description: The MITRE-ATT&amp;CK framework is a knowledge base of common tactics, techniques, and procedures \(TTP\) that your organization can access to develop specific threat models and methodologies against cyberattacks.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/about-mitre-attack.html
release: australia
topic_type: concept
last_updated: "2025-07-31"
reading_time_minutes: 5
breadcrumb: [Threat Intelligence, Enterprise security case management applications, Security Operations]
---

# MITRE-ATT&amp;CK framework overview

The MITRE-ATT&amp;CK framework is a knowledge base of common tactics, techniques, and procedures \(TTP\) that your organization can access to develop specific threat models and methodologies against cyberattacks.

The MITRE Adversarial Tactics, Techniques, and Common Knowledge \(ATT&amp;CK\) framework documents and tracks various adversarial techniques that are used during different stages of a cyberattack.

By using the MITRE-ATT&amp;CK framework's knowledge base, the cyberthreat intelligence community can quickly identify threats and coordinate cyberattack responses.

## MITRE-ATT&amp;CK and Security Operations

Learn how the MITRE-ATT&amp;CK information flows with [[security-operations-landing-page|Security Operations]] applications.

-   The [[setup-mitre-profile|pre-loaded TAXII client]] connects to the TAXII server to ingest the [[view-mitre-collection|data collections]] to Threat Intelligence.
-   Existing [[auto-extract-technique-rules|Security Information and Event Manager \(SIEM\) integrations]] ingest their threat data \(alerts and events\), with relevant TTPs and are [[associate-mitre-with-sir|associated with security incidents]].
-   When an [[associate-mitre-observables|IoC is associated to a security incident]], Threat Intelligence automatically searches threat feeds for relevant information and sends IoCs to third-party sources such as EDR, Sandbox, or TIP for additional analysis.
-   If any third-party source contains the MITRE-ATT&amp;CK information, then [[create-detection-rules|Threat Intelligence extracts the technique information]] and enriches the data in the Threat Intelligence repository for correlation and analysis.
-   MITRE-ATT&amp;CK also shares [[mitre-att-ck-heatmap-and-navigator|CVE context information]] for each technique. Your security team can review the exploited techniques in [[vuln-landing-page|Vulnerability Response]] to determine if your business-critical assets are threatened.

## MITRE-ATT&amp;CK matrixes, tactics, and techniques

The core of the MITRE-ATT&amp;CK framework is a matrix of adversary tactics and techniques. The sequence of the tactics represents what an adversary is trying to accomplish at the stage of an incident. When your security team understands this sequence, you have an opportunity to anticipate an adversary's next move and break the kill chain. ATT&amp;CK consists of the following matrixes:

-   Enterprise ATT&amp;CK: Describes the behaviors and actions that an adversary takes to compromise and operate in an enterprise network and cloud.

    **Note:** The Pre ATT&amp;CK matrix has been deprecated by MITRE and is merged with the Enterprise matrix.

-   ICS ATT&amp;CK: Describes the actions that an adversary takes while operating within an Industrial Control Systems \(ICS\) network.
-   Mobile ATT&amp;CK: Describes the adversary behaviors and actions that focus on mobile devices.

Tactics represent the why of an ATT&amp;CK technique. It is the adversary’s tactical objective for performing an action.

Techniques represent how an adversary achieves a tactical objective by performing an action.

Techniques may be associated with more than one tactic. For example, Access Token Manipulation is used by an adversary to achieve either the tactic of Privilege Escalation or Defense Evasion.

## Using an intent-based approach for incident responses

An intent-based response uses a dynamic and contextual kill chain framework that can help your organization to correlate security incidents and to identify a large scope of attacks. Your security team can use an intent-based response to understand how the organization is being attacked and what the attacker might do next. This type of response enables you to predict an attacker's behavior so that you can focus your resources effectively.

Using [[sir-landing-page|Security Incident Response]], your security team can manage the life cycle of each security incident from analysis to containment by focusing on [[c_IoCs|indicators of compromise]] \(IOCs\) like IP addresses, file hashes, and domains.

By integrating Security Incident Response with the MITRE-ATT&amp;CK framework, security incidents are handled as links in a larger enterprise-wide attack.

## How your organization can benefit from MITRE-ATT&amp;CK in Security Operations

Using the MITRE-ATT&amp;CK framework can help your organization do the following:

-   Equip security analysts with MITRE-ATT&amp;CK tactics, techniques, and procedures \(TTPs\) to better analyze and respond to security incidents.
-   Automate the incident workflows using the playbook for detecting and containing threats in the context of the MITRE-ATT&amp;CK framework.
-   Prioritize indicators of compromise and threat hunting with MITRE-ATT&amp;CK information.
-   Understand the high-level security posture of your organization in the context of the MITRE-ATT&amp;CK framework.

-   **[[mitre-att-ck-administration|MITRE-ATT&amp;CK administration]]**  
You can set up, map [[data-sources|data sources]], map overall technique detection coverage, and maintain the [[tisc-mitre-att-ck-framework-overview|MITRE-ATT&amp;CK repository]] in the ServiceNow AI Platform.
-   **[[mitre-att-ck-features|Using MITRE-ATT&amp;CK to detect and analyze threats]]**  
Use the MITRE-ATT&amp;CK framework across the Threat Intelligence and the SIR module to detect and analyze threats to your organization.

**Parent Topic:**[[threat-intel-landing-page|Threat Intelligence]]

**Related topics**  


[Understanding Threat Intelligence]()

[Set up Threat Intelligence]()

[IoC Repository]()

[MITRE D3FEND framework]()

[Threat Intelligence administration]()

[Threat Intelligence integrations]()

[Threat Intelligence Orchestration]()

[Security Case Management]()

## Related

- [[setup-mitre-profile|Set up the MITRE-ATT&amp;CK framework]]
- [[view-mitre-collection|Manage matrices]]
- [[auto-extract-technique-rules|Auto-extract technique rules for importing MITRE-ATT&amp;CK information]]
- [[associate-mitre-with-sir|Associate MITRE-ATT&amp;CK information with security incidents]]
- [[associate-mitre-observables|Associate MITRE-ATT&amp;CK information with observables]]
- [[create-detection-rules|Create and map detection rules]]
- [[mitre-att-ck-heatmap-and-navigator|MITRE-ATT&amp;CK heat map and navigator]]
- [[mitre-att-ck-administration|MITRE-ATT&amp;CK administration]]
- [[mitre-att-ck-features|Using MITRE-ATT&amp;CK to detect and analyze threats]]
- [[threat-intel-landing-page|Threat Intelligence]]
- [[security-operations-landing-page|Security Operations]]
- [[vuln-landing-page|Vulnerability Response]]
- [[sir-landing-page|Security Incident Response]]
- [[c_IoCs|Indicators of compromise]]
- [[data-sources|Data Sources]]
- [[tisc-mitre-att-ck-framework-overview|MITRE-ATT&amp;CK Repository]]
