---
title: IoC Repository
description: IoC repository contains STIX objects, each of these objects contain a specific piece of information.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/ioc-repository.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [Threat Intelligence, Enterprise security case management applications, Security Operations]
---

# IoC Repository

IoC repository contains STIX objects, each of these objects contain a specific piece of information.

When you combine STIX objects together through relationships, you allow for easy or complex representations of Cyber Threat Intelligence \(CTI\).

Threat Intelligence supports STIX versions 1.1, 2.0, and 2.1.

-   **[[c_AttackModeMethod|Attack modes and methods]]**  
Attack modes and methods, sometimes referred to as Tactics, Techniques, and Procedures \(TTPs\), are representations of how cyber adversaries behave. They characterize what these adversaries do and how they do it, in increasing levels of detail. Attack modes and methods apply for STIX 1.1.
-   **[[c_IoCs|Indicators of compromise]]**  
Indicators of Compromise \(IoC\) are artifacts observed on a network or operating system that are likely to indicate an intrusion. Typical IoCs are virus signatures and IP addresses, MD5 hashes of malware files or URLs, or domain names. IoC applies for STIX 1.1 and 2.x.
-   **[[c_Observables|Observables]]**  
Observables represent stateful properties \(such as the MD5 hash of a file or the value of a registry key\) or measurable events \(such as the creation of a registry key or the deletion of a file\) that are pertinent to the operation of computers and networks. Observables apply for STIX 1.1 and 2.x.
-   **[[attack-patterns|Attack patterns]]**  
Attack patterns are a type of Tactics, Techniques, and Procedures \(TTPs\) that describe the methods that adversaries attempt to compromise targets. Attack Patterns apply for STIX 2.x.
-   **[[threat-intelligence-campaigns|Campaigns]]**  
A [[campaign|Campaign]] is a grouping of adversarial behaviors. These behaviors describe a set of malicious activities or attacks that occur over time against a specific set of targets. Campaigns apply for STIX 2.x.
-   **[[threat-intelligence-course-actions|Course of actions]]**  
A course of action is an action taken either to prevent an attack or to respond to an attack that is in progress. Course of actions apply for STIX 2.x.
-   **[[threat-intelligence-identities|Identities]]**  
Identities represent actual individuals, organizations, or groups \(ACME, Inc.\) and classes of individuals, systems, or groups \(the finance sector\). Identities apply for STIX 2.x.
-   **[[threat-intelligence-infrastructure|Infrastructure]]**  
The Infrastructure SDO represents a type of Tactics, Techniques, and Procedures \(TTPs\). They describe any systems, software services, and any associated physical or virtual resources intended to support some purpose of an attack. Infrastructure applies for STIX 2.x.
-   **[[threat-intelligence-intrusion-sets|Intrusion set]]**  
An Intrusion Set is a grouped set of adversarial behaviors and resources with common properties. An Intrusion Set usually involves a single organization. Intrusion set applies for STIX 2.x.
-   **[[threat-intelligence-locations|Locations]]**  
A [[location|Location]] represents a geographic location. Locations are primarily used to give context to other SDOs. Locations apply for STIX 2.x.
-   **[[threat-intelligence-malware|Malware]]**  
Malware is a type of TTP that represents malicious code. It refers to a program that is covertly inserted into a system. Malware applies for STIX 2.x.
-   **[[threat-intelligence-malware-analysis|Malware analysis]]**  
Malware Analysis captures the metadata and results of a malware. Malware analysis applies for STIX 2.x.
-   **[[threat-intelligence-observed-data|Observed data]]**  
Observed Data conveys information about cyber security-related entities such as files, systems, and networks using the STIX Cyber-observable Objects \(SCOs\). Observed data applies for STIX 2.x.
-   **[[threat-actors|Threat actors]]**  
Threat Actors are individuals, groups, or organizations who act with malicious intent. Threat actors applies for STIX 2.x.
-   **[[threat-groupings|Threat groupings]]**  
A Threat Groupings object explicitly asserts that the referenced STIX Objects have a shared context. Threat groupings applies for STIX 2.x.
-   **[[marking-definitions|Marking definitions]]**  
The marking definitions object represents a specific marking.
-   **[[threat-intelligence-threat-notes|Threat notes]]**  
A [[threat-note|Threat Note]] conveys informative text to provide additional analysis not contained in the STIX Objects, [[marking-definition|Marking Definition]] objects, or Language Content objects which the Note relates to. Threat notes applies for STIX 2.x.
-   **[[threat-opinions|Threat opinions]]**  
An Opinion is an assessment of the accuracy of the information in a STIX Object produced by a different entity. Threat opinions apply for STIX 2.x.
-   **[[threat-reports|Threat reports]]**  
Threat Reports are collections of threat intelligence focused on one or more topics. Threat reports apply for STIX 2.x.
-   **[[indicator-sightings|Sightings]]**  
Sightings denote that an indicator or object was seen. Objects may be a malware, tool, [[threat-actor|threat actor]], and so on.
-   **[[tools|Tools]]**  
Tools are legitimate software that are used by threat actors to perform attacks. Tools apply for STIX 2.x.
-   **[[vulnerabilities|Vulnerabilities]]**  
A Vulnerability is a weakness or defect in a software or hardware component that attackers exploit. Vulnerabilities apply for STIX 2.x.
-   **[[stix-relationships|Relationships]]**  
Use the relationship objects to link together two SDOs or STIX Cyber-observable Objects \(SCOs\) to describe how they relate to each other.
-   **[[stix-visualizer|STIX Visualizer]]**  
The STIX Visualizer visually represents the structure of the STIX object and its relationship.

**Parent Topic:**[[threat-intel-landing-page|Threat Intelligence]]

**Related topics**  


[Understanding Threat Intelligence]()

[Set up Threat Intelligence]()

[MITRE-ATT&amp;CK framework overview]()

[MITRE D3FEND framework]()

[Threat Intelligence administration]()

[Threat Intelligence integrations]()

[Threat Intelligence Orchestration]()

[Security Case Management]()

## Related

- [[c_AttackModeMethod|Attack modes and methods]]
- [[c_IoCs|Indicators of compromise]]
- [[c_Observables|Observables]]
- [[attack-patterns|Attack patterns]]
- [[threat-intelligence-campaigns|Campaigns]]
- [[threat-intelligence-course-actions|Course of actions]]
- [[threat-intelligence-identities|Identities]]
- [[threat-intelligence-infrastructure|Infrastructure]]
- [[threat-intelligence-intrusion-sets|Intrusion set]]
- [[threat-intelligence-locations|Locations]]
- [[threat-intelligence-malware|Malware]]
- [[threat-intelligence-malware-analysis|Malware analysis]]
- [[threat-intelligence-observed-data|Observed data]]
- [[threat-actors|Threat actors]]
- [[threat-groupings|Threat groupings]]
- [[marking-definitions|Marking definitions]]
- [[threat-intelligence-threat-notes|Threat notes]]
- [[threat-opinions|Threat opinions]]
- [[threat-reports|Threat reports]]
- [[indicator-sightings|Sightings]]
- [[tools|Tools]]
- [[vulnerabilities|Vulnerabilities]]
- [[stix-relationships|Relationships]]
- [[stix-visualizer|STIX Visualizer]]
- [[threat-intel-landing-page|Threat Intelligence]]
- [[campaign|Campaign]]
- [[location|Location]]
- [[threat-note|Threat Note]]
- [[marking-definition|Marking Definition]]
- [[threat-actor|Threat Actor]]
