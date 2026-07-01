---
title: Indicators of compromise
description: Indicators of Compromise \(IoC\) are artifacts observed on a network or operating system that are likely to indicate an intrusion. Typical IoCs are virus signatures and IP addresses, MD5 hashes of malware files or URLs, or domain names. IoC applies for STIX 1.1 and 2.x.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/c\_IoCs.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [IoC Repository, Threat Intelligence, Enterprise security case management applications, Security Operations]
tags:
  - security-management
  - type-concept
---

# Indicators of compromise

Indicators of Compromise \(IoC\) are artifacts observed on a network or operating system that are likely to indicate an intrusion. Typical IoCs are virus signatures and IP addresses, MD5 hashes of [[threat-intelligence-malware|malware]] files or URLs, or domain names. IoC applies for STIX 1.1 and 2.x.

An IoC can be a single observable or a collection of [[c_Observables|observables]] \(for example, a single known bad URL or the presence of a specific file and a couple of specific registry key values\).

After IoCs have been identified in a process of incident response and computer forensics, they can be used for early detection of future attack attempts using intrusion detection systems and antivirus software.

IoC applies for STIX 1.1 and 2.x.

-   **[[t_AddIoCs|View an IoC]]**  
IoCs, sometimes referred to as [[indicator|indicators]], are most typically retrieved from a threat data source as STIX data. If needed, you can also create IoCs.
-   **[[t_AddObservToIoC|Add a related observable to an IoC]]**  
In addition to importing observables as STIX data, you can add related observables to an IoC manually.
-   **[[t_AddRelatedAttackModeToIoc|Add a related attack mode/method to an IoC]]**  
In addition to importing related attack modes/methods as STIX data, you can add related attack modes/methods to an IoC manually.
-   **[[t_IdentifyAssociatedIndicatorTypes|Identify associated indicator types]]**  
If an IoC has no associated indicator types defined, it tracks all types of observables. However, if you associate one or more types of indicators to an IoC, it limits the types of observables that can be associated with the IoC.
-   **[[t_IdentifyIndicatorSources|Identify indicator sources]]**  
Indicator sources are normally tracked automatically as part of the threat import process, but more sources can be manually added.
-   **[[t_AddAssociatedTasksToIoC|Add associated tasks to an IoC]]**  
In addition to importing associated tasks \(such as changes and incidents\) as STIX data, you can add them to an IoC manually.

**Parent Topic:**[[ioc-repository|IoC Repository]]

**Related topics**  


[Attack modes and methods]()

[Observables]()

[Attack patterns]()

[Campaigns]()

[Course of actions]()

[Identities]()

[Infrastructure]()

[Intrusion set]()

[Locations]()

[Malware]()

[Malware analysis]()

[Observed data]()

[Threat actors]()

[Threat groupings]()

[Marking definitions]()

[Threat notes]()

[Threat opinions]()

[Threat reports]()

[Sightings]()

[Tools]()

[Vulnerabilities]()

[Relationships]()

[STIX Visualizer]()

## Related

- [[t_AddIoCs|View an IoC]]
- [[t_AddObservToIoC|Add a related observable to an IoC]]
- [[t_AddRelatedAttackModeToIoc|Add a related attack mode/method to an IoC]]
- [[t_IdentifyAssociatedIndicatorTypes|Identify associated indicator types]]
- [[t_IdentifyIndicatorSources|Identify indicator sources]]
- [[t_AddAssociatedTasksToIoC|Add associated tasks to an IoC]]
- [[ioc-repository|IoC Repository]]
- [[threat-intelligence-malware|Malware]]
- [[c_Observables|Observables]]
- [[indicator|Indicators]]
