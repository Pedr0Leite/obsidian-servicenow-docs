---
title: MITRE-ATT&amp;CK administration
description: You can set up, map data sources, map overall technique detection coverage, and maintain the MITRE-ATT&amp;CK repository in the ServiceNow AI Platform.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/mitre-att-ck-administration.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [MITRE-ATT&amp;CK framework overview, Threat Intelligence, Enterprise security case management applications, Security Operations]
---

# MITRE-ATT&amp;CK administration

You can set up, map [[data-sources|data sources]], map overall technique detection coverage, and maintain the [[tisc-mitre-att-ck-framework-overview|MITRE-ATT&amp;CK repository]] in the ServiceNow AI Platform.

-   **[[get-started-with-mitre|Get started with MITRE-ATT&amp;CK framework]]**  
Review the following information before you start setting up your MITRE-ATT&amp;CK framework.
-   **[[understand-the-mitre-to-stix-data-model-mapping|Understand the MITRE to STIX data model]]**  
Review the terminology used by MITRE and STIX to efficiently use and understand the MITRE-ATT&amp;CK™ framework in the ServiceNow AI Platform.
-   **[[domain-separation-and-mitre-att-ck|Domain separation and MITRE-ATT&amp;CK]]**  
This domain separation overview pertains to MITRE-ATT&amp;CK. Domain separation allows you to separate data, processes, and administrative tasks into logical groupings called domains. You can then control several aspects of this separation, including which users can see and access data.
-   **[[setup-mitre-profile|Set up the MITRE-ATT&amp;CK framework]]**  
Activate the MITRE-ATT&amp;CK profile, and set up a scheduled job so that you can set up MITRE-ATT&amp;CK collections for threat detection in your organization.
-   **[[view-mitre-collection|Manage matrices]]**  
Manage the matrices that have been imported from the MITRE TAXII collections. Matrices are a collection of tactics and techniques. You can view the matrices to review if your collections are available in the MITRE-ATT&amp;CK repository.
-   **[[view-techniques|Manage techniques]]**  
Manage the techniques that have been imported from the MITRE TAXII collections. The techniques contain various ways attackers have developed to employ a given tactic. You can review and deactivate techniques that are not relevant to your organization. In STIX, techniques are known as [[attack-patterns|attack patterns]].
-   **[[manage-mitigations|Manage mitigations]]**  
Manage the mitigations that have been imported from the MITRE TAXII collections. Mitigations enable you to prevent an adversary from successfully executing techniques or sub-techniques against your organization. In STIX, mitigations are known as [[threat-intelligence-course-actions|course of actions]].
-   **[[manage-groups-threat-intel|Manage groups]]**  
Manage the groups that have been imported from the MITRE TAXII collections. Groups are sets of related intrusion activity that are tracked by a common name in the security community. Analysts track clusters of activities using various terms such as threat groups, activity groups, [[threat-actors|threat actors]], intrusion sets, and [[threat-intelligence-campaigns|campaigns]]. In STIX, groups are known as intrusion sets.
-   **[[manage-malware|Manage malware]]**  
Manage the [[threat-intelligence-malware|malware]] information that you imported from the MITRE TAXII collections. Malware is a type of TTP that represents malicious code. It refers to a program that is covertly inserted into a system. The intent of a malware is to compromise the confidentiality, integrity, or availability of the victim's data, applications, or operating system \(OS\).
-   **[[manage-tools|Manage tools]]**  
Manage the [[tools|tools]] information that you imported from the MITRE TAXII collections. Tools are legitimate software that are used by threat actors to perform attacks.
-   **[[manage-mitre-relationships|Manage MITRE relationships]]**  
Manage the MITRE [[stix-relationships|relationships]] information that you imported from the MITRE TAXII collections.
-   **[[manage-cve-and-technique-mapping|Manage CVE and technique mapping]]**  
Manage the CVE and technique information that is mapped after you import the MITRE TAXII collections.
-   **[[view-and-extend-information|Extend the MITRE-ATT&amp;CK data]]**  
Extend the MITRE-ATT&amp;CK repository data in the ServiceNow AI Platform by enriching it.
-   **[[manage-mitre-att-ck-data-sources|Define the data source and detection tool mapping]]**  
Define the data source and detection tool mapping for MITRE-ATT&amp;CK tactics and techniques. The data source [[mapping-logrhythm|mapping]] provides you with insight into the relevance and availability of the data sources and the detection tools for monitoring the data sources in your environment.
-   **[[map-the-data-source-and-data-components|Define the data source and data component mapping]]**  
Use the [[data-component|Data Component]] Mapping if you are using the latest TAXII collections, and you want to maintain a relationship between the data sources, data components, and the various techniques. Map the data sources with the additional context of data components that provides an extra sublayer of context to data sources that enable you to understand adversary behaviors in MITRE-ATT&amp;CK better.
-   **[[define-technique-coverage|Define the technique detection coverage]]**  
Define the technique detection coverage that your organization must measure and detect specific adversary techniques.
-   **[[map-technique-coverage|Map your technique detection coverage to a technique]]**  
Map your overall technique detection coverage with the technique that enables your organization to detect specific adversary techniques.
-   **[[define-the-mitigation-coverage|Define the mitigation coverage]]**  
Define the mitigation coverage for each mitigation that is associated with a technique so that you gain visibility into how well your organization can prevent the attacks that happen due to a particular technique.
-   **[[map-your-mitigation-coverage-to-a-technique|Map your mitigation coverage to a technique]]**  
Map your mitigation coverage with the technique that enables you to detect your organization's overall mitigation strategy.
-   **[[create-detection-rules|Create and map detection rules]]**  
Create detection rules and map them against the tactics and techniques. With this mapping, you can see the coverage for the detection rules in your organization.
-   **[[auto-extract-technique-rules|Auto-extract technique rules for importing MITRE-ATT&amp;CK information]]**  
Use the base system auto-extraction rules to import the MITRE-ATT&amp;CK information from any existing third-party integrations.
-   **[[review-threat-group-and-techniques-mapping|Review threat group and MITRE-ATT&amp;CK techniques mapping]]**  
Review the threat group and techniques object to object relationship mapping information that is imported from the MITRE TAXII collections. This mapping enables you to view the technique group and the corresponding technique mapping.
-   **[[threat-group-to-technique-heatmap-definition|Threat group to technique heatmap definition]]**  
Define the threat group to technique heatmap definition so that on the heatmap you can measure and detect the attack patterns that threat groups are using to attack your organization. The probability of an attack using a particular technique increases when you have a high number of attackers.
-   **[[configure-mitre-att-ck-properties|Review the MITRE-ATT&amp;CK system properties]]**  
Review the MITRE-ATT&amp;CK system property values.

