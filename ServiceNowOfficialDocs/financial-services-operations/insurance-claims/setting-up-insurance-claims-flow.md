---
title: Setting up Insurance claims
description: Plan and configure your implementation of the Insurance claims application by following the tasks in the configuration overview.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/financial-services-operations/insurance-claims/setting-up-insurance-claims-flow.html
release: australia
product: Insurance Claims
classification: insurance-claims
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 6
breadcrumb: [Insurance claims, Exploring insurance claims applications, Insurance applications, Financial Services Operations \(FSO\)]
tags:
  - financial-services-operations
  - insurance
  - claims
  - fso
  - processing
  - type-concept
---

# Setting up Insurance claims

Plan and configure your implementation of the [[insurance-claims-flow|Insurance claims]] application by following the tasks in the configuration overview.

## Prerequisites

Before beginning the configuration steps, you should familiarize yourself with the following topics:

-   [[financial-services-operations-core-data-model|Financial Services Operations Core]]
-   [[insurance-claims-core-data-model|Insurance Claims Core]]
-   [[integrating-with-document-processor|Integrating with Document Processor]]
-   [Best practices for setting up an instance](https://www.servicenow.com/community/in-other-news/best-practices-for-general-planning-and-setup-of-your-instance/ba-p/2287790)
-   [Table extension and classes](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/table-extension-and-classes.md)

## Configuration overview

The following table lists how to set up the components and relationships for an Insurance claims workflow.

<table id="table_zkg_yrm_zcc"><thead><tr><th>

Task

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Install the Insurance claims application

</td><td>

Install the Insurance claims application \(sn\_ins\_gen\_claim\) from the ServiceNow Store. For more information, see [Install Insurance claims](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/insurance-claims/install-insurance-claims-flow.md).

</td></tr><tr><td>

Set up customer data

</td><td>

Migrate the data for your personal and commercial customers on your instance. For more information, see [Setting up the customer data for Insurance claims](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/insurance-claims/data-setup-for-insurance-claims.md).

</td></tr><tr><td>

Set up policy data

</td><td>

Review the policy data options in this topic \(importing data or remote tables\). For more information, see [Setting up the policy data for Insurance claims](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/insurance-claims/set-up-policy-data-for-insurance-claims.md).You can also follow these topics to set up [[insurance-product-models|insurance product models]] and coverages, and to create insurance policies:

-   [Establish Insurance Product Models](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/insurance-claims/insurance-product-models.md)
-   [Specify coverages](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/insurance-claims/coverage-specification.md)
-   [Create Insurance Policies](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/insurance-claims/set-up-an-insurance-policy.md)

</td></tr><tr><td>

Review policy snapshots

</td><td>

Review the PolicySnapshotGenerator script include in your instance, which contains the code responsible for copying the relevant insurance policy for the claim. For more information, see [Policy snapshots in Insurance claims](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/insurance-claims/policy-snapshots.md).

</td></tr><tr><td>

Create service definitions

</td><td>

Create the service definitions for each of your claim types. For more information, see [Creating a service definition for Insurance claims](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/insurance-claims/create-service-definitions-for-insurance-claims.md).

</td></tr><tr><td>

[[link-the-insurance-product-model-and-service-definition|Link the insurance product model and claim case service definition]]

</td><td>

Link the insurance product model and service definition so that the system recognizes which policies are relevant to the service definition. For more information, see [Link the insurance product model and claim case service definition](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/insurance-claims/link-the-insurance-product-model-and-service-definition.md).

</td></tr><tr><td>

Set up claim incident tables

</td><td>

Define and configure new incident tables as needed for your workflow. A claim incident is a record of the details for a particular claim. For more information, see [Claim incidents](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/insurance-claims/claim-incidents.md).

</td></tr><tr><td>

Set up Claim Incident Configuration

</td><td>

Set up the claim incident configuration to define the relationships between the [[claim-incidents|claim incidents]], the service definition, how [[adjuster-tasks-workspace-pers|adjuster tasks]] are created, and whether losses can be itemized. For more information, see [Claim Incident Configuration table](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/insurance-claims/claim-incident-configuration-table.md).

</td></tr><tr><td>

Set up Document Processing

</td><td>

Set up FSO Document Processor to define the documentation that you need from customers to process claims. For more information, see [Integrating with Document Processor](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/integrating-with-document-processor.md).

</td></tr><tr><td>

Update service definitions with document requirements

</td><td>

Define the specific documentation that is required for each service. For more information, see [Add a document list definition to a service definition](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/insurance-claims/add-document-list-definition-to-service-definition.md).

</td></tr><tr><td>

Review the reserves and payments approval engine

</td><td>

Go through the rules for the reserve and payment approval process provided in Insurance Claims Core. For more information, see [[approval-engine-for-reserves-and-payments|Approval Engine for Reserves and Payments]].

</td></tr><tr><td>

Review claim automation using decision tables

</td><td>

Learn about the claim automation rules in the decision tables. For more information, see [Use claim automation decision tables](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/insurance-claims/update-insurance-claims-automation-using-decision-tables.md).

</td></tr><tr><td>

Configure assignment rules

</td><td>

Look at the rules that determine how cases and tasks are assigned to personas. For more information, see [[configure-assignment-rules-fso-applications|Configure assignment rules]].

</td></tr><tr><td>

Configure SLA definitions

</td><td>

Configure service level agreement \(SLA\) definitions to match your business needs.The SLA definitions are based on the service definition of case and adjuster tasks. For more information, see [[configure-sla-definitions-fso-cases|Configure SLA definitions]].

</td></tr><tr><td>

Set up Insurance claims workspaces and dashboards

</td><td>

See what's included in Insurance claims and review the guidelines for setting up the dashboards and workspaces for a new line of business. For more information, see [Setting up Insurance claims workspaces and dashboards](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/insurance-claims/insurance-claims-dashboards-and-workspaces.md).

</td></tr><tr><td>

[[insurance-claim-case-archival|Manage the Archive Claim Case rule]]

</td><td>

Manage the archive rule that is provisioned in the Claim Case \[sn\_ins\_gen\_claim\_case\] table. By default, inactive cases that are more than seven years old are automatically archived. For more information, see [Manage the Archive Claim Case rule](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/insurance-claims/insurance-claim-case-archival.md).

</td></tr></tbody>
</table>

## Related

- [[financial-services-operations-core-data-model|Financial Services Operations Core]]
- [[insurance-claims-core-data-model|Insurance Claims Core]]
- [[integrating-with-document-processor|Integrating with Document Processor]]
- [[approval-engine-for-reserves-and-payments|Approval Engine for Reserves and Payments]]
- [[configure-assignment-rules-fso-applications|Configure assignment rules]]
- [[configure-sla-definitions-fso-cases|Configure SLA definitions]]
- [[insurance-claims-flow|Insurance claims]]
- [[insurance-product-models|Insurance product models]]
- [[link-the-insurance-product-model-and-service-definition|Link the insurance product model and claim case service definition]]
- [[claim-incidents|Claim incidents]]
- [[adjuster-tasks-workspace-pers|Adjuster tasks]]
- [[insurance-claim-case-archival|Manage the Archive Claim Case rule]]
