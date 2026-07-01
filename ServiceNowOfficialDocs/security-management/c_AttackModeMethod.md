---
title: Attack modes and methods
description: Attack modes and methods, sometimes referred to as Tactics, Techniques, and Procedures \(TTPs\), are representations of how cyber adversaries behave. They characterize what these adversaries do and how they do it, in increasing levels of detail. Attack modes and methods apply for STIX 1.1.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/c\_AttackModeMethod.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [IoC Repository, Threat Intelligence, Enterprise security case management applications, Security Operations]
tags:
  - security-management
  - type-concept
---

# Attack modes and methods

Attack modes and methods, sometimes referred to as Tactics, Techniques, and Procedures \(TTPs\), are representations of how cyber adversaries behave. They characterize what these adversaries do and how they do it, in increasing levels of detail. Attack modes and methods apply for STIX 1.1.

For example, an attack mode/method might be to use [[threat-intelligence-malware|malware]] to steal credit card credentials. Or another, related tactic \(at a lower level of detail\) might be to send targeted emails with attachments that contain malicious code, which executes upon opening, captures credit card information from keystrokes, and uses http to communicate with a command and control server to transfer information.

Attack modes and methods apply for STIX 1.1.

-   **[[t_AddAttackModeMethod|Define an attack mode/method]]**  
Attack modes and methods are imported with STIX data, but you can add new modes/methods, as needed.
-   **[[t_AddIoCToAttackMode|Add an IoC to an attack mode/method]]**  
In addition to importing [[indicator|indicators]] as STIX data, you can add IoCs to an attack mode/method manually.
-   **[[t_AddRelatedAttackMode|Add a related attack mode method]]**  
In addition to importing attack modes/methods as STIX data, you can add related attack modes/methods manually.
-   **[[t_AddAssociatedTaskToAttackMode|Add associated task to an attack mode/method]]**  
In addition to importing associated tasks \(such as changes and incidents\) as STIX data, you can add them to an attack mode/method manually.

**Parent Topic:**[[ioc-repository|IoC Repository]]

**Related topics**  


[Indicators of compromise]()

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

- [[t_AddAttackModeMethod|Define an attack mode/method]]
- [[t_AddIoCToAttackMode|Add an IoC to an attack mode/method]]
- [[t_AddRelatedAttackMode|Add a related attack mode method]]
- [[t_AddAssociatedTaskToAttackMode|Add associated task to an attack mode/method]]
- [[ioc-repository|IoC Repository]]
- [[threat-intelligence-malware|Malware]]
- [[indicator|Indicators]]
