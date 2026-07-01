---
title: Threat Entities
description: The Threat Entities module provides structured records used to manage threat intelligence objects in the TISC. These records align with STIX domain object concepts and help standardize how threat activity is documented and analyzed.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/threat-intelligence-security-center/tisc-threat-entities.html
release: australia
product: Threat Intelligence Security Center
classification: threat-intelligence-security-center
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [TISC Library Repository, Threat Intelligence Security Center Library, Use, Threat Intelligence Security Center, Security Operations]
---

# Threat Entities

The Threat Entities module provides structured records used to manage [[threat-intel-landing-page|threat intelligence]] objects in the TISC. These records align with STIX domain object concepts and help standardize how threat activity is documented and analyzed.

Use this module to create and manage entities such as:

-   **[[attack-patterns|Attack Patterns]]** to document adversary tactics and techniques.
-   **[[threat-intelligence-campaigns|Campaigns]]** to track coordinated threat activity over time.
-   **[[course-of-action|Courses of Action]]** to define recommended remediation steps.
-   **[[threat-intelligence-identities|Identities]]** to represent individuals, groups, or organizations.
-   **[[threat-intelligence-infrastructure|Infrastructure]]** to record systems and services used in operations.
-   **Intrusion Sets** to group related threat activity.
-   **[[threat-intelligence-malware|Malware]]** and **[[threat-intelligence-malware-analysis|Malware Analysis]]** records for malicious [[tools|tools]] and findings.
-   **[[threat-actors|Threat Actors]]** to represent adversaries.
-   **Threat Events**, **[[threat-reports|Threat Reports]]**, **[[threat-intelligence-threat-notes|Threat Notes]]**, and **[[threat-opinion|Threat Opinion]]** to capture contextual intelligence.
-   **[[marking-definitions|Marking Definitions]]** to apply data handling classifications.

-   **[Attack Patterns](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/tisc-attack-patterns.md)**  
Attack patterns are a type of Tactics, Techniques, and Procedures \(TTPs\) that describe the methods that adversaries attempt to compromise targets.
-   **[Campaign](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/campaign.md)**  
[[campaign|Campaign]] is defined as grouping of adversarial behaviors that describes a set of malicious activities or attacks, sometimes called waves that occur over a period of time against a specific set of targets.
-   **[Courses of Action](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/course-of-action.md)**  
Courses of action is an action taken either to prevent an attack or to respond to an attack that is in progress.
-   **[Identity](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/identity.md)**  
Identities represent actual individuals, organizations or groups, and classes of individuals, systems, or groups. Identities apply for STIX 2.x.
-   **[Infrastructure](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/infrastructure.md)**  
The Infrastructure SDO represents a type of Tactics, Techniques, and Procedures \(TTPs\). They describe any systems, software services, and any associated physical or virtual resources intended to support some purpose of an attack. Infrastructure applies for STIX 2.x.
-   **[Intrusion Set](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/intrusion-set.md)**  
An [[threat-intelligence-intrusion-sets|Intrusion Set]] is a grouped set of adversarial behaviors and resources with common properties. An Intrusion Set usually involves a single organization. Intrusion set applies for STIX 2.x.
-   **[Location](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/location.md)**  
A [[location|Location]] represents a geographic location. [[threat-intelligence-locations|Locations]] are primarily used to give context to other SDOs. Locations apply for STIX 2.x.
-   **[Malware](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/malware.md)**  
Malware is a type of TTP that represents malicious code. It refers to a program that is covertly inserted into a system. Malware applies for STIX 2.x.
-   **[Malware Analysis](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/malware-analysis.md)**  
Malware Analysis captures the metadata and results of a malware. Malware analysis applies for STIX 2.x.
-   **[Marking Definition](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/marking-definition.md)**  
The marking-definition object represents a specific marking. Data markings typically represent handling or sharing requirements for data.
-   **[Object Sighting](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/object-sighting.md)**  
[[indicator-sightings|Sightings]] denote that an object was seen. Objects may be a malware, tool, [[threat-actor|threat actor]], and so on.
-   **[Observed Data](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/tisc-observed-data.md)**  
[[threat-intelligence-observed-data|Observed Data]] conveys information about cyber security-related entities such as files, systems, and networks using the STIX Cyber-observable Objects \(SCOs\). Observed data applies for STIX 2.x.
-   **[Threat Actor](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/threat-actor.md)**  
Threat Actors are individuals, groups, or organizations who act with malicious intent. Threat actors applies for STIX 2.x.
-   **[Threat Event](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/threat-event.md)**  
An event or situation that has the potential for causing undesirable consequences or impact.
-   **[Threat Grouping](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/threat-grouping.md)**  
A [[threat-groupings|Threat Groupings]] object explicitly asserts that the referenced STIX Objects have a shared context. Threat groupings applies for STIX 2.x.
-   **[Threat Note](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/threat-note.md)**  
A [[threat-note|Threat Note]] conveys informative text to provide additional analysis not contained in the STIX Objects, [[marking-definition|Marking Definition]] objects, or Language Content objects which the Note relates to. Threat notes applies for STIX 2.x.
-   **[Threat Opinion](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/threat-opinion.md)**  
An Opinion is an assessment of the accuracy of the information in a STIX Object produced by a different entity. [[threat-opinions|Threat opinions]] apply for STIX 2.x.
-   **[Threat Report](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/threat-report.md)**  
Threat Reports are collections of threat intelligence focused on one or more topics. Threat reports apply for STIX 2.x.
-   **[Tools](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/tool.md)**  
Tools are legitimate software that are used by threat actors to perform attacks. Tools apply for STIX 2.x.

**Parent Topic:**[TISC Library Repository](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/tisc-ioc.md)

**Related topics**  


[Observables]()

[Indicators]()

[Other Objects]()

[Vulnerability Artifacts]()

[View RSS Feeds]()

[Working with Reports in TISC]()

[MITRE-ATT&amp;CK Repository]()

[Relationships Objects]()

[Potential Relationships]()

[Vulnerability relationship mapping]()

[Observables](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/observables.md)

[Indicators](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/indicator.md)

## Related

- [[threat-intel-landing-page|Threat Intelligence]]
- [[attack-patterns|Attack patterns]]
- [[threat-intelligence-campaigns|Campaigns]]
- [[course-of-action|Courses of Action]]
- [[threat-intelligence-identities|Identities]]
- [[threat-intelligence-infrastructure|Infrastructure]]
- [[threat-intelligence-malware|Malware]]
- [[threat-intelligence-malware-analysis|Malware analysis]]
- [[tools|Tools]]
- [[threat-actors|Threat actors]]
- [[threat-reports|Threat reports]]
- [[threat-intelligence-threat-notes|Threat notes]]
- [[threat-opinion|Threat Opinion]]
- [[marking-definitions|Marking definitions]]
- [[campaign|Campaign]]
- [[threat-intelligence-intrusion-sets|Intrusion set]]
- [[location|Location]]
- [[threat-intelligence-locations|Locations]]
- [[indicator-sightings|Sightings]]
- [[threat-actor|Threat Actor]]
- [[threat-intelligence-observed-data|Observed data]]
- [[threat-groupings|Threat groupings]]
- [[threat-note|Threat Note]]
- [[marking-definition|Marking Definition]]
- [[threat-opinions|Threat opinions]]