**Parent Topic:**[[about-mitre-attack|MITRE-ATT&amp;CK framework overview]]

**Related topics**  


[Using MITRE-ATT&amp;CK to detect and analyze threats]()

## Related

- [[get-started-with-mitre|Get started with MITRE-ATT&amp;CK framework]]
- [[understand-the-mitre-to-stix-data-model-mapping|Understand the MITRE to STIX data model]]
- [[domain-separation-and-mitre-att-ck|Domain separation and MITRE-ATT&amp;CK]]
- [[setup-mitre-profile|Set up the MITRE-ATT&amp;CK framework]]
- [[view-mitre-collection|Manage matrices]]
- [[view-techniques|Manage techniques]]
- [[manage-mitigations|Manage mitigations]]
- [[manage-groups-threat-intel|Manage groups]]
- [[manage-malware|Manage malware]]
- [[manage-tools|Manage tools]]
- [[manage-mitre-relationships|Manage MITRE relationships]]
- [[manage-cve-and-technique-mapping|Manage CVE and technique mapping]]
- [[view-and-extend-information|Extend the MITRE-ATT&amp;CK data]]
- [[manage-mitre-att-ck-data-sources|Define the data source and detection tool mapping]]
- [[map-the-data-source-and-data-components|Define the data source and data component mapping]]
- [[define-technique-coverage|Define the technique detection coverage]]
- [[map-technique-coverage|Map your technique detection coverage to a technique]]
- [[define-the-mitigation-coverage|Define the mitigation coverage]]
- [[map-your-mitigation-coverage-to-a-technique|Map your mitigation coverage to a technique]]
- [[create-detection-rules|Create and map detection rules]]
- [[auto-extract-technique-rules|Auto-extract technique rules for importing MITRE-ATT&amp;CK information]]
- [[review-threat-group-and-techniques-mapping|Review threat group and MITRE-ATT&amp;CK techniques mapping]]
- [[threat-group-to-technique-heatmap-definition|Threat group to technique heatmap definition]]
- [[configure-mitre-att-ck-properties|Review the MITRE-ATT&amp;CK system properties]]
- [[about-mitre-attack|MITRE-ATT&amp;CK framework overview]]
- [[data-sources|Data Sources]]
- [[tisc-mitre-att-ck-framework-overview|MITRE-ATT&amp;CK Repository]]
- [[attack-patterns|Attack patterns]]
- [[threat-intelligence-course-actions|Course of actions]]
- [[threat-actors|Threat actors]]
- [[threat-intelligence-campaigns|Campaigns]]
- [[threat-intelligence-malware|Malware]]
- [[tools|Tools]]
- [[stix-relationships|Relationships]]
- [[mapping-logrhythm|Mapping]]
- [[data-component|Data Component]]
