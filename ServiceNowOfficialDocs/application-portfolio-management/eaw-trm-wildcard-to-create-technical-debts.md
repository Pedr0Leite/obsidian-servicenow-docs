---
title: Work with TRM lifecycle with wildcard
description: You can use Technology Reference Model \(TRM\) lifecycles with wildcards to update multiple TRM software product lifecycles simultaneously without having to specify the exact minor version details of individual TRM software products.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-portfolio-management/eaw-trm-wildcard-to-create-technical-debts.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Manage the Technology Reference Model in Enterprise Architecture Workspace, Exploring Technology Portfolio view, Exploring Enterprise Architecture Workspace, Enterprise Architecture Workspace, Enterprise Architecture]
tags:
  - application-portfolio-management
  - apm
  - portfolio
  - rationalization
  - lifecycle
  - type-concept
---

# Work with TRM lifecycle with wildcard

You can use Technology Reference Model \(TRM\) lifecycles with wildcards to update multiple TRM software product lifecycles simultaneously without having to specify the exact minor version details of individual TRM software products.

A TRM lifecycle with a wildcard is a TRM software product that has lifecycle version that ends with a '\*'. The '\*' means that exact specific version details aren’t provided.

**Note:** To define a version for a specific TRM product, see [[eaw-create-trm-prod-lifecycle-req|Add a TRM product lifecycle]].

## Use of TRM lifecycle with wildcard

The TRM lifecycle with wildcard helps you to automatically identify, categorize, and update TRM software products.

You can also create technical debts in bulk for multiple unapproved TRM software product versions, simultaneously.

Suppose you use Microsoft PowerPoint and have multiple versions like 1.1, 1.2, 1.3 installed for your organization. You create a TRM wildcard with the version ending 1.\*. Now, you update some details of the TRM lifecycle with wildcard. When the **Populate TRM technical debts in the EA Workspace** job runs for the TRM wildcard, the updated data from the TRM lifecycle with wildcard is passed on to versions 1.1, 1.2, 1.3.

## Create a TRM lifecycle with wildcard

A TRM lifecycle with wildcard is created in a similar process as to how you would [[eaw-request-a-trm-product-lifecycle|request a TRM product lifecycle]]. For information on how to add a TRM product lifecycle, see [Add a TRM product lifecycle](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-portfolio-management/eaw-create-trm-prod-lifecycle-req.md).

The only difference is, the TRM wildcard version ends with a ‘\*’.

You must be a part of the enterprise architects group to be able to create a TRM wildcard.

## Limitations of TRM lifecycle with wildcard

A TRM wildcard can’t create technical debts when the full version of a particular TRM software product exists.

**Parent Topic:**[[eaw-managing-the-technology-portfolio|Manage the Technology Reference Model in Enterprise Architecture Workspace]]

**Related topics**  


[[eaw-manage-trm-technical-debt|Manage TRM technical debt]]

[[view-trm-tech-debt|View TRM technical debts]]

[[eaw-trm-technical-debt-calc|TRM Technical Debt calculation in Enterprise Architecture Workspace]]

[[eaw-run-job-trm-tech-debts|Run a scheduled job to update TRM technical debt data in EA Workspace]]

[Add a TRM product lifecycle](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-portfolio-management/eaw-create-trm-prod-lifecycle-req.md)

## Related

- [[eaw-create-trm-prod-lifecycle-req|Add a TRM product lifecycle]]
- [[eaw-managing-the-technology-portfolio|Manage the Technology Reference Model in Enterprise Architecture Workspace]]
- [[eaw-manage-trm-technical-debt|Manage TRM technical debt]]
- [[view-trm-tech-debt|View TRM technical debts]]
- [[eaw-trm-technical-debt-calc|TRM Technical Debt calculation in Enterprise Architecture Workspace]]
- [[eaw-run-job-trm-tech-debts|Run a scheduled job to update TRM technical debt data in EA Workspace]]
- [[eaw-request-a-trm-product-lifecycle|Request a TRM product lifecycle]]
