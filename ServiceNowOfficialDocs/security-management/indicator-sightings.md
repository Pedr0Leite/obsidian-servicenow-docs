---
title: Sightings
description: Sightings denote that an indicator or object was seen. Objects may be a malware, tool, threat actor, and so on.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/indicator-sightings.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [IoC Repository, Threat Intelligence, Enterprise security case management applications, Security Operations]
tags:
  - security-management
  - type-concept
---

# Sightings

Sightings denote that an indicator or object was seen. Objects may be a [[threat-intelligence-malware|malware]], tool, [[threat-actor|threat actor]], and so on.

Sightings track who and what is the target, how attacks are carried out, and to track trends in attack behavior.

The Sighting relationship object contains extra properties not present in the generic relationship objects. These extra properties represent data specific to sighting [[stix-relationships|relationships]].

For example, a count, or representing how many times something was seen.

Sighting is captured as a relationship because you cannot have a sighting unless you have something that has been sighted.

-   What was sighted, such as the malware, [[campaign|campaign]], or other SDO
-   Who sighted it and/or where it was sighted, represented as an [[identity|identity]]
-   What was seen on systems and networks, represented as [[threat-intelligence-observed-data|observed data]]

-   **[[define-indicator-sightings|Define indicator sightings]]**  
Define sightings that denote that an indicator was seen.
-   **[[define-object-sightings|Define object sightings]]**  
[[define-object-sighting|Define object sighting]] that describes that an object \(malware, tool, threat actor, and so on\) was seen.

**Parent Topic:**[[ioc-repository|IoC Repository]]

**Related topics**  


[Attack modes and methods]()

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

[Tools]()

[Vulnerabilities]()

[Relationships]()

[STIX Visualizer]()

## Related

- [[define-indicator-sightings|Define indicator sightings]]
- [[define-object-sightings|Define object sightings]]
- [[ioc-repository|IoC Repository]]
- [[threat-intelligence-malware|Malware]]
- [[threat-actor|Threat Actor]]
- [[stix-relationships|Relationships]]
- [[campaign|Campaign]]
- [[identity|Identity]]
- [[threat-intelligence-observed-data|Observed data]]
- [[define-object-sighting|Define Object Sighting]]
