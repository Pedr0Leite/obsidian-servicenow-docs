---
title: CrowdStrike Next-Gen SIEM integration
description: The CrowdStrike Next-Gen SIEM integration automatically ingests detection data that may indicate potential security incidents and streamlines the creation of security incidents in the ServiceNow Security Incident Response \(SIR\), ensuring timely and effective response.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/security-incident-response/crowdstrike-next-gen-integration-secops.html
release: australia
product: Security Incident Response
classification: security-incident-response
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Security Incident Response integrations, Security Incident Response, Enterprise security case management applications, Security Operations]
tags:
  - security-management
  - sir
  - security-incidents
  - investigation
  - soar
  - type-concept
---

# CrowdStrike Next-Gen SIEM integration

The CrowdStrike Next-Gen SIEM integration automatically ingests detection data that may indicate potential security incidents and streamlines the creation of security incidents in the ServiceNow® [[sir-landing-page|Security Incident Response]] \(SIR\), ensuring timely and effective response.

## Request apps on the Store

Visit the [ServiceNow Store](https://store.servicenow.com/sn_appstore_store.do#!/store/home) website to view all the available apps and for information about submitting requests to the store. For cumulative release notes information for all released apps, see the [ServiceNow Store version history release notes](https://www.servicenow.com/docs/bundle/store-release-notes/page/release-notes/store/sn-store-release-notes.html).

## Overview of CrowdStrike Next-Gen SIEM integration

See the following graphic to learn how CrowdStrike Next-Gen SIEM integrates with the ServiceNow AI Platform [[security-operations-landing-page|Security Operations]] applications.

\[Omitted image "crowdstrike-next-gen-siem.png"\] Alt text: How CrowdStrike Next-Gen SIEM integrates with the ServiceNow AI Platform.

## Key features

Use the key features of this integration to do the following actions:

-   Discover CrowdStrike Next-Gen SIEM detections that are candidates for security incidents and automate the creation of these security incidents.
-   Map CrowdStrike Next-Gen SIEM defect and entity fields to SIR security incident fields.
-   Filter CrowdStrike Next-Gen SIEM defects.
-   Aggregate incidents to existing open security incidents so that you don't have to create duplicate security incidents.
-   Automate CrowdStrike Next-Gen SIEM detection status updates for Security Incident Response so that you can create and [[t_ClosingSecIncidents|close security incidents]].

    **Note:** ServiceNow updates the status of CrowdStrike Next-Gen SIEM detections based on the [[si-creation|security incident creation]] or closure. This update also includes comments of aggregated detections and new detections.

-   Schedule detection ingestion to create security incidents periodically.
-   Synchronize CrowdStrike Next-Gen SIEM detection comments with SIR Work notes.

## Related

- [[sir-landing-page|Security Incident Response]]
- [[security-operations-landing-page|Security Operations]]
- [[t_ClosingSecIncidents|Close security incidents]]
- [[si-creation|Security incident creation]]
