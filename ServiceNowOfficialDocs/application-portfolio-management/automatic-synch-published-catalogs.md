---
title: Automatic synchronization of published TRM catalogs
description: After you publish a TRM catalog, most updates to TRM data are synchronized automatically with the published knowledge base content.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-portfolio-management/automatic-synch-published-catalogs.html
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Working with the publishing center, Managing Enterprise Architecture Workspace, Enterprise Architecture Workspace, Enterprise Architecture]
tags:
  - application-portfolio-management
  - apm
  - portfolio
  - rationalization
  - lifecycle
  - type-reference
---

# Automatic synchronization of published TRM catalogs

After you publish a TRM catalog, most updates to TRM data are synchronized automatically with the published knowledge base content.

## What updates automatically

The following changes are reflected in the published knowledge base articles without requiring you to republish the catalog:

-   Updates to TRM product fields that are included in the publishing configuration
-   Updates to TRM product lifecycle fields that are included in the publishing configuration
-   Date-driven lifecycle phase transitions, where the TRM phase changes based on configured start and end dates

Automatic synchronization ensures that published TRM catalogs remain up to date as underlying TRM data changes.

## When republishing is required

You must republish the TRM catalog to apply certain structural or global changes to the published knowledge base content.

Republishing is required in the following scenarios:

-   Renaming a TRM phase \(for example, changing Divest to Divesting\)
-   Making structural changes that affect how content is rendered across all articles, such as modifying TRM category names or TRM phase definitions

When republishing is required, the Publishing Center prompts you to republish the catalog so that the changes are applied consistently across all published articles. For instructions on republishing, see [[republish-trm-cat|Republish a TRM catalog after updates]].

**Parent Topic:**[[working-with-publishing-center|Working with the publishing center]]

**Related topics**  


[[config-trm-data-to-publish|Create a configuration to publish TRM data]]

[[view-run-log|View publishing status and run log]]

[[access-the-published-kb|Access the published TRM catalog knowledge base]]

[[understand-publishing-output|Understanding the publishing results and knowledge base output]]

[[eaw-work-with-trm|Working with Technology Reference Model \(TRM\) in EA Workspace]]

## Related

- [[republish-trm-cat|Republish a TRM catalog after updates]]
- [[working-with-publishing-center|Working with the publishing center]]
- [[config-trm-data-to-publish|Create a configuration to publish TRM data]]
- [[view-run-log|View publishing status and run log]]
- [[access-the-published-kb|Access the published TRM catalog knowledge base]]
- [[understand-publishing-output|Understanding the publishing results and knowledge base output]]
- [[eaw-work-with-trm|Working with Technology Reference Model \(TRM\) in EA Workspace]]
