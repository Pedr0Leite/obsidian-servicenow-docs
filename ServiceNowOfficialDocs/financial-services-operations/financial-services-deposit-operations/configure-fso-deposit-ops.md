---
title: Configure Financial Services Deposit Operations
description: Review the components that are installed with the Financial Services Deposit Operations application and modify as needed for your organization's business needs.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/financial-services-operations/financial-services-deposit-operations/configure-fso-deposit-ops.html
release: australia
product: Financial Services Deposit Operations
classification: financial-services-deposit-operations
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Deposit Operations, Banking applications, Financial Services Operations \(FSO\)]
---

# Configure Financial Services Deposit Operations

Review the components that are installed with the [[fso-deposit-ops-landing-page|Financial Services Deposit Operations]] application and modify as needed for your organization's business needs.

## Before you begin

Make sure that the Financial Services Deposit Operations application is installed. For more information, see [Install Financial Services Business Deposit Operations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/financial-services-deposit-operations/install-fso-business-deposit-ops.md) and [Install Financial Services Personal Deposit Operations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/financial-services-deposit-operations/install-fso-personal-deposit-ops.md).

Role required:

-   For [[fso-overview|Financial Services]] Business Deposit Operations: sn\_bom\_deposit\_b2b.admin and admin
-   Financial Services Personal Deposit Operations: sn\_bom\_deposit\_b2c.admin and admin

## Procedure

1.  Import your financial accounts, financial products, financial institutions, and transactions data into ServiceNow tables.

    For more information, see [[import-financial-accounts-products-institutions|Import your financial data using import sets]].

2.  Review the installed components.

    Modify them or add new ones as applicable.

<table id="choicetable_ajc_kk5_z4b"><thead><tr><th align="left" id="d113363e162">

Task

</th><th align="left" id="d113363e165">

Description

</th></tr></thead><tbody><tr><td id="d113363e171">

**Configure service definitions**

</td><td>

[[configure-service-definitions|Configure service definitions]] to enable unique flows and views for deposit service cases and tasks. You can add new case types and configure service definitions for each type.

</td></tr><tr><td id="d113363e193">

**Edit or create flows**

</td><td>

[[configure-flow-designer-flows-fso-apps|Edit or create flows]] using Workflow Studio.

</td></tr><tr><td id="d113363e215">

**Configure playbooks**

</td><td>

[[configure-playbooks-fso-apps|Edit or create a new playbook]] using Playbooks.

</td></tr><tr><td id="d113363e237">

**Configure CSM Configurable Workspace**

</td><td>

[[configure-csm-workspace-fso-apps|Configure CSM Configurable Workspace]] to enable agents to interact with customers and create and work on cases.

</td></tr><tr><td id="d113363e265">

**Configure Service Level Agreements \(SLAs\)**

</td><td>

[[configure-sla-definitions-fso-cases|Configure the installed SLAs]] to configure SLA timings for deposit service cases and tasks.

</td></tr><tr><td id="d113363e284">

**Configure user groups**

</td><td>

[[configure-groups-fso|Configure user groups]] for assignment of cases and tasks. You can also assign roles to groups and users.Configure agent connector and contributor roles for the groups, if required. For more information, see [[fso-combine-csm-industry-roles|Roles and Personas]].

</td></tr><tr><td id="d113363e321">

**Configure assignment rules**

</td><td>

[[configure-assignment-rules-fso-applications|Configure assignment rules]] to identify cases that meet certain conditions and then route those cases to agents.

</td></tr><tr><td id="d113363e337">

**Configure Document Processor**

</td><td>

[[configuring-fso-document-processor|Configure Document Processor]] for document categories, document types, inbound and outbound document rules, and approval rules for document deferments and exceptions.

</td></tr></tbody>
</table>

## Related

- [[import-financial-accounts-products-institutions|Import your financial data using import sets]]
- [[configure-service-definitions|Configure service definitions]]
- [[configure-flow-designer-flows-fso-apps|Configure flows]]
- [[configure-playbooks-fso-apps|Configure playbooks]]
- [[configure-csm-workspace-fso-apps|Configure CSM Configurable Workspace]]
- [[configure-sla-definitions-fso-cases|Configure SLA definitions]]
- [[configure-groups-fso|Configure groups]]
- [[fso-combine-csm-industry-roles|Using agent connector and contributor roles in Financial Services Operations]]
- [[configure-assignment-rules-fso-applications|Configure assignment rules]]
- [[configuring-fso-document-processor|Configuring Financial Services Operations Document Processor]]
- [[fso-deposit-ops-landing-page|Financial Services Deposit Operations]]
- [[fso-overview|Financial Services]]
