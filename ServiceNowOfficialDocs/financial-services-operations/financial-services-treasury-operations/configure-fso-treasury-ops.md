---
title: Configure Financial Services Treasury Operations
description: Review the components that are installed with the Financial Services Treasury Operations application and modify as needed for your organization's business needs.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/financial-services-operations/financial-services-treasury-operations/configure-fso-treasury-ops.html
release: australia
product: Financial Services Treasury Operations
classification: financial-services-treasury-operations
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Treasury Operations, Banking applications, Financial Services Operations \(FSO\)]
tags:
  - financial-services-operations
  - treasury
  - fso
  - finance
  - banking
  - type-task
---

# Configure Financial Services Treasury Operations

Review the components that are installed with the [[fso-treasury-ops-landing-page|Financial Services Treasury Operations]] application and modify as needed for your organization's business needs.

## Before you begin

Make sure that the Financial Services Treasury Operations application is installed. For more information, see [Install Financial Services Treasury Operations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/financial-services-operations/financial-services-treasury-operations/install-fso-treasury-operations.md).

Role required: sn\_bom\_treasury.admin and admin

## Procedure

1.  Import your financial accounts, financial products, financial institutions, and transactions data into ServiceNow tables.

    For more information, see [[import-financial-accounts-products-institutions|Import your financial data using import sets]].

2.  Review the installed components.

    Modify them or add new ones as applicable.

<table id="choicetable_ajc_kk5_z4b"><thead><tr><th align="left" id="d112131e127">

Task

</th><th align="left" id="d112131e130">

Description

</th></tr></thead><tbody><tr><td id="d112131e136">

**Configure service definitions**

</td><td>

[[configure-service-definitions|Configure service definitions]] to enable unique flows and views for treasury service cases and tasks. You can add new case types and configure service definitions for each type.

</td></tr><tr><td id="d112131e158">

**Edit or create flows**

</td><td>

[[configure-flow-designer-flows-fso-apps|Edit or create flows]] using Workflow Studio.

</td></tr><tr><td id="d112131e180">

**Configure playbook**

</td><td>

[[configure-playbooks-fso-apps|Edit or create a new playbook]] using Playbooks.

</td></tr><tr><td id="d112131e202">

**Configure CSM Configurable Workspace**

</td><td>

[[configure-csm-workspace-fso-apps|Configure CSM Configurable Workspace]] to enable agents to interact with customers and create and work on cases.

</td></tr><tr><td id="d112131e230">

**Configure Service Level Agreements \(SLAs\)**

</td><td>

[[configure-sla-definitions-fso-cases|Configure the installed SLAs]] to configure SLA timings for treasury service cases and tasks.

</td></tr><tr><td id="d112131e249">

**Configure user groups**

</td><td>

[[configure-groups-fso|Configure user groups]] for assignment of cases and tasks. You can also assign roles to groups and users.

</td></tr><tr><td id="d112131e268">

**Configure assignment rules**

</td><td>

[[configure-assignment-rules-fso-applications|Configure assignment rules]] to identify cases that meet certain conditions and then route those cases to agents.

</td></tr><tr><td id="d112131e284">

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
- [[configure-assignment-rules-fso-applications|Configure assignment rules]]
- [[configuring-fso-document-processor|Configuring Financial Services Operations Document Processor]]
- [[fso-treasury-ops-landing-page|Financial Services Treasury Operations]]
