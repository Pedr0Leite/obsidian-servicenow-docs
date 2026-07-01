---
title: Observables
description: Observables represent stateful properties \(such as the MD5 hash of a file or the value of a registry key\) or measurable events \(such as the creation of a registry key or the deletion of a file\) that are pertinent to the operation of computers and networks. Observables apply for STIX 1.1 and 2.x.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/c\_Observables.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [IoC Repository, Threat Intelligence, Enterprise security case management applications, Security Operations]
tags:
  - security-management
  - type-concept
---

# Observables

Observables represent stateful properties \(such as the MD5 hash of a file or the value of a registry key\) or measurable events \(such as the creation of a registry key or the deletion of a file\) that are pertinent to the operation of computers and networks. Observables apply for STIX 1.1 and 2.x.

Sets of cyber observables are useful for identifying [[c_IoCs|indicators of compromise]] when they are combined with contextual information that represents the behaviors of cyber threats.

Observables apply for STIX 1.1 and 2.x.

-   **[[t_AddObservable|Define an observable]]**  
Observables are retrieved from the vendor server as STIX data. However, you can create observables, as needed.
-   **[[t_AddIoCToObserv|Add a related IoC to an observable]]**  
In addition to importing observables as STIX data, you can add related observables to an IoC manually.
-   **[[t_AddAssociatedTasksToObservable|Add associated tasks to an observable]]**  
In addition to importing associated tasks \(such as changes and incidents\) as STIX data, you can add them to an observable manually.
-   **[[t_AddRelatedObservable|Add a related observable]]**  
In addition to importing observables as STIX data, you can add related observables manually.
-   **[[t_LoadAdditionalIoCData|Load more IoC data]]**  
Depending on settings in two properties and a script include definition, you can load geolocation information for IP addresses and websites in the Observables form. With further customization, you can also add other information, such as country codes, city names.
-   **[[t_IdentifyObservbleSources|Identify observable sources]]**  
If an observable has no sources defined, it uses all types of sources. However, if you add one or more threat sources to an observable, it limits the sources used.
-   **[[perform-lookups-on-observables|Perform lookups on observables]]**  
You can perform [[threat-intel-landing-page|threat intelligence]] lookups on one or more observables to determine whether they’re associated with known security threats. The scanning implementations that run depend on the ones you’ve activated.
-   **[[perform-enrich-on-observs|Perform threat enrichment on observables]]**  
You can perform threat intelligence enrichment on one or more observables to determine whether they’re associated with known security threats. The implementations that run depend on the ones you’ve activated.

**Parent Topic:**[[ioc-repository|IoC Repository]]

**Related topics**  


[Attack modes and methods]()

[Indicators of compromise]()

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

- [[t_AddObservable|Define an observable]]
- [[t_AddIoCToObserv|Add a related IoC to an observable]]
- [[t_AddAssociatedTasksToObservable|Add associated tasks to an observable]]
- [[t_AddRelatedObservable|Add a related observable]]
- [[t_LoadAdditionalIoCData|Load more IoC data]]
- [[t_IdentifyObservbleSources|Identify observable sources]]
- [[perform-lookups-on-observables|Perform lookups on observables]]
- [[perform-enrich-on-observs|Perform threat enrichment on observables]]
- [[ioc-repository|IoC Repository]]
- [[c_IoCs|Indicators of compromise]]
- [[threat-intel-landing-page|Threat Intelligence]]
