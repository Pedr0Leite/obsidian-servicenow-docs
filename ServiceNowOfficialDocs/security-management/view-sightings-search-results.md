---
title: View Sightings Search Results
description: You can review Sightings Search Results for internal and external malicious indicators.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/view-sightings-search-results.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Create sightings search configuration records, Security Operations Integration- Sightings Search capability, Integration capabilities, Security Operations Integration Reference, Security Operations common functionality, Security Operations]
tags:
  - security-management
  - type-task
---

# View Sightings Search Results

You can review [[indicator-sightings|Sightings]] Search Results for internal and external malicious [[indicator|indicators]].

## Before you begin

Role required: sn\_si.analyst

## About this task

.

## Procedure

1.  Navigate to a security incident.

2.  Select the **Sightings Search Results** tab from **Show IoC** Related List group to view the list of sightings searches.

    **Note:** This data can be shared with Trusted Security Circle.

    |Result|Description|
    |------|-----------|
    |Number|Sightings Search identifier.|
    |Observable count|Number of [[c_Observables|observables]] searched for.|
    |Internal Sightings|Aggregated count of internal sightings.|
    |External Sightings|Aggregated count of external sightings. \(Received from threat sharing.\)|
    |Matched configuration items|Aggregated count of configuration items that matched an existing record in your `cmdb`.|
    |Start date range|Time to start looking for sightings.|
    |End date range|Time to stop looking for sightings.|
    |Updated|Date and time of last modification.|

    To view the details of a single search:

3.  Select a Sightings Search reult in the **Sightings Search Results** list.

    The Sightings Search Result form displays.

    |Detail|Description|
    |------|-----------|
    |Number|Internal Sightings Search identifier.|
    |Observable count|Count of observables searched for by this query.|
    |Internal sightings|Count of internal sightings for this search.|
    |External sightings|Count of external sightings for this search. \(Received from Trusted Security Circle.\)|
    |Unmatched hosts|List of potential configuration items for this search that were not matched with any records in your `cmdb`.|
    |Task|Security incident task identifier.|
    |Start date range|Time the sightings search started.|
    |End date range|Time the sightings search stopped.|
    |Updated|Date and time of last modification.|
    |Sightings Search Details|Type, number of sightings and modification date.|
    |Matched Configuration Items|Count of configuration items that matched an existing record in your `cmdb`. Lists the CI and the Sighting.|
    |Threat Shares|List of the threats shared with Trusted Security Circle.|


-   **[[share-sightings-search-results|Share Sightings Search results]]**  
You can share local sightings details or results that are associated with a particular search with your Trusted Security Circle.
-   **[[share-observable|Share observables from a security incident]]**  
Observables can be shared from a security incident in [[sir-landing-page|Security Incident Response]] to members in your trusted circle.

**Parent Topic:**[[sightings-search-configurations|Create sightings search configuration records]]

## Related

- [[share-sightings-search-results|Share Sightings Search results]]
- [[share-observable|Share observables from a security incident]]
- [[sightings-search-configurations|Create sightings search configuration records]]
- [[indicator-sightings|Sightings]]
- [[indicator|Indicators]]
- [[c_Observables|Observables]]
- [[sir-landing-page|Security Incident Response]]
